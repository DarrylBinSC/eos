#!/usr/bin/env python3
"""One-time Pulse intake for the 2026-10-20 Prompt 1 (delivery) and Prompt 2 (development) sweeps.
Run from the EOS root: python3 pulse_intake_2026-10-20.py
Sightings are keyed by issue, forum and meeting date; dates already in an item body are not re-counted."""
import json, re, sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
PULSE = ROOT / "Registers" / "pulse"
TODAY = "2026-10-20"
P1 = "`Evidence/M365_Evidence_PulseP1_2026-10-20.md` (transcript)"
P2 = "`Evidence/M365_Evidence_PulseP2_2026-10-20.md` (transcript)"

def read(pid):
    return (PULSE / f"{pid}.md").read_text(encoding="utf-8")

def write(pid, text):
    (PULSE / f"{pid}.md").write_text(text, encoding="utf-8")

def set_field(text, key, value):
    """Replace a front-matter scalar/list. value is the raw YAML right-hand side."""
    head, sep, body = text.partition("\n---\n")
    pat = re.compile(rf"^{key}: .*$", re.M)
    if pat.search(head):
        head = pat.sub(f"{key}: {value}", head, count=1)
    else:
        head = head.rstrip("\n") + f"\n{key}: {value}"
    return head + sep + body

def get_field(text, key):
    m = re.search(rf"^{key}: (.*)$", text, re.M)
    return m.group(1).strip() if m else ""

def people_list(text):
    raw = get_field(text, "people").strip("[]")
    return [p.strip().strip('"') for p in raw.split(",") if p.strip()]

def fmt_list(items):
    return "[" + ", ".join(f'"{x}"' for x in items) + "]"

def has_stamp(text, date, forum):
    return f"{date} ({forum}):" in text

def append(text, para):
    return text.rstrip("\n") + "\n\n" + para.strip() + "\n"

def touch(text):
    return set_field(text, "last_touched", f'"{TODAY}"')

def sighting(pid, date, forum_label, para, people_add=(), status_note=None):
    """Add a sighting (new key) or a note (existing key). Returns 'sighting' or 'note'."""
    t = read(pid)
    already = has_stamp(t, date, forum_label)
    if already:
        t = append(t, f"{date} ({forum_label}): Additional detail on the {date} session (already counted): {para}")
        kind = "note"
    else:
        t = append(t, f"{date} ({forum_label}): {para}")
        t = set_field(t, "sightings", str(int(get_field(t, "sightings") or 0) + 1))
        if date > get_field(t, "last_seen").strip('"'):
            t = set_field(t, "last_seen", f'"{date}"')
        kind = "sighting"
    if people_add:
        cur = people_list(t)
        for p in people_add:
            if p not in cur:
                cur.append(p)
        t = set_field(t, "people", fmt_list(cur))
    if status_note:
        t = append(t, f"{TODAY} (Claude, session): {status_note}")
    write(pid, touch(t))
    return kind

log = []

# ---------------------------------------------------------------- existing issues, delivery track
log.append(("P001", sighting("P001", "2026-10-20", "Daily Scrum",
    'Zaidi: "We were trying it for some time in Grid board, but it we didn\'t get much movement there. So now he\'s using Sky Spark for reporting and dashboard perspective." Pradeep is producing the report in SkySpark; Zaidi committed to follow up. Grid Board itself still unresolved. Source: ' + P1,
    people_add=["Syed Jamshed Zaidi", "Pradeep"],
    status_note="Status better, not resolved: the customer report now has an alternate path (SkySpark) while the Grid Board defect stays open. Owner still blank.")))

log.append(("P001", sighting("P001", "2026-10-15", "Daily Scrum",
    'Dunn, verbatim: "When I went to go put it in grid board, I can\'t even select our site properly from that Wesco Warehouse one where I\'m trying to do the test." Source: ' + P1)))

log.append(("P003", sighting("P003", "2026-10-20", "Daily Scrum",
    'Zaidi: "We may need to book some kind of a working session with their IT team or... temporary access for one of our team members, then we can share a screen with Babu so he can collect whatever he needs." No restoration owner named for the Malaysia PM8000 login on 10-15; Zaidi now proposing the route. Source: ' + P1,
    people_add=["Syed Jamshed Zaidi", "Scott Dunn"])))

