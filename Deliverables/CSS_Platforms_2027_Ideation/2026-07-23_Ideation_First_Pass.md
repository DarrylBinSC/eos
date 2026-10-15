# New Product Ideation — First Pass
Date: 2026-07-23 | Per: `2026-07-23_New_Product_Ideation_Charter.md` | Status: working draft for comparison with parallel ChatGPT pass

> **Caveats added 07-23 PM (Phase 0):** still an active Phase 1 input, but (1) scores below use the old 8-criterion unweighted scale — NOT comparable to the governing 10-criterion weighted scorecard in `Products/CDA/00_Charter/`; all concepts get re-scored at the Phase 1 merge. (2) "Verified rollback" language is superseded by the governing rollback standard: OEM-supported rollback where available and validated, otherwise defined recovery/isolation/replacement/field-remediation.

Evidence note: competitive and market claims below rest on general knowledge (as of mid-2025) and are marked **verify**. No fresh market research has been run yet; that is the next step for the surviving concept(s).

---

## Concept Cards

### 1. Device Firmware Assurance Service (seeded lead)
- **Problem / who feels it:** camera and edge-device firmware goes unpatched for years. Felt by security directors (cyber exposure, audit findings), facility/IT ops (no staff or tooling), procurement (insurance and compliance pressure). Pain validated by the existence of a paid market (**verify**: SecuriThings, Viakoo).
- **Who pays and why:** the security/facility budget owner; cheaper than staffing it, and transfers execution risk (approval, staging, rollback, assurance) to Wesco.
- **Offer:** Wesco keeps your security devices current. Approval workflow, staged rollout, verified rollback, compliance reporting. Customer does nothing but approve.
- **Architecture:** Azure VM + entroCIM with new firmware pod ↔ field Airwall (appliance or SFF PC). Start with 2–3 camera lines.
- **Competitors / why Wesco wins:** SecuriThings, Viakoo (tools + some service, **verify** current offers); free single-vendor manufacturer tools (Axis Device Manager etc.). Wesco wins on multi-vendor coverage, supplier relationships (firmware access, early notice), WAM install-base knowledge, low-footprint connectivity, and full service delivery vs. self-operated tools.
- **Revenue model:** per-device per-month subscription + onboarding fee; tiers by device criticality.
- **Service owner hypothesis:** product support in Darryl's team (entroCIM team runs the pod); service delivery interface with Managed Services defined at concept stage, mirroring the entroCIM support-model split.
- **Dependency gates:** manufacturer firmware access/redistribution rights (owner: supplier relations, named per vendor); Wesco security governance approval for pushing code to customer networks (owner: CSRA path already used for Docker); Airwall commercial/licensing terms (owner: Darryl — MSP agreement already under review).
- **Top risks:** liability for a bad update (mitigate: approval + staged + rollback + contract language); manufacturers making free tools good enough; per-device economics too small unless fleet counts are large.
- **First pilot profile:** existing entroCIM or CSS security customer with 200+ cameras of a supported line and compliance pressure.

### 2. Device Cyber-Hygiene & Compliance Service
- **Problem:** broader than firmware — default/stale passwords, expiring certificates, vulnerable/EOL devices, no compliance evidence for auditors or insurers.
- **Offer:** continuous hygiene posture (password rotation, cert management, vuln/EOL reporting) with a compliance dashboard; firmware service is a natural module inside it.
- **Architecture:** same Airwall + Azure pod backbone; adds credential/cert handling (higher security bar).
- **Competitors / why Wesco wins:** same players, head-on (**verify**); differentiation weaker at this scope because it is their core product. Wesco wins only if bundled with service delivery + device supply.
- **Revenue model:** per-device per-month, higher tier than firmware alone.
- **Dependency gates:** everything in Concept 1 plus credential custody policy, legal exposure review.
- **Risks:** scope breadth kills MVP speed; credential custody raises the security and trust bar substantially.
- **Assessment:** the destination, not the entry point. Converges with Concept 1.

### 3. Install-Base Refresh & EOL Intelligence Service
- **Problem:** customers can't see which devices are approaching end-of-support/EOL or unsupported firmware, so refresh is reactive and Wesco's refresh revenue is left to chance.
- **Offer:** governed device inventory (discovered via the same connectivity, enriched by ADM with supplier lifecycle data) driving refresh plans, budgets, and quotes.
- **Architecture:** Airwall + discovery pod feeding WAM/ADM; Strev as the customer experience; Sales notifications reuse the shipped WAM notification capability.
- **Why Wesco wins:** this is the strongest pull-thru engine of the set, and nobody else has Wesco's supplier + install-base position.
- **Risks / assessment:** largely an extension of WAM's existing commercial path rather than a new product — weaker "new concept" funding story — and it lands on WAM's known gates (supplier lifecycle data, MDM attributes), which are the portfolio's hardest open dependencies. Better positioned as the growth stage of Concept 1: the discovery data the firmware service collects **is** install-base intelligence, flowing into WAM.

