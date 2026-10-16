#!/usr/bin/env python3
"""
eos_pulse.py — the Operational Pulse: Darryl's rolling view of what his team-governed forums are carrying.

Added 2026-10-16. Design decision and rationale: CLAUDE.md, "Operational Pulse (lane model)".

Team-governed forums (deployment scrums, sprint stand-ups, backlog refinement and the like) run on their
own governance: a project-management process or a sprint cycle. Their issues are NOT register items.
They live here, one file per issue under Registers/pulse/P###.md, and age out on their own when the
forum stops raising them. Nothing in the Pulse needs disposal. An issue reaches Darryl's registers only
by escalation (one tap in the web app, or Claude proposing it at a brief).

Files:
  Registers/pulse/P###.md      one issue (front matter + dated sightings in the body)
  Registers/pulse/_forums.json the team-governed forums: key, name, governance type, owner
  Registers/pulse/_health.json daily account-health snapshots, for the trend
  11_Operational_Pulse.md      generated view (weekly governance agendas per forum)

Standard library only.
"""
from __future__ import annotations

import datetime as _dt
import json
import re
from pathlib import Path

import eos_registers as R

PULSE_DIR = R.REG_DIR / "pulse"
FORUMS_FILE = PULSE_DIR / "_forums.json"
ACCOUNTS_FILE = PULSE_DIR / "_accounts.json"
HEALTH_FILE = PULSE_DIR / "_health.json"
VIEW_FILE = R.ROOT / "11_Operational_Pulse.md"

WINDOW_DAYS = 14   # an issue not raised for 14 days goes quiet (drops out of the live window)
STUCK_BDAYS = 10   # an issue still being raised 10+ business days after it was first raised is stuck
KNOW_QUIET_DAYS = 45   # knowledge-concentration entries persist longer: silence does not remove a single point of failure
ABSENCE_LOOKAHEAD = 14  # an absence or departure within 14 days (or past, with coverage unconfirmed) needs a call
COVERAGE = ("none", "unknown", "partial", "covered")

# Account health. A transparent operational-friction index, not customer sentiment. Calibrate with Darryl.
HEALTH_WEIGHTS = {
    "live_high_visible": 8,   # each live High issue the customer can see
    "live_high": 6,           # each live High issue the customer cannot see
    "live_medium": 3,
    "live_low": 1,
    "stuck": 4,               # extra, per stuck issue
    "quiet": 1,               # per quiet issue: no fresh evidence, not confirmed resolved
    "candidate": 3,           # per open escalation candidate
    "at_your_level": 5,       # per open register item about the account (Watch Active, Register A, Critical)
}
BANDS = [(80, "green", "Healthy"), (60, "amber", "Strained"), (0, "red", "At risk")]
PINNED_ACCOUNTS = ["Dell"]    # Darryl, 2026-10-16: Dell is the largest customer; keep it in front of him

ESCALATION_TESTS = {
    "asked": "Darryl named or asked for a decision, resource or escalation",
    "boundary": "Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team",
    "stuck": "Still being raised 10+ business days after it was first raised",
    "gap": "No owner, or the customer is unaware of a material problem",
    "single": "One person holds knowledge a customer or a release depends on, and no backup is confirmed",
    "absence": "An absence or departure is near, or has passed, and the handover is not confirmed",
}


def is_knowledge(meta: dict) -> bool:
    return (meta.get("category") or "") == "knowledge"


# ----------------------------------------------------------------------------- dates

def _d(s):
    if isinstance(s, _dt.date):
        return s
    try:
        return _dt.date.fromisoformat(str(s)[:10])
    except Exception:
        return None


def bdays(a, b) -> int:
    """Business days from a to b (weekdays in (a, b])."""
    a, b = _d(a), _d(b)
    if not a or not b or b <= a:
        return 0
    n, d = 0, a
    while d < b:
        d += _dt.timedelta(days=1)
        if d.weekday() < 5:
            n += 1
    return n


# ----------------------------------------------------------------------------- forums

