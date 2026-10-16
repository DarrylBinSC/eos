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
import eos_pulse as P  # noqa: E402  (Operational Pulse, added 2026-10-16)

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
    "pulse": ["title", "status", "severity", "account", "product", "owner", "customer_visible", "next_action", "escalation", "escalation_test", "tags",
              "holder", "backup", "coverage", "exposure", "mitigation", "absence_date", "track"],
}
CLOSED_STATUSES = {"closed", "dropped", "aged_out"}
PULSE_DONE = {"resolved", "dropped"}


# ----------------------------------------------------------------------------- git

def git(*args) -> tuple[int, str]:
    try:
        p = subprocess.run(["git", *args], cwd=R.ROOT, capture_output=True, text=True, timeout=30)
        return p.returncode, (p.stdout + p.stderr).strip()
    except Exception as e:  # git missing, etc.
        return 1, str(e)


def git_commit_all(message: str) -> str:
    """Commit every tracked-text change in the EOS folder (code, docs, evidence), within .gitignore.
    Added 2026-10-16: session edits to Tools/ and the numbered files were sitting uncommitted because
    git_commit only adds Registers and the generated views."""
    if not (R.ROOT / ".git").exists():
        return "no git repo"
    git("add", "-A")
    rc, out = git("commit", "-q", "-m", message)
    return "committed" if rc == 0 else f"nothing to commit / {out[:120]}"


def git_commit(message: str) -> str:
    if not (R.ROOT / ".git").exists():
        return "no git repo"
    git("add", "-A", "--", "Registers", "03_Decision_Log.md", "04_Executive_Watch_List.md", "05_Commitments.md", "11_Operational_Pulse.md")
    rc, out = git("commit", "-q", "-m", message)
    return "committed" if rc == 0 else f"nothing to commit / {out[:120]}"


# ----------------------------------------------------------------------------- item ops

