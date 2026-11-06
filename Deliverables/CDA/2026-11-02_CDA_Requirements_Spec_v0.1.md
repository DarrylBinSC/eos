---
toc: true
---

# CDA Requirements Spec v0.1

## Status and purpose

| | |
|----------|--------------------------------|
| Version | 0.1, working draft |
| Date | 2026-11-02 |
| Status | Reviewed by Ron Snyder on first read; his answers to section 10 not yet captured |
| Audience | Ron Snyder and David Blondel, for the 2027 entroCIM roadmap reconciliation |
| Purpose | Give Ron a structure to correct, size and challenge, and separate what the entroCIM team can validate today from what depends on Nozomi |

::: {custom-style="Bottom Line"}
**The Phase 1 test.** A row is P0 only if cutting it breaks the first-site promise: devices discovered and recorded, health and firmware posture visible, Guardian findings surfaced against devices, an operator queue with evidence, and a monthly customer report.
:::

How to read the requirement tables:

| Column | Values | Meaning |
|--------|------------------|--------------------------|
| Depends on | [entroCIM] | The current platform; Ron can validate it |
| | [Nozomi] | Guardian, Nozomi APIs, MSP licensing or training; an assumption, not a requirement |
| | [Mixed] | Both, with the split stated in the cell; size the entroCIM part, park the Nozomi part |
| Reuse | Existing, Extension, Net-new, [Ron to confirm] | In production today; existing component needs work; built from scratch; Ron to place it |
| Priority | P0, P1, P2 | Phase 1 (the set Ron sizes); Phase 2; beyond Phase 2 |
| | Assumption, gates Phase n | A Nozomi dependency, sized once answered; tracked in section 6 |
| | Constraint, Document, Reference | Not build items |
| Source | Short name | A document in the CDA product record; full titles in section 12 |

IDs DI‑04, RP‑02 and DP‑07 were retired when their content was folded into DI‑01, RP‑01 and CY‑03; the gaps are deliberate. Where a source is silent, the text says [Not in source; Darryl to confirm].

## Problem statement and buyer

Devices Wesco sells (cameras first, then access control, IoT and OT devices, data center auxiliary systems, and IT devices reachable by SNMP) drift out of support, license and cyber compliance after the sale, and nobody is accountable for them. The VMS reports a camera offline; it does not report that the camera is past life cycle, out of license, short of capacity, or carrying a known vulnerability, and it covers only its own scope. Bill Muczko's estimate, directional only: around 85 percent of his account base is not managing camera assets effectively, and those that monitor use spreadsheets [Product record, Commercial Position].

The buyer is the security, facility or IT/OT leader accountable for device risk at a multi-site enterprise; the Wesco seller is a non-technical account owner whose one-sentence pitch is "we keep an eye on the devices you already bought" [Product record 2026-10-02 positioning]. The customer buys a per-site annual managed service, not a tool it must staff [Deep Dive §2.1; Product record 2026-09-29].

## Users and roles

| Role | What they need from the product |
|------------|----------------------------|
| Customer site or security operator | Posture, activity and service reports; approval of changes; evidence they can hand to audit; no tooling to run [Deep Dive §2.1; Business Case, Solution Analysis] |
| Wesco delivery (install and commissioning) | A repeatable site onboarding: node provisioning, connectivity, discovery, device reconciliation, coverage activation [Business Case, In Scope, service node] |
| Wesco operations center (ongoing service) | A prioritized work queue, device identity bound to WAM, diagnostic and pre-approved recovery actions, evidence capture, field work packages [Deep Dive §5.2, 12.2; Product record 2026-10-14] |
| Wesco field partner or TS tier 2 | A complete work package for remediation that cannot be done remotely [Deep Dive §5.2; Product record 2026-10-14] |
| Wesco sales | Refresh, replacement and license-renewal signals from service data; a per-site fee with size and complexity as the only variables [Business Case, In Scope, Manage; Product record 2026-09-29] |