def _forums_doc() -> dict:
    try:
        return json.loads(FORUMS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def load_forums() -> list[dict]:
    return _forums_doc().get("forums", [])


def load_tracks() -> list[dict]:
    """Darryl's governance tracks (2026-10-16): the weekly meetings he runs with each team's leads.
    Each forum carries a `track` key; a track's agenda spans all of its forums."""
    return _forums_doc().get("tracks", [])


def forum_name(key: str, forums=None) -> str:
    for f in forums or load_forums():
        if f.get("key") == key:
            return f.get("name", key)
    return key or "Unassigned forum"


# ----------------------------------------------------------------------------- per-item state

# Same person, different spellings in evidence. Extend as they surface.
ALIASES = {"Syed Zaidi": "Syed Jamshed Zaidi", "Syed J Zaidi": "Syed Jamshed Zaidi", "Robby Tefft": "Robert Tefft", "Robbie Tefft": "Robert Tefft"}

_SPLIT = re.compile(r",|;|/|\band\b|\bwith\b|&")


def names(s) -> list[str]:
    """'Alan Martin (working lead), with Stephen Karpinski and John Bartolotti' -> three names."""
    if isinstance(s, list):
        raw = s
    else:
        raw = _SPLIT.split(re.sub(r"\([^)]*\)", "", str(s or "")))
    out = []
    for n in raw:
        n = re.sub(r"\s+", " ", str(n)).strip(" .-")
        if not n or len(n) < 3 or not n[0].isupper():
            continue
        if n.lower() in ("tbc", "unclear", "owner unclear", "the team", "team", "darryl benson", "darryl"):
            continue
        out.append(ALIASES.get(n, n))
    return out


def state(meta: dict, today=None) -> str:
    today = _d(today) or _dt.date.today()
    st = (meta.get("status") or "live").lower()
    if st in ("resolved", "dropped"):
        return st
    ls = _d(meta.get("last_seen")) or _d(meta.get("first_seen"))
    if ls and (today - ls).days > (KNOW_QUIET_DAYS if is_knowledge(meta) else WINDOW_DAYS):
        return "quiet"
    return "live"


def is_stuck(meta: dict, today=None) -> bool:
    if is_knowledge(meta) or state(meta, today) != "live":
        return False
    return bdays(meta.get("first_seen"), meta.get("last_seen") or meta.get("first_seen")) >= STUCK_BDAYS


def candidate_reason(meta: dict, today=None) -> str:
    esc = (meta.get("escalation") or "").lower()
    if esc in ("escalated", "declined"):
        return ""
    if state(meta, today) != "live":
        return ""
    if esc == "candidate":
        return meta.get("escalation_test") or "flagged"
    if is_knowledge(meta):
        cov = (meta.get("coverage") or "unknown").lower()
        if cov == "covered":
            return ""
        ab = _d(meta.get("absence_date"))
        today_d = _d(today) or _dt.date.today()
        if ab and (ab - today_d).days <= ABSENCE_LOOKAHEAD:
            return "absence"
        exp = [str(x).lower() for x in (meta.get("exposure") or [])]
        if cov in ("none", "unknown") and ("customer" in exp or "release" in exp):
            return "single"
        return ""
    if is_stuck(meta, today):
        return "stuck"
    if not names(meta.get("owner")):
        return "gap"
    return ""


def annotate(meta: dict, today=None) -> dict:
    """Computed fields the web app needs; never written to disk."""
    d = dict(meta)
    d["_state"] = state(meta, today)
    d["_stuck"] = is_stuck(meta, today)
    d["_candidate"] = candidate_reason(meta, today)
    owners = names(meta.get("owner"))
    d["_owners"] = owners
    d["_involved"] = sorted(set(names(meta.get("people") or [])) - set(owners))
    d["_people"] = sorted(set(owners) | set(d["_involved"]))
    return d


# ----------------------------------------------------------------------------- health

def _band(score: int) -> tuple[str, str]:
    for floor, key, label in BANDS:
        if score >= floor:
            return key, label
    return "red", "At risk"


def load_accounts() -> list[dict]:
    """The account roster (Darryl's customers, internal programs, partners), so a tile does not depend on
    whether a Pulse issue happened to arrive. Each: name, aliases, type (customer | internal | partner), pinned."""
    try:
        return json.loads(ACCOUNTS_FILE.read_text(encoding="utf-8")).get("accounts", [])
    except Exception:
        return []


def _at_your_level(m: dict) -> bool:
    k = m.get("kind")
    if k == "watch":
        return m.get("tier") == "active" and m.get("status") != "closed"
    if k == "action":
        return m.get("status") == "open" and (m.get("register") == "A" or bool(m.get("critical")))
    return False


def attribute_register_items(regs, roster: dict) -> tuple[dict, list]:
    """Each register item at Darryl's level counts against one account at most (fixed 2026-10-16: C57 was lowering
    both Dell and Federal Reserve). An explicit `account` field on the item wins. Otherwise the item belongs to the one
    roster account whose name or alias appears in its title or product. An item that names two or more accounts and
    has no `account` set is not scored; it is returned as unattributed so Darryl can set it.
    Items linked to each other (`links`, either direction) are one exposure and count once (C62 and W002, the same
    Dell FTE request, were counted twice). Every row is still returned for display; `counted` says whether it scored."""
    alias_to, pats = {}, {}
    for name, r in roster.items():
        words = [name] + list(r.get("aliases") or [])
        for w in words:
            alias_to[w.lower()] = name
        pats[name] = re.compile(r"\b(" + "|".join(re.escape(w) for w in words) + r")\b", re.I)
    by = {name: [] for name in roster}
    unattributed = []
    for m, _b, _p in regs:
        if not _at_your_level(m):
            continue
        row = {"id": m["id"], "title": m.get("title", ""), "kind": m.get("kind"),
               "links": [str(x) for x in (m.get("links") or [])]}
        explicit = str(m.get("account") or "").strip()
        if explicit:
            hits = [alias_to.get(explicit.lower(), explicit)]
        else:
            text = " ".join(str(m.get(f) or "") for f in ("title", "product"))
            hits = [n for n, pat in pats.items() if pat.search(text)]
        if len(hits) == 1:
            by.setdefault(hits[0], []).append(row)
        elif len(hits) > 1:
            unattributed.append({"id": row["id"], "title": row["title"], "kind": row["kind"], "accounts": hits})
    for a, rows in by.items():
        seen: set = set()
        for r in sorted(rows, key=lambda r: (re.sub(r"\d", "", r["id"]), int(re.sub(r"\D", "", r["id"]) or 0))):
            group = {r["id"]} | set(r["links"])
            dup = sorted(group & seen)
            r["counted"] = not dup
            if dup:
                r["same_as"] = dup[0]
            seen |= group
    return by, unattributed


def account_health(pulse, regs, today=None, know=None) -> tuple[list[dict], list]:
    today = _d(today) or _dt.date.today()
    roster = {r["name"]: r for r in load_accounts()}
    reg_by, unattributed = attribute_register_items(regs, roster)
    alias_to = {}
    for r in roster.values():
        for al in [r["name"]] + list(r.get("aliases") or []):
            alias_to[al.lower()] = r["name"]
    accts = {name: [] for name in roster}
    # Knowledge entries with an account count as an open call against it (fixed 2026-10-16: K005, a Dell call, was
    # invisible to the Dell score and the Dell filter because no account was set and knowledge was not read here).
    for m, _b, _p in list(pulse) + list(know or []):
        a = (m.get("account") or "").strip()
        if a:
            accts.setdefault(alias_to.get(a.lower(), a), []).append(m)
    for a in PINNED_ACCOUNTS:
        accts.setdefault(a, [])
    snaps = _load_snapshots()
    out = []
    for a, ms in accts.items():
        c = {k: 0 for k in HEALTH_WEIGHTS}
        for m in ms:
            st = state(m, today)
            if is_knowledge(m):
                if candidate_reason(m, today):
                    c["candidate"] += 1
                continue
            if st == "live":
                sev = (m.get("severity") or "Medium").capitalize()
                if sev == "High":
                    c["live_high_visible" if m.get("customer_visible") else "live_high"] += 1
                elif sev == "Low":
                    c["live_low"] += 1
                else:
                    c["live_medium"] += 1
                if is_stuck(m, today):
                    c["stuck"] += 1
                if candidate_reason(m, today):
                    c["candidate"] += 1
            elif st == "quiet":
                c["quiet"] += 1
        escalated = {m.get("escalated_to") for m in ms if m.get("escalated_to")}
        regitems = [r for r in reg_by.get(a, []) if r["id"] not in escalated]
        c["at_your_level"] = sum(1 for r in regitems if r.get("counted", True))
        penalty = sum(c[k] * w for k, w in HEALTH_WEIGHTS.items())
        score = max(0, 100 - penalty)
        band, label = _band(score)
        prior = _prior_score(snaps, a, today)
        out.append({
            "account": a, "score": score, "band": band, "label": label,
            "pinned": a in PINNED_ACCOUNTS or bool((roster.get(a) or {}).get("pinned")), "components": c, "penalty": penalty,
            "type": (roster.get(a) or {}).get("type", "customer"),
            "signals": bool(ms) or bool(regitems),
            "live": sum(1 for m in ms if not is_knowledge(m) and state(m, today) == "live"),
            "register_items": regitems,
            "prior": prior, "delta": (score - prior["score"]) if prior else None,
        })
    out.sort(key=lambda h: (not h["pinned"], h["score"], h["account"]))
    return out, unattributed


def _load_snapshots() -> dict:
    try:
        return json.loads(HEALTH_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _prior_score(snaps: dict, account: str, today) -> dict | None:
    cutoff = today - _dt.timedelta(days=7)
    best = None
    for ds, row in snaps.items():
        d = _d(ds)
        if d and d <= cutoff and account in row and (best is None or d > _d(best[0])):
            best = (ds, row[account])
    return {"date": best[0], "score": best[1]} if best else None


def snapshot_health(health: list[dict], today=None) -> None:
    today = _d(today) or _dt.date.today()
    snaps = _load_snapshots()
    snaps[today.isoformat()] = {h["account"]: h["score"] for h in health}
    keep = sorted(snaps)[-180:]
    snaps = {k: snaps[k] for k in keep}
    PULSE_DIR.mkdir(parents=True, exist_ok=True)
    HEALTH_FILE.write_text(json.dumps(snaps, indent=1, sort_keys=True) + "\n", encoding="utf-8")


# ----------------------------------------------------------------------------- people

def people(pulse, regs, today=None, know=None) -> list[dict]:
    """Where named people concentrate. Counted separately, because they mean different things:
    owns     = named as owner of a live Pulse issue
    involved = named in the evidence on a live Pulse issue with a statement, commitment or stated role, not the owner
    delegated = owner of an open delegated or awaited register item."""
    agg = {}

    def row(n):
        return agg.setdefault(n, {"name": n, "owns": 0, "involved": 0, "delegated": 0, "sole": 0, "forums": set(), "ids": []})

    for m, _b, _p in pulse:
        if state(m, today) != "live":
            continue
        owners = set(names(m.get("owner")))
        for n in owners:
            r = row(n); r["owns"] += 1; r["forums"].add(m.get("forum") or ""); r["ids"].append(m["id"])
        for n in set(names(m.get("people") or [])) - owners:
            r = row(n); r["involved"] += 1; r["forums"].add(m.get("forum") or ""); r["ids"].append(m["id"])
    for m, _b, _p in regs:
        if m.get("kind") == "action" and m.get("register") == "other" and m.get("status") == "open":
            for n in set(names(m.get("owner"))):
                r = row(n); r["delegated"] += 1; r["ids"].append(m["id"])
    for m, _b, _p in know or []:
        if state(m, today) == "live" and (m.get("coverage") or "unknown") != "covered":
            for n in set(names(m.get("holder"))):
                r = row(n); r["sole"] += 1; r["ids"].append(m["id"])
    out = []
    for r in agg.values():
        r["forums"] = sorted(f for f in r["forums"] if f)
        r["pulse"] = r["owns"] + r["involved"]
        r["total"] = r["owns"] + r["delegated"]  # load carried; involvement is context, not load
        out.append(r)
    out.sort(key=lambda r: (-r["total"], -r["owns"], -r["involved"], r["name"]))
    return out


# ----------------------------------------------------------------------------- summary

def summary(today=None, write_snapshot: bool = False) -> dict:
    today = _d(today) or _dt.date.today()
    forums = load_forums()
    allp = R.load_items("pulse") if PULSE_DIR.exists() else []
    pulse = [t for t in allp if not is_knowledge(t[0])]
    know = [t for t in allp if is_knowledge(t[0])]
    regs = R.load_items("action") + R.load_items("watch")
    health, unattributed = account_health(pulse, regs, today, know)
    if write_snapshot:
        snapshot_health(health, today)
    week_ago = today - _dt.timedelta(days=7)
    win_start = (today - _dt.timedelta(days=WINDOW_DAYS)).isoformat()
    frows = []
    for f in forums:
        ms = [m for m, _b, _p in pulse if m.get("forum") == f.get("key")]
        live = [m for m in ms if state(m, today) == "live"]
        frows.append({
            **f,
            "live": len(live),
            "new7": sum(1 for m in live if (_d(m.get("first_seen")) or today) >= week_ago),
            "stuck": sum(1 for m in live if is_stuck(m, today)),
            "candidates": sum(1 for m in live if candidate_reason(m, today)),
            "quiet": sum(1 for m in ms if state(m, today) == "quiet"),
            "last_seen": max((str(m.get("last_seen") or "") for m in ms), default=""),
        })
        # Added 2026-10-16: silence from a forum is only meaningful if its evidence is arriving. `last_evidence` in
        # _forums.json is the date of the newest evidence package that covered the forum (set at each brief).
        r = frows[-1]
        r["last_evidence"] = max(str(f.get("last_evidence") or ""), r["last_seen"])
        r["evidence_in_window"] = bool(r["last_evidence"]) and r["last_evidence"] >= win_start
    trows = []
    for t in load_tracks():
        fs = [f for f in frows if f.get("track") == t.get("key")]
        kn = [m for m, _b, _p in know if m.get("track") == t.get("key") and state(m, today) == "live"]
        row = {**t, "forums": [f["key"] for f in fs],
               **{k: sum(f[k] for f in fs) for k in ("live", "new7", "stuck", "candidates", "quiet")},
               "knowledge": sum(1 for m in kn if (m.get("coverage") or "unknown") != "covered"),
               "no_evidence": sum(1 for f in fs if not f["evidence_in_window"])}
        # Knowledge calls belong to the track's call count too (fixed 2026-10-16: K005 showed 0 for Delivery).
        row["candidates"] += sum(1 for m in kn if candidate_reason(m, today))
        trows.append(row)
    cands = []
    for m, _b, _p in allp:
        r = candidate_reason(m, today)
        if r:
            cands.append({"id": m["id"], "title": m.get("title", ""), "reason": r,
                          "reason_text": ESCALATION_TESTS.get(r, r), "forum": m.get("forum", ""),
                          "account": m.get("account", ""), "severity": m.get("severity", "") or ("High" if r in ("single", "absence") else ""),
                          "category": m.get("category", "") or "issue", "track": m.get("track", "")})
    sev = {"High": 0, "Medium": 1, "Low": 2}
    cands.sort(key=lambda c: (sev.get(c["severity"], 3), c["id"]))
    return {
        "today": today.isoformat(),
        "window": {"start": (today - _dt.timedelta(days=WINDOW_DAYS)).isoformat(), "end": today.isoformat(),
                   "days": WINDOW_DAYS, "stuck_bdays": STUCK_BDAYS},
        "forums": frows,
        "tracks": trows,
        "health": [h for h in health if h["signals"] or h["pinned"]],
        "quiet_accounts": [h["account"] for h in health if not (h["signals"] or h["pinned"])],
        "unattributed": unattributed,
        "weights": HEALTH_WEIGHTS,
        "bands": [{"floor": f, "band": b, "label": l} for f, b, l in BANDS],
        "candidates": cands,
        "people": people(pulse, regs, today, know),
        "coverage": {c: sum(1 for m, _b, _p in know if state(m, today) == "live" and (m.get("coverage") or "unknown") == c) for c in COVERAGE},
        "tests": ESCALATION_TESTS,
        "counts": {
            "live": sum(1 for m, _b, _p in pulse if state(m, today) == "live"),
            "quiet": sum(1 for m, _b, _p in pulse if state(m, today) == "quiet"),
            "resolved": sum(1 for m, _b, _p in pulse if state(m, today) in ("resolved", "dropped")),
            "knowledge": sum(1 for m, _b, _p in know if state(m, today) == "live"),
        },
    }


# ----------------------------------------------------------------------------- escalation

def escalate(pid: str, decision: str, note: str = "", actor: str = "Darryl, web", today=None) -> dict:
    """decision: 'escalate' creates an Active Watch item linked to the issue; 'decline' leaves it with the team."""
    today_s = (_d(today) or _dt.date.today()).isoformat()
    p = PULSE_DIR / f"{pid}.md"
    if not p.exists():
        raise KeyError(pid)
    meta, body = R.read_item(p)
    out = {"pulse": pid}
    if decision == "escalate":
        if meta.get("escalated_to"):
            out["watch"] = meta["escalated_to"]
            return out
        wid = R.next_id("W")
        fname = forum_name(meta.get("forum", "")) if not is_knowledge(meta) else "knowledge concentration"
        title = meta.get("title", "")
        if is_knowledge(meta):
            title = f"Knowledge concentration: {title} ({meta.get('holder', '')})"
        w = {
            "id": wid, "kind": "watch", "tier": "active", "status": "open",
            "title": title, "product": meta.get("product", ""),
            "severity": meta.get("severity", "") or "Medium", "trend": "New",
            "evidence_basis": f"Escalated from Pulse {pid} ({fname})",
            "next_action": meta.get("next_action", ""),
            "created": today_s, "last_touched": today_s, "needs_triage": False,
            "account": meta.get("account", ""), "source_forum": meta.get("forum", ""),
        }
        reason = meta.get("escalation_test") or candidate_reason(meta, today) or "Darryl's call"
        wbody = (f"{today_s} ({actor}): Escalated from Pulse {pid} ({fname}). "
                 f"Test: {ESCALATION_TESTS.get(reason, reason)}. The team's governance still owns the work; "
                 f"this row tracks Darryl's part.")
        if note and note.strip():
            wbody += f"\n\n{today_s} ({actor}): {note.strip()}"
        R.write_item(w, wbody)
        meta["escalation"] = "escalated"
        meta["escalated_to"] = wid
        body = (body or "").rstrip("\n") + f"\n\n{today_s} ({actor}): Escalated to {wid}." + (f" {note.strip()}" if note and note.strip() else "") + "\n"
        out["watch"] = wid
    elif decision == "decline":
        meta["escalation"] = "declined"
        body = (body or "").rstrip("\n") + f"\n\n{today_s} ({actor}): Left with the team; not escalated." + (f" {note.strip()}" if note and note.strip() else "") + "\n"
    else:
        raise ValueError("decision must be 'escalate' or 'decline'")
    meta["last_touched"] = today_s
    R.write_item(meta, body)
    return out


# ----------------------------------------------------------------------------- generated view

def generate_view(s: dict | None = None) -> str:
    s = s or summary()
    today = _d(s["today"])
    pulse = R.load_items("pulse") if PULSE_DIR.exists() else []
    L = ["# Operational Pulse", "", R._banner(), ""]
    L.append(f"> Rolling window {s['window']['start']} to {s['window']['end']}. Issues from team-governed forums. "
             "The teams' own governance (project process, sprint cycle) owns the work; nothing here needs disposal. "
             "Issues go quiet after 14 days without a sighting. Escalated issues move to the Watch List. "
             "Design: `CLAUDE.md`, Operational Pulse.")
    L.append("")
    L.append("## Account health")
    L.append("")
    L.append("| Account | Score | Band | 7-day change | Live | Stuck | Quiet | At your level |")
    L.append("|---|---|---|---|---|---|---|---|")
    for h in s["health"]:
        c = h["components"]
        d = "" if h["delta"] is None else f"{h['delta']:+d}"
        L.append(f"| {h['account']} | {h['score']} | {h['label']} | {d or 'no prior week'} | {h['live']} | {c['stuck']} | {c['quiet']} | {c['at_your_level']} |")
    L.append("")
    L.append("Score = 100 minus: " + ", ".join(f"{k.replace('_', ' ')} x{v}" for k, v in s["weights"].items()) + ". "
             "Bands: 80+ healthy, 60 to 79 strained, below 60 at risk. Friction index from evidence, not customer sentiment.")
    if s.get("quiet_accounts"):
        L.append("")
        L.append("No signals in the window: " + ", ".join(s["quiet_accounts"]) + ".")
    if s.get("unattributed"):
        L.append("")
        L.append("Not scored, names more than one account (set the item's account): " +
                 "; ".join(f"{u['id']} ({', '.join(u['accounts'])})" for u in s["unattributed"]) + ".")
    L.append("")
    L.append("## Needs your call")
    L.append("")
    if s["candidates"]:
        for c in s["candidates"]:
            where = "knowledge concentration" if c.get("category") == "knowledge" else f"{c['account'] or 'no account'}; {forum_name(c['forum'])}"
            L.append(f"- **{c['id']}** {c['title']} ({where}). Test: {c['reason_text']}.")
    else:
        L.append("- None this cycle.")
    L.append("")
    know = [m for m, _b, _p in pulse if is_knowledge(m)]
    L.append("## Knowledge concentration")
    L.append("")
    L.append("Where one person holds knowledge a customer, a release or a migration depends on. Silence does not remove the risk: entries stay live for 45 days after the last evidence.")
    L.append("")
    covr = {c: i for i, c in enumerate(COVERAGE)}
    live_k = sorted([m for m in know if state(m, today) == "live"], key=lambda m: (covr.get(m.get("coverage") or "unknown", 1), str(m.get("title"))))
    if live_k:
        L.append("| ID | Knowledge area | Held by | Backup | Coverage | Exposure | Mitigation | Last evidence |")
        L.append("|---|---|---|---|---|---|---|---|")
        for m in live_k:
            L.append(f"| {m['id']} | {R.md_cell(m.get('title'))} | {R.md_cell(m.get('holder'))} | {R.md_cell(m.get('backup') or 'none named')} | {m.get('coverage') or 'unknown'} | "
                     f"{', '.join(m.get('exposure') or [])} | {R.md_cell(m.get('mitigation'))} | {m.get('last_seen', '')} |")
    else:
        L.append("None live.")
    qk = [m for m in know if state(m, today) == "quiet"]
    if qk:
        L.append("")
        L.append("Not seen in 45+ days (confirm whether still true): " + "; ".join(f"{m['id']} {m.get('title', '')} ({m.get('holder', '')})" for m in qk) + ".")
    L.append("")
    L.append("## People carrying the most")
    L.append("")
    L.append("| Person | Owns (Pulse) | Involved (Pulse) | Delegated/awaited | Sole holder | Forums |")
    L.append("|---|---|---|---|---|---|")
    for r in s["people"][:12]:
        L.append(f"| {r['name']} | {r['owns']} | {r['involved']} | {r['delegated']} | {r.get('sole', 0)} | {', '.join(forum_name(f) for f in r['forums'])} |")
    L.append("")
    L.append("Owns: named owner of a live Pulse issue. Involved: named in the evidence with a statement, commitment or stated role, not the owner. Delegated/awaited: open register items they own. Sole holder: knowledge areas they hold without a confirmed backup.")
    L.append("")
    sev = {"High": 0, "Medium": 1, "Low": 2}
    for f in s["forums"]:
        ms = [(m, b) for m, b, _p in pulse if m.get("forum") == f["key"]]
        if not ms and not f.get("show_empty", True):
            continue
        L.append(f"## {f['name']}")
        L.append("")
        L.append(f"Governance: {f.get('governance', '')}. Owner: {f.get('owner', '')}. "
                 f"Live {f['live']}, new this week {f['new7']}, stuck {f['stuck']}, quiet {f['quiet']}. "
                 f"Last sighting: {f['last_seen'] or 'none in the Pulse yet'}. "
                 f"Last evidence: {f.get('last_evidence') or 'none received'}{'' if f.get('evidence_in_window') else ' (none in the window)'}.")
        L.append("")
        live = sorted([m for m, _b in ms if state(m, today) == "live"],
                      key=lambda m: (not is_stuck(m, today), sev.get(m.get("severity"), 3), str(m.get("last_seen"))))
        quiet = [m for m, _b in ms if state(m, today) == "quiet"]
        if live:
            L.append("| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |")
            L.append("|---|---|---|---|---|---|---|---|---|")
            for m in live:
                flags = [x for x in ("stuck" if is_stuck(m, today) else "",
                                     "customer-visible" if m.get("customer_visible") else "",
                                     f"escalated to {m.get('escalated_to')}" if m.get("escalated_to") else "",
                                     ("candidate: " + candidate_reason(m, today)) if candidate_reason(m, today) else "") if x]
                L.append(f"| {m['id']} | {R.md_cell(m.get('title'))} | {R.md_cell(m.get('account'))} | {R.md_cell(m.get('owner'))} | "
                         f"{m.get('severity', '')} | {m.get('first_seen', '')} | {m.get('last_seen', '')} | {m.get('sightings', 1)} | {', '.join(flags)} |")
            L.append("")
        if quiet:
            L.append("Quiet (no sighting in 14+ days; confirm with the team whether resolved): " +
                     "; ".join(f"{m['id']} {m.get('title', '')}" for m in quiet) + ".")
            L.append("")
        if not live and not quiet:
            L.append("No issues in the Pulse yet.")
            L.append("")
    return "\n".join(L).rstrip() + "\n"


def write_view(write_snapshot: bool = True) -> dict:
    s = summary(write_snapshot=write_snapshot)
    VIEW_FILE.write_text(generate_view(s), encoding="utf-8")
    return s["counts"]


if __name__ == "__main__":
    print(write_view())
