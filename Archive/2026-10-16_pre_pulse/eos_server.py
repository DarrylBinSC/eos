#!/usr/bin/env python3
"""
eos_server.py — local web app over the EOS register item files.

Serves a triage view of Registers/<kind>/<ID>.md on the LAN, writes edits straight back to the
item files, regenerates 03/04/05, and commits each change to git so the next briefing can read
`git log` to see what Darryl changed. Standard library only.

Run from the EOS root (the launcher Tools/eos-server.command does this):
    python3 Tools/eos_server.py            # http://0.0.0.0:8765
Env:
    EOS_PORT      default 8765
    EOS_BIND      default 0.0.0.0 (LAN). Use 127.0.0.1 to restrict to this Mac.
    EOS_PASSWORD  unset = no login (Darryl's choice 2026-10-15). Set it to require HTTP Basic auth.
"""
from __future__ import annotations

import base64
import json
import os
import re
import subprocess
import sys
import threading
import datetime as dt
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

sys.path.insert(0, str(Path(__file__).resolve().parent))
import eos_registers as R  # noqa: E402

PORT = int(os.environ.get("EOS_PORT", "8765"))
BIND = os.environ.get("EOS_BIND", "0.0.0.0")
PASSWORD = os.environ.get("EOS_PASSWORD", "")
LOCK = threading.Lock()

# Fields the browser may change, per kind. Everything else is read-only from the app.
EDITABLE = {
    "action": ["title", "register", "status", "owner", "counterparty", "type", "product", "critical", "critical_reason",
               "due", "due_note", "trigger", "next_action", "basis", "source", "closed_by", "disposition_note", "needs_triage", "tags"],
    "watch": ["title", "tier", "status", "severity", "trend", "evidence_basis", "product", "next_action", "disposition_note", "needs_triage", "tags"],
    "decision": ["title", "tier", "status", "owner", "forum", "forum_date", "next_action", "source", "product", "disposition_note", "needs_triage", "tags"],
}
CLOSED_STATUSES = {"closed", "dropped", "aged_out"}


# ----------------------------------------------------------------------------- git

def git(*args) -> tuple[int, str]:
    try:
        p = subprocess.run(["git", *args], cwd=R.ROOT, capture_output=True, text=True, timeout=30)
        return p.returncode, (p.stdout + p.stderr).strip()
    except Exception as e:  # git missing, etc.
        return 1, str(e)


def git_commit(message: str) -> str:
    if not (R.ROOT / ".git").exists():
        return "no git repo"
    git("add", "-A", "--", "Registers", "03_Decision_Log.md", "04_Executive_Watch_List.md", "05_Commitments.md")
    rc, out = git("commit", "-q", "-m", message)
    return "committed" if rc == 0 else f"nothing to commit / {out[:120]}"


# ----------------------------------------------------------------------------- item ops

def item_json(meta, body, path):
    d = dict(meta)
    d["body"] = body
    d["path"] = str(path.relative_to(R.ROOT))
    return d


def apply_patch(item_id: str, patch: dict, note: str, actor: str) -> dict:
    found = R.find_item(item_id)
    if not found:
        raise KeyError(item_id)
    meta, body, path = found
    kind = meta["kind"]
    changed = []
    for k, v in (patch or {}).items():
        if k not in EDITABLE.get(kind, []):
            continue
        if k in ("critical", "needs_triage"):
            v = bool(v)
        if k == "tags" and isinstance(v, str):
            v = [t.strip() for t in v.split(",") if t.strip()]
        if meta.get(k) != v:
            changed.append(f"{k}: {meta.get(k)!r} -> {v!r}")
            meta[k] = v
    today = R.today()
    # Disposition side effects
    if "status" in (patch or {}):
        st = meta.get("status")
        if st in CLOSED_STATUSES and not meta.get("closed_date"):
            meta["closed_date"] = today
            meta.setdefault("closed_by", "")
            if not meta.get("closed_by"):
                meta["closed_by"] = f"Darryl, EOS web app, {today}"
        if st == "open":
            meta["closed_date"] = ""
            meta["closed_by"] = ""
    if kind == "watch" and "tier" in (patch or {}):
        if meta.get("tier") == "retired":
            meta["status"] = "closed"; meta.setdefault("closed_date", today)
            if not meta.get("closed_date"):
                meta["closed_date"] = today
        else:
            meta["status"] = "open"
    if note and note.strip():
        stamp = f"\n\n{today} ({actor}): {note.strip()}\n"
        body = (body or "").rstrip("\n") + stamp
        changed.append("note")
    if not changed:
        return item_json(meta, body, path)
    meta["last_touched"] = today
    import time as _t; SELF_WRITE_UNTIL[0] = _t.time() + 12
    R.write_item(meta, body)
    R.regenerate_all()
    git_commit(f"web: {item_id} — " + "; ".join(c[:60] for c in changed[:4]))
    return item_json(meta, body, path)


def create_item(title: str, note: str, kind: str = "action") -> dict:
    kind = kind if kind in R.KINDS else "action"
    iid = R.next_id("T")
    today = R.today()
    meta = {
        "id": iid, "kind": kind, "register": "triage", "tier": "", "status": "open", "title": title.strip(),
        "owner": "", "due": "", "next_action": "", "created": today, "last_touched": today,
        "needs_triage": True, "source": f"Darryl, EOS web app, {today}",
    }
    body = f"{today} (Darryl, web): {note.strip()}\n" if note and note.strip() else ""
    import time as _t; SELF_WRITE_UNTIL[0] = _t.time() + 12
    p = R.write_item(meta, body)
    R.regenerate_all()
    git_commit(f"web: new {iid} — {title.strip()[:60]}")
    return item_json(meta, body, p)


def recent_log(n: int = 30) -> list[dict]:
    rc, out = git("log", f"-{n}", "--date=short", "--pretty=format:%h\t%ad\t%s")
    if rc != 0:
        return []
    rows = []
    for l in out.splitlines():
        parts = l.split("\t", 2)
        if len(parts) == 3:
            rows.append({"hash": parts[0], "date": parts[1], "subject": parts[2]})
    return rows


# ----------------------------------------------------------------------------- HTTP

