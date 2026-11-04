# Operational Pulse

<!-- GENERATED 2026-11-04 10:32 from Registers/ by Tools/eos_registers.py. Do not hand-edit this section; edit the item files under Registers/ or use the EOS web app. Pre-migration history is preserved verbatim in Archive/2026-10-15_pre_registers/. -->

> Rolling window 2026-10-21 to 2026-11-04. Issues from team-governed forums. The teams' own governance (project process, sprint cycle) owns the work; nothing here needs disposal. Issues go quiet after 14 days without a sighting. Escalated issues move to the Watch List. Design: `CLAUDE.md`, Operational Pulse.

## Account health

| Account | 7-day trend | Change | Load now | Load a week ago | Live | Stuck | Quiet | At your level |
|---|---|---|---|---|---|---|---|---|
| Merck | Worsening | +11 | 11 | 0 | 1 | 0 | 0 | 0 |
| Dell | Steady | +1 | 183 | 177 | 24 | 4 | 14 | 1 |
| Federal Reserve | Steady | +3 | 24 | 11 | 3 | 0 | 0 | 2 |
| Coca-Cola (TCCC) | Steady | +0 | 13 | 13 | 4 | 0 | 1 | 0 |
| Ford | Steady | +0 | 11 | 1 | 0 | 0 | 1 | 2 |
| Microsoft | Steady | +0 | 11 | 11 | 2 | 0 | 0 | 0 |
| Intel | Steady | +0 | 6 | 6 | 2 | 0 | 0 | 0 |
| Louvre Abu Dhabi | Steady | +0 | 5 | 0 | 0 | 0 | 0 | 1 |
| Stanford | Steady | +0 | 5 | 0 | 0 | 0 | 0 | 1 |
| Cree Church / Premier | Steady | +0 | 3 | 3 | 1 | 0 | 0 | 0 |
| Waymo | Steady | +0 | 3 | 3 | 1 | 0 | 0 | 0 |
| Wesco Warehouse | Improving | -9 | 14 | 23 | 1 | 1 | 2 | 0 |
| Marygrove | Improving | -7 | 1 | 8 | 0 | 0 | 1 | 0 |

Load = live high visible x8, live high x6, live medium x3, live low x1, stuck x4, quiet x1, candidate x3, at your level x5. Trend = change in the team-raised load over 7 days, rebuilt from the dates meetings raised each issue; Worsening or Improving when it moves by at least 5 points and 15% of last week's load, otherwise Steady. Your register items are in the load but not the trend (no dated history). Friction from evidence, not customer sentiment.

No signals in the window: BAE, UWM.

## Needs your call

- **P131** Merck entroCIM license maintenance substantially overdue; remote access may have lapsed (Merck; 2026 Deployment Daily Scrum). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P135** Dell HQ display/alarm issue: new alarms not showing, blocking a Penang production rollout (Dell; 2026 Deployment Daily Scrum). Test: No owner, or the customer is unaware of a material problem.
- **P137** Prior Gridboard monorepo migration lost code and broke functionality; migration restarted (no account; entroCIM Daily Stand Up). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P132** Updated LATAM server returns a system error after yesterday's update (no account; 2026 Deployment Daily Scrum). Test: No owner, or the customer is unaware of a material problem.
- **P134** Dell 6 lab-meter integrations waiting on single-host-to-multi-host gateway replacement (Dell; 2026 Deployment Daily Scrum). Test: No owner, or the customer is unaware of a material problem.
- **P136** Quest VM backups exist but recoverability has not been proven with a restore test (no account; Quest Migration Weekly Check-In). Test: No owner, or the customer is unaware of a material problem.
- **P138** Dev03 HQ/Axon collective-site meter reading broken or corrupted (no account; entroCIM Daily Stand Up). Test: No owner, or the customer is unaware of a material problem.
- **P141** ServiceNow and EcoStruxure integrations both blocked (no account; entroCIM Backlog Deep Dive). Test: No owner, or the customer is unaware of a material problem.

## Knowledge concentration

Where one person holds knowledge a customer, a release or a migration depends on. Silence does not remove the risk: entries stay live for 45 days after the last evidence.

