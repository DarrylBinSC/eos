# Connected Device Assurance — Business Case Appendix

Companion to `CDA_Wesco_Business_Case_v2.docx`. Created 2026-08-11.

The version-two business case was shortened for an executive AOP audience. This appendix holds the detail that was removed from it. Nothing here is new material; every item is carried forward verbatim or near-verbatim from version one so that the technical, security, and delivery content remains available to reviewers who need it.

Referenced from two places in the business case: the Nonfunctional Requirements cell ("Full nonfunctional detail is in the appendix") and the Links section.

---

## 1. Nonfunctional requirements, full detail

**Security.** Least-privilege access to customer devices; segregated credential handling with no shared or embedded credentials; customer-approved connectivity; alignment with Wesco cyber governance and customer security review.

**Change control.** No action on a customer device without recorded authorization, an approved window, and pre-change validation.

**Auditability.** Immutable evidence record per action, retained to a defined period, exportable to the customer.

**Availability and performance.** Service platform availability appropriate to a business-hours managed service, with defined behavior on loss of connectivity, including local buffering and safe resumption.

**Scalability.** Support growth from pilot footprint to multi-site, multi-customer production without per-customer custom engineering.

**Multi-tenancy.** Strict tenant isolation of device data, evidence, and credentials.

**Data handling.** Customer data segregated by tenant with defined retention. Used to deliver the service and, under the customer agreement, to enable connected Wesco services such as WAM, entroCIM services, and Navigator. Not sold; no disclosure outside the service delivery chain without customer permission.

**Supportability.** Defined tiered support model with escalation to engineering, manufacturer, or partner.

**Compliance alignment.** Capability set mapped to recognized device-security guidance (NIST and CISA references), without claiming certification.

---

## 2. Service node engineering and operations

Removed from the business case In Scope list because it is build detail rather than service scope. Ownership sits with CSS Platforms IT, which is stated in the business case; the tasks below are the underlying work.

- Hardware selection and qualification for the containerized service node, including specification, sourcing, and supported configurations.
- Node build and integration: operating system, container runtime, service tools, partner sensor, and connectivity components.
- Security hardening of the node and container images to Wesco standards, with customer security review support.
- Container deployment testing: build, staged rollout, update, rollback, and recovery validation.
- Operational runbook covering provisioning, deployment, monitoring, update, incident response, and decommissioning.
- Ongoing node and container fleet management, operated by CSS Platforms IT.

Related category analysis on how the node fleet is managed, including vendor comparison, is held in `02_Phase_2_Dossiers/RMM_Category_Review_2026-07-28.md`.

---

## 3. In-scope capabilities, expanded detail

The business case groups these into seven summary paragraphs. The itemized form follows.

### Establish the compliance framework

- Device intake and registration process design, integrated with purchasing, project intake, and facilities work orders.
- Device classification and risk-review model, including managed and unmanaged determination and required controls by class.
- Approval and deployment standards: network zone, identity model, and support plan per device class.
- Exception register and remediation path for non-compliant and unsupported assets.
- Retirement and replacement policy tied to end-of-support identification.
- Evidence and reporting pack aligned to recognized guidance for audit use.

### Identify

- Automated discovery of connected devices on covered networks, with make, model, firmware version, and support status.
- Device record creation and reconciliation against Wesco asset data.
- Vulnerability and known-advisory correlation to covered devices.
- End-of-support and end-of-life identification.

### Monitor

- Continuous device health and availability checks.
- Continuous security posture assessment, including firmware currency and configuration exposure.
- Vendor advisory ingestion and impact assessment against the covered installed base.
- Prioritized service work queue for Managed Services operators.
- Customer-facing posture, activity, and service reporting.

### Manage

- Approved firmware and configuration baselines by device family.
- Compatibility and prerequisite checking prior to change.
- Change planning, scheduling, and maintenance-window management.
- Customer approval workflow with recorded authorization.
- Lifecycle and refresh recommendations delivered to Wesco Sales.

### Execute

- Remote firmware update execution with staged rollout.
- Post-change validation of device function.
- Supported rollback, or defined recovery, isolation, replacement, or field-remediation path.
- Exception handling and escalation to field service with a complete work package.
- Evidence capture for every action: approval, execution, validation, outcome.

### Platform and integration

- Wesco Device Assurance (Base) and Wesco Configuration Assurance (Advanced) service tools, built on the entroCIM platform.
- Partner sensor integration by API for endpoint and OT discovery and vulnerability context.
- Deployment on a containerized service node (Wesco-supplied small-form-factor PC or customer server), with secure remote connectivity for service delivery and management.
- WAM integration for asset identity, lifecycle, warranty, and refresh signals.
- Navigator integration for field work orders and closure, aligned to the 2027 redesign.
- Multi-tenant service delivery, role-based access, and service metering.

