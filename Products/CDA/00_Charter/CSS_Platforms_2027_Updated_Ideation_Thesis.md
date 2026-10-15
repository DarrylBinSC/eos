# CSS Platforms 2027 — Updated Product Ideation Thesis and Charter

**Date:** July 23, 2026  
**Owner:** Darryl Benson  
**Purpose:** Define the strategic thesis, decision rules, and funding logic for selecting a new CSS Platforms product or managed-service offering for the 2027 Annual Operating Plan.

---

# Executive Thesis

CSS Platforms should pursue a new recurring managed-service offering that extends Wesco's value beyond the original device and software sale and into ongoing operation, security, maintenance, lifecycle management, and refresh.

The strongest opportunity will:

- Solve a persistent and expensive customer problem involving devices and software Wesco already sells, supports, or influences.
- Monetize the installed base through recurring service revenue.
- Create measurable hardware, software, license, warranty, or refresh pull-through.
- Reuse capabilities from entroCIM, WAM, Airwall, Azure, Navigator, Spanr, and Wesco's service organization without forcing every asset into every solution.
- Use a narrow market-entry point that can be piloted in 2027.
- Create reusable platform services that allow the entroCIM and WAM teams to support several offerings rather than becoming dedicated to another single-purpose product.
- Carry a defined service owner, commercial model, measurable benefit, dependency map, and operating boundary before significant investment is approved.

The leading working hypothesis is **Device Lifecycle Assurance**: a managed service that verifies the identity, security posture, configuration, firmware, supportability, entitlement, warranty, and lifecycle condition of connected devices; executes approved remote actions where technically and contractually appropriate; and orchestrates field remediation or replacement when remote resolution is not possible.

Firmware management is a promising first module or market wedge, but it is not assumed to be the final product category.

---

# Why Now

CSS software sales and hardware pull-through are materially behind target at mid-year 2026. Leadership is looking for credible recurring-service revenue that:

1. Monetizes the existing installed base.
2. Strengthens customer retention after the initial sale.
3. Produces identifiable device, software, warranty, renewal, and refresh opportunities.
4. Demonstrates measurable economic value rather than technical capability alone.
5. Can contribute to the 2027 Annual Operating Plan.

A concept that is technically elegant but cannot generate recurring revenue, produce commercial pull-through, or establish accountable service ownership is not fundable in this cycle.

---

# Portfolio Context

## entroCIM

A mature connected-building and OT/IoT platform with:

- Device and system connectivity
- Protocol integration and normalization
- Telemetry, alarms, rules, analytics, and workflows
- Remote monitoring and controlled interaction
- Existing expertise in operational technology and building systems
- Azure and container deployment patterns

New concepts should use selected entroCIM capabilities as reusable platform services where appropriate. They should not automatically require a full entroCIM deployment.

## WAM: ADM and Strev

WAM provides a foundation for:

- Asset and installed-base identity
- Product classification and normalization
- Hardware, software, license, warranty, entitlement, and lifecycle visibility
- Renewal and expiration intelligence
- Customer-facing lifecycle reporting
- Sales and service opportunities generated from installed-base data

ADM is the internal ingestion, normalization, enrichment, and classification layer. Strev is the customer-facing experience and lifecycle layer.

WAM should be evaluated as a source of differentiation, particularly where operational device state can be connected to support status, commercial entitlement, risk, and replacement planning.

## Ascent Navigator

Navigator provides:

- Assets and site information
- Work orders
- Maintenance and service workflows
- Scheduling and dispatch
- Evidence collection and service closure
- Facility-management processes

Navigator is an integration partner, not an organizational dependency. Concepts must remain viable if Navigator does not report to CSS Platforms and should define a replaceable work-management interface where practical.

## Spanr and Connected Safety

Spanr may provide:

- Safety workflows
- Connected-worker and safety data
- Incident or compliance processes
- Opportunities to apply common device, monitoring, and service capabilities

Its role should be evaluated concept by concept rather than forced into every product.

## Airwall

Airwall can create a controlled Layer 3 presence on the customer's network with a minimal on-premises footprint. It may provide a practical foundation for secure remote service delivery.

Airwall is a preferred enabling asset, not a mandatory design constraint. Every concept must state whether Airwall is:

- Essential
- Advantageous but optional
- Unnecessary

## Azure and Edge Compute

Azure can provide:

- Virtual machines
- Containers
- Data services
- Workflow and job orchestration
- Multi-tenant control planes
- Logging, reporting, and audit
- Per-customer isolation where required

