# Operational Pulse

<!-- GENERATED 2026-10-29 09:39 from Registers/ by Tools/eos_registers.py. Do not hand-edit this section; edit the item files under Registers/ or use the EOS web app. Pre-migration history is preserved verbatim in Archive/2026-10-15_pre_registers/. -->

> Rolling window 2026-10-15 to 2026-10-29. Issues from team-governed forums. The teams' own governance (project process, sprint cycle) owns the work; nothing here needs disposal. Issues go quiet after 14 days without a sighting. Escalated issues move to the Watch List. Design: `CLAUDE.md`, Operational Pulse.

## Account health

| Account | 7-day trend | Change | Load now | Load a week ago | Live | Stuck | Quiet | At your level |
|---|---|---|---|---|---|---|---|---|
| Stanford | Steady | +0 | 5 | 0 | 0 | 0 | 0 | 1 |
| Dell | Worsening | +48 | 184 | 131 | 25 | 3 | 8 | 1 |
| Federal Reserve | Worsening | +8 | 21 | 3 | 2 | 0 | 0 | 2 |
| Coca-Cola (TCCC) | Worsening | +9 | 13 | 4 | 4 | 0 | 1 | 0 |
| Wesco Warehouse | Steady | -3 | 16 | 19 | 2 | 1 | 1 | 0 |
| Ford | Steady | +0 | 11 | 1 | 0 | 0 | 1 | 2 |
| Marygrove | Steady | +0 | 8 | 8 | 1 | 0 | 0 | 0 |
| Louvre Abu Dhabi | Steady | +0 | 5 | 0 | 0 | 0 | 0 | 1 |
| Cree Church / Premier | Steady | +3 | 3 | 0 | 1 | 0 | 0 | 0 |

Load = live high visible x8, live high x6, live medium x3, live low x1, stuck x4, quiet x1, candidate x3, at your level x5. Trend = change in the team-raised load over 7 days, rebuilt from the dates meetings raised each issue; Worsening or Improving when it moves by at least 5 points and 15% of last week's load, otherwise Steady. Your register items are in the load but not the trend (no dated history). Friction from evidence, not customer sentiment.

No signals in the window: BAE, UWM.

## Needs your call

- **P076** Cree Church alarm configuration pending with no owner, outstanding for some time (no account; 2026 Deployment Daily Scrum). Test: No owner, or the customer is unaware of a material problem.
- **P077** Vamil/Wimmel floor-plan graphics may be outside the quoted non-DC scope (Dell; 2026 Deployment Daily Scrum). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P081** Admin-app migration: several screens are missing source data needed for migration decisions (no account; entroCIM Daily Stand Up). Test: No owner, or the customer is unaware of a material problem.
- **P082** Migrated SkySpark APIs/types still need per-application integration work (no account; entroCIM Daily Stand Up). Test: No owner, or the customer is unaware of a material problem.
- **P084** WAM historical upload: record-merge defect affecting perpetual-parts rows (no account; WAM Product Backlog Refinement). Test: No owner, or the customer is unaware of a material problem.
- **P085** WAM upload pipeline processes one resource at a time, causing multi-day stalls (no account; WAM Product Backlog Refinement). Test: No owner, or the customer is unaware of a material problem.
- **P086** WAM Spring Boot upgrade has unresolved runtime API issues; production release carries an unscoped DD-team dependency (no account; WAM Product Backlog Refinement). Test: No owner, or the customer is unaware of a material problem.
- **P087** entroCIM refresh hanging for some time while Babu C. Dinesh was away (no account; 2026 Deployment Daily Scrum). Test: No owner, or the customer is unaware of a material problem.
- **P088** ~800-900 additional points pending across four IRCs at the Limerick (Dell) closeout site (Dell; 2026 Deployment Daily Scrum). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P093** WAM: supplier filter returns unrelated sales orders, purchase orders and column-filter values (no account; WAM Sprint Review). Test: No owner, or the customer is unaware of a material problem.
- **P106** Device-to-floor-plan linking at Dell Site 6 is outside the assigned 3D-render scope, implementer unconfirmed (Dell; 2026 Deployment Daily Scrum). Test: No owner, or the customer is unaware of a material problem.
- **P078** paas-dev-03w returned HTTP 502 on 10-23; reported back up, not formally confirmed resolved (no account; entroCIM Daily Stand Up). Test: No owner, or the customer is unaware of a material problem.

## Knowledge concentration

Where one person holds knowledge a customer, a release or a migration depends on. Silence does not remove the risk: entries stay live for 45 days after the last evidence.

