# RMM Category Review — Field Node Management Layer
2026-07-28. Prompted by Darryl: prior operational experience using an MSP management tool (NinjaOne) for services that place hardware in the field. Question: what does the category offer, who are the leaders, and where does it sit in the CDA product stack?

## Why this layer exists

The containerized service node creates a management obligation below the product itself: the physical SFF box, its Ubuntu OS, disks, certificates, agents, and network state must be monitored, patched, and serviceable at fleet scale. The ChatGPT Phase 2 dossier (§9) *recommended* K3s + Azure Arc + Flux GitOps for the container/workload layer with Portainer-class tooling as a pilot accelerator. **Status correction (07-28, Darryl):** that was a dossier recommendation only — never adopted in the decision log, and not tools the team operates today. The RMM category addresses the *device and OS* layer and the service-desk workflow on top of it; the open question is which instrument anchors node management given the team's actual operating capability.

## What NinjaOne offers (category-representative)

Cloud-native RMM / unified endpoint management: agent-based monitoring and alerting, cross-OS patch management (Windows, macOS, Linux including Ubuntu 22.04; Patch Intelligence AI added Jan 2026), remote access and remote terminal, scripting and task automation with auto-remediation, asset inventory, SNMP device monitoring, backup, ticketing/helpdesk, documentation, MDM. Per-device pricing; published figures range roughly $1.50/endpoint/month at 10,000 endpoints to $3.75 at ≤50 devices (source: competitor comparison content; verify direct with vendor). Positioned as the current category leader on usability and support.

Relevant caveat from category analysts: RMM platforms are optimized for standard computing devices (servers, laptops), not specialized appliances, kiosks, cameras, or OT/connected products. Linux feature depth is consistently shallower than Windows across the category.

## Competitive landscape

| Vendor | Model | Notes for our use case |
|---|---|---|
| NinjaOne | Per-device | Category leader on UX/support; solid Ubuntu agent (monitor, patch, terminal); Darryl has operating history with it |
| Datto RMM (Kaseya) | Per-device | SMB/MSP focus; Kaseya portfolio consolidation; Kaseya supply-chain history (VSA, 2021) is a diligence item |
| ConnectWise Automate/RMM | Quote-only | Deep MSP suite (PSA integration); heavier platform; pricing opaque |
| N-able N-central / N-sight | Per-device | Strong network/complex-estate management; built-in security stack (EDR, vuln scan) |
| Atera | Per-technician | All-in-one incl. PSA; per-tech pricing favors small teams managing many devices |
| Syncro, SuperOps, Pulseway | Per-tech / mixed | Mid-tier MSP alternatives; SuperOps AI-forward |
| Canopy (adjacent) | Specialized | Purpose-built for fielded connected products/appliances (kiosks, cameras, OT hardware) rather than IT endpoints — closest analog to our actual problem; worth a look |
| Azure Arc + Update Manager + Monitor (adjacent) | Azure meters | Not an RMM; covers Linux server inventory, patching, monitoring, SSH access. Dossier-recommended, never adopted; not a current team capability |

Category dynamics: consolidation (Kaseya owns Datto), two pricing camps (per-device vs per-technician), and AI-assisted patching/remediation as the current feature race.

## Fit assessment against the decided architecture

Facts: the node is a small, uniform, Linux-only appliance fleet, fully owned by Wesco, with an Airwall as the secure management path (decided architecture semantics: Airwall link = manage, Arcbeam = run from cloud). Fleet tooling above the Airwall is open.

