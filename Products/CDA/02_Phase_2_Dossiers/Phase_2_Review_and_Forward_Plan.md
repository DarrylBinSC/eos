# Phase 2 Review and Forward Plan
Date: 2026-07-23 | Companions: `CSS_Platforms_2027_Phase_2_Updated_Deep_Dive.md` (ChatGPT dossier), `Phase_2_Review_Timeline_and_Architecture.md` (Claude corrections), `CDA_Architecture_Executive.md/.mermaid` (diagrams)

## 1. What Phase 2 Concluded

**Recommended MVP: Connected Camera Assurance** (pilot scope name under the Connected Device Assurance umbrella brand):

| Element | Conclusion |
|---|---|
| Module composition | Cyber-hygiene **visibility** included for every eligible device (base tier) · Health & Recovery as **primary operational module** · Firmware as **controlled action**, Axis active first, Hanwha qualifying in parallel |
| Deployment sequence | **Land Mode 3** (zero-touch: Azure container over Airwall, nothing on site but the Airwall) → **expand Mode 1** (Wesco Ubuntu appliance) → Mode 2 (customer server) as enterprise alternative |
| Manufacturer sequence | Axis → Hanwha → Cisco (API-led via Meraki/Catalyst Center, orchestrate not rebuild) → HID (partner-led) → dormakaba (qualify per family) → open-API devices |
| Build | Container product, Arcbeam estate control, the **shared enablement layer** (registry, identity binding, policy, approval workflow, job state machine, validation, evidence ledger, service queue, partner abstraction, WAM loop, Navigator escalation, metering, guardrailed AI), Axis/Hanwha pods |
| Partner | Breadth remediation (Viakoo strongest immediate candidate; SecuriThings compare), credentials/certificates, OT visibility (Nozomi), advisory content |
| Do not build | Second WAM, second work-order platform, generic fleet manager, Nozomi replacement, OEM-tool feature parity |
| Fleet management | K3s + Azure Arc + Flux GitOps; Portainer-class as pilot accelerator |
| Pilot | 1 strategic customer, 2–5 sites, 250–1,000 cameras, 16 weeks, defined success criteria and stop conditions |
| Pricing | Tiered per-device subscriptions with zero-touch entry tier; ALL dollar ranges are assumptions — no public managed-service per-device benchmark exists |

Evidence discipline held throughout: fact/evidence/assumption/hypothesis labels, 32 official sources, honest UNVERIFIED flags.

## 2. Claude's Compilation — corrections applied

1. **Timeline reframed (the material correction).** The dossier compressed OEM qualification, partner RFIs, credential architecture, and liability review into Aug 7–28 — colliding with the pilot review (08-12), Sean window (08-17), AOP deadline (08-31), Quest migration (09-01). Fix is structural, not cosmetic: those gate actions ARE the funded 90-day validation (Oct–Dec 2026), pilot Q1–Q2 2027. Presenting them as unfunded August homework would weaken the ask. Pre-AOP lane is deliberately thin: incident-data pull, Arcbeam conversation (Ron Snyder), pilot shortlist, RFI drafts.
2. **Architecture diagrams rebuilt** per Mermaid standards: 30-node wall → executive overview (8 nodes) + controlled-action sequence (the liability-control story).
3. **Success thresholds** (≥25% remote resolution, ≥15% truck-roll reduction) reclassified as pilot hypotheses to calibrate, not commitments.
4. **Naming discipline:** Connected Device Assurance = umbrella brand; Connected Camera Assurance = pilot scope only.
5. **Outreach conflict resolved:** dossier's early-August formal Supplier Relations/Legal dates contradicted the 07-23 deferral decision; corrected by the two-lane timeline.

## 3. What Phase 2 Gives the Funding Case

The ask is now concrete: fund the **shared enablement layer** (named capabilities, built once), camera-scoped pilot content (Axis/Hanwha pods, hygiene visibility, health playbooks), container packaging for three delivery modes, and a 90-day validation with named gates. The spine of the story: *extend containerization investment already underway → one deploy-anywhere container product → camera-scoped pilot with measurable service outcomes → operating data feeds WAM → hardware refresh pull-through.*

**Weakest links, stated honestly (these are what pre-AOP work must shore up):**

| Weakness | Fix | Owner | When |
|---|---|---|---|
| Willingness-to-pay is hypothesis; no public per-device benchmark | Pilot-candidate conversations; partner RFI pricing data | Darryl + Sales; Claude drafts RFI | Pre-AOP shortlist; RFIs post-funding |
| Module B economics rest on unverified remote-resolution rate | **Internal incident/truck-roll data pull — single most important evidence item** | Darryl sponsors (service/support teams) | ~08-15 |
| Gate A: service-owner function unnamed | Name the Managed Services owner function in the Sean conversation | Darryl | Week of 08-17 |
| Commercial sponsor unnamed | Same conversation; Sales/BU sponsor for pilot account | Darryl | Week of 08-17 |
| Arcbeam clustering readiness unconfirmed | Conversation with Ron Snyder | Darryl | ~08-08 |
| Citations unverified by second source | Claude research track (verification + partner terms + pricing scan) | Claude | ~08-05, before Sean brief |

## 4. Decisions and Open Items (as of 07-23 PM)

1. **Checkpoint 2 (Darryl): confirm Connected Camera Assurance MVP composition** — the dossier recommends it, Claude concurs, nothing in the pre-AOP lane blocks it. On confirmation, Phase 3 packaging begins against the week-of-08-17 Sean window.
2. Research track go (Claude) — now on the critical path for citation verification before any Sean-facing document cites the OEM/partner claims.
3. Pre-AOP lane owners confirmed (incident data, Ron conversation, pilot shortlist).
4. Sean 1:1 booking, week of 08-17.

## 5. Phase 3 Preview (starts on Checkpoint 2 confirmation)

Product thesis · 90-day validation plan (the reframed gate actions, with owners) · three AOP funding scenarios · pitch ladder (one-sentence → 30-second → two-minute → funding slide → decision memo) · Sean brief via Pandoc · ChatGPT red-team pass · final package by ~08-28 for 08-31 AOP input.
