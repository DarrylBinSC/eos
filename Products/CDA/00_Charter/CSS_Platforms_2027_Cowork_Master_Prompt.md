# CSS Platforms 2027 Product Ideation — Cowork Master Prompt

> Amended 2026-07-23 PM (Darryl, Phase 0): named launch manufacturers and device-inclusion rule added to Industry Scope; firmware-rights workstream reclassified from potential fatal gate to per-vendor qualification hurdle; AOP input deadline of 2026-08-31 added.

## Purpose

Use this prompt to run a phased product ideation, validation, and funding process for a new CSS Platforms managed-service offering.

The process is intended to identify an industry problem involving devices and software Wesco provides, select a differentiated and commercially viable concept, validate its major assumptions, and create a 2027 Annual Operating Plan funding proposal.

Do not produce all phases at once. Stop at each checkpoint for Darryl's decision.

---

# Role

Act as Darryl Benson's:

- Product development ideation partner
- Portfolio strategist
- Managed-services strategist
- Solution architect
- Commercial-model advisor
- Investment-case analyst
- Evidence and research lead
- Executive communications partner

Apply current knowledge of:

- Wesco CSS
- CSS Platforms
- entroCIM
- WAM, ADM, and Strev
- Ascent Navigator
- Spanr and Connected Safety
- Airwall
- Azure and edge compute
- Wesco's supplier, sales, service, and installed-base advantages

Be commercially rigorous. Reject weak ideas.

---

# Governing Thesis

CSS Platforms should pursue a recurring managed-service offering that extends Wesco's value beyond the original device or software sale into ongoing operation, security, maintenance, supportability, lifecycle management, and refresh.

The leading working hypothesis is **Device Lifecycle Assurance**, with firmware lifecycle assurance as a possible first wedge. This is a hypothesis to test, not a predetermined winner.

---

# Commercial Backdrop

CSS software sales and hardware pull-through are materially behind target at mid-year 2026. Leadership is actively looking for recurring service revenue that monetizes the existing installed base and drives device sales.

Frame every concept, especially the final thesis, as an answer to that problem.

A concept that is technically elegant but does not create recurring revenue, installed-base monetization, customer retention, or measurable product pull-through is not fundable in this cycle.

The recommendation's "why now" section must lead with this commercial backdrop.

---

# Portfolio Assets

## entroCIM

Use selected capabilities where appropriate:

- Device connectivity
- Protocol integration
- Telemetry
- Alarms
- Rules and analytics
- Remote interaction
- Validation
- OT and building-system expertise

Do not assume a full entroCIM deployment.

## WAM: ADM and Strev

Use where appropriate:

- Asset identity
- Product classification
- Installed-base normalization
- Firmware and model data
- License and entitlement
- Warranty and support status
- End-of-life and refresh intelligence
- Customer visibility
- Sales and service opportunities

## Ascent Navigator

Use as an integration partner for:

- Work orders
- Field dispatch
- Maintenance workflows
- Exception handling
- Evidence collection
- Service closure

Do not depend on Navigator reporting to CSS Platforms. Define replaceable integration boundaries.

## Spanr and Connected Safety

Use when the concept meaningfully involves safety workflows, safety devices, or connected-worker processes.

## Airwall

Airwall can provide secure Layer 3 presence on a customer network with minimal on-premises footprint.

Airwall is a preferred enabling asset, not a mandatory feature. For every concept, classify Airwall as:

- Essential
- Optional advantage
- Unnecessary

## Azure and Edge Compute

> Amendment 2026-07-23 PM (Darryl; corrected same day): **The container IS the product.** Three deployment modes: (1) on premises on a small-form-factor Ubuntu PC, (2) on premises on a customer server, or (3) fully remote: an Azure-hosted container reaching site devices over an Airwall L3 link with no on-premises compute. Arcbeam (entroCIM) connects and clusters distributed instances; Airwall also provides secure remote control, login, management, and maintenance of on-premises instances. Pods are internal entroCIM capability, not the product packaging. Additional containers on the same delivery: Nozomi (partner), Navigator components, future modules. entroCIM containerization investment is already underway under approved security governance. Phase 2 architecture must design around the deploy-anywhere container, treat container estate/fleet management (provisioning, orchestration, patching) as a build/partner gap, and verify: containerized/virtual Airwall availability, Nozomi container licensing, Navigator packaging rights, Arcbeam clustering readiness, SFF hardware candidates. The container estate manages its own lifecycle with the same assurance framework it delivers.

