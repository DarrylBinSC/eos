# Operational Pulse

<!-- GENERATED 2026-11-12 10:21 from Registers/ by Tools/eos_registers.py. Do not hand-edit this section; edit the item files under Registers/ or use the EOS web app. Pre-migration history is preserved verbatim in Archive/2026-10-15_pre_registers/. -->

> Rolling window 2026-10-29 to 2026-11-12. Issues from team-governed forums. The teams' own governance (project process, sprint cycle) owns the work; nothing here needs disposal. An issue with no sighting for 10 days (21 for a bi-weekly forum) is closed as presumed resolved by silence and reopens if raised again. A Medium or Low issue counts as live from its third sighting. Escalated issues move to the Watch List. Design: `CLAUDE.md`, Operational Pulse.

## Account health

| Account | 7-day trend | Change | Load now | Load a week ago | Live | Stuck | Quiet | At your level |
|---|---|---|---|---|---|---|---|---|
| Dell | Improving | -115 | 73 | 183 | 8 | 2 | 1 | 1 |
| Federal Reserve | Worsening | +10 | 29 | 9 | 2 | 0 | 0 | 2 |
| Ford | Worsening | +5 | 16 | 1 | 1 | 0 | 0 | 2 |
| Coca-Cola (TCCC) | Worsening | +6 | 8 | 2 | 1 | 0 | 0 | 0 |
| Wesco Warehouse | Steady | -2 | 12 | 14 | 1 | 1 | 0 | 0 |
| Merck | Steady | +0 | 8 | 8 | 1 | 0 | 0 | 0 |
| Louvre Abu Dhabi | Steady | +0 | 5 | 0 | 0 | 0 | 0 | 1 |
| Cree Church / Premier | Steady | +0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Intel | Steady | -2 | 0 | 2 | 0 | 0 | 0 | 0 |
| Microsoft | Steady | -2 | 0 | 2 | 0 | 0 | 0 | 0 |
| Waymo | Steady | -1 | 0 | 1 | 0 | 0 | 0 | 0 |
| Marygrove | Improving | -8 | 0 | 8 | 0 | 0 | 0 | 0 |

Load = live high visible x8, live high x6, live medium x3, live low x1, stuck x4, quiet x1, candidate x3, at your level x5. Trend = change in the team-raised load over 7 days, rebuilt from the dates meetings raised each issue; Worsening or Improving when it moves by at least 5 points and 15% of last week's load, otherwise Steady. Your register items are in the load but not the trend (no dated history). Friction from evidence, not customer sentiment.

No signals in the window: BAE, Stanford, UWM.

## Needs your call

- **P174** Some Modbus "people counter" points have produced no data since April, at a site Copilot transcribed as "Louv" (no account; 2026 Deployment Daily Scrum). Test: Still being raised 10+ business days after it was first raised.
- **P180** Quest migration: Nextcloud recovery is complicated by 500 GB-1 TB of encrypted volume and an LDAP dependency on a domain controller slated for removal (no account; Quest Migration Weekly Check-In). Test: Darryl named or asked for a decision, resource or escalation.
- **P186** Federal Reserve environment blocks Internet-hosted font/dependency access, requiring an offline packaging or fallback strategy (Federal Reserve; entroCIM Daily Stand Up). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P176** A site transcribed as "Govardhan" may have an overloaded server with 771 Modbus connectors, preventing validation (no account; 2026 Deployment Daily Scrum). Test: No owner, or the customer is unaware of a material problem.
- **P177** Mobile-device data flow is blocked by a firewall owned by a team outside this forum (no account; 2026 Deployment Daily Scrum). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P178** WEML rendering/alarming work has an unresolved billing question: whether it should be a separate PO (no account; 2026 Deployment Daily Scrum). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P182** Quest migration: old servers believed stopped unexpectedly appeared to still be running (no account; Quest Migration Weekly Check-In). Test: No owner, or the customer is unaware of a material problem.
- **P187** Ford Rouge requires new points added before December 1 on a newly received tool, consuming allocated SME hours (Ford; entroCIM Daily Stand Up). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P189** Innovation Center Lab's unreliability (Bright Layer device unavailable) is blocking containerization/device work (no account; entroCIM Daily Stand Up). Test: Crossed out of the forum: contract, money, customer executive, customer communication, or an outside team.
- **P188** Version information for existing customer/platform versions is not maintained in any single, actively managed inventory (no account; entroCIM Daily Stand Up). Test: No owner, or the customer is unaware of a material problem.

## Knowledge concentration

Where one person holds knowledge a customer, a release or a migration depends on. Silence does not remove the risk: entries stay live for 45 days after the last evidence.

