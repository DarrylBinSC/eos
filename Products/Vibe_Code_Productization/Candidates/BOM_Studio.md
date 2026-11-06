# BOM Studio (Launch Studio candidate)

Candidate file. Launch Studio's front door is `../Vibe_Code_Productization.md`; this file holds what is known about one candidate. Not a product of Darryl's and not on the Products roster; it appears on the Launch Studio card through the dated section there.

**As of:** 2026-10-30. First filed from Darryl (direct), three screenshots and a full design export supplied by Robert Ehiemua.

## What it is (evidenced)

BOM Studio is a working web application, version 12.3, "Design" workspace, built by Robert Ehiemua (Senior Director, Technology Support Services). It generates AI data center reference designs: 3D hall and floor plan, power and cooling, schedules, a commercial view with budget allowances and lead times, and a complete bill of materials, from a configured platform selection.

Reference design on file, "AI Infrastructure Reference / RD-001", GB300, 1 scalable unit, 576 GPUs across 8 compute systems, 17 cabinets in 2 rows, 2 CDUs, 5 CRAHs, direct liquid with residual air, 1.122 MW connected IT (1.71 MW essential), 2,332 data connections, 125 model checks passing.

Commercial view: 132 purchase lines (Vertiv, Schneider Electric, NVIDIA among the vendors) with unit cost, extended cost and lead time in weeks; every line tagged "ROM allowance / budget assumption." Footer on the tool: generated equipment and installation scope; land, building shell, utility reinforcement, software subscriptions, financing and operations staffing excluded; services and contingencies are editable allowances, not contractor bids.

Export: the design exports to a 47-tab workbook (`Evidence/BOM_Studio_GB300_S01_Reference_Design_2026-10-29.xlsx`) and to GLB for the 3D model.

## What the export contains (so nobody has to reopen 47 tabs)

- Design: overview, design basis, cabinet layout, rack elevations front and rear, facility equipment with coordinates and clearances, device schedule.
- BOM: Equipment BOM (136 lines: manufacturer, model, SKU, identity type, installed and factory-included quantities, spare percent, total order quantity, specification, source URL), selected parts, installation materials, pathway materials.
- Connectivity: NVLink (about 10,000 rows), compute to leaf, leaf to spine, Ethernet uplinks, storage, management, local OOB and OOB uplinks, port inventory, optic placement, optical channel checks.
- Cabling: cable routes, assemblies, length totals, labels, connection checklist.
- Power: power connections, PDU outlet map, power capacity per PDU bank with normal and failover kW, current, limit and margin (PASS/FAIL), electrical feeders, earthing bonds.
- Cooling and facility: cooling calculations, liquid piping, control wiring, control panel channels, pathway installation.
- Operations handoff: **BMS Point Map** (460 rows: BACnet object type and instance, units, alarm limits, delay and sample intervals, fail action, per sensor), IP address plan, management server build, storage drive map, storage and adapter build, installation tests.
- Verification: design reconciliation (129 checks, PASS/FAIL with detail), technical sources (a "checked on" date and source URL per catalog identity; sampled rows dated 2026-09-10).

## Why it matters to Darryl's portfolio

- **First concrete Launch Studio candidate.** The product file had none before this. It is a strong first case: a working, deep application with a clear business owner, and a plain IT-absorption argument (it runs over HTTP on a bare public IP, port 8501, "Saved locally," and holds pricing data).
- **The operations handoff is already in the design.** The BMS Point Map is the data entroCIM would ingest; the Equipment BOM with SKUs and source URLs is close to what WAM / ADM would seed an asset register from. Layering managed services on top is less a bolt-on than it looks.
- **Two threads, kept apart.** (1) Productize the tool: a Launch Studio question (gate, sponsor, funding, run ownership). (2) Package the design-and-build with managed services (entroCIM for operations, WAM / ADM for assets, Navigator / Ascent): an offer and portfolio question with Sales in it. Decision `D099`.

## People

- **Robert Ehiemua**, Senior Director, Technology Support Services; builder of BOM Studio. Reports to Vinay Prabhu (org chart, 2026-10-29).
- **Vinay Prabhu**, VP Solutions and Services, Rahi US Fremont; reports to Matt Powers (org chart). Inference, not stated: this sits in the Rahi data-center side of TS.
- **Matt Powers**, VP Technology Services; the executive above it, already Darryl's CDA contact in TS and the sponsor of TSS BOM Revision Control.
- **Brad Stevens and Nate Kehr**: in the 2026-10-29 discussion with Darryl about layering managed services onto it (Darryl, direct). No commitment from either is in evidence.

## Not known

- How Robert built it (tooling, hosting, who else worked on it) and whether it is in use on real projects or quotes.
- Whether TS leadership (Vinay Prabhu, Matt Powers) knows of or sponsors it.
- What Robert has asked for, if anything.
- Whether the managed-services bundle has a customer or opportunity behind it.
- Pricing basis for the ROM allowances and who maintains the catalog identities.

## Fit against the Launch Studio inlet filter (Claude's first read, for Darryl to correct)

- Business value: high if TS quotes AI data center builds from it; unknown until usage is known.
- Prototype viability: high; the reconciliation and sources tabs show engineering discipline unusual for a prototype.
- Security exposure: material today (public IP, HTTP, pricing data). This is the argument for IT absorption, not against the candidate.
- Support load after launch: significant; catalog identities and reference designs need maintaining as platforms change (GB300 today).
- Sponsor: not yet identified. Under the Launch Studio rule (no sponsor, no production) this is the first thing to establish.

## 2026-10-30: Darryl's own description of the tool to the Launch Studio group, and a conversation set for today

BOM Studio runs on Robert Ehiemua's own desktop machine today, which makes scaling and IT absorption the first practical question, and Darryl has set a Launch Studio conversation on it for 2026-10-30. Source: Launch Studio Teams chat, 2026-10-29; `Evidence/M365_Evidence_Daily_2026-10-30.md`.

- Darryl: "A tool called BOM Studio has been developed to build and price data centers across the entire BOM. We're adding managed services (entroCIM, WAM etc.) to it."
- Darryl: "A guy named Robert Ehiemua built this in Matt Powers' organization."
- Darryl: "Right now it's running on his gaming rig on the desk behind him, so to scale this one, we'll need to get going." (Confirms the hosting picture inferred from the public-IP, port-8501 footer above; the machine is his own, not a server.)
- Darryl: "Lets talk about this one tomorrow." (2026-10-30.)
- Michael Wassil: "If you want me to discuss the launch studio, I'd be glad to do so." Darryl: "Go ahead and mention it to him; I already have." Who "him" is was not named in the extract; do not assume.
- The 2026-10-29 calendar entry "AI Bom Studio / ALM / Safety / Entrocim" was not transcribed, so the Brad Stevens and Nate Kehr discussion is on Darryl's word only (above).

## Sources

- `Evidence/BOM_Studio_Screenshots_Robert_Ehiemua_2026-10-29_1.pdf`, `_2.pdf`, `_3.pdf` (Robert Ehiemua; 3D hall, floor plan, commercial view)
- `Evidence/BOM_Studio_GB300_S01_Reference_Design_2026-10-29.xlsx` (full design export)
- Darryl, direct, 2026-10-29 (builder, organization, the managed-services discussion with Brad Stevens and Nate Kehr)
- Org chart screenshot, 2026-10-29 (Ehiemua, Prabhu, Powers, O'Brien, Naylor, Engel)
- Launch Studio Teams chat, 2026-10-29 (`Evidence/M365_Evidence_Daily_2026-10-30.md`)