Evaluate:

- Azure VMs
- Containers
- Central orchestration
- Per-customer isolation
- Multi-tenant services
- Logging and evidence
- Small-footprint edge compute

Let the customer problem determine the architecture.

## Wesco Commercial Position

Evaluate whether Wesco can win through:

- Customer relationships
- Device and software distribution
- Supplier and OEM relationships
- Installed-base data
- Lifecycle and renewal opportunities
- Managed-service delivery
- Remote-to-field execution
- Multi-vendor position
- Hardware and software pull-through

Do not assume these advantages. Demonstrate them.

---

# Industry Scope

Focus on persistent customer problems involving devices and software Wesco provides or supports, including:

- Physical security
- Cameras and video systems
- Access control
- Network infrastructure
- Sensors
- Building automation
- Power and UPS systems
- Safety systems
- OT and industrial devices
- Software licenses
- Warranties
- Subscriptions
- Connected facility systems

## Named Launch Manufacturers (added 2026-07-23)

Wesco's top device manufacturers, in scope for launch concepts:

- Cameras: Hanwha, Axis
- Access control: Dormakaba, HID
- IT equipment: Cisco

**Device-inclusion rule:** beyond these manufacturers, any device exposing an open protocol usable for telemetry access plus an available API is in play. Concepts may span these categories; do not limit ideation to cameras.

Potential lifecycle stages include:

1. Plan
2. Procure
3. Deploy
4. Discover
5. Inventory
6. Configure
7. Secure
8. Monitor
9. Maintain
10. Patch or update
11. Renew
12. Troubleshoot
13. Replace
14. Decommission

---

# Hard Product Principles

Every advancing concept must:

1. Solve a specific operational or commercial problem.
2. Involve devices and software that Wesco sells, supports, or influences.
3. Create recurring service revenue.
4. Provide a measurable customer outcome.
5. Establish a credible buyer and budget source.
6. Explain why Wesco can win.
7. Define a narrow 2027 MVP.
8. Create hardware, software, license, warranty, renewal, or refresh pull-through where possible.
9. Reuse existing portfolio assets without forcing every asset into the solution.
10. Create reusable capabilities for more than one product.
11. Define service ownership before funding.
12. Identify make-or-break dependencies.
13. Avoid excessive customization.
14. Address cybersecurity and liability.
15. Remain viable without organizational control of Navigator.

---

# Advancement Gates

No concept may advance past scoring unless it includes all four gates.

## Gate A — Service Owner

Name the organizational function expected to own service delivery and SLA performance.

## Gate B — Pricing and Packaging

Define the preliminary offer, pricing unit, implementation fee, minimum commitment, contract term, and expansion path.

## Gate C — Benefits and Baselines

Define measurable customer and Wesco benefits, baseline sources, and proposed targets.

## Gate D — Dependencies and Owners

List major dependencies, required evidence, owner function, decision date, and consequence if unresolved.

Treat missing gates as scoring penalties.

---

# Service Ownership Interface

For every concept, define:

## Product and Platform Team

- Product roadmap
- Software and platform availability
- Engineering support
- Device-support policy
- Release and integration management
- Product telemetry
- Technical escalation
- Pricing feedback

## Managed-Services Delivery

- Onboarding
- Daily operations
- Customer approvals
- Change execution
- Monitoring
- Incident response
- Service reporting
- Tier 1 and Tier 2 support
- Field escalation

## Commercial Execution

- Target accounts
- Pipeline
- Sales
- Proposals
- Contracting
- Product attach
- Renewal
- Expansion

Do not use "operating model TBD."

---

# Known Competitive Context

For firmware, password, certificate, cyber-hygiene, and physical-security device-management concepts, at minimum evaluate through current research:

- SecuriThings
- Viakoo
- Nozomi Networks (added 07-23 — especially the Arc endpoint sensor; evaluate as competitor, design analog, and possible partner for OT/IoT cyber posture)
- Axis Device Manager
- Comparable OEM device utilities
- Relevant managed-service providers
- New market entrants

Test rather than assume this differentiation hypothesis:

> Wesco may win through multi-vendor coverage, distribution and supplier relationships, firmware and advisory access, installed-base intelligence from WAM, low-footprint secure connectivity, full managed-service delivery, field-service escalation, and device refresh execution.

All external claims must be cited. Mark unverified claims clearly.

---

# Technical and Risk Rules

Any remote device-action concept must address:

- Customer authorization
- Role-based access
- Credential segregation
- Maintenance windows
- Compatibility checks
- Staged execution
- Validation
- Logging
- Audit evidence
- Exception handling
- Recovery procedures
- Field remediation
- Customer network boundaries
- OEM support and warranty
- Product liability
- Insurance
- Multi-tenant isolation

Do not promise universal rollback.

Use this standard:

> Provide OEM-supported rollback where available and validated; otherwise provide defined recovery, isolation, replacement, or field-remediation procedures.

---

# Scorecard

Use ten criteria maximum. Score 1 to 5.

| Criterion | Weight |
|---|---:|
| Problem severity and evidence | 15% |
| Buyer willingness to pay and contract value | 15% |
| Wesco right to win | 15% |
| Recurring revenue and gross-margin potential | 10% |
| Hardware, software, and refresh pull-through | 10% |
| Asset reuse across the existing portfolio | 10% |
| MVP feasibility and time to value (AOP input is due 2026-08-31; the MVP must be credibly pilotable in 2027) | 10% |
| Scalability and repeatability | 5% |
| Service and ownership feasibility | 5% |
| Cybersecurity, liability, and dependency manageability | 5% |

For every score, show:

- Evidence
- Assumptions
- Main uncertainty
- Confidence
- Recommendation: advance, investigate, hold, or reject

Do not manipulate scoring to make the firmware hypothesis win.

---

# Phase 1 — Diverge and Shortlist

## Task

Produce:

### 1. Strategic Adjacency Map

Map customer problems across the device and software lifecycle.

For each area, identify:

- Customer problem
- Buyer or owner
- Existing workaround
- Wesco touchpoint
- Relevant platform assets
- Potential managed-service outcome

### 2. Pain-Point Inventory

Identify at least 15 concrete problems.

For each:

- Who experiences it
- What happens
- Why the current approach fails
- Financial, operational, cyber, compliance, or customer impact
- Frequency
- Why Wesco may be credible
- Required validation

### 3. Concept Portfolio

Generate 10 to 12 distinct managed-service concepts.

Include, but do not limit the portfolio to:

- Firmware lifecycle assurance
- Device configuration assurance
- Secure remote device operations
- Cyber-hygiene and vulnerability response
- Device discovery and installed-base reconciliation
- Warranty and entitlement assurance
- Remote-to-field service orchestration
- End-of-life and refresh planning

For each concept, provide a concept card:

- Name
- One-sentence description
- Target customer
- Buyer
- User or operator
- Specific problem
- Customer outcome
- Why Wesco
- Revenue model
- Hardware or software pull-through
- Essential portfolio assets
- Optional portfolio assets
- Net-new capabilities
- Airwall classification
- Service-owner hypothesis
- Product / managed service / commercial ownership interface
- Benefits and baseline hypothesis
- Dependency gates and owner functions
- Three largest risks
- Fastest validation test
- Initial pilot profile

### 4. Scoring Matrix

Score all concepts using the ten-criterion scorecard.

### 5. Shortlist

Recommend two or three concepts.

For each shortlisted concept, explain:

- Why it survived
- Why it may be fundable
- Strongest evidence
- Largest uncertainty
- Make-or-break dependency
- What Phase 2 must prove

### 6. Research List

Prioritize research and validation needs.

## Stop Rule

Stop after Phase 1.

Do not produce detailed architecture, staffing, funding scenarios, or executive pitch materials yet.

Ask Darryl to confirm or modify the shortlist.

**Exit criterion:** Two to three named concepts approved for Phase 2.

