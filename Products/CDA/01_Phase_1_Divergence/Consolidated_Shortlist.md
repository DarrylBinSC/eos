# Consolidated Shortlist — Checkpoint 1 Decision Memo
Date: 2026-07-23 | Inputs: `CSS_Platforms_2027_Phase_1_Service_Led_Thesis.md` (ChatGPT), `Deliverables/2026-07-23_Ideation_First_Pass.md` (Claude), governing documents in `00_Charter/` incl. 07-23 amendments (manufacturers, firmware-rights reclassification, partnership lens, AOP 08-31)

## Opportunity Statement

A recurring managed service, built substantially on existing CSS Platforms technology and selected partnerships, under which Wesco assumes accountability for the operational, software, and lifecycle condition of connected devices it sells — generating recurring revenue in 2027, converting its own operating data into hardware refresh sales, and answering the mid-year commercial question directly.

## Process Note (input-sensitivity, stated honestly)

The ChatGPT run did not execute the Phase 1 contract (no adjacency map, pain inventory, 10–12 concept portfolio, or scoring matrix); it converged on Darryl's guidance and produced a reframed thesis plus a 3-item shortlist whose #1 is the umbrella category of #2 and #3. Divergence coverage therefore rests on the Claude first pass (5 concepts) plus the master prompt's 8 mandated concept categories — adequate, not exhaustive. **What matters more: the signal that stayed stable across three independently framed analyses** — device-lifecycle service on existing rails, firmware as candidate wedge, light-footprint delivery, WAM feedback loop, service-before-technology ordering. That convergence is the trustworthy core. Packaging and shortlist composition swung between runs; that is what Checkpoint 1 exists to pin down. Going forward, thesis changes happen only by dated amendment to the governing docs — regeneration is how input sensitivity does damage.

## Consolidated Concept Universe (both analyses reconciled)

| Concept | ChatGPT | Claude 1st pass | Disposition |
|---|---|---|---|
| Connected Device Assurance (umbrella) | Shortlist #1 | "Device Lifecycle Assurance" staircase | **Adopt as category** — not scored; it is the packaging |
| Firmware & Configuration Assurance | Shortlist #2 | Concept 1 (lead) + config elements of Concept 2 | **Score as Module A** |
| Remote Device Health & Recovery | Shortlist #3 | Concept 4 (NOC-lite) | **Score as Module B** |
| Lifecycle Refresh / EOL Intelligence | Absent as offer; present as "commercial signal" (§4.7) | Concept 3 | **Score as Module C** — test standalone vs. embedded |
| Cyber-Hygiene (credentials/certs/vuln) | Folded into umbrella scope | Concept 2 | **Score as Module D** — expansion candidate |
| Warranty/Entitlement Assurance | Mentioned in master prompt | — | Not a new product; existing WAM scope — route to WAM roadmap |
| Secure Access as a Service (Airwall standalone) | Correctly positioned as enabler | Concept 5 (rejected) | Remains backbone, not product — both analyses agree |

## Scoring (governing 10-criterion weighted scorecard; weighted score out of 5.0)

| Criterion (weight) | A: Firmware+Config | B: Health+Recovery | C: Refresh/EOL | D: Hygiene |
|---|---|---|---|---|
| Problem severity/evidence (15%) | 4 | 4 | 4 | 5 |
| Buyer willingness to pay / ACV (15%) | 4 | 3 | 2 | 4 |
| Wesco right to win (15%) | 3 | 3 | 5 | 2 |
| Recurring revenue & margin (10%) | 4 | 3 | 2 | 4 |
| Pull-through (10%) | 3 | 4 | 5 | 3 |
| Asset reuse (10%) | 5 | 5 | 4 | 4 |
| MVP feasibility, 2027 value (10%) | 4 | 4 | 3 | 2 |
| Scalability (5%) | 4 | 4 | 4 | 4 |
| Service/ownership feasibility (5%) | 3 | 3 | 4 | 3 |
| Cyber/liability/dependency (5%) | 3 | 4 | 4 | 2 |
| **Weighted** | **3.75** | **3.65** | **3.65** | **3.40** |

