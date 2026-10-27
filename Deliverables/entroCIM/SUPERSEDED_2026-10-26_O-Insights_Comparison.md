> **SUPERSEDED 2026-10-26, same day.** Darryl: keep the comparison in Excel so the vendor's context is not lost and columns can be added, and scope it to understanding the competitor and educating Supplier Relations; Wesco's own business choices are not in scope. The live deliverable is `2026-10-26_O-Insights_Comparison.xlsx`. This narrative is retained for the row-by-row reasoning only; its 'Why this matters' and 'Recommendation' sections (distribution framing, D098 as originally written) are withdrawn.

# O-Insights Core, SkySpark and entroCIM Comparison

> Draft for team validation, 2026-10-26. Built from the vendor's feature comparison workbook and the Copilot notes of the vendor demo, both shared by Jarrod Booth (Supplier Relations). The vendor's two columns are kept as written. The entroCIM column is stated firmly from the product record so that each cell can be confirmed or corrected; cells marked **Validate** name who should answer.

::: {custom-style="Bottom Line"}
**Bottom line:** the vendor's comparison establishes less than it appears to. Eleven of its twenty rows rate SkySpark "Not Verified," including every row where O-Insights claims a functional advantage, and three of the claimed advantages are roadmap items. Measured against entroCIM rather than bare SkySpark, most claimed advantages are parity. Four are real differences worth a closer look: 3D visualization, historical playback, live video in the operator interface (with the Milestone connector), and a visual low-code fault-rule builder. None of them changes the platform under entroCIM. They inform how Wesco answers Supplier Relations on whether to carry O-Insights, and what the entroCIM roadmap could borrow.
:::

## Why this matters

Jarrod Booth asked that O-Insights be considered for two reasons: it is reported to be much less expensive than SkyFoundry, and it has a connector to Milestone, a Wesco supplier in security video. Two different questions sit inside that ask and need separate answers.

1. **Could O-Insights replace SkySpark under entroCIM?** No. The entroCIM application layer, data model and analytics are built on SkySpark, Axon and Haystack. Replacing the foundation is a rebuild of entroCIM, not a license swap, and 2027 development capacity is reduced. The price comparison with SkyFoundry is therefore not the decision it looks like.
2. **Should Wesco carry O-Insights as a distributed product alongside entroCIM, or decline it?** This is the live question. It is a Supplier Relations and portfolio decision, not a technical one. This document is the technical input to it: where O-Insights overlaps entroCIM (channel conflict), where it adds something entroCIM does not offer, and where its claims are unverified.

## How to read the vendor document

- **Vendor-authored.** Twenty criteria in four groups (Functional, Architecture, Integration, Security), with columns for O-Insights Core, SkySpark, and "Advantages of Core." The company behind it is named only once, as "CTS," in the ISO 27001 line. No company profile, install base or references are in the material.
- **The SkySpark column is unverified where it matters.** "Not Verified" appears on 11 of 20 rows. Every row that claims an O-Insights functional advantage is one where SkySpark was not checked. The parity calls (operating systems, high availability, cloud and on-premises, protocols, authentication, audit, encryption) are fair. The advantage calls are assertions about O-Insights, not comparisons.
- **Roadmap scored as advantage.** Asset Manager, Predictive Maintenance and Genie AI are marked "On Road map" and then written up under "Advantages of Core."
- **One factual gap.** SkySpark's AI capability is rated "Not Verified." SkyFoundry shipped Woolly in beta in July 2026 (build 4.0.6) and in October 2026 added plan mode, custom LLM providers and background agents (build 4.0.7). The vendor's roadmap assistant is competing with a shipped product.
- **The product was pre-release at the demo.** The team stated a mid-July readiness target, pricing to follow by email, MQTT in the initial release, and BACnet, OPC UA and SNMP targeted for the end of September. The workbook lists those protocols as Available. Whether they shipped is unconfirmed.

## Summary table

Reads: **Parity**, **O-Insights ahead**, **entroCIM ahead**, **Both roadmap**, **Validate** (cannot be settled from the record). Detail and evidence for each row follow the table.

