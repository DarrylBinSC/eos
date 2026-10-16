#!/usr/bin/env python3
"""
eos_registers.py — shared library for the EOS register items.

One item per file under Registers/<kind>/<ID>.md:
  - YAML-style front matter (flat key: value; lists as [a, b]; no nesting)
  - Markdown body (notes, long next-step text, dated updates)

Three kinds:
  action    Register A (Mine) and Other-Owned (Delegated / Awaited)   -> 05_Commitments.md
  watch     Executive Watch List (active / passive / retired)          -> 04_Executive_Watch_List.md
  decision  Decision Radar and Decision Backlog                        -> 03_Decision_Log.md (those two sections only)

Standard library only. No PyYAML on purpose: the front matter is deliberately flat so
this file can parse and write it without a dependency, on any Mac with python3.
"""
from __future__ import annotations

import datetime as _dt
import os
import re
from pathlib import Path

ROOT = Path(os.environ.get("EOS_ROOT", Path(__file__).resolve().parent.parent))
REG_DIR = ROOT / "Registers"
KINDS = ("action", "watch", "decision", "pulse")  # pulse added 2026-10-16 (Operational Pulse, see eos_pulse.py)

# Field order inside the front matter. Unknown fields are written after these, alphabetically.
FIELD_ORDER = [
    "id", "kind", "register", "tier", "status", "title", "owner", "counterparty", "type",
    "product", "critical", "critical_reason", "severity", "trend", "evidence_basis",
    "due", "due_note", "trigger", "forum", "forum_date", "next_action", "basis", "source",
    "created", "last_touched", "closed_date", "closed_by", "disposition_note",
    "needs_triage", "tags", "legacy_section",
]

ISO_DATE = re.compile(r"\b(20\d\d-\d\d-\d\d)\b")


# ----------------------------------------------------------------------------- front matter

def _dump_scalar(v) -> str:
    if v is None:
        return '""'
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, list):
        return "[" + ", ".join(_dump_scalar(x) for x in v) + "]"
    s = str(v)
    # Always quote strings: the register text is full of colons, hashes, asterisks and pipes.
    s = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return f'"{s}"'


def _parse_scalar(raw: str):
    raw = raw.strip()
    if raw == "" or raw == '""':
        return ""
    if raw in ("true", "false"):
        return raw == "true"
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        out, cur, inq, esc = [], "", False, False
        for ch in inner:
            if esc:
                cur += ch; esc = False; continue
            if ch == "\\" and inq:
                esc = True; continue
            if ch == '"':
                inq = not inq; continue
            if ch == "," and not inq:
                out.append(cur.strip()); cur = ""; continue
            cur += ch
        out.append(cur.strip())
        return [o for o in out if o != ""]
    if raw.startswith('"') and raw.endswith('"') and len(raw) >= 2:
        s = raw[1:-1]
        return s.replace('\\"', '"').replace("\\\\", "\\")
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    return raw


def dump_item(meta: dict, body: str) -> str:
    keys = [k for k in FIELD_ORDER if k in meta] + sorted(k for k in meta if k not in FIELD_ORDER)
    lines = ["---"]
    for k in keys:
        lines.append(f"{k}: {_dump_scalar(meta[k])}")
    lines.append("---")
    body = (body or "").rstrip("\n")
    return "\n".join(lines) + "\n" + (body + "\n" if body else "")


