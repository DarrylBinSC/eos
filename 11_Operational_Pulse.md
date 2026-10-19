# Operational Pulse

<!-- GENERATED 2026-10-19 16:31 from Registers/ by Tools/eos_registers.py. Do not hand-edit this section; edit the item files under Registers/ or use the EOS web app. Pre-migration history is preserved verbatim in Archive/2026-10-15_pre_registers/. -->

> Rolling window 2026-10-05 to 2026-10-19. Issues from team-governed forums. The teams' own governance (project process, sprint cycle) owns the work; nothing here needs disposal. Issues go quiet after 14 days without a sighting. Escalated issues move to the Watch List. Design: `CLAUDE.md`, Operational Pulse.

## Account health

| Account | Score | Band | 7-day change | Live | Stuck | Quiet | At your level |
|---|---|---|---|---|---|---|---|
| Dell | 19 | At risk | no prior week | 9 | 2 | 2 | 1 |
| Federal Reserve | 75 | Strained | no prior week | 0 | 0 | 0 | 5 |
| Wesco Warehouse | 84 | Healthy | no prior week | 2 | 0 | 0 | 0 |
| Ford | 85 | Healthy | no prior week | 0 | 0 | 0 | 3 |
| Coca-Cola (TCCC) | 94 | Healthy | no prior week | 0 | 0 | 1 | 1 |
| Louvre Abu Dhabi | 95 | Healthy | no prior week | 0 | 0 | 0 | 1 |
| Stanford | 95 | Healthy | no prior week | 0 | 0 | 0 | 1 |

Score = 100 minus: live high visible x8, live high x6, live medium x3, live low x1, stuck x4, quiet x1, candidate x3, at your level x5. Bands: 80+ healthy, 60 to 79 strained, below 60 at risk. Friction index from evidence, not customer sentiment.

No signals in the window: BAE, UWM.

## Needs your call

- **P007** PC1/JCI large-scale point faults and intermittent site access (Dell; 2026 Deployment Daily Scrum). Test: Still being raised 10+ business days after it was first raised.
- **P014** Dell non-DC server unavailable since the prior week, blocking meter verification (Dell; 2026 Deployment Daily Scrum). Test: No owner, or the customer is unaware of a material problem.
- **P020** WAM historical upload mishandles one customer ID with different names; duplicate ETL error records (no account; WAM Product Backlog Refinement). Test: No owner, or the customer is unaware of a material problem.
- **P022** Missing EUDM shipping dates and country-code mapping block WAM data-enrichment completion (no account; WAM Sprint Review). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P016** Trane Tracer BMS integration (Dell non-DC) may be outside the original scope and need separate estimation (Dell; 2026 Deployment Daily Scrum). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.

## Knowledge concentration

Where one person holds knowledge a customer, a release or a migration depends on. Silence does not remove the risk: entries stay live for 45 days after the last evidence.

| ID | Knowledge area | Held by | Backup | Coverage | Exposure | Mitigation | Last evidence |
|---|---|---|---|---|---|---|---|
| K005 | Dell FTE Franklin/Apex/Hortolandia stability assessment and India deployment support | Chethan GR | none named | unknown | customer | Departure extended to 2026-10-08 as a knowledge-transfer window | 2026-09-14 |
| K001 | entroCIM tenant behavior and access model | Jason Ganiatsas | none named | partial | release | Michael Pieschel documenting in Confluence; Maggie Becker building enablement material | 2026-10-15 |

Not seen in 45+ days (confirm whether still true): K004 FRB load shed, Dell GMS energy points and KPIs, global metering due diligence (Elias Brewer).

## People carrying the most

| Person | Owns (Pulse) | Involved (Pulse) | Delegated/awaited | Sole holder | Forums |
|---|---|---|---|---|---|
| Akansh Gangil | 0 | 4 | 13 | 0 | WAM Product Backlog Refinement, WAM Sprint Review |
| Chad Steger | 0 | 2 | 6 | 0 | 2026 Deployment Daily Scrum |
| Syed Jamshed Zaidi | 4 | 1 | 1 | 0 | 2026 Deployment Daily Scrum |
| Babu Papanna | 1 | 0 | 4 | 0 | entroCIM Daily Stand Up |
| Natalie Marquardt | 0 | 0 | 5 | 0 |  |
| Scott Dunn | 2 | 4 | 2 | 0 | 2026 Deployment Daily Scrum |
| Ron Snyder | 1 | 0 | 3 | 0 | 2026 Deployment Daily Scrum |
| Nathan Kehr | 0 | 0 | 4 | 0 |  |
| Adam Lazare | 0 | 0 | 3 | 0 |  |
| Amy Aguirre | 0 | 0 | 3 | 0 |  |
| Ankit Chadha | 0 | 0 | 3 | 0 |  |
| Sean McCloskey | 0 | 0 | 3 | 0 |  |

Owns: named owner of a live Pulse issue. Involved: named in the evidence with a statement, commitment or stated role, not the owner. Delegated/awaited: open register items they own. Sole holder: knowledge areas they hold without a confirmed backup.

## 2026 Deployment Daily Scrum

