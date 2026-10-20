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


# ----------------------------------------------------------------------------- Copilot Pulse prompts (added 2026-10-19)
# Two prompts, one per governance track, so a run never asks Copilot for all 13 forums at once (the 10-19 catch-up run
# was throttled on five of them). Each prompt names itself ("PROMPT 1 OF 2, DELIVERY TRACK") in the text and asks
# Copilot to repeat that header in its answer, so a pasted result always says which prompt produced it.

PROMPT_TRACKS = [(1, "delivery", "Delivery track"), (2, "development", "Development track")]
CADENCE_DAYS = {"daily": 0, "weekly": 7, "bi-weekly": 14, "biweekly": 14}


def _forum_due(f: dict, today: dt.date) -> tuple[bool, str]:
    """A forum needs a sweep when its newest evidence is older than its cadence allows. Daily forums need today's."""
    last = f.get("last_evidence") or ""
    cad = (f.get("cadence") or "").strip().lower()
    if not last:
        return True, "never heard"
    try:
        d = dt.date.fromisoformat(last[:10])
    except ValueError:
        return True, "never heard"
    allow = CADENCE_DAYS.get(cad, 30)
    age = (today - d).days
    if cad == "daily":
        return (age >= 1, f"last heard {last}")
    return (age > allow, f"last heard {last}")


def copilot_prompts(today: dt.date | None = None) -> dict:
    today = today or dt.date.today()
    forums = P.load_forums()
    issues = [m for m, _b, _p in R.load_items("pulse")]
    out = []
    for n, track, label in PROMPT_TRACKS:
        tf = [f for f in forums if f.get("track") == track]
        rows = []
        for f in tf:
            due, why = _forum_due(f, today)
            rows.append({"key": f.get("key"), "name": f.get("name"), "aliases": f.get("aliases") or [],
                         "cadence": f.get("cadence") or "", "due": due, "why": why})
        due_rows = [r for r in rows if r["due"]]
        starts = []
        for r in due_rows:
            last = next((f.get("last_evidence") or "" for f in tf if f.get("key") == r["key"]), "")
            starts.append(dt.date.fromisoformat(last[:10]) if last else today - dt.timedelta(days=8))
        start = max(today - dt.timedelta(days=8), min(starts)) if starts else today - dt.timedelta(days=7)
        keys = {f.get("key") for f in tf}
        tracked = []
        for m in issues:
            st = P.state(m, today)
            if st not in ("live", "quiet"):
                continue
            if P.is_knowledge(m):
                if (m.get("track") or "") != track:
                    continue
                tracked.append(f'{m["id"]} Knowledge held mainly by one person: {m.get("title","")} ({m.get("holder","")})')
            elif m.get("forum") in keys:
                acct = f' ({m.get("account")})' if m.get("account") else ""
                tracked.append(f'{m["id"]} {m.get("title","")}{acct}')
        text = _prompt_text(n, label, due_rows or rows, start, today, tracked)
        out.append({"n": n, "track": track, "label": label, "needed": bool(due_rows), "forums": rows,
                    "window": [start.isoformat(), today.isoformat()], "tracked": len(tracked), "text": text})
    need = [o for o in out if o["needed"]]
    if len(need) == 2:
        advice = "Run both: Prompt 1 and Prompt 2, each in its own new Copilot chat."
    elif len(need) == 1:
        o = need[0]
        other = [x for x in out if not x["needed"]][0]
        advice = f'Run Prompt {o["n"]} only ({o["label"]}). Prompt {other["n"]} is not needed: every {other["track"]} forum has been heard within its cadence.'
    else:
        advice = "Nothing needed: every forum has been heard within its cadence. Either prompt can still be copied."
    return {"today": today.isoformat(), "advice": advice, "prompts": out}


def _fixed_prompt(section_head: str) -> str:
    """The Daily and Weekly prompts live in 02_Copilot_Intake_Prompts.md (single source); serve its first code block."""
    f = R.ROOT / "02_Copilot_Intake_Prompts.md"
    try:
        txt = f.read_text(encoding="utf-8")
        s = txt.index(section_head)
        e = txt.find("\n## ", s + 5)
        m = re.search(r"```\n(.*?)\n```", txt[s:e if e > 0 else None], re.S)
        return m.group(1) if m else ""
    except (OSError, ValueError):
        return ""


def _last_package(kind: str) -> str:
    ev = R.ROOT / "Evidence"
    dates = []
    for f in ev.glob(f"M365_Evidence_{kind}_*.md") if ev.exists() else []:
        m = re.search(r"(\d{4}-?\d{2}-?\d{2})", f.name)
        if m:
            d = m.group(1)
            dates.append(d if "-" in d else f"{d[:4]}-{d[4:6]}-{d[6:]}")
    return max(dates) if dates else ""


def copilot_all(today: dt.date | None = None) -> dict:
    today = today or dt.date.today()
    monday = today.weekday() == 0
    weekend = today.weekday() >= 5
    pulse = copilot_prompts(today)
    ld, lw = _last_package("Daily"), _last_package("Weekly")
    fixed = [
        {"id": "weekly", "label": "Weekly prompt", "sub": "Leadership evidence, last 8 days. Mondays.",
         "today": monday, "last": lw, "done": lw == today.isoformat(),
         "text": _fixed_prompt("## 3. Weekly Prompt")},
        {"id": "daily", "label": "Daily prompt", "sub": "Leadership evidence, last 24 hours, plus the Daily Scrum and Daily Stand Up. Tuesday to Friday.",
         "today": not monday and not weekend, "last": ld, "done": ld == today.isoformat(),
         "text": _fixed_prompt("## 2. Daily Prompt")},
    ]
    if not monday:
        fixed.reverse()
    first = next((f for f in fixed if f["today"]), None)
    steps = []
    if first:
        steps.append(("done" if first["done"] else "todo", f'{first["label"]}' + (" (today's package is saved)" if first["done"] else "")))
    else:
        steps.append(("skip", "Weekend: no Daily or Weekly prompt today"))
    need = [o for o in pulse["prompts"] if o["needed"]]
    if need:
        steps.append(("todo", " and ".join(f'Pulse Prompt {o["n"]} ({o["label"]})' for o in need)
                      + (", each in its own new Copilot chat" if len(need) == 2 else "")))
    else:
        steps.append(("done", "Pulse prompts: nothing needed, every forum heard within its cadence"))
    return {"today": today.isoformat(), "weekday": today.strftime("%A"), "steps": steps, "fixed": fixed, "pulse": pulse}


def _prompt_text(n, label, rows, start, end, tracked) -> str:
    head = f"PROMPT {n} OF 2: PULSE SWEEP, {label.upper()}"
    fl = "\n".join(f'{i}. {r["name"]}' + (f' (aliases: {", ".join(r["aliases"])})' if r["aliases"] else "")
                   + (f' [{r["cadence"]}]' if r["cadence"] else "") for i, r in enumerate(rows, 1))
    tl = "\n".join(tracked) if tracked else "(none currently tracked for this track)"
    return f"""{head}

Begin your answer with this exact line: "{head}, window {start.isoformat()} to {end.isoformat()}".

ROLE
You are extracting operational evidence from Microsoft 365 for a senior technology leader. Be literal and complete. Do not summarize away detail, and do not invent anything. If you cannot find or open something, say so in the coverage table.

WINDOW
{start.isoformat()} through {end.isoformat()} inclusive.

FORUMS (search for each one separately, by name and alias, one at a time, in this order)
{fl}

For each forum: find every occurrence in the window (calendar, meeting recap, transcript, Loop or meeting notes, meeting chat). Open each transcript and Loop component and read it to the end; continue if it is truncated. Check whether each meeting was transcribed. Do not stop after the first forum that returns results. If a search is throttled, wait and retry once; if it fails again, mark that forum "throttled" in the coverage table and move on.

ISSUES ALREADY BEING TRACKED (report new mentions of these as sightings, not as new issues)
{tl}

OUTPUT, in this order

A. Coverage, one row per forum listed above (every row, even when nothing was found)
| Forum | Occurrences found (dates) | Transcribed? (yes/no per date) | Artifacts opened (transcript / Loop / recap / chat / invite only) | Status: raised issues / met, nothing raised / not found / throttled |

B. Sightings of tracked issues
| Issue ID | Date | Forum | Source type (transcript / Loop / recap / chat) | What was said (quote, and name the speaker as shown) | Named owner, if any | Stated status: worse / same / better / resolved (resolved only if someone says it outright) |

C. New issues (anything raised that is not on the tracked list)
| Date | Forum | Source type | Issue in one line | Account or site, only if named (do not guess the customer) | Product | Severity: High / Medium / Low | Customer-visible? yes/no, and the customer if named | Named owner (blank if none named) | People with a statement, commitment or stated role on it (not attendees) | Quote | Sessions in the window that raised it |

D. Calls for the leader (rows from B or C only)
Flag a row only if: the leader was named or asked for a decision, resource or escalation; it involves contract or money, a customer executive, what to tell a customer, or a team outside the forum; it has been raised for 10 or more business days without resolution; or no owner is named, or the customer appears unaware of a material problem. Give the row reference and which test it meets. Severity alone is not a test.

E. Knowledge concentration
Only where the evidence says someone is the go-to or only person on something, work is waiting on one person, or an absence or departure opens a gap. Being busy does not count.
| Person | Area | Evidence (quote) | Backup named? | Absence or departure date, if stated |

RULES
- Attendance is not ownership. Never name someone as owner unless the words assign it.
- Quote, do not paraphrase, for anything in B, C and E, and label each quote's source type.
- Sprint task updates (ticket moved, story points, individual task progress, code migration progress) are excluded unless they block a customer, a release, or another team. State how many you excluded per forum.
- If a meeting was not transcribed, say so and use only its chat, recap or notes.
- Absence of a result means the search did not find it, not that it did not happen. Say which.
"""


# ----------------------------------------------------------------------------- briefs (added 2026-10-19)

BRIEFS_DIR = R.ROOT / "Briefings"
BRIEF_NAME = r"\d{4}-\d{2}-\d{2}_[A-Za-z0-9_-]+\.md"   # dated briefs only; also blocks path traversal
BRIEF_VIEWS = R.ROOT / "Dashboard" / "brief_views.jsonl"   # gitignored; the usage test for the tab


def list_briefs() -> list[dict]:
    out = []
    for f in BRIEFS_DIR.glob("*.md"):
        if not re.fullmatch(BRIEF_NAME, f.name):
            continue
        stem = f.stem
        date, _, rest = stem.partition("_")
        low = rest.lower()
        kind = ("Weekly" if "weekly" in low else "Daily" if "daily" in low else "Baseline" if "baseline" in low
                else rest.replace("_", " ")[:24])
        title = ""
        try:
            for line in f.read_text(encoding="utf-8").splitlines():
                if line.startswith("# "):
                    title = line[2:].strip()
                    break
        except Exception:
            pass
        out.append({"name": f.name, "date": date, "kind": kind, "title": title,
                    "docx": f.with_suffix(".docx").exists(), "bytes": f.stat().st_size})
    out.sort(key=lambda b: (b["date"], b["kind"] == "Weekly"), reverse=True)
    return out