| ID | Knowledge area | Held by | Backup | Coverage | Exposure | Mitigation | Last evidence |
|---|---|---|---|---|---|---|---|
| K008 | FRB-restricted file-transfer workflow (BLOB storage moves requiring Federal Reserve handling) | Adam Slingerland | none named | none | customer |  | 2026-10-20 |
| K009 | WAM ADM renewal-recommendation code: original author departed, no documented backup, team in maintenance mode |  | none named | none | release | Rework the recommendation feature from scratch (see P068); no interim owner for the existing code. |  |
| K007 | Americas/LATAM watchdog, temperature-sensor and power-failure alarm audit; point-level alarm configuration | Elias Brewer | Keith Bishop | partial | customer | Keith Bishop named as the next technical adviser if Elias cannot assist; Keith also sole holder of the Limerick RCA (K006), so the backup is itself concentrated | 2026-10-22 |
| K006 | Dell Limerick alarm-handler RCA and release/build context for affected pod updates | Keith Bishop | none named | partial | customer, release | Ron Snyder mentioned as someone to ask; not named as backup (and away this week and next) | 2026-10-27 |

Not seen in 45+ days (confirm whether still true): K004 FRB load shed, Dell GMS energy points and KPIs, global metering due diligence (Elias Brewer).

## People carrying the most

| Person | Owns (Pulse) | Involved (Pulse) | Delegated/awaited | Sole holder | Forums |
|---|---|---|---|---|---|
| Chad Steger | 7 | 11 | 4 | 0 | 2026 Deployment Daily Scrum, entroCIM Backlog Deep Dive, entroCIM Daily Stand Up, Quest Migration Weekly Check-In |
| Akansh Gangil | 2 | 5 | 6 | 0 | ADM connect with Natalie, WAM Product Backlog Refinement, WAM Sprint Review |
| Syed Jamshed Zaidi | 7 | 27 | 0 | 0 | 2026 Deployment Daily Scrum, entroCIM Backlog Deep Dive |
| Scott Dunn | 5 | 15 | 1 | 0 | 2026 Deployment Daily Scrum |
| Shawn Clark | 4 | 8 | 1 | 0 | 2026 Deployment Daily Scrum, entroCIM Daily Stand Up, Quest Migration Weekly Check-In |
| Matthew Heid | 4 | 9 | 0 | 0 | 2026 Deployment Daily Scrum |
| Keith Bishop | 4 | 5 | 0 | 1 | 2026 Deployment Daily Scrum, entroCIM Daily Stand Up |
| Ron Snyder | 3 | 4 | 1 | 0 | 2026 Deployment Daily Scrum, entroCIM Daily Stand Up |
| Amy Aguirre | 0 | 0 | 4 | 0 |  |
| Babu Papanna | 2 | 1 | 1 | 0 | entroCIM Daily Stand Up, Quest Migration Weekly Check-In |
| Nathan Kehr | 0 | 0 | 3 | 0 |  |
| Sean McCloskey | 0 | 0 | 3 | 0 |  |

Owns: named owner of a live Pulse issue. Involved: named in the evidence with a statement, commitment or stated role, not the owner. Delegated/awaited: open register items they own. Sole holder: knowledge areas they hold without a confirmed backup.

## 2026 Deployment Daily Scrum

