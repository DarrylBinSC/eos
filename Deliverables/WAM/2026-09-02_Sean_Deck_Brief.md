# Sean WAM Deck — Brief

**Created:** 2026-09-02. Written to be picked up cold in a later session.
**Sequence:** this brief, then a draft deck and storyline built by Darryl and Claude, then a working session with David and Akansh to correct the messaging and fill the gaps, then the deck to Sean.
**Background:** `Deliverables/WAM/2026-09-01_Sean_WAM_Program_Update_Prep.md`, `Products/WAM/Strev_2027_Priorities.md`.

## Audience and purpose

Sean McCloskey, first WAM program update ever given to him. He re-shares upward to Dirk and Engel, where WAM benefits underreporting already left a negative impression. The deck has to survive that audience without Darryl in the room.

## The two decisions the deck exists to produce

Everything in it earns its place by moving one of these.

1. **Funding attribution for the Strev 2027 investment.** Recommendation: fund it as a CSS Platforms investment, not a WAM one, because entroCIM and Ascent are named primary integration targets and two of the three investment areas deliver value outside WAM. Decided before the AOP number is set, not after.
2. **Cross-functional air cover on internal data collection.** Five constraint holders on serial number, metadata and license master data, four of them outside Darryl's organization. This is the ask only a VP can satisfy.

If a slide does not serve one of these, it is backup.

## Storyline

Nine slides. Each carries a title that names the page and a headline that says the thing, per `Reference/Communication_Preferences.md` section 2a.

| #   | Page                               | The sentence it has to land                                                                                                        |
| --- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Where the capability stands        | Position, not progress. License visibility is real; completeness is not, and completeness is what the business needs.              |
| 2   | What the business gets today       | License data in ADM is delivered and in use. Serial number capture works end to end for simple products.                           |
| 3   | Complex builds, the gap            | Serial-to-VAS association does not happen today. The VAS capture point was made explicit five weeks ago and is unproven at volume. |
| 4   | What is blocking completion        | Five constraint holders, four outside the organization. Named, with what each holds.                                               |
| 5   | The evidence                       | Three data-completeness defects, one without a fix owner for four weeks. Not an admission; the proof of slide 4.                   |
| 6   | Strev 2027 priorities              | Three investment areas in business terms: asset data management, tenant scalability, API and integration.                          |
| 7   | Why this is a portfolio investment | entroCIM and Ascent are the named integration targets. Funding it inside WAM misattributes spend that benefits three products.     |
| 8   | The 2027 requirement               | The number, its basis, and where it sits in the plan. Blocked until inputs land; see below.                                        |
| 9   | What I need from you               | The two decisions, each with a recommendation and what Darryl needs in order to act.                                               |

Backup, not presented: functional overview across license, asset, serial and metadata, entitlement and renewal; build plan with sequence and dependencies; coverage and completeness numbers; defect detail; FY27 P&L reconciliation.

## What must not be in it

Feature lists, sprint or release status, delivery milestones, ticket counts. Delivery competence is assumed and reporting it implies it was in doubt. No benefit stated as realized unless it has a baseline, a measure and evidence; planned and realized stay visibly separate. No 2027 figure quoted without its basis, because three FY27 items are already open with Finance and will be quoted back.

## What is still missing, and what it blocks

| Missing                                                                 | Blocks           | Owner                                   |
| ----------------------------------------------------------------------- | ---------------- | --------------------------------------- |
| Strev sizing by investment area                                         | Slide 8 entirely | Akansh, via Sunny Sharma's organization |
| Whether Strev SOW spend sits in the FY27 WAM P&L or nowhere             | Slides 7 and 8   | Akansh                                  |
| Which items are Wesco requirements versus Strev's own product direction | Slide 7          | Akansh                                  |
| Serial, MAC and asset tag coverage, simple versus complex               | Slide 3          | Akansh                                  |
| License master data completeness as a number                            | Slides 1 and 2   | Akansh, with MDM and DDP                |
| Whether Ron and the Navigator owners were consulted on the API targets  | Slide 7          | David                                   |

Slides 1 through 7 and 9 can be drafted without any of this. Slide 8 cannot.

## Where to pick this up

Say: "build the draft deck and storyline for the Sean WAM update, per the deck brief." Claude drafts slides 1 to 7 and 9 with placeholder positions where numbers are missing, marks every unverified figure, and produces the working-session agenda for David and Akansh from the gaps that remain. Format per `Reference/Deck_Construction_Standards.md`.

Open from the prep, still unanswered: is the meeting Sean alone or wider, did Sean give any timing, and is "Strev enhancement costs" his own phrase.


---

## Correction, 2026-09-09: audience position, and the storyline

**Source: Darryl, direct, 2026-09-09. Recorded during the WAM / ADM feasibility and ownership evidence pack session.**

The Audience and purpose section above describes this as the first WAM program update ever given to Sean. That is wrong. Sean has been involved with WAM and ADM since the project began, over a year ago, and became involved again earlier this year when the portfolio was assigned to Darryl. He holds the concept and the structure; what he lacks is the detail of the last several months. The original statement is left in place to preserve the decision trail.

What it changes about this brief: a deck written as a first introduction is pitched at the wrong person. The content is the delta since roughly the spring, and the program vocabulary (DDP, EUDM, WMX, VAS, P360, ADM, Strev, complex builds) can be used without definition.

**The storyline is also affected by scope.** Sean's 2026-09-09 message introduces a third and larger decision, whether Digital Products takes ADM development over from the current arrangement, which subsumes the two decisions this brief was built around. The disposition of the nine slides is recorded in `Deliverables/WAM/2026-09-09_WAM_ADM_Feasibility_Evidence_Pack.md` under "Relationship to the 2026-09-02 deck brief". In summary: slides 1 to 5 hold and slide 5 moves earlier, slides 6 and 7 demote to backup, slide 8 comes out of this meeting, slide 9 is rebuilt, and two new pages are added for the ownership boundary and the go or no-go. Re-sequence rather than rebuild.

**Note on the export copy.** `Pandoc/processed/2026-09-02_Sean_Deck_Brief-20260902-110019.md` carries the same uncorrected sentence. It is a generated export rather than a source of record and has been left as it stands; regenerate it from this file if it is used again.