| ID | Knowledge area | Held by | Backup | Coverage | Exposure | Mitigation | Last evidence |
|---|---|---|---|---|---|---|---|
| K010 | Dell Penang One BMS access and credentials | Scott Dunn | none named | none | customer | Syed Jamshed Zaidi to follow up with IT for credentials; Matthew Heid asked for a wider access conversation ("more people access and not just Scott") | 2026-10-29 |
| K008 | FRB-restricted file-transfer workflow (BLOB storage moves requiring Federal Reserve handling) | Adam Slingerland | none named | none | customer |  | 2026-10-27 |
| K009 | WAM ADM renewal-recommendation code: original author departed, no documented backup, team in maintenance mode |  | none named | none | release | Rework the recommendation feature from scratch (see P068); no interim owner for the existing code. | 2026-11-02 |
| K007 | Americas/LATAM watchdog, temperature-sensor and power-failure alarm audit; point-level alarm configuration | Elias Brewer | Keith Bishop | partial | customer | Keith Bishop named as the next technical adviser if Elias cannot assist; Keith also sole holder of the Limerick RCA (K006), so the backup is itself concentrated | 2026-10-22 |
| K006 | Dell Limerick alarm-handler RCA and release/build context for affected pod updates | Keith Bishop | none named | partial | customer, release | Ron Snyder mentioned as someone to ask; not named as backup (and away this week and next) | 2026-10-29 |

Not seen in 45+ days (confirm whether still true): K004 FRB load shed, Dell GMS energy points and KPIs, global metering due diligence (Elias Brewer).

## People carrying the most

| Person | Owns (Pulse) | Involved (Pulse) | Delegated/awaited | Sole holder | Forums |
|---|---|---|---|---|---|
| Chad Steger | 6 | 18 | 4 | 0 | 2026 Deployment Daily Scrum, entroCIM Daily Stand Up, Quest Migration Weekly Check-In |
| Akansh Gangil | 3 | 6 | 5 | 0 | ADM connect with Natalie, WAM Product Backlog Refinement, WAM Product discussion, WAM Sprint Review |
| Syed Jamshed Zaidi | 6 | 27 | 0 | 0 | 2026 Deployment Daily Scrum |
| Shawn Clark | 4 | 7 | 2 | 0 | 2026 Deployment Daily Scrum, Quest Migration Weekly Check-In |
| Keith Bishop | 5 | 3 | 0 | 1 | 2026 Deployment Daily Scrum, entroCIM Daily Stand Up |
| Scott Dunn | 4 | 14 | 1 | 1 | 2026 Deployment Daily Scrum |
| Ron Snyder | 3 | 6 | 2 | 0 | 2026 Deployment Daily Scrum, entroCIM Backlog Deep Dive, entroCIM Daily Stand Up |
| Amy Aguirre | 0 | 0 | 4 | 0 |  |
| Babu Papanna | 2 | 2 | 1 | 0 | entroCIM Daily Stand Up, Quest Migration Weekly Check-In |
| Nathan Kehr | 0 | 0 | 3 | 0 |  |
| Sean McCloskey | 0 | 0 | 3 | 0 |  |
| Matthew Heid | 2 | 14 | 0 | 0 | 2026 Deployment Daily Scrum |

Owns: named owner of a live Pulse issue. Involved: named in the evidence with a statement, commitment or stated role, not the owner. Delegated/awaited: open register items they own. Sole holder: knowledge areas they hold without a confirmed backup.

## 2026 Deployment Daily Scrum

