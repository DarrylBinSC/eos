# CSS Platforms 2027 Product Ideation and Investment Thesis Prompt



## 1. Commercial Backdrop (the "why now")
CSS software sales and hardware pull-thru are materially behind target at mid-year 2026. Leadership is actively looking for recurring service revenue that monetizes the existing installed base and drives device sales. Frame every concept, and especially the final thesis, as an answer to that question. A concept that is technically elegant but does not generate recurring revenue and hardware pull-thru is not fundable in this cycle. The "why now" section of the recommendation must lead with this.

## 2. Advancement Gate Discipline
A prior portfolio initiative built strong capability ahead of its commercial model and later faced a difficult "investment to date vs. value today" review. Do not repeat that pattern. No concept may advance past scoring unless it carries all four of: (a) a named service-owner hypothesis, (b) a pricing and packaging hypothesis, (c) measurable benefits with baselines defined at day one, (d) explicit dependency gates, each with a named owner function (e.g., supplier relations, legal, security governance). Treat a missing gate as a scoring penalty, not a footnote.

## 3. Service Ownership Interface
In the current portfolio, the boundary between product support (owned by the platform team) and managed-services delivery (owned elsewhere in the business) is a live, unresolved issue. Any new service offering will inherit this problem unless it is designed out. For every concept, explicitly state the proposed interface: what the product team owns (SLA, support, pricing feedback), what managed-services delivery owns, and what commercial execution owns. Do not defer this to "operating model TBD."

## 4. Known Competitive Context (verify with current research)
For device firmware, password, and certificate management in physical security, at minimum evaluate: SecuriThings, Viakoo, and manufacturer tools such as Axis Device Manager and similar OEM utilities. The working differentiation hypothesis to test, not assume: Wesco wins through multi-vendor coverage, distribution and supplier relationships (firmware access, early advisories), installed-base intelligence from its asset-management platform, low-footprint secure connectivity, and full service delivery (the customer does nothing but approve) versus tools the customer must staff and operate.

## 5. Scoring Simplification
Collapse the three platform-specific criteria (ability to use Airwall / entroCIM / WAM) into one criterion: "asset reuse across the existing portfolio." Cap the scorecard at 10 criteria total. Twenty criteria with weights creates false precision and structurally favors asset-heavy ideas over customer-pain-heavy ideas.

## 6. Phased Execution — do not produce everything in one response
Run the analysis in three phases and stop at the end of each for my review:
- Phase 1: Strategic adjacency map, pain-point inventory, product concept portfolio (10 to 12), and the simplified scoring matrix with a recommended shortlist of 2 to 3. Stop.
- Phase 2 (after I confirm the shortlist): deep dives on the surviving concepts only, including architecture, service operating model, and commercial model. Stop.
- Phase 3 (after I confirm the lead concept): recommended product thesis, MVP, 90-day validation plan, AOP funding scenarios, and the executive pitch ladder.
Depth over breadth in every phase. If a section would be thin, say so and shorten it rather than filling it.

## 7. Audience Sequencing
The funding path is: my direct leadership first, then business-unit leadership, then the formal 2027 AOP process. The executive pitch materials in Phase 3 should be written for the first conversation (direct leadership endorsement), with the AOP-ready version as a labeled variant.

## Role

Act as my product development ideation partner, portfolio strategist, solution architect, managed-services operator, and investment-case advisor.

Your job is to identify, evaluate, and shape new product and service opportunities that Wesco can adopt into the CSS Platforms portfolio and fund through the 2027 Annual Operating Plan.

Think like a senior product executive who understands:

- Connected devices, OT, IoT, building systems, physical security, networking, and lifecycle services
- Enterprise software platforms and cloud-to-edge architectures
- Managed services, recurring revenue, service delivery, and operating-model design
- Product portfolio strategy, product-market fit, commercial packaging, and investment prioritization
- Wesco's role as a distributor, integrator, solutions provider, and long-term customer partner
- The practical constraints of extending existing product teams across multiple solutions

Do not limit the analysis to incremental feature ideas. Look for valuable customer problems that can become repeatable, scalable offerings while remaining adjacent to Wesco CSS and the current CSS Platforms portfolio.

---

# Context

## Business Context

I lead the CSS Platforms portfolio within Wesco's CSS business. The portfolio includes:

- **entroCIM** — an established connected-building and OT/IoT platform that can connect to, normalize, monitor, analyze, and interact with devices and systems.
- **Wesco Asset Management, or WAM**
  - **ADM** — internal data ingestion, normalization, enrichment, classification, and lifecycle intelligence.
  - **Strev** — customer-facing asset, license, entitlement, warranty, renewal, and lifecycle visibility.
- **Spanr** — a connected safety platform and service.
- **Ascent Navigator** — a facility and service-management platform that can support work orders, site activity, maintenance, and service delivery. Navigator does not currently report directly to me, so ideas may leverage it, but must not depend on an organizational change or exclusive control of the platform.

The portfolio is increasingly expected to support a broader managed-services strategy across connected facilities, assets, safety, remote monitoring, site operations, and lifecycle management.

The entroCIM and WAM teams cannot remain dedicated to only one product. New ideas should deliberately create reusable capabilities, common services, shared architecture, and cross-product operating leverage.

## Strategic Assets

Consider the combined power of the following assets:

### entroCIM

- Device and system connectivity
- Protocol translation and normalization
- Rules, analytics, alarms, and workflows
- Remote interaction with customer devices
- Existing expertise in buildings, OT, IoT, and operational systems
- Ability to use only selected capabilities rather than requiring a full entroCIM deployment

### WAM: ADM and Strev

- Product, device, software, license, entitlement, warranty, and lifecycle data
- Data ingestion, normalization, classification, enrichment, and governance
- Customer-facing inventory and lifecycle visibility
- Renewal, refresh, warranty, and installed-base intelligence
- Potential to connect operational device state with commercial and lifecycle records

### Navigator

- Work orders
- Maintenance and service workflows
- Site and facility operations
- Dispatch, scheduling, evidence collection, and service closure
- Potential orchestration layer for human intervention when remote action is not sufficient

### Airwall

- Secure Layer 3 connectivity into customer environments
- Minimal on-site network footprint
- Controlled connectivity without a traditional broad remote-access architecture
- Potential to connect field devices to Azure-hosted services and virtual machines
- A practical mechanism for delivering remote managed services to customer devices

### Azure and Edge Compute

- Azure-hosted virtual machines, containers, data services, and automation
- Small-footprint on-premises compute when required
- Ability to deploy a focused service rather than a full application stack
- Potential for per-customer or multi-tenant service patterns
- Centralized policy, workflow, telemetry, audit, and operational control

### Wesco Commercial Position

Wesco already supplies or supports many of the devices, systems, and software that customers must operate throughout their lifecycle. Potential target domains may include:

- Physical security cameras and video systems
- Access-control systems
- Network infrastructure
- Sensors and connected building devices
- Power, UPS, and monitoring systems
- Safety devices
- Building automation and controls
- Industrial and OT devices
- Software, licenses, warranties, and subscriptions associated with these systems

The best opportunities should strengthen Wesco's position after the initial product sale and create a recurring service relationship around the devices and software Wesco provides.

---

# Initial Product Hypothesis

Use the following as a seed hypothesis, not as a predetermined answer:

## Firmware Lifecycle Assurance as a Service

A lightweight managed service that identifies device firmware, evaluates current versions, manages update policies, obtains customer approval, executes controlled updates, validates outcomes, supports rollback, and provides auditable assurance.

A possible architecture could include:

- An Azure VM or focused cloud service using selected entroCIM connectivity and orchestration capabilities
- A new purpose-built firmware-update service or application component
- A field Airwall connection providing secure Layer 3 access to customer devices
- Optionally, a small-form-factor on-premises computer containing the required Airwall agent, connector, or local execution service
- A narrow initial device scope, such as selected camera models and one or two additional device categories
- A simple customer interface for:
  - Inventory
  - Firmware status
  - Risk and compatibility review
  - Approval
  - Scheduling
  - Update execution
  - Validation
  - Rollback
  - Audit evidence
- Integration with WAM for asset identity, model, warranty, entitlement, lifecycle, and installed-base data
- Integration with Navigator for field work, exceptions, physical remediation, and service records

Potential customer value includes reduced cyber exposure, lower operational effort, improved device reliability, stronger governance, fewer unsupported devices, better auditability, and reduced dependence on fragmented manufacturer tools.

Challenge this hypothesis rigorously. Determine whether it is the strongest opportunity, a component of a broader service, or inferior to another adjacent problem.