Governance: Project management. Owner: Chad Steger. Live 42, new this week 26, stuck 4, quiet 10. Last sighting: 2026-10-28. Last evidence: 2026-10-29.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P007 | PC1/JCI large-scale point faults and intermittent site access | Dell | Scott Dunn | High | 2026-09-15 | 2026-10-15 | 3 | stuck, customer-visible, escalated to W099 |
| P006 | Dell alarm-database corruption: intermittent alarming failures, no root cause | Dell | Ron Snyder; Keith Bishop | High | 2026-08-25 | 2026-10-21 | 7 | stuck, customer-visible, escalated to W009 |
| P028 | Site-meter information missing at several Dell sites (Chile named), blocking rollup views | Dell | Scott Dunn | High | 2026-10-13 | 2026-10-27 | 5 | stuck, customer-visible |
| P015 | Panama HVAC points increase continuously; BACnet setup failed, Modbus option untested | Wesco Warehouse | Matthew Heid; Scott Dunn | High | 2026-10-13 | 2026-10-28 | 3 | stuck, customer-visible |
| P027 | Singapore devices in remote fault since about 1 October; about six meters missing from both the deployment database and Niagara | Dell |  | High | 2026-10-15 | 2026-10-15 | 1 | customer-visible |
| P002 | Dell meter-data integrity: negative values, missing main meters, unreliable PPS3B data, demand/utilization mismatches | Dell | Syed Jamshed Zaidi | High | 2026-10-13 | 2026-10-20 | 4 | customer-visible |
| P036 | Point-level email alarms do not exist (connector-level only); blocks El Dorado closeout and applies to any site | Dell | Matthew Heid | High | 2026-10-20 | 2026-10-20 | 1 | customer-visible |
| P001 | PC1 Grid Board site-selection defect blocking the KWH report and dashboard | Dell |  | High | 2026-10-13 | 2026-10-22 | 4 | customer-visible |
| P063 | Chennai: all entroCIM connectors down, BACnet IDs do not match the spreadsheet |  |  | High | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P064 | Israel: all alarm points unbound (discrepancy 1273), needs Scott Dunn or Elias Brewer |  |  | High | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P066 | Argentina: watchdog connectors flapping connected/disconnected within a minute, source unidentified |  | Matthew Heid | High | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P067 | Customer alarm-audit request: scope undefined, could run ~400 hours or consume the SME allocation |  | Chad Steger | High | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P011 | Commissioned El Dorado devices not producing expected alarms ahead of environment decommissioning | Dell | Syed Jamshed Zaidi | High | 2026-10-14 | 2026-10-27 | 2 | customer-visible |
| P057 | Watchdog and UPS devices integration status unclear for Latin America sites; original-scope ownership not established | Dell |  | High | 2026-10-22 | 2026-10-27 | 2 | customer-visible |
| P074 | India PM8000 meter integration may depend on an unconfirmed India PME environment | Dell |  | High | 2026-10-27 | 2026-10-27 | 1 | customer-visible |
| P103 | North Carolina Modbus meter onboarding blocked by missing MIB file and unavailable meter credentials | Dell |  | High | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P104 | Meter naming cannot be mapped between connector names and the GMS sheet at Chennai, Dell 8, Dell 11 | Dell | Syed Jamshed Zaidi | High | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P107 | Limerick failure-condition alarm validation method undefined before telling Dell the release is approved | Dell |  | High | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P108 | El Dorado end-to-end alarm validation needs customer/site participation; approach not yet defined | Dell | Syed Jamshed Zaidi | High | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P029 | Prospective data-center customer substation request cannot be scoped (equipment, model and IP readiness unknown) |  | Syed Jamshed Zaidi | Medium | 2026-10-15 | 2026-10-15 | 1 | customer-visible |
| P003 | Dell IT access and investigation dependencies: Malaysia login failure, refresh-page issue, Panek BMS validation | Dell | Syed Jamshed Zaidi | Medium | 2026-10-15 | 2026-10-20 | 2 |  |
| P037 | Panama: additional control drawings needed; second-floor NetBotz and watchdog devices not yet procured or installed | Wesco Warehouse |  | Medium | 2026-10-20 | 2026-10-20 | 1 | customer-visible |
| P038 | Apex: four meter connectors ready but connectivity cannot be established; waiting on information from Robbie | Dell | Matthew Heid | Medium | 2026-10-20 | 2026-10-20 | 1 | customer-visible |
| P024 | Standardized UPS/device point list for integration and alarm rules still unavailable | Dell |  | Medium | 2026-10-14 | 2026-10-21 | 2 | customer-visible |
| P035 | Coke 7th Floor: work assigned with no background material; PO and construction completion unconfirmed | Coca-Cola (TCCC) | Syed Jamshed Zaidi | Medium | 2026-10-20 | 2026-10-21 | 2 | customer-visible |
| P059 | Newly added meter needs database cleanup; site name ambiguous (Annapolis or New York) |  | Babu C. Dinesh | Medium | 2026-10-22 | 2026-10-22 | 1 |  |
| P065 | No formal integration QA/QC checklist for closeout (alarm, fault-management, graphics, database, point-addition) |  |  | Medium | 2026-10-22 | 2026-10-22 | 1 |  |
| P004 | Dell visualization scope unsettled: point pages only, or basic graphics and floor plans (El Dorado) | Dell |  | Medium | 2026-10-15 | 2026-10-27 | 2 | customer-visible |
| P058 | EMEA (Harsley) alarm/integration discrepancy surfaced while Elias Brewer was out |  |  | Medium | 2026-10-22 | 2026-10-27 | 2 | customer-visible |
| P071 | Heating-stage and Boolean-point sequencing for reheat boxes remains unclear |  | Chad Steger | Medium | 2026-10-27 | 2026-10-27 | 1 |  |
| P072 | Three to four recently created GMS weather stations missing from validation tests |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 |  |
| P075 | Durham OPC UA onboarding: limited prior experience with how points will appear | Dell |  | Medium | 2026-10-27 | 2026-10-27 | 1 | customer-visible |
| P076 | Cree Church alarm configuration pending with no owner, outstanding for some time |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 | candidate: gap |
| P077 | Vamil/Wimmel floor-plan graphics may be outside the quoted non-DC scope | Dell |  | Medium | 2026-10-27 | 2026-10-27 | 1 | customer-visible, candidate: boundary |
| P087 | entroCIM refresh hanging for some time while Babu C. Dinesh was away |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 | candidate: gap |
| P088 | ~800-900 additional points pending across four IRCs at the Limerick (Dell) closeout site | Dell |  | Medium | 2026-10-27 | 2026-10-27 | 1 | customer-visible, candidate: boundary |
| P073 | Commissioning spreadsheet will not accept commissioning dates (Dell sites) | Dell |  | Medium | 2026-10-27 | 2026-10-28 | 2 |  |
| P089 | TCCC ECR connector (TEC 7th floor) timing out; connection info needs verification | Coca-Cola (TCCC) | Scott Dunn | Medium | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P090 | Two new TCCC NAT IP gateways need internal confirmation before checking the customer network side | Coca-Cola (TCCC) | Scott Dunn | Medium | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P091 | Repeated timeout and HTTP 504 errors on TCCC devices that had not shown them before; no nginx timeout standard | Coca-Cola (TCCC) |  | Medium | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P105 | Cree/Premier network-communication custom alarm rules still need review for a suitable configuration | Cree Church / Premier | Elias Brewer | Medium | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P106 | Device-to-floor-plan linking at Dell Site 6 is outside the assigned 3D-render scope, implementer unconfirmed | Dell |  | Medium | 2026-10-28 | 2026-10-28 | 1 | customer-visible, candidate: gap |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P005 Commissioned Panama devices not producing expected alarms ahead of environment decommissioning; P008 Dell cluster session loss: fleet-wide configuration review still open; P009 TCCC/AOC Modbus gateway sourcing may delay gas-sensor integration; P012 Dell FTE Franklin tracker: categorize items for Scott Dunn review; P014 Dell non-DC server unavailable since the prior week, blocking meter verification; P016 Trane Tracer BMS integration (Dell non-DC) may be outside the original scope and need separate estimation; P017 North America lighting-site UPS alarms visible in PME/NMC but not reaching entroCIM; P023 Penang 2: down points not triggering the expected faults or notifications; P025 Dell "three-creatures" requirements undefined; related work waits on a Dell workshop; P026 New York: two meters in commissioning, two with connection issues.