Governance: Project management. Owner: Chad Steger. Live 46, new this week 19, stuck 5, quiet 16. Last sighting: 2026-11-04. Last evidence: 2026-11-04.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P006 | Dell alarm-database corruption: intermittent alarming failures, no root cause | Dell | Ron Snyder; Keith Bishop | High | 2026-08-25 | 2026-10-21 | 7 | stuck, customer-visible, escalated to W009 |
| P028 | Site-meter information missing at several Dell sites (Chile named), blocking rollup views | Dell | Scott Dunn | High | 2026-10-13 | 2026-10-27 | 5 | stuck, customer-visible |
| P015 | Panama HVAC points increase continuously; BACnet setup failed, Modbus option untested | Wesco Warehouse | Matthew Heid; Scott Dunn | High | 2026-10-13 | 2026-10-28 | 3 | stuck, customer-visible |
| P002 | Dell meter-data integrity: negative values, missing main meters, unreliable PPS3B data, demand/utilization mismatches | Dell | Syed Jamshed Zaidi | High | 2026-10-13 | 2026-10-29 | 5 | stuck, customer-visible |
| P003 | Dell IT access and investigation dependencies: Malaysia login failure, refresh-page issue, Panek BMS validation | Dell | Syed Jamshed Zaidi | Medium | 2026-10-15 | 2026-10-29 | 3 | stuck |
| P001 | PC1 Grid Board site-selection defect blocking the KWH report and dashboard | Dell |  | High | 2026-10-13 | 2026-10-22 | 4 | customer-visible |
| P063 | Chennai: all entroCIM connectors down, BACnet IDs do not match the spreadsheet |  |  | High | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P064 | Israel: all alarm points unbound (discrepancy 1273), needs Scott Dunn or Elias Brewer |  |  | High | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P066 | Argentina: watchdog connectors flapping connected/disconnected within a minute, source unidentified |  | Matthew Heid | High | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P067 | Customer alarm-audit request: scope undefined, could run ~400 hours or consume the SME allocation |  | Chad Steger | High | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P011 | Commissioned El Dorado devices not producing expected alarms ahead of environment decommissioning | Dell | Syed Jamshed Zaidi | High | 2026-10-14 | 2026-10-27 | 2 | customer-visible |
| P057 | Watchdog and UPS devices integration status unclear for Latin America sites; original-scope ownership not established | Dell |  | High | 2026-10-22 | 2026-10-27 | 2 | customer-visible |
| P074 | India PM8000 meter integration may depend on an unconfirmed India PME environment | Dell |  | High | 2026-10-27 | 2026-10-27 | 1 | customer-visible |
| P108 | El Dorado end-to-end alarm validation needs customer/site participation; approach not yet defined | Dell | Syed Jamshed Zaidi | High | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P103 | North Carolina Modbus meter onboarding blocked by missing MIB file and unavailable meter credentials | Dell |  | High | 2026-10-28 | 2026-10-29 | 2 | customer-visible |
| P104 | Meter naming cannot be mapped between connector names and the GMS sheet at Chennai, Dell 8, Dell 11 | Dell | Syed Jamshed Zaidi | High | 2026-10-28 | 2026-10-29 | 2 | customer-visible |
| P115 | HQ alarm list drops cleared alarms (longstanding, all sites); fix expected with the new pods, validation pending | Dell |  | High | 2026-10-29 | 2026-10-29 | 1 | customer-visible |
| P116 | Palo Alto NetBot found outside the earlier non-DC scope: new integration needed, device credentials unconfirmed | Dell |  | High | 2026-10-29 | 2026-10-29 | 1 | customer-visible |
| P107 | Limerick failure-condition alarm validation method undefined before telling Dell the release is approved | Dell |  | High | 2026-10-28 | 2026-11-03 | 3 | customer-visible |
| P131 | Merck entroCIM license maintenance substantially overdue; remote access may have lapsed | Merck |  | High | 2026-11-04 | 2026-11-04 | 1 | customer-visible, candidate: boundary |
| P135 | Dell HQ display/alarm issue: new alarms not showing, blocking a Penang production rollout | Dell |  | High | 2026-11-03 | 2026-11-04 | 1 | customer-visible, candidate: gap |
| P024 | Standardized UPS/device point list for integration and alarm rules still unavailable | Dell |  | Medium | 2026-10-14 | 2026-10-21 | 2 | customer-visible |
| P035 | Coke 7th Floor: work assigned with no background material; PO and construction completion unconfirmed | Coca-Cola (TCCC) | Syed Jamshed Zaidi | Medium | 2026-10-20 | 2026-10-21 | 2 | customer-visible |
| P059 | Newly added meter needs database cleanup; site name ambiguous (Annapolis or New York) |  | Babu C. Dinesh | Medium | 2026-10-22 | 2026-10-22 | 1 |  |
| P065 | No formal integration QA/QC checklist for closeout (alarm, fault-management, graphics, database, point-addition) |  |  | Medium | 2026-10-22 | 2026-10-22 | 1 |  |
| P004 | Dell visualization scope unsettled: point pages only, or basic graphics and floor plans (El Dorado) | Dell |  | Medium | 2026-10-15 | 2026-10-27 | 2 | customer-visible |
| P058 | EMEA (Harsley) alarm/integration discrepancy surfaced while Elias Brewer was out |  |  | Medium | 2026-10-22 | 2026-10-27 | 2 | customer-visible |
| P071 | Heating-stage and Boolean-point sequencing for reheat boxes remains unclear |  | Chad Steger | Medium | 2026-10-27 | 2026-10-27 | 1 |  |
| P072 | Three to four recently created GMS weather stations missing from validation tests |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 |  |
| P075 | Durham OPC UA onboarding: limited prior experience with how points will appear | Dell |  | Medium | 2026-10-27 | 2026-10-27 | 1 | customer-visible |
| P076 | Cree Church alarm configuration pending with no owner, outstanding for some time |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 |  |
| P091 | Repeated timeout and HTTP 504 errors on TCCC devices that had not shown them before; no nginx timeout standard | Coca-Cola (TCCC) |  | Medium | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P105 | Cree/Premier network-communication custom alarm rules still need review for a suitable configuration | Cree Church / Premier | Elias Brewer | Medium | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P106 | Device-to-floor-plan linking at Dell Site 6 is outside the assigned 3D-render scope, implementer unconfirmed | Dell |  | Medium | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P073 | Commissioning spreadsheet will not accept commissioning dates (Dell sites) | Dell |  | Medium | 2026-10-27 | 2026-10-29 | 3 |  |
| P077 | Vamil/Wimmel floor-plan graphics may be outside the quoted non-DC scope | Dell |  | Medium | 2026-10-27 | 2026-10-29 | 2 | customer-visible |
| P088 | ~800-900 additional points pending across four IRCs at the Limerick (Dell) closeout site | Dell |  | Medium | 2026-10-27 | 2026-10-29 | 2 | customer-visible |
| P089 | TCCC ECR connector (TEC 7th floor) timing out; connection info needs verification | Coca-Cola (TCCC) | Scott Dunn | Medium | 2026-10-28 | 2026-10-29 | 2 | customer-visible |
| P090 | Two new TCCC NAT IP gateways need internal confirmation before checking the customer network side | Coca-Cola (TCCC) | Scott Dunn | Medium | 2026-10-28 | 2026-10-29 | 2 | customer-visible |
| P117 | Non-DC closeout basis unclear: prior documentation may not identify El Dorado or carry a complete site list | Dell |  | Medium | 2026-10-29 | 2026-10-29 | 1 | customer-visible |
| P087 | entroCIM refresh hanging for some time while Babu C. Dinesh was away |  |  | Medium | 2026-10-27 | 2026-11-03 | 3 |  |
| P132 | Updated LATAM server returns a system error after yesterday's update |  |  | Medium | 2026-11-04 | 2026-11-04 | 1 | candidate: gap |
| P133 | Phoenix valve connector times out opening its large analog-input folder; CSV export used as a workaround |  | Chad Steger | Medium | 2026-11-04 | 2026-11-04 | 1 | customer-visible |
| P134 | Dell 6 lab-meter integrations waiting on single-host-to-multi-host gateway replacement | Dell |  | Medium | 2026-11-04 | 2026-11-04 | 1 | customer-visible, candidate: gap |
| P129 | ConnectorWise configuration churns repeatedly without an official equipment-and-points document |  |  | Medium | 2026-11-03 |  | 1 |  |
| P130 | FRB graphics blocked: only a BACnet point export is available, lighting floor-plan layouts still needed | Federal Reserve | Chad Steger | Medium | 2026-11-03 |  | 1 | customer-visible |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P005 Commissioned Panama devices not producing expected alarms ahead of environment decommissioning; P007 PC1/JCI large-scale point faults and intermittent site access; P008 Dell cluster session loss: fleet-wide configuration review still open; P009 TCCC/AOC Modbus gateway sourcing may delay gas-sensor integration; P012 Dell FTE Franklin tracker: categorize items for Scott Dunn review; P014 Dell non-DC server unavailable since the prior week, blocking meter verification; P016 Trane Tracer BMS integration (Dell non-DC) may be outside the original scope and need separate estimation; P017 North America lighting-site UPS alarms visible in PME/NMC but not reaching entroCIM; P023 Penang 2: down points not triggering the expected faults or notifications; P025 Dell "three-creatures" requirements undefined; related work waits on a Dell workshop; P026 New York: two meters in commissioning, two with connection issues; P027 Singapore devices in remote fault since about 1 October; about six meters missing from both the deployment database and Niagara; P029 Prospective data-center customer substation request cannot be scoped (equipment, model and IP readiness unknown); P036 Point-level email alarms do not exist (connector-level only); blocks El Dorado closeout and applies to any site; P037 Panama: additional control drawings needed; second-floor NetBotz and watchdog devices not yet procured or installed; P038 Apex: four meter connectors ready but connectivity cannot be established; waiting on information from Robbie.

