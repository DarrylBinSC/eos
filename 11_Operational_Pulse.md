# Operational Pulse

<!-- GENERATED 2026-11-10 13:31 from Registers/ by Tools/eos_registers.py. Do not hand-edit this section; edit the item files under Registers/ or use the EOS web app. Pre-migration history is preserved verbatim in Archive/2026-10-15_pre_registers/. -->

> Rolling window 2026-10-27 to 2026-11-10. Issues from team-governed forums. The teams' own governance (project process, sprint cycle) owns the work; nothing here needs disposal. An issue with no sighting for 10 days (21 for a bi-weekly forum) is closed as presumed resolved by silence and reopens if raised again. A Medium or Low issue counts as live from its third sighting. Escalated issues move to the Watch List. Design: `CLAUDE.md`, Operational Pulse.

## Account health

| Account | 7-day trend | Change | Load now | Load a week ago | Live | Stuck | Quiet | At your level |
|---|---|---|---|---|---|---|---|---|
| Dell | Improving | -72 | 85 | 152 | 9 | 1 | 2 | 1 |
| Merck | Worsening | +8 | 8 | 0 | 1 | 0 | 0 | 0 |
| Federal Reserve | Steady | -1 | 18 | 9 | 1 | 0 | 0 | 2 |
| Wesco Warehouse | Steady | -2 | 12 | 14 | 1 | 1 | 0 | 0 |
| Ford | Steady | -1 | 10 | 1 | 0 | 0 | 0 | 2 |
| Marygrove | Steady | +0 | 8 | 8 | 1 | 0 | 0 | 0 |
| Louvre Abu Dhabi | Steady | +0 | 5 | 0 | 0 | 0 | 0 | 1 |
| Coca-Cola (TCCC) | Steady | -2 | 0 | 2 | 0 | 0 | 0 | 0 |
| Cree Church / Premier | Steady | +0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Intel | Steady | -2 | 0 | 2 | 0 | 0 | 0 | 0 |
| Microsoft | Steady | -2 | 0 | 2 | 0 | 0 | 0 | 0 |
| Waymo | Steady | -1 | 0 | 1 | 0 | 0 | 0 | 0 |

Load = live high visible x8, live high x6, live medium x3, live low x1, stuck x4, quiet x1, candidate x3, at your level x5. Trend = change in the team-raised load over 7 days, rebuilt from the dates meetings raised each issue; Worsening or Improving when it moves by at least 5 points and 15% of last week's load, otherwise Steady. Your register items are in the load but not the trend (no dated history). Friction from evidence, not customer sentiment.

No signals in the window: BAE, Stanford, UWM.

## Needs your call

- **P066** Argentina: watchdog connectors flapping connected/disconnected within a minute, source unidentified (no account; 2026 Deployment Daily Scrum). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P135** Dell HQ display/alarm issue: new alarms not showing, blocking a Penang production rollout (Dell; 2026 Deployment Daily Scrum). Test: No owner, or the customer is unaware of a material problem.
- **P137** Prior Gridboard monorepo migration lost code and broke functionality; migration restarted (no account; entroCIM Daily Stand Up). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P142** Dell questioning redundancy/DR architecture and reuse of existing licenses for DR (Dell; 2026 Deployment Daily Scrum). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P145** Dell IT proposing to remove redundant license servers; no confirmed internal rationale for the current design (Dell; 2026 Deployment Daily Scrum). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P159** WAM Exact-supplier renewal notifications are not being sent; blocked on a custom-field enablement (no account; WAM Product Backlog Refinement). Test: No owner, or the customer is unaware of a material problem.
- **P162** Hanwa devices 121/123 and Bangalore access devices inaccessible ahead of a demo the following week (no account; entroCIM Daily Stand Up). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P143** Alarm database/Alarm Manager correctly triggers, but customer email notifications are blocked by an SMTP issue (no account; 2026 Deployment Daily Scrum). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P146** Cross-site alarm audit has no agreed validation baseline; prior environment decommissioned (no account; 2026 Deployment Daily Scrum). Test: No owner, or the customer is unaware of a material problem.
- **P147** Customer-requested battery-replacement alarms are not an existing entroCIM function (no account; 2026 Deployment Daily Scrum). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P148** North America PME/OPC UA integration has no pilot; first live test planned on Central Texas (Dell; 2026 Deployment Daily Scrum). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P149** Quest/Nextcloud retirement requires moving file and software-pull dependencies to SharePoint before shutdown (no account; entroCIM Daily Stand Up). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P154** Asset/license table reuse risks license workflows pulling in asset data without filtering (no account; WAM Product Backlog Refinement). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.