class H(BaseHTTPRequestHandler):
    server_version = "EOS/1.0"

    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (dt.datetime.now().strftime("%H:%M:%S"), fmt % args))

    # -- helpers
    def _auth_ok(self) -> bool:
        if not PASSWORD:
            return True
        h = self.headers.get("Authorization", "")
        if h.startswith("Basic "):
            try:
                user, _, pw = base64.b64decode(h[6:]).decode().partition(":")
                return pw == PASSWORD
            except Exception:
                return False
        return False

    def _send(self, code: int, body: bytes, ctype="application/json; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code, obj):
        self._send(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"))

    def _body(self) -> dict:
        n = int(self.headers.get("Content-Length", "0") or 0)
        raw = self.rfile.read(n) if n else b""
        try:
            return json.loads(raw.decode("utf-8")) if raw else {}
        except Exception:
            return {}

    def _gate(self) -> bool:
        if self._auth_ok():
            return True
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="EOS"')
        self.send_header("Content-Length", "0")
        self.end_headers()
        return False

    # -- routes
    def do_GET(self):
        if not self._gate():
            return
        u = urlparse(self.path)
        q = parse_qs(u.query)
        if u.path in ("/", "/index.html"):
            return self._send(200, HTML.encode("utf-8"), "text/html; charset=utf-8")
        if u.path == "/favicon.ico":
            return self._send(204, b"", "image/x-icon")
        if u.path == "/api/items":
            with LOCK:
                items = [item_json(m, b, p) for m, b, p in R.load_items()]
            if q.get("open", ["0"])[0] == "1":
                items = [i for i in items if i.get("status") not in CLOSED_STATUSES and i.get("tier") != "retired"]
            return self._json(200, {"items": items, "today": R.today()})
        m = re.fullmatch(r"/api/items/([A-Za-z0-9_.-]+)", u.path)
        if m:
            with LOCK:
                f = R.find_item(m.group(1))
            if not f:
                return self._json(404, {"error": "not found"})
            return self._json(200, item_json(*f))
        if u.path == "/api/guide":
            g = R.ROOT / "Reference" / "Registers_App_User_Guide.md"
            txt = g.read_text(encoding="utf-8") if g.exists() else "# Guide not found\n\nExpected at Reference/Registers_App_User_Guide.md."
            return self._json(200, {"markdown": txt})
        if u.path == "/api/log":
            return self._json(200, {"log": recent_log(int(q.get("n", ["30"])[0]))})
        return self._json(404, {"error": "no route"})

    def do_PATCH(self):
        if not self._gate():
            return
        u = urlparse(self.path)
        m = re.fullmatch(r"/api/items/([A-Za-z0-9_.-]+)", u.path)
        if not m:
            return self._json(404, {"error": "no route"})
        d = self._body()
        try:
            with LOCK:
                out = apply_patch(m.group(1), d.get("patch") or {}, d.get("note") or "", d.get("actor") or "Darryl, web")
            return self._json(200, out)
        except KeyError:
            return self._json(404, {"error": "not found"})
        except Exception as e:
            return self._json(500, {"error": str(e)})

    def do_POST(self):
        if not self._gate():
            return
        u = urlparse(self.path)
        d = self._body()
        if u.path == "/api/items":
            if not (d.get("title") or "").strip():
                return self._json(400, {"error": "title required"})
            with LOCK:
                out = create_item(d["title"], d.get("note", ""), d.get("kind", "action"))
            return self._json(201, out)
        if u.path == "/api/regenerate":
            with LOCK:
                counts = R.regenerate_all()
                msg = git_commit("regenerate 03/04/05 from Registers/")
            return self._json(200, {"counts": counts, "git": msg})
        return self._json(404, {"error": "no route"})


# ----------------------------------------------------------------------------- UI

HTML = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<title>EOS Registers</title>
<style>
:root{--bg:#f6f5f2;--card:#fff;--sunk:#efede8;--segOn:#fff;--ink:#1e2226;--ink2:#3c4249;--muted:#5f666e;--line:#e2dfd9;--line2:#eeece7;--acc:#2b5aa6;--accInk:#fff;--sel:#eef3fb;--red:#b23f2c;--amb:#94600a;--ambFill:#f2c66e;--ambInk:#3a2600;--shadow:0 1px 2px rgba(0,0,0,.12);--scrim:rgba(20,22,26,.32)}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#16181b;--card:#1d2024;--sunk:#26292e;--segOn:#3a3f46;--ink:#ecebe7;--ink2:#c8c6c1;--muted:#9ca1a8;--line:#33373d;--line2:#272a2f;--acc:#94b5ec;--accInk:#0f1520;--sel:#232b37;--red:#f2917f;--amb:#e8b762;--ambFill:#e8b762;--ambInk:#1e1607;--shadow:0 1px 2px rgba(0,0,0,.5);--scrim:rgba(0,0,0,.55)}}
:root[data-theme=dark]{--bg:#16181b;--card:#1d2024;--sunk:#26292e;--segOn:#3a3f46;--ink:#ecebe7;--ink2:#c8c6c1;--muted:#9ca1a8;--line:#33373d;--line2:#272a2f;--acc:#94b5ec;--accInk:#0f1520;--sel:#232b37;--red:#f2917f;--amb:#e8b762;--ambFill:#e8b762;--ambInk:#1e1607;--shadow:0 1px 2px rgba(0,0,0,.5);--scrim:rgba(0,0,0,.55)}
*{box-sizing:border-box}html,body{margin:0}
body{background:var(--bg);color:var(--ink);font:15px/1.4 -apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;-webkit-text-size-adjust:100%}
button,input,select,textarea{font:inherit;color:inherit}a{color:var(--acc)}
button{cursor:pointer}
button,.row,.tab{-webkit-tap-highlight-color:transparent}
input[type=search],textarea{-webkit-appearance:none;appearance:none}
body.locked{overflow:hidden}
:focus-visible{outline:2px solid var(--acc);outline-offset:1px}
/* header */
header{position:sticky;top:0;z-index:5;background:var(--card);border-bottom:1px solid var(--line)}
.hbar{display:flex;align-items:center;gap:16px;padding:0 24px;height:56px}
.brand{font-size:16px;font-weight:650;letter-spacing:-.01em;white-space:nowrap;margin:0}
.tabs{display:flex;gap:2px;align-self:stretch;flex:1;min-width:0;overflow-x:auto;scrollbar-width:none}.tabs::-webkit-scrollbar{display:none}
.tab{display:flex;align-items:center;gap:5px;padding:0 9px;border:0;border-bottom:2px solid transparent;background:none;color:var(--muted);white-space:nowrap;font-size:14px}
.tab:hover{color:var(--ink)}.tab.on{color:var(--ink);font-weight:650;border-bottom-color:var(--ink)}
.tab .n{font-size:12px;font-weight:500;color:var(--muted);font-variant-numeric:tabular-nums}
#q{width:190px;flex:none;height:34px;border:1px solid var(--line);border-radius:8px;background:var(--bg);padding:0 12px;font-size:14px}
.btn{height:34px;padding:0 14px;border:1px solid var(--line);border-radius:8px;background:transparent;color:var(--ink2);font-size:14px;white-space:nowrap;flex:none}
.btn.primary{background:var(--acc);border-color:var(--acc);color:var(--accInk);font-weight:600}
.btn .badge{display:inline-block;min-width:18px;padding:0 5px;margin-left:6px;border-radius:9px;background:var(--acc);color:var(--accInk);font-size:11.5px;line-height:18px;font-weight:600}
#searchBtn{display:none}
#helpBtn{width:34px;padding:0;font-weight:600}
.md h1{font-size:18px;margin:0 0 10px}.md h2{font-size:14px;margin:18px 0 6px;letter-spacing:.04em;text-transform:uppercase;color:var(--muted)}.md p{margin:6px 0;font-size:14px;line-height:21px}.md ul,.md ol{margin:6px 0;padding-left:22px;font-size:14px;line-height:21px}.md li{margin:3px 0}.md code{font:12.5px ui-monospace,Menlo,monospace;background:var(--sunk);padding:1px 4px;border-radius:4px}.md table{border-collapse:collapse;font-size:13px;margin:6px 0}.md td,.md th{border:1px solid var(--line);padding:4px 8px;text-align:left;vertical-align:top}
.caps{display:flex;align-items:center;gap:28px;padding:0 24px;height:40px;border-top:1px solid var(--line2);font-size:13px;color:var(--ink2);overflow-x:auto;white-space:nowrap;scrollbar-width:none}
.cap{display:flex;align-items:center;gap:8px}.cap .s{display:none}
.cap .bar{width:64px;height:4px;border-radius:2px;background:var(--sunk);overflow:hidden}.cap .bar i{display:block;height:100%;background:var(--ink2)}
.cap b{font-variant-numeric:tabular-nums;color:var(--ink)}.cap.over b{color:var(--red)}.cap.over .bar i{background:var(--red)}
.cap .dot{width:8px;height:8px;border-radius:50%;background:var(--ambFill)}
.caps .today{margin-left:auto;color:var(--muted)}
/* list */
main{padding:14px 20px 80px;max-width:1400px;margin:0 auto}
body.docked{padding-right:460px}
body.docked .hbar{flex-wrap:wrap;height:auto;padding-top:10px;row-gap:0}
body.docked .brand{flex:1}
body.docked .tabs{order:5;flex-basis:100%;height:44px;margin:0 -9px}
.group{background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden;margin-bottom:14px}
.ghead{display:flex;gap:8px;padding:10px 16px;font-size:12px;font-weight:650;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);margin:0}
.ghead.over{color:var(--red)}.ghead.tri{color:var(--amb)}.ghead.week{color:var(--ink)}.ghead .n{font-weight:500;color:var(--muted)}
.row{display:grid;grid-template-columns:48px minmax(0,1fr) 96px 212px;grid-template-areas:"id body due seg";gap:14px;align-items:start;padding:11px 16px;border-top:1px solid var(--line2);cursor:pointer}
.row:hover{background:var(--bg)}.row.sel{background:var(--sel)}
.row .id{grid-area:id}.row .body{grid-area:body;min-width:0}.row .due{grid-area:due}.row .seg{grid-area:seg}
.id{font:12px/20px ui-monospace,"SF Mono",Menlo,monospace;color:var(--muted)}
.title{font-size:14.5px;line-height:20px;font-weight:600;text-wrap:pretty;overflow-wrap:anywhere}
.row.done .title{color:var(--muted);text-decoration:line-through}
.next{font-size:14px;line-height:20px;color:var(--ink2);margin-top:1px;overflow-wrap:anywhere;text-wrap:pretty}.next.ctx{color:var(--muted)}
.meta{display:flex;flex-wrap:wrap;gap:4px 10px;align-items:center;margin-top:5px;font-size:12px;color:var(--muted)}
.t-tri{background:var(--ambFill);color:var(--ambInk);padding:1px 7px;border-radius:4px;font-weight:600}
.t-crit{color:var(--red);font-weight:700;letter-spacing:.06em;font-size:11px;text-transform:uppercase}
.t-sev{display:inline-flex;align-items:center;gap:5px;font-weight:600}.t-sev:before{content:"";width:7px;height:7px;border-radius:50%;background:currentColor}
.t-sev.high{color:var(--red)}.t-sev.medium{color:var(--amb)}
.due{text-align:right;padding-top:1px}.due b{display:block;font-size:13.5px;line-height:18px;font-weight:600;color:var(--muted);font-variant-numeric:tabular-nums}.due span{font-size:12px;color:var(--muted)}
.due.late b,.due.late span{color:var(--red)}.due.today b{color:var(--ink)}
.seg{display:flex;padding:2px;background:var(--sunk);border-radius:8px;align-self:start}
.seg button{flex:1;min-width:0;border:0;height:28px;padding:0 4px;border-radius:6px;background:transparent;color:var(--muted);font-size:12.5px}
.seg button:hover{color:var(--ink)}.seg button.on{background:var(--segOn);color:var(--ink);font-weight:650;box-shadow:var(--shadow)}
.more{display:block;width:100%;text-align:left;padding:10px 16px 10px 78px;border:0;border-top:1px solid var(--line2);background:none;color:var(--acc);font-size:13px;font-weight:500}
.empty{padding:40px 16px;color:var(--muted);text-align:center}
/* panel */
#scrim{position:fixed;inset:0;cursor:pointer;background:var(--scrim);z-index:9;display:none}
#drawer{position:fixed;top:0;right:0;bottom:0;width:460px;max-width:100%;background:var(--card);border-left:1px solid var(--line);z-index:10;display:none;overflow-y:auto;-webkit-overflow-scrolling:touch;overscroll-behavior:contain;padding-bottom:env(safe-area-inset-bottom)}
#drawer.open{display:block}
.p-top{padding:18px 22px 0}
.p-meta{display:flex;align-items:center;gap:10px;font-size:12px;color:var(--muted)}.p-meta .id{line-height:1}
.p-close{margin-left:auto;border:0;background:none;color:var(--ink2);font-size:14px;height:32px;padding:0 4px}
.p-back{display:none}
.p-title{font-size:18px;line-height:24px;font-weight:650;margin:8px 0 0;text-wrap:pretty;overflow-wrap:anywhere}
.p-next{font-size:14.5px;line-height:21px;color:var(--ink2);margin-top:6px}
.p-due{font-size:13px;margin-top:8px;font-weight:600;color:var(--ink2)}.p-due.late{color:var(--red)}
.p-act{padding:16px 22px 18px;border-bottom:1px solid var(--line2)}
.seg.lg{padding:3px;border-radius:9px}.seg.lg button{height:34px;font-size:14px;border-radius:7px}
textarea{display:block;width:100%;margin-top:12px;height:84px;padding:10px 12px;border:1px solid var(--line);border-radius:8px;background:var(--bg);font-size:14.5px;line-height:20px;resize:vertical}
.p-save{display:flex;align-items:center;gap:12px;margin-top:10px}.p-save .hint{font-size:12.5px;color:var(--muted)}.p-save .hint.ok{color:var(--ink2)}
.p-sec{padding:16px 22px}
.p-label{font-size:12px;font-weight:650;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);margin:0 0 6px}
.h{display:grid;grid-template-columns:72px minmax(0,1fr);gap:12px;padding:8px 0;border-top:1px solid var(--line2)}
.h .d{font-size:12.5px;color:var(--muted);line-height:20px}.h .w{font-size:12px;color:var(--muted);line-height:20px}
.h .t{font-size:14px;line-height:21px;white-space:pre-wrap;overflow-wrap:anywhere;text-wrap:pretty}
.h.new .t{color:var(--ink);font-weight:500}
details{border-top:1px solid var(--line);margin-top:14px}
summary{display:flex;justify-content:space-between;align-items:center;padding:12px 0;font-size:14px;font-weight:600;cursor:pointer;list-style:none}summary::-webkit-details-marker{display:none}
summary span{font-weight:400;color:var(--muted);font-size:13px}
.sl{display:inline-flex;align-items:center;gap:8px;font-weight:600;color:var(--acc)}
.sl:before{content:"";width:8px;height:8px;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:translateY(-2px) rotate(45deg);transition:transform .15s}
details[open] .sl:before{transform:translateY(2px) rotate(-135deg)}
summary:hover .sl{text-decoration:underline}
.fgrid{display:grid;grid-template-columns:1fr 1fr;gap:10px 12px}.fgrid .full{grid-column:1/-1}
.fgrid label{display:block;font-size:11.5px;color:var(--muted);margin-bottom:3px}
.fgrid input,.fgrid select{width:100%;height:32px;padding:0 9px;border:1px solid var(--line);border-radius:6px;background:var(--bg);font-size:13.5px}
.log{display:grid;grid-template-columns:90px minmax(0,1fr);gap:4px 12px;font-size:13.5px;line-height:20px}.log .d{color:var(--muted);font-variant-numeric:tabular-nums}
.toast{position:fixed;bottom:calc(20px + env(safe-area-inset-bottom));left:50%;transform:translateX(-50%);background:var(--ink);color:var(--bg);padding:10px 16px;border-radius:10px;font-size:14px;display:none;z-index:20;box-shadow:0 8px 24px rgba(0,0,0,.2);white-space:nowrap}
/* tablet: panel overlays */
@media (max-width:1099px){body.docked{padding-right:0}}
/* phone */
@media (max-width:820px){
 .hbar{flex-wrap:wrap;height:auto;padding:calc(10px + env(safe-area-inset-top)) 16px 0;gap:8px}
 .brand{flex:1;font-size:18px}
 .tabs{order:5;flex-basis:100%;margin:0 -8px;height:44px}.tab{padding:0 8px;font-size:14.5px}
 #searchBtn{display:block}#q{display:none;order:4;flex-basis:100%;width:100%;height:44px;font-size:16px}body.searching #q{display:block}
 .btn{height:44px;font-size:15px;padding:0 14px;border-radius:10px}#helpBtn{width:44px}
 .caps{gap:16px;padding:0 16px}.cap .l,.cap .bar,.caps .today{display:none}.cap .s{display:inline}
 main{padding:10px 0 80px}
 .group{border-radius:0;border-left:0;border-right:0;margin-bottom:10px}
 .row{grid-template-columns:minmax(0,1fr) auto;grid-template-areas:"id due" "body body" "seg seg";gap:4px 8px;padding:12px 16px}
 .row .due{display:flex;gap:6px;align-items:baseline;padding:0}.due b{display:inline;font-size:12.5px}.due span{font-size:12.5px}
 .row .id{font-size:12.5px}
 .title{font-size:16px;line-height:21px}.next{font-size:15px;line-height:20px;margin-top:3px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
 .meta{font-size:12.5px}.row .seg{margin-top:8px}.seg button{height:40px;font-size:14.5px}
 .more{padding:14px 16px}
 #drawer{width:100%;border-left:0}
 .p-top{padding:calc(8px + env(safe-area-inset-top)) 18px 0}
 .p-close{display:none}.p-back{display:block;border:0;background:none;color:var(--acc);font-size:16px;font-weight:500;height:44px;padding:0 12px 0 0}
 .p-title{font-size:19px;line-height:25px}.p-next{font-size:15px}
 .p-act{padding:14px 18px 18px}.seg.lg button{height:42px;font-size:15px}
 textarea,.fgrid input,.fgrid select{font-size:16px}.fgrid input,.fgrid select{height:40px}
 .p-save{flex-direction:column;align-items:stretch}.p-save .btn{height:48px;font-size:16px}.p-save .hint{text-align:center}
 .p-sec{padding:16px 18px}.fgrid{grid-template-columns:1fr}
 .toast{white-space:normal;max-width:calc(100% - 32px)}
}
</style></head><body>
<header>
 <div class="hbar">
  <h1 class="brand">EOS Registers</h1>
  <nav class="tabs" id="views" aria-label="Views"></nav>
  <input type="search" id="q" placeholder="Search title, owner, ID, notes…" autocomplete="off">
  <button class="btn" id="searchBtn">Search</button>
  <button class="btn primary" id="newBtn">Add</button>
  <button class="btn" id="logBtn">Changes</button>
  <button class="btn" id="helpBtn" aria-label="Help">?</button>
 </div>
 <div class="caps" id="meta"></div>
</header>
<main id="root"><div id="list"></div></main>
<div id="scrim"></div>
<aside id="drawer" aria-label="Item"><div id="panel"></div></aside>
<div class="toast" id="toast" role="status"></div>

<script>
const $=s=>document.querySelector(s);
let ITEMS=[],TODAY='',VIEW='triage',Q='',SEL=null,MOREW=false,DRAWER=null;
const BASE={},SESSION=[],SAVED={};
const CLOSED=new Set(['closed','dropped','aged_out']);
const isOpen=i=>!CLOSED.has(i.status)&&i.tier!=='retired';
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const plain=s=>String(s??'').replace(/\*\*([^*]+)\*\*/g,'$1').replace(/`([^`]+)`/g,'$1').replace(/~~([^~]+)~~/g,'$1');
let toastT;function toast(t){const e=$('#toast');e.textContent=t;e.style.display='block';clearTimeout(toastT);toastT=setTimeout(()=>e.style.display='none',2200)}
async function load(){const j=await (await fetch('/api/items')).json();ITEMS=j.items;TODAY=j.today;render();const o=new URLSearchParams(location.search).get('open');if(o&&!DRAWER)openDrawer(o)}

const VIEWS=[['triage','Triage'],['A','Mine'],['other','Other-owned'],['watch','Watch'],['decision','Decisions'],['needs','Needs triage'],['closed','Disposed']];
const MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],WD=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
const dn=s=>{const[y,m,d]=s.split('-').map(Number);return Date.UTC(y,m-1,d)};
const days=s=>Math.round((dn(s)-dn(TODAY))/864e5);
const fmt=s=>{if(!/^\d{4}-\d{2}-\d{2}/.test(s||''))return esc(s||'');const[y,m,d]=s.split('-').map(Number);return MON[m-1]+' '+d+(y!==+TODAY.slice(0,4)?', '+y:'')};
const cap=s=>s?s.charAt(0).toUpperCase()+s.slice(1).replace('_',' '):'';
function dueKey(i){return i.due||i.forum_date||'9999'}
function inView(i,v){
  if(v==='triage')return isOpen(i)&&((i.kind==='action'&&(i.register==='A'||i.register==='triage'||i.critical))||(i.kind==='watch'&&i.tier==='active')||(i.kind==='decision'&&i.tier==='radar'));
  if(v==='A')return isOpen(i)&&i.kind==='action'&&i.register==='A';
  if(v==='other')return isOpen(i)&&i.kind==='action'&&i.register==='other';
  if(v==='watch')return isOpen(i)&&i.kind==='watch';
  if(v==='decision')return isOpen(i)&&i.kind==='decision';
  if(v==='needs')return !!i.needs_triage;
  if(v==='closed')return !isOpen(i);
}
function filtered(){
  /* membership uses the item as it was before this session's edits, so a row you just closed stays put (struck through) until you switch views */
  let a=ITEMS.filter(i=>inView(BASE[i.id]||i,VIEW));
  if(Q){const q=Q.toLowerCase();a=a.filter(i=>[i.id,i.title,i.owner,i.counterparty,i.next_action,i.body,i.forum,i.critical?'critical':'',i.severity,i.type].join(' ').toLowerCase().includes(q))}
  const kr={action:0,watch:1,decision:2};const rr={triage:0,A:1,other:2};
  if(VIEW==='closed') a.sort((x,y)=>(y.closed_date||'').localeCompare(x.closed_date||''));
  else a.sort((x,y)=>(x.needs_triage?-1:0)-(y.needs_triage?-1:0)||(kr[x.kind]-kr[y.kind])||((rr[x.register]??3)-(rr[y.register]??3))||((y.critical?1:0)-(x.critical?1:0))||dueKey(x).localeCompare(dueKey(y))||(x.last_touched||'').localeCompare(y.last_touched||''));
  return a;
}
const SEV={high:0,medium:1,low:2};
function groups(a){
  if(VIEW!=='triage'){const l=Q?'Search results':VIEWS.find(v=>v[0]===VIEW)[1];return [{k:'',l,rows:a}]}
  const g={tri:[],over:[],week:[],later:[],nodate:[],watch:[]};
  for(const i of a){
    if(i.needs_triage){g.tri.push(i);continue}
    if(i.kind==='watch'){g.watch.push(i);continue}
    const d=i.due||i.forum_date;if(!d){g.nodate.push(i);continue}
    const n=days(d);(n<0?g.over:n<7?g.week:g.later).push(i);
  }
  for(const k of ['over','week','later'])g[k].sort((x,y)=>dueKey(x).localeCompare(dueKey(y)));
  g.watch.sort((x,y)=>(SEV[(x.severity||'').toLowerCase()]??3)-(SEV[(y.severity||'').toLowerCase()]??3));
  return [{k:'tri',l:'New · needs triage',rows:g.tri},{k:'over',l:'Overdue',rows:g.over},{k:'week',l:'Due this week',rows:g.week},{k:'',l:'Later',rows:g.later},{k:'',l:'No date',rows:g.nodate},{k:'watch',l:'Watch · active risks',rows:g.watch}].filter(x=>x.rows.length);
}
function tags(i){let t='';
  if(i.needs_triage)t+='<span class="t-tri">Needs triage</span>';
  if(i.critical)t+='<span class="t-crit">Critical</span>';
  if(i.kind==='watch'&&i.severity)t+=`<span class="t-sev ${esc(i.severity.toLowerCase())}">${esc(i.severity)}</span>`;
  return t}
function who(i){
  if(i.kind==='action')return i.register==='A'?'Mine':i.register==='triage'?'New':`${i.type||'Other-owned'}${i.owner?' · '+i.owner:''}`;
  if(i.kind==='watch')return [cap(i.tier),i.trend?'trend '+i.trend:'',i.evidence_basis].filter(Boolean).join(' · ');
  return [i.forum,i.owner].filter(Boolean).join(' · ');
}
function context(i){
  if(i.next_action)return {t:plain(i.next_action),ctx:false};
  if(i.kind==='decision'&&i.status)return {t:i.status,ctx:true};
  const b=(i.body||'').split(/\n+/).map(l=>l.replace(/^##\s.*$/,'').replace(/^\d{4}-\d{2}-\d{2} \([^)]+\):\s*/,'').replace(/^-\s*/,'').trim()).filter(Boolean)[0]||'';
  return {t:plain(b),ctx:true};
}
function statusOpts(i){return i.kind==='action'?['status',['open','closed','dropped'],i.status]:i.kind==='watch'?['tier',['active','passive','retired'],i.tier]:['tier',['radar','backlog'],i.tier]}
function seg(i,lg){const[k,opts,cur]=statusOpts(i);
  return `<div class="seg${lg?' lg':''}" role="group" aria-label="Status">${opts.map(o=>`<button type="button" class="${o===cur?'on':''}" aria-pressed="${o===cur}" data-id="${esc(i.id)}" data-k="${k}" data-val="${o}">${cap(o)}</button>`).join('')}</div>`}
function dueInfo(i){
  const due=i.due||i.forum_date||'';const open=isOpen(i);if(!due)return {due:'',rel:open?'':cap(i.status==='open'?i.tier:i.status),cls:''};
  const n=days(due);let rel=n<0?`${-n} day${n===-1?'':'s'} late`:n===0?'Today':n<7?WD[new Date(dn(due)).getUTCDay()]:`In ${n} days`;
  if(!open)rel=cap(i.kind==='action'?i.status:i.tier);
  return {due,rel,n,cls:open&&n<0?'late':open&&n===0?'today':''};
}
function rowHtml(i){
  const d=dueInfo(i);const c=context(i);
  return `<div class="row${SEL===i.id?' sel':''}${isOpen(i)?'':' done'}" data-id="${esc(i.id)}">
    <div class="id">${esc(i.id)}</div>
    <div class="body"><div class="title">${esc(i.title)}</div>${c.t?`<div class="next${c.ctx?' ctx':''}">${esc(c.t)}</div>`:''}<div class="meta">${tags(i)}<span>${esc(who(i))}</span></div></div>
    <div class="due ${d.cls}"><b>${fmt(d.due)}</b><span>${d.rel}</span></div>
    ${seg(i)}
  </div>`}
function render(){
  const a=filtered();const open=ITEMS.filter(isOpen);
  const A=open.filter(i=>i.kind==='action'&&i.register==='A').length,W=open.filter(i=>i.kind==='watch'&&i.tier==='active').length,D=open.filter(i=>i.kind==='decision'&&i.tier==='radar').length,N=ITEMS.filter(i=>i.needs_triage).length;
  $('#views').innerHTML=VIEWS.map(([v,l])=>`<button class="tab${v===VIEW?' on':''}" data-v="${v}"${v===VIEW?' aria-current="page"':''}>${l}<span class="n">${ITEMS.filter(i=>inView(i,v)).length}</span></button>`).join('');
  const m=(l,s,n,c)=>`<div class="cap${n>c?' over':''}"><span class="l">${l}</span><span class="s">${s}</span><span class="bar"><i style="width:${Math.min(100,n/c*100)}%"></i></span><b>${n}/${c}</b></div>`;
  const dt=new Date(dn(TODAY));
  $('#meta').innerHTML=m('Register A','A',A,15)+m('Watch active','Watch',W,20)+m('Radar','Radar',D,20)+`<div class="cap"><span class="dot"></span><span class="l">Needs triage</span><span class="s">Triage</span><b>${N}</b></div><span class="today">${a.length} shown · ${['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][dt.getUTCDay()]}, ${fmt(TODAY)}</span>`;
  $('#logBtn').innerHTML='Changes'+(SESSION.length?`<span class="badge">${SESSION.length}</span>`:'');
  const gs=groups(a);
  $('#list').innerHTML=gs.map(g=>{let rows=g.rows,more='';
    if(g.k==='watch'&&rows.length>3){more=`<button class="more" data-more>${MOREW?'Show fewer':'Show '+(rows.length-3)+' more risks'}</button>`;if(!MOREW)rows=rows.slice(0,3)}
    return `<section class="group"><h2 class="ghead ${g.k}">${g.l}<span class="n">${g.rows.length}</span></h2>${rows.map(rowHtml).join('')}${more}</section>`}).join('')||'<div class="empty">Nothing here.</div>';
}
document.addEventListener('click',e=>{
  const s=e.target.closest('.seg button');if(s){e.stopPropagation();const i=ITEMS.find(x=>x.id===s.dataset.id);if(i&&i[s.dataset.k]!==s.dataset.val)patch(s.dataset.id,{[s.dataset.k]:s.dataset.val},'');return}
  const c=e.target.closest('.tab[data-v]');if(c){VIEW=c.dataset.v;MOREW=false;for(const k in BASE)delete BASE[k];render();scrollTo(0,0);return}
  if(e.target.closest('[data-more]')){MOREW=!MOREW;render();return}
  const r=e.target.closest('.row[data-id]');if(r){openDrawer(r.dataset.id)}
});
$('#q').addEventListener('input',e=>{Q=e.target.value.trim();render()});
$('#searchBtn').onclick=()=>{document.body.classList.toggle('searching');if(document.body.classList.contains('searching'))$('#q').focus();else{$('#q').value='';Q='';render()}};
async function patch(id,p,note){
  const k=ITEMS.findIndex(x=>x.id===id);if(k<0)return null;
  if(!BASE[id])BASE[id]=ITEMS[k];
  const r=await fetch('/api/items/'+encodeURIComponent(id),{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({patch:p,note})});
  if(!r.ok){toast('Save failed · '+id);return null}
  const j=await r.json();
  ITEMS[k]=j;
  const what=[...Object.keys(p).filter(f=>String(p[f])!==String(BASE[id][f]??'')||f==='status'||f==='tier').map(f=>(f==='status'||f==='tier')?cap(p[f]):f.replace('_',' ')),note&&note.trim()?'note':''].filter(Boolean).join(', ')||'saved';
  SESSION.unshift({id,what,t:new Date().toLocaleTimeString([], {hour:'numeric',minute:'2-digit'})});
  SAVED[id]=SESSION[0];
  toast('Saved · '+id+' · '+what);render();
  if(DRAWER==='item'&&SEL===id)openDrawer(id);
  return j;
}
/* ---------- panel ---------- */
function layout(){const open=!!DRAWER;const dock=open&&innerWidth>=1100&&DRAWER==='item';
  document.body.classList.toggle('docked',dock);$('#scrim').style.display=open&&!dock?'block':'none';$('#drawer').classList.toggle('open',open);document.body.classList.toggle('locked',open&&!dock)}
function showDrawer(kind){DRAWER=kind;layout()}
function closeDrawer(){DRAWER=null;SEL=null;layout();render()}
addEventListener('resize',layout);
addEventListener('keydown',e=>{if(e.key==='Escape'&&DRAWER)closeDrawer()});
$('#scrim').onclick=closeDrawer;
function head(id,meta){return `<div class="p-meta"><button type="button" class="p-back" data-close>‹ Back</button>${id?`<span class="id">${esc(id)}</span>`:''}<span>${meta}</span><button type="button" class="p-close" data-close>Close</button></div>`}
function history(i){
  const out=[];let sec='';
  for(const p of (i.body||'').split(/\n\s*\n/)){const t=p.trim();if(!t)continue;
    const h=t.match(/^##\s+(.*)/);if(h){sec=h[1];out.push(null);continue}
    const m=t.match(/^(\d{4}-\d{2}-\d{2}) \(([^)]+)\):\s*([\s\S]*)/);
    const body=x=>plain(x.replace(/^(\s*)[-*] /gm,'$1• '));
    if(m)out.push({d:fmt(m[1]),w:m[2]==='Darryl, web'?'You, from the web':m[2],t:body(m[3]),isNew:m[1]===TODAY&&m[2]==='Darryl, web'});
    else if(out.length&&out[out.length-1])out[out.length-1].t+='\n\n'+body(t);
    else out.push({d:'',w:sec||'Record',t:body(t)});
  }
  for(let k=out.length;k--;)if(!out[k])out.splice(k,1);
  return out.reverse();
}
function field(l,k,v,type='text',opts,full){
  const inner=opts?`<select name="${k}">${opts.map(o=>`<option ${o===v?'selected':''}>${o}</option>`).join('')}</select>`:`<input name="${k}" type="${type}" value="${esc(v)}">`;
  return `<div${full?' class="full"':''}><label>${l}${inner}</label></div>`}
function fields(i){let f=field('Title','title',i.title,'text',null,true);
  if(i.kind==='action'){
    f+=field('Register','register',i.register,'',['A','other','triage'])+field('Status','status',i.status,'',['open','closed','dropped','aged_out']);
    f+=field('Owner','owner',i.owner)+field('Counterparty','counterparty',i.counterparty);
    f+=field('Type (other-owned)','type',i.type||'','',['','Delegated','Awaited'])+field('Critical','critical',String(!!i.critical),'',['false','true']);
    f+=field('Due (YYYY-MM-DD)','due',i.due)+field('Due note / gate','due_note',i.due_note);
    f+=field('Trigger','trigger',i.trigger)+field('Product','product',i.product||'');
    f+=field('Next action (one line)','next_action',i.next_action,'text',null,true);
    f+=field('Critical reason','critical_reason',i.critical_reason||'')+field('Basis','basis',i.basis||'');
  }else if(i.kind==='watch'){
    f+=field('Tier','tier',i.tier,'',['active','passive','retired'])+field('Severity','severity',i.severity||'','',['','High','Medium','Low']);
    f+=field('Trend','trend',i.trend||'')+field('Evidence basis','evidence_basis',i.evidence_basis||'');
    f+=field('Next action (one line)','next_action',i.next_action||'','text',null,true)+field('Product','product',i.product||'');
  }else{
    f+=field('Tier','tier',i.tier,'',['radar','backlog'])+field('Status (free text)','status',i.status||'');
    f+=field('Owner','owner',i.owner||'')+field('Forum date (YYYY-MM-DD)','forum_date',i.forum_date||'');
    f+=field('Forum','forum',i.forum||'','text',null,true)+field('Next action (one line)','next_action',i.next_action||'','text',null,true)+field('Product','product',i.product||'');
  }
  return f+field('Needs triage','needs_triage',String(!!i.needs_triage),'',['false','true'])}
function openDrawer(id){
  const i=ITEMS.find(x=>x.id===id);if(!i)return;
  const same=SEL===id&&DRAWER==='item';
  const keepNote=same&&$('#note')?$('#note').value:'',keepDet=same&&$('#det')?$('#det').open:false,keepScroll=same?$('#drawer').scrollTop:0;
  SEL=id;
  const reg=i.kind==='action'?(i.register==='A'?'Register A · Mine':i.register==='triage'?'New item':'Other-owned'+(i.type?' · '+i.type:'')):i.kind==='watch'?'Watch'+(i.severity?' · '+i.severity:''):'Decision · '+cap(i.tier);
  const d=dueInfo(i);const due=d.due?`${i.kind==='decision'?'Forum':'Due'} ${fmt(d.due)} · ${d.n<0?-d.n+' day'+(d.n===-1?'':'s')+' late':d.n===0?'today':'in '+d.n+' days'}`:(i.trigger?'No date · waits on: '+esc(i.trigger):'No due date');
  const nFields=(fields(i).match(/<label>/g)||[]).length;
  const sv=SAVED[id];
  $('#panel').innerHTML=`<div class="p-top">${head(i.id,esc(reg))}
     <h2 class="p-title">${esc(i.title)}</h2>
     ${i.next_action?`<div class="p-next">${esc(plain(i.next_action))}</div>`:''}
     <div class="p-due${d.cls==='late'?' late':''}">${due}${i.critical?' · <span class="t-crit">Critical</span>':''}</div></div>
   <form id="nf2" class="p-act">${seg(i,true)}
     <textarea id="note" name="note" placeholder="Add a note: what happened, what you decided, what Claude should know…">${esc(keepNote)}</textarea>
     <div class="p-save"><button type="submit" class="btn primary">Save note</button><span class="hint${sv?' ok':''}">${sv?`Saved ${sv.t} · ${esc(sv.what)} · committed`:'Status saves on tap. Notes are dated, appended and committed.'}</span></div></form>
   <div class="p-sec"><h3 class="p-label">History</h3>
     ${history(i).map(h=>`<div class="h${h.isNew?' new':''}"><div class="d">${h.d}</div><div><div class="w">${esc(h.w)}</div><div class="t">${esc(h.t)}</div></div></div>`).join('')||'<div class="h"><div></div><div class="t" style="color:var(--muted)">No notes yet.</div></div>'}
     <details id="det"${keepDet?' open':''}><summary><span class="sl">Details</span><span>${nFields} fields · ${esc(i.path||'')}</span></summary>
       <form id="f"><div class="fgrid">${fields(i)}</div><div class="p-save"><button type="submit" class="btn primary">Save details</button><span class="hint">Last touched ${fmt(i.last_touched)}</span></div></form></details>
   </div>`;
  showDrawer('item');if(!same)$('#drawer').scrollTop=0;else $('#drawer').scrollTop=keepScroll;
  render();
  $('#nf2').onsubmit=async ev=>{ev.preventDefault();const n=$('#note').value;if(!n.trim()){$('#note').focus();return}$('#note').value='';await patch(id,{},n)};
  $('#f').onsubmit=async ev=>{ev.preventDefault();const fd=new FormData(ev.target);const p={};
    for(const [k,v] of fd.entries())p[k]=(k==='critical'||k==='needs_triage')?(v==='true'):v;
    await patch(id,p,'')};
}
$('#panel').addEventListener('click',e=>{if(e.target.closest('[data-close]'))closeDrawer()});
/* Markdown-style lists in the note box: "1. " or "- " starts a list; Return continues it; Return on an empty item ends it. */
$('#panel').addEventListener('keydown',e=>{
  const t=e.target;if(!(t instanceof HTMLTextAreaElement)||e.key!=='Enter'||e.shiftKey||e.metaKey||e.ctrlKey||e.isComposing)return;
  const v=t.value,pos=t.selectionStart;const ls=v.lastIndexOf('\n',pos-1)+1;const line=v.slice(ls,pos);
  const m=line.match(/^(\s*)(?:([-*•])|(\d+)([.)]))(\s+)(.*)$/);if(!m)return;
  e.preventDefault();
  const [,ind,bul,num,punc,sp,rest]=m;
  if(!rest.trim()){t.setRangeText('',ls,pos,'end');t.setRangeText('\n',ls,ls,'end');return}
  const next=bul?`${ind}${bul}${sp}`:`${ind}${+num+1}${punc}${sp}`;
  t.setRangeText('\n'+next,pos,t.selectionEnd,'end');
  t.dispatchEvent(new Event('input',{bubbles:true}));
});
$('#newBtn').onclick=()=>{
  SEL=null;
  $('#panel').innerHTML=`<div class="p-top">${head('', 'New item')}</div>
   <form id="nf" class="p-act" style="border:0"><div class="fgrid"><div class="full"><label>Title<input name="title" required autocomplete="off" enterkeyhint="done"></label></div></div>
   <textarea name="note" placeholder="Note (optional)"></textarea>
   <div class="p-save"><button type="submit" class="btn primary">Add</button><span class="hint">Lands as a T-item flagged “needs triage”; Claude classifies it at the next brief.</span></div></form>`;
  showDrawer('new');$('#nf [name=title]').focus();
  $('#nf').onsubmit=async ev=>{ev.preventDefault();const fd=new FormData(ev.target);
    const r=await fetch('/api/items',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title:fd.get('title'),note:fd.get('note')})});
    if(!r.ok){toast('Add failed');return}const id=(await r.json()).id;await load();
    SESSION.unshift({id,what:'added',t:new Date().toLocaleTimeString([], {hour:'numeric',minute:'2-digit'})});
    toast('Added '+id+' · needs triage');closeDrawer()};
};
$('#logBtn').onclick=async()=>{const j=await (await fetch('/api/log?n=40')).json();
  SEL=null;
  $('#panel').innerHTML=`<div class="p-top">${head('','Changes')}<h2 class="p-title">This session</h2></div>
   <div class="p-sec">${SESSION.length?`<div class="log">${SESSION.map(s=>`<span class="d">${esc(s.t)}</span><span><b>${esc(s.id)}</b> · ${esc(s.what)}</span>`).join('')}</div>`:'<div style="color:var(--muted);font-size:14px">Nothing changed yet.</div>'}</div>
   <div class="p-sec"><h3 class="p-label">Recent commits (git)</h3>${j.log.length?`<div class="log">${j.log.map(l=>`<span class="d">${fmt(l.date)}</span><span>${esc(l.subject)}</span>`).join('')}</div>`:'<div style="color:var(--muted)">No git history yet.</div>'}</div>`;
  showDrawer('log');render()};