## entroCIM Daily Stand Up

Governance: Sprint (2-week). Owner: Ron Snyder. Live 24, new this week 13, stuck 0, quiet 2. Last sighting: 2026-10-28. Last evidence: 2026-10-29.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P041 | Showcase stopped running and recorded no data from Thursday night into Friday morning (10-15 to 10-16) |  |  | High | 2026-10-20 | 2026-10-21 | 2 | customer-visible |
| P111 | FRB alarm failures lack sufficient logging/data to diagnose why alarms fail to show up | Federal Reserve | Keith Bishop | High | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P039 | Tiles Grid Board compose chart: precision and date-handling defects cancel comparisons |  | Priyatosh Patra | Medium | 2026-10-15 | 2026-10-15 | 1 |  |
| P032 | Dell Showcase: virtual-point function failing, apparently around a faulty tag | Dell | Jason Ganiatsas | Medium | 2026-10-14 | 2026-10-20 | 2 | customer-visible |
| P040 | Shared UI components lack consistent button and styling standards as apps move into the monorepo |  | Harsha E | Medium | 2026-10-20 | 2026-10-20 | 1 |  |
| P042 | entroCIM 3.1.12.14 customer release notice one day behind the stated date (Chad out sick 10-19) |  | Chad Steger | Medium | 2026-10-20 | 2026-10-20 | 1 | customer-visible |
| P109 | HIS Express virtual-point inputs missing history, affecting rollups and downstream curve retrieval |  | Keith Bishop | Medium | 2026-10-21 | 2026-10-21 | 1 |  |
| P031 | SkySpark connectors failing in test: Energy Direct and others returning no data; 403 environment APIs returning HTTP 410 |  | Abhishek Savanur | Medium | 2026-10-13 | 2026-10-22 | 5 |  |
| P061 | HIS Express virtual-point UI stored constants as Y variables instead of literal values (hotfixed on demo one) |  | Michael Pieschel | Medium | 2026-10-22 | 2026-10-22 | 1 |  |
| P062 | FRB feedback: revised Graphics Builder documentation needs validation against their reported problem | Federal Reserve |  | Medium | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P069 | Another sensorless-connector defect found in testing; pod created, deployment pending |  | Abhishek Savanur | Medium | 2026-10-22 | 2026-10-22 | 1 |  |
| P070 | Commissioning app test-tracking coverage incomplete: tracks fields, not everything; no formal owner |  |  | Medium | 2026-10-22 | 2026-10-22 | 1 |  |
| P010 | entroCIM tenant redesign and boot-mode routing: no acceptance criteria, rollout sequence or release date yet |  | Michael Pieschel | Medium | 2026-10-14 | 2026-10-27 | 3 |  |
| P018 | Test server has no VPN connectivity to the private artifact repository (containerization) |  | Babu Papanna | Medium | 2026-10-14 | 2026-10-27 | 4 |  |
| P080 | Containerized release packaging question for GPO files/libraries in the entroCIM Release Builder |  | Narendra Singh | Medium | 2026-10-27 | 2026-10-27 | 1 |  |
| P081 | Admin-app migration: several screens are missing source data needed for migration decisions |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 | candidate: gap |
| P082 | Migrated SkySpark APIs/types still need per-application integration work |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 | candidate: gap |
| P110 | Demo 3 environment heavily loaded and difficult to use despite connector cleanup; helpdesk ticket open |  | Ron Snyder | Medium | 2026-10-28 | 2026-10-28 | 1 |  |
| P112 | Glenview Liberty PDU offline, blocking live data/graphic review for January Showcase planning |  | Keith Bishop | Medium | 2026-10-28 | 2026-10-28 | 1 |  |
| P056 | Freshdesk gives limited feedback visibility; no notification or digest for article ratings |  | Mike Reed | Low | 2026-10-20 | 2026-10-20 | 1 |  |
| P054 | Tiles Grid Board text widget: additional issues found in testing, follow-up needed |  | Nisha More | Low | 2026-10-14 | 2026-10-21 | 2 |  |
| P078 | paas-dev-03w returned HTTP 502 on 10-23; reported back up, not formally confirmed resolved |  |  | Low | 2026-10-27 | 2026-10-27 | 1 | candidate: gap |
| P079 | Zephyr Scale test tool inaccessible, blocking testing access; IT ticket raised |  | Shreyans Saklecha | Low | 2026-10-27 | 2026-10-27 | 1 |  |
| P083 | Monorepo migration still lacks a compiled list of remaining integration/build-script work |  | Ron Snyder | Low | 2026-10-27 | 2026-10-27 | 1 |  |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P030 PAS01 Grid Board pod not loaded after the pod update, blocking validation of completed fixes; P053 Grid Board monorepo migration: route broken because workspace components were not migrated correctly.

