# entroCIM Commercialization v11: Review Items
Built 2026-08-10. Companion to `2026-08-10_entroCIM_Commercialization_v10.1_to_v11_Comparison.md`, which holds the full change record and the method. This file is the action list.

Ordered by cost of leaving it alone, not by effort. Items 1 through 3 are corrections. Items 4 through 8 are judgment calls that need Darryl's decision. Items 9 through 11 are cleanup.

## 1. Fix the version labels on both documents

**Deck.** Title slide reads "Digital Products leadership brief | July 2026 (v8)". It is the only version marker in the file and it is on the first slide of a document addressed to six named executives.

**Report.** Classification line reads "Internal Draft, v9".

**Report Appendix G, version history.** The newest row is headed "v9 (July 28, 2026)" and its text describes the v11 restructure, including the four deck moves to A12 through A15, and states "Companion deck reissued as v9." The v10 row never existed and the original v9 changelog has been overwritten.

Recommended fix: label both documents v11; add a v11 row to Appendix G describing the restructure and voice pass; reconstruct or reinstate the v9 row; add the missing v10 row. If the v9 text cannot be recovered, say so in the row rather than leaving the gap silent, because Appendix G is the audit trail a reviewer uses to test whether the analysis has been stable or churning.

Why this matters beyond tidiness: this deck's central argument is that leadership should extend patience on the basis of disciplined execution. A cover page with the wrong version number is a small, visible contradiction of that argument.

## 2. Repair eleven broken cross-references in the report

Section 9 became Appendix K and sections 10 through 15 renumbered to 9 through 14, but the internal references were not updated. Full table in the comparison file. Summary of what to change:

- Three references to "Section 9" now point at Compensation, measurement, and P&L alignment when they mean product marketing. These should read Appendix K. This is the worst case, because the reader lands on real but wrong content rather than a dead end.
- Two references to "Section 15" and one to "Sections 13 through 15" should be Section 14 and Sections 12 through 14.
- Two references to "Section 12" (cross-business-unit model) should be Section 11.
- One reference to "Sections 10, 12, and 15" should be Sections 9, 11, and 14.
- The front-matter reading guide still describes Sections 7 through 12 as including product marketing. Both the span and the content list need updating.
- Appendix K retains subheadings 9.1 and 9.2.

Do this before the report goes anywhere. A reviewer who follows one pointer and lands on the wrong section will start checking the others.

## 3. Add an inbound pointer to deck A13

A12, A14, and A15 each received an explicit cross-reference in the main flow where the slide used to sit. A13, Product marketing: what the engine has to produce, did not.

This is the appendix slide covering the capability the deck names as the weakest thing Wesco has. The main flow asserts that weakness on the "product is strong, commercial system is missing" slide, recommends evaluating an external partner, and asks for a build/buy/hybrid decision on the decisions slide, answering it "hybrid: external acceleration plus a named internal owner." Nothing tells a reader who wants the substance behind that recommendation where to find it.

One sentence on either the commercial-system slide or the decisions slide closes it.

## 4. Reconsider moving A14 out of the main flow

This is the one relocation I would push back on. The other three are supporting material; A14 is a rebuttal.

A14 carries the argument that distributor conversion rates and quarterly product forecasts will always score entroCIM a laggard, and names what to measure instead: qualified opportunities, executive access, pilot conversions, install-base expansion, ARR growth. That is the pre-emptive answer to the most probable objection in the room, which is that the numbers say this is not working. The deck itself states $1.1M against a $6.6M target and 16.7% attainment on a main-flow slide, so the objection is invited by the deck's own honesty.

In v10.1 this sat at s29, immediately before the motion slide. In v11 the only trace in the main flow is one sentence on the five-mismatches slide pointing to the appendix. A rebuttal in an appendix only works if the objection is raised and there is time to navigate to it. If the objection is raised late, or raised by the most senior person present, that is exactly when navigating to an appendix is hardest.

Recommendation: restore A14 to the main flow, or promote its "why traditional pipeline metrics fail" panel into the slide that states the commercial shortfall. Keep the rest in the appendix.

## 5. Confirm the decisions-slide reframing is intended

"Executive decisions required (owners to be assigned by leadership)" became "Decisions we need from this group."