def item_json(meta, body, path):
    d = P.annotate(meta) if meta.get("kind") == "pulse" else dict(meta)
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
        if k in ("critical", "needs_triage", "customer_visible"):
            v = bool(v)
        if k in ("tags", "exposure") and isinstance(v, str):
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
    if kind == "pulse" and "status" in (patch or {}):
        if meta.get("status") in PULSE_DONE and not meta.get("closed_date"):
            meta["closed_date"] = today
            meta["closed_by"] = meta.get("closed_by") or f"Darryl, EOS web app, {today}"
        elif meta.get("status") == "live":
            meta["closed_date"] = ""; meta["closed_by"] = ""
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
        if u.path == "/api/pulse":
            with LOCK:
                return self._json(200, P.summary())
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
        m = re.fullmatch(r"/api/pulse/([A-Za-z0-9_.-]+)/escalate", u.path)
        if m:
            try:
                with LOCK:
                    import time as _t; SELF_WRITE_UNTIL[0] = _t.time() + 12
                    out = P.escalate(m.group(1), d.get("decision", ""), d.get("note", ""), d.get("actor") or "Darryl, web")
                    R.regenerate_all()
                    what = f"escalated to {out['watch']}" if out.get("watch") else "left with the team"
                    git_commit(f"web: {m.group(1)} — {what}")
                return self._json(200, out)
            except KeyError:
                return self._json(404, {"error": "not found"})
            except ValueError as e:
                return self._json(400, {"error": str(e)})
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
:root{--bg:#f6f5f2;--card:#fff;--sunk:#efede8;--segOn:#fff;--ink:#1e2226;--ink2:#3c4249;--muted:#5f666e;--line:#e2dfd9;--line2:#eeece7;--acc:#2b5aa6;--accInk:#fff;--sel:#eef3fb;--red:#b23f2c;--grn:#2f7a47;--amb:#94600a;--ambFill:#f2c66e;--ambInk:#3a2600;--shadow:0 1px 2px rgba(0,0,0,.12);--scrim:rgba(20,22,26,.32)}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#16181b;--card:#1d2024;--sunk:#26292e;--segOn:#3a3f46;--ink:#ecebe7;--ink2:#c8c6c1;--muted:#9ca1a8;--line:#33373d;--line2:#272a2f;--acc:#94b5ec;--accInk:#0f1520;--sel:#232b37;--red:#f2917f;--grn:#7cc896;--amb:#e8b762;--ambFill:#e8b762;--ambInk:#1e1607;--shadow:0 1px 2px rgba(0,0,0,.5);--scrim:rgba(0,0,0,.55)}}
:root[data-theme=dark]{--bg:#16181b;--card:#1d2024;--sunk:#26292e;--segOn:#3a3f46;--ink:#ecebe7;--ink2:#c8c6c1;--muted:#9ca1a8;--line:#33373d;--line2:#272a2f;--acc:#94b5ec;--accInk:#0f1520;--sel:#232b37;--red:#f2917f;--grn:#7cc896;--amb:#e8b762;--ambFill:#e8b762;--ambInk:#1e1607;--shadow:0 1px 2px rgba(0,0,0,.5);--scrim:rgba(0,0,0,.55)}
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
.t-sev.high{color:var(--red)}.t-sev.medium,.t-sev.medium-high{color:var(--amb)}
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
/* pulse (2026-10-16) */
.pwrap{display:flex;flex-direction:column;gap:14px}
.pintro{font-size:13.5px;color:var(--muted);margin:2px 2px 0;line-height:20px;max-width:900px}
.chips{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.chip{border:1px solid var(--line);background:var(--card);border-radius:14px;padding:3px 10px;font-size:13px;color:var(--ink2)}
.chip b{font-weight:600;color:var(--ink)}.chip.x{cursor:pointer;color:var(--acc)}
.hgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px}
.hcard{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;cursor:pointer;text-align:left;width:100%}
.hcard.on{outline:2px solid var(--acc)}
.hcard .top{display:flex;align-items:baseline;gap:10px}.hcard .acct{font-weight:650;font-size:15px}
.hcard .pin{font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
.score{font-size:34px;line-height:38px;font-weight:700;font-variant-numeric:tabular-nums;margin-top:6px}
.band{font-size:13px;font-weight:600}
.b-green{color:var(--grn)}.b-amber{color:var(--amb)}.b-red{color:var(--red)}
.comp{margin-top:6px;font-size:12.5px;color:var(--muted);line-height:18px}
.fgrid2{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px;padding:0 16px 14px}
.fcard{border:1px solid var(--line2);border-radius:8px;padding:10px 12px;background:var(--bg);cursor:pointer;text-align:left}
.fcard.on{outline:2px solid var(--acc)}.fcard.zero .fn,.fcard.zero .fs{color:var(--muted)}
.fcard .fn{font-weight:600;font-size:14px}.tcard{background:var(--card);border-color:var(--line)}.score .of{font-size:15px;font-weight:600;color:var(--muted);margin-left:3px}.fcard .fg{font-size:12px;color:var(--muted);margin-top:2px}
.fcard .fs{font-size:12.5px;color:var(--ink2);margin-top:6px;font-variant-numeric:tabular-nums}
.fcard .ag{margin-top:6px;font-size:12.5px;color:var(--acc);background:none;border:0;padding:0}
.prow{grid-template-columns:48px minmax(0,1fr) 150px;grid-template-areas:"id body due"}
.row.dim .title{color:var(--muted)}
.ppl{display:grid;grid-template-columns:minmax(0,1fr) 56px 68px 78px 52px minmax(0,1.3fr);gap:10px;padding:9px 16px;border-top:1px solid var(--line2);font-size:13.5px;cursor:pointer;align-items:baseline}
.ppl.h{cursor:default;font-size:11.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);font-weight:650}
.ppl:not(.h):hover{background:var(--bg)}.ppl.on{background:var(--sel)}
.ppl .num{font-variant-numeric:tabular-nums;text-align:right}.ppl .fl{color:var(--muted);font-size:12.5px}.ppl .hot{color:var(--amb);font-weight:650}
.t-cv{color:var(--ink2);font-weight:600}.t-stuck{background:var(--ambFill);color:var(--ambInk);padding:1px 7px;border-radius:4px;font-weight:600}.t-esc{color:var(--acc);font-weight:600}
.cand{display:grid;grid-template-columns:48px minmax(0,1fr) auto;gap:14px;padding:11px 16px;border-top:1px solid var(--line2);align-items:start}
.cand .why{font-size:13px;color:var(--muted);margin-top:3px}.cand .acts{display:flex;gap:8px;flex-wrap:wrap}
.cap .hs{font-weight:700}.cap b.b-red{color:var(--red)}.cap b.b-amber{color:var(--amb)}.cap b.b-green{color:var(--grn)}
.fempty{padding:0 16px 14px;font-size:13px;color:var(--muted);line-height:20px}.fempty a{cursor:pointer}.cap[data-pf],.cap[data-pv]{cursor:pointer}
.p-esc{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px;align-items:center}.p-esc .why{font-size:13px;color:var(--muted);flex-basis:100%}
/* sorting (2026-10-16) */
.sortbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:0 2px 10px;font-size:13px;color:var(--muted)}
.sortbar select{height:30px;border:1px solid var(--line);border-radius:6px;background:var(--card);padding:0 8px;margin-left:6px;font-size:13px;color:var(--ink)}
.btn.sm{height:30px;padding:0 10px;font-size:13px}.sortbar .sd{flex:1;min-width:220px}
.kcov{font-weight:650}.xp{border:1px solid var(--line);border-radius:4px;padding:0 6px;font-size:11.5px;color:var(--ink2)}
.kstrip{display:flex;gap:16px;flex-wrap:wrap;padding:0 16px 10px;font-size:13px}.kstrip b{font-variant-numeric:tabular-nums}
.gnote{margin:0;padding:0 16px 10px;font-size:13px;color:var(--muted);line-height:19px}
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
 .prow{grid-template-columns:minmax(0,1fr) auto;grid-template-areas:"id due" "body body"}
 .ppl{grid-template-columns:minmax(0,1fr) 44px 58px 66px 40px}.ppl .fl{display:none}
 .sortbar{margin:0 16px 10px}.sortbar select{height:40px;font-size:16px}.btn.sm{height:40px;font-size:15px}
 .cand{grid-template-columns:minmax(0,1fr)}.cand .id{display:none}.cand .acts .btn{flex:1}
 .score{font-size:30px}
 .pintro,.chips{margin-left:16px;margin-right:16px}.hgrid{padding:0 16px}
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
let ITEMS=[],TODAY='',VIEW='triage',Q='',SEL=null,MOREW=false,DRAWER=null,PULSE=null,PF={},PALL=false;
const BASE={},SESSION=[],SAVED={};
const CLOSED=new Set(['closed','dropped','aged_out']);
const isOpen=i=>!CLOSED.has(i.status)&&i.tier!=='retired';
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const plain=s=>String(s??'').replace(/\*\*([^*]+)\*\*/g,'$1').replace(/`([^`]+)`/g,'$1').replace(/~~([^~]+)~~/g,'$1');
let toastT;function toast(t){const e=$('#toast');e.textContent=t;e.style.display='block';clearTimeout(toastT);toastT=setTimeout(()=>e.style.display='none',2200)}
async function load(){const [j,p]=await Promise.all([fetch('/api/items').then(r=>r.json()),fetch('/api/pulse').then(r=>r.ok?r.json():null).catch(()=>null)]);ITEMS=j.items;TODAY=j.today;PULSE=p;render();const o=new URLSearchParams(location.search).get('open');if(o&&!DRAWER)openDrawer(o)}

const VIEWS=[['triage','Triage'],['pulse','Pulse'],['A','Mine'],['other','Other-owned'],['watch','Watch'],['decision','Decisions'],['needs','Needs triage'],['closed','Disposed']];
const MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],WD=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
const dn=s=>{const[y,m,d]=s.split('-').map(Number);return Date.UTC(y,m-1,d)};
const days=s=>Math.round((dn(s)-dn(TODAY))/864e5);
const fmt=s=>{if(!/^\d{4}-\d{2}-\d{2}/.test(s||''))return esc(s||'');const[y,m,d]=s.split('-').map(Number);return MON[m-1]+' '+d+(y!==+TODAY.slice(0,4)?', '+y:'')};
const cap=s=>s?s.charAt(0).toUpperCase()+s.slice(1).replace('_',' '):'';
function dueKey(i){return i.due||i.forum_date||'9999'}
function inView(i,v){
  if(v==='pulse')return i.kind==='pulse'&&i.category!=='knowledge'&&i._state==='live';
  if(v==='triage')return isOpen(i)&&((i.kind==='action'&&(i.register==='A'||i.register==='triage'||i.critical))||(i.kind==='watch'&&i.tier==='active')||(i.kind==='decision'&&i.tier==='radar'));
  if(v==='A')return isOpen(i)&&i.kind==='action'&&i.register==='A';
  if(v==='other')return isOpen(i)&&i.kind==='action'&&i.register==='other';
  if(v==='watch')return isOpen(i)&&i.kind==='watch';
  if(v==='decision')return isOpen(i)&&i.kind==='decision';
  if(v==='needs')return !!i.needs_triage;
  if(v==='closed')return !isOpen(i)&&i.kind!=='pulse';
}
/* ---------- sorting (2026-10-16): every list has a visible, stated order; choice remembered per view ---------- */
const SORTS={
 triage:{def:'urgency',opts:[['urgency','Urgency (default)'],['id','ID'],['due','Due / forum date'],['sev','Severity'],['touched','Last touched']]},
 pulse:{def:'pulse',opts:[['pulse','Attention (default)'],['id','ID'],['sev','Severity'],['seen','Last raised'],['first','First raised'],['owner','Owner'],['title','Title']]},
 A:{def:'due',opts:[['due','Due date'],['id','ID'],['title','Title'],['touched','Last touched']]},
 other:{def:'due',opts:[['due','Due date'],['id','ID'],['owner','Owner'],['crit','Critical first'],['title','Title'],['touched','Last touched']]},
 watch:{def:'id',opts:[['id','ID'],['sev','Severity'],['tier','Tier (Active first)'],['title','Title'],['touched','Last touched']]},
 decision:{def:'id',opts:[['id','ID'],['tier','Tier (Radar first)'],['due','Forum date'],['owner','Owner'],['title','Title'],['touched','Last touched']]},
 needs:{def:'id',opts:[['id','ID'],['touched','Last touched']]},
 closed:{def:'closed',opts:[['closed','Date disposed'],['id','ID'],['title','Title']]},
};
const SORTDESC={urgency:'grouped by urgency; within each group by due date, risks by severity, ties by ID',pulse:'live first, then stuck, then severity, then most recently raised'};
let SORT={};try{SORT=JSON.parse(localStorage.getItem('eos.sort')||'{}')}catch(e){SORT={}}
function defDir(k){return (k==='touched'||k==='closed'||k==='seen'||k==='first')?-1:1}
function sortOf(v){const c=SORTS[v],s=SORT[v];if(!c)return {k:'id',dir:1};return s&&c.opts.some(o=>o[0]===s.k)?s:{k:c.def,dir:defDir(c.def)}}
function saveSort(){try{localStorage.setItem('eos.sort',JSON.stringify(SORT))}catch(e){}}
const idKey=s=>{const m=String(s||'').match(/^([A-Za-z]+)-?(\d*)(.*)$/);return m?[m[1].toUpperCase(),m[2]?+m[2]:-1,m[3]]:[String(s||''),-1,'']};
function cmpId(x,y){const a=idKey(x.id),b=idKey(y.id);return a[0].localeCompare(b[0])||(a[1]-b[1])||a[2].localeCompare(b[2])}
const SEVR={'high':0,'medium-high':1,'medium':2,'low':3};
const sevr=i=>SEVR[String(i.severity||'').toLowerCase()]??9;
const dkey=i=>i.due||i.forum_date||'';
function blankLast(a,b,dir){a=String(a||'');b=String(b||'');if(!a&&!b)return 0;if(!a)return 1;if(!b)return -1;return a.localeCompare(b)*dir}
function cmpBy(k,dir){
  return (x,y)=>{let r=0;
    if(k==='id')r=cmpId(x,y)*dir;
    else if(k==='title')r=String(x.title||'').localeCompare(String(y.title||''))*dir;
    else if(k==='sev')r=(sevr(x)-sevr(y))*dir;
    else if(k==='due')r=blankLast(dkey(x),dkey(y),dir);
    else if(k==='touched')r=blankLast(x.last_touched,y.last_touched,dir);
    else if(k==='closed')r=blankLast(x.closed_date,y.closed_date,dir);
    else if(k==='seen')r=blankLast(x.last_seen,y.last_seen,dir);
    else if(k==='first')r=blankLast(x.first_seen,y.first_seen,dir);
    else if(k==='owner')r=blankLast(x.owner,y.owner,dir);
    else if(k==='crit')r=((y.critical?1:0)-(x.critical?1:0))*dir;
    else if(k==='tier'){const t={active:0,radar:0,passive:1,backlog:1,retired:2};r=((t[x.tier]??3)-(t[y.tier]??3))*dir}
    return r||cmpId(x,y)}}
function sortBar(v,n){const c=SORTS[v];if(!c)return '';const s=sortOf(v);
  const fixed=!!SORTDESC[s.k];const dated=['due','touched','closed','seen','first','owner'].includes(s.k);
  const desc=SORTDESC[s.k]||((s.dir>0?'ascending':'descending')+(dated?', blanks last':'')+', ties by ID');
  return `<div class="sortbar"><label>Sort<select id="sortSel" aria-label="Sort by">${c.opts.map(o=>`<option value="${o[0]}"${o[0]===s.k?' selected':''}>${o[1]}</option>`).join('')}</select></label>${fixed?'':`<button type="button" class="btn sm" id="sortDir" aria-label="Reverse the order">${s.dir>0?'↑ Ascending':'↓ Descending'}</button>`}<span class="sd">${n} shown · ${esc(desc)}</span></div>`}
document.addEventListener('change',e=>{if(e.target&&e.target.id==='sortSel'){SORT[VIEW]={k:e.target.value,dir:defDir(e.target.value)};saveSort();render()}});
function filtered(){
  /* membership uses the item as it was before this session's edits, so a row you just closed stays put (struck through) until you switch views */
  let a=ITEMS.filter(i=>inView(BASE[i.id]||i,VIEW));
  if(Q){const q=Q.toLowerCase();a=a.filter(i=>[i.id,i.title,i.owner,i.counterparty,i.next_action,i.body,i.forum,i.critical?'critical':'',i.severity,i.type].join(' ').toLowerCase().includes(q))}
  const kr={action:0,watch:1,decision:2};const rr={triage:0,A:1,other:2};
  const so=sortOf(VIEW);
  if(so.k!=='urgency'){a.sort(cmpBy(so.k,so.dir));return a}
  a.sort((x,y)=>(x.needs_triage?-1:0)-(y.needs_triage?-1:0)||(kr[x.kind]-kr[y.kind])||((rr[x.register]??3)-(rr[y.register]??3))||((y.critical?1:0)-(x.critical?1:0))||dueKey(x).localeCompare(dueKey(y))||(x.last_touched||'').localeCompare(y.last_touched||''));
  return a;
}
function groups(a){
  if(VIEW!=='triage'){const l=Q?'Search results':VIEWS.find(v=>v[0]===VIEW)[1];return [{k:'',l,rows:a}]}
  const g={tri:[],over:[],week:[],later:[],nodate:[],watch:[]};
  for(const i of a){
    if(i.needs_triage){g.tri.push(i);continue}
    if(i.kind==='watch'){g.watch.push(i);continue}
    const d=i.due||i.forum_date;if(!d){g.nodate.push(i);continue}
    const n=days(d);(n<0?g.over:n<7?g.week:g.later).push(i);
  }
  const so=sortOf('triage'),cf=so.k==='urgency'?null:cmpBy(so.k,so.dir);
  for(const k of ['over','week','later'])g[k].sort(cf||((x,y)=>dueKey(x).localeCompare(dueKey(y))||cmpId(x,y)));
  if(cf){g.tri.sort(cf);g.nodate.sort(cf)}
  g.watch.sort(cf||((x,y)=>(sevr(x)-sevr(y))||cmpId(x,y)));
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
function statusOpts(i){return i.kind==='pulse'?['status',['live','resolved'],i.status||'live']:i.kind==='action'?['status',['open','closed','dropped'],i.status]:i.kind==='watch'?['tier',['active','passive','retired'],i.tier]:['tier',['radar','backlog'],i.tier]}
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
  $('#meta').innerHTML=m('Register A','A',A,15)+m('Watch active','Watch',W,20)+m('Radar','Radar',D,20)+pulseCaps()+`<div class="cap"><span class="dot"></span><span class="l">Needs triage</span><span class="s">Triage</span><b>${N}</b></div><span class="today">${a.length} shown · ${['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][dt.getUTCDay()]}, ${fmt(TODAY)}</span>`;
  $('#logBtn').innerHTML='Changes'+(SESSION.length?`<span class="badge">${SESSION.length}</span>`:'');
  if(VIEW==='pulse'){$('#list').innerHTML=pulseHtml();return}
  const gs=groups(a);
  $('#list').innerHTML=sortBar(VIEW,a.length)+(gs.map(g=>{let rows=g.rows,more='';
    if(g.k==='watch'&&rows.length>3){more=`<button class="more" data-more>${MOREW?'Show fewer':'Show '+(rows.length-3)+' more risks'}</button>`;if(!MOREW)rows=rows.slice(0,3)}
    return `<section class="group"><h2 class="ghead ${g.k}">${g.l}<span class="n">${g.rows.length}</span></h2>${rows.map(rowHtml).join('')}${more}</section>`}).join('')||'<div class="empty">Nothing here.</div>');
}
document.addEventListener('click',e=>{
  const s=e.target.closest('.seg button');if(s){e.stopPropagation();const i=ITEMS.find(x=>x.id===s.dataset.id);if(i&&i[s.dataset.k]!==s.dataset.val)patch(s.dataset.id,{[s.dataset.k]:s.dataset.val},'');return}
  const c=e.target.closest('.tab[data-v]');if(c){VIEW=c.dataset.v;MOREW=false;for(const k in BASE)delete BASE[k];render();scrollTo(0,0);return}
  if(e.target.closest('[data-more]')){MOREW=!MOREW;render();return}
  const es=e.target.closest('[data-esc]');if(es){e.stopPropagation();escalateP(es.dataset.id,es.dataset.esc);return}
  const ag=e.target.closest('[data-agenda]');if(ag){e.stopPropagation();openAgenda(ag.dataset.agenda);return}
  const op=e.target.closest('[data-open]');if(op){e.preventDefault();openDrawer(op.dataset.open);return}
  if(e.target.closest('[data-pclear]')){PF={};render();return}
  if(e.target.closest('#sortDir')){const so=sortOf(VIEW);SORT[VIEW]={k:so.k,dir:-so.dir};saveSort();render();return}
  if(e.target.closest('[data-pall]')){PALL=!PALL;render();return}
  if(e.target.closest('[data-kall]')){KALL=!KALL;render();return}
  if(e.target.closest('[data-pv]')){VIEW='pulse';PF={};render();scrollTo(0,0);return}
  const pf=e.target.closest('[data-pf]');if(pf){const k=pf.dataset.pf,v=pf.dataset.val;const fromCap=!!pf.closest('#meta');PF=(!fromCap&&PF[k]===v)?{}:{[k]:v};VIEW='pulse';render();if(fromCap)scrollTo(0,0);else{const c=document.querySelector('.chips');if(c){c.scrollIntoView({block:'start'});scrollBy(0,-110)}}return}
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
  if(j.kind==='pulse')fetch('/api/pulse').then(r=>r.json()).then(p=>{PULSE=p;render()}).catch(()=>{});
  const what=[...Object.keys(p).filter(f=>String(p[f])!==String(BASE[id][f]??'')||f==='status'||f==='tier').map(f=>(f==='status'||f==='tier')?cap(p[f]):f.replace('_',' ')),note&&note.trim()?'note':''].filter(Boolean).join(', ')||'saved';
  SESSION.unshift({id,what,t:new Date().toLocaleTimeString([], {hour:'numeric',minute:'2-digit'})});
  SAVED[id]=SESSION[0];
  toast('Saved · '+id+' · '+what);render();
  if(DRAWER==='item'&&SEL===id)openDrawer(id);
  return j;
}
/* ---------- pulse (2026-10-16) ---------- */
const BANDCLS={green:'b-green',amber:'b-amber',red:'b-red'};
const fname=k=>((PULSE&&PULSE.forums)||[]).find(f=>f.key===k)?.name||k||'Unassigned forum';
function pulseCaps(){if(!PULSE)return '';const d=(PULSE.health||[]).find(h=>h.pinned);const c=(PULSE.candidates||[]).length;
  return (d?`<div class="cap" data-pf="account" data-val="${esc(d.account)}"><span class="l">${esc(d.account)} health score</span><span class="s">${esc(d.account)}</span><b class="hs ${BANDCLS[d.band]}">${d.score}/100</b></div>`:'')+
   `<div class="cap" data-pv="1"><span class="l">Pulse calls</span><span class="s">Calls</span><b${c?' class="hs b-amber"':''}>${c}</b></div>`}
function ptags(i){let t='';
  if(i.severity)t+=`<span class="t-sev ${esc(String(i.severity).toLowerCase())}">${esc(i.severity)}</span>`;
  if(i.customer_visible)t+='<span class="t-cv">Customer-visible</span>';
  if(i._stuck)t+='<span class="t-stuck">Stuck</span>';
  if(i.escalated_to)t+=`<span class="t-esc">Escalated · ${esc(i.escalated_to)}</span>`;else if(i._candidate)t+='<span class="t-esc">Needs your call</span>';
  if(i._state!=='live')t+=`<span>${cap(i._state)}</span>`;
  return t}
function prow(i){const c=i.next_action?plain(i.next_action):context(i).t;const cls=i._state==='live'?'':i._state==='quiet'?' dim':' done';
  return `<div class="row prow${SEL===i.id?' sel':''}${cls}" data-id="${esc(i.id)}"><div class="id">${esc(i.id)}</div>
   <div class="body"><div class="title">${esc(i.title)}</div>${c?`<div class="next ctx">${esc(c)}</div>`:''}<div class="meta">${ptags(i)}<span>${esc([i.account,fname(i.forum),i.owner?'Owner: '+i.owner:'No owner named'].filter(Boolean).join(' · '))}</span></div></div>
   <div class="due"><b>${fmt(i.last_seen||i.first_seen)}</b><span>${i.sightings||1}× since ${fmt(i.first_seen)}</span></div></div>`}
function pulseHtml(){
  if(!PULSE)return '<div class="empty">The Pulse did not load. Restart the EOS server so it picks up the new version.</div>';
  const P=PULSE,all=ITEMS.filter(i=>i.kind==='pulse'&&i.category!=='knowledge'),know=ITEMS.filter(i=>i.kind==='pulse'&&i.category==='knowledge');
  const fk=Object.keys(PF)[0],fv=fk?PF[fk]:null;
  const trk=fk==='track'?((P.tracks||[]).find(t=>t.key===fv)||{forums:[]}):null;
  const match=i=>!fk||(fk==='account'?i.account===fv:fk==='forum'?i.forum===fv:fk==='track'?trk.forums.includes(i.forum):(i._people||[]).includes(fv));
  const scope=all.filter(match);
  let a=scope.filter(i=>PALL||i._state==='live');
  if(Q){const q=Q.toLowerCase();a=a.filter(i=>[i.id,i.title,i.owner,i.account,i.body,(i.people||[]).join(' ')].join(' ').toLowerCase().includes(q))}
  const sv={high:0,medium:1,low:2},st={live:0,quiet:1,resolved:2,dropped:3};
  const pso=sortOf('pulse');
  if(pso.k!=='pulse')a.sort(cmpBy(pso.k,pso.dir));else a.sort((x,y)=>(st[x._state]-st[y._state])||((y._stuck?1:0)-(x._stuck?1:0))||((sv[String(x.severity||'').toLowerCase()]??3)-(sv[String(y.severity||'').toLowerCase()]??3))||String(y.last_seen||'').localeCompare(String(x.last_seen||'')));
  let h=`<div class="pwrap"><p class="pintro">Rolling ${P.window.days}-day window, ${fmt(P.window.start)} to ${fmt(P.window.end)}: what your team-governed forums are carrying. Each team's own governance owns the work. Issues go quiet when the forum stops raising them; nothing here needs closing. Escalate only what needs you.</p>`;
  if(fk)h+=`<div class="chips"><span class="chip">Showing ${fk}: <b>${esc(fk==='forum'?fname(fv):fk==='track'?(trk.name||fv):fv)}</b></span><button type="button" class="chip x" data-pclear>Clear</button></div>`;
  h+=`<div class="hgrid">${P.health.map(x=>{const c=x.components;
    const parts=[c.live_high_visible?c.live_high_visible+' High customer-visible':'',c.live_high?c.live_high+' High internal':'',c.live_medium?c.live_medium+' Medium':'',c.live_low?c.live_low+' Low':'',c.stuck?c.stuck+' stuck':'',c.quiet?c.quiet+' quiet':'',c.candidate?c.candidate+' need your call':'',c.at_your_level?c.at_your_level+' on your registers':''].filter(Boolean).join(' · ')||'No live issues';
    const d=x.delta==null?'Trend starts once a week of history exists':((x.delta>0?'+':'')+x.delta+' since '+fmt(x.prior.date));
    return `<button type="button" class="hcard${fk==='account'&&fv===x.account?' on':''}" data-pf="account" data-val="${esc(x.account)}"><div class="top"><span class="acct">${esc(x.account)}</span>${x.pinned?'<span class="pin">Largest customer</span>':x.type==='internal'?'<span class="pin">Internal</span>':x.type==='partner'?'<span class="pin">Partner</span>':''}</div><div class="score ${BANDCLS[x.band]}">${x.score}<span class="of">/100</span></div><div class="band ${BANDCLS[x.band]}">${esc(x.label)} · health score</div><div class="comp">${esc(parts)}</div><div class="comp">${esc(d)}</div></button>`}).join('')}</div>${(P.quiet_accounts||[]).length?`<p class="pintro">No signals in the window: ${esc(P.quiet_accounts.join(', '))}. A tile appears when an account has a Pulse issue or an item on your registers.</p>`:''}${(P.unattributed||[]).length?`<p class="pintro">Not scored because it names more than one account: ${P.unattributed.map(u=>`<a data-open="${esc(u.id)}">${esc(u.id)}</a> (${esc(u.accounts.join(', '))})`).join('; ')}. Set its account to count it once.</p>`:''}`;
  const cs=P.candidates.filter(c=>{const i=ITEMS.find(z=>z.id===c.id);if(!i)return false;if(i.category==='knowledge')return !fk||(fk==='track'&&i.track===fv)||(fk==='person'&&i.holder===fv)||(fk==='account'&&i.account===fv);return match(i)});
  let mid=`<section class="group"><h2 class="ghead${cs.length?' tri':''}">Needs your call<span class="n">${cs.length}</span></h2>${cs.length?cs.map(c=>`<div class="cand"><div class="id">${esc(c.id)}</div><div><div class="title" data-open="${esc(c.id)}" style="cursor:pointer">${esc(c.title)}</div><div class="why">${esc(c.reason_text)} · ${c.category==='knowledge'?'Knowledge concentration':esc(fname(c.forum))}${c.account?' · '+esc(c.account):''}</div></div><div class="acts"><button type="button" class="btn primary" data-esc="escalate" data-id="${esc(c.id)}">Escalate</button><button type="button" class="btn" data-esc="decline" data-id="${esc(c.id)}">Leave with team</button></div></div>`).join(''):'<div class="empty" style="padding:16px">Nothing needs you this cycle.</div>'}</section>`;
  const hidden=scope.length-scope.filter(i=>i._state==='live').length;
  const foot=hidden||PALL?`<button type="button" class="more" data-pall>${PALL?'Show live only':'Include quiet and resolved ('+hidden+')'}</button>`:'';
  const sec=(t,rows,note,ft)=>`<section class="group"><h2 class="ghead">${t}<span class="n">${rows.length}</span></h2>${note?`<p class="gnote">${note}</p>`:''}${rows.map(prow).join('')||`<div class="empty" style="padding:16px">None in the Pulse.${fk==='account'||fk==='person'?' Anything on your registers is listed below.':''}</div>`}${ft||''}</section>`;
  if((P.tracks||[]).length)mid+=`<section class="group"><h2 class="ghead">Your weekly governance<span class="n">${P.tracks.length}</span></h2><div class="fgrid2">${P.tracks.map(t=>`<div class="fcard tcard${fk==='track'&&fv===t.key?' on':''}" data-pf="track" data-val="${esc(t.key)}" role="button" tabindex="0"><div class="fn">${esc(t.name)}</div><div class="fg">With ${esc((t.leads||[]).join(' and '))} · ${t.forums.length} forums</div><div class="fs">${t.live} live · ${t.new7} new this week · ${t.stuck} stuck · ${t.candidates} need your call${t.knowledge?' · '+t.knowledge+' knowledge risk'+(t.knowledge>1?'s':''):''}</div>${t.no_evidence?`<div class="fg">No evidence in the window from ${t.no_evidence} of ${t.forums.length} forums</div>`:''}<button type="button" class="ag" data-agenda="track:${esc(t.key)}">Weekly governance agenda</button></div>`).join('')}</div></section>`;
  const focus=fk==='account'||fk==='person';
  if(!focus)h+=mid;  /* filtered by an account or a person: their issues and register items come straight after the tiles */
  const linked=regLinked(P,fk,fv,scope.length);
  if(!(focus&&!scope.length&&linked)){
    h+=sortBar('pulse',a.length);
    if(fk==='person'){const own=a.filter(i=>(i._owners||[]).includes(fv)),inv=a.filter(i=>!(i._owners||[]).includes(fv));
      h+=sec(`Owned by ${esc(fv)}`,own,'')+sec(`${esc(fv)} named, someone else owns`,inv,`${esc(fv)} is named on these in the evidence (a statement, a commitment or a stated role) but is not the owner. The owner is on each row.`,foot)}
    else h+=sec(PALL?'All issues':'Live issues',a,'',foot);
  }
  h+=linked;
  if(focus)h+=mid;
  h+=knowHtml(know,fk,fv,trk);
  h+=`<section class="group"><h2 class="ghead">Team-governed forums<span class="n">${P.forums.length}</span></h2><div class="fgrid2">${P.forums.filter(f=>f.live||f.quiet).map(f=>`<div class="fcard${f.live?'':' zero'}${fk==='forum'&&fv===f.key?' on':''}" data-pf="forum" data-val="${esc(f.key)}" role="button" tabindex="0"><div class="fn">${esc(f.name)}</div><div class="fg">${esc(f.governance||'')} · ${esc(f.owner||'Owner TBC')}${f.confirmed===false?' · not yet confirmed':''}</div><div class="fs">${f.live} live · ${f.new7} new this week · ${f.stuck} stuck${f.quiet?' · '+f.quiet+' quiet':''}</div><button type="button" class="ag" data-agenda="${esc(f.key)}">Governance agenda</button></div>`).join('')}</div>${(()=>{const e=P.forums.filter(f=>!f.live&&!f.quiet),lk=f=>`<a data-agenda="${esc(f.key)}">${esc(f.name)}</a>${f.confirmed===false?'*':''}`,a=e.filter(f=>f.evidence_in_window),b=e.filter(f=>!f.evidence_in_window);return (a.length?`<div class="fempty">Evidence in the window, nothing raised: ${a.map(lk).join(', ')}.</div>`:'')+(b.length?`<div class="fempty">No evidence in the window, so silence here means nothing: ${b.map(f=>lk(f)+(f.last_evidence?' (last '+fmt(f.last_evidence)+')':' (never)')).join(', ')}.</div>`:'')+(e.some(f=>f.confirmed===false)?'<div class="fempty">* classification not yet confirmed.</div>':'')})()}</section>`;
  const pp=(fk==='person'?P.people.filter(r=>r.name===fv):P.people).slice(0,15);
  h+=`<section class="group"><h2 class="ghead">People carrying the most<span class="n">${P.people.length}</span></h2><p class="gnote">Owns: owner of a live Pulse issue. Involved: named in the evidence on a live issue, not the owner. Delegated: open delegated or awaited register items they own. Sole: knowledge areas they hold with no confirmed backup. Highlighted at 8 or more owned or delegated.</p><div class="ppl h"><span>Person</span><span class="num">Owns</span><span class="num">Involved</span><span class="num">Delegated</span><span class="num">Sole</span><span class="fl">Forums</span></div>${pp.map(r=>`<div class="ppl${fk==='person'&&fv===r.name?' on':''}" data-pf="person" data-val="${esc(r.name)}"><span class="${r.total>=8?'hot':''}">${esc(r.name)}</span><span class="num">${r.owns??r.pulse}</span><span class="num">${r.involved??0}</span><span class="num">${r.delegated}</span><span class="num${r.sole?' hot':''}">${r.sole||0}</span><span class="fl">${esc(r.forums.map(fname).join(', '))}</span></div>`).join('')}</section>`;
  return h+'</div>'}
const KCOV={none:['No backup','b-red'],unknown:['Backup unknown','b-amber'],partial:['Partly covered','b-amber'],covered:['Covered','b-green']};
const TRK=k=>((PULSE&&PULSE.tracks)||[]).find(t=>t.key===k)?.name||k||'';
function krow(i){const cov=KCOV[i.coverage||'unknown']||KCOV.unknown;const cls=i._state==='live'?'':i._state==='quiet'?' dim':' done';
  const sub=[i.holder?'Held by '+i.holder:'',i.backup?'Backup: '+i.backup:'No backup named',i.mitigation?'Mitigation: '+plain(i.mitigation):''].filter(Boolean).join(' · ');
  return `<div class="row prow${SEL===i.id?' sel':''}${cls}" data-id="${esc(i.id)}"><div class="id">${esc(i.id)}</div>
   <div class="body"><div class="title">${esc(i.title)}</div><div class="next ctx">${esc(sub)}</div><div class="meta"><span class="kcov ${cov[1]}">${cov[0]}</span>${(i.exposure||[]).map(x=>`<span class="xp">${esc(cap(String(x)))}</span>`).join('')}${i.absence_date?`<span>Away from ${fmt(i.absence_date)}</span>`:''}${i.escalated_to?`<span class="t-esc">Escalated · ${esc(i.escalated_to)}</span>`:i._candidate?'<span class="t-esc">Needs your call</span>':''}${i._state==='quiet'?'<span>Not seen in 45+ days</span>':''}<span>${esc(TRK(i.track))}</span></div></div>
   <div class="due"><b>${fmt(i.last_seen||i.first_seen)}</b><span>${i.sightings||1}× since ${fmt(i.first_seen)}</span></div></div>`}
let KALL=false;
function knowHtml(know,fk,fv,trk){
  let k=know.filter(i=>!fk||(fk==='person'?(i.holder===fv||(i.backup||'').includes(fv)):fk==='track'?i.track===fv:fk==='account'?i.account===fv:false));
  if(fk&&fk!=='person'&&fk!=='track'&&fk!=='account')return '';
  const live=k.filter(i=>i._state==='live'),quiet=k.filter(i=>i._state==='quiet');
  const cr={none:0,unknown:1,partial:2,covered:3};
  const rows=(KALL?k:live).slice().sort((a,b)=>((a._state==='live'?0:1)-(b._state==='live'?0:1))||((cr[a.coverage||'unknown']??1)-(cr[b.coverage||'unknown']??1))||((b._candidate?1:0)-(a._candidate?1:0))||String(b.last_seen||'').localeCompare(String(a.last_seen||'')));
  const n=c=>live.filter(i=>(i.coverage||'unknown')===c).length;
  const strip=`<div class="kstrip"><span class="b-red"><b>${n('none')}</b> no backup</span><span class="b-amber"><b>${n('unknown')}</b> backup unknown</span><span class="b-amber"><b>${n('partial')}</b> partly covered</span><span class="b-green"><b>${n('covered')}</b> covered</span></div>`;
  const foot=quiet.length||KALL?`<button type="button" class="more" data-kall>${KALL?'Show live only':'Include not seen in 45+ days ('+quiet.length+')'}</button>`:'';
  return `<section class="group"><h2 class="ghead">Knowledge concentration<span class="n">${live.length}</span></h2><p class="gnote">Where one person holds knowledge a customer, a release or a migration depends on. This is a different risk from load: the fix is a named backup, documentation or cross-training. Entries stay live for 45 days after the last evidence, because silence does not remove a single point of failure.</p>${strip}${rows.map(krow).join('')||'<div class="empty" style="padding:16px">None.</div>'}${foot}</section>`}
/* Items behind a tile or a person that live in the registers, not the Pulse (2026-10-16). Tap opens the item; the row says which register. */
function regLinked(P,fk,fv,nPulse){
  let ids=[],what='';
  if(fk==='account'){const h=(P.health||[]).find(x=>x.account===fv);ids=(h?h.register_items:[]).map(r=>r.id);
    what=`The items counted as "on your registers" in the ${esc(fv)} tile: Watch Active, your own actions, and Critical other-owned items that name ${esc(fv)}.`}
  else if(fk==='person'){const r=(P.people||[]).find(x=>x.name===fv);ids=(r?r.ids:[]).filter(id=>!/^[PK]\d/.test(id));
    what=`The open delegated or awaited items ${esc(fv)} owns, counted in the Delegated column.`}
  else return '';
  const rows=[...new Set(ids)].map(id=>ITEMS.find(i=>i.id===id)).filter(Boolean).sort(cmpId);
  if(!rows.length)return '';
  const lead=nPulse?'':`<b>No Pulse issues for ${esc(fv)}.</b> `;
  return `<section class="group"><h2 class="ghead">On your registers<span class="n">${rows.length}</span></h2><p class="gnote">${lead}${what} They live in your registers, not the Pulse; each row shows which one. Tap to open it here, or use the status buttons as you would on that tab.</p>${rows.map(rowHtml).join('')}</section>`}
function agendaMd(k){let it,L,multi=false;
  const wk=dn(TODAY)-7*864e5,fs=i=>dn(String(i.first_seen||TODAY).slice(0,10));
  if(k.startsWith('track:')){const t=(PULSE.tracks||[]).find(x=>x.key===k.slice(6))||{name:k,forums:[],leads:[]};multi=true;
    it=ITEMS.filter(i=>i.kind==='pulse'&&t.forums.includes(i.forum));
    L=[`# ${t.name}: weekly governance review, ${fmt(TODAY)}`,'',`With ${(t.leads||[]).join(' and ')}. Window ${fmt(PULSE.window.start)} to ${fmt(PULSE.window.end)}. Covers: ${t.forums.map(fname).join(', ')}.`,'']}
  else{const f=PULSE.forums.find(x=>x.key===k)||{name:k};it=ITEMS.filter(i=>i.kind==='pulse'&&i.forum===k);
    L=[`# ${f.name}: governance review, ${fmt(TODAY)}`,'',`Window ${fmt(PULSE.window.start)} to ${fmt(PULSE.window.end)}. Owner: ${f.owner||'TBC'}. Governance: ${f.governance||''}.`,'']}
  const ln=i=>`**${i.id}** ${plain(i.title)}${multi?' ['+fname(i.forum)+']':''}${i.owner?' (owner: '+i.owner+')':' (no owner named)'}${i.next_action?'. Next: '+plain(i.next_action).replace(/\.$/,''):''}`;
  const sec=(t,xs,line)=>{L.push('## '+t,'');if(xs.length)xs.forEach(i=>L.push('- '+(line||ln)(i)));else L.push('- None.');L.push('')};
  const live=it.filter(i=>i._state==='live');
  sec('Stuck: what unblocks it, who decides, by when',live.filter(i=>i._stuck));
  const kc=multi?ITEMS.filter(i=>i.kind==='pulse'&&i.category==='knowledge'&&i.track===k.slice(6)&&i._candidate):[];
  sec('Needs a decision or escalation',[...live.filter(i=>i._candidate&&!i._stuck),...kc],i=>(i.category==='knowledge'?`**${i.id}** ${plain(i.title)} (knowledge risk; held by ${i.holder||'?'})`:ln(i))+'. Test: '+(PULSE.tests[i._candidate]||i._candidate));
  sec('New this week',live.filter(i=>!i._stuck&&!i._candidate&&fs(i)>=wk));
  sec('Still open',live.filter(i=>!i._stuck&&!i._candidate&&fs(i)<wk));
  sec('Gone quiet: confirm resolved or still open',it.filter(i=>i._state==='quiet'));
  sec('Escalated to my registers',it.filter(i=>i.escalated_to),i=>`**${i.id}** ${plain(i.title)}, now ${i.escalated_to}`);
  if(multi){const t=k.slice(6);const kn=ITEMS.filter(i=>i.kind==='pulse'&&i.category==='knowledge'&&i.track===t&&i._state==='live'&&(i.coverage||'unknown')!=='covered');
    sec('Knowledge risks: who backs up whom, and by when',kn,i=>`**${i.id}** ${plain(i.title)}: held by ${i.holder||'?'}; backup ${i.backup||'none named'} (${(KCOV[i.coverage||'unknown']||KCOV.unknown)[0].toLowerCase()})${i.mitigation?'. Mitigation: '+plain(i.mitigation).replace(/\.$/,''):''}${i.absence_date?'. Away from '+fmt(i.absence_date):''}`)}
  return L.join('\n')}
function openAgenda(k){return openAgendaText(agendaMd(k))}
function openAgendaText(txt){SEL=null;
  $('#panel').innerHTML=`<div class="p-top">${head('','Governance agenda')}</div><div class="p-act"><button type="button" class="btn primary" id="cpy">Copy as text</button></div><div class="p-sec md">${md(txt)}</div>`;
  showDrawer('agenda');$('#drawer').scrollTop=0;
  $('#cpy').onclick=async()=>{try{await navigator.clipboard.writeText(txt.replace(/\*\*/g,''));toast('Copied')}catch(e){toast('Copy is blocked here; select the text instead')}};render()}
async function escalateP(id,decision){
  const r=await fetch('/api/pulse/'+encodeURIComponent(id)+'/escalate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({decision})});
  if(!r.ok){toast('Save failed · '+id);return}const j=await r.json();
  SESSION.unshift({id,what:j.watch?'escalated to '+j.watch:'left with team',t:new Date().toLocaleTimeString([], {hour:'numeric',minute:'2-digit'})});
  toast(j.watch?`${id} escalated · ${j.watch} is on your Watch list`:`${id} left with the team`);
  await load();if(DRAWER==='item'&&SEL===id)openDrawer(id)}
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
  }else if(i.kind==='pulse'&&i.category==='knowledge'){
    f+=field('Held by','holder',i.holder||'')+field('Backup (name, or blank)','backup',i.backup||'');
    f+=field('Coverage','coverage',i.coverage||'unknown','',['none','unknown','partial','covered'])+field('Exposure (comma list: customer, release, migration, support)','exposure',(i.exposure||[]).join(', '));
    f+=field('Absence or departure date (YYYY-MM-DD)','absence_date',i.absence_date||'')+field('Track','track',i.track||'','',['','delivery','development']);
    f+=field('Mitigation under way','mitigation',i.mitigation||'','text',null,true);
    f+=field('Status','status',i.status||'live','',['live','resolved','dropped'])+field('Escalation','escalation',i.escalation||'','',['','candidate','escalated','declined']);
    return f;
  }else if(i.kind==='pulse'){
    f+=field('Status','status',i.status||'live','',['live','resolved','dropped'])+field('Severity','severity',i.severity||'','',['','High','Medium','Low']);
    f+=field('Account','account',i.account||'')+field('Product','product',i.product||'');
    f+=field('Owner (team)','owner',i.owner||'')+field('Customer-visible','customer_visible',String(!!i.customer_visible),'',['false','true']);
    f+=field('Escalation','escalation',i.escalation||'','',['','candidate','escalated','declined'])+field('Escalation test','escalation_test',i.escalation_test||'','',['','asked','boundary','stuck','gap']);
    f+=field('Next action (one line)','next_action',i.next_action||'','text',null,true);
    return f;
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
  const reg=i.kind==='pulse'&&i.category==='knowledge'?'Knowledge concentration · '+TRK(i.track):i.kind==='pulse'?'Pulse · '+fname(i.forum)+(i.severity?' · '+i.severity:''):i.kind==='action'?(i.register==='A'?'Register A · Mine':i.register==='triage'?'New item':'Other-owned'+(i.type?' · '+i.type:'')):i.kind==='watch'?'Watch'+(i.severity?' · '+i.severity:''):'Decision · '+cap(i.tier);
  const d=dueInfo(i);const due=d.due?`${i.kind==='decision'?'Forum':'Due'} ${fmt(d.due)} · ${d.n<0?-d.n+' day'+(d.n===-1?'':'s')+' late':d.n===0?'today':'in '+d.n+' days'}`:(i.trigger?'No date · waits on: '+esc(i.trigger):'No due date');
  const pdue=i.kind==='pulse'&&i.category==='knowledge'?`${(KCOV[i.coverage||'unknown']||KCOV.unknown)[0]} · held by ${esc(i.holder||'?')} · evidence ${i.sightings||1}× since ${fmt(i.first_seen)} · last ${fmt(i.last_seen||i.first_seen)}`:i.kind==='pulse'?`Raised ${i.sightings||1}× · first ${fmt(i.first_seen)} · last ${fmt(i.last_seen||i.first_seen)} · ${cap(i._state)}${i._stuck?' · stuck':''}`:null;
  const pesc=i.kind!=='pulse'?'':i.escalated_to?`<div class="p-esc"><span class="why">On your Watch list as <a href="#" data-open="${esc(i.escalated_to)}">${esc(i.escalated_to)}</a>. The team still owns the work.</span></div>`:`<div class="p-esc">${i._candidate?`<span class="why">Needs your call: ${esc((PULSE&&PULSE.tests[i._candidate])||i._candidate)}</span>`:i.escalation==='declined'?'<span class="why">You left this with the team. You can still escalate it.</span>':'<span class="why">With the team. Escalate only if it needs you.</span>'}<button type="button" class="btn primary" data-esc="escalate" data-id="${esc(i.id)}">Escalate to my Watch list</button>${i.escalation==='declined'?'':`<button type="button" class="btn" data-esc="decline" data-id="${esc(i.id)}">Leave with team</button>`}</div>`;
  const nFields=(fields(i).match(/<label>/g)||[]).length;
  const sv=SAVED[id];
  $('#panel').innerHTML=`<div class="p-top">${head(i.id,esc(reg))}
     <h2 class="p-title">${esc(i.title)}</h2>
     ${i.next_action?`<div class="p-next">${esc(plain(i.next_action))}</div>`:''}
     <div class="p-due${d.cls==='late'&&!pdue?' late':''}">${pdue||due}${i.critical?' · <span class="t-crit">Critical</span>':''}</div></div>
   <form id="nf2" class="p-act">${seg(i,true)}${pesc}
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
    for(const [k,v] of fd.entries())p[k]=(k==='critical'||k==='needs_triage'||k==='customer_visible')?(v==='true'):v;
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


TOOLS = [Path(__file__).resolve().parent / n for n in ("eos_server.py", "eos_registers.py", "eos_pulse.py")]


def _tools_mtime() -> tuple:
    out = []
    for t in TOOLS:
        try:
            out.append(t.stat().st_mtime)
        except FileNotFoundError:
            out.append(0)
    return tuple(out)


def _restart_if_code_changed(start: tuple) -> None:
    """Added 2026-10-16: when Claude changes the server or Pulse code, restart in place so the web app shows it
    without Darryl quitting and relaunching. Waits for the files to settle and to compile before restarting."""
    import py_compile, time
    if _tools_mtime() == start:
        return
    time.sleep(3)
    try:
        for t in TOOLS:
            py_compile.compile(str(t), doraise=True)
    except Exception as e:
        sys.stderr.write(f"[watch] code changed but does not compile; not restarting: {e}\n")
        return
    with LOCK:
        msg = git_commit_all("code change: restart server with updated Tools/")
    sys.stderr.write(f"[watch] code changed ({msg}); restarting\n")
    os.execv(sys.executable, [sys.executable] + sys.argv)


def watch_registers(interval: float = 5.0):
    """Every few seconds, if item files changed (and not by this server), regenerate 03/04/05 and commit.
    This is how Claude's session edits and any text-editor edits get the same treatment as web edits."""
    import time
    last = _snapshot()
    code_start = _tools_mtime()
    prev = None  # the previous poll's snapshot while a change is settling
    while True:
        time.sleep(interval)
        try:
            _restart_if_code_changed(code_start)
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
        print("startup:", git_commit_all("startup: commit changes made while the server was not watching (code, docs, evidence)"))
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