## entroCIM Backlog Deep Dive

Governance: Sprint / backlog. Owner: David Blondel. Live 4, new this week 0, stuck 0, quiet 0. Last sighting: 2026-10-20. Last evidence: 2026-10-21.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P043 | Schneider OPC UA protocol decision and proof of concept pending; constrains further Dell GMS completion | Dell |  | High | 2026-10-20 | 2026-10-20 | 1 | customer-visible |
| P046 | Marygrove: three open tickets; JACE down and customer IT cannot be reached | Marygrove |  | High | 2026-10-20 | 2026-10-20 | 1 | customer-visible |
| P044 | About $10,000 of completed delivery work may not yet be invoiced |  | Chad Steger | Medium | 2026-10-20 | 2026-10-20 | 1 |  |
| P045 | Automated weekly sales project updates paused: Rovo disabled pending AI approval |  | Chad Steger | Medium | 2026-10-20 | 2026-10-20 | 1 |  |

## Quest Migration Weekly Check-In

Governance: Project management. Owner: Chad Steger. Live 7, new this week 0, stuck 1, quiet 1. Last sighting: 2026-10-23. Last evidence: 2026-10-26.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P013 | Quest exit inventory: what must be retained and transferred to Wesco |  | Babu Papanna; Shawn Clark | Medium | 2026-09-16 | 2026-10-23 | 3 | stuck |
| P047 | Azure BLOB Storage accessible via browser but not through the required Linux command-line transfer path |  | Shawn Clark | High | 2026-10-20 | 2026-10-23 | 2 |  |
| P048 | MQTT cutover blocked pending DNS records and ports 1883/8883 |  | Chad Steger | High | 2026-10-20 | 2026-10-23 | 2 | customer-visible |
| P049 | Azure conductor still set up for high availability; primary-role turnover not yet switched |  | Shawn Clark | High | 2026-10-20 | 2026-10-23 | 2 |  |
| P050 | Libro may fail through the new conductor pending an outbound-IP or relay configuration change |  | Shawn Clark | High | 2026-10-20 | 2026-10-23 | 2 | customer-visible |
| P051 | Quest requesting additional $245/hour T&M on top of about $6,600/month; renewal and cancellation date unconfirmed |  |  | High | 2026-10-20 | 2026-10-23 | 2 |  |
| P052 | Workbench/BACnet Pro has no confirmed shared remote-access model after LogMeIn retirement |  | Chad Steger | Medium | 2026-10-20 | 2026-10-20 | 1 |  |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P100 Quest Migration: production MQTT/WAB path for Louvre Abu Dhabi -- Mosquitto FOSS code-change confirmation.