## entroCIM Daily Stand Up

Governance: Sprint (2-week). Owner: Ron Snyder. Live 21, new this week 10, stuck 3, quiet 4. Last sighting: 2026-11-04. Last evidence: 2026-11-04.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P030 | PAS01 Grid Board pod not loaded after the pod update, blocking validation of completed fixes |  | Ron Snyder | High | 2026-10-13 | 2026-10-28 | 2 | stuck, customer-visible |
| P031 | SkySpark connectors failing in test: Energy Direct and others returning no data; 403 environment APIs returning HTTP 410 |  | Abhishek Savanur | Medium | 2026-10-13 | 2026-10-29 | 7 | stuck |
| P018 | Test server has no VPN connectivity to the private artifact repository (containerization) |  | Babu Papanna | Medium | 2026-10-14 | 2026-11-04 | 5 | stuck |
| P041 | Showcase stopped running and recorded no data from Thursday night into Friday morning (10-15 to 10-16) |  |  | High | 2026-10-20 | 2026-10-21 | 2 | customer-visible |
| P111 | FRB alarm failures lack sufficient logging/data to diagnose why alarms fail to show up | Federal Reserve | Keith Bishop | High | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P137 | Prior Gridboard monorepo migration lost code and broke functionality; migration restarted |  | Nisha More | High | 2026-11-04 | 2026-11-04 | 1 | candidate: boundary |
| P109 | HIS Express virtual-point inputs missing history, affecting rollups and downstream curve retrieval |  | Keith Bishop | Medium | 2026-10-21 | 2026-10-21 | 1 |  |
| P061 | HIS Express virtual-point UI stored constants as Y variables instead of literal values (hotfixed on demo one) |  | Michael Pieschel | Medium | 2026-10-22 | 2026-10-22 | 1 |  |
| P062 | FRB feedback: revised Graphics Builder documentation needs validation against their reported problem | Federal Reserve |  | Medium | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P069 | Another sensorless-connector defect found in testing; pod created, deployment pending |  | Abhishek Savanur | Medium | 2026-10-22 | 2026-10-22 | 1 |  |
| P010 | entroCIM tenant redesign and boot-mode routing: no acceptance criteria, rollout sequence or release date yet |  | Michael Pieschel | Medium | 2026-10-14 | 2026-10-27 | 3 |  |
| P080 | Containerized release packaging question for GPO files/libraries in the entroCIM Release Builder |  | Narendra Singh | Medium | 2026-10-27 | 2026-10-27 | 1 |  |
| P112 | Glenview Liberty PDU offline, blocking live data/graphic review for January Showcase planning |  | Keith Bishop | Medium | 2026-10-28 | 2026-10-28 | 1 |  |
| P123 | SkySpark 4 license migration works with the tested connectors but is not yet compatible with containerization |  |  | Medium | 2026-10-28 | 2026-10-28 | 1 |  |
| P124 | January trade-show Showcase: the 3D render must match the physical booth hardware |  |  | Medium | 2026-10-28 | 2026-10-28 | 1 | customer-visible |
| P110 | Demo 3 environment heavily loaded and difficult to use despite connector cleanup; helpdesk ticket open |  | Ron Snyder | Medium | 2026-10-28 | 2026-10-29 | 2 |  |
| P138 | Dev03 HQ/Axon collective-site meter reading broken or corrupted |  |  | Medium | 2026-11-04 | 2026-11-04 | 1 | candidate: gap |
| P139 | SkySpark 4.0.6 connectors fail to install in release-builder testing |  | Narendra Singh; Sai Kiran Vadluri | Medium | 2026-11-04 | 2026-11-04 | 1 |  |
| P140 | SkySpark 4.0.7: HQ routing returns "not found" after JSON/Xeto changes |  | Nihar Ranjan Sahu | Medium | 2026-11-04 | 2026-11-04 | 1 |  |
| P127 | SkySpark 4 QA environment (Dev03W) missing Keith Bishop's pods; QA functionality missing for months |  | Keith Bishop | Medium | 2026-11-03 |  | 1 |  |
| P054 | Tiles Grid Board text widget: additional issues found in testing, follow-up needed |  | Nisha More | Low | 2026-10-14 | 2026-10-21 | 2 |  |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P032 Dell Showcase: virtual-point function failing, apparently around a faulty tag; P039 Tiles Grid Board compose chart: precision and date-handling defects cancel comparisons; P042 entroCIM 3.1.12.14 customer release notice one day behind the stated date (Chad out sick 10-19); P056 Freshdesk gives limited feedback visibility; no notification or digest for article ratings.