log.append(("P004", sighting("P004", "2026-10-15", "Daily Scrum",
    'Heid: "I thought she said that she was okay with the point page and not having graphics... but it sounds like it\'s changing." Dunn: "If anything, I would just make sure with him." Zaidi committed to confirm and review the floor-plan emails. Source: ' + P1,
    people_add=["Matthew Heid", "Scott Dunn", "Syed Jamshed Zaidi"])))

log.append(("P006", sighting("P006", "2026-10-20", "Daily Scrum",
    'Zaidi: "We again don\'t have the exact reason. Keith just applied the fix and we just like did the regression testing and we were unable to reproduce the issue." Keith Bishop applied the fix; Chad Steger named for the customer release communication. Felipe (Dell) had asked for assurance and an RCA on 10-14. Source: ' + P1,
    people_add=["Keith Bishop", "Chad Steger", "Syed Jamshed Zaidi"],
    status_note="Status better, not resolved: a fix is applied and regression testing cannot reproduce the failure, but the cause is still unknown, so the RCA Dell asked for cannot yet be written. The open question for Darryl is what Wesco is willing to tell Dell about a fix without a known root cause; Chad needs that position before he sends the customer communication.")))

log.append(("K006", sighting("K006", "2026-10-20", "Daily Scrum",
    'Keith Bishop applied the Limerick fix; nobody else could state the cause ("We again don\'t have the exact reason"). The RCA still runs through Keith alone. Source: ' + P1)))

log.append(("P028", sighting("P028", "2026-10-20", "Daily Scrum",
    'Zaidi: "It\'s kind of a standstill at the moment... the site meters tag are missing... we don\'t have a capability to build a roll up view in HQ." Shawn Clark and Gaby assigned in the Loop to obtain identification information from the local site teams. Blocks HQ roll-up views across the DMS program. Source: ' + P1,
    people_add=["Shawn Clark", "Gaby"])))

# Already-counted delivery sightings with new verbatim detail (notes only)
log.append(("P005", sighting("P005", "2026-10-14", "Daily Scrum",
    'Zaidi, verbatim: "They are not getting any alarms from El Dorado devices, the devices which are already commissioned and also the same for the Panama ones... they are going to decommission in a couple of weeks environment. So that is critical for them to have the visibility." Matthew Heid named for the new integration; no single owner for the full existing-device alarm gap. Source: ' + P1,
    people_add=["Syed Jamshed Zaidi", "Matthew Heid"])))
log.append(("P011", sighting("P011", "2026-10-14", "Daily Scrum",
    'Same statement as P005 (verbatim in that item). Matthew Heid named for the new integration; no single owner for the existing-device alarm gap. Source: ' + P1,
    people_add=["Syed Jamshed Zaidi", "Matthew Heid"])))
log.append(("P027", sighting("P027", "2026-10-15", "Daily Scrum",
    'Dunn, verbatim: "The ones that are in remote fault... went offline around October 1st... maybe 6 meters... are actually not even in the DB... but they\'re not in Niagara either." Still no restoration owner. Source: ' + P1)))
log.append(("P024", sighting("P024", "2026-10-14", "Daily Scrum",
    'Heid, verbatim: "That standardized list has been something that we\'ve honestly needed for a long time... once we have that, that\'s basically the rule of law." Robbie said to be working with Newcomb and Boyd; no delivery owner or date in the forum. Source: ' + P1)))
log.append(("P016", sighting("P016", "2026-10-13", "Daily Scrum",
    'Dunn, verbatim: "We didn\'t do it as part as Danny\'s original non-DC stuff because it wasn\'t part of the original scope." Zaidi: "We can estimate that, scope it up." Source: ' + P1)))

# ---------------------------------------------------------------- existing issues, development track
log.append(("P032", sighting("P032", "2026-10-20", "Daily Stand Up",
    'Ganiatsas: "I haven\'t followed up with anything on that, though." Bishop: "I have not either. I\'ll take a look at it after this meeting." Keith committed to look; Jason offered to recreate the issue. No movement since 10-14. Source: ' + P2,
    people_add=["Keith Bishop"])))

log.append(("P018", sighting("P018", "2026-10-15", "Daily Stand Up",
    'Singh, verbatim: "Not yet... The VPN connectivity... I think we needed the infra team help over there. So Babu looking that part of the connectivity to the that server." Depends on the infra/network team outside the forum; persisted 10-14 and 10-15. Source: ' + P2)))

