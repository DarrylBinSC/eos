# entroCIM Team Quality Standard — record and assessment

As of: 2026-09-17. Source document: `entroCIM_Team_Quality_Standard_v2.0_2026-09-17.pdf` (this folder).
Author: Ron Snyder. Version 2.0, dated September 2026, 11 pages, ~3,390 words. Stated owner: "entroCIM Leadership Team."
Provenance: Darryl asked Ron to create it; Ron delivered the draft 2026-09-17. Darryl has not yet returned feedback (`05` A50).

## Status

Draft under Darryl's review. Not issued, not rolled out, no adoption mechanism named. Do not cite it as an operating control anywhere until that changes.

## Scope, as written

Applies across the entire entroCIM delivery organization, named explicitly as Development, Application Specialists, Deployment/Integration/Graphics, IT Architecture, and Product/Support/Leadership. It is a cross-functional standard for complete customer outcomes, not a development standard.

## Structure

| Section | Content |
|---|---|
| 1. Our Commitment | Why quality matters; explicit "quality does not mean perfection" framing; no-blame on honest mistakes, no normalization of preventable rework |
| 2. What Quality Means for entroCIM | Six principles: customer outcomes first; one solution as one team; clear ownership; details are part of the deliverable; documentation is part of the work; professional pride |
| 3. End-to-End Quality Across the Customer Lifecycle | Six-stage table (Understand, Design, Build and configure, Integrate and validate, Deploy and transition, Operate and improve) with quality focus and cross-team contribution per stage. Handoffs defined as **shared control points**, not transfers of responsibility. "No silent handoffs" rule |
| 4. Readiness Before Work Is Committed | Eight readiness tests before commitment; a Discovery / Commitment / Delivery table distinguishing acceptable uncertainty from required discipline at each stage |
| 5. Definition of a Complete Customer Outcome | Six dimensions: customer outcome, solution integrity, validation, evidence and transparency, documentation and knowledge transfer, review/approval/transition. Completion rule: completion belongs to the customer outcome, not a departmental activity |
| 6. Documentation and Knowledge Standard | Six documentation areas with expected knowledge per area; six rules for documentation decisions |
| 7. Quality Expectations by Role | Five role groups, each with expectations and a "Success looks like" statement |
| 8. Quality, Capacity, and Tradeoffs | Tradeoffs must be visible; five named legitimate responses when scope, schedule, capacity and quality conflict; escalation expectation states that raising a risk early **is** ownership |
| 9. Required Team Behaviors | Twelve numbered behaviors, framed as how the standard becomes real in daily work |
| 10. Learning, Coaching, and Accountability | What to do when a quality issue occurs; nine coaching questions |
| 11. Quick Reference Checklist | Four checklists: before commitment, before a cross-team handoff, before deployment or customer transition, before closure |
| Closing | Shared commitment statement; document ownership and review table |

## Assessment (Darryl's, 2026-09-17, plus analysis)

**Darryl's read:** very good, tight, and clear. The sentiment is right. The gap is the connection to the actual team.

**Where it is strong, and this is more than a first pass suggests.** Three things in the document are doing real structural work rather than stating values:

- **Handoffs as shared control points** (§3). This is the direct answer to the recurring pattern in the EOS record where work crosses a team boundary and responsibility does not: the "no silent handoffs" rule makes the receiving role's ability to understand and use the work part of the sending role's completion test.
- **The Discovery / Commitment / Delivery table** (§4). It tells the team what uncertainty is acceptable at each stage rather than implying all uncertainty is a failure, which is the usual reason engineers ignore a quality document.
- **§8, capacity and tradeoffs.** It places an obligation on leadership, not only on the team: make tradeoffs visible, provide capacity, remove obstacles, address systemic causes. A quality standard that binds only the doers does not survive contact with a schedule.

**The gap: adoption, not content.** The document defines what good looks like. It does not define how this team, distributed across North America and India, comes to practice it. Specifically:

- No mechanism binds the §11 checklists to where work actually happens — Jira definition of done, pull-request review, release gate, deployment checklist, sprint retro. The document says expectations "should be reinforced through discovery, solution design, estimates, project plans, Jira, reviews, handoffs, validation, deployment, support, retrospectives, and leadership decisions" (§9), which names the surfaces but assigns nothing to anyone.
- No owner for rollout. "entroCIM Leadership Team" owns the document; no individual owns adoption.
- No first application named. Nothing says which release, which customer deployment, or which handoff is the first one run against it.
- **No treatment of the distributed team's actual conditions.** Ron's eleven reports are seven in India and four in North America, a flat span with no managers underneath (`06`). The handoff rules in §3 and the escalation expectation in §8 are the ones most affected by limited hours overlap, and the document is silent on how a handoff is confirmed, or a risk raised early, when the two roles share few working hours. This is the same working constraint already tracked for Akansh Gangil (`06`, 07-15).
- Role expectations in §7 are written by function, not by team. A member of Ron's team reading §7 sees "entroCIM Development" and a list of good practices, not what changes in their week.

**Two minor defects, worth one line to Ron and no more.** The numbered list in §10 continues the numbering from §9 (it runs 13 to 19 rather than 1 to 7). And the document is labeled Version 2.0 with no version history or statement of what changed from 1.0.

## Why this matters beyond Ron's team

It intersects the development-resource argument in `03` (2026-09-10). That thread records Darryl's own position that development has been slow, that quality has been questioned by his own team, and that Sean McCloskey already believes results have not been good. A cross-functional quality standard authored by the development director is relevant evidence in that conversation, but only in its adopted form. As a document it demonstrates intent; as an operating practice with measurable handoff and defect outcomes it would be evidence of control. Do not present it upward as the latter until it is one.

Related: `Reference/Engineering_Delivery_Governance.md`; `05` B9 (entroCIM release controls applied consistently, Ron Snyder).
