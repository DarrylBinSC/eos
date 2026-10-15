# Sean Update Standard

> Added 2026-07-14. Written update to Sean McCloskey. **Cadence added 2026-08-19:** generated with the first weekly briefing of each fortnight whether or not Darryl asks, and on request at any time.

## Meeting frame and close-out (added 2026-10-14, from Darryl; supersedes the fortnightly written update as the default)

**Why.** Four consecutive fortnightly drafts (08-19, 09-09, 09-28, 10-13) were never sent. Darryl, 2026-10-14: Sean does not read updates of that length; asked directly whether he wants updates, Sean said no. Darryl gets 30 minutes when he asks for a meeting, and the meeting is often hijacked or Sean does not see the priorities the same way. The written update was the wrong instrument for this reader. The pattern below replaces it.

**The pattern, around each meeting Darryl gets:**

1. **Morning of: a three-line Teams frame.** What the meeting is for, and the two or three things Darryl needs from Sean, numbered. Deck attached for reference, not as a pre-read. This puts the asks on record before the meeting can drift.
2. **In the meeting: the takeaways on the first content slide.** Title "Takeaways": one line per product, the ones that need something from Sean marked "from you" (Darryl, 2026-10-14: pick the top takeaway per product rather than guessing at what he needs to decide; some products matter more than the sensitive one). Before the portfolio. Exception to the briefing-deck rule that asks live in the notes: a meeting that may be hijacked needs the asks heard in the first minute, so a drift at minute eight comes after Sean has heard them, and Darryl can pull back to "I still need your answer on these." Then the sensitive item that carries the decisions, then awareness items, closing on whatever is Sean's own interest (his idea, his decision).
3. **Same evening: a three-line close-out.** What was decided, what was not, the next date for anything open, in Sean's words where possible. This is the written record Sean will tolerate: short, about his decisions, not Darryl's activity. The decisions go into `03` and `05` the same day.

**What stops.** The fortnightly generated draft (weekly briefing section 19) is retired as a default. `09_Impact_Ledger.md` remains the archive. A written update is produced only when Darryl asks for one or when a meeting is not available and something cannot wait; it then follows the scope, threshold and structure rules below, at one Teams screen.

**Showing Sean his own interests.** Darryl's products are not the company's most important. The deck cannot change that, so it shows Sean's own stakes inside the material: a decision he made (the capacity reduction), an idea that is his (Launch Studio), a question he asked (whether ADM is recoverable). Lead with what carries Darryl's asks; close on what is Sean's.

Template for the two messages: `Deliverables/Exec_Briefs/2026-10-14_Sean_Meeting_Frame_and_Closeout.md`.

## Scope and Threshold (added 2026-08-19, from Darryl, after the first draft was rejected)

**This is the most important section in this file. The first generated draft failed on both rules below.**

**Scope: four products only.** entroCIM, WAM, Ascent Navigator, and CDA. Customers, partners, and vendors appear only where they change one of those four products at a portfolio level. A TCCC control closure, a JCI negotiation step, a Dell escalation, a Louvre snag list, an FRB delivery, a Strev invoice: none of these belong in a Sean update on their own. The i3 Alliance is includable only because Section 8 decides whether entroCIM is the system of record on Alliance projects, which is entroCIM platform positioning; it would not be includable as a contract-status item.

**Threshold: what a VP needs to decide, fund, defend upward, or not be surprised by.** Nothing else. Apply this test to every candidate line, in Darryl's own framing:

> *There is no value in telling Sean about key things I worked on over the course of a week. I do not burden Sean with the day-to-day minutiae of my work. That is why he hired me and trusts me.*

An update that lists activity spends the trust that makes the role work. If an item would not change what Sean decides, funds, says upward, or would not embarrass him to learn late, it is not in the update. It is already in `09_Impact_Ledger.md`, which is the archive of everything Darryl works on and exists precisely so the update does not have to carry it.

**Things that read as valuable and are not:** shipped features and releases, sprint completion percentages, migration milestones, resolved tickets and outages, individual customer deployments, invoice and vendor administration, anything whose real message is "the team is working." Delivery competence is assumed. Reporting it implies it was in doubt.

