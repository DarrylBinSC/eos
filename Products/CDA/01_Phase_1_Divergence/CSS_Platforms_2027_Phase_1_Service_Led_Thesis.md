# CSS Platforms 2027 Product Ideation
# Phase 1 — Service-Led Product Thesis and Revised Shortlist

**Date:** July 23, 2026  
**Owner:** Darryl Benson  
**Purpose:** Reframe the Phase 1 shortlist so the customer-facing product is explicitly sold and delivered as a service, while the technology investment is justified by the revenue and operating leverage it creates across adjacent CSS Platforms capabilities.

---

# 1. Core Correction

The new product should not be presented primarily as:

- A connector framework
- A POD framework
- A remote-access platform
- A monitoring platform
- A lifecycle platform
- A work-order platform

Those are enabling capabilities.

The fundable proposition is a **repeatable managed service** that produces measurable customer outcomes and creates recurring revenue, hardware and software pull-through, and service-delivery leverage.

The product investment should therefore be evaluated in this order:

1. **What service does the customer buy?**
2. **What measurable outcomes does the service deliver?**
3. **What capabilities does the service-delivery organization need to deliver it efficiently and repeatedly?**
4. **Which existing CSS Platforms technologies provide those capabilities?**
5. **What narrow product gaps must be funded?**
6. **How does the service produce recurring revenue and adjacent product sales?**

Technology architecture follows the service and commercial model.

---

# 2. Revised Commercial Thesis

## Connected Device Assurance as a Service

CSS should offer a recurring managed service that assumes responsibility for defined aspects of the operational, software, security, and support condition of covered customer devices.

The service should provide a clear promise:

> Wesco will continuously assess covered devices, identify required action, manage customer approvals, perform supported remote remediation, validate the result, document the outcome, and coordinate field service or replacement when remote resolution is not possible.

The customer is not buying a tool they must staff.

The customer is buying:

- Coverage
- Accountability
- A defined service level
- Controlled device action
- Evidence
- Exception management
- Escalation
- Lifecycle recommendations
- Reduced operational burden

The technology investment is justified because it allows CSS Managed Services to deliver this service at scale across customers, sites, and device families.

---

# 3. Product, Service, and Platform Boundaries

## Customer-Facing Product

The customer-facing product is:

**Connected Device Assurance as a Service**

It should be packaged as a recurring service with defined coverage, supported device classes, service levels, reporting, and response commitments.

## Service Delivery Function

The service-delivery organization owns:

- Customer onboarding
- Service activation
- Device coverage confirmation
- Daily operations
- Approval management
- Remote action execution
- Exception handling
- Incident response
- Customer communication
- Service reporting
- Field escalation
- SLA performance
- Continuous service improvement

## Product and Platform Function

CSS Platforms provides the service-delivery organization with a repeatable product capability that:

- Connects to supported devices
- Reads operational and software state
- Normalizes device interactions
- Applies service policies
- Generates action recommendations
- Manages approvals and scheduling
- Executes authorized actions
- Validates outcomes
- Captures evidence
- Creates structured escalation packages
- Updates WAM
- Opens work in Navigator or another work-management platform
- Produces service metrics
- Supports cloud, on-premises, edge, and hybrid delivery

## Commercial Function

Commercial execution owns:

- Target-account selection
- Pipeline
- Service positioning
- Pricing
- Contracting
- Hardware and software attachment
- Renewal
- Expansion
- Refresh conversion
- OEM and supplier commercial alignment

---

# 4. Service Delivery Outcomes the Product Must Provide

The product should not merely expose technical functions.

It should provide the service-delivery organization with operational outputs that can be acted upon.

## 4.1 Covered Device Population

The product provides:

- Confirmed device identity
- Site and customer association
- Device family and model
- Current connectivity state
- Supported service modules
- Current supportability
- Confidence level
- Exceptions requiring manual reconciliation

**Service outcome:** The delivery team knows exactly which devices are in scope and which are not.

