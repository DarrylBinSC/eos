import sys, json
sys.path.insert(0, 'Tools')
import eos_registers as R

TODAY = "2026-10-28"

def close_pointer(item_id, note, body_note):
    path = R.REG_DIR / "action" / f"{item_id}.md"
    meta, body = R.read_item(path)
    meta['status'] = 'dropped'
    meta['closed_date'] = TODAY
    meta['closed_by'] = 'Claude, lane reconciliation (Darryl, 2026-10-28)'
    meta['disposition_note'] = note
    meta['last_touched'] = TODAY
    body = body.rstrip() + "\n\n" + body_note.strip() + "\n"
    R.write_item(meta, body)
    print(f"Dropped {item_id}: {note}")

def create_pulse(id_, title, body, **fields):
    meta = {
        "id": id_, "kind": "pulse", "status": "live", "title": title,
        "owner": "", "product": "", "severity": "Medium", "forum": "",
        "next_action": "", "created": TODAY, "last_touched": TODAY,
        "needs_triage": False, "account": "", "customer_visible": False,
        "escalated_to": "", "escalation": "", "escalation_test": "",
        "first_seen": TODAY, "last_seen": TODAY, "links": [], "people": [],
        "sightings": 1,
    }
    meta.update(fields)
    R.write_item(meta, body.strip() + "\n")
    print(f"Created {id_}: {title}")

# --- Pointer redundancies: substance already on Watch or Decision; nothing to move ---

close_pointer("B24",
    "Same substance already tracked on Watch as W021 (FRBNY release/bid thread); the 3.1.12.13 release-hold detail stays there, not duplicated here.",
    "2026-10-28 (Claude, Register B reconciliation): Dropped. The FRB release-hold substance this item tracked (3.1.12.13 held on an unresolved bug) is already carried on Watch as W021. No new information here; closing rather than duplicating.")

close_pointer("B31",
    "Same substance already tracked on Watch as W019 (Louvre Abu Dhabi closeout -- snag-list stall).",
    "2026-10-28 (Claude, Register B reconciliation): Dropped. The LAD escalation this item referenced is W019 on the Watch list, Active, already queued in the 2026-10-27 reconciliation worklist for the 11-02 read-back. No new information here.")

close_pointer("B58",
    "Same substance already tracked on the Decision Radar as D010 (AI Tech Review -> C2P gate path).",
    "2026-10-28 (Claude, Register B reconciliation): Dropped. The AI Tech Review gate this item referenced is D010 on the Decision Radar, with a named route, process owner (Sourav Pradhan) and gate list already recorded. No new information here.")

close_pointer("B62",
    "Same substance already tracked as Watch W008 (Ford entroCIM (UDAC) renewal and platform-trust gap) and Decision Backlog D045 (Ford system-audit schedule).",
    "2026-10-28 (Claude, Register B reconciliation): Dropped. The audit that gates Ford platform trust is D045 on the Decision Backlog (owner Tim Scott / Chad Steger); the broader trust gap is W008 on Watch. No new information here.")

close_pointer("B73",
    "Same substance already tracked on Watch as W023 (Managed-services staffing readiness for day-two entroCIM monitoring) -- same named owners, Brad Stevens and Nathan Kehr.",
    "2026-10-28 (Claude, Register B reconciliation): Dropped. W023 on the Watch list names the same two owners and the same staffing-readiness gap; already queued in the 2026-10-27 reconciliation worklist for the 11-02 read-back. No new information here.")

close_pointer("B74",
    "Same substance already tracked on Watch as W022 (IDP/ADM production integration -- approved but unstaffed).",
    "2026-10-28 (Claude, Register B reconciliation): Dropped. W022 on the Watch list is the same approved-but-unstaffed IDP/ADM integration this item tracked. No new information here.")

close_pointer("B96",
    "Same substance already tracked as Decision Backlog D045 (Ford system-audit schedule) -- same named owners, Tim Scott and Chad Steger.",
    "2026-10-28 (Claude, Register B reconciliation): Dropped. D045 on the Decision Backlog already carries the Ford audit-scheduling dependency with the same owners. No new information here.")

# --- Test 3: team-level, no Darryl attribution, no escalation basis; move substance to the Pulse ---

create_pulse("P095",
    "WAM resourcing: identify required headcount and skill sets for the data strategy, owed to WAM leadership",
    'Akansh Gangil, explicit: "we should identify the required resource needs, and skill sets necessary to execute this strategy." Owed to Sean McCloskey / WAM leadership. Source: M365 evidence, 2026-09-28.',
    owner="Akansh Gangil", product="WAM", severity="Medium", forum="",
    next_action="Akansh to identify the required resource needs and skill sets for the Wesco-owned-data strategy and bring it to WAM leadership.",
    account="", customer_visible=False, escalation="", escalation_test="",
    first_seen="2026-09-28", last_seen="2026-09-28",
    people=["Akansh Gangil"])

create_pulse("P096",
    "Dell EMS Executive FM Summit: platform leads to work with Robby to flesh out content",
    'Adam Lazare, implied: "I need our \'leads\' to work closely with Robby over the next few weeks to flush the necessary content out." Owed to Robby / Dell EMS, Executive FM Summit. Source: M365 evidence, 2026-09-28.',
    owner="Adam Lazare", product="", severity="Medium", forum="",
    next_action="Platform leads to work with Robby on the Executive FM Summit content.",
    account="Dell", customer_visible=True, escalation="", escalation_test="",
    first_seen="2026-09-28", last_seen="2026-09-28",
    people=["Adam Lazare"])

