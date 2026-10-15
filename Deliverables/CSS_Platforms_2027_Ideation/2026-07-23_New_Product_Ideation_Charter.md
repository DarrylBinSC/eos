> **SUPERSEDED 2026-07-23 PM** by the governing documents in `Products/CDA/00_Charter/`. Retained for record; do not cite as current.

# CSS Platforms — New Product Ideation Charter
Date: 2026-07-23 | Owner: Darryl Benson | Purpose: structure the ideation and selection of a new product/service proposal for funding and contribution to the 2027 Annual Operating Plan. Portable: usable as a standalone prompt in any AI tool.

# Context

## Role
Senior Director, CSS Digital Products and Platforms at Wesco (CSS = Communications & Security Solutions). Portfolio leadership role: product, engineering, deployment, support, managed services, AI strategy, platform architecture.

## Asset Inventory (what any new concept should reuse)
- **entroCIM** — mature OT/building-intelligence platform (10+ yrs, strong installed base): device integration, telemetry, alarms, analytics, remote monitoring. Quarterly release cadence, Azure deployment, Docker containerization under approved security governance.
- **WAM (Strev + ADM)** — asset lifecycle platform: hardware/software/license/warranty/entitlement visibility, install-base intelligence, renewal and expiration notifications to Sales. ADM = data normalization/enrichment backend; Strev = customer-facing experience layer.
- **Ascent Navigator** — facility-management platform (Maximo replacement: assets, work orders, budgeting, forecasting). Treat as an **integration partner, not an owned asset** — reporting alignment is unresolved; do not presume org outcomes.
- **Connected Safety / Spanr** — safety workflows and data; Connected Safety ownership currently in transition (open decision).
- **Airwall** — secure Layer-3 presence on the customer's network with minimal on-prem footprint (appliance or small-form-factor PC running an Airwall server/agent). Proven in a live partner POC deployment right now.
- **Azure cloud VMs** — cloud-side compute that can connect to and interact with customer devices through the Airwall, without a full platform deployment on site.
- **Wesco commercial position** — distribution relationships with device manufacturers, supplier network, existing CSS customer base, Managed Services delivery capability.

## Commercial Backdrop (why this matters now)
CSS software sales and hardware pull-thru are materially behind target at mid-year. The strategic answer leadership is looking for is recurring service revenue that monetizes the existing installed base and drives Wesco hardware sales. A new concept is fundable to the degree it answers that question, not to the degree it is technically interesting.

# Design Principles (hard constraints)

1. **Adjacent** to the CSS business and CSS Platforms portfolio today.
2. Addresses an **industry problem involving devices Wesco sells plus software** — not a pure-software play.
3. **Sold as a service** — recurring revenue, not perpetual license.
4. **Light footprint**: Airwall on-prem + Azure VM cloud-side. Not a full platform deployment; a value-added service a customer can adopt with minimal site impact.
5. **Team spread by design**: the concept should let the entroCIM and WAM teams extend across multiple solutions and create shared platform components.
6. **Commercial-first discipline** (hard-won lesson: capability built ahead of the commercial model creates an "investment vs. value today" problem later). No concept advances without: named service-owner hypothesis, pricing/packaging hypothesis, measurable benefits with baselines, explicit dependency gates with owners.
7. **Service-ownership interface defined upfront**: who owns product support vs. managed-services delivery vs. commercial execution — stated per concept, not deferred.

# Evaluation Criteria (score each 1–5)

| # | Criterion | What 5 looks like |
|---|---|---|
| 1 | Problem evidence | Validated customer pain with demonstrated willingness to pay |
| 2 | Asset reuse / adjacency | Built substantially from entroCIM, WAM, Airwall, Azure, existing teams |
| 3 | Recurring revenue & 2027 timing | Clear per-device/per-site subscription; first revenue achievable in 2027 |
| 4 | Hardware pull-thru | Directly generates Wesco device/refresh sales |
| 5 | Competitive position | A specific, defensible answer to "why does Wesco win?" |
| 6 | Delivery feasibility | Current teams can build and run the MVP without new hires |
| 7 | Dependency risk (inverted) | Few external gates; the ones that exist have named owners |
| 8 | Benefits measurability | Metrics with baselines exist from day one |

# Task

1. Generate 4–6 candidate concepts meeting the design principles. The seeded lead candidate below must be tested against alternatives honestly, not pre-selected.
2. Produce a **concept card** for each (contract below).
3. Score all concepts against the criteria; show the matrix.
4. Recommend one concept (or a staged combination) and develop it into a value-proposition skeleton suitable for a funding conversation: first with reporting-line leadership, then BU leadership, then AOP 2027 submission.

# Seeded Lead Candidate — Device Firmware Management Service

Managed firmware lifecycle for physical-security and building devices (starting narrow: a few camera lines and device types). Customer pain: firmware on cameras and edge devices goes unpatched for years — cyber exposure, compliance findings, insurance pressure, warranty and support risk — because updating is manual, risky, and nobody owns it.

Offer: Wesco keeps your devices current. Easy interface, customer approval workflow, staged rollout, verified rollback, and assurances. Architecture: Azure VM running entroCIM with a new firmware-update pod, connected through a field Airwall on-prem (appliance or small-form-factor PC with Airwall agent). Light footprint; not a full entroCIM deployment.

Known competitive context to verify with current research: SecuriThings and Viakoo sell device firmware/password/certificate management for physical security; manufacturers offer free single-vendor tools (e.g., Axis Device Manager). The Wesco differentiation hypothesis: multi-vendor coverage, distribution and supplier relationships, install-base knowledge via WAM, low-footprint connectivity via Airwall, and a managed service (customer does nothing) rather than a tool the customer must staff.

# Output Contract

For each concept, a card with: name; problem and who feels it; who pays and why; the offer in two sentences; architecture sketch (reused assets named); competitors and why Wesco wins; revenue model hypothesis; service-owner hypothesis; dependency gates with owners; top three risks; first-pilot candidate profile.

Then: scoring matrix, recommendation with staging logic, open questions, and a prioritized research list (items marked "verify" where claims rest on general knowledge rather than current evidence).
