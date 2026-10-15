# Phase 1 Review and Forward Plan
Date: 2026-07-23 | Purpose: step-back review — findings, what Phase 1 delivers, and the Phase 2 execution plan. Companion to `Consolidated_Shortlist.md` (the Checkpoint 1 decision record).

## 1. Findings: Shortlist, Scoring, Reasoning

**Decision (Checkpoint 1, made and amended 07-23):** one customer proposition — **Connected Device Assurance as a Service** — with modules deep-dived in Phase 2, funded once at a shared enablement layer built from entroCIM (connectors/PODs), Airwall, Azure/edge, WAM, and Navigator integration.

| Module | Weighted score | Disposition | Core reasoning |
|---|---|---|---|
| A — Firmware + Config Assurance | 3.75 | Phase 2 deep dive | Paid market proves the pain; best MVP feasibility and measurability; main uncertainty is right-to-win vs. incumbents — the partner option could flip it |
| B — Remote Health + Recovery | 3.65 | Phase 2 deep dive | Best pull-through (truck rolls → field service, parts, replacement); lowest liability; must prove remotely-resolvable incident volume for margin |
| C — Refresh/EOL Intelligence | 3.65 | Embedded, not sold | Strongest right-to-win (install-base + supplier position) but customers won't pay for what reads as sales enablement — ships inside every module as the commercial signal; carries the pull-through story |
| D — Cyber-Hygiene + Compliance | 3.40 | Phase 2 deep dive (Darryl amendment 07-23) | Most severe problem; table stakes in OT/IoT; split: *visibility* (candidate MVP base tier, low liability) vs. *remediation* (credential custody, sequenced later). Nozomi Arc as reference point |

Why A+B(+D) together rather than one wedge: ~80% shared enablement layer — one investment, multiple revenue-bearing modules, reusable across future services. Rejected by both analyses independently: standalone Airwall connectivity as a product; anything duplicating WAM, Navigator, or a monitoring platform.

## 2. What Phase 1 Delivers

A two-minute answer with a defensible process behind it:

> "I'm proposing a recurring managed service — Connected Device Assurance — where Wesco takes accountability for the firmware, configuration, health, and cyber posture of the connected devices we sell, starting with cameras and access control. It's built almost entirely from platforms we already own, it monetizes the installed base with subscription revenue, and its own operating data generates hardware refresh sales — a direct answer to both the software and pull-thru gaps. We evaluated the space systematically across two AI toolchains, scored alternatives against weighted funding criteria, and are now validating the top modules, including whether to partner rather than build for the device-management engine. I'll have a fundable thesis with a 90-day validation plan for the 2027 AOP by end of August."

Beyond the talk track: governing documents that stabilize the concept against drift (all changes by dated amendment); an auditable decision trail for AOP scrutiny; a named list of what must be proven before money is asked; two de-risking moves made — firmware rights reframed to a per-vendor hurdle, and build/partner/buy forced into every capability gap.

## 3. Phase 2 Execution Plan (Checkpoint 2 freeze target ~2026-08-14)

| Workstream | Owner | Target |
|---|---|---|
| ChatGPT Phase 2 run (A+B+D deep dives, amended Master Prompt) → save to `02_Phase_2_Dossiers/` | Darryl | ~07-28 |
| Cited research: competitive/partner scan (SecuriThings, Viakoo, Nozomi), pricing comparables, OEM API survey (Hanwha, Axis, Dormakaba, HID, Cisco) | Claude | Start on Darryl's go; complete ~08-05 |
| Internal evidence for Module B margin: remotely-resolvable incident volume, service history. Suggested sources (Darryl to confirm): entroCIM support data (Ron Snyder), ops (Senthil Govindaswamy), commercial (Nathan Kehr) | Darryl sponsors | Requests out ~07-30 |
| Merge + Concept Dossiers with architecture diagrams (Mermaid per standards) | Claude | ~08-08 to 08-12 |
| Checkpoint 2: concept freeze | Darryl | ~08-14 |

Calendar reality: freeze lands right after the 08-12 pilot review; Sean endorsement week of 08-17; AOP input due **08-31**. The Sean 1:1 booking is the critical-path item nobody controls late.

## 4. Open Decisions (as of 07-23)

1. **Phase 1 Wesco artifact: DONE 07-23** — `Connected_Device_Assurance_Phase_1_One_Pager.pptx` (this folder), single slide in the WAM diagram style: devices → enablement layer → three service modules + built-in commercial path → customer and Wesco value, with "Where we are" band. Outbound-scrubbed. Intended use: informal Sean heads-up before the endorsement meeting. Note: Wesco logo is a text placeholder; swap in the real logo mark from an existing deck before sharing.
2. **Research track start:** Claude ready to begin on go.
3. **Module B evidence sources:** owner names to confirm.
4. **Sean 1:1 (week of 08-17):** to be booked.