log.append(("P010", sighting("P010", "2026-10-15", "Daily Stand Up",
    'Pieschel, verbatim: "I think I\'m about 3/4 of the way down with the redesign... Maybe Monday." On whether equipment can belong to more than one tenant: "But that\'s more beyond my knowledge of it." No owner for confirming the tenant-assignment rule. Source: ' + P2,
    status_note="Status better on the redesign (three-quarters complete by Pieschel's own statement). The tenant-assignment rule (can equipment belong to more than one tenant) is unconfirmed and unowned; K001 was resolved by Darryl today, so this is recorded here rather than reopened there.")))

log.append(("P031", sighting("P031", "2026-10-13", "Daily Stand Up",
    'Savanur: "APIs are not working. They are giving 410 bad requests." Later: "the coordination type... is not getting updated in sync points." Supplied patches did not work. Snyder: "we might have to wait till 407 on that." 403 test environment; no explicit assignment. Source: ' + P2,
    status_note="Scope widened to cover the 403 test-environment connector failures (HTTP 410, sync-point coordinate type), which the 10-19 session had excluded as engineering detail; Prompt 2 on 10-20 raised them as a new issue with no owner, so they are captured here as the same connector-readiness problem rather than as a separate item. first_seen moved to 10-13.")))
t = read("P031"); t = set_field(t, "first_seen", '"2026-10-13"'); t = set_field(t, "title", '"SkySpark connectors failing in test: Energy Direct and others returning no data; 403 environment APIs returning HTTP 410"'); write("P031", t)

# ---------------------------------------------------------------- new issues
NEW = []
def new_issue(pid, **f):
    body = f.pop("body")
    fm = [
        f'id: "{pid}"', 'kind: "pulse"', 'status: "live"',
        f'title: "{f["title"]}"', f'owner: "{f.get("owner","")}"', f'product: "{f.get("product","entroCIM")}"',
        f'severity: "{f["severity"]}"', f'forum: "{f["forum"]}"', f'next_action: "{f["next_action"]}"',
        f'created: "{TODAY}"', f'last_touched: "{TODAY}"', 'needs_triage: false',
        f'account: "{f.get("account","")}"', f'customer_visible: {"true" if f.get("customer_visible") else "false"}',
        'escalated_to: ""', f'escalation: "{f.get("escalation","")}"', f'escalation_test: "{f.get("escalation_test","")}"',
        f'first_seen: "{f["first_seen"]}"', f'last_seen: "{f["first_seen"]}"', f'links: {fmt_list(f.get("links",[]))}',
        f'people: {fmt_list(f.get("people",[]))}', 'sightings: 1',
    ]
    text = "---\n" + "\n".join(fm) + "\n---\n" + body.strip() + "\n"
    assert not (PULSE / f"{pid}.md").exists(), pid
    write(pid, text)
    NEW.append(pid)

# Delivery track (Prompt 1, C1-C4)
new_issue("P035", title="Coke 7th Floor: work assigned with no background material; PO and construction completion unconfirmed",
    owner="Syed Jamshed Zaidi", severity="Medium", forum="deployment-scrum", account="Coca-Cola (TCCC)", customer_visible=True,
    escalation="candidate", escalation_test="boundary", first_seen="2026-10-20",
    next_action="Zaidi to obtain the background and confirm PO and construction status before work starts; contract-or-money test until the PO is confirmed.",
    people=["Matthew Heid", "Syed Jamshed Zaidi"],
    body='2026-10-20 (Daily Scrum): Assignee (unnamed in transcript, "Speaker @1"): "I don\'t know anything about it or have any emails or anything regarding it." Heid: "We just didn\'t either get the PO or they weren\'t fully finished with the construction." Zaidi committed to obtain the background and status. Source: ' + P1 + '\n\n' + TODAY + ' (Claude, session): Account set to Coca-Cola (TCCC) on the "Coke" site name in the package; confirm. Flagged on the boundary test (purchase order status unknown, so money is exposed if work starts).')

