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
import eos_products as PR  # noqa: E402  (Products tab, added 2026-10-21)
import eos_review as V  # noqa: E402  (Weekly review workbook, added 2026-10-27)

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
        tf = [f for f in forums if f.get("track") == track and f.get("active", True)]
        rows = []
        for f in tf:
            due, why = _forum_due(f, today)
            rows.append({"key": f.get("key"), "name": f.get("name"), "aliases": f.get("aliases") or [],
                         "cadence": f.get("cadence") or "", "due": due, "why": why,
                         "last_evidence": f.get("last_evidence") or ""})
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
        today_s = today.isoformat()
        touched_today = any(r["last_evidence"] == today_s for o in need for r in o["forums"])
        still_due = sum(1 for o in need for r in o["forums"] if r["due"])
        base = (" and ".join(f'Pulse Prompt {o["n"]} ({o["label"]})' for o in need)
                + (", each in its own new Copilot chat" if len(need) == 2 else ""))
        if touched_today:
            steps.append(("partial", base + f", partial: ran today, {still_due} forum(s) still not heard within cadence"))
        else:
            steps.append(("todo", base))
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


# ----------------------------------------------------------------------------- weekly review (2026-10-27)

REVIEW_PREVIEWS: dict = {}

def review_status() -> dict:
    """What the Weekly review panel needs: this week's workbook, the last return, the reviewer roster."""
    log = V._log()
    mf = V.latest_manifest()
    wb = None
    if mf:
        x = mf.with_name(mf.name.replace(".manifest.json", ".xlsx"))
        if x.exists():
            m = json.loads(mf.read_text())
            wb = {"date": m.get("date"), "file": x.name, "rows": len(m.get("rows", {}))}
    today = dt.date.fromisoformat(R.today())
    wed = today + dt.timedelta(days=(2 - today.weekday()) % 7)
    return {"today": R.today(), "weekday": today.strftime("%A"), "next_send": wed.isoformat(),
            "workbook": wb, "sent": log.get("sent", [])[-6:], "returned": log.get("returned", [])[-6:],
            "reviewers": V.REVIEWERS, "verdicts": V.VERDICTS}


# ----------------------------------------------------------------------------- git

def git(*args) -> tuple[int, str]:
    try:
        p = subprocess.run(["git", *args], cwd=R.ROOT, capture_output=True, text=True, timeout=30)
        return p.returncode, (p.stdout + p.stderr).strip()
    except Exception as e:  # git missing, etc.
        return 1, str(e)


_PUSH_STATE = {"busy": False, "last_fail": 0.0}