This is the largest substantive change in the deck and it is not voice. v10.1 deliberately deferred owner assignment. v11 asserts that the people in the room are the deciding body. Given the named audience, that is defensible and stronger.

The tradeoff is that it removes an escape hatch. Under v10.1 phrasing, a meeting ending without named owners was still a successful meeting, because assignment was explicitly a later step. Under v11 phrasing, a meeting ending without decisions is a visible failure.

Note also that the report did not make the same move: report section 1.7 reads "What we are asking leadership to decide," and section 14 is "Decisions we need from leadership." So the deck now says "this group decides" while the companion report says "we are asking leadership." If both circulate, align them.

## 6. Decide whether "moat" should have become "advantage"

"Device data models: the moat only a distributor can build" became "the advantage only a distributor can build."

My read is that "moat" was load-bearing. It asserted defensibility a competitor structurally cannot replicate, and that non-replicability is the whole basis of the distributor-adjacency argument and of the claim that this is a position rather than a feature. "Advantage" is generic; every vendor in the threat ranking claims advantages.

If the change was jargon avoidance, I understand it, but I would either restore "moat" or replace it with language that still asserts non-replicability, for example "the one advantage a software vendor cannot build."

## 7. Decide whether to restore the capitals on Infrastructure Lifecycle Intelligence

"Compete as Infrastructure Lifecycle Intelligence, not dashboards" became "We compete as infrastructure lifecycle intelligence, not dashboards."

In v10.1 this was a proper category name and it matches the positioning language carried in `Products/entroCIM/entroCIM.md`. Lowercase converts a category claim into a description of activity. If the intent is still to own and name the category, restore the capitals. If the intent has changed, that is a positioning decision worth recording, not a copy-edit.

## 8. Confirm the audience name spelling on the deck title slide

The title slide addresses "Greg O'Brien." `03_Decision_Log.md` and `04_Executive_Watch_List.md` both carry "Gregg O'Brien," flagged there as new and unconfirmed. One of the two is wrong, and the one on the cover is addressed to him personally.

## 9. Remove the stale "prior version" line in the deck

The competitive section reads "Feature content is cut ~30–40% from the prior version; the appendix battlecards carry the sell-against detail." That described an earlier transition. In v11 it implies content was cut relative to v10.1, which is not what happened; content was relocated and the page count is unchanged. Either update the comparison base or drop the clause and keep the battlecard pointer.

## 10. Resolve the licence/license mix in the deck

v11 introduces British "licence" twice while keeping American "license" seven times, including both spellings on the A12 slide. Pick one. The report has carried a single "licence" against nine "license" in both versions, so fixing the report is optional but consistent.

## 11. Minor residual carried forward from v10

Report slide 11 equivalent still uses "foundation" where the 2026-07-29 architecture preference was "platform" for SkySpark. Noted in the product record as cosmetic and not a correctness issue. Unchanged in v11; fix opportunistically.

## Not a v11 defect, but now live

Nothing in v11 resolves the framing-consistency exposure already recorded in `Products/entroCIM/entroCIM.md`. The deck still asks for enablement with no new headcount and no major capital, which sits against the entroCIM FY27 AOP request, and the Path B scale-up language still sits against the AOP audience rule that entroCIM reads as sustaining.

This was latent while the deck was unsent. Circulation remains gated on Mike Wassil per the 07-24 position, and AOP alignment carries an 08-21 deadline. If v11 is the version that moves, prepare the reconciliation answer first. The reviewer question to expect is why a document arguing for scale-up accompanies a sustaining budget request, and the answer needs to be one sentence, not an explanation.

## Consequence of retiring v10-EXEC

Per Darryl's decision 2026-08-10, v11 supersedes `Wesco_entroCIM_Commercialization_2026-08-05_v10-EXEC.pptx`.

Two follow-ons. First, every v10-EXEC slide carries a provenance stamp reading `v10-EXEC n / v10 src n` plus the same mapping in its speaker notes; those now point at a superseded source deck. Second, v10-EXEC and v11 solved the same problem by different means: v10-EXEC cut to 21 slides, v11 tightened the main flow to 31 while keeping the full 50-page artifact. If a short-form read is still wanted for a different audience, it should be regenerated from v11 rather than v10, so voice, structure, and appendix numbering match. Treated as a separate piece of work, not started.