Small-footprint edge compute may be used when local protocol access, latency, resiliency, or security boundaries require it.

The architecture should follow the customer problem. It should not begin with an assumption that every solution requires an Azure VM, an on-premises PC, or a permanent remote connection.

## Wesco Commercial Position

Wesco's potential advantages include:

- Existing device and software sales relationships
- Broad supplier and manufacturer relationships
- Customer access through CSS sales and service organizations
- Installed-base and transaction data
- Device, license, warranty, and renewal opportunities
- Managed-services delivery capabilities
- Ability to connect remote actions with field service and replacement sales
- Multi-vendor position across customer environments

These advantages must be demonstrated for each concept. They cannot be assumed.

---

# Product Decomposition and Service Tier Mapping (added 2026-07-27, Darryl sketch, session-refined)

Three service tiers, each delivered by a named product container. All containers ride the deploy-anywhere node (or Mode 3 remote) with Airwall connectivity; ship the containers the customer's tier requires.

| Tier | Service | Delivering container | Content |
|---|---|---|---|
| **A — Cyber-Hygiene Services (Base)** | Endpoint/OT threat and hygiene visibility | **Partner on-premises agent** (partner company; host-based sensor — profile matches Nozomi Arc, to be confirmed) | Detects compromised endpoints and insider threats; collects endpoint and network activity; identifies connected OT assets; enriches asset profiles with firmware/software version information for device-level visibility and vulnerability assessment. Integrated via API |
| **B — Device Status and Health** | Foundational assurance | **Base Wesco Connected Device Assurance Services tool** (entroCIM-based: connector, database, UI, API framework) | Functional checks, diagnostics, validation, field escalation, service evidence; API connection to the cyber-hygiene tool; provides the user interface for alerting and alarming on base functionality |
| **C — Firmware and Configuration** | Managed action and lifecycle planning | **Advanced Wesco Configuration Assurance Services tool** (entroCIM-based) | Service delivery, firmware posture (eligible devices) and tracking, configuration status, device health and telemetry depth, maintenance scheduling, firmware lifecycle planning; remediation and controllability dependent on product |

**Rulings (Darryl, 2026-07-27) — mapping questions resolved:**

1. **Repositioning (general):** containerization is **deployment and internal strategy** — it makes the offer appealing and scalable — but it is **not the basis of the product strategy**. Outward framing leads with the service value proposition and feasibility; containers appear as the delivery mechanism, not the headline.
2. **Data-fidelity ladder:** the partner product (A) *discovers* firmware/software version data — indicative, not authoritative. **Verified product models live in C**, and **validated versions come through direct device communication (integration)**. The base tool (B) may or may not have device integration completed for a given device; at minimum it carries partner-sourced data. Managed firmware lives in C. Narrative: **discovered (partner) → validated (device integration) → managed (controlled action).**
3. **Commercial tiering:** the **Base tier bundles the partner sensor (A) plus the Base entroCIM pod (B)** — B is the interface for the service providers (cyber-hygiene findings, base connectivity, mostly the partner sensor). The Advanced tier adds C. No pricing on slides.
4. **Navigator:** when Navigator is present, CDA must connect (work orders, field escalation). **Strategic point: the Navigator team is in a significant redesign with 2027 deadlines — CDA is positioned explicitly in support of those integrations. This is solidarity in the product and must appear in executive material.**
5. **Naming:** "partner sensor" only in shareable material; no partner company names until commercial terms exist.

# Strategic Product Principle

> Amendment 2026-07-23 PM (Darryl): **leverage existing technologies first; fill gaps with new products AND partnerships.** For every capability gap a concept requires, assess build vs. partner vs. buy before assuming internal build. Established portfolio precedents: Strev (white-labeled partner platform inside WAM), Airwall (partner technology under MSP agreement), Ascent (delivery partner). Wesco's differentiation is the integrated service, install-base intelligence, and distribution position — not ownership of every component.

The goal is not to create another dashboard.

The goal is to create a managed operational outcome around devices and software Wesco provides.

Strong concepts are likely to combine several of the following:

- Device discovery and identity
- Inventory reconciliation
- Firmware and software status
- Configuration assurance
- Password and certificate lifecycle
- Vulnerability response
- Warranty, entitlement, and support status
- Remote action and remediation
- Approval and change control
- Evidence and audit reporting
- Work-order escalation
- Field service
- End-of-life identification
- Refresh recommendations
- Commercial renewal and replacement opportunities

The customer should be buying an outcome and service commitment, not merely access to a software tool.

---

# Working Product Thesis