def log_brief_view(name: str, source: str) -> None:
    try:
        BRIEF_VIEWS.parent.mkdir(exist_ok=True)
        with BRIEF_VIEWS.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps({"at": dt.datetime.now().isoformat(timespec="seconds"), "brief": name,
                                 "from": source[:20]}) + "\n")
    except Exception:
        pass


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
        if u.path == "/api/copilot":
            with LOCK:
                return self._json(200, copilot_all())
        if u.path == "/api/pulse/prompts":
            with LOCK:
                return self._json(200, copilot_prompts())
        if u.path == "/api/pulse":
            with LOCK:
                return self._json(200, P.summary())
        if u.path == "/api/guide":
            g = R.ROOT / "Reference" / "Registers_App_User_Guide.md"
            txt = g.read_text(encoding="utf-8") if g.exists() else "# Guide not found\n\nExpected at Reference/Registers_App_User_Guide.md."
            return self._json(200, {"markdown": txt})
        if u.path == "/api/log":
            return self._json(200, {"log": recent_log(int(q.get("n", ["30"])[0]))})
        # Live refresh (added 2026-10-20): a cheap fingerprint of the item files and briefs. The page
        # polls it and re-fetches only when it changes, so a tab left open picks up edits made by
        # Claude sessions or by hand within about 30 seconds, and immediately when the tab regains focus.
        if u.path == "/api/version":
            return self._json(200, {"version": data_version()})
        # Briefs tab (added 2026-10-19): read-only view of Briefings/*.md, plus the Word copy when it exists.
        if u.path == "/api/briefs":
            return self._json(200, {"briefs": list_briefs(), "today": R.today()})
        m = re.fullmatch(r"/api/briefs/(" + BRIEF_NAME + r")", u.path)
        if m:
            f = BRIEFS_DIR / m.group(1)
            if not f.exists():
                return self._json(404, {"error": "not found"})
            log_brief_view(m.group(1), q.get("from", [""])[0])
            return self._json(200, {"name": f.name, "markdown": f.read_text(encoding="utf-8"),
                                    "docx": f.with_suffix(".docx").exists()})
        m = re.fullmatch(r"/briefs/(" + BRIEF_NAME[:-4] + r")\.docx", u.path)
        if m:
            f = BRIEFS_DIR / (m.group(1) + ".docx")
            if not f.exists():
                return self._json(404, {"error": "not found"})
            return self._send(200, f.read_bytes(),
                              "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
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
        if u.path == "/api/pulse/pin":
            acct = (d.get("account") or "").strip()
            try:
                with LOCK:
                    P.set_pinned(acct)
                    R.regenerate_all()
                    git_commit(f"web: pinned account -> {acct}")
                    return self._json(200, P.summary())
            except KeyError:
                return self._json(404, {"error": "unknown account"})
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
:root{--bg:#f6f5f2;--card:#fff;--sunk:#efede8;--segOn:#fff;--ink:#1e2226;--ink2:#3c4249;--muted:#5f666e;--line:#e2dfd9;--line2:#eeece7;--acc:#2b5aa6;--accInk:#fff;--sel:#eef3fb;--red:#b23f2c;--grn:#2f7a47;--hatch:#a8a39a;--barT:#3c4249;--barR:#8ea6d0;--amb:#94600a;--ambFill:#f2c66e;--ambInk:#3a2600;--shadow:0 1px 2px rgba(0,0,0,.12);--scrim:rgba(20,22,26,.32)}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#16181b;--card:#1d2024;--sunk:#26292e;--segOn:#3a3f46;--ink:#ecebe7;--ink2:#c8c6c1;--muted:#9ca1a8;--line:#33373d;--line2:#272a2f;--acc:#94b5ec;--accInk:#0f1520;--sel:#232b37;--red:#f2917f;--grn:#7cc896;--hatch:#6b7078;--barT:#d9d7d2;--barR:#4d6797;--amb:#e8b762;--ambFill:#e8b762;--ambInk:#1e1607;--shadow:0 1px 2px rgba(0,0,0,.5);--scrim:rgba(0,0,0,.55)}}
:root[data-theme=dark]{--bg:#16181b;--card:#1d2024;--sunk:#26292e;--segOn:#3a3f46;--ink:#ecebe7;--ink2:#c8c6c1;--muted:#9ca1a8;--line:#33373d;--line2:#272a2f;--acc:#94b5ec;--accInk:#0f1520;--sel:#232b37;--red:#f2917f;--grn:#7cc896;--hatch:#6b7078;--barT:#d9d7d2;--barR:#4d6797;--amb:#e8b762;--ambFill:#e8b762;--ambInk:#1e1607;--shadow:0 1px 2px rgba(0,0,0,.5);--scrim:rgba(0,0,0,.55)}
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
/* Pulse redesign 2026-10-16 (Claude Design handoff, Phase 1). Classes prefixed pv- are Pulse-only. */
.pv{display:flex;flex-direction:column;gap:16px}
.pv .group{margin-bottom:0}
.pv-col{display:flex;flex-direction:column;gap:16px;min-width:0}
.pv-g2{display:grid;grid-template-columns:minmax(0,1fr) 470px;gap:16px;align-items:start}
.pv-g3{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;align-items:start}
.pv-title{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;padding:0 2px}
.pv-title h2{font-size:20px;font-weight:650;margin:0}
.pv-title p{margin:0;font-size:14px;color:var(--ink2);flex:1;min-width:260px}
.pv-lk{font-size:13.5px;color:var(--acc);background:none;border:0;padding:0;cursor:pointer}
.pv-today{display:grid;grid-template-columns:1.35fr 1fr 1fr;gap:16px;align-items:stretch}
.pv-card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 18px;display:flex;flex-direction:column;min-width:0;text-align:left;font:inherit;color:inherit}
.pv-card.acc{border-color:var(--acc)}
.pv-h{font-size:12px;font-weight:650;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);margin:0 0 10px;display:flex;align-items:center;gap:8px}
.pv-h.acc{color:var(--acc)}
.pv-badge{background:var(--acc);color:var(--accInk);border-radius:9px;padding:0 7px;font-size:11.5px;line-height:18px;font-weight:650;letter-spacing:0}
.pv-foot{display:block;margin-top:auto;padding-top:10px;border-top:1px solid var(--line2);font-size:13px;color:var(--muted);line-height:19px}
.pv-empty{margin:0 0 6px;font-size:14px;color:var(--ink2)}
.pv-call{display:grid;grid-template-columns:44px minmax(0,1fr);gap:4px 10px;padding:12px 0;border-top:1px solid var(--line2)}
.pv-calls .pv-h+.pv-call{border-top:0;padding-top:0}
.pv-call .id{font-size:12.5px;line-height:22px}
.pv-call .ttl{font-size:16px;line-height:22px;font-weight:600;text-align:left;background:none;border:0;padding:0;color:var(--ink);cursor:pointer;overflow-wrap:anywhere}
.pv-call .ttl:hover{text-decoration:underline}
.pv-call .why,.pv-call .bd,.pv-call .acts{grid-column:2}
.pv-call .why{font-size:13.5px;line-height:19px;color:var(--ink2)}
.pv-call .bd{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:12px}
.pv-call .acts{display:flex;gap:8px;margin-top:6px;flex-wrap:wrap}
.pv-tag{border:1px solid var(--line);border-radius:4px;padding:0 6px;font-size:11.5px;color:var(--ink2);line-height:18px}
.pv-calls .pv-lk{align-self:flex-start;margin:4px 0 2px 54px}
.pv-pin{cursor:pointer;width:100%}
.pv-pin:hover{border-color:var(--muted)}
.pv-pin .l1{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}
.pv-pin .nm{font-size:16px;font-weight:650;white-space:nowrap}
.pv-pin .pt{font-size:11.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);white-space:nowrap;display:inline-flex;gap:4px;align-items:center}
.pv-pin .vi{margin-left:auto;font-size:13px;color:var(--acc);white-space:nowrap}
.pv-pin .l2{display:flex;align-items:baseline;gap:8px;margin-top:8px;flex-wrap:wrap}
.pv-pin .sc{font-size:40px;line-height:44px;font-weight:650;font-variant-numeric:tabular-nums}
.pv-pin .of{font-size:16px;color:var(--muted)}
.pv-pin .bw{font-size:15px;font-weight:650}
.pv-bar{display:flex;background:var(--sunk);border-radius:5px;overflow:hidden;margin:10px 0 8px}
.pv-bar i{display:block;height:100%}
.pv-bar .t{background:var(--barT)}.pv-bar .r{background:var(--barR)}
.pv-leg{display:flex;gap:16px;flex-wrap:wrap;font-size:13px;color:var(--ink2);align-items:center}
.pv-leg span{display:inline-flex;align-items:center;gap:6px}
.pv-sw{display:inline-block;width:10px;height:10px;border-radius:2px;flex:none}
.pv-sw.t{background:var(--barT)}.pv-sw.r{background:var(--barR)}
.pv-drv{display:block;font-size:13px;color:var(--ink2);margin:6px 0 10px}
.pinsvg{flex:none;vertical-align:-1px}
.pv-ev .hl{font-size:16px;font-weight:700}
.pv-strip{display:flex;flex-wrap:wrap;gap:4px;margin:10px 0}
.pv-mk{display:inline-block;width:22px;height:22px;border-radius:3px;flex:none;box-sizing:border-box}
.pv-mk.raised{background:var(--barT)}
.pv-mk.nothing{border:2px solid var(--barT)}
.pv-mk.nh{background:repeating-linear-gradient(135deg,var(--hatch) 0 1.5px,transparent 1.5px 5px);border:1px dashed var(--muted)}
.pv-evl{display:flex;flex-direction:column;gap:5px;font-size:13px;color:var(--ink2)}
.pv-evl span{display:inline-flex;align-items:center;gap:8px}
.pv-evl .pv-mk,.pv-fr .pv-mk,.pv-afoot .pv-mk,.c-n .pv-mk{width:14px;height:14px}
.pv-evl.ph{display:block;line-height:24px}.pv-evl.ph .pv-mk{width:12px;height:12px;vertical-align:-1px;margin-right:3px}
.pv-sil{font-size:13px;color:var(--muted);margin:8px 0 10px}
.pv-ah .ghead,.pv-gov .ghead{flex-wrap:wrap;align-items:baseline}
.ghead .sub{font-size:13px;color:var(--muted);font-weight:400;text-transform:none;letter-spacing:0}
.pv-arow{display:grid;grid-template-columns:minmax(0,1fr) 104px;gap:12px;align-items:center;padding:0 18px;border-top:1px solid var(--line2)}
.pv-arow.pinned{background:var(--sel)}.pv-arow.sel{box-shadow:inset 3px 0 0 var(--acc)}
.pv-arow .af{display:grid;grid-template-columns:200px 150px 190px 150px 110px minmax(0,1fr) 20px;gap:16px;align-items:center;padding:10px 0;width:100%;background:none;border:0;text-align:left;font:inherit;color:inherit;cursor:pointer}
.pv-arow.hd{border-top:0}.pv-arow.hd .af{cursor:default;padding:0 0 6px;font-size:11.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);font-weight:650}
.pv-arow.hd .c-pinh{font-size:11.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);font-weight:650;text-align:center;padding-bottom:6px}
.pv-arow .an{font-weight:600}.pv-arow .at{font-size:11.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);white-space:nowrap}
.pv-arow .as{font-size:22px;font-variant-numeric:tabular-nums}.pv-arow .of{font-size:13px;color:var(--muted)}.pv-arow .ab{font-size:13px}
.pv-arow .c-bar .pv-bar{margin:0}
.pv-arow .c-n b{display:flex;align-items:center;gap:6px;font-size:14px}.pv-arow .c-n b.nhv{color:var(--ink2)}
.pv-arow .c-n small{display:block;font-size:12px;color:var(--muted)}
.pv-arow .c-drv{font-size:13px;color:var(--ink2)}
.pv-arow .c-ch{color:var(--muted);font-size:18px}
.pv-arow .af:hover .an{text-decoration:underline}
.pinbtn{display:inline-flex;align-items:center;justify-content:center;gap:6px;height:32px;padding:0 10px;border:1px solid var(--line);border-radius:8px;background:transparent;color:var(--ink2);font-size:13px;cursor:pointer;justify-self:stretch}
.pinbtn.on{border-color:var(--acc);color:var(--acc);background:var(--card);font-weight:600;cursor:default}
.pv-afoot{display:flex;flex-wrap:wrap;gap:6px 24px;align-items:center;padding:10px 18px 12px;border-top:1px solid var(--line2);font-size:13px;color:var(--muted)}
.pv-afoot>div:last-child:not(.pv-leg){flex-basis:100%}
.pv-trk{padding:12px 18px 10px;border-top:1px solid var(--line2)}
.pv-gov .ghead+.pv-trk{border-top:0;padding-top:2px}
.pv-trk.on{box-shadow:inset 3px 0 0 var(--acc)}
.pv-trk .r1{display:flex;align-items:flex-start;gap:10px}.pv-trk .tt{flex:1;min-width:0}
.pv-trk .tn{font-size:15px;font-weight:650;background:none;border:0;padding:0;text-align:left;color:var(--ink);cursor:pointer}
.pv-trk .tn:hover{text-decoration:underline}
.pv-trk .ld{font-size:13px;color:var(--muted)}
.pv-trk .cn{font-size:13.5px;margin-top:6px}
.pv-hbox{background:var(--sunk);border-radius:6px;padding:8px 10px;margin:8px 0 4px;font-size:13.5px}
.pv-hbox .v{font-size:13px;color:var(--ink2);margin-top:2px}
.pv-fr{display:grid;grid-template-columns:14px minmax(0,1fr) auto;gap:10px;align-items:center;min-height:40px;width:100%;background:none;border:0;border-top:1px solid var(--line2);padding:6px 4px;text-align:left;font:inherit;color:inherit;cursor:pointer}
.pv-frs .pv-fr:first-child{border-top:0}
.pv-fr:hover{background:var(--bg)}.pv-fr.on{background:var(--sel)}
.pv-fr .fn{font-size:13.5px;min-width:0}.pv-fr .fs{display:block;font-size:12px;color:var(--muted)}
.pv-fr .fc{font-size:13px;color:var(--ink2);white-space:nowrap}.pv-fr .fc.dash{color:var(--muted);font-size:15px}
.pv-2b{display:flex;gap:8px;margin-top:8px}.pv-2b .btn{flex:1}
.pv-sum{display:flex;align-items:center;gap:6px;width:100%;min-height:48px;padding:10px 16px;background:var(--card);border:1px solid var(--line);border-radius:10px;font:inherit;font-size:14px;color:var(--ink2);text-align:left;cursor:pointer}
.pv-sum b{color:var(--ink)}.pv-sum span{margin-left:auto;color:var(--muted)}
.pv-newrow{width:100%;min-height:44px;background:none;border:0;border-top:1px solid var(--line2);text-align:left;cursor:pointer;color:var(--ink2);font:inherit;font-size:13.5px}
button.ppl{width:100%;background:none;border:0;border-top:1px solid var(--line2);font:inherit;color:inherit;text-align:left}
.cap .pinsvg{color:var(--muted)}
@media (max-width:1099px){
 .pv-today{grid-template-columns:1fr 1fr}.pv-calls{grid-column:1/-1}
 .pv-g2,.pv-g3{grid-template-columns:minmax(0,1fr)}
 .pv-arow .af{grid-template-columns:minmax(120px,1.2fr) 130px minmax(90px,1fr) 120px 100px 16px}
 .pv-arow .c-drv{display:none}
}
@media (max-width:820px){
 .pv{padding:0 12px;gap:12px}.pv .group{border-radius:10px;border-left:1px solid var(--line);border-right:1px solid var(--line)}
 .pv-col{gap:12px}
 .pv-title p{font-size:13px;min-width:0;flex-basis:100%}
 .pv-today{grid-template-columns:minmax(0,1fr);gap:12px}
 .pv-card{padding:14px 16px}
 .pv-call{grid-template-columns:minmax(0,1fr)}.pv-call .id{display:none}.pv-call .why,.pv-call .bd,.pv-call .acts{grid-column:1}
 .pv-call .acts .btn{flex:1;height:44px}.pv-calls .pv-lk{margin-left:0;min-height:44px}
 .pv-strip{flex-wrap:nowrap;gap:3px}.pv-strip .pv-mk{flex:1;width:auto;height:18px}
 .pv-arow.ph{grid-template-columns:minmax(0,1fr) 44px;gap:8px;padding:0 12px}
 .pv-arow.ph .af{display:block;padding:10px 0}
 .pv-arow.ph .a1{display:flex;align-items:baseline;gap:5px}.pv-arow.ph .an{flex:1;min-width:0}
 .pv-arow.ph .as{font-size:18px}.pv-arow.ph .ab{min-width:58px;text-align:right}
 .pv-arow.ph .pv-bar{margin:6px 0}.pv-arow.ph .a3{display:block;font-size:12.5px;color:var(--ink2)}
 .pinbtn{flex-direction:column;gap:1px;width:44px;height:44px;padding:0;font-size:10.5px}
 .pv-afoot{padding:10px 12px}
 .pv-trk{padding:12px 12px 10px}
 .pv-fr{min-height:44px}
}
/* Pulse redesign Phase 2 (C14 to C19), 2026-10-16 */
.pv-b{display:inline-flex;align-items:center;border:1px solid var(--line);border-radius:4px;padding:0 6px;font-size:11.5px;line-height:18px;color:var(--ink2);font-weight:600;white-space:nowrap}
.pv-b.sev-high,.pv-b.sev-mediumhigh,.pv-b.red{border-color:var(--red);color:var(--red)}
.pv-b.grn{border-color:var(--grn);color:var(--grn)}
.pv-b.stuck{background:var(--ambFill);border-color:var(--ambFill);color:var(--ambInk)}
.pv-b.new,.pv-b.esc{border-color:var(--acc);color:var(--acc)}
.pv-b.call{background:var(--acc);border-color:var(--acc);color:var(--accInk)}
.pv-iss .ghead,.pv-kn .ghead,.pv-ppl .ghead{flex-wrap:wrap;align-items:center}
.ghead .sub.r,.pv-srt{margin-left:auto}
.pv-sl{flex:1;text-align:right}
.pv-srt{display:inline-flex;gap:6px;align-items:center;text-transform:none;letter-spacing:0}
.pv-srt select{height:30px;border:1px solid var(--line);border-radius:6px;background:var(--card);padding:0 8px;font-size:13px;color:var(--ink)}
.pv-ir{display:grid;grid-template-columns:48px minmax(0,1fr) 236px;gap:14px;padding:12px 18px;border-top:1px solid var(--line2);align-items:start;cursor:pointer}
.pv-ir:hover{background:var(--bg)}.pv-ir.sel{background:var(--sel)}
.pv-ir .id{font:12.5px ui-monospace,Menlo,monospace;color:var(--muted);line-height:21px}
.pv-ir .ttl{display:block;font-size:15px;line-height:21px;font-weight:600;text-align:left;background:none;border:0;padding:0;color:var(--ink);cursor:pointer;overflow-wrap:anywhere}
.pv-ir .ttl:hover{text-decoration:underline}
.pv-ir .iid{font:12.5px ui-monospace,Menlo,monospace;color:var(--muted);font-weight:400;margin-right:6px}
.pv-ir .bdg,#pv-sheet .bdg,#pv-meet .bdg{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 4px}
.pv-ir .ow{font-size:13px;color:var(--ink2);line-height:19px}
.pv-ir .ow .no,#pv-sheet .no{color:var(--red);font-weight:700}
.pv-ir .nx{font-size:13px;color:var(--muted);line-height:19px;margin-top:3px}
.pv-ir .ac{display:flex;gap:8px;justify-content:flex-end;align-items:center;flex-wrap:wrap}
.pv-ir .ac .lw{font-size:13px;color:var(--muted)}
.pv-wl{font-size:13.5px;color:var(--acc)}
.pv-ir.dim .ttl{color:var(--muted)}.pv-ir.done .ttl{text-decoration:line-through;color:var(--muted)}
.pv-kr{grid-template-columns:48px minmax(0,1fr)}
.pv-chk{display:flex;align-items:center;gap:10px;width:100%;min-height:44px;padding:8px 18px;border:0;border-top:1px solid var(--line2);background:none;font:inherit;font-size:13.5px;color:var(--ink2);text-align:left;cursor:pointer}
.pv-chk .bx{display:inline-flex;align-items:center;justify-content:center;width:16px;height:16px;border:1.5px solid var(--muted);border-radius:3px;font-size:12px;color:var(--acc);flex:none}
.pv-chk[aria-checked=true] .bx{border-color:var(--acc)}
.pv-chip{position:sticky;top:var(--hdrH,96px);z-index:4;background:var(--bg);padding:6px 0;margin:-6px 0}
.pv-kf{padding:10px 18px 12px;border-top:1px solid var(--line2);font-size:13px;color:var(--muted)}
.ppl.pv-pp{grid-template-columns:minmax(0,1fr) 70px 80px 96px}
.pv-pp.g{cursor:default;padding-bottom:0;border-top:0;font-size:11.5px;color:var(--muted);font-weight:650}
.pv-pp.g .gl{grid-column:span 2;text-align:center;border-bottom:1px solid var(--line);padding-bottom:3px}
.pv-pp.g .gl.r{grid-column:span 1}
.pv-pp.h{border-top:0}
.pv-pp .z{color:var(--muted)}
button.pv-pp{min-height:40px;align-items:center}
.pv-pmore{padding-left:16px}
.pv-pn{padding-top:10px;border-top:1px solid var(--line2);font-size:12.5px}
/* C16 sheet */
#pv-sheet{position:fixed;inset:0;z-index:30}
#pv-sheet .sc{position:absolute;inset:0;background:var(--scrim)}
#pv-sheet .sh{position:absolute;left:0;right:0;bottom:0;max-height:min(640px,92vh);overflow:auto;background:var(--card);border-radius:14px 14px 0 0;padding:8px 16px calc(16px + env(safe-area-inset-bottom));box-shadow:0 -4px 20px rgba(0,0,0,.18)}
#pv-sheet .grab{width:36px;height:4px;border-radius:2px;background:var(--line);margin:0 auto 10px}
#pv-sheet .l1{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--muted)}
#pv-sheet .l1 .id{font-family:ui-monospace,Menlo,monospace}
#pv-sheet .cl{margin-left:auto;min-height:44px;font-size:15px}
#pv-sheet h2{font-size:19px;line-height:25px;font-weight:650;margin:4px 0 8px}
#pv-sheet .nb{background:var(--sunk);border-radius:8px;padding:10px 12px;font-size:15px;line-height:21px;margin:10px 0}
#pv-sheet .nb span,#pv-sheet .facts span{display:block;font-size:12.5px;color:var(--muted)}
#pv-sheet .facts{display:grid;grid-template-columns:1fr 1fr;gap:12px 16px;font-size:14.5px;margin:12px 0 14px}
#pv-sheet .facts .w{grid-column:1/-1}#pv-sheet .facts a{color:var(--acc)}
#pv-sheet .ft{border-top:1px solid var(--line2);padding-top:12px;margin:0 -16px;padding-left:16px;padding-right:16px}
#pv-sheet .b2{display:flex;gap:10px}#pv-sheet .b2 .btn{flex:1;height:44px}
#pv-sheet .full{display:block;margin:10px auto 0;min-height:44px;font-size:15px}
#pv-sheet .snf{display:flex;flex-direction:column;gap:8px;margin-top:10px}#pv-sheet textarea{min-height:90px;font-size:16px}
/* C17 meeting view */
#pv-meet{position:fixed;inset:0;z-index:25;overflow:auto;background:var(--bg);color:var(--ink);font-size:17px;outline:0}
#pv-meet .mw{max-width:1240px;margin:0 auto;padding:40px 64px}
#pv-meet .mh{display:flex;gap:16px;align-items:flex-start}#pv-meet .mh>div:first-child{flex:1;min-width:0}
#pv-meet .kk{font-size:14px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
#pv-meet h2{font-size:34px;line-height:42px;font-weight:650;margin:2px 0 4px}
#pv-meet .sb{font-size:16px;color:var(--ink2)}
#pv-meet .mb{display:flex;gap:8px;flex-wrap:wrap}
#pv-meet .mban{display:flex;gap:14px;border:1.5px dashed var(--muted);border-radius:8px;padding:14px 18px;margin:28px 0 8px;background:var(--card)}
#pv-meet .mban .hx{width:22px;flex:none;background:repeating-linear-gradient(135deg,var(--hatch) 0 1.5px,transparent 1.5px 5px)}
#pv-meet .mban b{font-size:19px;font-weight:650}#pv-meet .mban p{margin:4px 0 0;font-size:16px;line-height:24px;color:var(--ink2)}
#pv-meet .mg{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:48px;align-items:start;margin-top:24px}
#pv-meet .ms{margin-bottom:28px}
#pv-meet .ms h3{display:flex;align-items:baseline;gap:10px;font-size:15px;letter-spacing:.05em;text-transform:uppercase;font-weight:650;margin:0;padding-bottom:10px;border-bottom:1px solid var(--line)}
#pv-meet .ms h3 .nm{font-size:28px;color:var(--muted);letter-spacing:0}
#pv-meet .mi{display:grid;grid-template-columns:72px minmax(0,1fr);gap:0;padding:14px 0;border-bottom:1px solid var(--line2)}
#pv-meet .mi.none{display:block;color:var(--muted);font-size:15px}
#pv-meet .mi .id{font:14px ui-monospace,Menlo,monospace;color:var(--muted);line-height:26px}
#pv-meet .mt{font-size:18px;line-height:26px;font-weight:600;background:none;border:0;padding:0;text-align:left;color:var(--ink);cursor:pointer}
#pv-meet .mt:hover{text-decoration:underline}
#pv-meet .mm{font-size:15px;color:var(--ink2);margin-top:2px}#pv-meet .mn{font-size:15px;color:var(--muted);margin-top:4px}
#pv-meet .mr{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:18px;position:sticky;top:20px}
#pv-meet .rh{font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:0 0 8px}
#pv-meet .rh.sep{border-top:1px solid var(--line2);padding-top:14px;margin-top:14px}
#pv-meet .rc{font-size:16px;margin-bottom:18px}#pv-meet .rh.sep+.rc{margin-bottom:4px}
#pv-meet .rf{display:flex;gap:10px;align-items:flex-start;font-size:15px;margin-bottom:12px}#pv-meet .rf .pv-mk{width:14px;height:14px;margin-top:4px}
#pv-meet .rf small{display:block;font-size:13px;color:var(--muted)}
@media (max-width:1099px){#pv-meet .mw{padding:28px 28px}#pv-meet .mg{grid-template-columns:minmax(0,1fr) 280px;gap:28px}}
@media (max-width:820px){
 .pv-ir{grid-template-columns:minmax(0,1fr);gap:8px;padding:12px}.pv-ir>.id{display:none}
 .pv-ir .ac{justify-content:stretch}.pv-ir .ac .btn{flex:1;height:44px}.pv-ir .ac:empty{display:none}
 .pv-ir .ac .lw{flex:1}.pv-wl{display:inline-flex;align-items:center;min-height:44px}
 .pv-sl{flex-basis:100%;text-align:left;order:3}.pv-srt select{height:40px;font-size:16px}
 .pv-chk{padding:8px 12px}.pv-kf{padding:10px 12px}
 .ppl.pv-pp{grid-template-columns:minmax(0,1fr) 52px 64px 78px}
 #pv-meet{font-size:16px}#pv-meet .mw{padding:calc(16px + env(safe-area-inset-top)) 16px 40px}
 #pv-meet .mh{flex-direction:column}#pv-meet h2{font-size:26px;line-height:32px}#pv-meet .mb{width:100%}#pv-meet .mb .btn{flex:1}#pv-meet [data-mfs]{display:none}
 #pv-meet .mg{grid-template-columns:minmax(0,1fr);gap:20px}#pv-meet .mr{position:static;order:-1}
 #pv-meet .mi{grid-template-columns:56px minmax(0,1fr)}#pv-meet .mt{font-size:16.5px;line-height:23px}
}
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
.bv{display:grid;grid-template-columns:260px minmax(0,1fr) 220px;gap:0;min-height:calc(100vh - 140px)}
.bl{border-right:1px solid var(--line);padding:8px 0;min-width:0}.bl .ghead{padding:12px 16px 6px}
.bi{display:block;width:100%;text-align:left;border:0;background:none;padding:8px 16px;color:var(--ink);font-size:14px;cursor:pointer;border-left:3px solid transparent}
.bi:hover{background:var(--sel)}.bi.on{background:var(--sel);border-left-color:var(--acc)}
.bi .bd{font-weight:600;font-variant-numeric:tabular-nums}.bi .bk{font-size:12px;color:var(--muted);margin-left:6px}
.bi .bk.w{color:var(--acc);font-weight:600}
.br{padding:24px 40px 80px;min-width:0;overflow-wrap:anywhere}
.br .bh{display:flex;flex-wrap:wrap;align-items:center;gap:6px 16px;font-size:13px;color:var(--muted);margin:0 auto 18px;max-width:72ch}
.br .bh a{color:var(--acc)}.bsel{display:none;font:inherit;font-size:14px;padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink)}
.md.brief{max-width:72ch;margin:0 auto;font-size:16px}
.md.brief h1{font-size:26px;line-height:32px;margin:0 0 22px;letter-spacing:-.01em}
.md.brief p,.md.brief li{font-size:16px;line-height:26px;color:var(--ink)}.md.brief p{margin:0 0 14px}.md.brief p.muted{font-size:13.5px;line-height:21px;color:var(--muted)}
.md.brief ul,.md.brief ol{padding-left:22px;margin:0 0 16px}.md.brief li{margin:0 0 10px}
.bsec{border-top:1px solid var(--line);padding:4px 0}.bsec>summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:flex-start;gap:10px;padding:0;background:none;border:0}.bsec>summary h2{flex:1;text-align:left}
.bsec>summary::-webkit-details-marker{display:none}
.bsec>summary::before{content:'';width:7px;height:7px;border-right:2px solid var(--muted);border-bottom:2px solid var(--muted);transform:rotate(-45deg);transition:transform .15s;flex:none;margin-left:2px}
.bsec[open]>summary::before{transform:rotate(45deg)}
.md.brief .bsec h2{font-size:19px;line-height:26px;margin:14px 0;text-transform:none;letter-spacing:0;color:var(--ink);font-weight:650}
.bsec:not([open]) h2{color:var(--ink2);font-weight:550}.bsb{padding:0 0 10px}
.pcard{border:1px solid var(--line);border-radius:10px;background:var(--card);padding:14px 16px;margin:0 0 14px}
.pc-lead{font-size:16px;line-height:24px;margin-bottom:8px}
.pcard dl{display:grid;grid-template-columns:150px minmax(0,1fr);gap:6px 14px;margin:0}
.pcard dt{font-size:12px;font-weight:650;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);padding-top:4px}
.pcard dd{margin:0;font-size:15px;line-height:23px}.pcard dd.nx{font-weight:600}.pcard dt.nx{color:var(--acc)}
.md.brief li.lic{list-style:none;margin-left:-22px}
.md.brief li.kv{list-style:none;margin-left:-22px;display:grid;grid-template-columns:150px minmax(0,1fr);gap:14px}
.md.brief li.kv .k{font-size:12px;font-weight:650;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);padding-top:3px}.md.brief li.kv.nx .v{font-weight:600}
.tw{overflow-x:auto;margin:0 0 16px}.md.brief table{font-size:14px;width:100%;border-collapse:collapse}
.md.brief th{background:var(--sunk);font-weight:600}.md.brief td,.md.brief th{border:0;border-bottom:1px solid var(--line);padding:7px 10px}
.md.brief tr:nth-child(even) td{background:color-mix(in srgb,var(--sunk) 45%,transparent)}
.md a.iid{font:600 12.5px ui-monospace,Menlo,monospace;color:var(--acc);text-decoration:none;background:var(--sel);border-radius:4px;padding:0 3px;white-space:nowrap}
.md a.iid:hover{background:var(--acc);color:var(--accInk)}
.co{border-radius:10px;padding:12px 16px;margin:0 0 16px;background:var(--sunk)}.co p{margin:4px 0}
.co.risk{border-left:4px solid var(--red)}.co.dec{border:1px solid var(--acc);background:var(--sel)}
.co.src{background:none;padding:0;margin-top:-6px}.co.src p{font-size:13px;line-height:19px;color:var(--muted)}
.co.bl1{border-top:2px solid var(--ink);border-bottom:2px solid var(--ink);border-radius:0;background:none}
.co.cap{background:none;padding:0}.co.cap p{font-size:13.5px;color:var(--muted);font-style:italic}
.chart{border:1px dashed var(--line);border-radius:10px;padding:12px 16px;color:var(--muted);font-size:14px;margin:0 0 14px}
.btoc{position:sticky;top:var(--hdrH,100px);align-self:start;padding:24px 16px;max-height:calc(100vh - 120px);overflow:auto}
.btoc a{display:block;font-size:13px;line-height:18px;padding:5px 0 5px 10px;color:var(--ink2);text-decoration:none;border-left:2px solid var(--line)}
.btoc a:hover{color:var(--acc);border-left-color:var(--acc)}.btoc a.cl{color:var(--muted)}
.bsec{scroll-margin-top:120px}
.tab .nd{width:7px;height:7px;border-radius:50%;background:var(--acc);display:inline-block}
.bback{display:none}
@media (max-width:1280px){.bv{grid-template-columns:240px minmax(0,1fr)}.btoc{display:none}.bsel{display:inline-block}}
@media (max-width:820px){.bv{grid-template-columns:1fr}.bl{border-right:0}.bv.reading .bl{display:none}.bv:not(.reading) .br{display:none}.br{padding:14px 16px 60px}.bback{display:inline-block}.br .bh .bp{display:none}
 .md.brief{font-size:16px}.md.brief h1{font-size:21px;line-height:27px}.pcard dl,.md.brief li.kv{grid-template-columns:1fr;gap:2px}.pcard dd{margin-bottom:8px}}