new_issue("P036", title="Point-level email alarms do not exist (connector-level only); blocks El Dorado closeout and applies to any site",
    owner="Matthew Heid", severity="High", forum="deployment-scrum", account="Dell", customer_visible=True,
    escalation="candidate", escalation_test="boundary", first_seen="2026-10-20", links=["P011", "P023"],
    next_action="Heid to update the Jira item and get guidance from Elias Brewer or Keith Bishop; development track (Ron Snyder, David Blondel) to say whether point-level alarm push is a product change and when.",
    people=["Matthew Heid", "Syed Jamshed Zaidi", "Elias Brewer", "Keith Bishop"],
    body='2026-10-20 (Daily Scrum): Heid: "Right now it\'s currently tied to the connectors for an alarm push out, but on device or like if an individual point goes down, there\'s nothing that\'s pushed out." Stated as potentially applicable to any site. Heid assigned to update the Jira item and seek guidance; Elias Brewer or Keith Bishop named as technical advisers. Source: ' + P1 + '\n\n' + TODAY + ' (Claude, session): Flagged on the boundary test: a product capability gap raised in the delivery forum whose fix belongs to the development team, and it gates a customer closeout. It has not appeared in any development forum in this window. Related: P011 (El Dorado alarms) and P023 (Penang 2 fault notifications) may be the same underlying limitation.')

new_issue("P037", title="Panama: additional control drawings needed; second-floor NetBotz and watchdog devices not yet procured or installed",
    owner="", severity="Medium", forum="deployment-scrum", account="Wesco Warehouse", customer_visible=True,
    first_seen="2026-10-20", links=["P005", "P015"],
    next_action="Name the procurement owner for the second-floor NetBotz and watchdog devices; Zaidi updating tasks and references.",
    people=["Syed Jamshed Zaidi"],
    body='2026-10-20 (Daily Scrum): Zaidi: "There is a second floor where they have to procure net bots and watchdog monitors because nothing is being installed there." Zaidi owns task and reference updates; no procurement owner named. Source: ' + P1 + '\n\n' + TODAY + ' (Claude, session): Account set to Wesco Warehouse per the roster (Panama is a Wesco site, Darryl 2026-10-16); the package labelled it "Panama, Dell". Owner left blank so the no-owner gap test applies to procurement.')

new_issue("P038", title="Apex: four meter connectors ready but connectivity cannot be established; waiting on information from Robbie",
    owner="Matthew Heid", severity="Medium", forum="deployment-scrum", account="Dell", customer_visible=True,
    first_seen="2026-10-20",
    next_action="Heid waiting on connection details from Robbie (Dell); chase if not received this week.",
    people=["Matthew Heid", "Robbie"],
    body='2026-10-20 (Daily Scrum): Heid: "I\'ve got the connectors good, but we\'re not able to connect. So I asked for some more information. So I\'m waiting for that from him." Source: ' + P1 + '\n\n' + TODAY + ' (Claude, session): Account set to Dell on the package label ("Apex, Dell") and K005 (Apex listed with Franklin and Hortolandia as Dell FTE sites); Apex added as a Dell alias in the roster, confirm.')

# Development track (Prompt 2, C1-C9); C1 folded into P031 above
new_issue("P039", title="Tiles Grid Board compose chart: precision and date-handling defects cancel comparisons",
    owner="Priyatosh Patra", severity="Medium", forum="entrocim-standup", customer_visible=False,
    first_seen="2026-10-15", links=["P001", "P030"],
    next_action="Patra to retest against a current build and confirm the fixes.",
    people=["Priyatosh Patra"],
    body='2026-10-15 (Daily Stand Up): Patra: "One is the precision one, the other one is... Date in the compose chart, all comparisons are cancelled." Team attempting fixes; Patra to obtain a current build for retesting. Source: ' + P2)

new_issue("P040", title="Shared UI components lack consistent button and styling standards as apps move into the monorepo",
    owner="Harsha E", severity="Medium", forum="entrocim-standup", customer_visible=False,
    first_seen="2026-10-20",
    next_action="Joseph Kusnir to document the inconsistencies; Harsha E to set the unified component standard, per David Blondel.",
    people=["Joseph Kusnir", "David Blondel", "Harsha E"],
    body='2026-10-20 (Daily Stand Up): Kusnir: "we need to come up with some sort of unified setting for... buttons and stuff before this gets out of control again." Blondel: "let\'s start with Harsha and just make sure everything\'s consistent." Source: ' + P2)

new_issue("P041", title="Showcase stopped running and recorded no data from Thursday night into Friday morning (10-16 to 10-17)",
    owner="", severity="High", forum="entrocim-standup", customer_visible=True,
    first_seen="2026-10-20", links=["P032"],
    next_action="Name an owner for the Showcase outage and the data gap; confirm whether anyone external saw it and whether Showcase has uptime monitoring.",
    people=["Keith Bishop"],
    body='2026-10-20 (Daily Stand Up): Bishop: "Showcase does have a gap Thursday night, Friday morning, because nothing was recording data as well. It wasn\'t running." Keith checked subsequent shutdown behavior and confirmed the data gap; no owner assigned. Source: ' + P2 + '\n\n' + TODAY + ' (Claude, session): No owner (gap test). Showcase is used for external positioning, so customer_visible is set true on potential exposure; no customer was named. Whether the gap is known outside the forum is not in evidence.')