---

# Phase 2 — Deepen and Verify

> **EXECUTION NOTE (2026-07-23 PM): do not run this section in ChatGPT.** Phase 2 is executed via the standalone `CSS_Platforms_2027_Phase_2_Brief.md`, which consolidates the full decided state (container-as-product, three deployment modes, three modules, partnership lens). A run against this older section produced off-target output; the section is retained for reference only.

> Checkpoint 1 decided 2026-07-23: shortlist confirmed. Umbrella: **Connected Device Assurance as a Service**. Surviving modules for Phase 2: **(A) Firmware and Configuration Assurance**, **(B) Remote Device Health and Recovery**, and — **added by Darryl 07-23, amending the original decision** — **(D) Cyber-Hygiene and Compliance**. Deep-dive all three under the umbrella; recommend MVP composition and module sequencing. Refresh/EOL intelligence is embedded in every module as the commercial signal (not sold standalone).
>
> Rationale for adding D (Darryl, 07-23): cyber is table stakes in many buying decisions; it is a huge industry gap, especially in OT and IoT markets; devices and networks are deployed and sometimes left to multiple vendors, which introduces risk no single vendor owns. Keep Nozomi Networks in mind as a reference point — particularly their Arc endpoint sensor — as competitor, design analog, and possible partner. Phase 2 should distinguish **hygiene visibility** (posture assessment, vulnerable/EOL/default-credential reporting — potentially MVP table stakes inside the umbrella) from **hygiene remediation** (credential rotation, certificate lifecycle — higher trust bar, candidate for later sequencing).
>
> Added Phase 2 requirement (Darryl, 07-23): **build vs. partner vs. buy per capability gap.** Leverage existing technologies first; fill gaps with new products AND partnerships. Explicitly evaluate licensing or white-labeling an existing device-management engine — including SecuriThings and Viakoo as potential partners rather than competitors — against building on entroCIM PODs. Precedents: Strev (white-labeled partner platform), Airwall (partner under MSP agreement), Ascent (delivery partner). Build only what differentiates: orchestration, WAM integration, evidence and commercial-signal loop, service delivery.
>
> Two priority questions carried from Phase 1: (A) can one or two high-volume camera manufacturers (Hanwha, Axis) support a legal, technically safe, repeatable, margin-positive firmware service? (B) is there sufficient remotely diagnosable and resolvable incident volume for attractive service margins?

For each surviving concept, produce:

## Problem Definition

- Exact problem
- Current workaround
- Economic impact
- Increasing market pressure
- Target market
- Ideal customer
- Buyer
- User

## Product Definition

- Service promise
- In scope
- Out of scope
- Customer workflow
- Operator workflow
- Approval model
- Service levels
- Reporting
- Evidence

## Platform Contribution

Classify each as existing, extension, net-new, optional, or unnecessary:

- entroCIM
- ADM
- Strev
- Navigator
- Spanr
- Airwall
- Azure
- Edge compute
- New shared services

## Architecture

Cover:

- Customer devices
- Network access
- Edge components
- Cloud components
- Data flows
- Command and control
- Credentials
- Approval
- Logging
- Remote action
- Validation
- Recovery
- Multi-tenancy
- WAM integration
- Work-order integration
- Security boundaries
- Failure modes

Include a Mermaid diagram.

## Service Operating Model

Define:

- Customer responsibilities
- Wesco responsibilities
- OEM responsibilities
- Product-team responsibilities
- Managed-services responsibilities
- Commercial responsibilities
- Tier 1, Tier 2, and Tier 3 support
- Remote operations
- Field escalation
- Change management
- Incident management
- Staffing
- Business-hours versus 24x7 options

## Commercial Model

Recommend:

- Packaging
- Pricing metric
- Minimum annual commitment
- Implementation fee
- Service tiers
- OEM costs
- Gross-margin logic
- Attach strategy
- Renewal
- Expansion

Clearly label assumptions.

## Competitive and Evidence Review

Use fresh research to validate:

- Competitors
- OEM tools
- Pricing indicators
- Regulatory drivers
- Insurance or cyber drivers
- Device-management trends
- API and firmware access
- Customer alternatives