## Knowledge concentration

Where one person holds knowledge a customer, a release or a migration depends on. Silence does not remove the risk: entries stay live for 45 days after the last evidence.

| ID | Knowledge area | Held by | Backup | Coverage | Exposure | Mitigation | Last evidence |
|---|---|---|---|---|---|---|---|
| K010 | Dell Penang One BMS access and credentials | Scott Dunn | none named | none | customer | Syed Jamshed Zaidi to follow up with IT for credentials; Matthew Heid asked for a wider access conversation ("more people access and not just Scott") | 2026-10-29 |
| K008 | FRB-restricted file-transfer workflow (BLOB storage moves requiring Federal Reserve handling) | Adam Slingerland | none named | none | customer |  | 2026-10-27 |
| K009 | WAM ADM renewal-recommendation code: original author departed, no documented backup, team in maintenance mode |  | none named | none | release | Rework the recommendation feature from scratch (see P068); no interim owner for the existing code. | 2026-11-02 |
| K007 | Americas/LATAM watchdog, temperature-sensor and power-failure alarm audit; point-level alarm configuration | Elias Brewer | Keith Bishop | partial | customer | Keith Bishop named as the next technical adviser if Elias cannot assist; Keith also sole holder of the Limerick RCA (K006), so the backup is itself concentrated | 2026-11-05 |
| K006 | Dell Limerick alarm-handler RCA and release/build context for affected pod updates | Keith Bishop | none named | partial | customer, release | Ron Snyder mentioned as someone to ask; not named as backup (and away this week and next) | 2026-10-29 |

Not seen in 45+ days (confirm whether still true): K004 FRB load shed, Dell GMS energy points and KPIs, global metering due diligence (Elias Brewer).

## People carrying the most

| Person | Owns (Pulse) | Involved (Pulse) | Delegated/awaited | Sole holder | Forums |
|---|---|---|---|---|---|
| Chad Steger | 2 | 10 | 4 | 0 | 2026 Deployment Daily Scrum, entroCIM Backlog Deep Dive, entroCIM Daily Stand Up, Quest Migration Weekly Check-In |
| Shawn Clark | 3 | 3 | 2 | 0 | entroCIM Daily Stand Up, Quest Migration Weekly Check-In |
| Akansh Gangil | 0 | 6 | 5 | 0 | ADM connect with Natalie, WAM Product Backlog Refinement, WAM Sprint Review |
| Amy Aguirre | 0 | 0 | 4 | 0 |  |
| Ron Snyder | 1 | 2 | 2 | 0 | entroCIM Daily Stand Up |
| Natalie Marquardt | 0 | 1 | 3 | 0 | ADM connect with Natalie |
| Nathan Kehr | 0 | 0 | 3 | 0 |  |
| Sean McCloskey | 0 | 0 | 3 | 0 |  |
| Syed Jamshed Zaidi | 2 | 9 | 0 | 0 | 2026 Deployment Daily Scrum |
| Matthew Heid | 2 | 5 | 0 | 0 | 2026 Deployment Daily Scrum |
| Scott Dunn | 1 | 5 | 1 | 1 | 2026 Deployment Daily Scrum |
| Babu Papanna | 1 | 2 | 1 | 0 | entroCIM Daily Stand Up, Quest Migration Weekly Check-In |

Owns: named owner of a live Pulse issue. Involved: named in the evidence with a statement, commitment or stated role, not the owner. Delegated/awaited: open register items they own. Sole holder: knowledge areas they hold without a confirmed backup.

## 2026 Deployment Daily Scrum