### 4. Remote Device Health Monitoring (NOC-lite)
- **Problem:** camera/device downtime discovered only when footage is needed; no one watches device health.
- **Offer:** lightweight monitoring (up/down, health, storage, tamper) with alerting and dispatch coordination.
- **Architecture:** same backbone; entroCIM's monitoring strengths apply directly.
- **Risks / assessment:** staffing/ownership question is unresolved at portfolio level (Managed Services operating model, CSS/TSS split) — this concept inherits that ambiguity at MVP stage rather than after proving value. Strong later module; weak lead.

### 5. Secure Remote Access as a Service (productized Airwall)
- **Problem:** integrators/vendors need secure access to customer OT/security networks; VPNs are overexposed.
- **Offer:** managed segmented access via Airwall as a standalone subscription.
- **Assessment:** crowded ZTNA/secure-access market where Wesco has no brand permission to win standalone (**verify**); commercial terms with the Airwall vendor still in review. Its real value is as the delivery backbone of Concepts 1–4, and as an on-ramp asset already proven in the Ascent POC. Not a lead candidate.

---

## Scoring Matrix (1–5; dependency risk inverted, higher = lower risk)

| Criterion | 1 Firmware | 2 Hygiene | 3 Refresh/EOL | 4 Monitoring | 5 Access |
|---|---|---|---|---|---|
| Problem evidence | 4 | 5 | 4 | 4 | 3 |
| Asset reuse | 5 | 4 | 5 | 5 | 4 |
| Recurring rev & 2027 timing | 4 | 3 | 3 | 4 | 4 |
| Hardware pull-thru | 3 | 3 | 5 | 3 | 2 |
| Competitive position | 3 | 2 | 4 | 3 | 2 |
| Delivery feasibility | 4 | 3 | 4 | 3 | 4 |
| Dependency risk (inv.) | 4 | 3 | 2 | 3 | 3 |
| Benefits measurability | 5 | 4 | 4 | 4 | 3 |
| **Total** | **32** | **27** | **31** | **29** | **25** |

---

## Recommendation — staged, one service line

**Lead with Concept 1 as the MVP wedge of a service line called something like "Device Lifecycle Assurance," staged to become Concepts 3 and 2.** The firmware idea survives the comparison on its own merits: fastest to first revenue, narrowest MVP, best measurability, lowest dependency load. But the fundable story is the staircase, not the step:

1. **Stage 1 (MVP, first revenue 2027):** firmware assurance for 2–3 camera lines. Proves the Airwall + Azure pod delivery model and the commercial motion.
2. **Stage 2:** the discovery data the service already collects becomes install-base/EOL intelligence flowing into WAM/ADM → refresh planning → **hardware pull-thru** (this is what makes the proposal answer the pull-thru miss, not just the software miss).
3. **Stage 3:** expand to hygiene/compliance modules and health monitoring as Managed Services ownership matures.

**Team spread falls out naturally:** entroCIM team owns the connectivity pod and device interaction; WAM team owns inventory, lifecycle data, and notifications; Managed Services owns delivery per an interface defined at funding time. Navigator integrates as a surface later, without presuming reporting outcomes.

**One-sentence executive takeaway:** a light-footprint subscription service that keeps customers' security devices current, built almost entirely from assets we already own, that generates recurring software revenue in 2027 and converts its own operating data into Wesco hardware refresh sales.

---

## Open Questions
1. Manufacturer firmware redistribution rights: can Wesco legally acquire and push vendor firmware as a service? Per-vendor answer needed early — this is the make-or-break gate.
2. Airwall commercial terms for embedding in a Wesco service (MSP agreement in review).
3. Liability/assurance model for a failed update: what does Legal need, what do customers accept?
4. Which camera/device lines first (candidates: highest CSS sales volume + best vendor firmware APIs)?
5. Pilot candidate: which existing customer (Fed? BAE? an Ascent-served site?) — pick where relationship strength tolerates MVP roughness.
6. Pricing reality check: what do SecuriThings/Viakoo charge per device (**verify**)?

## Prioritized Research List (next session)
1. Current competitive scan: SecuriThings, Viakoo, manufacturer tools, any new entrants since 2025.
2. Market sizing signals: physical-security device fleet sizes, regulatory/insurance drivers (NDAA §889, cyber-insurance device-patching requirements — **verify** current state).
3. Vendor firmware API/access survey for top CSS camera lines.
4. Comparable per-device pricing.