1. **Capability fit.** The dossier's K3s + Azure Arc + Flux recommendation would cover patching, monitoring, and drift control, but it presumes platform-engineering skills the delivery team does not have. An RMM provides monitoring, patching, alerting, scripting, and technician workflow in the operating model the team already runs. For a service business, the tool the operators can run today beats the architecturally purer tool nobody operates (Darryl, 07-28).
2. **Channel proliferation (risk).** Every RMM is agent-plus-vendor-cloud. Adding one gives the node a fourth northbound channel (Arcbeam, Airwall, Azure Arc, RMM) and a second privileged management plane outside the Airwall story we present to customers. In OT-adjacent sales, "which vendors have root on the box in our building" is a due-diligence question; each added agent weakens the answer.
3. **Supply-chain exposure (risk).** RMM agents run privileged on every node; the category is a proven high-value attack target (Kaseya VSA ransomware event, 2021). Vendor security posture becomes part of our own security narrative.
4. **Where RMM clearly wins anyway.** If the service scope grows to managing *customer* serviceable hosts (VMS servers, badge servers — the same hosts identified for optional Nozomi Arc attach), a multi-tenant RMM is the right instrument and Azure Arc is not a natural fit on customer-owned Windows estates. That is an attach-tier decision, not a node decision.

## Recommendation (revised 07-28 after Darryl's challenge)

**RMM is the primary candidate for the node management layer.** Rationale (Darryl): the team operates RMM-class tooling today and does not run Azure Arc or GitOps; the Airwall provides manual access, but the product needs *monitoring-as-a-service built into every node sold*, which is exactly the RMM operating model, and per-device RMM cost prices cleanly into service COGS. Operating-model fit outranks the dossier's platform-native elegance; the GitOps stack presumed a platform-engineering capability that does not exist in the delivery organization.

- NinjaOne is the default candidate (category leader, Ubuntu agent with monitoring/patching/remote terminal, per-device pricing, existing operating familiarity). N-able is the challenger if customer-site network-device monitoring matters; Canopy gets one qualification call (fielded-appliance management is its native category).
- **Container lifecycle (resolved in principle, 07-28, Darryl):** image distribution rides the Docker Hub service Wesco is enabling now — new versions pushed to the registry, nodes kept current from it. Aligns with the CSRA-approved entroCIM Docker work. The node-side half is RMM territory: scripted, staged pulls triggered through RMM automation (not unattended auto-pull), with pre/post health checks and a rollback tag. Open specifics for pilot design: registry auth handling on nodes, outbound path for pulls (via Airwall or direct, must match the security narrative), staged rollout policy, and whether Arcbeam clustering carries update coordination for the entroCIM containers (Ron Snyder conversation, ~08-08).
- The security-architecture condition stands regardless of vendor: the RMM agent is a privileged channel to a Wesco cloud console; either route it via the Airwall path or document it explicitly as an additional channel in the customer-facing security narrative. Vendor supply-chain posture (Kaseya 2021 precedent) is a diligence item in selection.
- Azure Arc/GitOps is not excluded for a future scale stage, but it is no longer the baseline assumption.
- Revisit RMM scope again at the customer-host attach tier (VMS/badge servers) when that tier is scoped — same instrument, different estate.

Owner: Darryl (decision at Checkpoint 2, ~08-14), with pilot ops input; RMM vendor qualification can start pre-AOP as a thin-lane item. Filed to Research Log queue item 6.

## Sources
- [NinjaOne RMM review 2026 (ITT Systems)](https://www.ittsystems.com/ninjaone-rmm-review/)
- [NinjaOne review (AIMultiple)](https://aimultiple.com/ninjaone-review)
- [NinjaOne MSP guide (Rotech)](https://rotechgroup.eu/en/blog-ninjaone-rmm-msp-comprehensive-guide.html)
- [Best RMM tools for MSPs 2026 (NOCDOC)](https://nocdoc.com/2026/05/07/11-best-rmm-tools-for-msps-in-2026/)
- [RMM platform comparison (TechnologyMatch)](https://technologymatch.com/blog/ninjarmm-vs-connectwise-automate-vs-datto-rmm-vs-atera-rmm-platform-comparison)
- [NinjaOne alternatives (Syncro)](https://syncrosecure.com/blog/ninjaone-competitors/), [NinjaOne alternatives (SuperOps)](https://superops.com/best-ninjaone-alternatives)
- [Canopy on RMM vs connected-product management](https://www.gocanopy.com/glossary/ninjaone)
- Vendor-published comparison pages (NinjaOne blog) used for landscape orientation only; pricing figures third-party, unverified — confirm in vendor conversations. Kaseya 2021 incident: background knowledge, verify current posture in diligence.