function md(src){const inl=t=>esc(t).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>');
  const out=[];let list=null,tbl=null;const flush=()=>{if(list){out.push(`</${list}>`);list=null}if(tbl){out.push('</table>');tbl=null}};
  for(const raw of src.split('\n')){const l=raw.trimEnd();
    if(!l.trim()){flush();continue}
    let m;
    if((m=l.match(/^(#{1,3}) (.*)/))){flush();out.push(`<h${m[1].length}>${inl(m[2])}</h${m[1].length}>`);continue}
    if((m=l.match(/^\|(.+)\|$/))){if(/^\|[\s|:-]+\|$/.test(l))continue;const cells=m[1].split('|').map(c=>c.trim());if(!tbl){flush();tbl=1;out.push('<table>');out.push('<tr>'+cells.map(c=>`<th>${inl(c)}</th>`).join('')+'</tr>')}else out.push('<tr>'+cells.map(c=>`<td>${inl(c)}</td>`).join('')+'</tr>');continue}
    if((m=l.match(/^- (.*)/))){if(list!=='ul'){flush();list='ul';out.push('<ul>')}out.push(`<li>${inl(m[1])}</li>`);continue}
    if((m=l.match(/^\d+\. (.*)/))){if(list!=='ol'){flush();list='ol';out.push('<ol>')}out.push(`<li>${inl(m[1])}</li>`);continue}
    flush();out.push(`<p>${inl(l)}</p>`)}
  flush();return out.join('')}
$('#helpBtn').onclick=async()=>{const j=await (await fetch('/api/guide')).json();SEL=null;
  $('#panel').innerHTML=`<div class="p-top">${head('','Help')}</div><div class="p-sec md">${md(j.markdown)}</div>`;
  showDrawer('help');$('#drawer').scrollTop=0;render()};
load();
/* ?theme=light|dark forces a scheme (useful for screenshots); ?open=ID opens an item after load. */
(()=>{const t=new URLSearchParams(location.search).get('theme');if(t)document.documentElement.dataset.theme=t})();
</script></body></html>
"""


# ----------------------------------------------------------------------------- watcher for edits made outside the app

SELF_WRITE_UNTIL = [0.0]


def _snapshot() -> dict:
    out = {}
    if R.REG_DIR.exists():
        for p in R.REG_DIR.rglob("*.md"):
            try:
                out[str(p)] = p.stat().st_mtime
            except FileNotFoundError:
                pass
    return out


def watch_registers(interval: float = 5.0):
    """Every few seconds, if item files changed (and not by this server), regenerate 03/04/05 and commit.
    This is how Claude's session edits and any text-editor edits get the same treatment as web edits."""
    import time
    last = _snapshot()
    prev = None  # the previous poll's snapshot while a change is settling
    while True:
        time.sleep(interval)
        try:
            now = _snapshot()
            if now == last:
                prev = None
                continue
            if time.time() < SELF_WRITE_UNTIL[0]:
                last = now; prev = None
                continue
            if prev is None or now != prev:  # keep waiting until two consecutive polls agree
                prev = now
                continue
            changed = sorted({Path(k).stem for k in set(now) ^ set(last)} |
                             {Path(k).stem for k in now if k in last and now[k] != last[k]})
            with LOCK:
                R.regenerate_all()
                msg = git_commit("edit outside the web app: " + ", ".join(changed[:12]) + (" …" if len(changed) > 12 else ""))
            sys.stderr.write(f"[watch] regenerated for {len(changed)} changed item(s): {msg}\n")
            last = _snapshot(); prev = None
        except Exception as e:
            sys.stderr.write(f"[watch] error: {e}\n")


def main():
    os.chdir(R.ROOT)
    # Catch up on anything changed while the server was not running.
    with LOCK:
        R.regenerate_all()
        print("startup:", git_commit("startup: regenerate 03/04/05 from Registers/"))
    threading.Thread(target=watch_registers, daemon=True).start()
    srv = ThreadingHTTPServer((BIND, PORT), H)
    print(f"EOS Registers server on http://{BIND}:{PORT}  (root: {R.ROOT})")
    print("Auth:", "password required" if PASSWORD else "none (LAN open)")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