## 4.2 Prioritized Service Work Queue

The product provides:

- Devices requiring attention
- Reason for action
- Severity
- Customer impact
- Recommended response
- Required approval
- Maintenance-window constraints
- Supporting evidence

**Service outcome:** Operators work from a prioritized queue rather than raw alerts.

## 4.3 Approved Action Plan

The product provides:

- Proposed action
- Target devices
- Dependencies
- Compatibility checks
- Risk level
- Rollout sequence
- Validation steps
- Recovery plan
- Customer approval status

**Service outcome:** The service team can execute controlled, repeatable changes.

## 4.4 Remote Execution Package

The product provides:

- Device connector
- POD workflow
- Required credentials or authorization
- Execution target
- Scheduled window
- Action steps
- Logging
- Validation
- Exception handling

**Service outcome:** The delivery team can perform supported work consistently across customers.

## 4.5 Validated Service Result

The product provides:

- Success or failure
- Before-and-after state
- Functional validation
- Remaining exceptions
- Recovery action
- Customer-visible evidence
- WAM update
- Work-order requirement

**Service outcome:** The operator can prove what happened and close the service event.

## 4.6 Remote-to-Field Escalation Package

When remote resolution is not possible, the product provides:

- Diagnosed condition
- Device identity and location
- Prior actions attempted
- Recommended field action
- Required parts
- Warranty and entitlement status
- Technician instructions
- Required evidence
- Closure validation

**Service outcome:** Field teams receive a complete work package rather than a generic ticket.

## 4.7 Lifecycle and Commercial Signal

The product provides WAM and Commercial teams with:

- Repeated failure history
- Unsupported firmware
- Configuration limitations
- End-of-support status
- Failed recovery
- Warranty eligibility
- Replacement recommendation
- Renewal or service opportunity

**Service outcome:** Operational evidence becomes a qualified lifecycle or refresh opportunity.

## 4.8 Service Performance Reporting

The product provides:

- Devices covered
- Devices compliant
- Actions completed
- Exceptions
- Mean time to action
- Mean time to recovery
- Remote-resolution rate
- Field escalations
- Avoided truck rolls
- Unsupported devices
- Refresh opportunities
- SLA performance

**Service outcome:** The Managed Services organization can demonstrate value, manage margin, and support renewal.

---

# 5. Technology Adjacencies

The architecture should maximize use of the current technology base.

## entroCIM

entroCIM is the primary device interaction and operational-integration layer.

Use:

- Existing connectors
- New device-specific connectors where required
- Protocol support
- API support
- Telemetry
- Rules
- Remote actions
- Validation
- POD framework
- Cloud and on-premises execution patterns

Do not create a second connector framework.

## POD Framework

PODs provide focused, service-specific functionality.

Potential PODs include:

- Firmware assurance
- Configuration assurance
- Device health
- Recovery
- Credential operations
- Certificate operations
- Evidence collection

A POD should package the operational logic required by a service module without requiring a complete traditional entroCIM deployment.

## Airwall

Airwall provides secure Layer 3 access where local device communication is required.

Use it to:

- Reach devices without broad VPN access
- Constrain connectivity
- Support remote diagnostics
- Support controlled actions
- Minimize on-site footprint

Airwall should be positioned as a service-enabling connectivity component, not the product itself.

## Azure, On-Premises, and Edge

The same service capability should support:

- Azure-hosted execution
- Per-customer VM or container deployment
- On-premises deployment
- Edge deployment
- Hybrid deployment

This flexibility is commercially important because customer security and network requirements will differ.

## WAM, ADM, and Strev

WAM remains the asset and commercial lifecycle system.

The service should consume:

- Asset identity
- Manufacturer
- Model
- Serial
- Warranty
- Entitlement
- Support status
- End-of-life status
- Replacement information

The service should write back:

- Firmware state
- Configuration state
- Health state
- Action history
- Failure history
- Recovery result
- Replacement trigger