Per-module evidence notes (governing-doc requirement, condensed):
- **A (3.75):** Evidence — paid competitor market exists (SecuriThings, Viakoo — verify Phase 2); compliance/insurance drivers. Assumption — Wesco differentiation via multi-vendor + service delivery. Main uncertainty — right to win vs. incumbents; partner-vs-compete option changes this materially. Confidence: Medium. **Advance.**
- **B (3.65):** Evidence — truck-roll economics, entroCIM monitoring strength directly applicable; lowest liability profile (read-mostly + recovery actions). Assumption — enough remotely resolvable incident volume for margin (ChatGPT's Phase 2 question — correct). Main uncertainty — willingness to pay vs. expectation monitoring is bundled; staffing model. Confidence: Medium. **Advance.**
- **C (3.65):** Evidence — strongest right-to-win (install-base + supplier position) and pull-through of the set. Weakness as a *sold* service — customers underpay for what reads as sales enablement; and it lands on WAM's hardest known gates (supplier lifecycle data, MDM). **ChatGPT's structural instinct was right: embed as the commercial-signal capability (§4.7) inside every module rather than sell separately** — but elevate it in the funding story, because it is the pull-through answer. **Embed, don't sell standalone.**
- **D (3.40):** Evidence — most severe problem, head-on incumbent competition, highest trust bar (credential custody). **Hold** as designed expansion; architecture must not preclude it.

## Recommendation

**Adopt the service-led structure — one customer proposition, funded once at the enablement layer:**

1. **Connected Device Assurance as a Service** — the umbrella customer proposition and contract vehicle.
2. **Advance Modules A and B together into Phase 2.** They share roughly 80% of the enablement layer (connectivity, device identity, work queue, approval, execution, validation, evidence, WAM writeback, Navigator escalation) — which is precisely the funding logic: pay for the layer once, ship two revenue-bearing modules on it. Phase 2 determines whether the MVP launches with one module or both, using ChatGPT's two Phase 2 questions (A: can 1–2 camera manufacturers support a legal, safe, margin-positive firmware service? B: is remotely resolvable incident volume sufficient for margin?).
3. **Module C ships embedded from day one** (WAM writeback + refresh signal) and carries the pull-through slide in the funding case. **Module D is the named expansion path**, not MVP scope.

## Partnership Lens (per 07-23 thesis amendment — new Phase 2 requirement)

For each capability gap, Phase 2 assesses build vs. partner vs. buy before assuming internal build:

| Gap | Build case | Partner case | Precedent |
|---|---|---|---|
| Multi-vendor device-management engine (firmware/config logic per OEM) | entroCIM PODs + connectors, full control | **License/white-label an existing engine — including evaluating SecuriThings/Viakoo as partner instead of competitor** | Strev/Revnue white-label |
| OEM firmware feeds, advisories, certification | Per-OEM integration effort | Hanwha/Axis/Dormakaba/HID/Cisco technology-partner programs | Distribution relationships |
| Secure connectivity | — | Airwall (already partnered; MSP terms in review = D2) | Airwall/JCI-Ascent POC |
| Field remediation | Wesco field service | Ascent as delivery partner | Live JCI/Ascent relationship |
| Advisory/vulnerability intelligence | Curate internally | Commercial feed partnership | — |

Decision rule: build only what differentiates — the orchestration, WAM integration, evidence/commercial-signal loop, and service delivery. Partner for commodity capability. The partner-vs-compete evaluation of SecuriThings/Viakoo is now a first-order Phase 2 research question, not just a competitive scan.

## What Phase 2 Must Prove (exit: one lead thesis, Checkpoint 2 ~08-14)

1. Module A viability: firmware rights + safe update path for 1–2 camera lines (Hanwha, Axis) — per-vendor hurdle per 07-23 reclassification.
2. Module B margin: remotely resolvable incident volume (needs internal service-history evidence — Sales/field interviews).
3. Build/partner/buy answer per gap above, with the SecuriThings/Viakoo partner option explicitly priced.
4. Service ownership interface named (Gate A) — cannot carry the entroCIM ambiguity into the funding ask.
5. Pricing hypothesis tested against comparable per-device market pricing (Gate B).
6. Benefits/baselines per Gate C; dependency gates per Gate D (log: `05_Operating_Record/Risk_and_Dependency_Log.md`).

Optional backfill: ChatGPT produces the 15-pain-point inventory during Phase 2 as raw material for the funding case's problem slide — useful, not blocking.

## Checkpoint 1 Decision

**DECIDED 2026-07-23 (Darryl): confirmed as recommended.** (a) Umbrella adopted, (b) Modules A+B advance to Phase 2, (c) C embedded / D held, (d) partnership lens is a Phase 2 requirement. **Amended same day (Darryl): Module D (Cyber-Hygiene) promoted into Phase 2 scope** — cyber is table stakes, major OT/IoT gap, multi-vendor deployment risk; Nozomi Arc as reference point. Phase 2 deep-dives A+B+D; visibility-vs-remediation split defined in the Master Prompt Phase 2 amendment. Recorded in `03_Decision_Log.md` (master). Phase 1 closed.