---

# Objective

Identify industry problems involving devices and software that Wesco provides, supports, or influences, then define high-value product and service opportunities that:

1. Are adjacent to the current CSS business and CSS Platforms portfolio.
2. Create a credible recurring managed-service revenue stream.
3. Use existing portfolio capabilities without requiring a full deployment of every platform.
4. Benefit from secure cloud-to-customer connectivity through Airwall.
5. Use Azure-hosted services, virtual machines, containers, or light edge compute where appropriate.
6. Combine device operations, asset data, software lifecycle data, work management, and service delivery.
7. Give the entroCIM and WAM teams reusable capabilities that can support multiple products.
8. Can begin with a narrow, practical market entry point and expand over time.
9. Address a specific, expensive, persistent, and measurable customer pain point.
10. Strengthen Wesco's position across the full lifecycle of devices and software it sells.
11. Can be explained through a clear, concise value proposition suitable for executive approval and 2027 AOP funding.
12. Do not depend on Navigator reporting directly to my organization.
13. Do not require Wesco to become the original equipment manufacturer of the underlying devices.
14. Do not assume unrestricted access to customer networks or devices.
15. Provide a defensible role for Wesco that is more valuable than simple monitoring or resale.

---

# Ideation Principles

Use these principles throughout the analysis.

## Start With the Problem

Do not begin by combining technologies and then searching for a use case. Start with customer and business problems that are:

- Operationally expensive
- Difficult to solve consistently
- Fragmented across vendors
- Increasing because of device proliferation, cybersecurity, labor constraints, compliance, or lifecycle complexity
- Poorly addressed by existing point products
- Relevant to devices and software Wesco already sells or supports

## Favor Service-Led Productization

Prioritize opportunities where software enables a repeatable service rather than a stand-alone software license.

The offering should ideally include:

- Continuous or periodic monitoring
- Policy management
- Remote action
- Human review or approval where necessary
- Exception handling
- Audit evidence
- Reporting
- Escalation to field service
- Ongoing asset and lifecycle intelligence

## Use the Platforms Selectively

Do not force every product into every idea.

For each concept, specify:

- Which existing platform capabilities are essential
- Which are optional
- Which new capabilities must be built
- Whether the customer sees a unified interface or multiple integrated services
- Whether a platform is used as an internal service component rather than deployed as a full customer-facing product

## Build Reusable Capabilities

Look for common service components that can support multiple offerings, such as:

- Secure remote device access
- Device identity and inventory
- Credential and access governance
- Configuration collection and comparison
- Firmware and software version intelligence
- Policy evaluation
- Change approval
- Remote job execution
- Validation and rollback
- Audit evidence
- Risk scoring
- Work-order creation
- Field-service escalation
- Customer notifications
- Vendor advisory ingestion
- Lifecycle and replacement recommendations
- Multi-tenant operations
- Role-based access control
- Service-level monitoring

## Avoid Overreach

Do not recommend a concept merely because it is technically possible.

Reject or penalize ideas that:

- Require deep support for hundreds of device manufacturers at launch
- Depend on unrestricted privileged access
- Create unacceptable product-liability or cybersecurity exposure
- Require a large custom-services engagement for every customer
- Compete directly with mature OEM tools without a clear Wesco advantage
- Depend on data Wesco cannot realistically obtain
- Require a major reorganization before launch
- Cannot produce a narrow MVP within a reasonable investment envelope
- Provide generic dashboards without a clear operational outcome
- Lack a credible service-delivery model

---

# Required Analysis

## 1. Strategic Adjacency Map

Describe the opportunity space around the current portfolio.

Map potential problems across the following lifecycle:

1. Plan and specify
2. Procure
3. Deploy
4. Discover and inventory
5. Configure
6. Secure
7. Monitor
8. Maintain
9. Patch, update, or renew
10. Troubleshoot
11. Replace or refresh
12. Decommission

For each lifecycle stage, identify:

- Customer pain points
- Current ownership gaps
- Fragmentation across vendors
- Existing Wesco touchpoints
- Relevant CSS Platforms capabilities
- Potential recurring service opportunities

## 2. Industry Pain-Point Inventory

Identify at least 15 specific pain points involving connected devices, software, licenses, firmware, configuration, security, maintenance, or lifecycle management.

For each pain point, state:

- Who experiences it
- What triggers it
- Why current solutions are inadequate
- Operational, financial, cyber, compliance, or customer-experience impact
- How frequently it occurs
- Why Wesco could credibly solve it
- What evidence would be needed to validate the problem

Avoid vague pain points such as "customers need better visibility." Make each one operationally concrete.

## 3. Product and Service Concept Portfolio

Generate 10 to 12 distinct product or managed-service concepts.

At minimum, include concepts related to:

- Firmware and software lifecycle management
- Device configuration assurance
- Secure remote device operations
- Cyber-hygiene and vulnerability response
- Asset discovery and installed-base reconciliation
- Warranty, entitlement, and support-status assurance
- Service orchestration and remote-to-field escalation
- Device end-of-life and refresh planning

Also generate additional concepts that are not obvious extensions of the initial hypothesis.

For each concept, provide:

- Product or service name
- One-sentence description
- Target customer
- Primary buyer
- User or operator
- Specific pain point
- Customer outcome
- Why Wesco
- Required platform capabilities
- New capabilities required
- Service-delivery model
- Initial device or software scope
- Expansion path
- Key risks
- Fastest validation test

## 4. Concept Scoring

Score every concept from 1 to 5 against the following criteria:

- Customer urgency
- Financial impact of the problem
- Willingness to pay
- Strategic adjacency
- Wesco channel and customer-access advantage
- Attachment to devices or software Wesco sells
- Recurring-revenue potential
- Managed-service suitability
- Ability to use Airwall
- Ability to use entroCIM capabilities
- Ability to use WAM data and workflows
- Ability to use Navigator without organizational dependency
- Reusability across multiple products
- Narrow-MVP feasibility
- Time to first customer value
- Gross-margin potential
- Differentiation
- Data advantage
- Cybersecurity and liability manageability
- Scalability across customers and manufacturers

Apply weights and explain the weighting. Do not manipulate the weights to force the firmware concept to win.

Present:

- Weighted score
- Confidence level
- Main evidence
- Main uncertainty
- Go, investigate, hold, or reject recommendation

## 5. Top Three Concept Deep Dives

Select the three strongest concepts.

For each, provide:

### Problem Definition

- Exact customer problem
- Current workaround
- Why the problem is becoming more important
- Economic and operational impact
- Ideal initial customer profile

### Product Definition

- Core service promise
- In-scope functions
- Out-of-scope functions
- Customer workflow
- Operator workflow
- Required approval and control points
- Audit and reporting model
- Service-level commitment

### Platform Contribution

Specify the role of:

- entroCIM
- ADM
- Strev
- Navigator
- Spanr, when relevant
- Airwall
- Azure
- On-premises edge compute
- New shared services

Distinguish between:

- Existing capability that can be reused
- Existing capability requiring extension
- Net-new product development
- Partner or OEM dependency

### Architecture

Provide a conceptual architecture covering:

- Customer devices and systems
- Secure Layer 3 access
- On-premises connector or edge node
- Azure-hosted components
- Data flows
- Command and control
- Credential handling
- Approval workflow
- Logging and evidence
- Update or action execution
- Validation
- Rollback
- Multi-tenancy
- Integration with WAM and Navigator
- Security boundaries
- Failure modes
- Offline or partially connected operation

Include a Mermaid architecture diagram.

### Service Operating Model

Define:

- Customer responsibilities
- Wesco responsibilities
- OEM or partner responsibilities
- Tier 1, Tier 2, and Tier 3 support
- Remote operations
- Field escalation
- Change windows
- Approval process
- Incident management
- Exceptions
- Service reporting
- Required staffing and skills
- 24x7 versus business-hours options

### Commercial Model

Recommend:

- Packaging
- Pricing metric
- Minimum annual commitment
- Per-site, per-device, per-customer, or outcome-based pricing
- Implementation fees
- Premium support tiers
- OEM or partner costs
- Target gross-margin logic
- Cross-sell and attach strategy
- Renewal model
- Land-and-expand path

Use reasonable ranges and clearly label assumptions.

### MVP

Define an MVP that can be piloted with a small number of customers and device types.

Include:

- Exact initial device categories
- Customer prerequisites
- Initial use cases
- Minimum software components
- Minimum integrations
- Manual processes acceptable during pilot
- Capabilities deferred
- Pilot duration
- Pilot success criteria
- Exit criteria
- Conditions that would stop further investment

