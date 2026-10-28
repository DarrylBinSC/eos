#!/usr/bin/env python3
"""
eos_products.py — the Products tab (added 2026-10-21).

One card per live product in Products/_products.json (a product may list several files, e.g. a supplier file under the product it supports): what changed in the product file in the
last N days (dated `## ` sections), the register item IDs those entries cite, and the open register
items that touch the product. Products with live: false are hidden and named in the tab footer.
Darryl flips `live` in the tab. Standard library only; read by eos_server.py.

Matching an open register item to a product: the item's `product` field when set; otherwise an
alias from the roster found in the item title (word-bounded, case-insensitive). The `product`
field was blank on most items at 2026-10-21; set it at intake from now on.
"""
from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path

import eos_registers as R

ROSTER = R.ROOT / "Products" / "_products.json"
VIEW_LOG = R.ROOT / "Dashboard" / "product_views.jsonl"
ID_RE = re.compile(r"\b([ABCDTWPK]\d{1,3})\b")
DATE_RE = re.compile(r"20\d\d-\d\d-\d\d")
HEAD_NOTE_RE = re.compile(r"\s*\((added|updated|revised)[^)]*\)", re.I)


def load_roster() -> dict:
    if not ROSTER.exists():
        return {"products": []}
    return json.loads(ROSTER.read_text(encoding="utf-8"))


def save_roster(d: dict) -> None:
    ROSTER.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def set_live(name: str, live: bool) -> dict:
    d = load_roster()
    for p in d["products"]:
        if p["name"] == name:
            p["live"] = bool(live)
            save_roster(d)
            return p
    raise KeyError(name)


def _clean(s: str) -> str:
    s = re.sub(r"\*\*|`", "", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return s.strip()


def _lead_lines(body: str, n: int = 2, limit: int = 240) -> list[str]:
    out = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.lower().startswith("source") or line.startswith("|") or line.startswith("---"):
            continue
        line = _clean(line.lstrip("-*• ").strip())
        if not line:
            continue
        out.append(line if len(line) <= limit else line[:limit].rsplit(" ", 1)[0] + " …")
        if len(out) >= n:
            break
    return out


def _section_date(head: str, today: str) -> str:
    """The date a section was filed. Fixed 2026-10-28: the heading's max date was used, so a 10-26 entry whose
    title mentioned a future date ("Woolly is free only until 2027-05-01") dated the whole card at 2027-05-01 and
    the entroCIM card read "updated -185d ago". Prefer the date inside the "(added|updated|revised ...)" note;
    otherwise the latest heading date that is not in the future."""
    note = HEAD_NOTE_RE.search(head)
    cands = DATE_RE.findall(note.group(0)) if note else []
    if not cands:
        cands = [d for d in DATE_RE.findall(head) if d <= today]
    return max(cands) if cands else ""


def _sections(path: Path, today: str | None = None) -> list[dict]:
    """Dated `## ` sections of a product file, newest first."""
    if not path.exists():
        return []
    today = today or R.today()
    txt = path.read_text(encoding="utf-8")
    out = []
    for chunk in re.split(r"(?m)^## ", txt)[1:]:
        head, _, body = chunk.partition("\n")
        date = _section_date(head, today)
        if not date:
            continue
        out.append({
            "date": date,
            "heading": HEAD_NOTE_RE.sub("", _clean(head)).strip(),
            "lead": _lead_lines(body),
            "ids": sorted(set(ID_RE.findall(body)), key=lambda i: (i[0], int(i[1:])))[:12],
        })
    out.sort(key=lambda s: s["date"], reverse=True)
    return out


def _alias_res(aliases: list[str]) -> list[re.Pattern]:
    return [re.compile(r"(?<![A-Za-z0-9])" + re.escape(a) + r"(?![A-Za-z0-9])", re.I) for a in aliases if a]


def _is_open(m: dict) -> bool:
    k = m.get("kind")
    if k == "decision":
        return m.get("tier") == "radar"
    if k == "watch":
        return m.get("status") == "open" and m.get("tier") == "active"
    if k == "action":
        return m.get("status") == "open"
    return False


def _item(m: dict) -> dict:
    return {k: m.get(k, "") for k in ("id", "kind", "title", "status", "tier", "register", "due", "severity",
                                       "owner", "forum_date", "last_touched", "critical", "product")}


def summary(window: int = 14, today: str | None = None) -> dict:
    today_d = dt.date.fromisoformat(today or R.today())
    roster = load_roster()
    items = [m for m, _b, _p in R.load_items() if _is_open(m)]
    cards, hidden = [], []
    for p in roster.get("products", []):
        if not p.get("live"):
            hidden.append(p["name"])
            continue
        files = p.get("files") or [p["file"]]
        secs = []
        for f in files:
            for sec in _sections(R.ROOT / f, str(today_d)):
                sec["file"] = f
                secs.append(sec)
        secs.sort(key=lambda s: s["date"], reverse=True)
        recent = [s for s in secs if (today_d - dt.date.fromisoformat(s["date"])).days <= window]
        pats = _alias_res(p.get("aliases", []))
        linked = []
        for m in items:
            prod = (m.get("product") or "").strip().lower()
            if prod == p["name"].lower() or (not prod and any(r.search(m.get("title", "")) for r in pats)):
                linked.append(_item(m))
        linked.sort(key=lambda i: ({"action": 0, "watch": 1, "decision": 2}.get(i["kind"], 3), i.get("register") != "A", i["id"]))
        last = secs[0]["date"] if secs else ""
        age = (today_d - dt.date.fromisoformat(last)).days if last else None
        cards.append({
            "name": p["name"], "file": ", ".join(files), "live": True,
            "last_entry": last, "age_days": age,
            "recent": recent, "entries_total": len(secs),
            "items": linked,
            "counts": {
                "mine": sum(1 for i in linked if i["kind"] == "action" and i["register"] == "A"),
                "other": sum(1 for i in linked if i["kind"] == "action" and i["register"] != "A"),
                "watch": sum(1 for i in linked if i["kind"] == "watch"),
                "radar": sum(1 for i in linked if i["kind"] == "decision"),
            },
        })
    cards.sort(key=lambda c: c["last_entry"], reverse=True)
    return {"today": str(today_d), "window": window, "products": cards, "hidden": hidden,
            "roster": [{"name": p["name"], "live": bool(p.get("live"))} for p in roster.get("products", [])]}


def log_view(source: str, window: int) -> None:
    """One line per open of the tab (same idea as Dashboard/brief_views.jsonl); the falsification test reads it."""
    try:
        VIEW_LOG.parent.mkdir(parents=True, exist_ok=True)
        with VIEW_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"ts": dt.datetime.now().isoformat(timespec="seconds"), "source": source, "window": window}) + "\n")
    except Exception:
        pass


if __name__ == "__main__":
    s = summary()
    for c in s["products"]:
        print(f'{c["name"]:16} last {c["last_entry"]:10} recent {len(c["recent"]):2}  items {len(c["items"]):3}  {c["counts"]}')
    print("hidden:", s["hidden"])