## WAM Product Backlog Refinement

Governance: Sprint. Owner: Sakshi Mathur. Live 4, new this week 4, stuck 0, quiet 2. Last sighting: 2026-10-27. Last evidence: 2026-10-27.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P068 | WAM renewal recommendation feature: quality rejected, rework from start |  |  | Medium | 2026-10-23 | 2026-10-23 | 1 |  |
| P084 | WAM historical upload: record-merge defect affecting perpetual-parts rows |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 | candidate: gap |
| P085 | WAM upload pipeline processes one resource at a time, causing multi-day stalls |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 | candidate: gap |
| P086 | WAM Spring Boot upgrade has unresolved runtime API issues; production release carries an unscoped DD-team dependency |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 | candidate: gap |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P019 WAM production: cancelled orders appear in export; expiry-chip criteria need validation; P020 WAM historical upload mishandles one customer ID with different names; duplicate ETL error records.

## WAM Sprint Review

Governance: Sprint. Owner: Sakshi Mathur. Live 5, new this week 3, stuck 2, quiet 0. Last sighting: 2026-10-27. Last evidence: 2026-10-28.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P021 | EUDM truncates manufacturer part numbers over 15 characters, causing ADM data loss |  |  | High | 2026-10-13 | 2026-10-27 | 3 | stuck, customer-visible, escalated to W016 |
| P022 | Missing EUDM shipping dates and country-code mapping block WAM data-enrichment completion |  |  | High | 2026-10-13 | 2026-10-27 | 3 | stuck, customer-visible |
| P094 | WAM critical security vulnerabilities remain open past the team's intended close date |  |  | High | 2026-10-27 | 2026-10-27 | 1 |  |
| P092 | WAM: selected supplier disappears from License and Orders after navigating away and back |  | Akansh Gangil | Medium | 2026-10-27 | 2026-10-27 | 1 | customer-visible |
| P093 | WAM: supplier filter returns unrelated sales orders, purchase orders and column-filter values |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 | customer-visible, candidate: gap |

## WAM Product discussion

Governance: Product execution. Owner: Akansh Gangil. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: 2026-10-22.

No issues in the Pulse yet.

## ADM connect with Natalie

Governance: Product execution. Owner: Akansh Gangil. Live 3, new this week 3, stuck 0, quiet 2. Last sighting: 2026-10-28. Last evidence: 2026-10-29.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P114 | Exact renewals cannot reliably identify end users from current data; no path to obtain it except possibly integrators |  |  | High | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P060 | Milestone/Exact missing sales-order data; Gina has not responded to Natalie's follow-up |  |  | Medium | 2026-10-22 | 2026-10-22 | 1 |  |
| P113 | ADM UI/data-quality feedback batch from Natalie's 10-28 review session (search debounce, filter logic, slowness, sort order) |  | Akansh Gangil | Medium | 2026-10-28 | 2026-10-28 | 1 |  |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P033 ADM removed/cancelled-orders page missing the removal-date column and export; P034 ADM renewal identification is manual and unreliable; renewal metrics cannot be sustained this way.

## Product Team / Platform Team connect

Governance: Team practice. Owner: Keyur Patel. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: 2026-10-21.

No issues in the Pulse yet.
