import sys, json
sys.path.insert(0, 'Tools')
import eos_registers as R

TODAY = "2026-10-28"

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

create_pulse("P087",
    "entroCIM refresh hanging for some time while Babu C. Dinesh was away",
    'Zaidi, Syed Jamshed: "I will follow up with Babu around this entroCIM refresh. This is hanging for some time. He was away." Source: `Evidence/M365_Evidence_PulseP1_2026-10-28.md` (transcript).',
    owner="", product="entroCIM", severity="Medium", forum="deployment-scrum",
    next_action="Zaidi to follow up with Babu C. Dinesh on the overdue entroCIM refresh now that he is back.",
    account="", customer_visible=False, escalation="", escalation_test="",
    first_seen="2026-10-27", last_seen="2026-10-27",
    people=["Syed Jamshed Zaidi", "Dinesh Babu C"])

create_pulse("P088",
    "~800-900 additional points pending across four IRCs at the Limerick (Dell) closeout site",
    'Zaidi, Syed Jamshed: "There is like around 800, 900 points more to be added... There are four IRC on this site." Raised alongside the NetBot/watchdog scope-overage discussion (`P057`) at the same Limerick closeout site; no single delivery owner assigned. Source: `Evidence/M365_Evidence_PulseP1_2026-10-28.md` (transcript).',
    owner="", product="entroCIM", severity="Medium", forum="deployment-scrum",
    next_action="Confirm the commercial and delivery disposition of the additional 800-900 IRC points before closeout proceeds.",
    account="Dell", customer_visible=True, escalation="candidate", escalation_test="boundary",
    first_seen="2026-10-27", last_seen="2026-10-27", links=["P057"],
    people=["Syed Jamshed Zaidi", "Scott Dunn", "Mike Reed"])

create_pulse("P089",
    "TCCC ECR connector (TEC 7th floor) timing out; connection info needs verification",
    'Dunn, Scott: "I tried to add the connector for that ECR device yesterday but im getting a timeout, i\'ll need to get Jeremy Hick to verify below info looks correct." TEC 7th floor site. Source: `Evidence/M365_Evidence_PulseP1_2026-10-28.md` (chat).',
    owner="Scott Dunn", product="entroCIM", severity="Medium", forum="deployment-scrum",
    next_action="Dunn to get Jeremy Hick to verify the ECR connector's connection information.",
    account="Coca-Cola (TCCC)", customer_visible=True, escalation="candidate", escalation_test="boundary",
    people=["Scott Dunn", "Jeremy Hick"])

create_pulse("P090",
    "Two new TCCC NAT IP gateways need internal confirmation before checking the customer network side",
    'Dunn, Scott: "Can we just confirm that was the case Clark, Shawn? If so i\'ll see if there is anything Neal can see from the TCCC network side." Source: `Evidence/M365_Evidence_PulseP1_2026-10-28.md` (chat).',
    owner="Scott Dunn", product="entroCIM", severity="Medium", forum="deployment-scrum",
    next_action="Shawn Clark to confirm the NAT IP gateway configuration; Dunn to loop in Neal on the TCCC network side if needed.",
    account="Coca-Cola (TCCC)", customer_visible=True, escalation="candidate", escalation_test="boundary",
    people=["Scott Dunn", "Shawn Clark"])

create_pulse("P091",
    "Repeated timeout and HTTP 504 errors on TCCC devices that had not shown them before; no nginx timeout standard",
    'Dunn, Scott: "I feel like im getting those a lot more frequently now, and on devices we didn\'t before at tccc." Directed to Clark, Shawn; no owner assigned for the nginx timeout standard. Source: `Evidence/M365_Evidence_PulseP1_2026-10-28.md` (chat).',
    owner="", product="entroCIM", severity="Medium", forum="deployment-scrum",
    next_action="Assign an owner to determine the server nginx timeout standard and investigate the increase in timeout/504 errors.",
    account="Coca-Cola (TCCC)", customer_visible=True, escalation="candidate", escalation_test="gap",
    people=["Scott Dunn", "Shawn Clark"])