Operating model as stated: a building operations center, a few people in North America, a couple in Europe, the bulk in India, with in-market tier 2 for larger remediation [Product record 2026-10-14, Darryl's words to Matt Powers]. Delivery organization is TS; staffing model not yet designed [Risk Log, gate D8; Product record 2026-10-14].

## Goals and non-goals

Goals for Phase 1:

1. A customer buys one per-site annual fee and gets discovery, health, posture and cyber-posture visibility for cameras and SNMP-reachable IT devices, operated by Wesco with evidence.
2. Every Phase 1 capability runs on entroCIM components the team already has or extends, so the build fits a reduced team with no incremental FY27 budget.
3. A new entroCIM component reads Nozomi Guardian's analysis and delivers results from it, with no point-level integration into the entroCIM data model yet.
4. Guardian's inventory drives auto-onboarding, so a new site's devices are created and tagged in CDA with minimal integration work.
5. The interfaces, reports, alarms and KPIs needed to run the service exist as one reusable set on entroCIM's rules and views; FDD rules follow in Phase 2 once a site has produced operating data.
6. CDA opens accounts for entroCIM and pulls through ALM, WAM and refresh.

Basis: goals 1, 2 and 6 from the product record (2026-10-06 AOP outcome, 2026-10-30 story); goals 3, 4 and 5 from Darryl, 2026-11-02; the Guardian MSP arrangement from the product record, 2026-10-30.

Non-goals:

| Non-goal | Reason |
|----------------|------------------------|
| IT device management or an RMM product | SNMP coverage completes the cyber picture; IT already manages these devices. Monitoring yes, managing no [Product record 2026-09-20] |
| Standalone SOC, MDR, threat hunting or incident response | Out of scope across every source; Nozomi provides detection context, Wesco does not operate a SOC [Deep Dive §6.2; Business Case, Out of Scope] |
| Replacing the customer's existing security tooling or enterprise vulnerability management | CDA normalizes findings into Wesco evidence; it does not replace Nozomi or the customer's VM stack [Deep Dive §10.3; Deep Dive §6.2] |
| Product tiers | One packaged service, one fee per site; modules may exist architecturally but never surface in pricing or positioning [Product record 2026-09-29] |
| Module-level pricing, add-ons, per-device pricing | Same decision; tiers are kit sizes, Complex is a connection-difficulty adder [Product record 2026-09-29] |
| Credential rotation, certificate lifecycle, autonomous hardening | Later capabilities; write actions carry the liability and governance work the reduced team cannot absorb in Phase 1 [Deep Dive, Executive Decision; Business Case, Out of Scope] |
| Compliance certification or attestation | Observed evidence only; customer owns risk acceptance [Deep Dive §6.6; Business Case, Out of Scope] |
| 24x7 human response | Business-hours service at launch; premium tier only after economics are proven [Business Case, Out of Scope] |
| Another asset-lifecycle, work-order or generic fleet-management platform | WAM and Navigator exist; integrate, do not duplicate [Deep Dive, Executive Decision, Do not build] |

## Functional requirements

### Device discovery and inventory

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| DI‑01 | Discover connected devices on covered networks and record make, model, firmware version and support status; flag unsupported or unmanaged devices found | [Mixed]: [Nozomi] if Guardian is the discovery source (DI‑05); [entroCIM] for the device record and connector-based discovery | [Ron to confirm] (Axis and Hanwha connectors exist; discovery method for a new site not stated) | P0 | Business Case, In Scope, Identify; Risk Log, manufacturer matrix |
| DI‑02 | Create a device record and reconcile it against Wesco asset data (WAM) with confidence and lineage | [entroCIM] | Extension (WAM integration) | P1 | Business Case, Identify; Deep Dive §8.1 |
| DI‑03 | Identify end-of-support and end-of-life devices; in Phase 1 from a maintained EOL table in CDA, from WAM lifecycle data once DI‑02 ships | [entroCIM] | Extension | P0 | Business Case, Identify; Deep Dive §4.2 |
| DI‑05 | Assumption: Guardian passive discovery supplies endpoint and OT asset inventory to the CDA instance by API, and is the preferred discovery method because passive clears customer security review faster. This inventory is the input to auto-onboarding (AO‑01) | [Nozomi] | Net-new integration | Assumption, gates Phase 1 | Business Case, notes; Architecture view sensor node; Darryl 2026-11-02 |
| DI‑06 | Discover SNMP-reachable IT devices (switches, APs, UPS, PDU) and record identity, version and reachability; monitor only | [Mixed]: [entroCIM] for SNMP polling; [Nozomi] where Guardian identifies these devices passively first | [Ron to confirm] (SNMP connector status in entroCIM not in source) | P0 | Product record 2026-09-20; Deep Dive §11 open devices; Darryl 2026-11-02 |

### Device health and availability

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| HM‑01 | Continuous reachability and device-state checks for covered devices | [entroCIM] | Existing (camera connectors) | P0 | Deep Dive §5.2; Business Case, Monitor |
| HM‑02 | Functional checks where device APIs permit: stream, recording, time, storage, service state | [entroCIM] | Extension | P1 | Deep Dive §5.2 |
| HM‑03 | Detect repeated offline or reboot conditions and correlate into one prioritized incident | [entroCIM] | Extension (rules and alerting) | P0 | Deep Dive §5.2 |
| HM‑04 | Approved low-risk recovery actions: device restart, service restart, PoE cycle, reconnect, under customer policy by device class and criticality | [entroCIM] | [Ron to confirm] (write actions; PoE cycle needs switch integration) | P1 | Deep Dive §5.2 approval model |
| HM‑05 | Root-cause hypothesis and diagnostic component for an incident | [entroCIM] | Net-new | P1 | Deep Dive §5.2 |
| HM‑06 | Failure history written back to WAM per device | [entroCIM] | Extension | P2 (with CN‑05 write) | Deep Dive §5.2; Architecture view |

### Configuration and firmware posture

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| CP‑01 | Collect firmware and software version per device and compare to an approved target-version policy per device family | [entroCIM] | Extension | P0 | Deep Dive §4.2; Business Case, Manage |
| CP‑02 | Correlate vendor advisories and support dates to covered devices | [Mixed]: [Nozomi] for vulnerability and advisory correlation (assumed a Guardian output); [entroCIM] for support and EOL dates from the maintained EOL table (DI‑03), from WAM once DI‑02 ships | [Ron to confirm] (advisory content source not chosen) | P0 | Deep Dive §6.2; Business Case, Identify |
| CP‑03 | Read-only configuration baseline and policy findings; no configuration writes | [entroCIM] | Extension | P1 | Deep Dive §4.2; Deep Dive, Executive Decision |
| CP‑04 | Remote firmware update with compatibility precheck, staged rollout, post-change validation, OEM-supported rollback, evidence; Axis first via VAPIX, Hanwha after qualification | [entroCIM] | Net-new (update state machine on existing framework) | P2 | Deep Dive §4.2, 11.1, 11.2; Business Case, Execute |
| CP‑05 | Firmware source integrity: signature or checksum, model match, prerequisite check before any transfer | [entroCIM] | Net-new | P2 (with CP‑04) | Deep Dive §4.2; Deep Dive §7.7 |

### Cyber posture and anomaly signals

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| CY‑01 | Per-device cyber posture: firmware currency, vulnerability correlation, default or shared-credential indicators, certificate status where available, insecure protocol or service observations | [Mixed]: [entroCIM] for what connectors expose; [Nozomi] for vulnerability and credential indicators | Mixed; [Ron to confirm] which items the Axis and Hanwha connectors expose today | P0 | Deep Dive §6.2 visibility scope |
| CY‑02 | Assumption: Guardian supplies vulnerability correlation, insecure-service observations and anomaly or threat context for covered devices. CDA consumes these through the Nozomi analysis component (NZ‑01 to NZ‑04), not through per-device point integration | [Nozomi] | Net-new integration (see NZ area) | Assumption, gates Phase 1 | Deep Dive §8.1, 10.3; Architecture view; Darryl 2026-11-02 |
| CY‑03 | Assumption: one Guardian instance runs on, or alongside, each CDA service node, container-packaged, under a Wesco MSP license | [Nozomi] | Net-new | Assumption, gates Phase 1 | Product record 2026-10-30; Product record 2026-10-30 open items |
| CY‑04 | Nozomi Arc endpoint sensor on customer serviceable hosts (VMS, badge servers) as a later attach | [Nozomi] | Not built | P2 | Deep Dive §10.3; RMM Review item 4 |
| CY‑05 | Map findings to a practical control framework (NIST and CISA references) without claiming certification | [Mixed]: [Nozomi] if Guardian supplies framework mapping (unverified); otherwise [entroCIM] content | Net-new (content) | P1 | Deep Dive §6.2; Business Case, NFR |
| CY‑06 | Exception register: finding, owner, customer disposition (remediate, accept risk), aging | [entroCIM] | Net-new | P1 | Deep Dive §6.2 |

### Alerting, workflow and service actions

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| AW‑01 | Prioritized service work queue for operations center staff, with SLA, assignment and escalation | [entroCIM] | [Ron to confirm] (entroCIM alerting exists; queue semantics may be net-new) | P0 | Deep Dive §8.1; Business Case, Monitor |
| AW‑02 | Customer approval workflow with recorded authorization; approval expires when target, device list or window changes | [entroCIM] | Net-new | P1 | Deep Dive §4.2; Business Case, Manage |
| AW‑03 | Field work package generation when remote resolution is not possible: device identity, site, diagnosis, parts, dispatch target (integrator tied to the account) | [entroCIM] | Net-new | P1 (manual handoff by the operator in Phase 1) | Deep Dive §5.2; Product record 2026-10-14 Matt Powers |
| AW‑04 | Navigator integration for field work orders and closure | [entroCIM] | Extension; interface must be replaceable | P1 | Architecture view; Risk Log, gate D7; Business Case, Dependencies |
| AW‑05 | Evidence capture per action: source, timestamp, device identity (WAM identity once DI‑02 ships), approval, execution identity, result, final state | [entroCIM] | Net-new (evidence ledger) | P0 | Deep Dive §8.1; Business Case, NFR auditability |

### Reporting and customer-facing views

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| RP‑01 | Customer-facing posture, activity and service report, monthly on a business-hours cadence: coverage, availability, incidents, firmware and support posture, exceptions, refresh candidates, SLA performance | [entroCIM] | Extension (entroCIM views) | P0 | Deep Dive §4.2, 5.2, 6.2 reporting |
| RP‑03 | Lifecycle and refresh recommendations delivered to Wesco Sales, drawn from service data | [entroCIM] | Extension (WAM loop) | P1 | Business Case, Manage; Architecture view |
| RP‑04 | Export of evidence to the customer in a defined format | [entroCIM] | [Ron to confirm] | P1 | Business Case, NFR |
| RP‑05 | Feed customer platforms such as Datadog | [entroCIM] | Not built | P2 | Product record 2026-10-02 (Bob Caprise) |

### Data model and tagging

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| DM‑01 | Device, site, tenant and coverage registry in the Haystack model: customer, site, mode, devices, criticality, service entitlement | [entroCIM] | [Ron to confirm] (how much of this the entroCIM site model already carries) | P0 | Deep Dive §8.1 |
| DM‑02 | Connector and component support matrix: manufacturer, model, API, supported observations and actions, version | [entroCIM] | Net-new | P0 | Deep Dive §8.1 |
| DM‑03 | Points-based sizing: Small 1,000 points, Medium 2,500, Large 5,000; about 25 points per asset; Complex is a connection-difficulty adder | [entroCIM] | Existing (SkySpark licensing model) | Constraint | Product record 2026-09-29 |
| DM‑04 | Source lineage and conflict handling when CDA writes to WAM | [entroCIM] | Extension | P2 (with CN‑05 write) | Deep Dive §7.5 |

### Connectors and integrations

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| CN‑01 | Axis camera connector | [entroCIM] | Existing, in production | P0 | Risk Log, manufacturer matrix (Darryl 08-12) |
| CN‑02 | Hanwha camera connector | [entroCIM] | Existing, in production | P0 | Risk Log, manufacturer matrix (Darryl 08-12) |
| CN‑03 | SNMP connector for IT devices; read-only | [entroCIM] | [Ron to confirm] | P0 | Product record 2026-09-20; Darryl 2026-11-02 |
| CN‑04 | Guardian is integrated through the Nozomi analysis component only (NZ‑01), behind the partner abstraction (NZ‑06); the API exposure assumption is NZ‑04 | [Nozomi] | Design constraint | Constraint | Deep Dive §8.1; Deep Dive §10.3; Darryl 2026-11-02 |
| CN‑05 | WAM integration: read lifecycle, warranty, entitlement, EOL; write health, firmware, failure, refresh signals | [entroCIM] | Extension (Strev platform; WAM roadmap capacity) | P1 read, P2 write | Architecture view; Business Case, Dependencies |
| CN‑06 | Panduit connector (built) and Schneider EcoStruxure (in development) as reference patterns for later device classes | [entroCIM] | Existing / in development | P2 | Product record 2026-09-18 |
| CN‑07 | Cisco Meraki and Catalyst Center API integration | [entroCIM] | Not built | P2 | Deep Dive §11.3 |
| CN‑08 | Access control (HID, dormakaba) via partner tools; assumed reachable without a per-vendor build, not verified | [entroCIM] | Not built | P2 | Product record 2026-09-20; Deep Dive §11.4, 11.5 |
| CN‑09 | New direct manufacturer integration estimated at 8 to 12 weeks each | [entroCIM] | Planning figure | Reference | Product record, What It Is |

### Deployment and commissioning

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| DP‑01 | Containerized service node on a Wesco-supplied small-form-factor Ubuntu PC or customer server, running the entroCIM runtime, connectors and entroCIM components; first node supports 250 or more cameras | [entroCIM] | Existing (CSRA-approved entroCIM Docker work) | P0 | Deep Dive §2.2; Product record, What It Is; Risk Log, gate D3 |
| DP‑02 | Central deployment, as entroCIM is deployed today, for large enterprises or small branches that do not justify an appliance | [entroCIM] | Existing pattern (Dell regional-collector pattern) | P1 | Product record 2026-10-26 correction; Product record 2026-10-02 |
| DP‑03 | Secure remote management of the node over Airwall; Airwall link manages the devices, Arcbeam runs entroCIM instances from the Wesco cloud | [entroCIM] | Existing (Airwall); Arcbeam clustering readiness [Ron to confirm] | P0 | Architecture view validation items |
| DP‑04 | Node fleet management by RMM-class tooling (NinjaOne default candidate): monitoring, patching, scripted staged container pulls from the registry with pre and post health checks and a rollback tag | [entroCIM] | Extension (operating model the team runs today) | P1 (Airwall access and manual patching for the pilot node) | RMM Review recommendation |
| DP‑05 | Air-gapped and restricted-network pattern: offline buffering, degraded operation, safe resumption | [entroCIM] | Existing capability for entroCIM installs; CDA-specific buffering [Ron to confirm] | P0 | Deep Dive §9.1; Business Case, NFR availability |
| DP‑06 | Node hardening to Wesco standards and customer security review support | [entroCIM] | Extension | P0 | Business Case, service node engineering |
| DP‑08 | Operational runbook: provisioning, deployment, monitoring, update, incident response, decommissioning | [entroCIM] | Net-new (document) | Document, Phase 1 | Business Case, service node engineering |
| DP‑09 | Hardware selection and qualification for the service node: specification, sourcing, supported configurations, sizing for 250 or more cameras plus SNMP devices and a co-located Guardian; the chosen unit feeds the pro forma BOM | [Mixed]: [entroCIM] for the node; [Nozomi] for Guardian sizing (N‑3) | Net-new; owner (development or delivery) [Darryl to confirm] | P0 | Business Case, service node engineering; Product record 2026-09-18 (BOM); Darryl 2026-11-02 |
| DP‑10 | Node build and integration: operating system, container runtime, entroCIM runtime and components, Guardian container, RMM agent, Airwall and connectivity components, as one repeatable image | [Mixed]: [entroCIM] build; [Nozomi] for Guardian packaging (CY‑03) | Net-new | P0 | Business Case, service node engineering; Darryl 2026-11-02 |
| DP‑11 | Container deployment testing: build, staged rollout, update, rollback and recovery validated on the qualified hardware before any customer site, and repeated for every release | [entroCIM] | Net-new (test plan and lab); lab instances come from the BIR | P0 | Business Case, service node engineering; Deep Dive §9.1; Darryl 2026-11-02 |
| DP‑12 | Customer network prerequisite for Guardian: a SPAN, TAP or mirror port on the covered segment so the sensor sees device traffic; stated in the site onboarding checklist and the sales qualification | [Mixed]: [Nozomi] for what Guardian needs (N‑9); [entroCIM] for the checklist | Net-new (document and delivery step) | P0 | Deep Dive §7.6; Darryl 2026-11-02 |

### Multi-site and multi-tenant operation

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| MT‑01 | Central services logically multi-tenant with strict partitioning; execution containers dedicated per customer or site | [entroCIM] | [Ron to confirm] (how entroCIM's multi-customer deployments partition today) | P1 (design kept open in Phase 1; single customer) | Deep Dive §7.5; Business Case, NFR |
| MT‑02 | Assumption: Guardian multi-customer terms allow one Wesco MSP console across customer instances with tenant separation | [Nozomi] | Unknown | Assumption, gates Phase 2 | Product record 2026-10-30 open items |
| MT‑03 | Service metering: instance, connector, action, device count, SLA, per tenant | [entroCIM] | Net-new | P1 | Deep Dive §8.1; Business Case, In Scope |
| MT‑04 | Scale from pilot to multi-site, multi-customer without per-customer custom engineering | [entroCIM] | Design constraint | Constraint | Business Case, NFR scalability |

### Security of the platform itself

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| PS‑01 | Least-privilege, segregated credential handling; no shared or embedded credentials; preferred order customer vault, tenant vault, OEM OAuth, break-glass with two-person control | [entroCIM] | [Ron to confirm] | P0 | Deep Dive §7.4; Business Case, NFR; Risk Log, gate D6 |
| PS‑02 | Each credential use tied to tenant, site, device, action and operator identity | [entroCIM] | Net-new | P1 | Deep Dive §7.4 |
| PS‑03 | RBAC, MFA and just-in-time access for remote support | [entroCIM] | [Ron to confirm] | P0 | Deep Dive §7.5 |
| PS‑04 | Product self-assurance: container version, SBOM and vulnerability posture, certificates, heartbeat, connector health, configuration drift | [entroCIM] | Extension (covered partly by DP‑04) | P1 | Deep Dive §9.4 |
| PS‑05 | No action on a customer device without recorded authorization, approved window and pre-change validation | [entroCIM] | Policy; enforced by AW‑02 | Constraint | Business Case, NFR change control |
| PS‑06 | Every northbound channel from the node (Airwall, Arcbeam, RMM, Nozomi) documented in the customer-facing security narrative | [Mixed]: all channels | Document | Document, Phase 1 | RMM Review risk 2 |

### Nozomi analysis component

Darryl's stated goal, 2026-11-02: a new entroCIM component that interfaces with Nozomi, reads in its analysis, and delivers results based on that analysis, without point integration into entroCIM yet. The component is the only place Guardian touches CDA in Phase 1; Guardian findings are consumed as analysis results, not mapped onto entroCIM points.

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| NZ‑01 | A new entroCIM component that connects to a Guardian instance, authenticates, and reads its analysis output (asset inventory, vulnerability assessment, risk and alert data) on a schedule or by event | [Mixed]: [entroCIM] build; [Nozomi] for what Guardian exposes | Net-new (component on the existing entroCIM framework) | P0 | Darryl 2026-11-02; Deep Dive §8.1 partner abstraction |
| NZ‑02 | The component stores Guardian results as device-level findings keyed to the CDA device record (not as entroCIM points), with source, timestamp, Guardian identifier and confidence | [entroCIM] | Net-new; [Ron to confirm] the storage pattern that avoids the point model | P0 | Darryl 2026-11-02; Deep Dive §6.2 evidence |
| NZ‑03 | The component delivers results: findings to the work queue (AW‑01), posture to the customer report (RP‑01), alarms per the rule set (SX‑02), without any per-device point integration | [entroCIM] | Net-new | P0 | Darryl 2026-11-02 |
| NZ‑04 | Assumption: Guardian's analysis is exposed by API (or exportable) at the device level with stable identifiers, so results can be keyed to CDA device records | [Nozomi] | Unknown | Assumption, gates Phase 1 | Darryl 2026-11-02 |
| NZ‑05 | Point-level integration of Nozomi data into the entroCIM data model (Haystack-tagged points per device) | [entroCIM] | Not built | P2 | Darryl 2026-11-02 ("yet") |
| NZ‑06 | The component is written behind a partner abstraction so a second sensor source could be substituted without changing NZ‑02 or NZ‑03 | [entroCIM] | Design constraint | Constraint | Deep Dive §8.1 |

### Auto-onboarding from Guardian data

Darryl's stated goal, 2026-11-02: use the data a Guardian gathers to create an auto-onboarding function for Wesco's tools, minimizing integration work per site.

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| AO‑01 | From the Guardian inventory (DI‑05), automatically create CDA device records for a new site: identity, vendor, model, firmware, IP, role, protocol, with site and tenant assignment | [Mixed]: [entroCIM] build; [Nozomi] for inventory fields | Net-new; [Ron to confirm] whether entroCIM has any bulk site or device provisioning today | P0 | Darryl 2026-11-02 |
| AO‑02 | Apply Haystack tags and device-class assignment automatically from the Guardian device classification (camera, switch, AP, UPS, access control) using a maintained mapping table | [entroCIM] | Net-new; mapping table is content | P0 | Darryl 2026-11-02; DM‑01 |
| AO‑03 | Where an entroCIM connector exists for the discovered device (Axis, Hanwha, SNMP), auto-configure the connector instance from the inventory record so the device is monitored without manual integration | [entroCIM] | [Ron to confirm] (depends on connector configuration model) | P1 | Darryl 2026-11-02 |
| AO‑04 | Reconcile auto-onboarded records against WAM (DI‑02) and raise an exception for unmatched devices rather than blocking onboarding | [entroCIM] | Extension | P1 | Darryl 2026-11-02; Deep Dive §8.1 |
| AO‑05 | Re-run onboarding on a schedule so devices added or removed at the site appear or are flagged, with a review step before records are retired | [entroCIM] | Net-new | P1 | Darryl 2026-11-02 |
| AO‑06 | Assumption: Guardian inventory carries enough fields (MAC, IP, vendor, model, firmware, device role) at sufficient accuracy to drive onboarding without manual correction for the majority of devices | [Nozomi] | Unknown | Assumption, gates Phase 1 | Darryl 2026-11-02 |

### Service execution: interfaces, reports, alarming, KPIs and FDD rules

Darryl's stated goal, 2026-11-02: the interfaces, reports, alarming, KPIs and FDD rules associated with executing the service. This area collects the rule and view set; RP and AW rows above remain the delivery surfaces.

| ID | Requirement | Depends on | Reuse | Priority | Source |
|-------|---------------------------|-----------|-----------|-------|---------|
| SX‑01 | Operator interface: site and device inventory, posture, incident queue, evidence, onboarding review, one view per role in section 3 | [entroCIM] | Extension (entroCIM views) | P0 | Darryl 2026-11-02; Deep Dive §12.2 |
| SX‑02 | Alarm rule set for the service: device offline, repeated flap, firmware behind policy, EOL or end-of-support reached, new Guardian finding above a severity threshold, Guardian itself unreachable, node health | [Mixed]: [entroCIM] for the rule engine and device alarms; [Nozomi] for the two Guardian-triggered rules | Extension (entroCIM alerting) | P0 | Darryl 2026-11-02; Deep Dive §5.2, 6.2 |
| SX‑03 | FDD rules for device health: patterns that indicate a failing device or a failing dependency (recorder, switch port, PoE budget, storage full, time drift) and produce a diagnosed incident rather than a raw alarm | [entroCIM] | Extension (entroCIM FDD engine); rules are net-new content | P1 | Darryl 2026-11-02; Deep Dive §5.2 |
| SX‑04 | KPI definitions computed from service data. The five FY27 AOP KPIs: device inventory completeness, firmware currency, advisory-to-remediation time (measured as advisory-to-assessment time until remediation actions exist), remote resolution rate (from Phase 2, when recovery actions exist), service evidence completeness. Spec additions: time to detect (MTTD), time to commission a site | [entroCIM] | Extension (entroCIM KPI views) | P0 | Darryl 2026-11-02; Product record, Current State |
| SX‑05 | Report set: customer monthly service report (RP‑01), internal operations report (queue aging, SLA attainment, per-site load), sales refresh signal report (RP‑03) | [entroCIM] | Extension | P0 customer, P1 internal and sales | Darryl 2026-11-02 |
| SX‑06 | Rule, alarm, KPI and report definitions are packaged as a versioned set deployed with the CDA component so every site runs the same service logic | [entroCIM] | [Ron to confirm] (how entroCIM packages rules per deployment today) | P1 | Darryl 2026-11-02; DM‑02 |
| SX‑07 | Customer-facing interface: read-only posture and report access, approval of changes (when AW‑02 ships) | [entroCIM] | Extension | P1 | Deep Dive §2.1 |

## Nozomi dependency register

::: {custom-style="Risk"}
**What we know about Nozomi is thin.** The record holds only public outlines: Guardian is a network sensor, Arc an endpoint sensor, Vantage the analytics layer, and Nozomi runs an MSSP program. Nobody on the team is trained, no API documentation has been reviewed, and there is no lab instance. The 2027 BIR buys exactly those things: MSP enrollment, five lab Guardian instances, four certification seats and onboarding support.
:::

Every Nozomi dependency in the requirement tables, collected here for reuse in the BIR. Entries marked Yes under Blocks P0 must be answered before Phase 1 can be sized.

| Ref | Assumption as currently held | What we need to learn | Who can answer | Blocks P0 |
|------|----------------------|----------------------|-----------|-----|
| N‑1 (DI‑05) | Guardian passive discovery supplies endpoint and OT inventory by API | API coverage: asset fields, polling or push, rate limits, version stability | Nozomi; Ron's team after training | Yes |
| N‑2 (CY‑02, CP‑02, CY‑01) | Guardian supplies vulnerability correlation, insecure-service observations and anomaly context, exportable by API | Which findings are exposed by API versus Vantage UI only; data format; licensing of threat content | Nozomi | Yes |
| N‑3 (CY‑03, DP‑10) | One Guardian per CDA node, container-packaged on a Wesco-owned node | Whether Guardian is licensed as a container on third-party hardware; sizing per node; physical versus virtual sensor | Nozomi | Yes |
| N‑4 (MT‑02) | Multi-customer MSP console with tenant separation | MSP program terms, central management product, per-tenant isolation model | Nozomi MSP program | No (Phase 2; licensing itself is N‑3) |
| N‑5 (CN‑04) | Integration can sit behind a partner abstraction so another sensor could substitute | API semantics stable enough to abstract; export rights on Wesco-collected data | Nozomi; Ron's team | No (design choice) |
| N‑6 (CY‑04) | Arc endpoint sensor on customer hosts is a later attach | Arc licensing and attach terms | Nozomi | No |
| N‑7 (pricing) | Production Guardian licenses scale with sites from 2028 and are recovered in the site fee; placeholder $500 upfront plus $500 annual per instance | Actual MSP unit pricing and volume terms (the largest lever on the CDA fee) | Nozomi; Darryl | No for build, yes for pricing |
| N‑8 (training) | Four certification seats and onboarding support let the entroCIM team build and operate the integration | Training path and time for engineers with no Nozomi experience; support entitlement during build | Nozomi; Ron | Yes |
| N‑9 (network, DP‑12) | Guardian sees enough traffic on the customer segment to discover and profile devices | SPAN or TAP requirement per site; what the customer must provide; effect on the "no customer compute" land motion | Nozomi; TS delivery | Yes |
| N‑10 (NZ‑01, NZ‑04) | Guardian's analysis (vulnerability assessment, risk scores, alerts) is readable by a Wesco-built component at the device level with stable identifiers | Which analysis outputs are available on Guardian versus only in Vantage; API or export format; identifier stability across rescans; polling limits | Nozomi; Ron's team after training | Yes |
| N‑11 (AO‑01, AO‑06, DI‑06) | Guardian inventory fields are rich and accurate enough to auto-create and tag CDA device records | Field list (MAC, IP, vendor, model, firmware, role); classification accuracy for cameras, switches, APs, UPS; how unknown devices are reported | Nozomi; validate in the lab | Yes |
| N‑12 (SX‑02) | Guardian exposes its own health or heartbeat so CDA can alarm when the sensor is down | Whether a health endpoint or status export exists; polling interval | Nozomi; Ron's team after training | Yes |

## Phasing and exit criteria

Dates are owned by the 2027 roadmap reconciliation (Darryl, Ron, David Blondel) and are not set here.

| Phase 1: first site, one customer | Phase 2: second customer, first write actions | Beyond Phase 2 |
|------------------------|------------------------|--------------------|
| Discovery and device records, cameras plus SNMP/IT devices (DI) | WAM integration: reconciliation, lifecycle read (DI‑02, CN‑05, AO‑04) | Point-level Nozomi integration into the entroCIM data model (NZ‑05) |
| Reachability, flap detection, firmware and EOL posture from a maintained table (HM‑01, HM‑03, CP‑01, CP‑02, DI‑03) | Field work packages and Navigator integration (AW‑03, AW‑04) | Firmware execution, Axis first (CP‑04, CP‑05) |
| Nozomi analysis component, findings keyed to device records (NZ‑01 to NZ‑03) | Multi-tenancy and metering (MT‑01, MT‑03) | WAM write-back (CN‑05 write, HM‑06, DM‑04) |
| Auto-onboarding core: records and tags from Guardian inventory (AO‑01, AO‑02) | RMM fleet management and central deployment (DP‑04, DP‑02) | Access control, Cisco and other device classes (CN‑06 to CN‑08) |
| Alarm rules, KPIs, operator interface (SX‑01, SX‑02, SX‑04) | Connector auto-configuration and scheduled re-onboarding (AO‑03, AO‑05) | Arc endpoint attach (CY‑04); feeds to customer platforms (RP‑05) |
| Work queue and evidence record (AW‑01, AW‑05) | Functional health checks, diagnostics, FDD rules (HM‑02, HM‑05, SX‑03) | Credential and certificate work, partner first; 24x7 |
| Customer monthly report (RP‑01, SX‑05 customer part) | Rule-set packaging, configuration baseline, credential identity binding, self-assurance (SX‑06, CP‑03, PS‑02, PS‑04) | |
| Service node: hardware, build, hardening, deployment testing, Airwall management, offline buffering, Guardian network prerequisite (DP‑01, DP‑03, DP‑05, DP‑06, DP‑09 to DP‑12) | First write actions: low-risk recovery under the approval workflow (HM‑04, AW‑02) | |
| Credentials and access (PS‑01, PS‑03); connectors (CN‑01 to CN‑03); support matrix (DM‑02) | Control-framework mapping, exception register, internal and sales reports, customer interface (CY‑05, CY‑06, SX‑05, RP‑03, RP‑04, SX‑07) | |

Run by hand at the Phase 1 pilot, on purpose:

- WAM lookups (EOL and support dates kept in a maintained table)
- Field work packages (operator handoff with the diagnosis in the evidence record)
- Tenant partitioning (one customer)
- Node fleet management (Airwall access and manual patching on one node)
- Connector configuration after onboarding
- FDD tuning and rule-set packaging

Phase 1 has no device write actions and no point-level Nozomi integration.

Phase 1 exit criteria:

- One customer, two to five sites, two camera manufacturers plus SNMP devices under coverage
- A new site onboarded from Guardian inventory with manual correction on a minority of devices
- Every acceptance criterion in section 9 met
- Nozomi items N‑1 to N‑3 and N‑8 to N‑12 resolved, or an explicit decision to ship without Guardian

Phase 2 exit criteria:

- A second customer onboarded without custom engineering
- Write actions proven under the approval model, with evidence, on the Phase 1 estate

## Success metrics

| Metric | Type | Measurable today or needs instrumentation |
|------------------|------|------------------|
| Device inventory completeness (discovered versus customer's known estate) | Product, AOP KPI | Needs instrumentation (DI‑01; DI‑02 from Phase 2) |
| Firmware currency (share of covered devices at approved version) | Product, AOP KPI | Needs instrumentation (CP‑01) |
| Advisory-to-remediation time (advisory-to-assessment in Phase 1) | Product, AOP KPI | Needs instrumentation (CP‑02) |
| Time to detect a device failure (MTTD) | Product, spec addition | Needs instrumentation (HM‑03) |
| Time to commission a site | Product, spec addition | Measurable from delivery records once a site exists |
| Remote resolution rate; truck rolls avoided | Product, AOP KPI | Phase 2, once recovery actions exist |
| Service evidence completeness (actions with full evidence record) | Product, AOP KPI | Needs instrumentation (AW‑05) |
| Sites under contract | Business | Measurable from sales records |
| entroCIM attach (accounts where CDA preceded an entroCIM sale) | Business | Needs a tracking rule in CRM |

The five rows marked AOP KPI are the FY27 AOP Value KPI block [Product record, Current State]; readiness metrics only until a site is in production. MTTD and time to commission are additions from this spec.

## Phase 1 acceptance criteria

1. Given a commissioned node on a covered network, when discovery runs, then every Axis and Hanwha camera and every SNMP-reachable IT device on the covered segment appears in inventory with make, model, firmware version and reachability, and unmanaged or unsupported devices are flagged.
2. Given a covered camera goes offline, when the outage exceeds the configured threshold, then one incident appears in the work queue within the service-level target with device identity, site and last known state, and repeated flaps do not create duplicate incidents.
3. Given a device's firmware version and an approved target policy, when posture is evaluated, then the device is reported as current, behind or unknown, with EOL or end-of-support status from the maintained EOL table.
4. Given Guardian is running and the Nozomi analysis component is connected, when Guardian reports a vulnerability or anomaly on a covered device, then the finding appears against that device in CDA with source, timestamp and confidence, raises an alarm if above the severity threshold, and appears in the customer posture report, with no entroCIM point created for it. If Guardian is not integrated at release, this criterion is replaced by an explicit decision record.
4a. Given a new site with a commissioned Guardian, when auto-onboarding runs, then CDA device records exist for the devices in the Guardian inventory with correct site, device class and Haystack tags, and unclassified devices are listed for review rather than silently dropped. (Connector auto-configuration is a Phase 2 criterion.)
4b. Given the alarm rules are deployed to a site, when a device meets an alarm condition (offline past threshold, repeated flap, firmware behind policy, EOL reached, Guardian finding above threshold), then one alarm is raised per condition and the AOP KPIs measurable in Phase 1 (four of five; remote resolution rate from Phase 2) compute for that site from service data. (FDD patterns and the versioned rule package are Phase 2 criteria.)
5. Given an operator closes an incident, when evidence is recorded, then the record carries source, device identity, operator identity, timestamps, action taken and final state.
6. Given remote resolution is not possible, when the operator closes the incident as escalated, then the evidence record carries the diagnosis and the handoff note so a field package can be assembled by hand without re-entry. (Generated field work packages are a Phase 2 criterion.)
7. Given the Airwall or WAN path is lost, when it returns, then the node has preserved its queue, reports degraded coverage for the gap, and resumes without duplicate records.
8. Given a site is onboarded, when the monthly report is generated, then it shows coverage, availability, posture and exceptions for that site only.
9. Negative: no requirement in Phase 1 writes configuration or firmware to a customer device; any such attempt is blocked and logged.
10. Negative: no credential is stored in WAM, in a container image or visible to a routine operator.

## Questions for Ron

Ordered by how much the answer changes the sizing.

| # | Topic | Question | Rows |
|---|-----------|------------------------------|--------|
| 1 | Discovery and SNMP | How does entroCIM discover devices on a new site today? Is there any SNMP capability in the platform now, and what would an SNMP connector for switches, APs and UPS cost in weeks? | DI‑01, DI‑06, CN‑03 |
| 2 | Write actions | Does the current platform execute any write action against a camera (restart, PoE cycle)? What governance and engineering does the first write action pull in, for Phase 2 sizing? | HM‑04, AW‑02 |
| 3 | Multi-tenancy (Phase 2) | How do today's multi-customer entroCIM deployments partition data, credentials and views? Is tenant isolation at the level the business case promises existing, extension or net-new? | MT‑01 |
| 4 | Queue and evidence | How far does entroCIM alerting get us toward a prioritized queue with SLA and assignment, and an immutable evidence record per action? Both are net-new in the record; confirm or correct. | AW‑01, AW‑05 |
| 5 | Camera connectors | Of the posture items in CY‑01, which does each of the Axis and Hanwha connectors expose today (version, certificate status, local accounts, insecure services)? | CN‑01, CN‑02, CY‑01 |
| 6 | Containerized node | What is the state of the CSRA-approved Docker packaging, and is Arcbeam clustering ready to run entroCIM instances from the Wesco cloud? Flagged for validation with you in July; no recorded answer. | DP‑01, DP‑03 |
| 7 | Node fleet (Phase 2) | Does the team run an RMM today that could manage a fleet of Ubuntu nodes, and does a scripted staged container pull from the Docker Hub registry match how the team updates entroCIM containers now? | DP‑04 |
| 8 | Credentials | How are device credentials handled in current deployments, and what would a vault adapter with per-use identity binding take? | PS‑01, PS‑02 |
| 9 | WAM integration (Phase 2) | What integration exists between entroCIM and WAM today, if any, and who on the WAM side would own the write-back? | CN‑05, DI‑02 |
| 10 | Points and sizing | Does the 25-points-per-asset conversion hold for cameras and SNMP devices, and does the Complex adder change anything in the build? | DM‑03 |
| 11 | Nozomi analysis component | How would you build a component that reads Guardian analysis and stores it as device-level findings without creating entroCIM points? Is there a precedent for non-point data keyed to a device record, and what does the partner abstraction cost? | NZ‑01, NZ‑02, NZ‑06 |
| 12 | Auto-onboarding | Does entroCIM have any bulk site or device provisioning today? Can a connector instance be configured programmatically from an inventory record, and can Haystack tagging be applied from a mapping table? | AO‑01 to AO‑03 |
| 13 | Rule-set packaging | How are alarm, FDD and KPI rules packaged and deployed per site today, and could a versioned CDA rule set ride the same mechanism as the container image? | SX‑02, SX‑03, SX‑06 |
| 14 | Nozomi training | What training and lab time would your team need to integrate a product none of them has used? | N‑8 |
| 15 | Service node | Which hardware has entroCIM shipped on for appliance-style deployments, is there a candidate unit already, and does your team or delivery own hardware qualification and the node image? | DP‑09 to DP‑11 |
| 16 | Phase 1 size | With the above answered, a rough sizing of Phase 1 in team-weeks against the 2027 entroCIM roadmap you and David are reconciling. | All P0 |

## Questions for Darryl

| # | Topic | Question | Rows |
|---|-----------|------------------------------|--------|
| 1 | Firmware execution | Phase 2 or beyond? Phase 1 is read-only on devices by your 2026-11-02 decision. The record carried two readings: the August business case put Axis firmware execution in the 2027 investment; the 2026-10-26 review states launch scope is read-only. | CP‑04, CP‑05 |
| 2 | Ship without Guardian | Does Phase 1 ship if the Nozomi MSP terms or the BIR slip? | Acceptance criterion 4 |
| 3 | Base and Advanced tools | Does the July split still exist internally, or is it one service tool now? Affects how Ron packages the entroCIM components, not pricing. | DP‑10 |
| 4 | Phase 1 customer | Which customer and sites? The pilot definition (one enterprise, two to five sites, sixteen weeks) dates from July, was carried into the August business case, and predates the AOP outcome. | Phase 1 exit criteria |
| 5 | SecuriThings | Evaluate as a device engine behind the Wesco service, which changes the build scope for CP, CY and CN rows, or position against only? | CP, CY, CN |
| 6 | BIR scope | Is the Nozomi register (section 6) the full scope of the BIR, or is the BIR narrower? | Section 6 |
| 7 | Service node owner | Development (Ron) or delivery (Chad) for hardware selection, the node image and deployment testing? The business case assigned it to CSS Platforms IT without naming which. | DP‑09 to DP‑11 |
| 8 | Auto-onboarding target | "Wesco's tools" is read here as CDA device records and connector configuration only, with WAM in Phase 2. Confirm. | AO‑01 |

## Source references

All documents are in the CDA product record, maintained by Darryl, and can be shared on request. None is a decision of record on its own; decisions are noted by date in the Product record.

| Short name used above | Document | Date | What it is and how it was used |
|--|------------|----|--------------------------|
| Start Here | CDA: Start Here | 2026-10-30 | Entry page for the product: current state, working rules, the Nozomi BIR summary |
| Product record [date] | Connected Device Assurance (CDA) product file, dated entry | 2026-08 to 2026-10 | Running record of decisions and positioning: commercial model (2026-09-29), device-class sequencing (2026-09-20), AOP outcome (2026-10-06), TS delivery model (2026-10-14), SecuriThings comparison (2026-10-26), Nozomi scope (2026-10-30) |
| Architecture view | Connected Device Assurance, Solution Structure (Executive View) | 2026-07-27 | Darryl's architecture: service node, partner sensor, Airwall and Arcbeam roles, WAM and Navigator links |
| Deep Dive §n | CSS Platforms 2027 Phase 2 Deep Dive: Connected Device Assurance as a Service | 2026-07-23 | Ideation-stage functional detail: module scope and exclusions, approval models, service levels, cross-module architecture, fleet management, manufacturer qualification. Treated as ideas, not decisions |
| Business Case, section | CDA Wesco Business Case, working document | 2026-07-28 to 2026-08-18 | Scope, nonfunctional requirements, out-of-scope list and dependencies as written for the FY27 AOP; predates the AOP outcome |
| Risk Log | Risk and Dependency Log | 2026-07 to 2026-10 | Dependency gates D1 to D8 and the manufacturer rights matrix (Axis and Hanwha connectors live, 2026-08-12) |
| SecuriThings review | SecuriThings Deck Review | 2026-10-26 | Competitor comparison; states launch scope as read-only on devices |
| RMM Review | RMM Category Review, Field Node Management Layer | 2026-07-28 | Decision that the node fleet is managed with RMM-class tooling; channel-proliferation risk |
| Darryl 2026-11-02 | Darryl's direction while this draft was prepared | 2026-11-02 | SNMP/IT devices in Phase 1; the three capability goals (Nozomi analysis component, auto-onboarding, service execution rule set) |

## Change log

| Date | Change |
|------------|--------------------------------|
| 2026-11-02 | First draft from the CDA product record. Same day: three capability goals added (Nozomi analysis component, auto-onboarding, service execution rule set); after Ron Snyder's first read, Priority legend, dependency re-audit with [Mixed] rows, Nozomi knowledge statement, readable sources, service node rows; priorities refactored with Darryl (P0 from 59 rows to 35 against the first-site promise; WAM, field packages, multi-tenancy and RMM fleet management to Phase 2); independent consistency pass applied; tables and prose reformatted for readability |