.cp{border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:0 0 14px;background:var(--card)}.cp.need{border-color:var(--acc)}
.cp-h{display:flex;align-items:center;gap:10px;margin-bottom:4px}.cp-n{font:700 12px ui-monospace,Menlo,monospace;background:var(--acc);color:var(--accInk);border-radius:5px;padding:2px 7px}
.cp:not(.need) .cp-n{background:var(--sunk);color:var(--ink2)}.cp-b{margin-left:auto;font-size:12px;font-weight:650}.cp-b.y{color:var(--acc)}.cp-b.n{color:var(--muted)}
.cp-m{font-size:12.5px;color:var(--muted);margin-bottom:8px}.cp-f{list-style:none;margin:0 0 10px;padding:0;font-size:13px}
.cp-f li{display:flex;justify-content:space-between;gap:10px;padding:3px 0;border-bottom:1px solid var(--line2);color:var(--muted)}.cp-f li.d{color:var(--ink)}.cp-f li span:last-child{font-size:12px;color:var(--muted);white-space:nowrap}
.cp-adv{font-size:15px;font-weight:650;line-height:22px}.cp-how{font-size:13px;color:var(--muted);line-height:19px;margin:6px 0 0}
.cp-t{margin-top:8px}.cp-t textarea{width:100%;height:220px;font:12px ui-monospace,Menlo,monospace;border:1px solid var(--line);border-radius:8px;background:var(--sunk);color:var(--ink);padding:8px}
.csteps{margin:0;padding:0;list-style:none}.cs{display:flex;gap:10px;align-items:flex-start;padding:5px 0;font-size:14.5px;line-height:21px}
.cs .ck{flex:none;width:22px;height:22px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;background:var(--acc);color:var(--accInk)}
.cs.done .ck{background:var(--grn)}.cs.done span:last-child{color:var(--muted)}.cs.skip .ck{background:var(--sunk);color:var(--muted)}
.b-neutral{color:var(--ink2)}.pv-arow.ph .spk{margin:4px 0 6px}.spk{display:block;overflow:visible}.spk.b-neutral{color:var(--muted)}
.pv-spk{display:flex;flex-direction:column;gap:4px;margin:6px 0 4px}.pv-spkn{font-size:12.5px;color:var(--muted)}
</style></head><body>
<header>
 <div class="hbar">
  <h1 class="brand">EOS Registers</h1>
  <nav class="tabs" id="views" aria-label="Views"></nav>
  <input type="search" id="q" placeholder="Search title, owner, ID, notes…" autocomplete="off">
  <button class="btn" id="searchBtn">Search</button>
  <button class="btn primary" id="newBtn">Add</button>
  <button class="btn" id="cpBtn" data-cprompts>Copilot</button>
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
let BRIEFS=[],BRIEF=null,BREAD=false,ITEMS=[],TODAY='',VIEW='triage',Q='',SEL=null,MOREW=false,DRAWER=null,PULSE=null,PF={},PALL=false;
const BASE={},SESSION=[],SAVED={};
const CLOSED=new Set(['closed','dropped','aged_out']);
const isOpen=i=>!CLOSED.has(i.status)&&i.tier!=='retired';
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const plain=s=>String(s??'').replace(/\*\*([^*]+)\*\*/g,'$1').replace(/`([^`]+)`/g,'$1').replace(/~~([^~]+)~~/g,'$1');
let toastT;function toast(t){const e=$('#toast');e.textContent=t;e.style.display='block';clearTimeout(toastT);toastT=setTimeout(()=>e.style.display='none',2200)}
async function load(){const [j,p]=await Promise.all([fetch('/api/items').then(r=>r.json()),fetch('/api/pulse').then(r=>r.ok?r.json():null).catch(()=>null),loadBriefs()]);ITEMS=j.items;TODAY=j.today;PULSE=p;render();const o=new URLSearchParams(location.search).get('open');if(o&&!DRAWER)openDrawer(o)}

const VIEWS=[['triage','Focus'],['pulse','Pulse'],['briefs','Briefs'],['A','Mine'],['other','Other-owned'],['watch','Watch'],['decision','Decisions'],['needs','Needs triage'],['closed','Disposed']];
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
  $('#views').innerHTML=VIEWS.map(([v,l])=>`<button class="tab${v===VIEW?' on':''}" data-v="${v}"${v===VIEW?' aria-current="page"':''}>${l}${v==='briefs'?(BRIEFS.some(b=>b.date===TODAY)?'<span class="nd" title="Today\u2019s brief is in"></span>':''):`<span class="n">${ITEMS.filter(i=>inView(i,v)).length}</span>`}</button>`).join('');
  const m=(l,s,n,c)=>`<div class="cap${n>c?' over':''}"><span class="l">${l}</span><span class="s">${s}</span><span class="bar"><i style="width:${Math.min(100,n/c*100)}%"></i></span><b>${n}/${c}</b></div>`;
  const dt=new Date(dn(TODAY));
  $('#meta').innerHTML=m('Register A','A',A,15)+m('Watch active','Watch',W,20)+m('Radar','Radar',D,20)+pulseCaps()+`<div class="cap"><span class="dot"></span><span class="l">Needs triage</span><span class="s">Triage</span><b>${N}</b></div><span class="today">${VIEW==='briefs'?BRIEFS.length+' briefs':a.length+' shown'} · ${['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][dt.getUTCDay()]}, ${fmt(TODAY)}</span>`;
  $('#logBtn').innerHTML='Changes'+(SESSION.length?`<span class="badge">${SESSION.length}</span>`:'');
  if(VIEW==='briefs'){$('#list').innerHTML=briefsHtml();const hd=document.querySelector('header');if(hd)document.documentElement.style.setProperty('--hdrH',hd.offsetHeight+'px');return}
  if(VIEW==='pulse'){$('#list').innerHTML=pulseHtml();const hd=document.querySelector('header');if(hd)document.documentElement.style.setProperty('--hdrH',hd.offsetHeight+'px');return}
  const gs=groups(a);
  $('#list').innerHTML=sortBar(VIEW,a.length)+(gs.map(g=>{let rows=g.rows,more='';
    if(g.k==='watch'&&rows.length>3){more=`<button class="more" data-more>${MOREW?'Show fewer':'Show '+(rows.length-3)+' more risks'}</button>`;if(!MOREW)rows=rows.slice(0,3)}
    return `<section class="group"><h2 class="ghead ${g.k}">${g.l}<span class="n">${g.rows.length}</span></h2>${rows.map(rowHtml).join('')}${more}</section>`}).join('')||'<div class="empty">Nothing here.</div>');
}
document.addEventListener('click',e=>{
  if(e.target.closest('[data-sclose]')){closeSheet();return}
  if(e.target.closest('[data-snote]')){SHEETNOTE=!SHEETNOTE;openSheet(SHEET);return}
  if(e.target.closest('[data-sfull]')){const id=SHEET;closeSheet();openDrawer(id);return}
  const so=e.target.closest('[data-sopen]');if(so){e.preventDefault();closeSheet();closeMeet();openDrawer(so.dataset.sopen);return}
  if(e.target.closest('[data-mclose]')){closeMeet();return}
  if(e.target.closest('[data-mcopy]')){const txt=agendaMd(MEET);(navigator.clipboard?navigator.clipboard.writeText(txt):Promise.reject()).then(()=>toast('Copied'),()=>toast('Copy is blocked here; select the text instead'));return}
  if(e.target.closest('[data-mfs]')){const el=$('#pv-meet');if(document.fullscreenElement)document.exitFullscreen();else if(el&&el.requestFullscreen)el.requestFullscreen().catch(()=>toast('Full screen is not available here'));else toast('Full screen is not available here');return}
  const mo=e.target.closest('[data-mopen]');if(mo){closeMeet();openDrawer(mo.dataset.mopen);return}
  if(e.target.closest('[data-pplall]')){PPLALL=!PPLALL;render();return}
  const s=e.target.closest('.seg button');if(s){e.stopPropagation();const i=ITEMS.find(x=>x.id===s.dataset.id);if(i&&i[s.dataset.k]!==s.dataset.val)patch(s.dataset.id,{[s.dataset.k]:s.dataset.val},'');return}
  if(e.target.closest('[data-cprompts]')){openPrompts();return}
  const cpy=e.target.closest('[data-cpy]');if(cpy){copyPrompt(cpy.dataset.cpy);return}
  const tc=e.target.closest('[data-toc]');if(tc){e.preventDefault();jumpSec(tc.dataset.toc);return}
  const bi=e.target.closest('[data-brief]');if(bi){openBrief(bi.dataset.brief,'list');return}
  if(e.target.closest('[data-bback]')){BREAD=false;render();scrollTo(0,0);return}
  const cb=e.target.closest('.tab[data-v]');if(cb&&cb.dataset.v==='briefs'){VIEW='briefs';loadBriefs().then(()=>{if(!BRIEF&&BRIEFS.length)openBrief(BRIEFS[0].name,'tab');else render()});scrollTo(0,0);return}
  const c=e.target.closest('.tab[data-v]');if(c){VIEW=c.dataset.v;MOREW=false;for(const k in BASE)delete BASE[k];render();scrollTo(0,0);return}
  if(e.target.closest('[data-more]')){MOREW=!MOREW;render();return}
  const es=e.target.closest('[data-esc]');if(es){e.stopPropagation();escalateP(es.dataset.id,es.dataset.esc);return}
  const ag=e.target.closest('[data-agenda]');if(ag){e.stopPropagation();openAgenda(ag.dataset.agenda);return}
  const op=e.target.closest('[data-open]');if(op){e.preventDefault();openDrawer(op.dataset.open);return}
  if(e.target.closest('[data-pclear]')){PF={};render();return}
  if(e.target.closest('#sortDir')){const so=sortOf(VIEW);SORT[VIEW]={k:so.k,dir:-so.dir};saveSort();render();return}
  if(e.target.closest('[data-pall]')){PALL=!PALL;render();return}
  const pinb=e.target.closest('[data-pin]');if(pinb){e.stopPropagation();pinAccount(pinb.dataset.pin);return}
  if(e.target.closest('[data-callall]')){CALLALL=!CALLALL;render();return}
  if(e.target.closest('[data-issall]')){ISSALL=!ISSALL;render();return}
  if(e.target.closest('[data-kopen]')){KOPEN=!KOPEN;render();return}
  if(e.target.closest('[data-popen]')){POPEN=!POPEN;render();return}
  const tko=e.target.closest('[data-trk]');if(tko){TRKOPEN[tko.dataset.trk]=!TRKOPEN[tko.dataset.trk];render();return}
  const gd=e.target.closest('[data-guide]');if(gd){openHelp(gd.dataset.guide||'Pulse');return}
  if(e.target.closest('[data-kall]')){KALL=!KALL;render();return}
  if(e.target.closest('[data-pv]')){VIEW='pulse';PF={};render();scrollTo(0,0);return}
  const pf=e.target.closest('[data-pf]');if(pf){const k=pf.dataset.pf,v=pf.dataset.val;const fromCap=!!pf.closest('#meta');PF=(!fromCap&&PF[k]===v)?{}:{[k]:v};VIEW='pulse';render();if(fromCap)scrollTo(0,0);if(PF[k]){const c=document.getElementById('pv-issues');if(c){c.scrollIntoView({block:'start'});scrollBy(0,-110)}}return}
  const pi=e.target.closest('[data-pi]');if(pi){if(PHONE())openSheet(pi.dataset.pi);else openDrawer(pi.dataset.pi);return}
  const kr=e.target.closest('[data-kid]');if(kr){openDrawer(kr.dataset.kid);return}
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
const BANDCLS={green:'b-green',amber:'b-amber',red:'b-red',neutral:'b-neutral'};
/* Trend (2026-10-19): the headline is how the team-raised load moved in 7 days, not a score out of 100. */
function th(x){if(x.delta==null)return {big:String(x.load),unit:'load',word:x.label||'Baseline',note:x.trend_from?'7-day trend from '+fmt(x.trend_from):''};
  return {big:(x.delta>0?'↑ +'+x.delta:x.delta<0?'↓ −'+Math.abs(x.delta):'→ 0'),unit:'in 7 days',word:x.label,note:'load '+x.load+(x.load_7!=null?', was '+x.load_7:'')}}
function spark(x,w,h){const s=x.series||[];w=w||120;h=h||26;if(s.length<2)return '';const mx=Math.max(...s,20),st=w/(s.length-1);
  const pts=s.map((v,i)=>`${(i*st).toFixed(1)},${(h-2-(v/mx)*(h-4)).toFixed(1)}`).join(' ');
  return `<svg class="spk ${BANDCLS[x.band]||''}" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" role="img" aria-label="Team-raised load, ${s.length} days from ${fmt(x.series_start)}: ${s.join(', ')}"><polyline points="${pts}" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/><circle cx="${((s.length-1)*st).toFixed(1)}" cy="${(h-2-(s[s.length-1]/mx)*(h-4)).toFixed(1)}" r="2.6" fill="currentColor"/></svg>`}
const fname=k=>((PULSE&&PULSE.forums)||[]).find(f=>f.key===k)?.name||k||'Unassigned forum';
function pulseCaps(){if(!PULSE)return '';const d=(PULSE.health||[]).find(h=>h.pinned);const c=(PULSE.candidates||[]).length;
  /* C10: the pinned account (a setting, Dell by default), with score and band word, on every tab */
  return (d?`<div class="cap" data-pf="account" data-val="${esc(d.account)}" title="Pinned account">${PIN_SVG(1)}<span>${esc(d.account)}</span><b class="hs ${BANDCLS[d.band]}">${esc(th(d).big)}${d.delta==null?' load':''}</b><b class="hs ${BANDCLS[d.band]}">· ${esc(d.label)}</b></div>`:'')+
   `<div class="cap" data-pv="1"><span class="l">Pulse calls</span><span class="s">Calls</span><b${c?' class="hs b-amber"':''}>${c}</b></div>`}
function ptags(i){let t='';
  if(i.severity)t+=`<span class="t-sev ${esc(String(i.severity).toLowerCase())}">${esc(i.severity)}</span>`;
  if(i.customer_visible)t+='<span class="t-cv">Customer-visible</span>';
  if(i._stuck)t+='<span class="t-stuck">Stuck</span>';
  if(i.escalated_to)t+=`<span class="t-esc">Escalated · ${esc(i.escalated_to)}</span>`;else if(i._candidate)t+='<span class="t-esc">Needs your call</span>';
  if(i._state!=='live')t+=`<span>${cap(i._state)}</span>`;
  return t}
/* Phase 2, C14: issue rows on a shared grid (48px · body · 236px actions). Badges are additive; the drawer is unchanged. */
const isNewI=i=>dn(String(i.first_seen||'1970-01-01').slice(0,10))>=dn(TODAY)-7*864e5;
const stOf=i=>i.escalated_to?'esc':i.escalation==='declined'?'left':'open';
function ibadges(i,withState){let t='';const sv=String(i.severity||'');
  if(sv)t+=`<span class="pv-b sev-${esc(sv.toLowerCase().replace(/[^a-z]/g,''))}">${esc(sv)}</span>`;
  if(i.customer_visible)t+='<span class="pv-b">Customer-visible</span>';
  if(i._stuck)t+=`<span class="pv-b stuck">Stuck · raised since ${fmt(i.first_seen)}</span>`;
  if(isNewI(i)&&i._state==='live')t+='<span class="pv-b new">New</span>';
  if(i.escalated_to)t+=`<span class="pv-b esc">Escalated · ${esc(i.escalated_to)}</span>`;
  else if(i._candidate)t+='<span class="pv-b call">Needs your call</span>';
  if(withState&&!i.escalated_to&&i.escalation==='declined')t+='<span class="pv-b">Left with team</span>';
  if(i._state!=='live')t+=`<span class="pv-b">${cap(i._state)}</span>`;
  return t}
function iacts(i){if(i._state!=='live')return '';const s=stOf(i),id=esc(i.id);
  if(s==='esc')return `<a href="#" class="pv-wl" data-open="${esc(i.escalated_to)}">Open Watch ${esc(i.escalated_to)}</a>`;
  if(s==='left')return `<span class="lw">Left with team</span><button type="button" class="btn" data-esc="escalate" data-id="${id}">Escalate</button>`;
  return `<button type="button" class="btn primary" data-esc="escalate" data-id="${id}">Escalate</button><button type="button" class="btn" data-esc="decline" data-id="${id}">Leave with team</button>`}
function prow(i){const ph=PHONE(),id=esc(i.id),cls=i._state==='live'?'':i._state==='quiet'?' dim':' done';
  const own=i.owner?'Owner: '+esc(i.owner):'<b class="no">No owner named</b>';
  const meta=[own,esc(i.account||'No account'),ph?'':esc(fname(i.forum)),(ph?'':'last raised ')+fmt(i.last_seen||i.first_seen)].filter(Boolean).join(' · ');
  const nx=!ph&&i.next_action?`<div class="nx">Next: ${esc(plain(i.next_action))}</div>`:'';
  return `<div class="pv-ir${SEL===i.id?' sel':''}${cls}" data-pi="${id}"><div class="id">${id}</div>
   <div class="bd"><button type="button" class="ttl" data-pi="${id}">${ph?`<span class="iid">${id}</span>`:''}${esc(i.title)}</button><div class="bdg">${ibadges(i)}</div><div class="ow">${meta}</div>${nx}</div>
   <div class="ac">${iacts(i)}</div></div>`}
/* C14 footer: a real toggle with the quiet IDs named */
function allToggle(scope){const q=scope.filter(i=>i._state==='quiet'),r=scope.filter(i=>i._state!=='live'&&i._state!=='quiet');
  if(!q.length&&!r.length&&!PALL)return '';
  const what=[q.length?`${q.length} quiet: ${q.map(i=>i.id).join(', ')}`:'',r.length?`${r.length} resolved or dropped`:''].filter(Boolean).join('; ');
  return `<button type="button" class="pv-chk" role="checkbox" aria-checked="${PALL}" data-pall><span class="bx" aria-hidden="true">${PALL?'✓':''}</span>Include quiet and resolved (${esc(what)})</button>`}
function sortMini(n){const c=SORTS.pulse,s=sortOf('pulse');
  const lab=s.k==='pulse'?'Sorted by attention: stuck, severity, customer-visible, most recent':`${n} shown · `+(SORTDESC[s.k]||((s.dir>0?'ascending':'descending')+', ties by ID'));
  return `<span class="sub pv-sl">${esc(lab)}</span><span class="pv-srt"><select id="sortSel" aria-label="Sort live issues">${c.opts.map(o=>`<option value="${o[0]}"${o[0]===s.k?' selected':''}>${o[0]==='pulse'?'Attention':o[1]}</option>`).join('')}</select>${s.k==='pulse'||SORTDESC[s.k]?'':`<button type="button" class="btn sm" id="sortDir" aria-label="Reverse the order">${s.dir>0?'↑':'↓'}</button>`}</span>`}

/* Phase 2, C16: phone preview sheet. Desktop keeps the drawer. */
let SHEET=null,SHEETNOTE=false;
function openSheet(id){const i=ITEMS.find(x=>x.id===id);if(!i)return;SHEET=id;
  let el=$('#pv-sheet');if(!el){el=document.createElement('div');el.id='pv-sheet';document.body.appendChild(el)}
  const ppl=(i.people||[]).filter(p=>p!==i.owner);
  const links=(i.links||[]).map(l=>`<a href="#" data-sopen="${esc(l)}">${esc(l)}</a>`).join(' · ');
  const s=stOf(i);
  const act=i._state!=='live'?'':s==='esc'?`<button type="button" class="btn primary" data-sopen="${esc(i.escalated_to)}">Open Watch ${esc(i.escalated_to)}</button>`:s==='left'?`<button type="button" class="btn primary" data-esc="escalate" data-id="${esc(i.id)}">Escalate</button>`:`<button type="button" class="btn primary" data-esc="escalate" data-id="${esc(i.id)}">Escalate</button><button type="button" class="btn" data-esc="decline" data-id="${esc(i.id)}">Leave with team</button>`;
  el.innerHTML=`<div class="sc" data-sclose></div><div class="sh" role="dialog" aria-modal="true" aria-label="${esc(i.id)} preview"><div class="grab" aria-hidden="true"></div>
   <div class="l1"><span class="id">${esc(i.id)}</span><span>Pulse issue${i.account?' · '+esc(i.account):''}</span><button type="button" class="pv-lk cl" data-sclose>Close</button></div>
   <h2>${esc(i.title)}</h2><div class="bdg">${ibadges(i,true)}</div>
   ${i.next_action?`<div class="nb"><span>Next action</span>${esc(plain(i.next_action))}</div>`:''}
   <div class="facts"><div><span>Owner</span>${i.owner?esc(i.owner):'<b class="no">No owner named</b>'}</div><div><span>Named in evidence</span>${ppl.length?esc(ppl.join(', ')):'None named'}</div>
   <div><span>Forum</span>${esc(fname(i.forum))}</div><div><span>First and last raised</span>${fmt(i.first_seen)} · ${fmt(i.last_seen||i.first_seen)}</div>
   ${links?`<div class="w"><span>Linked</span>${links}</div>`:''}</div>
   <div class="ft"><div class="b2">${act}<button type="button" class="btn" data-snote>Add a note</button></div>
   ${SHEETNOTE?`<form id="snf" class="snf"><textarea id="snote" placeholder="What happened, what you decided, what Claude should know…"></textarea><button type="submit" class="btn primary">Save note</button></form>`:''}
   <button type="button" class="pv-lk full" data-sfull>Full detail and history</button></div></div>`;
  document.body.classList.add('locked');
  const f=$('#snf');if(f){$('#snote').focus();f.onsubmit=async ev=>{ev.preventDefault();const n=$('#snote').value;if(!n.trim())return;SHEETNOTE=false;await patch(id,{},n);if(SHEET===id)openSheet(id)}}}
function closeSheet(){SHEET=null;SHEETNOTE=false;const el=$('#pv-sheet');if(el)el.remove();if(!DRAWER)document.body.classList.remove('locked')}
/* ---------- Pulse redesign, 2026-10-16 (Claude Design handoff, Phase 1: C1-C13) ---------- */
const PIN_SVG=f=>`<svg class="pinsvg" viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M5.5 1.5h5l-.8 4.2 2.6 2.6v1.2H8.6V14L8 15.2 7.4 14V9.5H3.7V8.3l2.6-2.6z" fill="${f?'currentColor':'none'}" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg>`;
const PHONEQ=matchMedia('(max-width:820px)');const PHONE=()=>PHONEQ.matches;
let CALLALL=false,ISSALL=false,KOPEN=false,POPEN=false;const TRKOPEN={};
const joinAnd=xs=>xs.length<2?(xs[0]||''):xs.slice(0,-1).join(', ')+' and '+xs[xs.length-1];
const TYPEW={customer:'Customer',internal:'Internal',partner:'Partner'};
function evLine(f){if(f.ev_state==='not_heard')return f.last_evidence?`Not heard · last evidence ${fmt(f.last_evidence)}`:'Not heard · no evidence on file';return `Heard ${fmt(f.last_evidence)}`}
function evCount(f){if(f.ev_state==='not_heard')return '<span class="fc dash" aria-label="no evidence">—</span>';if(f.ev_state==='nothing_raised')return '<span class="fc">Nothing raised</span>';
  return `<span class="fc">${[f.live+' live',f.stuck?f.stuck+' stuck':'',f.quiet?f.quiet+' quiet':''].filter(Boolean).join(' · ')}</span>`}
const mk=st=>`<span class="pv-mk ${st==='raised'?'raised':st==='nothing_raised'?'nothing':'nh'}" aria-hidden="true"></span>`;
function verdict(t){if(t.heard>=t.total)return '';if(t.heard<=t.total/2)return 'Mostly not heard: these counts are incomplete.';
  const n=t.not_heard.map(f=>f.name);return n.length<=2?`${joinAnd(n)} not heard; their counts are unknown.`:`${n.length} forums not heard; their counts are unknown.`}
function drivers(c){return [c.live_high_visible?c.live_high_visible+' High customer-visible':'',c.live_high?c.live_high+' High internal':'',c.live_medium?c.live_medium+' Medium':'',c.live_low?c.live_low+' Low':'',c.stuck?c.stuck+' stuck':'',c.quiet?c.quiet+' quiet':'',c.candidate?c.candidate+' open call'+(c.candidate>1?'s':''):'',c.at_your_level?c.at_your_level+' register item'+(c.at_your_level>1?'s':''):''].filter(Boolean).join(' · ')}
function ptsBar(x,h){const w=v=>Math.min(100,v/60*100);const t=w(x.teams_points),r=Math.min(100-t,w(x.registers_points));
  return `<div class="pv-bar" style="height:${h||10}px" role="img" aria-label="Points lost: teams raised ${x.teams_points}, your registers ${x.registers_points}"><i class="t" style="width:${t}%"></i><i class="r" style="width:${r}%"></i></div>`}
function teamsCell(x,P){if(x.teams_points>0)return {v:x.teams_points+(x.teams_points===1?' pt':' pts'),n:[x.live?x.live+' live':'',x.quiet?x.quiet+' quiet':'',x.calls?x.calls+' call'+(x.calls>1?'s':''):''].filter(Boolean).join(' · ')};
  const sc=(P.forums||[]).find(f=>f.key==='deployment-scrum');
  if(x.open_project===false)return {v:'No open project',n:''};
  if(x.open_project==null)return {v:'None raised',n:'Project status not set'};
  if(sc&&!sc.evidence_in_window)return {v:'Not heard',n:sc.last_evidence?'Last evidence '+fmt(sc.last_evidence):'No evidence on file',nh:true};
  return {v:'None raised',n:sc?'Heard '+fmt(sc.last_evidence):''}}
function callsCard(P,cs){
  const shown=CALLALL?cs:cs.slice(0,3);
  const tag=t=>`<span class="pv-tag">${esc(t)}</span>`;
  const rows=shown.map(c=>{const i=ITEMS.find(z=>z.id===c.id)||{};
    const bd=[c.severity?`<span class="t-sev ${esc(String(c.severity).toLowerCase())}">${esc(c.severity)}</span>`:'',tag(c.category==='knowledge'?'Knowledge risk':'Issue'),c.account?tag(c.account):'',c.track?tag(TRK(c.track)):(c.forum?tag(fname(c.forum)):'')].join('');
    return `<div class="pv-call"><div class="id">${esc(c.id)}</div><button type="button" class="ttl" data-open="${esc(c.id)}">${esc(c.title)}</button><div class="why">${esc(c.reason_line||c.reason_text)}</div><div class="bd">${bd}</div><div class="acts"><button type="button" class="btn primary" data-esc="escalate" data-id="${esc(c.id)}">Escalate</button><button type="button" class="btn" data-esc="decline" data-id="${esc(c.id)}">Leave with team</button></div></div>`}).join('');
  const more=cs.length>3?`<button type="button" class="pv-lk" data-callall>${CALLALL?'Show fewer':'Show all '+cs.length}</button>`:'';
  const el=(P.escalated_live||[]);
  const foot=el.length?`<div class="pv-foot">Already escalated and still live: ${el.map(e=>`<a href="#" data-open="${esc(e.id)}">${esc(e.id)} ${esc(e.title)}</a> → <a href="#" data-open="${esc(e.watch)}">Watch ${esc(e.watch)}</a>`).join('; ')}</div>`:'';
  return `<section class="pv-card acc pv-calls" aria-label="Needs your call"><h2 class="pv-h acc">Needs your call <span class="pv-badge">${cs.length}</span></h2>${rows||'<p class="pv-empty">Nothing needs your call.</p>'}${more}${foot}</section>`}
function pinnedCard(P){const x=(P.health||[]).find(h=>h.pinned);if(!x)return '';
  const bc=BANDCLS[x.band];
  return `<button type="button" class="pv-card pv-pin" data-pf="account" data-val="${esc(x.account)}" aria-label="${esc(x.account)}, pinned account, ${esc(th(x).big)} ${esc(th(x).unit)}, ${esc(x.label)}. Select to see its items.">
   <span class="l1"><span class="nm">${esc(x.account)}</span><span class="pt">${PIN_SVG(1)} Pinned · ${esc(TYPEW[x.type]||'Customer')}</span><span class="vi">View items ›</span></span>
   <span class="l2"><span class="sc ${bc}">${esc(th(x).big)}</span><span class="of">${esc(th(x).unit)}</span><span class="bw ${bc}">${esc(x.label)}</span></span>
   <span class="pv-spk">${spark(x,260,40)}<span class="pv-spkn">${esc(th(x).note)}${x.series_start?' · since '+fmt(x.series_start):''}</span></span>
   <span class="pv-leg"><span>Teams raised <b>${x.teams_points?x.teams_points+' pts':'none'}</b></span><span>Your registers <b>${x.registers_points?x.registers_points+' pts':'none'}</b></span></span>
   <span class="pv-drv">${esc(drivers(x.components)||'No signals')}</span>
   ${PHONE()?'':'<span class="pv-foot">Pin a different account from Account health below.</span>'}</button>`}
function evidenceCard(P){const e=P.evidence;if(!e)return '';
  const order=[...P.forums].sort((a,b)=>({raised:0,nothing_raised:1,not_heard:2}[a.ev_state]-{raised:0,nothing_raised:1,not_heard:2}[b.ev_state]));
  const strip=`<div class="pv-strip" role="img" aria-label="${e.raised} forums heard with items raised, ${e.nothing_raised} heard with nothing raised, ${e.not_heard} not heard">${order.map(f=>mk(f.ev_state).replace('aria-hidden="true"',`title="${esc(f.name)}: ${esc(evLine(f))}" aria-hidden="true"`)).join('')}</div>`;
  const leg=PHONE()?`<div class="pv-evl ph">${mk('raised')} Raised <b>${e.raised}</b> · ${mk('nothing_raised')} Nothing raised <b>${e.nothing_raised}</b> · ${mk('not_heard')} Not heard <b>${e.not_heard}</b></div>`
    :`<div class="pv-evl"><span>${mk('raised')}Heard, items raised <b>${e.raised}</b></span><span>${mk('nothing_raised')}Heard, nothing raised <b>${e.nothing_raised}</b></span><span>${mk('not_heard')}Not heard <b>${e.not_heard}</b></span></div>`;
  const sil=e.not_heard>e.total/2?'<p class="pv-sil">Silence below mostly means not heard, not all clear.</p>':'';
  const byT=(e.new7_by_track||[]).map(t=>`${esc(t.name.replace(/ governance$/,''))} ${t.new7}`).join(' · ');
  const foot=PHONE()?`<button type="button" class="pv-foot pv-newrow" data-pf="new" data-val="7"><b>${e.new7} new</b> in the last 7 days ›</button>`
    :`<div class="pv-foot"><b>${e.new7} new</b> in the last 7 days${byT?' · '+byT:''} · <button type="button" class="pv-lk" data-pf="new" data-val="7">Show new</button></div>`;
  return `<section class="pv-card pv-ev" aria-label="Evidence this window"><h2 class="pv-h">Evidence this window</h2><div class="hl">Heard from ${e.heard} of ${e.total} forums</div>${strip}${leg}${sil}${foot}</section>`}
function accountsSec(P,fk,fv){
  const ph=PHONE();
  const pinBtn=x=>`<button type="button" class="pinbtn${x.pinned?' on':''}" data-pin="${esc(x.account)}" aria-pressed="${x.pinned}" aria-label="${x.pinned?esc(x.account)+' is pinned to the top':'Pin '+esc(x.account)+' to the top'}">${PIN_SVG(x.pinned)}<span>${x.pinned?'Pinned':'Pin'}</span></button>`;
  const rows=P.health.map(x=>{const bc=BANDCLS[x.band],tc=teamsCell(x,P),on=fk==='account'&&fv===x.account;
    const rg=x.registers_points?{v:x.registers_points+' pts',n:x.components.at_your_level+' item'+(x.components.at_your_level>1?'s':'')}:{v:'None',n:''};
    if(ph){const l3=`${x.teams_points?'Teams '+x.teams_points+(x.teams_points===1?' pt':' pts'):tc.v==='No open project'?'Teams: no open project':tc.v==='Not heard'?'Teams: not heard':'Teams: none raised'} · ${x.registers_points?'Your registers '+x.registers_points+' pts':'Your registers: none'}`;
      return `<div class="pv-arow ph${x.pinned?' pinned':''}${on?' sel':''}"><button type="button" class="af" data-pf="account" data-val="${esc(x.account)}"><span class="a1"><span class="an">${esc(x.account)}</span><b class="as ${bc}">${esc(th(x).big)}</b><span class="of">${esc(th(x).unit)}</span><b class="ab ${bc}">${esc(x.label)}</b></span>${spark(x,200,22)}<span class="a3">${esc(l3)}</span></button>${pinBtn(x)}</div>`}
    return `<div class="pv-arow${x.pinned?' pinned':''}${on?' sel':''}"><button type="button" class="af" data-pf="account" data-val="${esc(x.account)}">
      <span class="c-ac"><span class="an">${esc(x.account)}</span> <span class="at">${esc(TYPEW[x.type]||'Customer')}</span></span>
      <span class="c-sc"><b class="as ${bc}">${esc(th(x).big)}</b><span class="of"> ${esc(th(x).unit)}</span> <b class="ab ${bc}">${esc(x.label)}</b></span>
      <span class="c-bar">${spark(x,170,26)}</span>
      <span class="c-n"><b${tc.nh?' class="nhv"':''}>${tc.nh?mk('not_heard'):''}${esc(tc.v)}</b><small>${esc(tc.n)}</small></span>
      <span class="c-n"><b>${esc(rg.v)}</b><small>${esc(rg.n)}</small></span>
      <span class="c-drv">${esc(drivers(Object.assign({},x.components,{at_your_level:0}))||(x.registers_points?'Register items only':''))}</span>
      <span class="c-ch" aria-hidden="true">›</span></button>${pinBtn(x)}</div>`}).join('');
  const hd=ph?'':`<div class="pv-arow hd" aria-hidden="true"><span class="af"><span>Account</span><span>7-day trend</span><span>Team load, daily</span><span>Teams raised</span><span>Your registers</span><span class="c-drv">What drives it</span><span></span></span><span class="c-pinh">Pin to top</span></div>`;
  const q=(P.quiet_accounts||[]).length?`No signals this window: ${esc(P.quiet_accounts.join(', '))}. `:'';
  const ua=(P.unattributed||[]).length?`<div>Not scored because it names more than one account: ${P.unattributed.map(u=>`<a href="#" data-open="${esc(u.id)}">${esc(u.id)}</a> (${esc(u.accounts.join(', '))})`).join('; ')}. Set its account to count it once.</div>`:'';
  return `<section class="group pv-ah"><h2 class="ghead">Account health${ph?'':'<span class="sub">7-day trend in the load of open issues teams raised · load also counts your register items · select a row to filter · pin one account to the top</span>'}</h2>${hd}${rows}
    <div class="pv-afoot"><div>${q}The line is the daily team-raised load since forum-by-forum capture began; the 7-day trend starts ${P.health&&P.health[0]&&P.health[0].trend_from?fmt(P.health[0].trend_from):'after a week of history'}. Worsening or Improving means a move of at least 5 points and 15%. Friction from evidence, not customer sentiment. <button type="button" class="pv-lk" data-guide="How load and trend are calculated">How issues are weighted</button></div>${ua}</div></section>`}
function govSec(P,fk,fv){const ph=PHONE();
  const tr=(P.tracks||[]).map(t=>{const fs=t.forums.map(k=>P.forums.find(f=>f.key===k)).filter(Boolean).sort((a,b)=>({raised:0,nothing_raised:1,not_heard:2}[a.ev_state]-{raised:0,nothing_raised:1,not_heard:2}[b.ev_state]));
    const cnt=[t.live+' live',t.new7+' new',t.stuck+' stuck',t.candidates+' call'+(t.candidates===1?'':'s'),t.knowledge?t.knowledge+' knowledge risk'+(t.knowledge>1?'s':''):''].filter(Boolean).join(' · ');
    const v=verdict(t);const box=`<div class="pv-hbox"><b>Heard from ${t.heard} of ${t.total} forums</b>${v?`<div class="v">${esc(v)}</div>`:''}</div>`;
    const frows=fs.map(f=>`<button type="button" class="pv-fr${fk==='forum'&&fv===f.key?' on':''}" data-pf="forum" data-val="${esc(f.key)}">${mk(f.ev_state)}<span class="fn">${esc(f.name)}<span class="fs">${esc(evLine(f))}</span></span>${evCount(f)}</button>`).join('');
    const open=!ph||TRKOPEN[t.key];
    return `<div class="pv-trk${fk==='track'&&fv===t.key?' on':''}"><div class="r1"><div class="tt"><button type="button" class="tn" data-pf="track" data-val="${esc(t.key)}">${esc(t.name)}</button><div class="ld">With ${esc(joinAnd(t.leads||[]))}</div></div>${ph?'':`<button type="button" class="btn sm" data-agenda="track:${esc(t.key)}">Open agenda</button>`}</div>
      <div class="cn">${esc(cnt)}</div>${box}${ph?`<div class="pv-2b"><button type="button" class="btn" data-agenda="track:${esc(t.key)}">Open agenda</button><button type="button" class="btn" data-trk="${esc(t.key)}" aria-expanded="${!!TRKOPEN[t.key]}">Forums (${fs.length})</button></div>`:''}${open?`<div class="pv-frs">${frows}</div>`:''}</div>`}).join('');
  return `<section class="group pv-gov"><h2 class="ghead">Your weekly governance${ph?'':'<span class="sub">Select a forum to filter</span>'}</h2>${tr}</section>`}
function pulseHtml(){
  if(!PULSE)return '<div class="empty">The Pulse did not load. Restart the EOS server so it picks up the new version.</div>';
  const P=PULSE,ph=PHONE(),all=ITEMS.filter(i=>i.kind==='pulse'&&i.category!=='knowledge'),know=ITEMS.filter(i=>i.kind==='pulse'&&i.category==='knowledge');
  const fk=Object.keys(PF)[0],fv=fk?PF[fk]:null;
  const trk=fk==='track'?((P.tracks||[]).find(t=>t.key===fv)||{forums:[]}):null;
  const match=i=>!fk||(fk==='account'?i.account===fv:fk==='forum'?i.forum===fv:fk==='track'?trk.forums.includes(i.forum):fk==='new'?isNewI(i):(i._people||[]).includes(fv));
  const scope=all.filter(match);
  let a=scope.filter(i=>PALL||i._state==='live');
  if(Q){const q=Q.toLowerCase();a=a.filter(i=>[i.id,i.title,i.owner,i.account,i.body,(i.people||[]).join(' ')].join(' ').toLowerCase().includes(q))}
  const sv={high:0,mediumhigh:0.5,medium:1,low:2},st={live:0,quiet:1,resolved:2,dropped:3};
  const svk=i=>sv[String(i.severity||'').toLowerCase().replace(/[^a-z]/g,'')]??3;
  const pso=sortOf('pulse');
  /* attention: state, stuck, severity, customer-visible, most recent (C14 head states this order) */
  if(pso.k!=='pulse')a.sort(cmpBy(pso.k,pso.dir));else a.sort((x,y)=>(st[x._state]-st[y._state])||((y._stuck?1:0)-(x._stuck?1:0))||(svk(x)-svk(y))||((y.customer_visible?1:0)-(x.customer_visible?1:0))||String(y.last_seen||'').localeCompare(String(x.last_seen||''))||cmpId(x,y));
  const cs=P.candidates.filter(c=>{const i=ITEMS.find(z=>z.id===c.id);if(!i)return false;if(i.category==='knowledge')return !fk||fk==='new'||(fk==='track'&&i.track===fv)||(fk==='person'&&i.holder===fv)||(fk==='account'&&i.account===fv);return match(i)});
  let h=`<div class="pv"><div class="pv-title"><h2>Pulse</h2><p>Rolling ${P.window.days} days, ${fmt(P.window.start)} to ${fmt(P.window.end)}. What your team-governed forums are carrying. The teams own the work; escalate only what needs you.</p><button type="button" class="btn" data-cprompts>Copilot prompts</button><button type="button" class="pv-lk" data-guide>How to read this page</button></div>`;
  h+=`<div class="pv-today">${callsCard(P,cs)}${pinnedCard(P)}${evidenceCard(P)}</div>`;
  h+=accountsSec(P,fk,fv);
  /* C15: the filter chip is sticky under the header strip */
  const fname2=fk==='forum'?fname(fv):fk==='track'?(trk.name||fv):fk==='new'?'new in the last 7 days':fv;
  let L=fk?`<div class="chips pv-chip" id="pv-issues"><span class="chip">Showing ${fk==='new'?'':esc(fk)+': '}<b>${esc(fname2)}</b></span><button type="button" class="chip x" data-pclear>Clear</button></div>`:'<span id="pv-issues"></span>';
  const lim=rows=>ph&&!ISSALL&&rows.length>4?rows.slice(0,4):rows;
  const showAll=rows=>ph&&rows.length>4?`<button type="button" class="more" data-issall>${ISSALL?'Show fewer':'Show all '+rows.length+' '+(PALL?'issues':'live issues')}</button>`:'';
  const sec=(t,rows,note,ft,hd)=>`<section class="group pv-iss"><h2 class="ghead">${t}<span class="n">${rows.length}</span>${hd||''}</h2>${note?`<p class="gnote">${note}</p>`:''}${lim(rows).map(prow).join('')||`<div class="empty" style="padding:16px">None in the Pulse.${fk==='account'||fk==='person'?' Anything on your registers is listed below.':''}</div>`}${showAll(rows)}${ft||''}</section>`;
  const focus=fk==='account'||fk==='person';
  const linked=regLinked(P,fk,fv,scope.length);
  const foot=allToggle(scope);
  if(!(focus&&!scope.length&&linked)){
    if(fk==='person'){const own=a.filter(i=>(i._owners||[]).includes(fv)),inv=a.filter(i=>!(i._owners||[]).includes(fv));
      L+=sec(`Owned by ${esc(fv)}`,own,'','',sortMini(a.length))+sec(`${esc(fv)} named, someone else owns`,inv,`${esc(fv)} is named on these in the evidence (a statement, a commitment or a stated role) but is not the owner. The owner is on each row.`,foot)}
    else L+=sec(PALL?'All issues':'Live issues',a,'',foot,sortMini(a.length));
  }
  L+=linked;
  h+=`<div class="pv-g2"><div class="pv-col">${L}</div><div class="pv-col">${govSec(P,fk,fv)}</div></div>`;
  const kn=knowHtml(know,fk,fv,trk);
  const peo=peopleHtml(P,fk,fv);
  if(ph){const kl=know.filter(i=>i._state==='live'),kc=kl.filter(i=>i._candidate).length,kq=know.filter(i=>i._state==='quiet').length;
    h+=`<button type="button" class="pv-sum" data-kopen aria-expanded="${KOPEN}"><b>Knowledge concentration</b> · ${kl.length} live${kc?' · '+kc+' needs your call':''}${kq?' · '+kq+' quiet':''} <span aria-hidden="true">${KOPEN?'⌃':'›'}</span></button>${KOPEN?kn:''}`;
    h+=`<button type="button" class="pv-sum" data-popen aria-expanded="${POPEN}"><b>People carrying the most</b> · ${P.people.length} people · top: ${esc(P.people.slice(0,3).map(r=>r.name).join(', '))} <span aria-hidden="true">${POPEN?'⌃':'›'}</span></button>${POPEN?peo:''}`}
  else h+=`<div class="pv-g3"><div class="pv-col">${kn}</div><div class="pv-col">${peo}</div></div>`;
  return h+'</div>'}
/* Phase 2, C18: top 8, grouped columns, Sole removed, zero shown as a dot */
let PPLALL=false;
function peopleHtml(P,fk,fv){const ph=PHONE();
  const src=fk==='person'?P.people.filter(r=>r.name===fv):P.people;const pp=PPLALL||fk==='person'?src:src.slice(0,8);
  const z=n=>n?`${n}`:'<span class="z" aria-label="none">·</span>';
  const rows=pp.map(r=>`<button type="button" class="ppl pv-pp${fk==='person'&&fv===r.name?' on':''}" data-pf="person" data-val="${esc(r.name)}" title="${esc(r.forums.map(fname).join(', ')||'No forum')}"><span>${esc(r.name)}</span><span class="num">${z(r.owns??r.pulse)}</span><span class="num">${z(r.involved??0)}</span><span class="num">${z(r.delegated)}</span></button>`).join('');
  const more=fk!=='person'&&P.people.length>8?`<button type="button" class="more pv-pmore" data-pplall>${PPLALL?'Show top 8':'Show all '+P.people.length+' people'}</button>`:'';
  return `<section class="group pv-ppl"><h2 class="ghead">People carrying the most<span class="sub">${PPLALL||fk==='person'?P.people.length+' people':'top 8 of '+P.people.length}</span>${ph?'':'<span class="sub r">Select a name to filter</span>'}</h2>
   <div class="ppl pv-pp g" aria-hidden="true"><span></span><span class="gl">In the Pulse</span><span class="gl r">Your registers</span></div>
   <div class="ppl pv-pp h"><span>Person</span><span class="num">Owns</span><span class="num">Involved</span><span class="num">Delegated</span></div>${rows}${more}
   <p class="gnote pv-pn">Owns: owner of a live Pulse issue. Involved: named in the evidence on a live issue, not the owner. Delegated: open delegated or awaited items on your registers.</p></section>`}
/* Phase 2, C19: knowledge concentration stays the one view of single points of failure */
const KCOV={none:['No backup','red'],unknown:['Backup unknown','red'],partial:['Partly covered',''],covered:['Covered','grn']};
const TRK=k=>((PULSE&&PULSE.tracks)||[]).find(t=>t.key===k)?.name||k||'';
const bkp=i=>i.backup?i.backup:(i.coverage||'unknown')==='unknown'?'not confirmed':'none named';
function xpo(i){return (i.exposure||[]).map(x=>{x=String(x);return x==='customer'&&i.account?'Customer · '+i.account:cap(x)})}
function krow(i){const cov=KCOV[i.coverage||'unknown']||KCOV.unknown;const cls=i._state==='live'?'':i._state==='quiet'?' dim':' done';
  const bd=`<span class="pv-b ${cov[1]}">${cov[0]}</span>${xpo(i).map(x=>`<span class="pv-b">${esc(x)}</span>`).join('')}${i.escalated_to?`<span class="pv-b esc">Escalated · ${esc(i.escalated_to)}</span>`:i._candidate?'<span class="pv-b call">Needs your call</span>':''}${i.absence_date?`<span class="pv-b">Away from ${fmt(i.absence_date)}</span>`:''}${i._state!=='live'?`<span class="pv-b">${cap(i._state)}</span>`:''}`;
  return `<div class="pv-ir pv-kr${SEL===i.id?' sel':''}${cls}" data-kid="${esc(i.id)}"><div class="id">${esc(i.id)}</div>
   <div class="bd"><button type="button" class="ttl" data-open="${esc(i.id)}">${PHONE()?`<span class="iid">${esc(i.id)}</span>`:''}${esc(i.title)}</button><div class="bdg">${bd}</div><div class="ow">Held by ${esc(i.holder||'?')} · Backup: ${esc(bkp(i))}</div>${i.mitigation?`<div class="nx">${esc(plain(i.mitigation))}</div>`:''}</div></div>`}
let KALL=false;
function knowHtml(know,fk,fv,trk){
  if(fk&&fk!=='person'&&fk!=='track'&&fk!=='account')return '';
  const k=know.filter(i=>!fk||(fk==='person'?(i.holder===fv||(i.backup||'').includes(fv)):fk==='track'?i.track===fv:i.account===fv));
  const live=k.filter(i=>i._state==='live'),quiet=k.filter(i=>i._state==='quiet');
  const cr={none:0,unknown:1,partial:2,covered:3};
  const rows=(KALL?k:live).slice().sort((a,b)=>((a._state==='live'?0:1)-(b._state==='live'?0:1))||((b._candidate?1:0)-(a._candidate?1:0))||((cr[a.coverage||'unknown']??1)-(cr[b.coverage||'unknown']??1))||String(b.last_seen||'').localeCompare(String(a.last_seen||'')));
  const qd=quiet.map(i=>`${i.id} (${(KCOV[i.coverage||'unknown']||KCOV.unknown)[0].toLowerCase()}${i.backup?', backup '+i.backup:''})`);
  const foot=`<div class="pv-kf">${quiet.length?`${quiet.length} quiet: ${esc(joinAnd(qd))}. `:''}Live for 45 days after last evidence.${quiet.length||KALL?` <button type="button" class="pv-lk" data-kall>${KALL?'Hide quiet':'Show quiet'}</button>`:''}</div>`;
  return `<section class="group pv-kn"><h2 class="ghead">Knowledge concentration<span class="sub">${live.length} live</span><span class="sub r">One person holds what a customer or release depends on</span></h2>${rows.map(krow).join('')||'<div class="empty" style="padding:16px">None.</div>'}${foot}</section>`}
async function pinAccount(name){const x=(PULSE.health||[]).find(h=>h.account===name);if(x&&x.pinned)return;
  const r=await fetch('/api/pulse/pin',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({account:name})});
  if(!r.ok){toast('Pin failed · '+name);return}PULSE=await r.json();
  SESSION.unshift({id:name,what:'pinned to the top',t:new Date().toLocaleTimeString([], {hour:'numeric',minute:'2-digit'})});
  toast(name+' pinned to the top');render()}
PHONEQ.addEventListener('change',()=>render());
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
/* Phase 2, C17: governance meeting view. One model feeds the presentable view and "Copy as text". */
function agendaModel(k){const P=PULSE,wk=dn(TODAY)-7*864e5,fs=i=>dn(String(i.first_seen||TODAY).slice(0,10));
  let it,m,multi=false,t=null;
  const dt=new Date(dn(TODAY)),day=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][dt.getUTCDay()];
  if(k.startsWith('track:')){t=(P.tracks||[]).find(x=>x.key===k.slice(6))||{name:k,forums:[],leads:[],not_heard:[],heard:0,total:0};multi=true;
    it=ITEMS.filter(i=>i.kind==='pulse'&&i.category!=='knowledge'&&t.forums.includes(i.forum));
    m={kicker:'Weekly governance review',title:t.name,sub:`${day}, ${fmt(TODAY)} · with ${joinAnd(t.leads||[])} · evidence window ${fmt(P.window.start)} to ${fmt(P.window.end)}`,
      forums:t.forums.map(x=>P.forums.find(f=>f.key===x)).filter(Boolean)}}
  else{const f=P.forums.find(x=>x.key===k)||{name:k,key:k};it=ITEMS.filter(i=>i.kind==='pulse'&&i.category!=='knowledge'&&i.forum===k);
    m={kicker:'Governance review',title:f.name,sub:`${day}, ${fmt(TODAY)} · owner ${f.owner||'TBC'} · evidence window ${fmt(P.window.start)} to ${fmt(P.window.end)}`,forums:[f]}}
  const nh=m.forums.filter(f=>f.ev_state==='not_heard');
  m.banner=nh.length?{h:`Heard from ${m.forums.length-nh.length} of ${m.forums.length} forum${m.forums.length>1?'s':''} this window`,
    t:`Not heard: ${joinAnd(nh.map(f=>`${f.name} (${f.last_evidence?'last evidence '+fmt(f.last_evidence):'no evidence on file'})`))}. Ask for status before reading these counts as calm.`}:null;
  const live=it.filter(i=>i._state==='live');
  const sevw=i=>[i.severity,i.customer_visible?'customer-visible':'internal'].filter(Boolean).join(' · ');
  const own=i=>i.owner?'owner '+i.owner:'no owner named';
  const nx=i=>i.next_action?'Next: '+plain(i.next_action).replace(/\.$/,'')+'.':'';
  const kn=multi?ITEMS.filter(i=>i.kind==='pulse'&&i.category==='knowledge'&&i.track===t.key):[];
  const cand=P.candidates||[];const why=id=>(cand.find(c=>c.id===id)||{}).reason_line||'';
  const S=[];
  S.push({t:'Stuck: what unblocks it, who decides, by when',items:live.filter(i=>i._stuck).map(i=>({id:i.id,title:i.title,b:i,meta:`Owner: ${i.owner||'no owner named'} · last raised ${fmt(i.last_seen||i.first_seen)}${multi?' · '+fname(i.forum):''}`,next:nx(i)}))});
  S.push({t:'Needs a decision or escalation',items:[...live.filter(i=>i._candidate&&!i._stuck).map(i=>({id:i.id,title:i.title,meta:`${sevw(i)} · ${own(i)} · ${i.account||'no account'}`,next:why(i.id)||('Test: '+(P.tests[i._candidate]||i._candidate))})),
    ...kn.filter(i=>i._candidate&&i._state==='live').map(i=>({id:i.id,title:i.title,meta:`Knowledge risk · held by ${i.holder||'?'}${i.absence_date?' · away from '+fmt(i.absence_date):''} · backup ${bkp(i)}`,next:why(i.id)||'Decide: who holds this now, and when the handover is confirmed.'}))]});
  const rest=live.filter(i=>!i._stuck&&!i._candidate);
  S.push({t:'New this week',items:rest.filter(i=>fs(i)>=wk).map(i=>({id:i.id,title:i.title,meta:`${sevw(i)} · ${own(i)} · ${i.account||'no account'}${multi?' · '+fname(i.forum):''}`,next:nx(i)}))});
  const older=rest.filter(i=>fs(i)<wk);
  if(older.length)S.push({t:'Still open',items:older.map(i=>({id:i.id,title:i.title,meta:`${sevw(i)} · ${own(i)} · ${i.account||'no account'} · raised since ${fmt(i.first_seen)}`,next:nx(i)}))});
  S.push({t:'Gone quiet: resolved, or dropped?',items:it.filter(i=>i._state==='quiet').map(i=>({id:i.id,title:i.title,meta:`${[i.severity,i.account].filter(Boolean).join(' · ')} · ${own(i)} · last raised ${fmt(i.last_seen||i.first_seen)}`,next:''}))});
  if(multi)S.push({t:'Who backs up whom, and by when',items:kn.filter(i=>i._state==='live'||i._state==='quiet').map(i=>({id:i.id,title:i.title,meta:`${i.holder||'?'} · backup ${bkp(i)}${(i.exposure||[]).length?' · '+(i.exposure||[]).map(x=>String(x)==='customer'&&i.account?'customer exposure ('+i.account+')':String(x)+' exposure').join(', '):''}${i._state==='quiet'?' · quiet; confirm still current':''}`,next:i.mitigation?plain(i.mitigation):''}))});
  m.sections=S;
  m.counts=multi?[t.live+' live',t.new7+' new',t.stuck+' stuck',t.candidates+' call'+(t.candidates===1?'':'s'),t.quiet+' quiet'].join(' · '):[live.length+' live',it.filter(i=>i._state==='quiet').length+' quiet'].join(' · ');
  m.escalated=it.filter(i=>i.escalated_to).map(i=>`${i.id} → Watch ${i.escalated_to}`);
  return m}
function agendaMd(k){const m=agendaModel(k);const L=[`# ${m.title}: ${m.kicker.toLowerCase()}`,'',m.sub,''];
  if(m.banner)L.push(`${m.banner.h}. ${m.banner.t}`,'');
  m.sections.forEach((s,n)=>{L.push(`## ${n+1}. ${s.t}`,'');if(!s.items.length)L.push('- None.');s.items.forEach(x=>L.push(`- ${x.id} ${plain(x.title)}. ${x.meta}.${x.next?' '+x.next:''}`));L.push('')});
  L.push('## This track','',m.counts,'');m.forums.forEach(f=>L.push(`- ${f.name}: ${evLine(f)}`));
  if(m.escalated.length)L.push('','## Escalated to you','',...m.escalated.map(e=>'- '+e));
  return L.join('\n')}
let MEET=null;
function openAgenda(k){MEET=k;const m=agendaModel(k);
  let el=$('#pv-meet');if(!el){el=document.createElement('div');el.id='pv-meet';el.setAttribute('role','dialog');el.setAttribute('aria-modal','true');document.body.appendChild(el)}
  const bd=b=>b?ibadges(b):'';
  const secs=m.sections.map((s,n)=>`<section class="ms"><h3><span class="nm">${n+1}</span>${esc(s.t)}</h3>${s.items.length?s.items.map(x=>`<div class="mi"><span class="id">${esc(x.id)}</span><div><button type="button" class="mt" data-mopen="${esc(x.id)}">${esc(x.title)}</button>${x.b?`<div class="bdg">${bd(x.b)}</div>`:''}<div class="mm">${esc(x.meta)}</div>${x.next?`<div class="mn">${esc(x.next)}</div>`:''}</div></div>`).join(''):'<div class="mi none">None.</div>'}</section>`).join('');
  const rail=`<aside class="mr"><div class="rh">This track</div><div class="rc">${esc(m.counts)}</div><div class="rh">Forums</div>${m.forums.map(f=>`<div class="rf">${mk(f.ev_state)}<div>${esc(f.name)}<small>${esc(evLine(f))}${f.ev_state==='raised'?' · '+f.live+' live':''}</small></div></div>`).join('')}${m.escalated.length?`<div class="rh sep">Escalated to you</div>${m.escalated.map(e=>`<div class="rc">${esc(e)}</div>`).join('')}`:''}</aside>`;
  el.innerHTML=`<div class="mw"><div class="mh"><div><div class="kk">${esc(m.kicker)}</div><h2>${esc(m.title)}</h2><div class="sb">${esc(m.sub)}</div></div>
   <div class="mb"><button type="button" class="btn primary" data-mcopy>Copy as text</button><button type="button" class="btn" data-mfs>${document.fullscreenElement?'Exit full screen':'Present full screen'}</button><button type="button" class="btn" data-mclose>Close</button></div></div>
   ${m.banner?`<div class="mban"><span class="hx" aria-hidden="true"></span><div><b>${esc(m.banner.h)}</b><p>${esc(m.banner.t)}</p></div></div>`:''}
   <div class="mg"><div class="msecs">${secs}</div>${rail}</div></div>`;
  document.body.classList.add('locked');el.scrollTop=0;el.focus&&el.setAttribute('tabindex','-1');el.focus()}
function closeMeet(){MEET=null;if(document.fullscreenElement)document.exitFullscreen().catch(()=>{});const el=$('#pv-meet');if(el)el.remove();if(!DRAWER&&!SHEET)document.body.classList.remove('locked')}
document.addEventListener('fullscreenchange',()=>{const b=document.querySelector('[data-mfs]');if(b)b.textContent=document.fullscreenElement?'Exit full screen':'Present full screen'});
async function escalateP(id,decision){
  const r=await fetch('/api/pulse/'+encodeURIComponent(id)+'/escalate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({decision})});
  if(!r.ok){toast('Save failed · '+id);return}const j=await r.json();
  SESSION.unshift({id,what:j.watch?'escalated to '+j.watch:'left with team',t:new Date().toLocaleTimeString([], {hour:'numeric',minute:'2-digit'})});
  toast(j.watch?`${id} escalated · ${j.watch} is on your Watch list`:`${id} left with the team`);
  await load();if(SHEET===id)openSheet(id);if(DRAWER==='item'&&SEL===id)openDrawer(id)}
/* ---------- panel ---------- */
function layout(){const open=!!DRAWER;const dock=open&&innerWidth>=1100&&DRAWER==='item';
  document.body.classList.toggle('docked',dock);$('#scrim').style.display=open&&!dock?'block':'none';$('#drawer').classList.toggle('open',open);document.body.classList.toggle('locked',open&&!dock)}
function showDrawer(kind){DRAWER=kind;layout()}
function closeDrawer(){DRAWER=null;SEL=null;layout();render()}
addEventListener('resize',layout);
addEventListener('keydown',e=>{if(e.key!=='Escape')return;if(SHEET){closeSheet();return}if(MEET&&!document.fullscreenElement){closeMeet();return}if(DRAWER)closeDrawer()});
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
/* ---------- Briefs tab (2026-10-19): the daily and weekly briefs, in sight, with item IDs that open the item ---------- */
async function loadBriefs(){try{const j=await (await fetch('/api/briefs')).json();BRIEFS=j.briefs||[]}catch(e){BRIEFS=[]}}
async function openBrief(name,from){try{const j=await (await fetch('/api/briefs/'+encodeURIComponent(name)+'?from='+encodeURIComponent(from||''))).json();BRIEF=j;BREAD=true}catch(e){toast('Could not open '+name)}render();if(from==='list')scrollTo(0,0)}
function wkStart(s){const d=new Date(dn(s));const w=(d.getUTCDay()+6)%7;return dn(s)-w*864e5}
function briefsHtml(){
  if(!BRIEFS.length)return '<div class="empty">No briefs in the Briefings folder yet.</div>';
  const thisWk=wkStart(TODAY),lastWk=thisWk-7*864e5,g={a:[],b:[],c:[]};
  for(const b of BRIEFS){const w=wkStart(b.date);(w>=thisWk?g.a:w>=lastWk?g.b:g.c).push(b)}
  const row=b=>`<button type="button" class="bi${BRIEF&&BRIEF.name===b.name?' on':''}" data-brief="${esc(b.name)}"><span class="bd">${WD[new Date(dn(b.date)).getUTCDay()]} ${fmt(b.date)}</span><span class="bk${b.kind==='Weekly'?' w':''}">${esc(b.kind)}</span>${b.date===TODAY?'<span class="bk w">Today</span>':''}</button>`;
  const sec=(l,a)=>a.length?`<h2 class="ghead">${l}<span class="n">${a.length}</span></h2>${a.map(row).join('')}`:'';
  const list=`<nav class="bl" aria-label="Briefs">${sec('This week',g.a)}${sec('Last week',g.b)}${sec('Earlier',g.c)}</nav>`;
  let rd='<div class="br"><div class="empty">Select a brief.</div></div>',toc='';
  if(BRIEF){const r=briefMd(BRIEF.markdown);
    const words=(BRIEF.markdown.match(/\S+/g)||[]).length,mins=Math.max(1,Math.round(words/230));
    toc=r.toc.length?`<nav class="btoc" aria-label="Sections"><div class="p-label">Sections</div>${r.toc.map(x=>`<a href="#${x.id}" data-toc="${x.id}"${x.closed?' class="cl"':''}>${esc(x.t)}</a>`).join('')}</nav>`:'';
    const sel=r.toc.length?`<select class="bsel" data-tocsel aria-label="Jump to section"><option value="">Sections</option>${r.toc.map(x=>`<option value="${x.id}">${esc(x.t)}</option>`).join('')}</select>`:'';
    rd=`<article class="br"><div class="bh"><button type="button" class="btn bback" data-bback>All briefs</button><span>${mins} min read</span>${BRIEF.docx?`<a href="/briefs/${esc(BRIEF.name.replace(/\.md$/,''))}.docx">Word version</a>`:'<span>No Word version yet</span>'}<span class="bp">Briefings/${esc(BRIEF.name)}</span>${sel}</div><div class="md brief">${r.html}</div></article>`}
  return `<div class="bv${BREAD?' reading':''}">${list}${rd}${toc}</div>`}
const IDRE=/\b(C-i3-\d+b?|[ABCDWPKTX]\d{1,3})\b/g;
function linkIds(h){return h.split(/(<code>[\s\S]*?<\/code>|<[^>]+>)/).map((s,k)=>k%2?s:s.replace(IDRE,m=>ITEMS.some(i=>i.id===m)?`<a href="#" class="iid" data-open="${m}">${m}</a>`:m)).join('')}
/* Sections a reader needs open by default; everything else (reference material) starts collapsed. */
const BOPEN=/summary|priorit|risk|my actions|register a|closure|decision required|changes since|this week.s objectives|chief of staff|calibration/i;
const BLABEL=/(Business impact|Why you personally|Why Darryl personally|Risk if delayed|Next step|Expected outcome|Recommended action):\s*/g;
function briefMd(src){
  const inl=t=>linkIds(esc(t).replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>').replace(/(^|[^*])\*([^*\s][^*]*)\*/g,'$1<i>$2</i>'));
  const CO={'Risk':'risk','Decision Required':'dec','Source Note':'src','Bottom Line':'bl1','Image Caption':'cap'};
  /* A paragraph that carries two or more field labels becomes a card, one field per line, Next step highlighted. */
  const fields=t=>{const parts=t.split(BLABEL);if(parts.length<5)return null;
    let h=`<div class="pcard"><div class="pc-lead">${inl(parts[0].trim())}</div><dl>`;
    for(let k=1;k<parts.length;k+=2)h+=`<dt${/Next step|Recommended/.test(parts[k])?' class="nx"':''}>${esc(parts[k])}</dt><dd${/Next step|Recommended/.test(parts[k])?' class="nx"':''}>${inl(parts[k+1].trim())}</dd>`;
    return h+'</dl></div>'};
  const out=[],toc=[];let list=null,tbl=null,fence=null,fbuf=[],co=null,para=[],insec=false,sn=0,secOpen=true;
  const fp=()=>{if(para.length){const t=para.join(' ');const f=fields(t);const cov=/^Email:\s/.test(t);out.push(f||`<p${cov?' class="muted"':''}>${inl(t)}</p>`);para=[]}};
  const flush=()=>{fp();if(list){out.push(`</${list}>`);list=null}if(tbl){out.push('</table></div>');tbl=null}};
  const li=t=>{const m=t.match(/^\*\*([^*]{2,40}):\*\*\s*(.*)$/);if(m)return `<li class="kv${/Next step|Recommended/.test(m[1])?' nx':''}"><span class="k">${esc(m[1])}</span><span class="v">${inl(m[2])}</span></li>`;const f=fields(t);return f?`<li class="lic">${f}</li>`:`<li>${inl(t)}</li>`};
  for(const raw of src.split('\n')){const l=raw.trimEnd();let m;
    if(fence!==null){if(/^```/.test(l)){out.push(fence==='mermaid'?`<div class="chart">Chart (${/xychart/.test(fbuf.join(' '))?'items taken vs disposed':'diagram'}): see the Word version.</div>`:`<pre class="md-pre"><code>${esc(fbuf.join('\n'))}</code></pre>`);fence=null;fbuf=[]}else fbuf.push(raw);continue}
    if((m=l.match(/^```\s*(\w*)/))){flush();fence=m[1]||'';continue}
    if((m=l.match(/^:::\s*\{custom-style="([^"]+)"\}/))){flush();co=CO[m[1]]||'src';out.push(`<div class="co ${co}">`);continue}
    if(/^:::\s*$/.test(l)&&co){flush();out.push('</div>');co=null;continue}
    if(!l.trim()){flush();continue}
    if((m=l.match(/^## (.*)/))){flush();if(insec)out.push('</div></details>');const id='s'+(sn++);const title=m[1].replace(/\*\*/g,'');
      secOpen=BOPEN.test(title);toc.push({id,t:title.replace(/^\d+[a-z]?\.\s*/,'').replace(/`/g,''),closed:!secOpen});
      out.push(`<details class="bsec" id="${id}"${secOpen?' open':''}><summary><h2>${inl(m[1])}</h2></summary><div class="bsb">`);insec=true;continue}
    if((m=l.match(/^(#{1,3}) (.*)/))){flush();out.push(`<h${m[1].length}>${inl(m[2])}</h${m[1].length}>`);continue}
    if((m=l.match(/^\|(.+)\|$/))){fp();if(/^\|[\s|:-]+\|$/.test(l))continue;const cells=m[1].split('|').map(c=>c.trim());if(!tbl){flush();tbl=1;out.push('<div class="tw"><table>');out.push('<tr>'+cells.map(c=>`<th>${inl(c)}</th>`).join('')+'</tr>')}else out.push('<tr>'+cells.map(c=>`<td>${inl(c)}</td>`).join('')+'</tr>');continue}
    if((m=l.match(/^\s*- (.*)/))){fp();if(list!=='ul'){flush();list='ul';out.push('<ul>')}out.push(li(m[1]));continue}
    if((m=l.match(/^\d+\. (.*)/))){fp();if(list!=='ol'){flush();list='ol';out.push('<ol>')}out.push(li(m[1]));continue}
    if(list&&/^\s{2,}\S/.test(raw)){out[out.length-1]=out[out.length-1].replace(/<\/li>$/,' '+inl(l.trim())+'</li>');continue}
    if(list||tbl)flush();
    para.push(l)}
  flush();if(co)out.push('</div>');if(insec)out.push('</div></details>');return {html:out.join(''),toc}}
function jumpSec(id){const d=document.getElementById(id);if(!d)return;d.open=true;d.scrollIntoView({block:'start'})}
document.addEventListener('change',e=>{const s=e.target.closest('[data-tocsel]');if(s&&s.value){jumpSec(s.value);s.value=''}});
/* ---------- Copilot prompts (2026-10-19): Prompt 1 = Delivery track, Prompt 2 = Development track ---------- */
let CPR=null;
async function openPrompts(){try{CPR=await (await fetch('/api/copilot')).json()}catch(e){toast('Could not build the prompts');return}
  SEL=null;const P=CPR.pulse;
  const stp=CPR.steps.map((s,i)=>`<li class="cs ${s[0]}"><span class="ck">${s[0]==='done'?'✓':s[0]==='skip'?'–':i+1}</span><span>${esc(s[1])}</span></li>`).join('');
  const fx=o=>`<section class="cp${o.today&&!o.done?' need':''}"><div class="cp-h"><b>${esc(o.label)}</b><span class="cp-b ${o.today&&!o.done?'y':'n'}">${o.today?(o.done?'Done today':'Today'):'Not today'}</span></div>
    <div class="cp-m">${esc(o.sub)} Last package saved: ${o.last?fmt(o.last):'none'}.</div>
    <button type="button" class="btn${o.today&&!o.done?' primary':''}" data-cpy="${o.id}">Copy ${esc(o.label)}</button>
    <details class="cp-t"><summary>Show ${esc(o.label)} text</summary><textarea readonly id="cpt${o.id}">${esc(o.text)}</textarea></details></section>`;
  const ph=o=>`<section class="cp${o.needed?' need':''}"><div class="cp-h"><span class="cp-n">Prompt ${o.n}</span><b>Pulse · ${esc(o.label)}</b><span class="cp-b ${o.needed?'y':'n'}">${o.needed?'Needed':'Not needed'}</span></div>
    <div class="cp-m">Window ${fmt(o.window[0])} to ${fmt(o.window[1])} · ${o.forums.filter(f=>f.due).length||o.forums.length} forum${(o.forums.filter(f=>f.due).length||o.forums.length)===1?'':'s'} to search · ${o.tracked} tracked issue${o.tracked===1?'':'s'} listed</div>
    <ul class="cp-f">${o.forums.map(f=>`<li class="${f.due?'d':''}"><span>${esc(f.name)}</span><span>${f.due?'search':'heard'} · ${esc(f.why)}</span></li>`).join('')}</ul>
    <button type="button" class="btn${o.needed?' primary':''}" data-cpy="${o.n}">Copy Prompt ${o.n} · ${esc(o.label)}${o.needed?'':' (anyway)'}</button>
    <details class="cp-t"><summary>Show Prompt ${o.n} text</summary><textarea readonly id="cpt${o.n}">${esc(o.text)}</textarea></details></section>`;
  $('#panel').innerHTML=`<div class="p-top">${head('','Copilot')}<h2 class="p-title">Copilot prompts · ${esc(CPR.weekday)}</h2></div>
   <div class="p-sec"><h3 class="p-label">Today</h3><ol class="csteps">${stp}</ol><p class="cp-how">Run each prompt in its own new Copilot chat and paste the answer to Claude. Pulse answers start with "PROMPT 1 OF 2" or "PROMPT 2 OF 2", so they can come back in any order.</p></div>
   <div class="p-sec"><h3 class="p-label">Leadership evidence</h3>${CPR.fixed.map(fx).join('')}</div>
   <div class="p-sec" id="cp-pulse"><h3 class="p-label">Pulse: team-governed forums</h3><div class="cp-adv">${esc(P.advice)}</div><p class="cp-how">Prompt 1 searches the delivery forums, Prompt 2 the development forums, and only those not heard within their cadence.</p>${P.prompts.map(ph).join('')}</div>`;
  showDrawer('prompts');$('#drawer').scrollTop=0;render()}
function copyPrompt(id){const all=[...CPR.fixed.map(o=>({k:o.id,label:o.label,text:o.text})),...CPR.pulse.prompts.map(o=>({k:String(o.n),label:`Prompt ${o.n} (${o.label})`,text:o.text}))];
  const o=all.find(x=>x.k===String(id));if(!o)return;
  if(!o.text){toast(o.label+' text not found in the prompts file');return}
  const done=()=>toast(`${o.label} copied. Paste it into a new Copilot chat.`);
  const fall=()=>{const ta=document.getElementById('cpt'+id);if(!ta)return toast('Copy blocked: open the text and copy it');ta.closest('details').open=true;ta.focus();ta.select();try{document.execCommand('copy')?done():toast('Text selected: press Cmd-C to copy '+o.label)}catch(e){toast('Text selected: press Cmd-C to copy '+o.label)}};
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(o.text).then(done,fall);else fall()}
async function openHelp(sec){const j=await (await fetch('/api/guide')).json();SEL=null;
  $('#panel').innerHTML=`<div class="p-top">${head('','Help')}</div><div class="p-sec md">${md(j.markdown)}</div>`;
  showDrawer('help');$('#drawer').scrollTop=0;render();
  if(sec){const hs=[...document.querySelectorAll('#panel h2, #panel h3')];const h=hs.find(x=>x.textContent.trim().startsWith(sec));if(h)setTimeout(()=>h.scrollIntoView({block:'start'}),30)}}
$('#helpBtn').onclick=()=>openHelp('');
load();
/* ---------- Live refresh (2026-10-20): re-fetch when the files change, never while you are editing ---------- */
let VER=null;
function busy(){const ae=document.activeElement;const typing=ae&&(ae.tagName==='INPUT'||ae.tagName==='TEXTAREA');return !!(DRAWER||SHEET||typing)}
async function checkVersion(){try{const j=await (await fetch('/api/version',{cache:'no-store'})).json();
  if(VER===null){VER=j.version;return}
  if(j.version!==VER){if(busy())return;VER=j.version;await load();if(VIEW==='briefs')render();toast('Updated from the files')}}catch(e){}}
setInterval(checkVersion,30000);
document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible')checkVersion()});
window.addEventListener('focus',checkVersion);
/* ?theme=light|dark forces a scheme (useful for screenshots); ?open=ID opens an item after load. */
(()=>{const t=new URLSearchParams(location.search).get('theme');if(t)document.documentElement.dataset.theme=t})();
</script></body></html>
"""


def data_version() -> str:
    """Fingerprint of Registers/**/*.md and Briefings/*.md mtimes (added 2026-10-20, live refresh)."""
    import hashlib
    h = hashlib.sha1()
    for k in sorted(_snapshot().items()):
        h.update(f"{k[0]}:{k[1]}".encode())
    if BRIEFS_DIR.exists():
        for f in sorted(BRIEFS_DIR.glob("*.md")):
            try:
                h.update(f"{f.name}:{f.stat().st_mtime}".encode())
            except FileNotFoundError:
                pass
    return h.hexdigest()[:16]


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