Do not recreate WAM functions.

## Navigator

Navigator or another work-management platform should receive:

- Escalation
- Work scope
- Device and location
- Parts requirements
- Technician instructions
- Evidence requirements
- Closure criteria

Do not create another work-order platform.

## AI

AI should improve service productivity through:

- Device-to-WAM matching
- Advisory interpretation
- Release-note analysis
- Risk prioritization
- Event correlation
- Anomaly detection
- Recommended actions
- Exception summarization
- Technician instructions
- Customer reporting
- Refresh recommendations

AI should assist service decisions, not replace deterministic controls for high-risk actions.

---

# 6. Revised Shortlist

## 1. Connected Device Assurance as a Service

### Commercial definition

A recurring managed service under which Wesco assumes responsibility for assessing, prioritizing, remediating, validating, and reporting on defined aspects of covered connected devices.

### Customer outcome

- Reduced operational burden
- Better device availability
- Improved software and configuration posture
- Faster response
- Fewer site visits
- Better audit evidence
- Planned lifecycle decisions

### Revenue model

- Annual managed-service contract
- Per-device, per-site, or estate pricing
- Service tiers
- Onboarding fee
- Premium response options
- Field service billed separately or included by tier
- Hardware, warranty, support, and software attachment

### Product investment

Fund the reusable service-enablement capability required to let Managed Services deliver this consistently and profitably.

### Essential product outputs to service delivery

- Covered-device population
- Prioritized work queue
- Approval workflow
- Remote execution
- Validation
- Evidence
- Exception management
- Field escalation
- Service reporting
- Commercial signals

### Phase 2 question

Can this be defined as a sufficiently concrete service category, or must it launch through a narrower initial module?

---

## 2. Firmware and Configuration Assurance as a Service

### Commercial definition

A recurring service that keeps supported customer devices on approved firmware and configuration baselines through managed assessment, approval, execution, validation, and exception handling.

### Customer outcome

- Improved firmware compliance
- Reduced cyber exposure
- Reduced configuration drift
- Controlled change
- Audit evidence
- Fewer emergency remediation events
- Clear replacement path for unsupported devices

### Revenue model

Possible tiers:

1. **Visibility**
   - Firmware and configuration status
   - Risk identification
   - Reporting

2. **Assurance**
   - Policy
   - Approval workflow
   - Scheduled remediation
   - Validation

3. **Managed Response**
   - Priority advisory response
   - Expedited remediation
   - Recovery coordination
   - Field escalation

### Product outputs to service delivery

- Current state
- Approved target state
- Compatibility assessment
- Risk-prioritized work queue
- Customer approval
- Staged rollout plan
- Execution workflow
- Validation
- Recovery plan
- Evidence
- WAM update
- Navigator escalation

### Technology leverage

- entroCIM connectors
- POD framework
- OEM APIs
- Airwall
- Azure/edge
- WAM
- Navigator
- AI-assisted advisory and release-note analysis

### Revenue and pull-through

- Recurring per-device revenue
- Airwall or edge attachment
- Support and warranty attachment
- Replacement of unsupported devices
- Professional and field services
- Customer expansion to additional device families

### Phase 2 question

Can one or two high-volume camera manufacturers support a legal, technically safe, repeatable, and margin-positive service?

---

## 3. Remote Device Health and Recovery as a Service

### Commercial definition

A recurring service that continuously validates supported device function, diagnoses faults, performs authorized remote recovery, and coordinates field service when remote resolution fails.

### Customer outcome

- Higher device availability
- Faster detection
- Faster recovery
- Fewer truck rolls
- Better first-time fix
- Lower support cost
- Better evidence
- Better replacement decisions

### Revenue model

Possible tiers:

1. **Health Visibility**
   - Functional monitoring
   - Reporting
   - Alert prioritization

2. **Managed Diagnosis**
   - Triage
   - Root-cause analysis
   - Recommended action

3. **Managed Recovery**
   - Approved remote actions
   - Validation
   - Escalation