new_issue("P042", title="entroCIM 3.1.12.14 customer release notice one day behind the stated date (Chad out sick 10-19)",
    owner="Chad Steger", severity="Medium", forum="entrocim-standup", customer_visible=True,
    first_seen="2026-10-20", links=["P030"],
    next_action="Chad to send the external customer correspondence on 10-20 and coordinate PAS01 to PAS06 updates with Shawn Clark; Darryl named on the copy list.",
    people=["Chad Steger", "Shawn Clark"],
    body='2026-10-20 (Daily Stand Up): Steger: "today\'s the 20th and it says the 19th. I was out sick yesterday, so I\'m going to be working to try to get the e-mail correspondence out to the customers today." Dell was separately named as already sent. The 10-20 transcript names Darryl among the people Chad intended to copy. Source: ' + P2 + '\n\n' + TODAY + ' (Claude, session): The package lists the forum as Daily Stand Up and the session as the 10-20 Backlog Deep Dive; filed under the stand-up as the package\'s forum column states. Not flagged as a call: an owner and a same-day action are named, and being copied is awareness, not a decision.')

new_issue("P043", title="Schneider OPC UA protocol decision and proof of concept pending; constrains further Dell GMS completion",
    owner="", severity="High", forum="entrocim-backlog", account="Dell", customer_visible=True,
    escalation="candidate", escalation_test="boundary", first_seen="2026-10-20", links=["K004"],
    next_action="Name who on the Wesco side owns the push on Schneider (vendor relationship, likely Darryl or Sean McCloskey); get a date for the proof of concept.",
    people=["Chad Steger"],
    body='2026-10-20 (Backlog Deep Dive): Steger: "Schneider has a protocol OPC UA that I think is the route we\'re going to be going, but it\'s kind of in Schneider\'s court right now. So there\'s a big opportunity to get a lot more of our GMS programme complete once that door opens up." Schneider holds the decision; no individual owner named. Source: ' + P2 + '\n\n' + TODAY + ' (Claude, session): Flagged on the boundary test: an external vendor outside the forum gates Dell GMS completion and no one on our side owns the push.')

new_issue("P044", title="About $10,000 of completed delivery work may not yet be invoiced",
    owner="Chad Steger", severity="Medium", forum="entrocim-backlog", customer_visible=False,
    escalation="candidate", escalation_test="boundary", first_seen="2026-10-20",
    next_action="Chad to verify with Lindsay Cotten whether the invoices were issued and raise them if not.",
    people=["Chad Steger", "Lindsay Cotten"],
    body='2026-10-20 (Backlog Deep Dive): Steger: "we should have invoiced and if we haven\'t, I\'ll work with Lindsay to get those invoice... we should be invoicing for around 10 grand for that." Dell context in the delivery and billing section; the exact projects were not named in the quoted passage. Source: ' + P2 + '\n\n' + TODAY + ' (Claude, session): Flagged on the money test. Account left blank: the package places it in a Dell context but does not name the projects.')

new_issue("P045", title="Automated weekly sales project updates paused: Rovo disabled pending AI approval",
    owner="Chad Steger", severity="Medium", forum="entrocim-backlog", product="Jira / Rovo", customer_visible=False,
    escalation="candidate", escalation_test="boundary", first_seen="2026-10-20",
    next_action="Identify who at Wesco owns the Rovo AI approval; Chad to decide on an alternative route if it is not re-enabled.",
    people=["Chad Steger", "Syed Jamshed Zaidi"],
    body='2026-10-20 (Backlog Deep Dive): Steger: "they shut it off and we\'re kind of waiting for them to turn it back on... And if they don\'t, then I\'ll have to look at alternative routes for doing this." Chad and Zaidi were developing the workflow; no approval owner named. Sales loses the planned customer talking points. Source: ' + P2 + '\n\n' + TODAY + ' (Claude, session): Flagged on the boundary test: the approval sits with an AI governance function outside the forum, and Sales is the consumer.')