| ID | Knowledge area | Held by | Backup | Coverage | Exposure | Mitigation | Last evidence |
|---|---|---|---|---|---|---|---|
| K010 | Dell Penang One BMS access and credentials | Scott Dunn | none named | none | customer | Syed Jamshed Zaidi to follow up with IT for credentials; Matthew Heid asked for a wider access conversation ("more people access and not just Scott") | 2026-10-29 |
| K008 | FRB-restricted file-transfer workflow (BLOB storage moves requiring Federal Reserve handling) | Adam Slingerland | none named | none | customer |  | 2026-10-27 |
| K009 | WAM ADM renewal-recommendation code: original author departed, no documented backup, team in maintenance mode |  | none named | none | release | Rework the recommendation feature from scratch (see P068); no interim owner for the existing code. | 2026-11-02 |
| K007 | Americas/LATAM watchdog, temperature-sensor and power-failure alarm audit; point-level alarm configuration | Elias Brewer | Keith Bishop | partial | customer | Keith Bishop named as the next technical adviser if Elias cannot assist; Keith also sole holder of the Limerick RCA (K006), so the backup is itself concentrated | 2026-11-12 |
| K006 | Dell Limerick alarm-handler RCA and release/build context for affected pod updates | Keith Bishop | none named | partial | customer, release | Ron Snyder mentioned as someone to ask; not named as backup (and away this week and next) | 2026-10-29 |
| K011 | Shawn Clark concentration on Quest migration recovery and network tasks (Windows Restore, Airwall DNS, port testing) | Shawn Clark | Chad Steger (partial -- retained follow-up on external port requests and cloud-PC/Airwall access work only, not the Windows Restore or DNS tasks) | partial | migration |  | 2026-11-10 |

Not seen in 45+ days (confirm whether still true): K004 FRB load shed, Dell GMS energy points and KPIs, global metering due diligence (Elias Brewer).

## People carrying the most

| Person | Owns (Pulse) | Involved (Pulse) | Delegated/awaited | Sole holder | Forums |
|---|---|---|---|---|---|
| Chad Steger | 5 | 9 | 4 | 0 | 2026 Deployment Daily Scrum, entroCIM Daily Stand Up, Quest Migration Weekly Check-In |
| Shawn Clark | 3 | 4 | 2 | 1 | Quest Migration Weekly Check-In |
| Akansh Gangil | 0 | 4 | 5 | 0 | ADM connect with Natalie, WAM Product Backlog Refinement, WAM Sprint Review |
| Ron Snyder | 2 | 6 | 2 | 0 | entroCIM Daily Stand Up, Quest Migration Weekly Check-In |
| Amy Aguirre | 0 | 0 | 4 | 0 |  |
| Scott Dunn | 2 | 4 | 1 | 1 | 2026 Deployment Daily Scrum |
| Natalie Marquardt | 0 | 1 | 3 | 0 | ADM connect with Natalie |
| Nathan Kehr | 0 | 0 | 3 | 0 |  |
| Sean McCloskey | 0 | 0 | 3 | 0 |  |
| Syed Jamshed Zaidi | 2 | 7 | 0 | 0 | 2026 Deployment Daily Scrum |
| Matthew Heid | 2 | 6 | 0 | 0 | 2026 Deployment Daily Scrum |
| Babu Papanna | 1 | 1 | 1 | 0 | entroCIM Daily Stand Up, Quest Migration Weekly Check-In |

Owns: named owner of a live Pulse issue. Involved: named in the evidence with a statement, commitment or stated role, not the owner. Delegated/awaited: open register items they own. Sole holder: knowledge areas they hold without a confirmed backup.

## 2026 Deployment Daily Scrum

