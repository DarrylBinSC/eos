# Sean Meeting Brief — Thursday, July 16, 2026

*Prepared 07-15. For Darryl's use. Decisions to leave with: (1) WAM narrative and presenter split for Dirk/Akash, (2) org structure endorsement or revision path, (3) Navigator ownership path, (4) acknowledged date for the AI backlog response.*

## 1. Akash / Dirk WAM Meeting Prep — product capability and plan (refocused 07-16)

**Financial side: settled.** Metric definition, 87.23% attainment story, and the Engel briefing decks are decided and updated. Reference only if asked; if the metric revision comes up, the rationale stays "the original metric measured the wrong thing," never re-measurement rescuing performance. The $32M pipeline number remains entroCIM-only — keep it out of the WAM narrative.

**The talk track: "ADM does not meet expectations today. Here is the plan."**

Lead with the honest current state: ADM's data foundation is the constraint — license identification is manual, attribute coverage is incomplete, supplier data participation is thin, and complex-build assets aren't captured. The product is production-ready and sellable where source data and outputs are defined; ADM is what limits "where."

The plan, three moves, each with an owner and a next step:

| Move | What it fixes | Owner | Next step |
|---|---|---|---|
| 1. Fix the data problem: add attributes | Classification, software/hardware differentiation, warranty/subscription logic (DDPTRK-6346 global attributes) | Akansh (track owner); process ownership ask in flight to Anna Baker/MDM | Rescheduled attributes session with mandatory decision-owners; Darryl asks Anna Baker directly |
| 2. Work with vendors to populate data | Attribute coverage at scale; renewal and entitlement accuracy | David Blondel (Jarod Booth's org) + Akansh; Natalie Marquardt (Sales Ops side) | Finalized attribute requirements to Jarod (flagged High urgency); supplier engagement by revenue priority |
| 3. Add VAS as a capability | Complex-build asset capture — serial/MAC, the WMX gap that otherwise persists "through at least 2028" | Akansh driving; roadmap authority: Steve Leslie (GPO) | Steve/Sid gap confirmation + GPO decision session — dates committed by end of July |

- **Proof point in flight:** first sales-notification release (MVP1) tentative Aug 3 behind a quality gate; EUDM license feed live but manually triggered pending a clustering fix. Framing discipline: capability delivered, automation in progress, first send gated on quality. Do not let "July release" survive in anyone's slides.
- **Summary line for Sean:** the product is sellable where data is defined; ADM is the constraint; the plan attacks the constraint on three fronts — attributes, vendor data, VAS — and every front has a named owner and a dated next step. None of the gates are new product spend; they're enterprise participation.
- **Timing discipline (new 07-16):** the first sales-notification release is no longer "July" — MVP1 is tentative **Aug 3** behind a quality gate (supplier exclusions, cancelled-line cleanup, sender/format, FAQ/SharePoint). And the EUDM license feed, while live, is manually triggered daily pending a clustering fix. In any Dirk/Akash framing: capability delivered, automation in progress, first send gated on quality. Do not let "July release" survive in anyone's slides.
- **Demand-side signal worth using (new 07-16):** Debbie Hunter (Senior Director, Sales Operations — Natalie Marquardt's leadership, under Kim Thomas → Dirk) proactively asked about ADM's future and received the service/platform slides. Sales Ops leadership pulling for the WAM commercial path is the best kind of evidence for the resource case.
- **Logistics to close with Sean:** who presents what; Lisa Orton pre-meeting heads-up; slide readiness date.

## 2. CSS Platforms Product Strategy

### 2a. Team and organization (Product / Platforms / Deployment)

Current structure (confirmed via org chart 07-15): Darryl org of 32. Ron Snyder (Development) carries a flat span of 11 with no managers beneath him while also running release governance. Chad Steger (Platform/Deployment) has 9 via two managers (Scott Dunn, Syed Zaidi) plus India engineers. David Blondel (Product) carries both WAM and entroCIM product leadership plus two Showcase executors.

- **Point to make:** the org conversation is an operating-model response to portfolio expansion (budgeting, accountability, execution), not a land grab. Ron's flat span is the visible strain point; any broadened scope needs a structure answer there.
- **Near-term evidence:** delivery coverage window is now **Jul 15 – Aug 11** (Chad on paternity leave; Syed out/limited Jul 16–21 while relocating; Matt Heid also on paternity leave) with active blockers at eight customers — shows how thin the middle layer is. Counterpoint that helps the org story: Chad left a comprehensive 13-project handoff with named primaries — the team runs on process, not heroics; the ask is structure to make that durable.

### 2b. Broadened scope: entroCIM, WAM, CSS AI backlog, Navigator

- **CSS AI backlog:** this is Ankit's Power BI list; access is still blocked, which blocks the full sweep. But do not walk in with only "blocked" — lead with what doesn't need the list: **two candidates are already evident** from the AI strategy work. (1) AI part classification and research — researches and classifies manufacturer parts, software, licenses, warranties; feeds MDM readiness and the same global-attributes work your team is already driving, and it's already named in the WAM 90-day plan as under evaluation. (2) Document-to-asset/contract extraction — structured data from invoices, POs, contracts; cuts WAM onboarding effort. Both fit the evaluation framework (bounded, measurable, human-reviewed, CSS synergies). Then: "full shortlist within X days of Power BI access" and ask Sean to lean on the access. Risk if it drifts: AOP proceeds without credible AI commitments, and the AI-pace dissatisfaction is Sean's personally.
- **Navigator (the ownership item):** the Digital Product List (marked Team to Review) names Chris Gazdic as Product Executive with Dirk Naylor as sponsor, while Navigator sits in Darryl's stated portfolio scope. The integrated portfolio model positions Ascent/Navigator as the customer-facing service-delivery layer over WAM and entroCIM, so the interface matters regardless of who owns it.
  - Option 1: Navigator PE moves to Darryl; consistent with the service-delivery integration story; adds scope and resource needs.
  - Option 2: Chris retains PE; Darryl's scope statement is corrected; a defined integration interface (roadmap alignment, shared milestones) protects the portfolio model.
  - Option 3: split accountability; PE with Chris, service-delivery integration with Darryl; workable only if the boundary is written down.
  - **Ask of Sean:** pick a path or name the forum and date where it gets decided. The product list is in team review, so the correction window is now.
- **Related gap worth surfacing:** Insight by Anixter is CSS-impacted with no PE and no sponsor on the list. As the review comment, propose it get an owner (not necessarily Darryl).

### 2c. Resources and costs vs. portfolio priorities

**Name AOP explicitly** — "wrestle WAM AOP planning to the ground" was Sean's own phrase on Monday. Frame this section as the start of exactly that: constraints identified per product, resource alignment following the constraints, AI commitments entering AOP only at credible readiness. Sean should leave hearing his Monday asks being answered, not a parallel conversation.

The portfolio's two commercial stories point in opposite directions, which is the resource argument:

| | Objective | YTD | Attainment |
|---|---|---|---|
| WAM sales | $19M | ~$16.7M | 87.23% |
| entroCIM software | $6.6M | ~$1.1M | 16.7% |
| entroCIM pull-thru | $3M | ~$28K | 0.95% |

entroCIM counterweights: $32M approved pipeline; June saw 11 opportunities created ($915K), 4 wins, $373K bookings. The takeaway: WAM's constraint is enterprise data and operating model, not funding; entroCIM's constraint is commercial conversion, not product readiness. Resource alignment should follow those constraints rather than splitting evenly.

## 3. One-line mentions (added 07-15 — do not let these grow into agenda items)

- **Supplier-data governance:** "I've assigned ownership inside my team — Akansh runs the attribute/data-governance track, David handles Jarod Booth. What I need from you is air cover with the cross-functional data teams. Yesterday's data-requirements session couldn't proceed because the MDM and IT stakeholders didn't show — that's the pattern: attendance is unreliable and accountability outside my org still isn't named." The ask: Sean's weight behind attendance/accountability, not a decision.
- **Complex-build asset gap (WMX):** "A formally identified capability gap — WMX can't capture serial/MAC for complex builds through at least 2028 absent action. Akansh is driving GPO engagement with Steve Leslie; I've targeted end of July for the decision path." Visibility only; no ask unless GPO stalls.
- **Architect role (fits the 2a org discussion):** "Closed — Shawn Clark, internal move, done as a transfer (HR confirmed same-day, no req needed); David is running it while Chad's on leave, and Shawn keeps his current duties through the transition." Evidence the org can move fast on staffing with zero continuity gap.
- **JCI MSP agreement (new):** "The Johnson Controls MSP agreement — the connectivity backbone for Hosted entroCIM Managed Services — sat idle for five weeks after eight months of negotiation. I restarted it yesterday and I'm driving it to signature. One internal dependency I may need help clearing: the Wesco Cloud Architecture review of our Azure hosting proposal, which may never have been completed." Visibility now; the Cloud Architecture nudge is the ask if it surfaces as stuck.

## Watch-outs

- Sean drove the reset, the AI ask, and the AOP push personally (attribution corrected 07-14). Treat all three as his priorities, not staff noise.
- **If Sean raises agile execution concerns** (he did Monday; the brief doesn't otherwise cover it), the holding answer is real and specific: entroCIM Jul 20 release is under go/no-go discipline with code freeze active and deal-breaker-bugs-only; a single release-readiness view with red/yellow items and owners has been requested from Ron and David; definition-of-done and code-coverage work plus the knowledge-sharing initiative are live. Offer a follow-up if he wants depth — don't improvise metrics in the room.
- If the org discussion goes deep, avoid committing to structure changes in the room; take a proposal action with a date instead.
- Field-note discipline: anything decided verbally Thursday goes to `08_Field_Notes.md` so the record catches it.