Governance: Project management. Owner: Chad Steger. Live 12, new this week 10, stuck 2, quiet 3. Last sighting: 2026-10-15. Last evidence: 2026-10-16.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P006 | Dell alarm-database corruption: intermittent alarming failures, no root cause | Dell | Ron Snyder; Keith Bishop | High | 2026-08-25 | 2026-10-14 | 5 | stuck, customer-visible, escalated to W009 |
| P007 | PC1/JCI large-scale point faults and intermittent site access | Dell | Scott Dunn | High | 2026-09-15 | 2026-10-15 | 3 | stuck, customer-visible, candidate: stuck |
| P014 | Dell non-DC server unavailable since the prior week, blocking meter verification | Dell |  | High | 2026-10-13 | 2026-10-13 | 1 | customer-visible, candidate: gap |
| P015 | Panama HVAC points increase continuously; BACnet setup failed, Modbus option untested | Wesco Warehouse | Matthew Heid; Scott Dunn | High | 2026-10-13 | 2026-10-13 | 1 | customer-visible |
| P005 | Commissioned Panama devices not producing expected alarms ahead of environment decommissioning | Wesco Warehouse | Syed Jamshed Zaidi | High | 2026-10-14 | 2026-10-14 | 1 | customer-visible |
| P011 | Commissioned El Dorado devices not producing expected alarms ahead of environment decommissioning | Dell | Syed Jamshed Zaidi | High | 2026-10-14 | 2026-10-14 | 1 | customer-visible |
| P017 | North America lighting-site UPS alarms visible in PME/NMC but not reaching entroCIM |  | Leanne | High | 2026-10-14 | 2026-10-14 | 1 | customer-visible |
| P001 | PC1 Grid Board site-selection defect blocking the KWH report and dashboard | Dell |  | High | 2026-10-13 | 2026-10-15 | 2 | customer-visible |
| P002 | Dell meter-data integrity: negative values, missing main meters, unreliable PPS3B data, demand/utilization mismatches | Dell | Syed Jamshed Zaidi | High | 2026-10-13 | 2026-10-15 | 3 | customer-visible |
| P016 | Trane Tracer BMS integration (Dell non-DC) may be outside the original scope and need separate estimation | Dell | Matthew Heid | Medium | 2026-10-13 | 2026-10-13 | 1 | customer-visible, candidate: boundary |
| P003 | Dell IT access and investigation dependencies: Malaysia login failure, refresh-page issue, Panek BMS validation | Dell | Syed Jamshed Zaidi | Medium | 2026-10-15 | 2026-10-15 | 1 |  |
| P004 | Dell visualization scope unsettled: point pages only, or basic graphics and floor plans (El Dorado) | Dell |  | Medium | 2026-10-15 | 2026-10-15 | 1 | customer-visible |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P008 Dell cluster session loss: fleet-wide configuration review still open; P009 TCCC/AOC Modbus gateway sourcing may delay gas-sensor integration; P012 Dell FTE Franklin tracker: categorize items for Scott Dunn review.

## entroCIM Daily Stand Up

Governance: Sprint (2-week). Owner: Ron Snyder. Live 2, new this week 2, stuck 0, quiet 0. Last sighting: 2026-10-15. Last evidence: 2026-10-16.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P018 | Test server has no VPN connectivity to the private artifact repository (containerization) |  | Babu Papanna | Medium | 2026-10-14 | 2026-10-14 | 1 |  |
| P010 | entroCIM tenant redesign and boot-mode routing: no acceptance criteria, rollout sequence or release date yet |  | Michael Pieschel | Medium | 2026-10-14 | 2026-10-15 | 2 |  |

## entroCIM Backlog Deep Dive

Governance: Sprint / backlog. Owner: David Blondel. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: 2026-09-14 (none in the window).

No issues in the Pulse yet.

## DCOE & entroCIM Weekly

Governance: Release governance (DCOE). Owner: Balachandar Murali. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: 2026-10-05.

No issues in the Pulse yet.

## Quest Migration Weekly Check-In

Governance: Project management. Owner: Chad Steger. Live 0, new this week 0, stuck 0, quiet 1. Last sighting: 2026-09-16. Last evidence: 2026-09-16 (none in the window).

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P013 Quest exit inventory: what must be retained and transferred to Wesco.

## Showcase recurring

Governance: Project management. Owner: David Blondel. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: none received (none in the window).

No issues in the Pulse yet.

## Deployment Team Knowledge Share

Governance: Team practice. Owner: TBC. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: none received (none in the window).

No issues in the Pulse yet.

## WAM Product Backlog Refinement

Governance: Sprint. Owner: Sakshi Mathur. Live 2, new this week 2, stuck 0, quiet 0. Last sighting: 2026-10-13. Last evidence: 2026-10-13.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P019 | WAM production: cancelled orders appear in export; expiry-chip criteria need validation |  | Bhupathi | High | 2026-10-13 | 2026-10-13 | 1 | customer-visible |
| P020 | WAM historical upload mishandles one customer ID with different names; duplicate ETL error records |  |  | High | 2026-10-13 | 2026-10-13 | 1 | customer-visible, candidate: gap |

## WAM Sprint Review

Governance: Sprint. Owner: Sakshi Mathur. Live 2, new this week 2, stuck 0, quiet 0. Last sighting: 2026-10-13. Last evidence: 2026-10-13.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P021 | EUDM truncates manufacturer part numbers over 15 characters, causing ADM data loss |  |  | High | 2026-10-13 | 2026-10-13 | 1 | customer-visible, escalated to W016 |
| P022 | Missing EUDM shipping dates and country-code mapping block WAM data-enrichment completion |  |  | High | 2026-10-13 | 2026-10-13 | 1 | customer-visible, candidate: boundary |

## WAM India Dev Team weekly

Governance: Sprint. Owner: TBC. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: none received (none in the window).

No issues in the Pulse yet.

## WAM Product discussion

Governance: Product execution. Owner: Akansh Gangil. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: 2026-09-09 (none in the window).

No issues in the Pulse yet.

## ADM connect with Natalie

Governance: Product execution. Owner: Akansh Gangil. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: 2026-09-09 (none in the window).

No issues in the Pulse yet.

## Product Team / Platform Team connect

Governance: Team practice. Owner: Keyur Patel. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: none received (none in the window).

No issues in the Pulse yet.
