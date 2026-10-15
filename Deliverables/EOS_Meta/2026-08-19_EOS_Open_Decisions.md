# Three Open Decisions

**Date:** 2026-08-19
**Why this exists:** recommendation 6 of the use case review, which you asked to see in detail before deciding. A third item is added because executing recommendation 3 surfaced something that needs your answer rather than mine.

---

## Decision 1 — `Deliverables/CSS_Platforms_2027_Ideation/`: superseded or distinct?

### The finding: the files already answer this, and the 08-06 flag was wrong to treat it as open

The 08-06 review flagged these three files as "look like precursors to the more developed `Products/CDA/` material, needs Darryl's read on whether they're superseded or distinct." Reading them, two of the three declare their own status in a banner on line 1, written the same day they were created.

| File | Self-declared status | Actual state |
|---|---|---|
| `2026-07-23_New_Product_Ideation_Charter.md` | "SUPERSEDED 2026-07-23 PM by the governing documents in `Products/CDA/00_Charter/`. Retained for record; do not cite as current." | Dead. Superseded within hours of being written |
| `2026-07-23_ChatGPT_Addendum_and_Joint_Workplan.md` | "SUPERSEDED 2026-07-23 PM ... (content absorbed). Retained for record; do not cite as current." | Dead, content absorbed |
| `2026-07-23_Ideation_First_Pass.md` | No supersession banner. Carries two scoped caveats and the line "still an active Phase 1 input" | **Live.** Not superseded |

So the question was never "are these superseded." Two are, explicitly, and have been for four weeks. The real issue is the third one.

### The actual problem

`2026-07-23_Ideation_First_Pass.md` is a live Phase 1 input to the CDA programme, and it is sitting in `Deliverables/`, outside the initiative it belongs to. On 2026-08-18 you reorganised `Products/` so that `CDA/` is "the home for all current and future Connected Device Assurance material." This file is current CDA material and it is not there. Anyone working the CDA phase structure, including me in a future session, would not find it.

Its two caveats matter and should travel with it: its concept scores use the old 8-criterion unweighted scale and are not comparable to the governing 10-criterion weighted scorecard, and its "verified rollback" language is superseded by the governing rollback standard. Those caveats are written into the file, which is why moving it is safe.

### Options

| | Option | Effect | Cost |
|---|---|---|---|
| **A** | **Move all three into `Products/CDA/`.** First Pass to `01_Phase_1_Divergence/` alongside the other Phase 1 material; the two superseded files to a new `00_Charter/Superseded/` | CDA material is all in one place. The live input becomes findable. The decision trail is preserved and visibly dead | One move. No content change |
| **B** | Move only the First Pass; leave the two superseded files in `Deliverables/` as a dated record of the 07-23 session | Fixes the findability problem only. Leaves two dead files in the studio folder where live work lives | One move |
| **C** | Leave all three where they are | Nothing breaks today. The live Phase 1 input stays invisible to anyone working CDA | Zero now, recurring later |

### Recommendation: A

The superseded files are not worth protecting as a separate record; their supersession is documented in their own banners and in `Products/CDA/00_Charter/`, which is where anyone would look. The reason to move all three rather than just the live one is that splitting a session's output across two trees is what created this ambiguity in the first place. Keep the 07-23 session's material together, under the initiative it produced.

**What you are accepting:** `Deliverables/CSS_Platforms_2027_Ideation/` disappears as a folder. If you think of that session as a studio artifact rather than CDA programme material, choose B.

---

## Decision 2 — The team interface: force the pilot, or drop it?

### The finding: this decision has already failed the system's own rule for triggers

On 08-06 you decided: "Team interface: test before building. Next session where a 'brief me on [person]' or 'state of play with my directs' request comes in, treat it as the pilot."

Thirteen days later the trigger has not fired, because you have not made that request. The pilot has therefore not happened, and no evidence exists either way.

`CLAUDE.md` has a rule for exactly this, written on 07-27, nine days before the decision that violates it. The trigger backstop: "a trigger whose own event has no date is an undated item in disguise," and "when a trigger depends on something unknown, the unknown becomes the action." The 08-06 team-interface decision is an undated item in disguise. Its triggering event has no date, no owner, and no reason to expect it will occur, since you have run five weeks of this system without organically asking for a stakeholder briefing. The absence of the request over thirteen days is itself the strongest evidence available: this is not a thing you reach for.

### What a team interface would actually be

Worth stating concretely, because "team interface" has never been defined. The raw material exists: `06_Stakeholder_Map.md` is 54 KB, covering your directs, executive leadership, customers, and cross-functional contacts, with priorities, decision style, and open topics. It is maintained on every briefing and has never once been read back to you as a product. The plausible outputs are a "state of play with my directs" synthesis (who is carrying what, who is stuck, who needs your attention this week, drawn from `06` plus the registers plus `Products/`), or a per-person brief before a one-to-one.

### Options