| # | Criterion | O-Insights claim (vendor) | entroCIM today | Read |
|--|------------|-------------|-------------|------|
| 1 | Dashboards and visualization | Eight packaged domain dashboards, GIS map view, hierarchy drill-down, cross-site comparison | Tiles and Gridboard dashboards, Graphics Builder, multi-site views, floor plans from CAD, site/building/floor/space hierarchy | Parity in substance. Packaged domain dashboards and GIS map: Validate |
| 2 | Reporting and scheduled exports | Six packaged report types, scheduled, branded | Reports and historian data; scheduled branded report packages: Validate | Parity, pending validation |
| 3 | Fault detection and diagnostics | Visual low-code workflow builder, equipment templates, 11-technique library, staged diagnosis (observation, cause, impact, recommendation) | Rules on the SkySpark analytics engine, Commissioning FDD app, fault and alarm logic; authoring in Axon, the Rule app, and Woolly | Parity on capability; different authoring experience. O-Insights ahead on the visual builder if the demo reflects the shipped product |
| 4 | Alarm Manager | Unified console, multi-level escalation, email, SMS and WhatsApp | Alarms and notifications delivered in every deployment; escalation tiers and channels: Validate | Parity likely; escalation channels Validate |
| 5 | Asset Manager | Roadmap: CMMS, work orders, QR codes, inventory, rosters | Not in entroCIM by design: WAM owns asset lifecycle, Navigator owns work orders, ServiceNow and TRIRIGA by integration | Portfolio answer, not a gap |
| 6 | Predictive maintenance | Roadmap: AI/ML health scoring, remaining useful life | Impact Analysis planned (2027); entroCIM AI on Woolly, Q1 2027 | Both roadmap |
| 7 | Agentic AI assistant | Roadmap; demo showed a working conversational query tool | Woolly shipped by SkyFoundry (plan mode, custom providers, background agents); entroCIM AI launch Q1 2027 with entroCIM 4 | SkySpark and entroCIM ahead |
| 8 | 3D visualization | Available; demoed with sensor placement and floor navigation | Not supported: static image of a 3D space and CAD floor plans; no BIM or COBie | O-Insights ahead |
| 9 | Historical playback | Available; demoed, exports to video | No equivalent on record | O-Insights ahead; Validate |
| 10 | IP camera video | Live view, alarm-linked video, recorded playback; Milestone connector (reported by Jarrod) | Hanwha and Axis connectors in production for device data; no live video in the interface | O-Insights ahead on video in the interface; Validate what the camera connectors present |
| 11 | Operating system support | Windows services; Linux as K3s containers | Windows and Linux; containerized with entroCIM 4 (Q1 2027) | Parity |
| 12 | Commissioning | Bulk configuration of points, alarms, histories | Connector Upload app, Batch Point Writer, SkySpark 4 Point Mapper; Site Readiness app planned | Parity; bulk alarm and history configuration: Validate |
| 13 | Tag support | Brick, Haystack, custom | Haystack, Xeto (Haystack 5), custom; Brick not supported | Parity; Brick is marginal |
| 14 | High availability and DR | Multi-node K3s | SkySpark clustering and replicas, Arcbeam; Azure hosting | Parity; HA pattern per deployment: Validate |
| 15 | Cloud and on-premises | Both; white-label cloud | Wesco-hosted Azure, on-premises, edge; Airwall for remote connectivity | Parity; entroCIM has a hosted managed option |
| 16 | Protocols | MQTT, BACnet (BBMD, BACnet/SC), OPC UA, SNMP, webhooks, REST, ICMP; no Modbus listed | BACnet, Modbus, OPC UA, SNMP, MQTT, SQL, REST, oBIX, Sedona, plus entroCIM connectors (Hanwha, Axis, Sensolus, RF Code, AMI, SafeTrust, Panduit) | entroCIM ahead today; O-Insights BACnet, OPC UA and SNMP release status unconfirmed; BACnet/SC on SkySpark: Validate |
| 17 | Authentication, SSO, MFA, LDAP | Password, MFA, LDAP; SSO "subject to implementation and configuration" | SAML SSO in production for Wesco and customers; LDAP and MFA | Parity; entroCIM's SSO is proven, theirs conditional |
| 18 | Role-based access control | Custom roles, granular permissions by module | SkySpark base roles (superuser, admin, operator); entroCIM application-level permissions: Validate | Validate; possible O-Insights advantage |
| 19 | Audit trail | Audit trail | Audit trail | Parity |
| 20 | Encryption and compliance | TLS; CTS holds ISO/IEC 27001:2022 | TLS; Wesco holds corporate ISO 27001 and CMMC; no entroCIM-scoped attestation published | Parity in kind: both are corporate certifications, neither is product-scoped |