Governance: Project management. Owner: Chad Steger. Live 15, new this week 8, stuck 3, quiet 2. Last sighting: 2026-11-05. Last evidence: 2026-11-10.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P015 | Panama HVAC points increase continuously; BACnet setup failed, Modbus option untested | Wesco Warehouse | Matthew Heid; Scott Dunn | High | 2026-10-13 | 2026-11-04 | 4 | stuck, customer-visible |
| P066 | Argentina: watchdog connectors flapping connected/disconnected within a minute, source unidentified |  | Matthew Heid | High | 2026-10-22 | 2026-11-05 | 2 | stuck, customer-visible, candidate: boundary |
| P004 | Dell visualization scope unsettled: point pages only, or basic graphics and floor plans (El Dorado) | Dell |  | Medium | 2026-10-15 | 2026-11-05 | 3 | stuck, customer-visible |
| P107 | Limerick failure-condition alarm validation method undefined before telling Dell the release is approved | Dell |  | High | 2026-10-28 | 2026-11-03 | 3 | customer-visible |
| P108 | El Dorado end-to-end alarm validation needs customer/site participation; approach not yet defined | Dell | Syed Jamshed Zaidi | High | 2026-10-28 | 2026-11-05 | 2 | customer-visible |
| P116 | Palo Alto NetBot found outside the earlier non-DC scope: new integration needed, device credentials unconfirmed | Dell |  | High | 2026-10-29 | 2026-11-05 | 2 | customer-visible |
| P131 | Merck entroCIM license maintenance substantially overdue; remote access may have lapsed | Merck |  | High | 2026-11-04 | 2026-11-05 | 2 | customer-visible |
| P135 | Dell HQ display/alarm issue: new alarms not showing, blocking a Penang production rollout | Dell |  | High | 2026-11-03 | 2026-11-05 | 2 | customer-visible, candidate: gap |
| P142 | Dell questioning redundancy/DR architecture and reuse of existing licenses for DR | Dell | Syed Jamshed Zaidi | High | 2026-11-04 | 2026-11-05 | 1 | customer-visible, candidate: boundary |
| P145 | Dell IT proposing to remove redundant license servers; no confirmed internal rationale for the current design | Dell |  | High | 2026-11-04 | 2026-11-05 | 1 | customer-visible, candidate: boundary |
| P087 | entroCIM refresh hanging for some time while Babu C. Dinesh was away |  |  | Medium | 2026-10-27 | 2026-11-03 | 3 |  |
| P143 | Alarm database/Alarm Manager correctly triggers, but customer email notifications are blocked by an SMTP issue |  |  | Medium | 2026-11-04 | 2026-11-04 | 1 | customer-visible, candidate: boundary |
| P146 | Cross-site alarm audit has no agreed validation baseline; prior environment decommissioned |  |  | Medium | 2026-11-05 | 2026-11-05 | 1 | customer-visible, candidate: gap |
| P147 | Customer-requested battery-replacement alarms are not an existing entroCIM function |  |  | Medium | 2026-11-05 | 2026-11-05 | 1 | customer-visible, candidate: boundary |
| P148 | North America PME/OPC UA integration has no pilot; first live test planned on Central Texas | Dell |  | Medium | 2026-11-05 | 2026-11-05 | 1 | customer-visible, candidate: boundary |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P007 PC1/JCI large-scale point faults and intermittent site access; P012 Dell FTE Franklin tracker: categorize items for Scott Dunn review.

## entroCIM Daily Stand Up

Governance: Sprint (2-week). Owner: Ron Snyder. Live 5, new this week 2, stuck 1, quiet 1. Last sighting: 2026-11-10. Last evidence: 2026-11-10.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P018 | Test server has no VPN connectivity to the private artifact repository (containerization) |  | Babu Papanna | Medium | 2026-10-14 | 2026-11-04 | 5 | stuck |
| P111 | FRB alarm failures lack sufficient logging/data to diagnose why alarms fail to show up | Federal Reserve | Keith Bishop | High | 2026-10-28 | 2026-11-04 | 2 | customer-visible |
| P137 | Prior Gridboard monorepo migration lost code and broke functionality; migration restarted |  | Nisha More | High | 2026-11-03 | 2026-11-04 | 2 | candidate: boundary |
| P162 | Hanwa devices 121/123 and Bangalore access devices inaccessible ahead of a demo the following week |  | Ron Snyder | High | 2026-11-10 | 2026-11-10 | 1 | customer-visible, candidate: boundary |
| P149 | Quest/Nextcloud retirement requires moving file and software-pull dependencies to SharePoint before shutdown |  |  | Medium | 2026-10-29 | 2026-10-29 | 1 | candidate: boundary |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P042 entroCIM 3.1.12.14 customer release notice one day behind the stated date (Chad out sick 10-19).

