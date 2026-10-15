# CSS Platforms 2027 — Phase 2 Deep-Dive Brief
Date: 2026-07-23 | Supersedes the Phase 2 section of the Cowork Master Prompt for execution purposes. Paste this document alone into ChatGPT. Decided state is settled; do not re-open Phase 1 questions.

# Role

Act as my product strategist, solution architect, managed-services operator, commercial-model advisor, and evidence lead. Be rigorous. Depth over breadth. Cite external claims. Label assumptions. Do not pad weak sections.

# Decided State (settled at Checkpoint 1, 2026-07-23 — build on this, do not revisit)

## The proposition
**Connected Device Assurance as a Service**: a recurring managed service in which Wesco assumes accountability for defined aspects of the operational, software, security, and support condition of covered connected devices, with customer approval workflows, validation, evidence, and field escalation.

## The modules (deep-dive all three)
- **A. Firmware and Configuration Assurance** — devices stay on approved firmware and configuration baselines.
- **B. Device Health and Recovery** — faults detected, diagnosed, resolved remotely; field dispatch with a complete work package when not.
- **D. Cyber Hygiene and Compliance** — split scope: *visibility* (posture assessment, vulnerable/EOL/default-credential reporting; candidate base-tier content) vs. *remediation* (credential rotation, certificate lifecycle; higher trust bar, later sequencing).
- **Refresh/EOL intelligence is embedded, not sold**: every module writes lifecycle, failure, and end-of-support signals back to our asset platform (WAM), generating refresh and renewal opportunities for Sales. It carries the hardware pull-through story.

## The product
**The container IS the product.** The platform ships as a container (or container set) with three deployment modes:
1. On premises on a Wesco-supplied small-form-factor PC (Ubuntu).
2. On premises on the customer's own server.
3. Fully remote: an Azure-hosted container reaching site devices over an Airwall Layer 3 link, no on-premises compute.

Arcbeam (entroCIM) connects and clusters distributed instances into one operable estate. Airwall provides the secure path to remotely control, log in, manage, and maintain on-premises instances. Pods are internal entroCIM capability (a firmware pod is a new pod inside entroCIM), not the product packaging. entroCIM containerization investment is already underway under approved security governance. Additional containers ride the same delivery: Nozomi (partner capability), Navigator components, future modules. The container estate manages its own lifecycle with the same assurance framework it sells.

## Scope and constraints
- Launch manufacturers: Hanwha, Axis (cameras); Dormakaba, HID (access control); Cisco (IT equipment). Plus any device exposing an open telemetry protocol and an available API.
- Firmware rights are a **per-vendor qualification hurdle**, not a concept gate (market precedent: third-party solutions exist). Do not penalize firmware concepts for it; treat it as vendor selection.
- Navigator is an integration partner; concepts must remain viable without organizational control of it.
- Rollback standard: OEM-supported rollback where available and validated; otherwise defined recovery, isolation, replacement, or field remediation. Never promise universal rollback.
- Advancement gates apply to every module: (A) named service-owner function, (B) pricing/packaging hypothesis, (C) measurable benefits with baselines, (D) dependencies with owner functions, dates, consequences.
- Service ownership interface must be stated (product/platform team vs. managed-services delivery vs. commercial execution). "Operating model TBD" is not acceptable.
- **Partnership lens (mandatory)**: for every capability gap, assess build vs. partner vs. buy. Explicitly evaluate SecuriThings and Viakoo as license/white-label partners rather than competitors, and Nozomi (especially Arc) as partner for cyber posture. Precedents: Strev (white-labeled partner platform), Airwall (partner under MSP agreement), Ascent (delivery partner). Build only what differentiates: orchestration, WAM integration, evidence and commercial-signal loop, service delivery.
- Commercial backdrop: CSS software sales and hardware pull-through are materially behind target at mid-year 2026; the funding case must lead with recurring revenue and installed-base monetization. AOP input is due **2026-08-31**; the MVP must be credibly pilotable in 2027.

# Task

## Part 1 — Per module (A, B, D)
1. **Problem and buyer**: exact problem, current workaround, buyer and budget source, ideal initial customer profile, willingness-to-pay evidence.
2. **Service definition**: service promise, in scope, out of scope, customer workflow, operator workflow, approval model, service levels, reporting and evidence.
3. **Platform contribution**: for each component (entroCIM incl. new pods, Arcbeam, Airwall, Azure, WAM, Navigator, Nozomi or other partner, container packaging, estate/fleet management), classify: existing / extension / net-new / partner-supplied / unnecessary.
4. **Commercial model**: pricing metric and tiers, minimum commitment, implementation fee, expansion path, pull-through attach. Include a **zero-touch entry tier** built on deployment mode 3 (remote over Airwall, nothing installed but the Airwall) graduating to on-prem modes as coverage grows — land-and-expand.
5. **Dependency gates** per the four-gate discipline, with owner functions and dates.
6. **Risks**: top five with mitigations; liability boundary explicitly stated.

## Part 2 — Cross-module (the product decisions)
7. **Architecture**: one architecture for the deploy-anywhere container serving all three modules across the three deployment modes. Cover: device connectivity, command and control, credentials, approval, logging/evidence, validation, recovery, multi-tenancy, Arcbeam clustering, Airwall management path, WAM integration, Navigator escalation, security boundaries, failure modes. Include a Mermaid diagram. Note where the fully-remote mode constrains module capability (e.g., local protocol access).
8. **Shared enablement layer**: exactly what gets built once and reused across modules; what is module-specific; what is partner-supplied. This is the funding object — be precise.
9. **Estate/fleet management**: how container instances are provisioned, updated, monitored; build/partner/buy recommendation (e.g., k3s, Azure IoT Edge, Portainer-class, or partner tooling).
10. **MVP composition recommendation**: which module(s) launch first, on which deployment mode(s), with which manufacturers, and why; pilot profile, duration, success criteria, stop conditions.
11. **Service operating model**: the three-way ownership interface, tiered support, staffing for pilot scale, business-hours vs. 24x7 options.
12. **Competitive and evidence review** (cited): SecuriThings, Viakoo, Nozomi (Arc), Axis Device Manager and OEM utilities, managed-service competitors, new entrants; pricing indicators; regulatory/insurance drivers; for each named launch manufacturer, firmware/API accessibility and update mechanisms. Mark every unverified claim.

# Output rules
- Distinguish fact, evidence, assumption, and hypothesis throughout.
- Ranges, not false precision, for all financials.
- Preserve open questions in a dedicated list.
- Stop after producing this. Do not produce funding scenarios, pitch materials, or AOP packaging (that is Phase 3). Ask me to select the MVP composition.

**Exit criterion:** one recommended MVP composition with verified or credibly-cited differentiation, a defined shared enablement layer, and no unexamined make-or-break dependency.