## entroCIM Backlog Deep Dive

Governance: Sprint / backlog. Owner: David Blondel. Live 1, new this week 1, stuck 0, quiet 4. Last sighting: 2026-11-03. Last evidence: 2026-11-03.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P141 | ServiceNow and EcoStruxure integrations both blocked |  |  | Medium | 2026-11-03 | 2026-11-03 | 1 | candidate: gap |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P043 Schneider OPC UA protocol decision and proof of concept pending; constrains further Dell GMS completion; P044 About $10,000 of completed delivery work may not yet be invoiced; P045 Automated weekly sales project updates paused: Rovo disabled pending AI approval; P046 Marygrove: three open tickets; JACE down and customer IT cannot be reached.

## Quest Migration Weekly Check-In

Governance: Project management. Owner: Chad Steger. Live 8, new this week 1, stuck 6, quiet 1. Last sighting: 2026-11-03. Last evidence: 2026-11-03.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P047 | Azure BLOB Storage accessible via browser but not through the required Linux command-line transfer path |  | Shawn Clark | High | 2026-10-20 | 2026-11-03 | 4 | stuck |
| P048 | MQTT cutover blocked pending DNS records and ports 1883/8883 |  | Chad Steger | High | 2026-10-20 | 2026-11-03 | 4 | stuck, customer-visible |
| P049 | Azure conductor still set up for high availability; primary-role turnover not yet switched |  | Shawn Clark | High | 2026-10-20 | 2026-11-03 | 3 | stuck |
| P050 | Libro may fail through the new conductor pending an outbound-IP or relay configuration change |  | Shawn Clark | High | 2026-10-20 | 2026-11-03 | 4 | stuck, customer-visible |
| P013 | Quest exit inventory: what must be retained and transferred to Wesco |  | Babu Papanna; Shawn Clark | Medium | 2026-09-16 | 2026-10-29 | 5 | stuck |
| P052 | Workbench/BACnet Pro has no confirmed shared remote-access model after LogMeIn retirement |  | Chad Steger | Medium | 2026-10-20 | 2026-11-03 | 3 | stuck |
| P051 | Quest requesting additional $245/hour T&M on top of about $6,600/month; renewal and cancellation date unconfirmed |  |  | High | 2026-10-20 | 2026-10-23 | 2 |  |
| P136 | Quest VM backups exist but recoverability has not been proven with a restore test |  |  | Medium | 2026-11-03 | 2026-11-03 | 1 | candidate: gap |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P100 Quest Migration: production MQTT/WAB path for Louvre Abu Dhabi -- Mosquitto FOSS code-change confirmation.