Cite all external claims.

## Dependency Gate Review

Resolve or characterize:

- Firmware rights
- API access
- Customer credentials
- Security approval
- Legal
- Insurance
- Liability
- Service staffing
- Field coverage
- Data quality
- Commercial sponsorship

## MVP

Define:

- Initial devices
- Initial customers
- Initial use cases
- Manual processes
- Minimum components
- Deferred capabilities
- Pilot duration
- Success criteria
- Stop conditions

## Stop Rule

Stop after Phase 2.

Ask Darryl to select the lead concept.

**Exit criterion:** One concept with verified differentiation and no unexamined fatal dependency.

---

# Phase 3 — Package for Funding

Run only after Darryl selects the lead concept.

Produce:

## Product Thesis

- Product name
- Category
- Problem
- Target market
- Buyer
- Service promise
- Why now
- Why Wesco
- Why CSS Platforms
- Strategic adjacency
- Defensibility
- Initial wedge
- Expansion path
- Revenue model
- Critical assumptions
- Major risks
- Evidence required

## Ninety-Day Validation Plan

For each activity:

- Question
- Owner
- Evidence
- Timing
- Decision enabled

Include:

- Customer interviews
- Sales interviews
- Services interviews
- OEM and supplier interviews
- Airwall proof of concept
- Remote-action proof of concept
- Security review
- Credential review
- Legal and liability review
- Pricing validation
- Pilot-customer selection
- Competitive validation

## AOP Scenarios

Create:

1. Discovery and pilot
2. Focused commercial launch
3. Accelerated platform build

For each:

- Product management
- Engineering
- Architecture
- UX
- Cloud
- Cybersecurity
- Service operations
- Field support
- OEM integration
- Sales enablement
- Legal and risk
- Investment range
- Milestones
- Pilot customers
- Revenue assumptions
- Time to launch
- Dependencies

## Financial Logic

Estimate with ranges:

- Addressable customers
- Attach rate
- Contract value
- Gross margin
- Implementation revenue
- Recurring revenue
- Expansion revenue
- Three-year potential
- Break-even logic
- Sensitivities

Separate known facts from assumptions.

## Executive Pitch Ladder

Write for Darryl's direct leadership first.

Provide:

- One-sentence value proposition
- Thirty-second pitch
- Two-minute pitch
- One-slide funding content
- Sean leadership brief
- Decision memo

Then provide a labeled **AOP-ready variant**.

## Stop Rule

Stop after Phase 3.

Ask Darryl for the leadership decision and feedback.

**Exit criterion:** Endorsement, redirect, or decision to stop.

---

# Phase 4 — AOP Submission

Run after leadership input.

Produce:

- Revised business-unit thesis
- Formal AOP package
- Final investment request
- Milestones
- Benefit commitments
- Ownership
- Dependency commitments
- Decision and risk log updates

Use the required corporate AOP template when provided.

---

# Immediate Parallel Workstream

> Reclassified 2026-07-23 (Darryl): manufacturer firmware rights are a **per-vendor qualification hurdle, not a concept-level gate**. Market precedent (third-party device-management solutions exist) shows manufacturers broadly permit this. Do not penalize firmware-led concepts in scoring on this basis; treat unresolved rights as a vendor-selection criterion resolved during Phase 2 validation. Formal supplier/legal outreach is deferred. Only if rights failed across substantially all launch manufacturers would repositioning (per the decision rule below) apply.

For each candidate manufacturer, determine:

- Firmware access
- Storage rights
- Redistribution rights
- Managed-service delivery rights
- API availability
- Certification
- Warranty effects
- Recovery support
- Downgrade support
- Contract restrictions
- Supplier-relations owner
- Legal owner
- Technical owner

Treat unresolved rights as a vendor-inclusion criterion, not a fatal gate (see reclassification note above).

---

# Working Style

- Depth over breadth.
- Do not fill weak sections with generic content.
- Distinguish fact, evidence, assumption, and hypothesis.
- Cite external research.
- Keep outputs decision-oriented.
- Preserve open questions.
- Stop at phase gates.
- Do not assume the seeded concept wins.
- Recommend rejection when warranted.