new_issue("P046", title="Marygrove: three open tickets; JACE down and customer IT cannot be reached",
    owner="", severity="High", forum="entrocim-backlog", account="Marygrove", customer_visible=True,
    first_seen="2026-10-20",
    next_action="Name an owner for the Marygrove tickets and a route to the customer's IT team; some hosted tickets depend on the Q3 release rollout (Mike).",
    people=["Chad Steger", "Mike"],
    body='2026-10-20 (Backlog Deep Dive): Steger: "Marygrove... have three tickets open right now that we\'re working through. Unfortunately, it\'s a Jace down, can\'t get a hold of IT conversation right now." Mike stated that some hosted tickets depended on rollout of the Q3 release. No owner assigned. Source: ' + P2 + '\n\n' + TODAY + ' (Claude, session): No owner (gap test). Marygrove added to the account roster as a customer; confirm.')

# Knowledge: Elias Brewer alarm audit
k7 = f'''---
id: "K007"
kind: "pulse"
status: "live"
category: "knowledge"
title: "Americas/LATAM watchdog, temperature-sensor and power-failure alarm audit; point-level alarm configuration"
holder: "Elias Brewer"
backup: "Keith Bishop"
coverage: "partial"
exposure: ["customer"]
mitigation: "Keith Bishop named as the next technical adviser if Elias cannot assist; Keith also sole holder of the Limerick RCA (K006), so the backup is itself concentrated"
absence_date: ""
account: "Dell"
track: "delivery"
product: "entroCIM"
created: "{TODAY}"
last_touched: "{TODAY}"
needs_triage: false
escalated_to: ""
escalation: ""
escalation_test: ""
first_seen: "2026-10-14"
last_seen: "2026-10-20"
links: ["K006", "P036", "P011", "P005"]
sightings: 2
---
2026-10-14 (Daily Scrum): Zaidi: "That is a task I have assigned to Eli... I'm hoping like once he's back, we can pick those these tasks." The alarm audit waits on Elias's return; no return date stated. Source: {P1}

2026-10-20 (Daily Scrum): Heid, on the point-level alarm configuration needed for El Dorado closeout: "That'd be an Eli question. Or if not Eli, Keith Bishop." Source: {P1}

{TODAY} (Claude, session): Created on the "absence opens a gap" and "work waits on one person" tests. Both Elias and Keith were out during the window, and the alarm-handler, alarm-audit and alarm-configuration knowledge that P006, P011/P005 and P036 depend on sits with the two of them. Coverage partial because Keith is a named backup; the exposure is that the backup is the other single point of failure.
'''
write("K007", k7)
NEW.append("K007")

# ---------------------------------------------------------------- forums and accounts
fj = PULSE / "_forums.json"
forums = json.loads(fj.read_text(encoding="utf-8"))
for f in forums["forums"]:
    if f["key"] in ("deployment-scrum", "entrocim-standup", "entrocim-backlog"):
        f["last_evidence"] = TODAY
    if f["key"] == "quest-migration":
        f["notes"] = (f.get("notes", "") + " " if f.get("notes") else "") + "2026-10-20 sweep: 10-13 occurrence met but no transcript, Loop, recap or chat was accessible; 10-20 occurrence (3:00 PM) had not happened at sweep time. last_evidence not advanced."
    if f["key"] == "deployment-knowledge-share":
        f["notes"] = (f.get("notes", "") + " " if f.get("notes") else "") + "Not found by exact name in the 2026-10-12 to 10-20 sweep; calendar title to be confirmed."
fj.write_text(json.dumps(forums, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

aj = PULSE / "_accounts.json"
acc = json.loads(aj.read_text(encoding="utf-8"))
for a in acc["accounts"]:
    if a["name"] == "Dell" and "Apex" not in a["aliases"]:
        a["aliases"].append("Apex")
        a["note"] += "; Apex added 2026-10-20 from the Prompt 1 label and K005, confirm"
    if a["name"] == "Coca-Cola (TCCC)" and "Coke" not in a["aliases"]:
        a["aliases"].append("Coke")
if not any(a["name"] == "Marygrove" for a in acc["accounts"]):
    acc["accounts"].append({"name": "Marygrove", "type": "customer", "aliases": [], "note": "Hosted entroCIM customer; added 2026-10-20 from the Backlog Deep Dive (P046), confirm"})
aj.write_text(json.dumps(acc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

print("NEW:", ", ".join(NEW))
for pid, kind in log:
    print(f"{pid}: {kind}")