## WAM Product Backlog Refinement

Governance: Sprint. Owner: Sakshi Mathur. Live 5, new this week 1, stuck 0, quiet 2. Last sighting: 2026-11-02. Last evidence: 2026-11-04.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P084 | WAM historical upload: record-merge defect affecting perpetual-parts rows |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 |  |
| P085 | WAM upload pipeline processes one resource at a time, causing multi-day stalls |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 |  |
| P086 | WAM Spring Boot upgrade has unresolved runtime API issues; production release carries an unscoped DD-team dependency |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 |  |
| P068 | WAM renewal recommendation feature: quality rejected, rework from start |  |  | Medium | 2026-10-23 | 2026-11-02 | 2 |  |
| P128 | WMX asset refresh trails Gold EUDM by six hours; order and serial-number data may need two separate jobs |  |  | Medium | 2026-11-03 |  | 1 |  |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P019 WAM production: cancelled orders appear in export; expiry-chip criteria need validation; P020 WAM historical upload mishandles one customer ID with different names; duplicate ETL error records.

## WAM Sprint Review

Governance: Sprint. Owner: Sakshi Mathur. Live 5, new this week 0, stuck 2, quiet 0. Last sighting: 2026-11-02. Last evidence: 2026-11-02.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P021 | EUDM truncates manufacturer part numbers over 15 characters, causing ADM data loss |  |  | High | 2026-10-13 | 2026-10-27 | 3 | stuck, customer-visible, escalated to W016 |
| P022 | Missing EUDM shipping dates and country-code mapping block WAM data-enrichment completion |  |  | High | 2026-10-13 | 2026-10-27 | 3 | stuck, customer-visible |
| P094 | WAM critical security vulnerabilities remain open past the team's intended close date |  |  | High | 2026-10-27 | 2026-11-02 | 2 |  |
| P092 | WAM: selected supplier disappears from License and Orders after navigating away and back |  | Akansh Gangil | Medium | 2026-10-27 | 2026-10-27 | 1 | customer-visible |
| P093 | WAM: supplier filter returns unrelated sales orders, purchase orders and column-filter values |  |  | Medium | 2026-10-27 | 2026-10-27 | 1 | customer-visible |