::: {custom-style="Source Note"}
**Source:** vendor workbook "O-insights Software Comparison" (sheet Feature Comparison, 20 rows) and Copilot demo notes, both via Jarrod Booth; entroCIM positions from the product record as of 2026-10-26 (release 3.1.12.14 shipped; SkyFoundry build 4.0.7 release notes of 2026-10-23; FRBNY bid positions of 2026-10-20). "Reported" marks statements relayed by Jarrod that are not in the vendor material.
:::

## Row-by-row detail

**1. Dashboards and visualization.** The vendor lists eight packaged dashboards (energy, comfort, facility management, maintenance, utility, IAQ, space management, alarms), a GIS map with site status, a configurable hierarchy from portfolio to asset, and drill-down from map to point. The demo showed the map view, site and building drill-down, and reusable widget templates. entroCIM covers the same ground with Tiles and Gridboard, Graphics Builder, multi-site views and floor-plan navigation built from CAD, with the hierarchy carried by the Haystack model. Where entroCIM is less packaged is domain-specific out-of-the-box dashboards; much of that is delivered as project configuration. **Validate (David Blondel):** which domain dashboards ship as standard content, and whether a GIS or map-based portfolio view is standard.

**2. Reporting and scheduled exports.** Six packaged report types with scheduling and branded templates. entroCIM has reporting on historian data; the question is packaging and scheduling, not capability. **Validate (David Blondel):** scheduled, branded report packages as standard content.

**3. Fault detection and diagnostics.** This is the vendor's strongest functional story and the demo supported it: a fault dashboard, staged diagnosis (symptoms, causes, impact, recommendation), and a visual block editor for building rules from templates. The vendor's own SkySpark column concedes the substance: Axon rules, sparks, a Rule app with ready algorithms, reusable equipment-oriented analytics, timelines, cost analysis and custom functions. entroCIM adds the Commissioning FDD app and packaged fault and alarm logic, and with SkySpark 4 Woolly can write rules from natural language. The real difference is the authoring experience: a drag-and-drop workflow with templates versus rule configuration and scripting. That matters for a customer who self-configures; it matters less where Wesco delivers and maintains the rules. **Validate (Keith Bishop):** whether entroCIM presents a staged diagnosis per fault (observation, probable cause, impact, recommendation) or a spark with configured context, and how far the Rule app closes the no-code gap.

**4. Alarm Manager.** Unified console, classification, filtering, acknowledgment, lifecycle tracking, multi-level escalation of unacknowledged alarms, and notifications by email, SMS and WhatsApp. Alarms and notifications are standard in every entroCIM deployment and are inside the support scope. **Validate (David Blondel, Chad Steger):** time-based multi-level escalation and the notification channels entroCIM offers today (email is assumed; SMS and WhatsApp are not).

**5. Asset Manager (roadmap).** A full CMMS: asset register, preventive maintenance, work orders, QR codes, mobile checklists, inventory, shift rosters, condition-based tickets from FDD. entroCIM does not do this, and the portfolio does not want it to: WAM owns asset lifecycle and commercial intelligence, Navigator owns work orders and field operations, and ServiceNow and TRIRIGA are reached by integration. A single-vendor closed loop is a fair pitch for a small operator; it is not a gap in the Wesco portfolio.

**6. Predictive maintenance (roadmap).** Health scoring, failure probability, remaining useful life, through "Gyan AI/ML models." Nothing demonstrable. entroCIM's equivalents are also roadmap: Impact Analysis (2027) and the entroCIM AI layer on Woolly. Both roadmap; no basis to rank.

**7. Agentic AI assistant (roadmap).** The demo showed a conversational tool answering counts and lists and drawing a pie chart, plus a help assistant. The vendor rates SkySpark "Not Verified" here, which is the clearest error in the document: Woolly ships inside SkySpark today, with plan and confirm modes, custom LLM providers (any OpenAI-protocol endpoint, including gateways and local models) and event-triggered background agents as of build 4.0.7. entroCIM AI launches on that foundation with entroCIM 4 in Q1 2027. On the record, SkySpark and entroCIM are ahead, not behind.

**8. 3D visualization.** Interactive 3D with orbit, fly, walk and plan modes, equipment placement, live point values. The demo showed it working with converted 3D model files. entroCIM does not support 3D model navigation; it presents a static image of a 3D space and floor-plan navigation from CAD, and it does not create or maintain BIM models or ingest COBie. This is a real difference. How much it is worth depends on demand; it has come up in one current bid as a specification item answered by deviation.