def parse_item(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated front matter")
    head = text[4:end]
    body = text[end + 5:]
    meta = {}
    for line in head.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        k, _, v = line.partition(":")
        meta[k.strip()] = _parse_scalar(v)
    return meta, body


# ----------------------------------------------------------------------------- items on disk

def item_path(meta: dict) -> Path:
    return REG_DIR / meta["kind"] / f"{meta['id']}.md"


def write_item(meta: dict, body: str) -> Path:
    p = item_path(meta)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(dump_item(meta, body), encoding="utf-8")
    return p


def read_item(p: Path) -> tuple[dict, str]:
    meta, body = parse_item(p.read_text(encoding="utf-8"))
    meta.setdefault("kind", p.parent.name)
    meta.setdefault("id", p.stem)
    return meta, body


def load_items(kind: str | None = None) -> list[tuple[dict, str, Path]]:
    out = []
    for k in (KINDS if kind is None else (kind,)):
        d = REG_DIR / k
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            if p.name.startswith("_"):
                continue
            meta, body = read_item(p)
            out.append((meta, body, p))
    return out


def find_item(item_id: str) -> tuple[dict, str, Path] | None:
    for k in KINDS:
        p = REG_DIR / k / f"{item_id}.md"
        if p.exists():
            meta, body = read_item(p)
            return meta, body, p
    return None


def next_id(prefix: str) -> str:
    """Next free ID for a prefix (A, B, C, W, D, P). Scans all kinds so IDs never collide."""
    best = 0
    for k in KINDS:
        d = REG_DIR / k
        if not d.exists():
            continue
        for p in d.glob(f"{prefix}[0-9]*.md"):
            m = re.fullmatch(rf"{prefix}(\d+)", p.stem)
            if m:
                best = max(best, int(m.group(1)))
    width = 3 if prefix in ("W", "D", "P") else 0
    n = best + 1
    return f"{prefix}{n:0{width}d}" if width else f"{prefix}{n}"


def today() -> str:
    return _dt.date.today().isoformat()


# ----------------------------------------------------------------------------- helpers for text

def first_sentence(text: str, limit: int = 160) -> str:
    t = re.sub(r"\s+", " ", (text or "")).strip()
    t = t.replace("**", "")
    m = re.match(r"(.+?[.;])(\s|$)", t)
    s = m.group(1) if m else t
    if len(s) > limit:
        s = s[: limit - 1].rstrip() + "…"
    return s


def latest_date(*texts: str) -> str:
    ds = []
    for t in texts:
        ds += ISO_DATE.findall(t or "")
    return max(ds) if ds else ""


def md_cell(s: str) -> str:
    """Make a string safe inside a markdown table cell."""
    return (s or "").replace("\n", " ").replace("|", "\\|").strip()


# ----------------------------------------------------------------------------- sorting

def _due_key(meta):
    d = meta.get("due") or ""
    return (0, d) if d else (1, "")


def sort_actions(items):
    return sorted(items, key=lambda t: (_due_key(t[0]), t[0]["id"]))


def _id_num(i: str) -> int:
    m = re.search(r"(\d+)", i or "")
    return int(m.group(1)) if m else 0


# ----------------------------------------------------------------------------- generators

GEN_BANNER = (
    "<!-- GENERATED {stamp} from Registers/ by Tools/eos_registers.py. "
    "Do not hand-edit this section; edit the item files under Registers/ or use the EOS web app. "
    "Pre-migration history is preserved verbatim in Archive/2026-10-15_pre_registers/. -->"
)


def _banner():
    return GEN_BANNER.format(stamp=_dt.datetime.now().strftime("%Y-%m-%d %H:%M"))


def _link(meta):
    return f"`Registers/{meta['kind']}/{meta['id']}.md`"


def generate_05(items_action) -> str:
    mine = [t for t in items_action if t[0].get("register") == "A" and t[0].get("status") == "open"]
    other = [t for t in items_action if t[0].get("register") == "other" and t[0].get("status") == "open"]
    closed = [t for t in items_action if t[0].get("status") == "closed"]
    aged = [t for t in items_action if t[0].get("status") == "aged_out"]
    dropped = [t for t in items_action if t[0].get("status") == "dropped"]
    triage = [t for t in items_action if t[0].get("needs_triage")]

    dated = [t for t in mine if not t[0].get("trigger")]
    trig = [t for t in mine if t[0].get("trigger")]

    L = []
    L.append("# Action Registers")
    L.append("")
    L.append(_banner())
    L.append("")
    L.append("> **Restructured 2026-07-27** per `EOS_Redefinition_Proposal_2026-07-27.md`; **moved to one item per file 2026-10-15** per `Deliverables/EOS_Meta/2026-10-15_EOS_Registers_Build_Spec.md`. This file is a generated view of `Registers/action/`. The per-session notes that used to accumulate between the tables now live in each item's file and in the git history; the last hand-maintained version is `Archive/2026-10-15_pre_registers/05_Commitments.md`.")
    L.append("")
    L.append("## How This File Works")
    L.append("")
    L.append("Four registers. The delineation is the point.")
    L.append("")
    L.append("| Register | Contains | Test | Briefing |")
    L.append("|---|---|---|---|")
    L.append("| **A. My Actions** | Darryl personally takes the next step | If Darryl does nothing, this does not move | Daily, rule-selected, max 7 |")
    L.append("| **Other-Owned (Delegated)** | Darryl's org owns it; named executor; Darryl engages at a gate | Answerable for the outcome, not for the next step | Weekly, condensed |")
    L.append("| **Other-Owned (Awaited)** | Owed to Darryl | Darryl's action is chasing, not doing | Weekly, condensed |")
    L.append("| **D. Standing Responsibilities** | Recurring role duties, no completion state | Cannot be closed | Not tracked here. See `07_Operating_Cadence.md` |")
    L.append("")
    L.append("**Attribution test, dating rule, focus rule, closure discipline, 14-day forced disposition, Critical tag test and the Other-Owned aging rule** are in `CLAUDE.md` (Commitment Attribution and Focus Rules; Register Caps). They are unchanged by the move to item files.")
    L.append("")
    L.append(f"**Counts at generation:** Register A {len(mine)} (ceiling 15, by disposal only) · Other-Owned {len(other)} (Critical {sum(1 for t in other if t[0].get('critical'))}) · Needs triage {len(triage)}.")
    L.append("")
    if triage:
        L.append("## Needs Triage (added from the web app, not yet classified)")
        L.append("")
        L.append("| # | Title | Added | Note |")
        L.append("|---|---|---|---|")
        for m, b, p in sorted(triage, key=lambda t: t[0].get("created", "")):
            L.append(f"| {m['id']} | {md_cell(m.get('title'))} | {m.get('created','')} | {md_cell(first_sentence(b, 200))} |")
        L.append("")
    L.append("---")
    L.append("")
    L.append("## Register A — My Actions")
    L.append("")
    L.append("### Dated")
    L.append("")
    L.append("*Sorted by due date; **the A-numbers are stable identifiers, not sequence positions**. `03` and `04` cross-reference these IDs.*")
    L.append("")
    L.append("| # | Action | Next Step | Counterparty | Due | Basis | Source |")
    L.append("|---|---|---|---|---|---|---|")
    for m, b, p in sort_actions(dated):
        due = m.get("due") or ""
        if m.get("due_note"):
            due = f"{due} {m['due_note']}".strip()
        L.append(f"| {m['id']} | **{md_cell(m.get('title'))}** | {md_cell(m.get('next_action'))} | {md_cell(m.get('counterparty'))} | {md_cell(due)} | {md_cell(m.get('basis'))} | {md_cell(m.get('source'))} |")
    L.append("")
    L.append("### Triggered")
    L.append("")
    L.append("*A trigger whose own event has no date is an undated item in disguise; see the trigger backstop in `CLAUDE.md`.*")
    L.append("")
    L.append("| # | Action | Next Step | Counterparty | Trigger | Basis | Source |")
    L.append("|---|---|---|---|---|---|---|")
    for m, b, p in sorted(trig, key=lambda t: _id_num(t[0]["id"])):
        L.append(f"| {m['id']} | **{md_cell(m.get('title'))}** | {md_cell(m.get('next_action'))} | {md_cell(m.get('counterparty'))} | {md_cell(m.get('trigger'))} | {md_cell(m.get('basis'))} | {md_cell(m.get('source'))} |")
    L.append("")
    L.append("## Other-Owned — Delegated and Awaited")
    L.append("")
    L.append("**Merged 2026-08-06** (was Register B + Register C), per `EOS_Value_and_Purpose_Review_2026-08-06.md` §10. Type records which it was. Non-Critical items age out after 14 days with no referencing evidence; Critical items need Darryl's explicit close. Surfaced weekly in condensed form, sorted by gate with anything nearing its aging window first.")
    L.append("")
    L.append("| # | Item | Owner | Type | Gate / Due | Critical? | Last evidence | Note |")
    L.append("|---|---|---|---|---|---|---|---|")
    for m, b, p in sort_actions(other):
        due = m.get("due") or ""
        if m.get("due_note"):
            due = f"{due} {m['due_note']}".strip()
        crit = "**Critical**" if m.get("critical") else "--"
        if m.get("critical") and m.get("critical_reason"):
            crit += f" -- {md_cell(m['critical_reason'])}"
        L.append(f"| {m['id']} | {md_cell(m.get('title'))} | {md_cell(m.get('owner'))} | {md_cell(m.get('type'))} | {md_cell(due)} | {crit} | {m.get('last_touched','')} | {md_cell(first_sentence(b, 220))} |")
    L.append("")
    L.append("## Register D — Standing Responsibilities")
    L.append("")
    L.append("Removed from the commitment system. No completion state, so counting them permanently inflated the register. Filed in `07_Operating_Cadence.md`.")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Archive — Closed")
    L.append("")
    L.append("*Pre-07-27 closures are in `Archive/05_Commitments_pre-restructure_2026-07-27.md`. Closures stay on the disposed-item check for 30 days.*")
    L.append("")
    L.append("| Date closed | Item | Confirmed by | Note |")
    L.append("|---|---|---|---|")
    for m, b, p in sorted(closed, key=lambda t: (t[0].get("closed_date", ""), t[0]["id"]), reverse=True):
        L.append(f"| {m.get('closed_date','')} | **{m['id']} — {md_cell(m.get('title'))}** | {md_cell(m.get('closed_by'))} | {md_cell(m.get('disposition_note') or first_sentence(b, 220))} |")
    L.append("")
    L.append("## Archive — Aged Out (Presumed)")
    L.append("")
    L.append("*Non-Critical Other-Owned items with no referencing evidence for 14 days. Presumed resolved by silence, not confirmed. Reopen on contradicting evidence.*")
    L.append("")
    L.append("| Date aged out | Item | Was | Gate/date it passed | Reopened? |")
    L.append("|---|---|---|---|---|")
    for m, b, p in sorted(aged, key=lambda t: (t[0].get("closed_date", ""), t[0]["id"]), reverse=True):
        L.append(f"| {m.get('closed_date','')} | {md_cell(m.get('title'))} | {m['id']} | {md_cell(m.get('due') or m.get('due_note'))} | {md_cell(m.get('disposition_note') or first_sentence(b, 220))} |")
    L.append("")
    L.append("## Archive — Dropped")
    L.append("")
    L.append("*De-scoped by Darryl. Not completed. Permanent do-not-re-add; a recurrence after 30 days surfaces as a new item with a note that it was previously dropped.*")
    L.append("")
    L.append("| Item | Was | Dropped | Reason |")
    L.append("|---|---|---|---|")
    for m, b, p in sorted(dropped, key=lambda t: (t[0].get("closed_date", ""), t[0]["id"]), reverse=True):
        L.append(f"| **{md_cell(m.get('title'))}** | {m['id']} | {m.get('closed_date','')} | {md_cell(m.get('disposition_note') or first_sentence(b, 240))} |")
    L.append("")
    return "\n".join(L)


def generate_04(items_watch) -> str:
    act = [t for t in items_watch if t[0].get("tier") == "active"]
    pas = [t for t in items_watch if t[0].get("tier") == "passive"]
    ret = [t for t in items_watch if t[0].get("tier") == "retired"]
    sev_rank = {"High": 0, "Medium": 1, "Low": 2}

    L = []
    L.append("# Executive Watch List")
    L.append("")
    L.append(_banner())
    L.append("")
    L.append("> Maintained by Claude during briefings. Trend: ↑ worsening / → stable / ↓ improving. Seeded 2026-07-13; restructured 2026-07-27; capped 2026-08-19 (Active 20); **moved to one item per file 2026-10-15**. This file is a generated view of `Registers/watch/`; the cap-check notes that used to accumulate here now live in git history and `Archive/2026-10-15_pre_registers/04_Executive_Watch_List.md`.")
    L.append(">")
    L.append("> **Evidence basis:** **Direct** (concrete event/impact evidenced), **Single-source** (direct but one source, unverified recency), **Repetition** (recurring unresolved mention), **Inferred** (pattern Claude drew). Mention-frequency is never treated as severity.")
    L.append(">")
    L.append("> **Tiers.** *Active* requires attention or a decision. *Passive* is logged for completeness and needs no action; it does not count toward risk load. *Retired* is closed with a reason. The Active ceiling is 20; overflow goes to Passive tagged with former severity and trend, reversible in one line.")
    L.append("")
    L.append(f"**Counts at generation:** Active {len(act)} (ceiling 20) · Passive {len(pas)} · Retired {len(ret)}.")
    L.append("")
    L.append("## Active")
    L.append("")
    L.append("| ID | Watch Item | Severity | Trend | Evidence Basis | Last Update | Notes |")
    L.append("|---|---|---|---|---|---|---|")
    for m, b, p in sorted(act, key=lambda t: (sev_rank.get(t[0].get("severity"), 9), t[0].get("last_touched", ""), t[0]["id"])):
        L.append(f"| {m['id']} | {md_cell(m.get('title'))} | {md_cell(m.get('severity'))} | {md_cell(m.get('trend'))} | {md_cell(m.get('evidence_basis'))} | {m.get('last_touched','')} | {md_cell(first_sentence(b, 260))} |")
    L.append("")
    L.append("## Passive Watch")
    L.append("")
    L.append("Logged for completeness. No action required; does not count toward risk load. Escalate to Active only on a direct signal.")
    L.append("")
    L.append("| ID | Watch Item | Former severity | Evidence Basis | Last Update | Notes |")
    L.append("|---|---|---|---|---|---|")
    for m, b, p in sorted(pas, key=lambda t: (t[0].get("last_touched", ""), t[0]["id"]), reverse=True):
        L.append(f"| {m['id']} | {md_cell(m.get('title'))} | {md_cell(m.get('severity'))} | {md_cell(m.get('evidence_basis'))} | {m.get('last_touched','')} | {md_cell(first_sentence(b, 260))} |")
    L.append("")
    L.append("## Retired")
    L.append("")
    L.append("| Retired | ID | Item | Reason |")
    L.append("|---|---|---|---|")
    for m, b, p in sorted(ret, key=lambda t: (t[0].get("closed_date", ""), t[0]["id"]), reverse=True):
        L.append(f"| {m.get('closed_date','')} | {m['id']} | {md_cell(m.get('title'))} | {md_cell(m.get('disposition_note') or first_sentence(b, 260))} |")
    L.append("")
    return "\n".join(L)


def _decision_entry(m, b) -> list[str]:
    head = f"### {m.get('created') + ' — ' if m.get('created') else ''}{m.get('title','')}"
    L = [head]
    L.append(f"- ID: {m['id']}")
    if m.get("status"):
        L.append(f"- Status: {m['status']}")
    if m.get("owner"):
        L.append(f"- Owner: {m['owner']}")
    if m.get("forum") or m.get("forum_date"):
        f = m.get("forum", "")
        if m.get("forum_date"):
            f = f"{f} ({m['forum_date']})".strip()
        L.append(f"- Forum: {f}")
    if m.get("next_action"):
        L.append(f"- Next action: {m['next_action']}")
    body = (b or "").strip("\n")
    if body:
        L.append(body)
    L.append("")
    return L


def generate_03(items_decision, existing_text: str) -> str:
    """Replace only the Decision Radar and Decision Backlog sections of the existing 03 file."""
    radar = [t for t in items_decision if t[0].get("tier") == "radar" and t[0].get("status") != "closed"]
    backlog = [t for t in items_decision if t[0].get("tier") == "backlog" and t[0].get("status") != "closed"]
    resolved = [t for t in items_decision if t[0].get("status") == "closed"]

    def key(t):
        return (t[0].get("created", ""), t[0]["id"])

    R = ["## Decision Radar", "", _banner(), "",
         f"*Generated view of `Registers/decision/` (tier radar). Radar requires a named forum with a live date; ceiling 20, overflow to Backlog with the reason. Count at generation: {len(radar)}.*", ""]
    for m, b, p in sorted(radar, key=key, reverse=True):
        R += _decision_entry(m, b)
    B = ["## Decision Backlog", "",
         f"*Generated view of `Registers/decision/` (tier backlog): raised, not yet routed to a forum. Count at generation: {len(backlog)}.*", ""]
    for m, b, p in sorted(backlog, key=key, reverse=True):
        B += _decision_entry(m, b)
    if resolved:
        B += ["### Resolved while on the Radar or Backlog (retained for the disposed-item check)", ""]
        for m, b, p in sorted(resolved, key=lambda t: (t[0].get("closed_date", ""), t[0]["id"]), reverse=True):
            B.append(f"- {m['id']} — {m.get('title','')} — resolved {m.get('closed_date','')}: {first_sentence(m.get('disposition_note') or b, 200)}")
        B.append("")

    lines = existing_text.split("\n")
    def find(h):
        for i, l in enumerate(lines):
            if l.strip() == h:
                return i
        raise ValueError(f"heading not found in 03: {h}")
    i_r = find("## Decision Radar")
    i_b = find("## Decision Backlog")
    i_a = find("## Decisions Being Avoided or Stalled")
    assert i_r < i_b < i_a
    out = lines[:i_r] + R + B + lines[i_a:]
    return "\n".join(out)


def regenerate_all(write: bool = True) -> dict:
    acts = load_items("action")
    watches = load_items("watch")
    decs = load_items("decision")
    t05 = generate_05(acts)
    t04 = generate_04(watches)
    p03 = ROOT / "03_Decision_Log.md"
    t03 = generate_03(decs, p03.read_text(encoding="utf-8"))
    counts = {"action": len(acts), "watch": len(watches), "decision": len(decs)}
    if write:
        (ROOT / "05_Commitments.md").write_text(t05, encoding="utf-8")
        (ROOT / "04_Executive_Watch_List.md").write_text(t04, encoding="utf-8")
        p03.write_text(t03, encoding="utf-8")
        # Operational Pulse view and the daily account-health snapshot (added 2026-10-16).
        try:
            import eos_pulse
            counts["pulse"] = eos_pulse.write_view()
        except Exception as e:  # the Pulse must never block the register views
            counts["pulse_error"] = str(e)
    return counts


if __name__ == "__main__":
    print(regenerate_all())