## entroCIM Backlog Deep Dive

Governance: Sprint / backlog. Owner: David Blondel. Live 2, new this week 0, stuck 0, quiet 0. Last sighting: 2026-11-03. Last evidence: 2026-11-03.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P043 | Schneider OPC UA protocol decision and proof of concept pending; constrains further Dell GMS completion | Dell |  | High | 2026-10-20 | 2026-10-20 | 1 | customer-visible |
| P046 | Marygrove: three open tickets; JACE down and customer IT cannot be reached | Marygrove |  | High | 2026-10-20 | 2026-10-20 | 1 | customer-visible |

## Quest Migration Weekly Check-In

Governance: Project management. Owner: Chad Steger. Live 5, new this week 0, stuck 5, quiet 0. Last sighting: 2026-11-03. Last evidence: 2026-11-03.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P047 | Azure BLOB Storage accessible via browser but not through the required Linux command-line transfer path |  | Shawn Clark | High | 2026-10-20 | 2026-11-03 | 4 | stuck |
| P048 | MQTT cutover blocked pending DNS records and ports 1883/8883 |  | Chad Steger | High | 2026-10-20 | 2026-11-03 | 4 | stuck, customer-visible |
| P049 | Azure conductor still set up for high availability; primary-role turnover not yet switched |  | Shawn Clark | High | 2026-10-20 | 2026-11-03 | 3 | stuck |
| P050 | Libro may fail through the new conductor pending an outbound-IP or relay configuration change |  | Shawn Clark | High | 2026-10-20 | 2026-11-03 | 4 | stuck, customer-visible |
| P052 | Workbench/BACnet Pro has no confirmed shared remote-access model after LogMeIn retirement |  | Chad Steger | Medium | 2026-10-20 | 2026-11-03 | 3 | stuck |

## WAM Product Backlog Refinement

Governance: Sprint. Owner: Sakshi Mathur. Live 3, new this week 0, stuck 0, quiet 0. Last sighting: 2026-11-04. Last evidence: 2026-11-04.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P159 | WAM Exact-supplier renewal notifications are not being sent; blocked on a custom-field enablement |  |  | High | 2026-11-02 | 2026-11-02 | 1 | customer-visible, candidate: gap |
| P154 | Asset/license table reuse risks license workflows pulling in asset data without filtering |  |  | Medium | 2026-11-02 | 2026-11-02 | 1 | candidate: boundary |
| P068 | WAM renewal recommendation feature: quality rejected, rework from start |  |  | Medium | 2026-10-23 | 2026-11-04 | 3 |  |

## WAM Sprint Review

Governance: Sprint. Owner: Sakshi Mathur. Live 3, new this week 0, stuck 2, quiet 0. Last sighting: 2026-11-02. Last evidence: 2026-11-02.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P021 | EUDM truncates manufacturer part numbers over 15 characters, causing ADM data loss |  |  | High | 2026-10-13 | 2026-10-27 | 3 | stuck, customer-visible, escalated to W016 |
| P022 | Missing EUDM shipping dates and country-code mapping block WAM data-enrichment completion |  |  | High | 2026-10-13 | 2026-10-27 | 3 | stuck, customer-visible |
| P094 | WAM critical security vulnerabilities remain open past the team's intended close date |  |  | High | 2026-10-27 | 2026-11-02 | 2 |  |

## WAM Product discussion

Governance: Product execution. Owner: Akansh Gangil. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: 2026-10-22. Last evidence: 2026-10-22 (none in the window).

No issues in the Pulse yet.

## ADM connect with Natalie

Governance: Product execution. Owner: Akansh Gangil. Live 1, new this week 0, stuck 0, quiet 0. Last sighting: 2026-11-04. Last evidence: 2026-11-04.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P114 | Exact renewals cannot reliably identify end users from current data; no path to obtain it except possibly integrators |  |  | High | 2026-10-28 | 2026-11-02 | 2 | customer-visible |

## Product Team / Platform Team connect

Governance: Team practice. Owner: Keyur Patel. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: 2026-10-30.

No issues in the Pulse yet.