**9. Historical playback.** Replay of historical readings as animated color on a layout, with date range and speed, saved as a video for people without system access. Demoed, and the one feature Jarrod singled out. No entroCIM equivalent is on record; the Graphics Builder animation work on the 2026 roadmap may or may not be the same idea. **Validate (David Blondel):** whether anything in entroCIM or SkySpark does this, and whether it is a small build.

**10. IP camera video.** Live view, camera-to-location mapping, alarm-linked video, recorded playback, unified view with BMS points. Jarrod reports a connector to Milestone (the team's demo notes mention XProtect, Milestone's video management product). entroCIM has Hanwha and Axis connectors in production for device connection and data retrieval, not live video in the operator interface. This is the row with the most Wesco relevance: Milestone is the largest supplier in the WAM/ADM sales figures and sits in the CDA market-feedback work. **Validate (Ron Snyder):** exactly what the Hanwha and Axis connectors present in entroCIM today, and whether a Milestone or XProtect connector has ever been scoped.

**11. Operating system support.** Windows as services; Linux as K3s containers. entroCIM runs on Windows and Linux today and moves to containers with entroCIM 4. Parity. The vendor's Linux path being K3s-only is a constraint on their side, not an advantage.

**12. Commissioning.** Bulk configuration of points, alarms and histories. entroCIM has the Connector Upload app and Batch Point Writer, and SkySpark 4.0.7 adds a Xeto-based Point Mapper; the Site Readiness app is planned. **Validate (Chad Steger):** bulk alarm and history configuration from a single upload, which is the specific claim.

**13. Tag support.** Brick Schema, Haystack and custom tags. entroCIM uses Haystack and Xeto (Haystack 5) with custom tags; Brick is not supported natively. Brick-to-Haystack mapping is a known exercise and customer demand for Brick in the Wesco base is not evidenced. Marginal.

**14. High availability and disaster recovery.** Multi-node K3s HA on their side; SkySpark clustering, replicas and Arcbeam on ours, plus Azure hosting for Wesco-hosted customers. The vendor calls this parity and that is right. **Validate (Ron Snyder, Chad Steger):** the HA pattern Wesco actually deploys on hosted and on-premises instances, so the claim can be stated per deployment type.

**15. Cloud and on-premises.** Both offer both. The vendor adds white-label cloud hosting under a customer's brand. entroCIM offers Wesco-hosted Azure instances with Airwall secure connectivity, on-premises, and edge. Parity; the Wesco-hosted option is itself a managed service, which the vendor does not claim.

**16. Protocols.** The vendor lists MQTT, BACnet (with BBMD and BACnet/SC), OPC UA, SNMP, webhooks, REST and ICMP, "subject to the availability and implementation status of individual protocol connectors," and does not list Modbus. At the demo only MQTT was in the initial release; BACnet, OPC UA and SNMP were end-of-September targets. entroCIM, through SkySpark and its own connectors, covers BACnet, Modbus, OPC UA, SNMP, MQTT, SQL, REST, oBIX and Sedona, plus Hanwha, Axis, Sensolus, RF Code, AMI, SafeTrust and Panduit. entroCIM is ahead today, and Modbus absence matters for data-center and metering work. **Validate (Ron Snyder):** BACnet/SC support in the SkySpark version entroCIM runs, which is the one specific claim in this row.

**17. Authentication.** Password, MFA and LDAP; SSO via SAML, OAuth or OpenID Connect "subject to implementation and configuration." entroCIM runs SAML SSO in production for Wesco and for customers, with LDAP and MFA from the platform. Parity in list; entroCIM's SSO is proven in production and theirs is conditional.

**18. Role-based access control.** Custom roles with granular permissions across modules, against SkySpark's three base roles. The vendor's SkySpark description is accurate for the platform's built-in roles. entroCIM applications sit above that. **Validate (Ron Snyder):** whether entroCIM exposes custom roles or module-level permissions beyond the SkySpark roles. If not, this is a real, if narrow, O-Insights advantage.

**19. Audit trail.** Both maintain one. Parity.

**20. Encryption and compliance.** Both use TLS. The vendor's differentiator is that CTS holds ISO/IEC 27001:2022. Wesco holds corporate ISO 27001 and CMMC. Neither side offers a product-scoped attestation (SOC 2 or equivalent) in this material. Parity in kind. The entroCIM gap already on record is the absence of a published platform-scoped attestation, and nothing in the vendor document closes or widens it.