## Device Lifecycle Assurance

### Category

A multi-vendor managed service for the operational, security, support, and commercial lifecycle of connected devices.

### Customer Problem

Customers operate large fleets of cameras, access-control devices, sensors, network devices, building systems, safety devices, and other connected infrastructure. These fleets are frequently:

- Incompletely inventoried
- Inconsistently configured
- Running unsupported or vulnerable firmware
- Dependent on fragmented OEM tools
- Poorly aligned with warranty and entitlement records
- Expensive to maintain manually
- Difficult to govern across multiple sites and manufacturers
- Replaced reactively rather than through planned lifecycle management

Ownership is often fragmented among IT, physical security, facilities, OT, service providers, and individual site teams.

### Service Promise

Wesco continuously verifies the state and supportability of covered devices, identifies required action, obtains customer approval, performs controlled remote remediation where supported, validates the result, preserves evidence, and escalates unresolved conditions to field service or replacement.

### Initial Wedge

The initial wedge may be firmware and support-status assurance for a narrow set of physical-security devices, such as selected camera and edge-device product lines.

The MVP should be limited to manufacturers and device models for which Wesco can establish:

- Reliable device identification
- Supported access methods
- Firmware availability and use rights
- Compatibility and prerequisite checks
- Safe update procedures
- Post-action validation
- Defined recovery or field-remediation procedures
- Sufficient customer demand

### Expansion Path

Possible modules include:

1. Firmware assurance
2. Configuration assurance
3. Credential and certificate lifecycle
4. Vulnerability-response operations
5. Warranty and entitlement assurance
6. End-of-support and refresh planning
7. Remote health and availability checks
8. Field-service orchestration
9. Device replacement and procurement
10. Broader OT and building-device lifecycle services

### Wesco Differentiation Hypothesis

The differentiation hypothesis to test is that Wesco can combine:

- Multi-vendor device coverage
- Supplier and OEM relationships
- Installed-base intelligence from WAM
- Secure low-footprint access through Airwall
- Device interaction and validation through entroCIM capabilities
- Remote-to-field orchestration through Navigator or equivalent workflows
- Full managed-service delivery
- Hardware and software refresh execution

This may be more valuable than a manufacturer-specific utility or a customer-operated device-management tool.

The hypothesis must be validated through competitive research, customer interviews, OEM discussions, and technical proof of concept.

---

# Advancement Gate Discipline

No concept may advance beyond initial scoring unless it includes all four of the following.

## 1. Service-Owner Hypothesis

Identify the function expected to own:

- Managed-service delivery
- Customer SLA performance
- Operational staffing
- Escalation
- Service reporting
- Continuous improvement

A named individual is not required during early ideation, but the accountable organizational function must be identified.

## 2. Pricing and Packaging Hypothesis

State:

- What the customer buys
- Pricing unit
- Minimum commitment
- Implementation fee
- Service tiers
- Contract term
- Expected recurring value
- Hardware, license, warranty, or refresh attachment

## 3. Measurable Benefits and Baselines

Define:

- Customer outcome
- Metric
- Baseline source
- Measurement frequency
- Target improvement
- Evidence required

Examples may include:

- Percentage of covered devices on approved firmware
- Time to remediate critical vulnerabilities
- Unsupported-device reduction
- Avoided site visits
- Device availability
- Audit-compliance rate
- Planned refresh revenue
- Warranty recovery
- Reduction in manual inventory effort

## 4. Dependency Gates With Owner Functions

Identify make-or-break dependencies such as:

- Firmware redistribution or access rights
- OEM API access
- Supplier participation
- Customer credential model
- Airwall security approval
- Azure architecture approval
- Legal and contract language
- Insurance
- Product liability
- Service staffing
- Field-service coverage
- Data availability
- Commercial sponsorship

Every dependency must have:

- Owner function
- Required evidence
- Decision date
- Effect if unresolved

A missing gate is a scoring penalty, not a footnote.

---

# Service Ownership Interface

Every concept must define the operating boundary among three groups.

## Product and Platform Team

Expected responsibilities may include:

- Product roadmap
- Platform availability
- Software support
- Technical service levels
- Release and integration management
- Device-support policy
- Product telemetry and reporting
- Pricing and packaging feedback
- Product documentation
- Escalation to engineering

## Managed-Services Delivery

Expected responsibilities may include:

- Service onboarding
- Daily operations
- Customer approvals
- Change execution
- Monitoring and exception handling
- Incident response
- Service reporting
- Tier 1 and Tier 2 support
- Field-service coordination
- SLA performance