def git_push_async() -> None:
    """Added 2026-10-28: after each commit, push to the backup remote in the background so the history exists
    off this Mac (set up by Tools/eos-git-setup.command). No remote, or a push failure, never affects the app;
    a failure is logged at most once a minute and the next commit tries again."""
    import time
    if _PUSH_STATE["busy"]:
        return
    rc, remotes = git("remote")
    if rc != 0 or "origin" not in remotes.split():
        return

    def run():
        _PUSH_STATE["busy"] = True
        try:
            p = subprocess.run(["git", "push", "-q", "origin", "HEAD:main"], cwd=R.ROOT, capture_output=True,
                               text=True, timeout=120, env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
            if p.returncode != 0 and time.time() - _PUSH_STATE["last_fail"] > 60:
                _PUSH_STATE["last_fail"] = time.time()
                sys.stderr.write(f"[push] failed: {(p.stdout + p.stderr).strip()[:200]}\n")
        except Exception as e:
            sys.stderr.write(f"[push] error: {e}\n")
        finally:
            _PUSH_STATE["busy"] = False

    threading.Thread(target=run, daemon=True).start()


def git_commit_all(message: str) -> str:
    """Commit every tracked-text change in the EOS folder (code, docs, evidence), within .gitignore.
    Added 2026-10-16: session edits to Tools/ and the numbered files were sitting uncommitted because
    git_commit only adds Registers and the generated views."""
    if not (R.ROOT / ".git").exists():
        return "no git repo"
    git("add", "-A")
    rc, out = git("commit", "-q", "-m", message)
    if rc == 0:
        git_push_async()
    return "committed" if rc == 0 else f"nothing to commit / {out[:120]}"


def git_commit(message: str) -> str:
    if not (R.ROOT / ".git").exists():
        return "no git repo"
    git("add", "-A", "--", "Registers", "03_Decision_Log.md", "04_Executive_Watch_List.md", "05_Commitments.md", "11_Operational_Pulse.md")
    rc, out = git("commit", "-q", "-m", message)
    if rc == 0:
        git_push_async()
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
            return self._send(200, page().encode("utf-8"), "text/html; charset=utf-8")
        if u.path.startswith("/ui/"):
            r = ui_file(u.path[4:])
            if r is None:
                return self._send(404, b"not found", "text/plain")
            return self._send(200, r[0], r[1])
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
        # Weekly Pulse review workbook (added 2026-10-27): generate, hand out, read back.
        if u.path == "/api/review":
            with LOCK:
                return self._json(200, review_status())
        if u.path == "/api/review/workbook":
            date = q.get("date", [R.today()])[0]
            with LOCK:
                import time as _t; SELF_WRITE_UNTIL[0] = _t.time() + 12
                out, teams, _np = V.build(today=date)
                V.note_sent(date)
                git_commit_all(f"review: workbook {date} generated")
            data = out.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            self.send_header("Content-Disposition", f'attachment; filename="{out.name}"')
            self.send_header("Content-Length", str(len(data))); self.send_header("Cache-Control", "no-store")
            self.end_headers(); self.wfile.write(data); return
        if u.path == "/api/pulse/prompts":
            with LOCK:
                return self._json(200, copilot_prompts())
        if u.path == "/api/pulse":
            with LOCK:
                return self._json(200, P.summary())
        # Products tab (added 2026-10-21): one card per live product in Products/_products.json.
        if u.path == "/api/products":
            try:
                w = int(q.get("window", ["14"])[0])
            except ValueError:
                w = 14
            w = w if w in (7, 14, 30) else 14
            src = q.get("from", [""])[0]
            if src:
                PR.log_view(src, w)
            with LOCK:
                return self._json(200, PR.summary(w))
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
        if u.path == "/api/review/upload":
            q = parse_qs(u.query)
            name = re.sub(r"[^A-Za-z0-9_.-]", "_", (q.get("name", ["returned.xlsx"])[0] or "returned.xlsx"))
            if not name.lower().endswith(".xlsx"):
                return self._json(400, {"error": "upload the returned .xlsx"})
            n = int(self.headers.get("Content-Length", "0") or 0)
            raw = self.rfile.read(n) if n else b""
            if not raw:
                return self._json(400, {"error": "empty upload"})
            stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
            V.RETURNED.mkdir(parents=True, exist_ok=True)
            dest = V.RETURNED / f"{stamp}_{name}"
            dest.write_bytes(raw)
            try:
                with LOCK:
                    pv = V.read_back(dest)
            except Exception as e:
                return self._json(400, {"error": f"could not read the workbook: {e}"})
            if pv.get("error"):
                return self._json(400, pv)
            pv["saved_as"] = dest.name
            REVIEW_PREVIEWS[dest.name] = pv
            return self._json(200, pv)
        d = self._body()
        if u.path == "/api/review/apply":
            pv = REVIEW_PREVIEWS.get(d.get("saved_as") or "")
            if not pv:
                return self._json(400, {"error": "preview expired; upload the workbook again"})
            with LOCK:
                import time as _t; SELF_WRITE_UNTIL[0] = _t.time() + 12
                out = V.apply(pv, d.get("accept") or [])
                R.regenerate_all()
                who = ", ".join(sorted({a["reviewer"] for a in out["applied"]} | {c["reviewer"] for c in out["created"]}))
                msg = git_commit_all(f"review: {pv.get('manifest_date')} workbook read back, {len(out['applied'])} changes, {len(out['created'])} new ({who})")
            REVIEW_PREVIEWS.pop(d.get("saved_as"), None)
            out["git"] = msg
            return self._json(200, out)
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
        if u.path == "/api/products/live":
            try:
                with LOCK:
                    import time as _t; SELF_WRITE_UNTIL[0] = _t.time() + 12
                    p = PR.set_live((d.get("product") or "").strip(), bool(d.get("live")))
                    git_commit_all(f"web: product {p['name']} -> {'live' if p['live'] else 'not live'}")
                    try:
                        w = int(d.get("window") or 14)
                    except ValueError:
                        w = 14
                    return self._json(200, PR.summary(w if w in (7, 14, 30) else 14))
            except KeyError:
                return self._json(404, {"error": "unknown product"})
        if u.path == "/api/regenerate":
            with LOCK:
                counts = R.regenerate_all()
                msg = git_commit("regenerate 03/04/05 from Registers/")
            return self._json(200, {"counts": counts, "git": msg})
        return self._json(404, {"error": "no route"})


# ----------------------------------------------------------------------------- UI

UI_DIR = Path(__file__).resolve().parent / "ui"   # index.html, app.css, app.js (split out of this file 2026-10-29)
UI_TYPES = {".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8", ".js": "text/javascript; charset=utf-8"}


def ui_version() -> str:
    """Cache-buster for the stylesheet and script: the newest mtime of the three UI files."""
    try:
        return str(int(max(f.stat().st_mtime for f in UI_DIR.iterdir() if f.suffix in UI_TYPES)))
    except (ValueError, FileNotFoundError):
        return "0"


def page() -> str:
    """The app page, read from Tools/ui/ on every request so a UI edit shows on reload with no restart
    (2026-10-28 review, item 4: the UI is a static file served by the same process; nothing else changed)."""
    return (UI_DIR / "index.html").read_text(encoding="utf-8").replace("__V__", ui_version())


def ui_file(name: str) -> tuple[bytes, str] | None:
    f = UI_DIR / name
    if "/" in name or f.suffix not in UI_TYPES or not f.exists():
        return None
    return f.read_bytes(), UI_TYPES[f.suffix]



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
    # Products tab (2026-10-21): product files and the roster count too, so an open tab picks up filing.
    pd = R.ROOT / "Products"
    if pd.exists():
        for f in sorted(list(pd.rglob("*.md")) + [pd / "_products.json"]):
            try:
                h.update(f"{f}:{f.stat().st_mtime}".encode())
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


TOOLS = [Path(__file__).resolve().parent / n for n in ("eos_server.py", "eos_registers.py", "eos_pulse.py", "eos_products.py", "eos_review.py", "eos_smoke.py")]
SMOKE = Path(__file__).resolve().parent / "eos_smoke.py"


def run_smoke(timeout: int = 120) -> tuple[bool, str]:
    """Added 2026-10-29 (2026-10-28 review, item 3): the smoke test runs in a subprocess so it exercises the code on
    disk (the new code, not the modules this process already loaded) and so a crash in it cannot take the server down.
    Returns (passed, last line of its report)."""
    try:
        r = subprocess.run([sys.executable, str(SMOKE), "--quiet"], capture_output=True, text=True, timeout=timeout,
                           cwd=str(R.ROOT), env={**os.environ, "EOS_ROOT": str(R.ROOT)})
        out = (r.stdout.strip() or r.stderr.strip()).splitlines()
        return r.returncode == 0, (out[-1] if out else f"exit {r.returncode}, no output")
    except subprocess.TimeoutExpired:
        return False, f"smoke test timed out after {timeout}s"
    except Exception as e:
        return False, f"smoke test could not run: {e}"


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
    without Darryl quitting and relaunching. Waits for the files to settle, to compile, and (since 2026-10-29) to pass
    Tools/eos_smoke.py before restarting."""
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
    ok, verdict = run_smoke()
    if not ok:
        # Old code keeps running. The change is still committed so the history shows what was tried and why it did
        # not deploy; the next edit to Tools/ re-runs the gate.
        with LOCK:
            msg = git_commit_all(f"code change: SMOKE TEST FAILED, old code still running ({verdict})")
        sys.stderr.write(f"[watch] code changed but the smoke test failed; NOT restarting: {verdict} ({msg})\n")
        return
    with LOCK:
        msg = git_commit_all(f"code change: restart server with updated Tools/ ({verdict})")
    sys.stderr.write(f"[watch] code changed, {verdict} ({msg}); restarting\n")
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
    ok, verdict = run_smoke()
    print("startup:", verdict if ok else f"SMOKE FAILED: {verdict} (server starts anyway; fix before the next code change)")
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