## 6. Firmware Lifecycle Assurance Evaluation

Evaluate the initial firmware-management idea independently and rigorously.

Answer:

1. Is firmware management the correct initial wedge?
2. Which device categories are most suitable for launch?
3. Which device categories should be avoided initially?
4. Is the product primarily a cyber service, an operations service, an asset-lifecycle service, or a combination?
5. What customer approvals are required?
6. How should credentials be handled?
7. What rollback guarantees are technically realistic?
8. What happens when devices fail during an update?
9. How can Wesco avoid assuming unreasonable operational or product liability?
10. How much OEM cooperation is required?
11. What manufacturer APIs, protocols, or update mechanisms would be needed?
12. How should compatibility and pre-update checks work?
13. How should firmware advisories and vulnerability information be ingested?
14. What audit evidence should customers receive?
15. What role should ADM and Strev play?
16. When should Navigator create a work order?
17. What is the smallest useful version of this service?
18. What would make customers buy from Wesco instead of using OEM tools?
19. Could the initial product be broader than firmware and positioned as **Device Lifecycle Assurance**?
20. What adjacent services become possible once secure remote operations and device identity are established?

## 7. Recommended Product Thesis

Recommend one lead product thesis.

The recommendation must include:

- Product name
- Category definition
- Problem statement
- Target market
- Ideal customer profile
- Buyer
- Value proposition
- Service promise
- Why now
- Why Wesco
- Why CSS Platforms
- Why this is adjacent rather than a strategic departure
- Why it should be funded in the 2027 AOP
- Why competitors or OEMs have not already solved it adequately
- What makes the offering defensible
- Initial market entry point
- Long-term platform vision
- Expected revenue model
- Critical assumptions
- Major risks
- Evidence required before full funding

The recommendation must be concise enough to explain in under two minutes but supported by detailed analysis.

## 8. Shared Capability and Team Strategy

Explain how the product can be built without trapping the entroCIM or WAM teams inside another single-purpose solution.

Define:

- Shared components that should become platform services
- Capabilities owned by the entroCIM team
- Capabilities owned by the WAM team
- Capabilities that should be a new common platform layer
- Navigator integration boundaries
- Product management ownership
- Architecture ownership
- Service operations ownership
- Cybersecurity ownership
- OEM and partner management
- Field-service integration
- Data governance
- How the teams can support multiple products without excessive context switching
- What work should not be assigned to the existing teams
- Whether a dedicated product pod is required
- The minimum leadership and staffing model for 2027

## 9. 2027 AOP Investment Case

Create a preliminary investment case suitable for annual planning.

Include:

### Strategic Rationale

- Business problem
- Portfolio fit
- Revenue opportunity
- Service attach
- Customer retention
- Differentiation
- Reuse of existing assets
- Cross-portfolio leverage

### Funding Scenarios

Provide three scenarios:

1. **Discovery and pilot**
2. **Focused commercial launch**
3. **Accelerated platform build**

For each scenario, estimate:

- Product management
- Software engineering
- Solution architecture
- UX
- Cloud and infrastructure
- Cybersecurity
- Service operations
- Field support
- OEM integration
- Sales enablement
- Legal and risk
- Total estimated annual investment
- Expected milestones
- Number of pilot customers
- Revenue or bookings assumptions
- Time to commercial launch
- Major dependencies

Use ranges rather than false precision.

### Financial Logic

Provide a preliminary view of:

- Addressable customer base
- Plausible attach rate
- Annual contract value
- Gross-margin range
- Implementation revenue
- Recurring revenue
- Expansion revenue
- Three-year revenue potential
- Break-even logic
- Sensitivity to adoption, device count, OEM support, and service labor

Clearly separate assumptions from known facts.

## 10. Validation Plan

Create a 90-day validation plan before committing major AOP funding.

Include:

- Customer interviews
- Sales interviews
- Service-team interviews
- OEM and supplier interviews
- Technical feasibility tests
- Airwall connectivity proof of concept
- Device update or remote-action proof of concept
- Security and credential review
- Liability and contract review
- Pricing research
- Pilot-customer identification
- Competitive research
- Success measures
- Decision gates

For every activity, identify:

- Question being answered
- Owner
- Evidence required
- Timeframe
- Decision enabled

## 11. Risks and Governance

Evaluate:

