#!/usr/bin/env python3
"""
migrate_2026-10-15.py — one-time migration of 03/04/05 register content into Registers/<kind>/<ID>.md.

Reads the hand-maintained files (from the Archive snapshot, never the live files), writes one item
file per row or entry, and prints a reconciliation: rows found per section vs. items written, plus
every ID assigned where none existed before (watch items, decisions) and every row it could not
parse cleanly. Nothing in the source files is modified by this script.

Run:  python3 Tools/migrate_2026-10-15.py  [--src Archive/2026-10-15_pre_registers] [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import eos_registers as R  # noqa: E402

MIGRATION_DATE = "2026-10-15"


def _latest_not_future(*texts):
    ds = [d for t in texts for d in R.ISO_DATE.findall(t or "") if d <= MIGRATION_DATE]
    return max(ds) if ds else ""


R.latest_date = _latest_not_future  # migration must not take a future due date as "last touched"
report = {"sections": [], "assigned": [], "warnings": []}


# ----------------------------------------------------------------------------- generic parsers

def split_row(line: str) -> list[str]:
    s = line.strip()
    assert s.startswith("|"), line
    s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells, cur, esc = [], "", False
    for ch in s:
        if esc:
            cur += ch; esc = False; continue
        if ch == "\\":
            esc = True; cur += ch; continue
        if ch == "|":
            cells.append(cur.strip()); cur = ""; continue
        cur += ch
    cells.append(cur.strip())
    return [c.replace("\\|", "|") for c in cells]


def find_table(lines: list[str], start: int, end: int, header_starts: str, pad_index: int | None = None) -> tuple[list[str], list[list[str]], int]:
    """First table between start and end whose header starts with header_starts. Returns (header, rows, header_line_no)."""
    for i in range(start, end):
        l = lines[i]
        if l.startswith("|") and l.lstrip("| ").startswith(header_starts) and i + 1 < end and re.match(r"^\|\s*-{2,}", lines[i + 1]):
            header = split_row(l)
            rows = []
            j = i + 2
            # Rows may be split into fragments by blank lines or prose notes; take every pipe row
            # in the section after the header, skipping repeated header/separator lines.
            while j < end:
                if not lines[j].startswith("|"):
                    j += 1; continue
                if re.match(r"^\|\s*-{2,}", lines[j]) or split_row(lines[j]) == header:
                    j += 1; continue
                cells = split_row(lines[j])
                if len(cells) != len(header):
                    report["warnings"].append(f"line {j+1}: {len(cells)} cells vs {len(header)} header cells; row kept, cells padded/merged")
                    if len(cells) > len(header):
                        cells = cells[: len(header) - 1] + [" | ".join(cells[len(header) - 1:])]
                    elif pad_index is not None and len(cells) == len(header) - 1:
                        cells = cells[:pad_index] + [""] + cells[pad_index:]
                        report["warnings"].append(f"line {j+1}: '{cells[0]}' had no value in column '{header[pad_index]}' — padded blank; check it (dating rule)")
                    else:
                        cells = cells + [""] * (len(header) - len(cells))
                rows.append(cells)
                j += 1
            return header, rows, i
    raise ValueError(f"table starting '{header_starts}' not found between lines {start+1}-{end}")


def section_bounds(lines: list[str], heading: str, level: str = "## ") -> tuple[int, int]:
    start = None
    for i, l in enumerate(lines):
        if l.strip() == heading:
            start = i
            break
    if start is None:
        raise ValueError(f"heading not found: {heading}")
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith(level) and not lines[j].startswith(level + "#"):
            end = j
            break
    return start, end


def strip_bold(s: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*", r"\1", s or "").strip()


def iso_in(s: str) -> str:
    m = R.ISO_DATE.search(s or "")
    return m.group(1) if m else ""


def split_due(cell: str) -> tuple[str, str]:
    """'**2026-10-15** (review call)' -> ('2026-10-15', '(review call)'); 'Not dated' -> ('', 'Not dated')."""
    c = strip_bold(cell)
    d = iso_in(c)
    if d:
        rest = c.replace(d, "", 1)
        rest = re.sub(r"\(\s*due\s*" + re.escape(d) + r"\s*\)", "", rest)
        rest = re.sub(r"\(\s*\)", "", rest)
        rest = re.sub(r"\s{2,}", " ", rest).strip(" -–—:;,")
        return d, rest
    return "", c


def sec(name, found, written):
    report["sections"].append((name, found, written))


# ----------------------------------------------------------------------------- 05 Commitments

def migrate_05(text: str, dry: bool):
    lines = text.split("\n")
    written = 0

    # Register A — Dated
    s, e = section_bounds(lines, "### Dated", "### ")
    hdr, rows, _ = find_table(lines, s, e, "#", pad_index=4)
    n = 0
    for c in rows:
        cid, action, nxt, cp, due, basis, src = c
        d, dn = split_due(due)
        dn = re.sub(r"\s{2,}", " ", dn)
        meta = {
            "id": cid, "kind": "action", "register": "A", "status": "open",
            "title": strip_bold(action), "owner": "Darryl Benson", "counterparty": strip_bold(cp),
            "due": d, "due_note": dn, "trigger": "", "next_action": R.first_sentence(nxt),
            "basis": strip_bold(basis), "source": strip_bold(src),
            "created": "", "last_touched": R.latest_date(nxt, due, src) or MIGRATION_DATE,
            "needs_triage": False, "legacy_section": "05 Register A Dated",
        }
        body = f"## Next step\n\n{nxt}\n"
        if not dry:
            R.write_item(meta, body)
        n += 1
    sec("05 Register A — Dated", len(rows), n); written += n

    # Register A — Triggered
    s, e = section_bounds(lines, "### Triggered", "### ")
    e2 = section_bounds(lines, "## Other-Owned — Delegated and Awaited")[0]
    hdr, rows, _ = find_table(lines, s, e2, "#", pad_index=4)
    n = 0
    for c in rows:
        cid, action, nxt, cp, trig, basis, src = c
        meta = {
            "id": cid, "kind": "action", "register": "A", "status": "open",
            "title": strip_bold(action), "owner": "Darryl Benson", "counterparty": strip_bold(cp),
            "due": "", "due_note": "", "trigger": strip_bold(trig), "next_action": R.first_sentence(nxt),
            "basis": strip_bold(basis), "source": strip_bold(src),
            "created": "", "last_touched": R.latest_date(nxt, trig, src) or MIGRATION_DATE,
            "needs_triage": False, "legacy_section": "05 Register A Triggered",
        }
        body = f"## Next step\n\n{nxt}\n"
        if not dry:
            R.write_item(meta, body)
        n += 1
    sec("05 Register A — Triggered", len(rows), n); written += n

    # Other-Owned
    s, e = section_bounds(lines, "## Other-Owned — Delegated and Awaited")
    hdr, rows, _ = find_table(lines, s, e, "#", pad_index=4)
    n = 0
    seen = set()
    for c in rows:
        cid, item, owner, typ, gate, crit, note = c
        struck = cid.startswith("~~")
        cid = cid.strip("~ ").strip()
        if not re.fullmatch(r"[BC]\d+", cid):
            report["warnings"].append(f"Other-Owned row with non-standard ID kept as-is: {cid!r}")
        if cid in seen or (R.find_item(cid) and not dry):
            report["warnings"].append(f"Other-Owned duplicate ID {cid}; second row written as {cid}b")
            cid = cid + "b"
        seen.add(cid)
        d, dn = split_due(gate)
        critical = strip_bold(crit).lower().startswith("critical")
        creason = ""
        if critical:
            creason = re.sub(r"^\**critical\**\s*(--|—|-|:)?\s*", "", strip_bold(crit), flags=re.I).strip()
        meta = {
            "id": cid, "kind": "action", "register": "other", "status": "closed" if struck else "open",
            "title": strip_bold(item).strip("~ "), "owner": strip_bold(owner).strip("~ "), "type": strip_bold(typ).strip("~ "),
            "critical": critical, "critical_reason": creason,
            "due": d, "due_note": dn, "next_action": "",
            "source": "", "created": "",
            "last_touched": R.latest_date(note, gate) or MIGRATION_DATE,
            "needs_triage": False, "legacy_section": "05 Other-Owned",
        }
        if struck:
            meta["closed_date"] = iso_in(note)
            meta["disposition_note"] = R.first_sentence(note, 220)
            report["warnings"].append(f"Other-Owned {cid} was struck through in the live table; migrated as closed ({meta['closed_date'] or 'no date'})")
        if not dry:
            R.write_item(meta, note + "\n")
        n += 1
    sec("05 Other-Owned", len(rows), n); written += n

    # Archive — Closed
    s, e = section_bounds(lines, "## Archive — Closed")
    hdr, rows, _ = find_table(lines, s, e, "Date closed")
    n = 0
    used = set()
    for c in rows:
        dc, item, by, note = c
        it = strip_bold(item)
        m = re.match(r"^([ABC]\d+)\s*(—|--|-|–)\s*(.+)$", it)
        if m:
            cid, title = m.group(1), m.group(3).strip()
        else:
            cid = R.next_id("X") if False else None
            cid = f"X{len(used)+1:03d}"
            title = it
            report["assigned"].append((cid, "closed, no ID in source", title[:80]))
        if cid in used:
            cid2 = cid + "b"
            report["warnings"].append(f"duplicate closed ID {cid}; second written as {cid2}")
            cid = cid2
        elif R.find_item(cid) and not dry:
            report["warnings"].append(f"closed {cid} also appeared in a live table (struck through); the Archive — Closed row is kept as the record and overwrites it")
        used.add(cid)
        meta = {
            "id": cid, "kind": "action", "register": "A" if cid.startswith("A") else "other", "status": "closed",
            "title": title, "owner": "Darryl Benson" if cid.startswith("A") else "",
            "closed_date": iso_in(dc) or strip_bold(dc), "closed_by": strip_bold(by),
            "disposition_note": R.first_sentence(note, 220),
            "last_touched": iso_in(dc) or MIGRATION_DATE, "needs_triage": False,
            "legacy_section": "05 Archive Closed",
        }
        body = f"## Closure\n\nDate closed (as recorded): {dc}\n\n{note}\n"
        if not dry:
            R.write_item(meta, body)
        n += 1
    sec("05 Archive — Closed", len(rows), n); written += n

    # Archive — Aged Out
    s, e = section_bounds(lines, "## Archive — Aged Out (Presumed)")
    hdr, rows, _ = find_table(lines, s, e, "Date aged out")
    n = 0
    for c in rows:
        da, item, was, gate, reopened = c
        cid = strip_bold(was).strip() or f"X{200+n:03d}"
        if not re.fullmatch(r"[ABC]\d+", cid):
            report["assigned"].append((f"X{200+n:03d}", f"aged out, 'Was' column = {was!r}", strip_bold(item)[:80]))
            cid = f"X{200+n:03d}"
        if R.find_item(cid) and not dry:
            report["warnings"].append(f"aged-out {cid} already written from another section; written as {cid}x")
            cid = cid + "x"
        meta = {
            "id": cid, "kind": "action", "register": "other", "status": "aged_out",
            "title": strip_bold(item), "due": iso_in(gate), "due_note": strip_bold(gate),
            "closed_date": iso_in(da) or strip_bold(da), "disposition_note": R.first_sentence(reopened, 220),
            "last_touched": iso_in(da) or MIGRATION_DATE, "needs_triage": False,
            "legacy_section": "05 Archive Aged Out",
        }
        if not dry:
            R.write_item(meta, f"## Aged out\n\n{reopened}\n")
        n += 1
    sec("05 Archive — Aged Out", len(rows), n); written += n

    # Archive — Dropped: table rows + bold paragraph entries
    s, e = section_bounds(lines, "## Archive — Dropped")
    hdr, rows, hl = find_table(lines, s, e, "Item")
    n = 0
    for c in rows:
        item, was, reason = c
        cid = strip_bold(was).strip()
        title = strip_bold(item)
        dd = iso_in(item) or iso_in(reason)
        if not re.fullmatch(r"[ABC]\d+", cid):
            newid = f"X{300+n:03d}"
            report["assigned"].append((newid, f"dropped, 'Was' = {was!r}", title[:80]))
            cid = newid
        if R.find_item(cid) and not dry:
            report["warnings"].append(f"dropped {cid}: the ID was later reused for a live item; the old dropped one is written as {cid}-old")
            cid = cid + "-old"
        meta = {
            "id": cid, "kind": "action", "register": "A" if cid.startswith("A") else "other", "status": "dropped",
            "title": re.sub(r"\s*\(dropped [^)]*\)\s*$", "", title), "closed_date": dd,
            "disposition_note": R.first_sentence(reason, 240),
            "last_touched": dd or MIGRATION_DATE, "needs_triage": False, "legacy_section": "05 Archive Dropped (table)",
        }
        if not dry:
            R.write_item(meta, f"## Dropped\n\n{reason}\n")
        n += 1
    # paragraph entries: "**A48 -- title. Killed 2026-10-13, ...**" followed by prose until blank+next bold or table
    paras = []
    i = s + 1
    while i < hl:
        l = lines[i]
        m = re.match(r"^\*\*([ABC]\d+)\s*(--|—|-|–)\s*(.+)$", l)
        if m:
            cid = m.group(1)
            rest = m.group(3)
            blk = [l]
            j = i + 1
            while j < hl and not re.match(r"^\*\*[ABC]\d+\s*(--|—|-|–)", lines[j]) and not lines[j].startswith("|"):
                blk.append(lines[j]); j += 1
            paras.append((cid, rest, "\n".join(blk).strip()))
            i = j
        else:
            i += 1
    pn = 0
    for cid, rest, blk in paras:
        rest_plain = strip_bold(rest)
        mm = re.match(r"^(.*?)\.\s+(Killed|Dropped|Retired|Cancelled|Canceled)\b(.*)$", rest_plain)
        title = mm.group(1).strip() if mm else rest_plain.split(". ")[0]
        dd = iso_in(rest_plain)
        if R.find_item(cid) and not dry:
            report["warnings"].append(f"dropped paragraph {cid} already exists; written as {cid}-old")
            cid = cid + "-old"
        meta = {
            "id": cid, "kind": "action", "register": "A" if cid.startswith("A") else "other", "status": "dropped",
            "title": title, "closed_date": dd,
            "disposition_note": R.first_sentence(rest_plain[len(title):].lstrip(". "), 240),
            "last_touched": dd or MIGRATION_DATE, "needs_triage": False, "legacy_section": "05 Archive Dropped (paragraph)",
        }
        if not dry:
            R.write_item(meta, f"## Dropped\n\n{blk}\n")
        pn += 1
    sec("05 Archive — Dropped (table)", len(rows), n)
    sec("05 Archive — Dropped (paragraphs)", len(paras), pn)
    written += n + pn
    return written


# ----------------------------------------------------------------------------- 04 Watch List

def migrate_04(text: str, dry: bool):
    lines = text.split("\n")
    counter = [0]

    def wid():
        counter[0] += 1
        return f"W{counter[0]:03d}"

    total = 0
    s, e = section_bounds(lines, "## Active")
    hdr, rows, _ = find_table(lines, s, e, "Watch Item")
    n = 0
    for c in rows:
        item, sev, trend, ev, last, notes = c
        cid = wid()
        meta = {
            "id": cid, "kind": "watch", "tier": "active", "status": "open",
            "title": strip_bold(item), "severity": strip_bold(sev), "trend": strip_bold(trend),
            "evidence_basis": strip_bold(ev), "last_touched": iso_in(last) or R.latest_date(notes) or MIGRATION_DATE,
            "created": "", "needs_triage": False, "legacy_section": "04 Active",
        }
        report["assigned"].append((cid, "watch active", meta["title"][:80]))
        if not dry:
            R.write_item(meta, notes + "\n")
        n += 1
    sec("04 Active", len(rows), n); total += n

    s, e = section_bounds(lines, "## Passive Watch")
    hdr, rows, _ = find_table(lines, s, e, "Watch Item")
    n = 0
    for c in rows:
        item, ev, last, notes = c
        cid = wid()
        m = re.search(r"\(was (High|Medium|Low)", notes)
        meta = {
            "id": cid, "kind": "watch", "tier": "passive", "status": "open",
            "title": strip_bold(item), "severity": m.group(1) if m else "", "trend": "",
            "evidence_basis": strip_bold(ev), "last_touched": iso_in(last) or R.latest_date(notes) or MIGRATION_DATE,
            "created": "", "needs_triage": False, "legacy_section": "04 Passive",
        }
        report["assigned"].append((cid, "watch passive", meta["title"][:80]))
        if not dry:
            R.write_item(meta, notes + "\n")
        n += 1
    sec("04 Passive", len(rows), n); total += n

    s, e = section_bounds(lines, "## Retired")
    hdr, rows, _ = find_table(lines, s, e, "Retired")
    n = 0
    for c in rows:
        when, item, reason = c
        cid = wid()
        meta = {
            "id": cid, "kind": "watch", "tier": "retired", "status": "closed",
            "title": strip_bold(item), "closed_date": iso_in(when) or strip_bold(when),
            "disposition_note": R.first_sentence(reason, 240),
            "last_touched": iso_in(when) or MIGRATION_DATE, "needs_triage": False, "legacy_section": "04 Retired",
        }
        report["assigned"].append((cid, "watch retired", meta["title"][:80]))
        if not dry:
            R.write_item(meta, f"## Retired\n\n{reason}\n")
        n += 1
    sec("04 Retired", len(rows), n); total += n
    return total


# ----------------------------------------------------------------------------- 03 Decision Log (Radar + Backlog only)

FIELD_MAP = {
    "status": "status", "owner": "owner", "forum": "forum", "forum where this should be decided": "forum",
    "next action": "next_action", "source": "source", "added": "created",
}


def parse_entries(lines: list[str], s: int, e: int):
    entries = []
    i = s + 1
    while i < e:
        if lines[i].startswith("### "):
            head = lines[i][4:].strip()
            j = i + 1
            while j < e and not lines[j].startswith("### "):
                j += 1
            entries.append((head, lines[i + 1:j]))
            i = j
        else:
            i += 1
    return entries


def migrate_03(text: str, dry: bool):
    lines = text.split("\n")
    counter = [0]

    def did():
        counter[0] += 1
        return f"D{counter[0]:03d}"

    total = 0
    for heading, tier in (("## Decision Radar", "radar"), ("## Decision Backlog", "backlog")):
        s, e = section_bounds(lines, heading)
        entries = parse_entries(lines, s, e)
        n = 0
        for head, body_lines in entries:
            cid = did()
            created = ""
            title = head
            m = re.match(r"^(20\d\d-\d\d-\d\d)\s*(—|--|-|–)\s*(.+)$", head)
            if m:
                created, title = m.group(1), m.group(3).strip()
            meta = {
                "id": cid, "kind": "decision", "tier": tier, "status": "", "title": title,
                "owner": "", "forum": "", "forum_date": "", "next_action": "", "source": "",
                "created": created, "last_touched": "", "needs_triage": False,
                "legacy_section": f"03 {tier}",
            }
            kept = []
            for l in body_lines:
                mm = re.match(r"^- \**([A-Za-z][A-Za-z /]{1,45}?)\**:\s*(.*)$", l)
                if mm:
                    label = mm.group(1).strip().lower()
                    val = mm.group(2).strip()
                    key = FIELD_MAP.get(label)
                    if key and not meta.get(key):
                        if key == "created":
                            meta[key] = iso_in(val) or meta.get("created", "")
                            kept.append(l)  # keep the Added line too; it often carries context
                        else:
                            meta[key] = strip_bold(val)
                            if key == "forum":
                                meta["forum_date"] = iso_in(val)
                        continue
                kept.append(l)
            body = "\n".join(kept).strip("\n")
            resolved = re.search(r"\bRESOLVED\b\s*(20\d\d-\d\d-\d\d)?", head)
            if resolved:
                meta["status"] = "closed"
                meta["closed_date"] = resolved.group(1) or ""
                meta["title"] = re.sub(r"\s*(—|--|-|–)\s*RESOLVED.*$", "", title).strip()
                meta["disposition_note"] = f"Marked RESOLVED in the heading at migration ({resolved.group(1) or 'no date'})."
            meta["last_touched"] = R.latest_date(body, head) or created or MIGRATION_DATE
            report["assigned"].append((cid, f"decision {tier}", meta["title"][:80]))
            if not dry:
                R.write_item(meta, body + "\n")
            n += 1
        sec(f"03 {heading[3:]}", len(entries), n); total += n
    return total


# ----------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="Archive/2026-10-15_pre_registers")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    src = R.ROOT / a.src
    if R.REG_DIR.exists() and any(R.REG_DIR.rglob("*.md")) and not a.dry_run:
        print(f"Registers/ already has items under {R.REG_DIR}; refusing to run twice. Delete it to re-run.", file=sys.stderr)
        sys.exit(2)
    t05 = (src / "05_Commitments.md").read_text(encoding="utf-8")
    t04 = (src / "04_Executive_Watch_List.md").read_text(encoding="utf-8")
    t03 = (src / "03_Decision_Log.md").read_text(encoding="utf-8")
    w5 = migrate_05(t05, a.dry_run)
    w4 = migrate_04(t04, a.dry_run)
    w3 = migrate_03(t03, a.dry_run)

    print("# Migration reconciliation", MIGRATION_DATE, "(dry run)" if a.dry_run else "")
    print()
    print("| Section | Rows/entries found | Items written |")
    print("|---|---|---|")
    for name, f, w in report["sections"]:
        flag = "" if f == w else "  <-- MISMATCH"
        print(f"| {name} | {f} | {w}{flag} |")
    print(f"| **Total** | {sum(f for _, f, _ in report['sections'])} | {w5 + w4 + w3} |")
    print()
    print(f"IDs assigned where the source had none: {len(report['assigned'])}")
    print()
    print("| New ID | From | Title |")
    print("|---|---|---|")
    for cid, frm, title in report["assigned"]:
        print(f"| {cid} | {frm} | {R.md_cell(title)} |")
    print()
    print(f"Warnings: {len(report['warnings'])}")
    for w in report["warnings"]:
        print("-", w)


if __name__ == "__main__":
    main()