## Commercial Execution

Expected responsibilities may include:

- Target-account selection
- Pipeline development
- Solution selling
- Proposal and contracting
- Hardware and software attachment
- Renewal
- Account expansion
- Customer success sponsorship

The interface cannot be deferred to an undefined future operating model.

---

# Architecture and Risk Principles

> Amendment 2026-07-23 PM (Darryl; corrected same day): **The container IS the product.** Wesco is investing in containerization capability for entroCIM (Docker work already advancing under approved security governance). The product ships as a container (or container set) with three deployment modes: **(1) on premises on a Wesco-supplied small-form-factor PC (Ubuntu), (2) on premises on the customer's own server, or (3) fully remote: an Azure-hosted container reaching site devices over an Airwall L3 link, with no on-premises compute required.** **Arcbeam (entroCIM)** connects and clusters distributed instances into one operable estate; **Airwall** also provides the secure path to remotely control, log in, manage, and maintain on-premises instances. Terminology discipline: pods are internal entroCIM capability (a firmware pod is a new pod *inside* entroCIM), not the product packaging. Additional containers ride the same delivery: Nozomi (partner capability), Navigator components, future modules. Implications: modular service delivery by container configuration; deployment form follows customer constraints, not ours; field hardware is a Wesco sale (pull-through); the container estate manages its own lifecycle with the same assurance framework (credibility proof point). Build/partner gap: container estate/fleet management (provisioning, orchestration, patching). Verify in Phase 2: containerized/virtual Airwall availability and licensing; Nozomi container licensing and partnership terms; Navigator packaging rights (organizational boundary applies); Arcbeam clustering readiness for this pattern (validate with Ron Snyder); candidate SFF hardware.

A likely pattern is:

- Customer devices
- Secure Airwall Layer 3 connectivity
- Optional small-form-factor edge connector
- Azure-hosted control plane or per-customer service
- Selected entroCIM connectivity and action services
- WAM asset and lifecycle data
- Customer approval and evidence interface
- Navigator or equivalent work-order integration
- Managed-service operations

This is a reference pattern, not a mandatory solution.

## Remote Change Controls

Any service that changes customer devices must include:

- Explicit authorization
- Role-based access
- Credential segregation
- Approved maintenance windows
- Compatibility and prerequisite checks
- Staged execution
- Post-action validation
- Full logging
- Exception handling
- Recovery or field-remediation plan
- Customer-visible evidence

## Rollback Language

Do not promise universal firmware rollback.

Use the following standard:

> The service will provide OEM-supported rollback where available and validated. Where rollback is unavailable, the service will provide defined recovery, isolation, replacement, or field-remediation procedures.

## Liability Boundary

The service must distinguish between:

- Process assurance
- Outcome validation
- Device availability commitments
- Manufacturer defects
- Customer network conditions
- Unsupported devices
- Customer-delayed approvals
- Physical recovery requirements

Legal, insurance, supplier, and security review are required before commercial launch.

---

# Concept Evaluation Scorecard

Use no more than ten criteria. Score each from 1 to 5 and apply the weights below.

| Criterion | Weight | What a 5 Means |
|---|---:|---|
| Problem severity and evidence | 15% | A frequent, expensive problem validated by customers and operators |
| Buyer willingness to pay and contract value | 15% | A clear budget owner, strong service economics, and credible annual contract value |
| Wesco right to win | 15% | A defensible advantage based on customer access, supplier position, data, service, and lifecycle execution |
| Recurring revenue and gross-margin potential | 10% | Attractive recurring revenue with scalable service delivery |
| Hardware, software, and refresh pull-through | 10% | The service reliably generates additional Wesco product and lifecycle sales |
| Asset reuse across the portfolio | 10% | Meaningful reuse of existing platforms, data, connectivity, and teams without forced complexity |
| MVP feasibility and time to value | 10% | A narrow MVP can reach customer value in 2027 under a credible investment plan |
| Scalability and repeatability | 5% | The service can expand across customers, sites, and manufacturers without excessive custom work |
| Service and ownership feasibility | 5% | Accountable delivery, support, commercial ownership, and staffing can be established |
| Cybersecurity, liability, and dependency manageability | 5% | Major risks have credible mitigations and no unresolved fatal dependency |

Do not create false precision. Scores must be accompanied by:

- Evidence
- Assumption
- Main uncertainty
- Confidence level
- Advancement recommendation

---

# Decision Rules

A concept should advance only when:

- It addresses a named operational problem.
- A clear buyer exists.
- A recurring-service model is plausible.
- Wesco has a differentiated role.
- The initial scope is narrow enough to pilot.
- The product can produce measurable benefit.
- The service ownership interface is credible.
- Make-or-break dependencies are identified.
- The required investment is proportionate to the opportunity.
- The architecture and risk profile are manageable.

A concept should be rejected or held when:

- It is primarily a generic dashboard.
- It requires hundreds of custom device integrations at launch.
- It relies on unrestricted customer-network access.
- It duplicates mature OEM tools without differentiation.
- It lacks credible firmware, data, or API rights.
- It requires a custom-services engagement for every customer.
- It cannot support acceptable gross margins.
- It creates unreasonable liability.
- It has no commercial owner.
- It does not create recurring revenue or meaningful pull-through.

---

# Phased Execution

Do not attempt to produce the full investment case in one response.

## Phase 1 — Diverge and Shortlist

Produce:

1. Strategic adjacency map
2. At least 15 specific customer pain points
3. Ten to twelve product or service concepts
4. Consistent concept cards
5. Simplified weighted scoring matrix
6. Recommended shortlist of two to three concepts
7. Open questions and prioritized research list

Stop for Darryl's decision.

**Exit criterion:** Two to three named surviving concepts.

## Phase 2 — Deepen and Verify

For the confirmed shortlist, produce:

1. Problem definition
2. Target market and buyer
3. Product and service definition
4. Platform contribution
5. Architecture and Mermaid diagram
6. Service operating model
7. Commercial model
8. Competitive position
9. Security and liability assessment
10. Dependency gates
11. MVP definition
12. Evidence and unresolved questions

Stop for Darryl's decision.

**Exit criterion:** One named lead concept with a credible competitive position and no unexamined make-or-break dependency.

## Phase 3 — Package for Funding

For the selected lead concept, produce:

1. Final product thesis
2. One-sentence value proposition
3. MVP and pilot plan
4. Ninety-day validation plan
5. Staffing and ownership model
6. Three 2027 funding scenarios
7. Preliminary financial logic
8. Risk and governance model
9. Thirty-second pitch
10. Two-minute pitch
11. Sean leadership brief
12. AOP-ready variant
13. Decision memo

Stop for Darryl's decision.

**Exit criterion:** Leadership-ready funding package and explicit endorsement request.

## Phase 4 — AOP Submission

After leadership input:

1. Revise the thesis
2. Create the business-unit version
3. Align to the formal AOP template
4. Finalize investment, benefit, and milestone commitments
5. Record decisions and ownership

**Exit criterion:** Formal AOP submission or documented redirect.

---

# Immediate Make-or-Break Investigation

> Reclassified 2026-07-23 (Darryl): firmware rights are a **per-vendor qualification hurdle, not a concept-level gate** — market precedent shows manufacturers broadly permit third-party firmware management. Resolved per vendor during Phase 2 validation; formal outreach deferred. Named launch manufacturers: Hanwha, Axis (cameras); Dormakaba, HID (access control); Cisco (IT equipment); plus any device with an open telemetry protocol and available API. AOP input deadline: 2026-08-31.

Begin this independently of the phased analysis:

## Manufacturer Firmware Rights

Determine, for candidate launch manufacturers and device categories:

- Whether Wesco may obtain and store firmware
- Whether Wesco may redistribute firmware to customers
- Whether firmware may be delivered through a managed service
- Whether customer-specific portal access is required
- Whether APIs or automated update mechanisms are available
- Whether OEM certification is required
- Whether updates affect warranty
- Whether downgrades or recovery images are supported
- Whether supplier agreements impose restrictions

Potential owner functions:

- Supplier relations
- Legal
- Cybersecurity
- Product management
- OEM technical contacts

Per the 07-23 reclassification: unresolved rights exclude a vendor from the launch program rather than invalidating the concept; repositioning applies only if rights fail across substantially all launch manufacturers.

---

# Final Strategic Position

The working thesis is not that Wesco should build a generic firmware tool.

The working thesis is that Wesco may be able to create a differentiated **Device Lifecycle Assurance managed service** that connects:

- Devices Wesco sells
- Secure remote access
- Operational condition
- Firmware and configuration state
- Cybersecurity response
- Warranty and entitlement
- Service operations
- Field remediation
- Planned replacement and refresh

The 2027 decision is whether this problem is sufficiently urgent, differentiated, scalable, and commercially attractive to justify a narrow pilot and the creation of reusable remote-device-service capabilities within CSS Platforms.