create_pulse("P097",
    "Complex-build data model: cross-SBU requirements call with Alan, Daniel and Ramesh",
    'Akansh Gangil, explicit: "I will set up a call next week with them." First concrete forum movement on the complex-build data model since the 09-14 Decision Log reopening. Source: M365 evidence, 2026-09-28 to 2026-09-30.',
    owner="Akansh Gangil", product="entroCIM", severity="Medium", forum="",
    next_action="Akansh to hold the requirements call with Alan, Daniel and Ramesh; confirm it happened and what was agreed.",
    account="", customer_visible=False, escalation="", escalation_test="",
    first_seen="2026-10-01", last_seen="2026-10-01",
    people=["Akansh Gangil"])

create_pulse("P098",
    "Digital Products leadership deck: access and instructions for WAM/entroCIM/Navigator/CDA content review",
    'Sridhar Loke, explicit: "I will give all of you access to this deck with some clear instructions as to what I want from each of you." Owed to Digital Products leadership. Source: M365 evidence, 2026-10-01, attribution upgraded to Explicit 2026-10-05.',
    owner="Sridhar Loke", product="", severity="Medium", forum="",
    next_action="Confirm access and instructions were received and the content review proceeded.",
    account="", customer_visible=False, escalation="", escalation_test="",
    first_seen="2026-10-01", last_seen="2026-10-05",
    people=["Sridhar Loke"])

create_pulse("P099",
    "Complex-build cross-SBU data points: share with the team per Darryl's direction to Akansh",
    'Darryl Benson, direct to Akansh: "Make sure you share data points you know we need with the team." See 03 Decisions Made, 2026-10-01 (complex-build cross-SBU entry). The sharing itself is the team action; Darryl\'s direction is not a Darryl commitment under the attribution test.',
    owner="Akansh Gangil", product="entroCIM", severity="Medium", forum="",
    next_action="Confirm Akansh shared the complex-build data points with the team.",
    account="", customer_visible=False, escalation="", escalation_test="",
    first_seen="2026-10-01", last_seen="2026-10-01",
    people=["Akansh Gangil"])

create_pulse("P100",
    "Quest Migration: production MQTT/WAB path for Louvre Abu Dhabi -- Mosquitto FOSS code-change confirmation",
    'Babu Papanna, explicit: "Absolutely, I will follow-up with him and keep you all on e-mail." Owed to the Quest Migration/entroCIM group. Advanced 2026-10-05: the Mosquitto FOSS submission located and can cover production if application code is unchanged (Sean O\'Brien, weekly evidence); code-change confirmation still owner-unclear. Source: M365 evidence, 2026-10-01.',
    owner="Babu Papanna", product="entroCIM", severity="Medium", forum="quest-migration",
    next_action="Confirm whether the application code changed since the Mosquitto FOSS submission; if unchanged, the production MQTT/WAB path for Louvre Abu Dhabi is clear.",
    account="", customer_visible=True, escalation="", escalation_test="",
    first_seen="2026-10-01", last_seen="2026-10-05",
    people=["Babu Papanna", "Sean O'Brien"])

create_pulse("P101",
    "Ford/Wesco: share passwords and create a SharePoint folder for the working team",
    'Jacob Nicosia, explicit: "I\'m going to send the passwords out to the greater team" and "I\'m going to create a folder on SharePoint." Owed to the Ford/Wesco working team. Source: M365 weekly evidence, 2026-10-13.',
    owner="Jacob Nicosia", product="entroCIM", severity="Low", forum="",
    next_action="Confirm the passwords and SharePoint folder were set up for the Ford/Wesco working team.",
    account="Ford", customer_visible=False, escalation="", escalation_test="",
    first_seen="2026-10-13", last_seen="2026-10-13",
    people=["Jacob Nicosia"])

create_pulse("P102",
    "WAM: quick-turn ask to be raised with the team this iteration",
    'Akansh Gangil, explicit: "I\'ll take up to the team if that\'s something that is pretty much quick and we can do it in this iteration itself. I\'ll ask." Source: M365 weekly evidence, 2026-10-13.',
    owner="Akansh Gangil", product="WAM", severity="Low", forum="",
    next_action="Confirm Akansh raised the ask with the team and whether it landed in the iteration.",
    account="", customer_visible=False, escalation="", escalation_test="",
    first_seen="2026-10-13", last_seen="2026-10-13",
    people=["Akansh Gangil"])

for iid, pid, title in [
    ("B88", "P095", "WAM resourcing"),
    ("B89", "P096", "Dell EMS Summit content"),
    ("B90", "P097", "Complex-build data model call"),
    ("B91", "P098", "Digital Products leadership deck access"),
    ("B92", "P099", "Complex-build cross-SBU data points"),
    ("B93", "P100", "Quest Migration MQTT/WAB path"),
    ("B97", "P101", "Ford/Wesco password/SharePoint handoff"),
    ("B99", "P102", "WAM quick-turn ask"),
]:
    close_pointer(iid,
        f"Created under the old intake rule, before the lane model (2026-10-16); moved to the Pulse as {pid}.",
        f"2026-10-28 (Claude, Register B reconciliation): Dropped from the register; the commitment is recorded in Pulse {pid}. A team commitment made in a governed-forum-style evidence sweep is the team's to track.")

print("--- done ---")