4. **Full Service Assurance**
   - SLA
   - Field coordination
   - Parts and replacement workflow
   - Business-hours or 24x7 options

### Product outputs to service delivery

- Functional health state
- Prioritized incidents
- Diagnosis
- Recommended recovery
- Approved action
- Remote execution
- Validation
- Escalation work package
- Incident history
- WAM update
- Service metrics

### Technology leverage

- entroCIM telemetry, rules, connectors, and PODs
- Airwall
- Azure/edge
- WAM
- Navigator
- AI event correlation and anomaly detection

### Revenue and pull-through

- Recurring per-device or per-site service
- Airwall or edge attachment
- Field service
- Replacement devices
- Parts
- Warranty and support
- Expansion to more sites and device classes

### Phase 2 question

Can Wesco demonstrate sufficient remotely diagnosable and resolvable incident volume to create attractive service margins?

---

# 7. Recommended Product Structure

The recommended structure is:

## Customer-Facing Service Portfolio

**Connected Device Assurance as a Service**

With initial modules:

- Firmware and Configuration Assurance
- Remote Device Health and Recovery

## Internal Product Capability

**Connected Device Service Enablement Layer**

Built from:

- entroCIM connectors
- PODs
- API framework
- Airwall
- Azure/on-premises/edge
- Approval workflow
- Action orchestration
- Validation
- Evidence
- Service reporting
- WAM integration
- Navigator integration
- AI assistance

The internal capability is not the primary customer proposition.

It exists to make the service:

- Repeatable
- Scalable
- Secure
- Measurable
- Profitable
- Expandable across device classes

---

# 8. Funding Logic

Funding should be justified through service economics, not technology potential alone.

The case must show:

## Revenue

- Target customers
- Service pricing
- Number of devices or sites
- Annual contract value
- Pilot-to-production conversion
- Expansion path
- Renewal model

## Pull-Through

- Hardware replacement
- Software
- Licenses
- Warranty
- Support
- Airwall
- Edge compute
- Field service
- Deployment
- Professional services

## Margin

- Devices per operator
- Automation rate
- Exception rate
- Remote-resolution rate
- Field-escalation rate
- OEM-support effort
- Cloud and infrastructure cost
- Connector maintenance cost
- Service-delivery labor

## Reuse

- Existing connectors reused
- Existing POD capability reused
- Existing Airwall capability reused
- Existing Azure and edge patterns reused
- WAM integration reused
- Navigator integration reused
- Shared capability across future services

## Avoided Duplication

The plan should explicitly show that it does not fund:

- A second WAM
- A second work-order platform
- A second connector framework
- A second monitoring platform
- A new generic dashboard

---

# 9. Phase 2 Evaluation Criteria

Each candidate service must prove:

1. A named buyer
2. A measurable customer outcome
3. A credible annual contract value
4. A clear service owner
5. A repeatable service-delivery workflow
6. Product outputs that reduce service labor
7. A defined supported-device scope
8. A narrow MVP
9. Hardware or software pull-through
10. Reuse of existing technology
11. No material platform overlap
12. Manageable cyber and liability risk
13. A credible gross-margin path
14. Customer willingness to permit the access model
15. A path from one module to a broader service portfolio

---

# 10. Revised Recommendation

Advance the following service-led structure into Phase 2:

1. **Connected Device Assurance as a Service**  
   The umbrella customer proposition and recurring service category.

2. **Firmware and Configuration Assurance as a Service**  
   A candidate first module focused on cyber posture, controlled maintenance, and compliance.

3. **Remote Device Health and Recovery as a Service**  
   A candidate first module focused on availability, service cost, and remote resolution.

Architect each service by composing existing capabilities from entroCIM, WAM, Airwall, Azure/on-premises/edge, Navigator, and Managed Services.

Fund only the product gaps required to enable repeatable service delivery, measurable customer outcomes, recurring revenue, and adjacent technology and service pull-through.
