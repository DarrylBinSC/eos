#!/usr/bin/env python3
"""
pulse_seed_2026-10-16.py — one-time setup of the Operational Pulse (lane model), 2026-10-16.

Decision: Darryl, 2026-10-16 session. Issues from team-governed forums (deployment scrum, sprint
stand-ups, backlog refinement, ...) leave the registers and live in the Pulse. They reach the registers
only by escalation. Design and tests: CLAUDE.md, "Operational Pulse (lane model)".

What this does (idempotent; safe to re-run):
  1. Writes Registers/pulse/_forums.json (team-governed forums from 07_Operating_Cadence.md).
  2. Seeds Pulse issues P001-P009 from the 2026-10-16 evidence package and from the Watch items whose
     substance is deployment-level.
  3. Retires W004, W012, W013, W024, W098 to the Pulse (reversible: set tier back to active).
     W009 stays Active as the escalated home of P006 (stuck since 08-25; customer RCA owed).
  4. Drops B108, B109, B110 (created this morning under the old rule) into the Pulse.
  5. Notes on B15 and B37: the closure question raised this morning is withdrawn.
  6. Regenerates 03/04/05 and 11_Operational_Pulse.md.

Run from the EOS root:  python3 Tools/pulse_seed_2026-10-16.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import eos_registers as R  # noqa: E402
import eos_pulse as P  # noqa: E402

T = "2026-10-16"
STAMP = f"{T} (Claude, session)"

FORUMS = {
    "note": "Team-governed forums: run on the team's own governance (project process or sprint cycle). "
            "Their issues live in the Pulse, not the registers. 'confirmed' = Darryl has confirmed the classification. "
            "Source: 07_Operating_Cadence.md, 2026-10-16. Edit by hand or ask Claude.",
    "forums": [
        {"key": "deployment-scrum", "name": "2026 Deployment Daily Scrum", "governance": "Project management", "owner": "Chad Steger", "facilitator": "Syed Jamshed Zaidi", "cadence": "Daily", "products": ["entroCIM"], "aliases": ["2026 Deployment - Daily Scrum", "Deployment Daily Scrum", "Daily Scrum"], "confirmed": True},
        {"key": "entrocim-standup", "name": "entroCIM Daily Stand Up", "governance": "Sprint (2-week)", "owner": "Ron Snyder", "facilitator": "David Blondel (cover)", "cadence": "Daily", "products": ["entroCIM"], "aliases": ["Daily Stand Up", "Daily Standup"], "confirmed": True},
        {"key": "entrocim-backlog", "name": "entroCIM Backlog Deep Dive", "governance": "Sprint / backlog", "owner": "David Blondel", "cadence": "Bi-weekly", "products": ["entroCIM"], "aliases": [], "confirmed": False, "notes": "07 lists Darryl as Attend; confirm it is team-governed"},
        {"key": "dcoe-entrocim", "name": "DCOE & entroCIM Weekly", "governance": "Release governance (DCOE)", "owner": "Balachandar Murali", "cadence": "Weekly", "products": ["entroCIM"], "aliases": [], "confirmed": False},
        {"key": "quest-migration", "name": "Quest Migration Weekly Check-In", "governance": "Project management", "owner": "Chad Steger", "cadence": "Weekly", "products": ["entroCIM"], "aliases": [], "confirmed": False},
        {"key": "showcase", "name": "Showcase recurring", "governance": "Project management", "owner": "David Blondel", "cadence": "Bi-weekly", "products": ["entroCIM"], "aliases": [], "confirmed": False},
        {"key": "deployment-knowledge-share", "name": "Deployment Team Knowledge Share", "governance": "Team practice", "owner": "TBC", "cadence": "Periodic", "products": ["entroCIM"], "aliases": [], "confirmed": False},
        {"key": "wam-backlog-refinement", "name": "WAM Product Backlog Refinement", "governance": "Sprint", "owner": "Sakshi Mathur", "cadence": "Bi-weekly", "products": ["WAM"], "aliases": [], "confirmed": False},
        {"key": "wam-sprint-review", "name": "WAM Sprint Review", "governance": "Sprint", "owner": "Sakshi Mathur", "cadence": "Bi-weekly", "products": ["WAM"], "aliases": [], "confirmed": False},
        {"key": "wam-india-dev", "name": "WAM India Dev Team weekly", "governance": "Sprint", "owner": "TBC", "cadence": "Weekly", "products": ["WAM"], "aliases": [], "confirmed": False},
        {"key": "wam-product-discussion", "name": "WAM Product discussion", "governance": "Product execution", "owner": "Akansh Gangil", "cadence": "Weekly", "products": ["WAM"], "aliases": [], "confirmed": False},
        {"key": "adm-connect", "name": "ADM connect with Natalie", "governance": "Product execution", "owner": "Akansh Gangil", "cadence": "Weekly", "products": ["WAM"], "aliases": [], "confirmed": False, "notes": "07 raises Darryl to Attend while the part-number and leaf-node dependencies are open"},
        {"key": "product-platform-connect", "name": "Product Team / Platform Team connect", "governance": "Team practice", "owner": "Keyur Patel", "cadence": "Weekly", "products": [], "aliases": [], "confirmed": False},
    ],
}

SRC_SCRUM = "2026 Deployment - Daily Scrum, 2026-10-15 (transcript and Loop, retrieved complete); `Evidence/M365_Evidence_Daily_2026-10-16.md`"
SRC_STAND = "Daily Stand Up, 2026-10-15 (transcript, retrieved complete); `Evidence/M365_Evidence_Daily_2026-10-16.md`"

ISSUES = [
    dict(id="P001", forum="deployment-scrum", account="Dell", product="entroCIM", severity="High", customer_visible=True,
         title="PC1 Grid Board site-selection defect blocking the KWH report and dashboard",
         owner="", people=["Scott Dunn", "Syed Jamshed Zaidi", "Pradyumna Umarji"],
         first_seen="2026-10-15", last_seen="2026-10-15", sightings=1, links=["W098", "B108", "B15", "B37"],
         next_action="Name a recovery owner and date; validate the fix in the target environment before telling Dell it is fixed.",
         body=[f"2026-10-15 (Daily Scrum): The test site could not be selected correctly on the PC1 Grid Board; the KWH report and dashboard Robbie (Dell) is waiting on are unfinished. No recovery owner or date named in evidence. Scott Dunn, explicit: \"let me find where that was saved and I can ping it to you guys\" (the prior PC1 report). Source: {SRC_SCRUM}.",
               f"{STAMP}: Moved from W098 and B108 under the lane model. Flagged \"needs your call\" on the gap test (no recovery owner). The B15/B37 closure question from this morning is withdrawn: this issue is where that substance lives now."]),
    dict(id="P002", forum="deployment-scrum", account="Dell", product="entroCIM", severity="High", customer_visible=True,
         title="Dell meter-data integrity: negative values, missing main meters, unreliable PPS3B data, demand/utilization mismatches",
         owner="Syed Jamshed Zaidi", people=["Scott Dunn", "Matthew Heid"],
         first_seen="2026-10-15", last_seen="2026-10-15", sightings=1, links=["B109", "B15"],
         next_action="Site-by-site data-quality log with the source-system owner and a resolution date (Syed tracking).",
         body=[f"2026-10-15 (Daily Scrum): Negative values, unreliable PPS3B data, missing main meters, and demand/utilization mismatches discussed. RTP meter now connected and providing data (Matthew Heid); Apex meters still open. Singapore records updated with remote-fault conditions and meters absent from both the internal database and Niagara (Scott Dunn). Sites missing site-meter information stay in due diligence until it is available (Rob aligned). Syed Jamshed Zaidi, explicit: \"I'll make sure that we have somewhere we are tracking it and logging that one too.\" Source: {SRC_SCRUM}.",
               f"{STAMP}: Moved from B109 under the lane model. Related history: B15 (PC1 meters offline, ticket 3046, closed 2026-10-15)."]),
    dict(id="P003", forum="deployment-scrum", account="Dell", product="entroCIM", severity="Medium", customer_visible=False,
         title="Dell IT access and investigation dependencies: Malaysia login failure, refresh-page issue, Panek BMS validation",
         owner="Syed Jamshed Zaidi", people=[],
         first_seen="2026-10-15", last_seen="2026-10-15", sightings=1, links=["B110"],
         next_action="Book the review with Robbie and Dell IT; get an ETA from each Dell-side owner.",
         body=[f"2026-10-15 (Daily Scrum): Logs supplied to Dell IT; findings and site access still incomplete; trend worsening if unresolved. Syed Jamshed Zaidi, explicit: \"I will book some time with ... Robbie and Dell IT team.\" Source: {SRC_SCRUM}.",
               f"{STAMP}: Moved from B110 under the lane model."]),
    dict(id="P004", forum="deployment-scrum", account="Dell", product="entroCIM", severity="Medium", customer_visible=True,
         title="Dell visualization scope unsettled: point pages only, or basic graphics and floor plans (El Dorado)",
         owner="", people=["Syed Jamshed Zaidi"], escalation="candidate", escalation_test="boundary",
         first_seen="2026-10-15", last_seen="2026-10-15", sightings=1, links=[],
         next_action="Written scope confirmation from Dell (Robbie, Danny) before graphics work is added.",
         body=[f"2026-10-15 (Daily Scrum): Point pages may have been accepted earlier; current Dell expectations may include basic graphics and floor plans. Scope appears to be changing. Dell-side stakeholders Robbie and Danny; no Wesco owner named. Source: {SRC_SCRUM}.",
               f"{STAMP}: Flagged \"needs your call\" on the boundary test: a scope expansion is a commercial question the scrum cannot settle on its own."]),
    dict(id="P005", forum="deployment-scrum", account="", product="entroCIM", severity="High", customer_visible=True,
         title="Commissioned El Dorado and Panama devices not producing expected alarms ahead of environment decommissioning",
         owner="Syed Jamshed Zaidi", people=["Chad Steger"],
         first_seen="2026-10-14", last_seen="2026-10-14", sightings=1, links=["W024"],
         next_action="Dated recovery plan; validate alarms before decommissioning proceeds.",
         body=["2026-10-14 (Daily Scrum): Syed Zaidi, direct: the customer is not getting alarms from commissioned devices, and called visibility critical before an environment decommissioning expected within weeks. No RCA or remediation timeline in evidence. Escalation path Chad Steger.",
               f"{STAMP}: Moved from W024 under the lane model. Account not stated in evidence; El Dorado appears in a Dell context on 2026-10-15 (visualization scope, P004). Confirm whether these are Dell sites; if so set account to Dell."]),
    dict(id="P006", forum="deployment-scrum", account="Dell", product="entroCIM", severity="High", customer_visible=True,
         title="Dell alarm-database corruption: intermittent alarming failures, no root cause",
         owner="Ron Snyder; Keith Bishop", people=[],
         first_seen="2026-08-25", last_seen="2026-10-14", sightings=4, links=["W009"],
         escalation="escalated", escalated_to="W009",
         next_action="Written RCA from Keith Bishop or Ron Snyder; formal assurance response to Dell.",
         body=["2026-08-25 (Daily Scrum): Intermittent alarming failures traced to alarm-database corruption; no root cause; manual live-reset only; preventive fix scheduled for the October release.",
               "2026-09-15 (Daily Scrum): Recurred and manually repaired twice this cycle; no named root-cause owner.",
               "2026-09-16 (Daily Stand Up): Keith Bishop, corrupted alarm data of unknown origin; Ron Snyder to verify the Limerick 2 SkySpark version; cleared-alarm notification config unconfirmed.",
               "2026-10-14 (Daily Scrum): Limerick RCA still not provided; test notifications worked, which does not resolve the intermittent cause.",
               f"{STAMP}: Seeded from W009. Stays escalated: stuck (raised since 2026-08-25) and it crosses the boundary test (a customer RCA and assurance response is owed). W009 keeps tracking your part."]),
    dict(id="P007", forum="deployment-scrum", account="Dell", product="entroCIM", severity="High", customer_visible=True,
         title="PC1/JCI large-scale point faults and intermittent site access",
         owner="Scott Dunn", people=[],
         first_seen="2026-09-15", last_seen="2026-09-15", sightings=1, links=["W012", "B15"],
         next_action="JCI-side screenshots, consolidated equipment inventory, a named root-cause owner.",
         body=["2026-09-15 (Daily Scrum): Roughly half the points described as faulted (reference to 12,000 points), a JCI equipment-availability dimension, on-site stakeholders treating it as emergency service. Scott Dunn committed to a consolidated PC1 equipment inventory.",
               f"{STAMP}: Moved from W012 under the lane model. No sighting since 2026-09-15, so it shows as quiet: confirm with the team whether it is resolved or still open. Related: P001 (Grid Board), same PC1 site."]),
    dict(id="P008", forum="deployment-scrum", account="Dell", product="entroCIM", severity="Medium", customer_visible=False,
         title="Dell cluster session loss: fleet-wide configuration review still open",
         owner="Syed Jamshed Zaidi; Elias Brewer", people=["Ron Snyder"],
         first_seen="2026-09-16", last_seen="2026-09-28", sightings=2, links=["W004", "B84"],
         next_action="Confirm whether the bidirectional-URI misconfiguration exists on other Dell cluster nodes.",
         body=["2026-09-18 (Re: Server Session Lost Issues, email): Root cause confirmed (both nodes initiating the cluster connection); Ron Snyder's fix holds; fleet-wide review open; Syed Zaidi to assist Elias Brewer with cleanup (B84).",
               "2026-09-28 (weekly evidence): cleanup commitment reconfirmed, still in progress; no new session-loss events.",
               f"{STAMP}: Moved from W004 under the lane model. Quiet since 2026-09-28."]),
    dict(id="P009", forum="deployment-scrum", account="Coca-Cola (TCCC)", product="entroCIM", severity="High", customer_visible=True,
         title="TCCC/AOC Modbus gateway sourcing may delay gas-sensor integration",
         owner="Scott Dunn", people=[],
         first_seen="2026-09-15", last_seen="2026-09-15", sightings=1, links=["W013"],
         next_action="Alternate sourcing and a committed delivery date.",
         body=["2026-09-15 (Daily Scrum): Required Modbus gateways may have long lead times; Scott Dunn: sourcing \"is going to hold it up\". Risk of schedule delay and panel rework.",
               f"{STAMP}: Moved from W013 under the lane model. Quiet since 2026-09-15: confirm with the team."]),
    dict(id="P010", forum="entrocim-standup", account="", product="entroCIM", severity="Medium", customer_visible=False,
         title="entroCIM tenant redesign and boot-mode routing: no acceptance criteria, rollout sequence or release date yet",
         owner="Michael Pieschel", people=["Nihar Ranjan Sahu", "Jason Ganiatsas", "Maggie Becker", "David Blondel"],
         first_seen="2026-10-15", last_seen="2026-10-15", sightings=1, links=["W066"],
         next_action="Acceptance criteria, migration plan, security review and a release date before rollout.",
         body=[f"2026-10-15 (Daily Stand Up): Tenant redesign (tenant creation, asset assignment and removal, user-to-tenant access boundaries) about three-quarters complete (Michael Pieschel). New boot-mode routing (user-specific dev URL and dev view) implemented, tested and on the dev server (Nihar Ranjan Sahu). Release-gate criteria not captured. Michael to update the Confluence documentation; Nihar to share the boot-mode story and documentation. Michael named Jason Ganiatsas as the go-to on tenant behavior (\"Jason G is pretty knowledgeable about it\"); Maggie Becker ramping to build enablement material. Source: {SRC_STAND}.",
               f"{STAMP}: Seeded under the lane model. The knowledge-concentration angle stays visible in People and in W066 (Darryl's carve-out, 2026-10-16)."]),
]

RETIRE_W = {
    "W098": "P001", "W024": "P005", "W012": "P007", "W004": "P008", "W013": "P009",
}
DROP_B = {"B108": "P001", "B109": "P002", "B110": "P003"}


def main():
    P.PULSE_DIR.mkdir(parents=True, exist_ok=True)
    P.FORUMS_FILE.write_text(json.dumps(FORUMS, indent=1) + "\n", encoding="utf-8")
    print("forums:", len(FORUMS["forums"]))

    for d in ISSUES:
        d = dict(d)
        body = "\n\n".join(d.pop("body"))
        meta = {"kind": "pulse", "status": "live", "escalation": "", "escalation_test": "", "escalated_to": "",
                "created": T, "last_touched": T, "needs_triage": False}
        meta.update(d)
        if (P.PULSE_DIR / f"{meta['id']}.md").exists():
            print("exists, skipped:", meta["id"]); continue
        R.write_item(meta, body)
        print("pulse:", meta["id"])

    for wid, pid in RETIRE_W.items():
        f = R.find_item(wid)
        if not f:
            print("missing:", wid); continue
        meta, body, _ = f
        if meta.get("tier") == "retired":
            continue
        meta.update({"tier": "retired", "status": "closed", "closed_date": T,
                     "closed_by": "Claude, lane model (Darryl, 2026-10-16)",
                     "disposition_note": f"Returned to team governance; tracked in the Pulse as {pid}. Reversible: set tier to active.",
                     "last_touched": T})
        body = (body or "").rstrip("\n") + f"\n\n{STAMP}: Retired to the Pulse as {pid} under the lane model (Darryl, 2026-10-16): deployment-level issues run on the team's own governance and reach the registers only by escalation. Set tier back to active to reverse.\n"
        R.write_item(meta, body)
        print("retired:", wid, "->", pid)

    for bid, pid in DROP_B.items():
        f = R.find_item(bid)
        if not f:
            print("missing:", bid); continue
        meta, body, _ = f
        if meta.get("status") != "open":
            continue
        meta.update({"status": "dropped", "closed_date": T, "closed_by": "Claude, lane model (Darryl, 2026-10-16)",
                     "disposition_note": f"Created this morning under the old intake rule; moved to the Pulse as {pid}.", "last_touched": T})
        body = (body or "").rstrip("\n") + f"\n\n{STAMP}: Dropped from the registers; the commitment is recorded in Pulse {pid}. A team commitment made in a governed forum is the team's to track.\n"
        R.write_item(meta, body)
        print("dropped:", bid, "->", pid)

    for bid, pid in (("B15", "P001, P002, P007"), ("B37", "P001")):
        f = R.find_item(bid)
        if not f:
            continue
        meta, body, _ = f
        if "lane model" in (body or ""):
            continue
        body = (body or "").rstrip("\n") + f"\n\n{STAMP}: The closure question raised in this morning's brief is withdrawn. Under the lane model (Darryl, 2026-10-16) the Dell/PC1 substance is deployment-level and lives in the Pulse ({pid}); your 2026-10-15 closure stands.\n"
        meta["last_touched"] = T
        R.write_item(meta, body)
        print("noted:", bid)

    f = R.find_item("W009")
    if f:
        meta, body, _ = f
        if "P006" not in (body or ""):
            body = (body or "").rstrip("\n") + f"\n\n{STAMP}: Stays Active as the escalated home of Pulse P006. The deployment detail now accumulates in P006; this row tracks your part: a written RCA and a formal assurance response to Dell.\n"
            meta["last_touched"] = T
            R.write_item(meta, body)
            print("noted: W009")

    print(R.regenerate_all())


if __name__ == "__main__":
    main()