## WAM Product discussion

Governance: Product execution. Owner: Akansh Gangil. Live 5, new this week 0, stuck 0, quiet 0. Last sighting: 2026-10-22. Last evidence: 2026-10-22.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P118 | Microsoft data uploads waiting on Microsoft's review of lower-confidence corrections; no internal owner for obtaining it | Microsoft |  | High | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P119 | Microsoft post-cleanup operating model undefined: continual imports, dashboard access, internal/external user model | Microsoft |  | Medium | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P120 | Latest Intel BOM arrived without manufacturer part numbers; cause unknown | Intel |  | Medium | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P121 | Intel components may not be serialized, so barcode-based serial capture may not apply | Intel |  | Medium | 2026-10-22 | 2026-10-22 | 1 | customer-visible |
| P122 | Waymo: Wesco systems may not capture address-level differentiators when several builds share one sales order and PO | Waymo | Akansh Gangil | Medium | 2026-10-22 | 2026-10-22 | 1 | customer-visible |

## ADM connect with Natalie

Governance: Product execution. Owner: Akansh Gangil. Live 3, new this week 2, stuck 0, quiet 2. Last sighting: 2026-11-02. Last evidence: 2026-11-02.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P114 | Exact renewals cannot reliably identify end users from current data; no path to obtain it except possibly integrators |  |  | High | 2026-10-28 | 2026-11-02 | 2 | customer-visible |
| P060 | Milestone/Exact missing sales-order data; Gina has not responded to Natalie's follow-up |  |  | Medium | 2026-10-22 | 2026-10-22 | 1 |  |
| P113 | ADM UI/data-quality feedback batch from Natalie's 10-28 review session (search debounce, filter logic, slowness, sort order) |  | Akansh Gangil | Medium | 2026-10-28 | 2026-11-02 | 2 |  |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P033 ADM removed/cancelled-orders page missing the removal-date column and export; P034 ADM renewal identification is manual and unreliable; renewal metrics cannot be sustained this way.

## Product Team / Platform Team connect

Governance: Team practice. Owner: Keyur Patel. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: 2026-10-21.

No issues in the Pulse yet.