---

## 4. Out of scope, full list

The business case carries a consolidated seven-item version. The full list from version one follows.

- Guarantee of device availability, or any commitment beyond the contracted monitoring, response, and remediation for covered devices.
- Universal firmware rollback; recovery is limited to manufacturer-supported rollback or the defined recovery and field-remediation path.
- Remediation of unsupported, end-of-life, or customer-modified devices beyond identification and replacement recommendation.
- Credential rotation, certificate lifecycle management, and autonomous hardening; these are later capabilities, not part of this investment.
- Security operations center services, managed detection and response, threat hunting, and incident response.
- Compliance certification or attestation on behalf of the customer.
- Support for all device manufacturers at launch; coverage expands by qualified device family.
- Full network, VMS, or IT infrastructure management.
- Twenty-four by seven human response at launch; a premium tier is considered only after volume and economics are proven.
- Replacement of Wesco asset management or field service platforms; this service integrates with them rather than duplicating them.
- Ownership of the customer's security policy, procurement policy, or risk-acceptance decisions.
- Acting as the customer's named asset owner or executive sponsor.

---

## 5. Positioning statement

Retained in the business case Investment Description at Darryl's direction, 2026-08-11, on the basis that it is part of the template. Reproduced here for reference.

For security, facility, and IT/OT operations leaders accountable for cyber risk in connected-device footprint, who face growing exposure from under-managed and unmanaged devices (out-of-date firmware, unpatched vulnerabilities, degrading security posture, incomplete inventory, and device health discovered only at failure), the Connected Device Assurance Services offering is a recurring managed service that keeps device firmware, configuration, health, and security posture current through one platform and one interface, on site or delivered from the Wesco cloud, with automated discovery to establish and maintain coverage. It measurably reduces device cyber risk and downtime through continuous posture visibility, customer-approved remediation, validated outcomes, audit-ready evidence, and planned lifecycle and refresh recommendations. Unlike per-manufacturer utilities the customer must staff, periodic assessments that age the day they are delivered, or point tools that stop at visibility, our solution puts an accountable service behind the risk: one interface across manufacturers, remediation rather than reporting alone, device condition connected directly to replacement and field service through Wesco's system integrator relationships, and a foundation that extends into Wesco's asset management and facility services without a second onboarding.

---

## 6. Change record, version one to version two

| Area | Change |
|---|---|
| Investment Description | Reduced from about 800 words to about 270. Positioning statement retained unchanged. |
| Business Outcome | Twelve measures to ten; advisory revenue folded into the revenue line; timeline wording aligned to the corrected 2027 plan. |
| Risks of not doing | Six paragraphs to six single lines under one lead paragraph. |
| In Scope | About 40 bullets to seven grouped paragraphs. Service node engineering moved to this appendix, section 2. |
| Nonfunctional requirements | Nine items to six. Full text in this appendix, section 1. |
| Out of Scope | Twelve items to seven, consolidated by theme. Full list in this appendix, section 4. |
| Customers affected | Trimmed about 30 percent, no content removed. |
| Dependencies | All eleven retained, each compressed to one line. |
| In-house or outsourced | Light trim. "entroCIM service tools" changed to "entroCIM platform-based service tools" throughout. |
| Resources and capacity | Restructured into five grouped lines. Resource Managers question answered: yes, all development resource managers contacted. |
| Investment cost, planned year | Restructured into a bucket list. Amount now sourced from the CDA P&L model. |
| Estimated total costs | Rewritten to state that the total scales with device, site, and customer count, and to separate scaling buckets from fixed buckets. |
| Benefit and timeline | Corrected. Version one showed 2026 funded validation; the plan is 2027 product development for eight months, an August 2027 product approval gate, then the pilot. Production follows pilot completion. |
| Links | Each source reduced to citation plus one line. Four internal working files replaced with a single "presented and discussed internally" summary. |
| Scoring | Twelve of thirteen controls were already answered in version one and were left unchanged. Implementation Cost set to less than $1 Million. A framing paragraph was added above the grids. Work Dependencies detail prompt answered. |
| Spelling | "envrionment" corrected to "environment" in all four occurrences. |

---

## 7. Open items in version two

1. `[target] percent` placeholder in Business Outcome, firmware currency target for the first service year. Owner: Darryl with Brad Stevens.
2. Pilot start and end months, and the production start year. Deliberately not asserted in the document; add once the 2027 development schedule is fixed.
3. CDA P&L model file not yet named in the document. Referenced generically.
4. Pilot customer not named. Tracked as a dependency.