Governance: Project management. Owner: Chad Steger. Live 18, new this week 6, stuck 4, quiet 1. Last sighting: 2026-11-12. Last evidence: 2026-11-12.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P015 | Panama HVAC points increase continuously; BACnet setup failed, Modbus option untested | Wesco Warehouse | Matthew Heid; Scott Dunn | High | 2026-10-13 | 2026-11-04 | 4 | stuck, customer-visible |
| P007 | PC1/JCI large-scale point faults and intermittent site access | Dell | Scott Dunn | High | 2026-09-15 | 2026-11-05 | 5 | stuck, customer-visible, escalated to W099 |
| P066 | Argentina: watchdog connectors flapping connected/disconnected within a minute, source unidentified |  | Matthew Heid | High | 2026-10-22 | 2026-11-05 | 2 | stuck, customer-visible |
| P004 | Dell visualization scope unsettled: point pages only, or basic graphics and floor plans (El Dorado) | Dell |  | Medium | 2026-10-15 | 2026-11-05 | 3 | stuck, customer-visible |
| P107 | Limerick failure-condition alarm validation method undefined before telling Dell the release is approved | Dell |  | High | 2026-10-28 | 2026-11-03 | 3 | customer-visible |
| P108 | El Dorado end-to-end alarm validation needs customer/site participation; approach not yet defined | Dell | Syed Jamshed Zaidi | High | 2026-10-28 | 2026-11-05 | 2 | customer-visible |
| P116 | Palo Alto NetBot found outside the earlier non-DC scope: new integration needed, device credentials unconfirmed | Dell |  | High | 2026-10-29 | 2026-11-05 | 2 | customer-visible |
| P131 | Merck entroCIM license maintenance substantially overdue; remote access may have lapsed | Merck |  | High | 2026-11-04 | 2026-11-05 | 2 | customer-visible |
| P135 | Dell HQ display/alarm issue: new alarms not showing, blocking a Penang production rollout | Dell |  | High | 2026-11-03 | 2026-11-05 | 2 | customer-visible |
| P142 | Dell questioning redundancy/DR architecture and reuse of existing licenses for DR | Dell | Syed Jamshed Zaidi | High | 2026-11-04 | 2026-11-10 | 2 | customer-visible |
| P145 | Dell IT proposing to remove redundant license servers; no confirmed internal rationale for the current design | Dell |  | High | 2026-11-04 | 2026-11-10 | 2 | customer-visible |
| P174 | Some Modbus "people counter" points have produced no data since April, at a site Copilot transcribed as "Louv" |  | Chad Steger | High | 2026-11-11 | 2026-11-11 | 1 | customer-visible, candidate: stuck |
| P168 | PME upgrade did not complete on schedule; blocked by a cybersecurity control |  |  | High | 2026-11-10 | 2026-11-12 | 3 | customer-visible |
| P173 | Coca-Cola (TCCC) gateway IPs are configured but not pingable, blocking remaining gateway connectivity | Coca-Cola (TCCC) | Chad Steger | High | 2026-11-11 | 2026-11-12 | 2 | customer-visible |
| P087 | entroCIM refresh hanging for some time while Babu C. Dinesh was away |  |  | Medium | 2026-10-27 | 2026-11-03 | 3 |  |
| P176 | A site transcribed as "Govardhan" may have an overloaded server with 771 Modbus connectors, preventing validation |  |  | Medium | 2026-11-12 | 2026-11-12 | 1 | candidate: gap |
| P177 | Mobile-device data flow is blocked by a firewall owned by a team outside this forum |  |  | Medium | 2026-11-12 | 2026-11-12 | 1 | candidate: boundary |
| P178 | WEML rendering/alarming work has an unresolved billing question: whether it should be a separate PO |  |  | Medium | 2026-11-12 | 2026-11-12 | 1 | customer-visible, candidate: boundary |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P012 Dell FTE Franklin tracker: categorize items for Scott Dunn review.

## entroCIM Daily Stand Up

Governance: Sprint (2-week). Owner: Ron Snyder. Live 9, new this week 6, stuck 1, quiet 1. Last sighting: 2026-11-12. Last evidence: 2026-11-12.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P018 | Test server has no VPN connectivity to the private artifact repository (containerization) |  | Babu Papanna | Medium | 2026-10-14 | 2026-11-04 | 5 | stuck |
| P137 | Prior Gridboard monorepo migration lost code and broke functionality; migration restarted |  | Nisha More | High | 2026-11-03 | 2026-11-04 | 2 |  |
| P111 | FRB alarm failures lack sufficient logging/data to diagnose why alarms fail to show up | Federal Reserve | Keith Bishop | High | 2026-10-28 | 2026-11-10 | 3 | customer-visible |
| P162 | Hanwa devices 121/123 and Bangalore access devices inaccessible ahead of a demo the following week |  | Ron Snyder | High | 2026-11-10 | 2026-11-10 | 1 | customer-visible |
| P169 | Keith Bishop flags the next 8 working days of sprint scope (Dell query, SkySpark 4 rebuild, Ford SFTP work) as infeasible |  |  | High | 2026-11-10 | 2026-11-10 | 1 | customer-visible |
| P186 | Federal Reserve environment blocks Internet-hosted font/dependency access, requiring an offline packaging or fallback strategy | Federal Reserve |  | High | 2026-11-11 | 2026-11-11 | 1 | customer-visible, candidate: boundary |
| P187 | Ford Rouge requires new points added before December 1 on a newly received tool, consuming allocated SME hours | Ford | Jason Ganiatsas | Medium | 2026-11-11 | 2026-11-11 | 1 | customer-visible, candidate: boundary |
| P189 | Innovation Center Lab's unreliability (Bright Layer device unavailable) is blocking containerization/device work |  | Ron Snyder | Medium | 2026-11-12 | 2026-11-12 | 1 | candidate: boundary |
| P188 | Version information for existing customer/platform versions is not maintained in any single, actively managed inventory |  |  | Low | 2026-11-11 | 2026-11-11 | 1 | candidate: gap |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P042 entroCIM 3.1.12.14 customer release notice one day behind the stated date (Chad out sick 10-19).