## What the demo adds

The demo notes support rows 1, 3, 4, 7, 8 and 9 as working software, on a rental-property portfolio fed by IoT sensors over MQTT. Three points from the notes are not in the workbook and matter:

- The product was pre-release (mid-July readiness target) and the building-automation protocols were later targets. The workbook's "Available" column should be read as of a date the vendor has not given.
- The platform is offered cloud-hosted and white-labeled under a customer's own brand, which is the shape of a distribution or OEM offer rather than a direct sale.
- The group discussed sales collateral and sales-team awareness, which suggests the conversation on the Wesco side was already framed as carrying the product, not evaluating it.

## Commercial and strategic read

- **Price.** "Much less expensive than SkyFoundry" is reported, not quantified; pricing was to follow by email and is not in the material. A lower-priced analytics platform does not lower entroCIM's cost unless entroCIM is rebuilt on it, which is not on the table. The comparison that would matter is O-Insights list price against entroCIM licensing for a comparable site, and that needs the vendor's price list and model (per point, per site, per server).
- **Milestone connector.** This is the angle with real Wesco relevance and the one entroCIM cannot match today. If security-video customers want building data beside video, either O-Insights serves them or entroCIM gains a Milestone connector. Which of those is right depends on what the connector does, which is not stated, and on whether those customers are entroCIM's buyers.
- **Maturity and references.** No install base, references, company profile or release history are in the material. The vendor was pre-release at the demo.
- **Overlap.** O-Insights Core overlaps entroCIM's core: dashboards, alarms, FDD, reporting, playback-style visualization, hosted delivery. A lower-priced product with that overlap in the same sales channel competes for the same sales attention and the same customers.
- **What entroCIM could borrow.** Historical playback, a visual rule builder, time-based alarm escalation with more channels, and video in the operator interface are each small to moderate, and each has shown up in customer or sales conversations. They are roadmap inputs for entroCIM 4 planning, not commitments.

## Recommendation

1. **Do not position O-Insights as an alternative to SkySpark for entroCIM.** The platform question is settled by architecture and capacity, and the price comparison with SkyFoundry is not the decision.
2. **Treat the Supplier Relations ask as a distribution question and answer it on that basis.** The position to give: O-Insights overlaps entroCIM's core, most of its claimed advantages against SkySpark are unverified, three are roadmap, and the four real differences (3D, playback, video with Milestone, visual rule builder) are features, not a platform case. Carrying it would put an overlapping, lower-priced product into the same channel as entroCIM. Before any further step, Wesco needs the price list and model, release status of the building-automation protocols, references, the Milestone connector specification, and security documentation.
3. **Validate the cells marked above before this leaves the team**, then decide whether to add playback, the visual rule builder, escalation channels and a Milestone connector to the entroCIM 4 roadmap discussion.

## Validation asks for the team

| Row | Question | Who |
|--|------------|----|
| 1, 2 | Which domain dashboards and scheduled report packages ship as standard content; is there a map-based portfolio view | David Blondel |
| 3 | Does entroCIM present staged diagnosis per fault; how far does the Rule app close the no-code gap | Keith Bishop |
| 4 | Multi-level, time-based escalation and the notification channels available today | David Blondel, Chad Steger |
| 9 | Any equivalent to historical playback; effort if not | David Blondel |
| 10 | What the Hanwha and Axis connectors present; whether a Milestone or XProtect connector has been scoped | Ron Snyder |
| 12 | Bulk alarm and history configuration from one upload | Chad Steger |
| 14 | HA pattern deployed on hosted and on-premises instances | Ron Snyder, Chad Steger |
| 16 | BACnet/SC support in the SkySpark version entroCIM runs | Ron Snyder |
| 18 | Custom roles or module-level permissions in entroCIM beyond the SkySpark roles | Ron Snyder |

## Information to request from the vendor

Price list and licensing model; release status and dates for BACnet, OPC UA, SNMP and Modbus; install base and references; the Milestone connector specification (XProtect versions, what it reads and writes); the security documentation behind the ISO 27001 claim and any product-scoped attestation; a company profile for CTS; and the terms of the white-label or distribution offer.

---

Editorial choices: the vendor's long cell text is summarized in the table and quoted only where the wording matters; the full text is in the source workbook. Register and file references are left out so the document can go to the team as is. The note to Jarrod Booth is not drafted here.