create_pulse("P092",
    "WAM: selected supplier disappears from License and Orders after navigating away and back",
    'WAM Sprint Review 2026-10-27.loop: a selected supplier would disappear when a user navigated to another page and returned to License and Orders, even though the underlying data remained filtered to that supplier; an intermittent error appears after the action. Natalie reported the error per the Loop notes. Source: `Evidence/M365_Evidence_PulseP2_2026-10-28.md` (Loop).',
    owner="Akansh Gangil", product="WAM", severity="Medium", forum="wam-sprint-review",
    next_action="Gangil to investigate the intermittent error accompanying the supplier-selection display defect.",
    account="", customer_visible=True, escalation="", escalation_test="",
    first_seen="2026-10-27", last_seen="2026-10-27", links=["P093"],
    people=["Akansh Gangil", "Natalie Marquardt"])

create_pulse("P093",
    "WAM: supplier filter returns unrelated sales orders, purchase orders and column-filter values",
    'WAM Sprint Review 2026-10-27.loop: the supplier filter "was returning unrelated sales orders, purchase orders, and column-filter values, making it difficult for users to find relevant records." No owner named. Source: `Evidence/M365_Evidence_PulseP2_2026-10-28.md` (Loop).',
    owner="", product="WAM", severity="Medium", forum="wam-sprint-review",
    next_action="Name an owner to fix the supplier-filter query returning unrelated records.",
    account="", customer_visible=True, escalation="candidate", escalation_test="gap",
    first_seen="2026-10-27", last_seen="2026-10-27", links=["P092"])

create_pulse("P094",
    "WAM critical security vulnerabilities remain open past the team's intended close date",
    'WAM Sprint Review 2026-10-27.loop: critical vulnerabilities had been identified and remained under investigation; the team had expected to close them by the day of the meeting but needed additional time. No owner named in evidence. Source: `Evidence/M365_Evidence_PulseP2_2026-10-28.md` (Loop).',
    owner="", product="WAM", severity="High", forum="wam-sprint-review",
    next_action="Name an owner and a revised close date for the open critical vulnerabilities.",
    account="", customer_visible=False, escalation="candidate", escalation_test="gap",
    first_seen="2026-10-27", last_seen="2026-10-27")

print("--- next id now:", R.next_id("P"), "---")

# Update _forums.json last_evidence
fpath = R.REG_DIR / "pulse" / "_forums.json"
data = json.loads(fpath.read_text())
for forum in data["forums"]:
    if forum["key"] in ("deployment-scrum", "entrocim-standup", "wam-sprint-review"):
        forum["last_evidence"] = TODAY
fpath.write_text(json.dumps(data, indent=2) + "\n")
print("Updated _forums.json last_evidence for deployment-scrum, entrocim-standup, wam-sprint-review")

# Update D096
d_path = R.REG_DIR / "decision" / "D096.md"
meta, body = R.read_item(d_path)
meta["last_touched"] = TODAY
meta["next_action"] = "Confirm with Darryl whether the Stanford roll-back structure call happened and what was agreed; all three information gaps (C73, C74, C76) are now closed."
body = body.rstrip() + "\n\n" + (
    '2026-10-28 (Claude, daily brief): All three information gaps this decision was waiting on are now closed: C73 (Keith, pod dependency) closed 2026-10-20, C74 (Mike, PO terms) closed 2026-10-21, and C76 (Nikos/Brandon, carve-out/18.5) closed 2026-10-27. Darryl\'s own words on C76: "Met with legal, and they were pleased that I brought this to their attention... With the background information provided by the team (Keith and Mike) we are in the clear since the code was started in 2021 (screenshot from Keith)... going forward, we\'ll work with sales and legal to ensure we don\'t miss the click through terms." This clears the IP/ownership blocker on telling Stanford about the Commissioning App. The roll-back structure itself (point counts, dev instance, term, SkySpark-only renewal pricing) is not yet recorded as decided or discussed with Stanford in any evidence reviewed. Needs Darryl\'s word: did the Thursday Stanford call happen, and if so what was the roll-back structure agreed, if anything.'
) + "\n"
R.write_item(meta, body)
print("Updated D096")
