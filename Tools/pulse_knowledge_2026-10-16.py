#!/usr/bin/env python3
"""pulse_knowledge_2026-10-16.py — one-time: account roster, knowledge-concentration entries K001-K005,
W066 retired into them, P005 split by site (Panama: Wesco Warehouse; El Dorado: Dell -> P011). Idempotent.
Decisions: Darryl, 2026-10-16 session."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent) if Path(__file__).resolve().parent.name == "Tools" else "Tools")
import eos_registers as R, eos_pulse as P
T = "2026-10-16"; ST = f"{T} (Claude, session)"; DS = f"{T} (Darryl, session)"

ACCOUNTS = {"note": "Account roster for the Pulse health tiles (2026-10-16). Aliases match Pulse accounts and register titles. "
            "type: customer | internal | partner. A tile shows when the account has a Pulse issue or an item on Darryl's registers. Edit freely; confirm with Darryl.",
 "accounts": [
  {"name": "Dell", "type": "customer", "pinned": True, "aliases": ["Limerick", "El Dorado", "PC1"], "note": "Largest customer. El Dorado is a Dell site (Darryl, 2026-10-16)"},
  {"name": "Wesco Warehouse", "type": "internal", "aliases": ["Panama"], "note": "Internal program deploying entroCIM at Wesco; Panama is a Wesco site (Darryl, 2026-10-16)"},
  {"name": "Ford", "type": "customer", "aliases": ["UDAC", "Rouge"]},
  {"name": "Federal Reserve", "type": "customer", "aliases": ["FRB", "FRBNY", "SASTEC", "Federal Reserve Bank"]},
  {"name": "Coca-Cola (TCCC)", "type": "customer", "aliases": ["TCCC", "Coca-Cola", "AOC"]},
  {"name": "BAE", "type": "customer", "aliases": ["BAE Systems"]},
  {"name": "Stanford", "type": "customer", "aliases": []},
  {"name": "Louvre Abu Dhabi", "type": "customer", "aliases": ["Louvre"]},
  {"name": "UWM", "type": "customer", "aliases": []},
 ]}

SRC_W066 = "Carried from W066 (Knowledge concentration / engineering quality), retired into this area 2026-10-16."
KNOW = [
 dict(id="K001", title="entroCIM tenant behavior and access model", holder="Jason Ganiatsas", backup="", coverage="partial",
      exposure=["release"], track="development", product="entroCIM", first_seen="2026-10-15", last_seen="2026-10-15", sightings=1,
      mitigation="Michael Pieschel documenting in Confluence; Maggie Becker building enablement material", links=["P010", "W066"],
      body=["2026-10-15 (Daily Stand Up): Michael Pieschel, demonstrating the tenant redesign: \"Jason G is pretty knowledgeable about it. He would be a good resource to ask about this.\" Michael is documenting; Maggie Becker is ramping to build training material.",
            f"{ST}: Coverage set to partial: no backup named, but documentation and enablement are under way ahead of the tenant-redesign release (P010)."]),
 dict(id="K002", title="entroCIM release packaging, sprint coordination and platform engineering", holder="Ron Snyder",
      backup="David Blondel (stand-up, sprint planning), Chad Steger (release communication, escalation), Joseph Kusnir (frontend), during PTO",
      coverage="partial", exposure=["release", "customer"], track="development", product="entroCIM", absence_date="2026-10-14",
      first_seen="2026-07-22", last_seen="2026-10-14", sightings=6, mitigation="PTO coverage note issued 2026-10-13; no return date", links=["W066"],
      body=[f"{SRC_W066} Ron Snyder was named across six consecutive evidence cycles (2026-08-05 to 2026-08-19) as the key contributor on engineering execution, containerization, AI documentation, SkySpark rollout, Mapbox, Batch Point Writer design and release coordination; 2026-07-22 migration and SAML work also depended on him.",
            "2026-10-14 (PTO Awareness email; eCIM Leadership chat): on PTO; coordination handed to David Blondel, Chad Steger and Joseph Kusnir during an active pod rollout. No end date given.",
            f"{ST}: Coverage partial: coordination is covered for the PTO, platform knowledge is not. Flagged on the absence test: confirm his return date and who holds platform decisions meanwhile."]),
 dict(id="K003", title="Quest-to-Azure migration and SAML/authentication (PaaS-02)", holder="Babu Papanna", backup="", coverage="unknown",
      exposure=["migration"], track="delivery", product="entroCIM", first_seen="2026-07-22", last_seen="2026-07-22", sightings=1,
      mitigation="", links=["W066"],
      body=[f"{SRC_W066} 2026-07-22 (Quest Migration and SAML threads): migration and authentication work depended on a small number of platform staff, Babu Papanna and Ron Snyder; backup ownership on the migration/auth track was never confirmed.",
            f"{ST}: All entroCIM environments completed migration to Wesco Azure (Products/entroCIM, 2026-10-13), so the migration exposure has largely passed. Shows as not seen in 45+ days; confirm whether SAML/authentication knowledge is still concentrated."]),
 dict(id="K004", title="FRB load shed, Dell GMS energy points and KPIs, global metering due diligence", holder="Elias Brewer",
      backup="Keith Bishop (named by Chad Steger, 2026-08-06)", coverage="covered", exposure=["customer"], track="delivery", product="entroCIM",
      first_seen="2026-08-06", last_seen="2026-08-06", sightings=1, mitigation="", links=["W066"],
      body=[f"{SRC_W066} 2026-08-06 (Daily Scrum): Chad Steger described Elias Brewer as \"really swamped\" across FRB load shed, Dell GMS energy points and KPI mock-ups, and global metering due diligence, naming Keith Bishop as the only stated backup.",
            f"{ST}: Coverage covered: a backup is named. Load (Elias swamped) is visible in People, not here."]),
 dict(id="K005", title="Dell FTE Franklin/Apex/Hortolandia stability assessment and India deployment support", holder="Chethan GR",
      backup="", coverage="unknown", exposure=["customer"], track="delivery", product="entroCIM", absence_date="2026-10-08",
      first_seen="2026-09-14", last_seen="2026-09-14", sightings=1, mitigation="Departure extended to 2026-10-08 as a knowledge-transfer window", links=["B23"],
      body=["2026-09-14 (weekly evidence): Chethan GR's departure extended to 2026-10-08, adding about four weeks of overlap on the Dell FTE Franklin/Apex/Hortolandia communication-stability assessment (B23) and India-side deployment support under Chad Steger.",
            f"{ST}: The departure date has passed and no evidence confirms the handover. Flagged on the absence test: ask Chad who now holds the Dell FTE assessment."]),
]

def main():
    P.ACCOUNTS_FILE.write_text(json.dumps(ACCOUNTS, indent=1) + "\n", encoding="utf-8"); print("accounts:", len(ACCOUNTS["accounts"]))
    for d in KNOW:
        d = dict(d); body = "\n\n".join(d.pop("body"))
        if (P.PULSE_DIR / f"{d['id']}.md").exists():
            print("exists:", d["id"]); continue
        meta = {"kind": "pulse", "category": "knowledge", "status": "live", "escalation": "", "escalation_test": "", "escalated_to": "",
                "created": T, "last_touched": T, "needs_triage": False}
        meta.update(d); R.write_item(meta, body); print("knowledge:", d["id"])
    # W066 retired into the knowledge area
    f = R.find_item("W066")
    if f and f[0].get("tier") != "retired":
        meta, body, _ = f
        meta.update({"tier": "retired", "status": "closed", "closed_date": T, "closed_by": "Claude, Darryl's decision 2026-10-16",
                     "disposition_note": "Moved to the Pulse knowledge-concentration area (K001-K005). Reversible: set tier to active.", "last_touched": T})
        body = body.rstrip("\n") + f"\n\n{ST}: Retired into the Pulse's knowledge-concentration area (Darryl agreed 2026-10-16): K001 Jason Ganiatsas, K002 Ron Snyder, K003 Babu Papanna, K004 Elias Brewer (covered), K005 Chethan GR. Capacity instances (Scott Dunn, Joseph Kusnir) are load, not knowledge, and show in the People view.\n"
        R.write_item(meta, body); print("retired W066")
    # P005 split by site
    m5, b5, _ = R.find_item("P005")
    if "El Dorado" in m5.get("title", ""):
        m5["title"] = "Commissioned Panama devices not producing expected alarms ahead of environment decommissioning"
        m5["account"] = "Wesco Warehouse"; m5["last_touched"] = T
        b5 = b5.rstrip("\n") + f"\n\n{DS}: El Dorado is a Dell site; Panama is Wesco. Split: this issue is Panama (Wesco Warehouse); El Dorado is P011 (Dell).\n"
        R.write_item(m5, b5); print("P005 -> Panama")
    if not (P.PULSE_DIR / "P011.md").exists():
        m11 = {k: m5.get(k) for k in ("kind", "status", "forum", "product", "severity", "customer_visible", "owner", "people", "first_seen", "last_seen", "sightings", "next_action", "escalation", "escalation_test", "escalated_to", "needs_triage")}
        m11.update({"id": "P011", "account": "Dell", "title": "Commissioned El Dorado devices not producing expected alarms ahead of environment decommissioning",
                    "links": ["P005", "W024", "P004"], "created": T, "last_touched": T})
        b11 = ("2026-10-14 (Daily Scrum): Syed Zaidi, direct: the customer is not getting alarms from commissioned devices (El Dorado and Panama), and called visibility critical before an environment decommissioning expected within weeks. No RCA or remediation timeline in evidence. Escalation path Chad Steger.\n\n"
               f"{DS}: El Dorado is a Dell site. Split from P005 (Panama, Wesco Warehouse); same evidence, different accounts.")
        R.write_item(m11, b11); print("P011 created")
    m4, b4, _ = R.find_item("P004")
    if "Darryl, session" not in b4:
        b4 = b4.rstrip("\n") + f"\n\n{DS}: Confirmed Dell; El Dorado is a Dell site.\n"; m4["last_touched"] = T
        R.write_item(m4, b4); print("P004 noted")
    print(R.regenerate_all())

if __name__ == "__main__":
    main()
