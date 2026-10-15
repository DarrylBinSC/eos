# Connected Device Assurance (CDA)
As of: 2026-09-01. Created this date to close a routing gap: CDA has substantial evidence and decision history (see `03`, `05`, and this folder's phase files) but, unlike WAM, entroCIM, and Navigator, had no single durable knowledge file at the folder root. This file is that front door; phase files (`00_Charter` through `05_Operating_Record`) hold the working detail and are not duplicated here.

## Daily evidence, 2026-09-15 to 2026-09-16 (added 2026-09-16)

- **New commercialization angle opened: data-center market, possibly through the existing TSS virtual site-survey service (Durable).** Darryl raised this as a faster-moving route than the current path in the Digital Products / Agile Staff Meeting, 2026-09-15. Sean McCloskey set explicit conditions before it advances: a credible, sized market and a committed sales partner — not a capability argument alone. Darryl committed to following up with Bill Musco and Sridhar Loke on 2026-09-16. **This is a second, parallel validation track alongside the existing Converging Technologies/Bill Muczko pilot-account gate** (`05` C42/A37) — reconcile rather than run as two separate CDA strategies before either goes back to Sean or Chris Gazdic. See `03` Decision Backlog, 2026-09-16.
- **Key People addition:** Sridhar Loke and Bill Musco now active on the data-center/TSS thread specifically, distinct from Bill Muczko (Global Enterprise) already tracked above — do not conflate Bill Musco and Bill Muczko, two different people on two different CDA tracks.

## Weekly evidence, 2026-09-09 to 2026-09-14 (added 2026-09-14)

- **Commercial discovery with sales leadership continues** (CDA Product Review; Connected Device Assurance email thread). Durable in direction, but the package names no accounts, no owners beyond the standing ones, and no dates, so it does not move `05` C42 (pilot-account identification, Chris Mooney and Bill Muczko) off its undated gate. Treat as continuation, not progress against the pilot-account gate that governs the 2027 build decision.

## What It Is / Value Proposition

A Wesco-managed service for customer camera and connected-device fleets: firmware currency, device inventory completeness, and lifecycle assurance, sold bundled with other Wesco services or standalone. Cameras first (Hanwha and Axis connectors already live in production via entroCIM); direct integrations with new manufacturers estimated at 8–12 weeks each. First node supports 250+ cameras. Deployment model is hybrid: cloud plus an on-premises device (a physical appliance, "like a gateway" per Bill Muczko) at the customer site — CDA is not built on entroCIM but uses its underlying platform, tools, and expertise, and must not read as an entroCIM feature add-on (`03`, 2026-08-26).

## Current State

FY27 AOP submission complete and confirmed ("GTG, nothing needed," John Erickson, 2026-08-24/25). Value KPI block carries five customer-site outcome metrics on a quarterly cadence (device inventory completeness, firmware currency, advisory-to-remediation time, remote resolution rate, service evidence completeness), with FY27 readiness metrics (not service metrics) reported starting 2Q27 — the service does not exist in production before then and the investment is not yet approved for build.

**Weekly evidence, 2026-09-02 to 2026-09-09 (added 2026-09-09):** CDA explicitly positioned by Darryl Benson, in a Teams budget discussion with Chris Gazdic, as a **new camera-focused product**, with **ISC West named as a relevant commercial event**. No pilot accounts confirmed yet — the validation-gate question below is unchanged.

**As of the 2026-08-24 to 08-31 window, CDA moved from internal concept packaging into customer-validation planning.** Sales leadership (Chris Mooney, Bill Muczko) was engaged 2026-08-28 and asked to judge whether CDA is worth building and to help identify two or three pilot accounts before an estimated eight-month 2027 build is committed. This is the next evidence gate — see Open Decisions below.

## Commercial Position

**Strongest external validation to date, from Bill Muczko (Global Enterprise, ~200 Fortune 200 accounts):** "customers aren't managing their camera assets effectively today. I could say probably across 85% of our account base. If they're even monitoring it, they're using spreadsheets." His estimate, not a measured figure — treat as directional, not a stated statistic. Chris Mooney (Converging Technologies) separately validated the need, citing customer mixed-use-environment compliance and firmware-currency concerns, and recalled an expensive subscription alternative he thought was called Secure Things (SecuriThings, recollection uncertain) — a competitive signal worth confirming, not yet independently researched this cycle.

FY27 AOP figure: $246,787 (B18), collation template at `CDA/04_Phase_4_AOP/`.

## Key Dependencies

Sales-leadership engagement now open on two tracks: Suzanne Betterton's team (practitioner/integrator view, via Chris Mooney) and Bill Muczko's senior directors/GAMs — both working sessions to be set up by Darryl (`05` A37, due 2026-09-02, no reply yet as of 2026-08-28). Manufacturer rights and integration effort tracked per-vendor in `05_Operating_Record/Risk_and_Dependency_Log.md`. Airwall/JCI commercial terms and Wesco TSS professional-services capacity remain open dependency gates there (D2, D8).

## Managed Services Angle

Explicitly a managed service, not a product sale alone — the customer buys the service; the appliance and application are "back-of-house" (Darryl, answering Bill Muczko directly, 2026-08-28: entroCIM is not required for the customer relationship). Nathan Kehr's endorsement is pitched at Bill Muczko specifically: low barrier to entry, a lighter way to get behind the customer firewall and pull install-base asset data into Wesco systems, with the option to layer further services later.

## Benefits Realization

Planned, not yet realized — no production customers exist. The distinction matters given the WAM benefits-reporting history in this portfolio (`01`); do not describe CDA capability as live before a pilot lands.

## Key People

- **Darryl Benson** — Product Executive; resource manager for the investment.
- **Chris Mooney** — Converging Technologies sales, Alan Farrimond's org; new relationship (first met 2026-08-28); routed Darryl to Suzanne Betterton's team.
- **Bill Muczko** — Global Enterprise segment lead, ~200 Fortune 200 accounts; strongest external validation source; new relationship (first met 2026-08-28).
- **Suzanne Betterton** — leads Mooney's US team, integrator background; practitioner-view session pending (A37).
- **Cody Remington** — market validation and positioning research; spelling flag: also appears as "Cody Remmington" in the 07-29 SPARC white paper entry — treat as the same person.

## Major Risks and Open Decisions

Pointer to `03`/`04`/`05` for current status; do not duplicate register state here.

- **Whether CDA is worth the 2027 build, and which two or three pilot accounts validate it** — open, new this week (2026-08-24 to 08-31 window). Owners: Chris Mooney, Bill Muczko, Darryl. Blocking: customer interviews and named pilot candidates not yet secured. Risk of delay: build priority set without market evidence, or the 2027 window slips.
- **CDA investment confidence** — decreases if pilots are secured (a positive signal), currently unchanged; no pilot accounts named yet in evidence.
- See `05_Operating_Record/Risk_and_Dependency_Log.md` for dependency gates (D1–D8) and initiative-level risks (R1–R8), and `04_Phase_4_AOP/` for the FY27 submission package.

## History and Lessons

Full ideation and phase history retained in this folder: `00_Charter` (thesis, master prompt), `01_Phase_1_Divergence` through `04_Phase_4_AOP` (concept development, dossiers, funding case, AOP intake), `05_Operating_Record` (risk log, source index, research log). See `Products/README.md` for the folder structure rationale.