**Things that almost always clear the bar:** a funding case that does not hold up, a plan that cannot reach breakeven at authorised levels, an attribution or accounting problem a reviewer will find, a benefit claim that needs a decision before it can be made, a platform positioning question that applies across every project, a number that will be quoted upward and needs to be right, and anything Sean would be blindsided by in a review.

**Structural preference.** Lead with the portfolio position, not with progress. A compact table comparing the four products on the dimension that matters usually does more work than any amount of prose. Then the exceptions that need a decision. Then the decisions themselves, each with a recommendation and what Darryl needs in order to act.

**Length follows from the threshold.** If it does not fit one screen in Teams, the filter was applied too loosely before it was applied too tightly. Genuine exceptions (a first update, an AOP window) become an email with the same structure.

## What Sean Needs (per 06_Stakeholder_Map)

Executive updates and status visibility across: platform portfolio, entroCIM, WAM (reset discipline), staffing and hiring, investment/AOP decisions, AI progress and team ownership, agile execution. Sean re-shares upward; every claim must survive Dirk/Engel scrutiny, so realized-vs-planned discipline (Benefits_Realization_Standards) is mandatory.

## Generation Procedure (Claude)

1. Pull from: `09_Impact_Ledger.md` (wins since last update), `03_Decision_Log.md` (made + approaching that need Sean), `04_Executive_Watch_List.md` (High items only), `05_Commitments.md` (items involving Sean either direction), latest briefing. **During an AOP cycle, read `AOP_FY27/Change_Logs/` first** — the funding cases, margin positions, and attribution problems in those logs are usually the whole update, and they are not visible from the registers. The 08-19 rewrite found the entire VP-level story there after the first draft missed it by working from the ledger alone.
1a. **Filter before drafting, not after.** Apply the scope and threshold rules above to the candidate list and discard first. Drafting everything and then trimming produces an activity report with the small items removed, which is still an activity report.
2. Track the date of the last Sean update at the top of `09_Impact_Ledger.md`; report the delta since then, not cumulative history.
3. Filter to Sean's altitude: portfolio and business outcomes, not execution detail. If an item wouldn't change what Sean decides, funds, or says upward, cut it.
4. Draft in Darryl's voice per `Communication_Preferences.md`: no em dashes, minimal bold, direct, measured. Financial metrics in a compact table, never inline prose.
5. Default length: fits on one screen in Teams. If it can't, it becomes an email with the same structure.

## Update Structure

1. **Opening line** — the single thing that matters, stated as a position rather than an activity. Not "here is what happened," but "here is where the portfolio stands and what is wrong with it."
2. **Portfolio position** — the four products compared on the dimension that decides something. A table, usually.
3. **The exceptions** — one short section per product that needs attention, saying what is wrong and why it is above Darryl's line, not what was done about it.
4. **Awareness only, no action** — anything Sean must not learn late. Keep to a paragraph. Omit when empty.
5. **Decisions needed from you** — each with a recommendation, the options if they are genuinely open, and what Darryl needs in order to move.
6. **Ask** — the specific time or support required.

**Replaced the old "Progress" section on 2026-08-19.** A standing Progress section guarantees an activity report, because a section that exists must be filled. Wins appear only where they change a decision, and then they appear inside the relevant product section, not as a list. Sections 4 and 6 are omitted when empty; never padded.

## Quality Bar

- Successes tie to measurable or observable outcomes, not activity ("connection completed Jul 3" not "made progress on integration").
- Never let a High-risk item Sean would expect to know about appear first in someone else's channel. If it's High on the watch list and portfolio-visible, it's in the update.
- Consistency check before sending: does this match the current narrative in flight (e.g., WAM reset framing, Engel deck, Dirk/Akash slides)? One story everywhere.


## Failure Mode to Check Before Sending (added 2026-08-19)

Read the draft and ask: could a competent director have written this from their calendar? If yes, it is an activity report and it goes back. The test the update has to pass is different: could anyone but Darryl have written it, and does it put a decision in front of Sean that only Sean can make?

The first generated draft (2026-08-19, v1, retained at `Deliverables/Exec_Briefs/2026-08-19_Sean_Update.md`) failed this test. It covered six weeks across every account and partner, led with delivered features, and buried the one fact that mattered: entroCIM's FY27 plan does not reach breakeven at any authorised revenue level, and cannot be fixed on the cost side. v2 is the corrected version and the model to follow.
