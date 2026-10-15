> **SUPERSEDED 2026-07-23 PM** by the governing documents in `Products/CDA/00_Charter/` (content absorbed). Retained for record; do not cite as current.

# ChatGPT Prompt Addendum + Joint Execution Plan
Date: 2026-07-23 | Companion to: `2026-07-23_New_Product_Ideation_Charter.md`, `2026-07-23_Ideation_First_Pass.md`, and `Products/CDA/ChatGPT_CSS_Platforms_2027_Product_Ideation_Prompt.md`

---

## Part 1 — Addendum Block (paste into ChatGPT with the main prompt, before running)

Copy everything between the markers.

```
# Addendum — Additional Context and Execution Rules

Apply these on top of the main prompt. Where they conflict with it, the addendum wins.

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
```

---

## Part 2 — Joint Execution Plan (Claude + ChatGPT, step by step)

Division of labor: **ChatGPT** = breadth and divergence (big concept portfolio, structured analysis) and later red-team critique. **Claude (this workspace)** = inside context, evidence discipline, merging and arbitration, cited market research, deliverable production in Darryl's voice, and filing to the operating record. Darryl = decision-maker at each checkpoint.

### Phase 1 — Diverge (target: this week)
1. Darryl pastes the addendum + main prompt into ChatGPT; runs Phase 1 (map, pain inventory, concepts, scoring, shortlist).
2. Darryl saves the output into `Products/` or pastes it here.
3. Claude merges it against `2026-07-23_Ideation_First_Pass.md`: reconciles overlapping concepts, arbitrates scoring differences with reasons, flags anything ChatGPT surfaced that the first pass missed (and vice versa).
4. Output: **Consolidated Shortlist memo** (2–3 concepts, one page).
- **Checkpoint 1 (Darryl decides):** confirm the shortlist. Exit criterion: 2–3 named surviving concepts.

### Phase 2 — Deepen and verify (target: next week)
5. Darryl runs ChatGPT Phase 2 (deep dives on survivors only).
6. In parallel, Claude runs fresh web research: competitive scan (SecuriThings, Viakoo, OEM tools, new entrants), regulatory and insurance drivers, comparable per-device pricing, vendor firmware API accessibility for top CSS camera lines. All claims cited; "verify" flags from the first pass resolved.
7. Claude merges deep dives + research into a single **Concept Dossier** per survivor, including a Mermaid architecture diagram per Darryl's diagram standards.
- **Checkpoint 2 (Darryl decides):** concept freeze — pick the lead thesis. Exit criterion: one named concept with verified competitive position and no unexamined make-or-break gate (firmware redistribution rights answered at least directionally).

### Phase 3 — Package for funding (target: early August, ahead of a Sean 1:1)
8. Claude drafts the funding package: 90-day validation plan with owners and decision gates; three funding scenarios (discovery/pilot, focused launch, accelerated); pitch ladder (one-sentence value proposition, 30-second, two-minute, funding slide, decision memo). Written for the Sean conversation first, AOP variant labeled.
9. Darryl pastes the draft package into ChatGPT for red-team critique ("attack this case as a skeptical CFO/GM"); Claude incorporates whatever survives scrutiny.
10. Output: **Sean brief** (and supporting one-pager), converted to .docx via the Pandoc pipeline.
- **Checkpoint 3 (Darryl decides):** take to Sean. Exit criterion: Sean endorsement or redirect.

### Phase 4 — AOP submission (timing: per AOP calendar, [date TBD — Darryl to confirm])
11. After Sean's input: adjust, produce the Dirk/BU version, then the formal AOP submission per whatever template the process requires.
12. Claude files outcomes throughout: decision log (03), commitments (05), and a new `Products/` context file for the concept once it has a name and an endorsement.

### Progress tracking
- The decision log entry (03, "New product concept for AOP 2027") is the master record; each checkpoint outcome gets logged there.
- Each phase has one exit criterion; if a phase stalls more than a week, that is a signal to cut scope, not extend timeline — the AOP window is the fixed constraint.
- Open make-or-break item to start immediately, independent of phases: **manufacturer firmware redistribution rights** — a per-vendor legal/commercial question that can kill the lead concept. Worth an early informal question to supplier relations and legal rather than waiting for Phase 2.