| | Option | Effect | Cost |
|---|---|---|---|
| **A** | **Force the pilot once, on a date.** I generate the "state of play with my directs" synthesis at the next weekly briefing, 08-24, unrequested. You judge it against one question: did it tell you anything you did not already know | Converts an undated trigger into a dated action, which is what the backstop rule requires. Produces evidence either way | One section of one weekly briefing |
| **B** | Drop the idea and close the decision | Removes an open item that has been quietly stalled for thirteen days. `06` continues as underlying data feeding briefings and drafts, which is what it already does well | Zero. You lose an option you have not reached for |
| **C** | Build a standing file or briefing section now | Adds surface area to a system whose diagnosed problem is surface area, on no evidence | Not recommended |

### Recommendation: A, with B as the automatic outcome if it lands flat

Run it once at the 08-24 weekly, unrequested, and judge it. If it tells you something you did not know, it earns a place. If it reads as a restatement of the stakeholder map, drop it that day and close the decision permanently rather than leaving it open for another month.

The reason to spend the one session rather than drop it outright: `06` is 54 KB of maintained knowledge that has never been surfaced as output, and the cost of finding out is a single briefing section. The reason not to spend more than that: thirteen days of non-request is real evidence, and the honest prior is that this lands flat.

---

## Decision 3 — Register A disposal sweep (added, not in the original seven)

### Why this is here

Recommendation 3 capped Register A at 15. Executing it revealed that Register A cannot be capped the way `03` and `04` can. Those two came down by moving items between tiers, which I can do and reverse. Register A holds your own commitments; there is nowhere to move them, and me dropping them unilaterally would be the 07-27 mis-attribution failure running in reverse. It comes down by disposal, and disposal needs you.

The register is at 21. Twelve items are overdue and one has no date at all.

### The finding worth more than the sweep

Of the twelve overdue items, **ten carry a date I proposed, not a date you set.** Only A3 and A5 carry dates recorded as yours.

That is a defect in how the dating rule is being satisfied. The rule says every Register A item carries a date. It is being met by me proposing one, which produces a dated register but not a set of commitments you actually made. An item three weeks overdue on a date I invented is not evidence that you are behind; it is evidence that the item was never really yours to be behind on, or that the date was never real.

**Proposed fix, for your yes or no:** a proposed date expires. If a date I proposed passes without you acknowledging it, the item comes back to you once as "set a date or drop it," and if it comes back a second time unanswered it is dropped automatically. This stops the register accumulating fictional overdue items, and it makes the overdue count mean something again.

### The sweep

One line each. Answer with: **done** / **drop** / **delegate to [name]** / **[new date]**.

**No date at all, in breach of the dating rule**

1. **A1** WMX complex-build follow-up. Waiting on Akansh's confirmed date since 07-17. Under the backstop rule, getting that date is the actual action.

**Overdue on dates you set**

2. **A3** FY27 financial goals, capacity model, capabilities. Due 08-03, sixteen days.
3. **A5** AOP alignment meeting with Brad Stevens and Gregg O'Brien. Due 08-07, twelve days. AOP submits in two days, so this is either urgent or moot.

**Overdue on dates I proposed** (these are the ten; several look like they should simply close)

4. **A10** Dell Service Management Process, confirm the cadence. Proposed 07-29, twenty-one days. Oldest item in the register.
5. **A8** AI Council, get the council date and prep materials. Proposed 07-30, twenty days.
6. **A14** Verify whether the Rob Cook meeting is Thursday or Friday and inform the group. Proposed 08-03. This is a two-minute task sixteen days old, which usually means it is already done or no longer relevant.
7. **A4** CSS product ideas and AI-researched needs analysis. Proposed 08-05, fourteen days.
8. **A9** CMP tool residence and Connected Safety adoption. Proposed 08-05. Rides with A4.
9. **A15** First-pass 2027 scenario analysis, hold-costs versus development-cost-reduction. Proposed 08-05. Overlaps the AOP work now in flight; may be absorbed.
10. **A16** Colliers 211 West Fort St legacy support model, name the support owner. Proposed 08-06.
11. **A27** i3 Alliance, send the Section 8 edits and rationale to Legal. Proposed 08-07. This one is load-bearing: the i3 win in the ledger is not banked until Legal has it, and C-i3-1 is waiting on it.
12. **A23** Leading Managers baseline assessment. Proposed 08-07.
13. **A26** Reply to Jeff Verdun on whether the Wesco role is still open. Proposed 08-07. A reply, twelve days old.

**Not overdue, listed so the register is complete:** A24 (08-20), A19 and A21 (08-21, AOP), A28 (08-24), A22 (08-31, under challenge), A25 (08-14, five days), plus the two triggered items A6 and A7.

Six dispositions from the thirteen above brings the register to 15. My read is that items 6, 13, and 11 are the most likely to clear in seconds, and that 4 and 5 have been carried long enough to be candidates for dropping outright rather than re-dating.