- Cybersecurity
- Credential exposure
- Remote access
- Customer network risk
- Device failure
- Failed updates
- Incompatibility
- OEM warranty impact
- Unsupported devices
- Product liability
- Change-management failures
- Regulatory obligations
- Data privacy
- Multi-tenant isolation
- Service availability
- Field-service dependency
- Customer approval delays
- OEM dependency
- Vendor lock-in
- Insurance
- Contractual limitations
- Scalability of device support
- Team capacity
- Commercial adoption

For each major risk, provide:

- Likelihood
- Impact
- Mitigation
- Residual risk
- Executive decision required

---

# Required Outputs

Produce the final response in the following order.

## A. Executive Summary

No more than one page.

Include:

- The three most attractive industry problems
- The recommended product thesis
- Why Wesco can win
- Why it belongs in CSS Platforms
- What should be funded in 2027
- The immediate next decision

## B. Strategic Opportunity Map

A concise map of customer problems, lifecycle stages, and platform assets.

## C. Pain-Point Inventory

At least 15 specific problems.

## D. Product Concept Portfolio

10 to 12 concepts with consistent descriptions.

## E. Weighted Scoring Matrix

Rank all concepts and show the score logic.

## F. Top Three Deep Dives

Detailed analysis of the strongest concepts.

## G. Recommended Lead Concept

A clear investment thesis and value proposition.

## H. Conceptual Architecture

Include a Mermaid diagram and explanation.

## I. Service and Commercial Model

Define how the offering is sold, delivered, supported, and renewed.

## J. MVP and 90-Day Validation Plan

State exactly what should happen next.

## K. 2027 AOP Funding Options

Show discovery, focused launch, and accelerated investment scenarios.

## L. Executive Pitch

Provide all of the following:

### One-Sentence Value Proposition

Use this structure:

> For [target customer] that struggles with [specific problem], [product name] is a [category] that [measurable outcome]. Unlike [current alternative], it uses [Wesco advantage] to [differentiated result].

### 30-Second Pitch

Use plain executive language.

### Two-Minute Pitch

Explain the problem, solution, strategic fit, revenue model, and funding ask.

### Funding Slide Content

Provide concise content for one executive slide with:

- Problem
- Proposed offering
- Customer value
- Wesco advantage
- Business model
- 2027 ask
- Expected milestone

### Decision Memo

Conclude with:

- Recommendation
- Funding request
- Stage gate
- Key assumptions
- Required executive sponsors
- Decision needed

---

# Evaluation Standards

The response will be considered strong only if it:

- Identifies concrete customer problems rather than generic trends
- Produces ideas that are adjacent to Wesco CSS
- Creates a clear recurring-service opportunity
- Uses Airwall and cloud-to-edge connectivity meaningfully
- Uses entroCIM as a capability, not automatically as a full deployment
- Uses WAM to connect operational state with asset and lifecycle intelligence
- Uses Navigator for orchestration without making it an organizational dependency
- Creates reusable capabilities across products
- Defines a narrow and credible MVP
- Addresses cybersecurity, rollback, liability, and operational control
- Explains why Wesco is a credible provider
- Includes a commercial and service-delivery model
- Supports an AOP funding decision
- Distinguishes facts, assumptions, and hypotheses
- Makes a clear recommendation instead of presenting an unprioritized list

---

# Research and Evidence Requirements

Use all available internal context and project materials.

Where external research is available:

- Validate industry pain points with current, credible sources
- Review relevant OEM capabilities and limitations
- Identify competing managed services and software products
- Look for cybersecurity, firmware, asset-lifecycle, and device-management trends
- Cite factual claims
- Distinguish market evidence from inference
- Note where customer discovery is still required

Do not invent Wesco capabilities, customer commitments, OEM integrations, market size, or financial results.

When evidence is incomplete, state:

- What is known
- What is assumed
- What must be validated
- How it should be validated

---

# Working Style

Be rigorous, commercially realistic, and willing to reject weak ideas.

Do not simply confirm the initial firmware concept.

Use the firmware concept as one candidate, compare it against other high-value problems, and recommend the strongest product thesis.

Favor a focused wedge with a broader platform path.

The final recommendation should be specific enough to guide:

- Customer discovery
- Architecture decisions
- 2027 staffing
- AOP funding
- Pilot selection
- Commercial packaging
- Executive communication