## entroCIM Backlog Deep Dive

Governance: Sprint / backlog. Owner: David Blondel. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: 2026-11-03. Last evidence: 2026-11-03.

No issues in the Pulse yet.

## Quest Migration Weekly Check-In

Governance: Project management. Owner: Chad Steger. Live 7, new this week 2, stuck 5, quiet 0. Last sighting: 2026-11-10. Last evidence: 2026-11-10.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P049 | Azure conductor still set up for high availability; primary-role turnover not yet switched |  | Shawn Clark | High | 2026-10-20 | 2026-11-03 | 3 | stuck |
| P050 | Libro may fail through the new conductor pending an outbound-IP or relay configuration change |  | Shawn Clark | High | 2026-10-20 | 2026-11-03 | 4 | stuck, customer-visible |
| P047 | Azure BLOB Storage accessible via browser but not through the required Linux command-line transfer path |  | Shawn Clark | High | 2026-10-20 | 2026-11-10 | 5 | stuck |
| P048 | MQTT cutover blocked pending DNS records and ports 1883/8883 |  | Chad Steger | High | 2026-10-20 | 2026-11-10 | 5 | stuck, customer-visible |
| P052 | Workbench/BACnet Pro has no confirmed shared remote-access model after LogMeIn retirement |  | Chad Steger | Medium | 2026-10-20 | 2026-11-10 | 4 | stuck |
| P180 | Quest migration: Nextcloud recovery is complicated by 500 GB-1 TB of encrypted volume and an LDAP dependency on a domain controller slated for removal |  | Chad Steger | High | 2026-11-10 | 2026-11-10 | 1 | candidate: asked |
| P182 | Quest migration: old servers believed stopped unexpectedly appeared to still be running |  |  | Medium | 2026-11-10 | 2026-11-10 | 1 | candidate: gap |

## WAM Product Backlog Refinement

Governance: Sprint. Owner: Sakshi Mathur. Live 2, new this week 0, stuck 0, quiet 0. Last sighting: 2026-11-04. Last evidence: 2026-11-04.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P159 | WAM Exact-supplier renewal notifications are not being sent; blocked on a custom-field enablement |  |  | High | 2026-11-02 | 2026-11-02 | 1 | customer-visible |
| P068 | WAM renewal recommendation feature: quality rejected, rework from start |  |  | Medium | 2026-10-23 | 2026-11-04 | 3 |  |

## WAM Sprint Review

Governance: Sprint. Owner: Sakshi Mathur. Live 2, new this week 0, stuck 1, quiet 1. Last sighting: 2026-11-02. Last evidence: 2026-11-02.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P022 | Missing EUDM shipping dates and country-code mapping block WAM data-enrichment completion |  |  | High | 2026-10-13 | 2026-10-27 | 3 | stuck, customer-visible |
| P094 | WAM critical security vulnerabilities remain open past the team's intended close date |  |  | High | 2026-10-27 | 2026-11-02 | 2 |  |

Quiet (no sighting in 14+ days; confirm with the team whether resolved): P021 EUDM truncates manufacturer part numbers over 15 characters, causing ADM data loss.

## WAM Product discussion

Governance: Product execution. Owner: Akansh Gangil. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: 2026-10-22. Last evidence: 2026-10-22 (none in the window).

No issues in the Pulse yet.

## ADM connect with Natalie

Governance: Product execution. Owner: Akansh Gangil. Live 1, new this week 0, stuck 0, quiet 0. Last sighting: 2026-11-04. Last evidence: 2026-11-04.

| ID | Issue | Account | Owner | Severity | First seen | Last seen | Seen | Flags |
|---|---|---|---|---|---|---|---|---|
| P114 | Exact renewals cannot reliably identify end users from current data; no path to obtain it except possibly integrators |  |  | High | 2026-10-28 | 2026-11-02 | 2 | customer-visible |

## Product Team / Platform Team connect

Governance: Team practice. Owner: Keyur Patel. Live 0, new this week 0, stuck 0, quiet 0. Last sighting: none in the Pulse yet. Last evidence: 2026-11-11.

No issues in the Pulse yet.
