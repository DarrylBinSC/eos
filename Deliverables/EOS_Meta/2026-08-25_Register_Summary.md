# Open Items Across All Registers

**As of 2026-08-25**, after the closure checks, the aging sweep and the weekly processing. Source of truth remains `03`, `04`, `05` and `07`; this is a cross-register read, not a replacement.

## 1. Where everything stands

| Register | Open | Cap | State |
|---|---|---|---|
| `05` Register A — Mine | **16** | 15 | One over. Down from 39 in July and 22 this morning |
| `05` Other-Owned | **72** | — | 36 Critical, 36 non-Critical. Was 86 before the sweep |
| `04` Watch List, Active | **20** | 20 | At cap. **19 of 20 are High** |
| `04` Watch List, Passive | 40 | — | Logged only, no action |
| `03` Decision Radar | **26** | 20 | Six over |
| `03` Decision Backlog | 30 | — | Unforumed, reviewed monthly |
| `03` Decisions being avoided | 1 | — | WAM/DDP/EUDM data-model alignment, 30+ days |
| `07` Register D — Standing | 3 | — | No completion state by design |

**Total open items carrying an expectation of movement: 141.** Of those, 16 are yours to act on.

## 2. Register A — yours, 16 items

**Overdue: 11 of 16.** Only A22 carries a future date.

| # | Item | Due | Whose date |
|---|---|---|---|
| A3 | FY27 financial goals, capacity model, capabilities | 08-03 | **Yours** |
| A5 | AOP alignment meeting, Brad Stevens and Gregg O'Brien | 08-07 | **Yours** |
| A25 | AOP workshop, three named inputs | 08-14 | **Yours** (stated) |
| A4 | CSS product ideas and AI-researched needs analysis | 08-05 | Proposed |
| A9 | CMP tool residence and Connected Safety adoption | 08-05 | Proposed |
| A15 | First-pass 2027 scenario analysis | 08-05 | Proposed |
| A16 | Colliers legacy support model, name the owner | 08-06 | Proposed |
| A23 | Leading Managers baseline assessment | 08-07 | Proposed |
| A27 | **i3 Alliance, send the Section 8 edits and rationale to Legal** | 08-07 | Proposed |
| A24 | SPA Engine, confirm what it is and whether it belongs | 08-20 | Proposed |
| A28 | AD groups for the Claude Code rollout | 08-24 | Proposed |
| A22 | CDA AOP submission package | 08-31 | Stated, under challenge |
| A1 | WMX complex-build follow-up | **No date at all** | — |
| A29 | Escalate the truncated part number dependency | Trigger: B53 returns no owner | **Yours** |
| A6 | JCI API connection through the Architecture Review Board | Trigger: C8 received | — |
| A7 | Priya Agarwal to Nathan Kehr introduction | Trigger: next Nate 1:1 | — |

**A27 is the one that blocks other people.** Two Critical Other-Owned items, C-i3-1 and C-i3-2, are both waiting on Legal receiving your Section 8 edits. Eighteen days.

**A1 still has no date**, which breaches the dating rule outright. Under the trigger backstop, getting Akansh's date is itself the action.

## 3. Other-Owned — 72 items, and the tag is now the problem

**Exactly half are tagged Critical, and that is why the register does not shrink.** Critical items are exempt from the aging rule and require your explicit confirmation to close. At least twelve of them are already past their gate and cannot age out:

| # | Item | Owner | Gate, passed |
|---|---|---|---|
| C8 | JCI technical data for the WAB submission | Jeff McCorvey | **07-30** |
| C11 | Correct the controller-capacity diagnosis | Scott Dunn | 07-29 |
| C12 | TCCC/AOC correlation data, scoped hardware question | Scott Dunn | 07-29 |
| C13 | Matt Shepherd TCCC meeting outcome | Sarah Monteleone | 07-29 |
| C1 | **JCI final legal markup sent to JCI** | Brian Miller | **07-31, stalled** |
| C2 | One-page MVP1 gate view | Akansh Gangil | before 08-03 |
| C4 | Backup distribution list for failed notification routing | Natalie Marquardt | before 08-03 |
| C-i3-1 | Legal's response to the Section 8 redline | Brandon Thompson | ~08-07 |
| C-i3-2 | Review of §8.10 and the §6.2 clause | Nikos Minas | ~08-07 |
| C16 | Documented basis for FY27 financial assumptions | Tom Boss | ~08-07 |
| B39 | Recipient list and sample notification for Natalie | Akansh Gangil | 08-10 |
| B34 | AOP workshop follow-through | Chris Gazdic | 08-14 |

**This is the finding worth acting on.** The 08-06 redesign traded automatic roll-off for low-stakes items against strict discipline on things that matter. In practice half the register got marked as mattering, so half of it can never leave without you personally closing it, which is the friction the redesign was built to remove. The tag is being applied to mean *important* rather than *expensive to be wrong about*. A re-audit that moved it back toward ten or fifteen items would let the rule do its job.

**Clustered by where the pressure actually is:**

- **JCI, 5 items** (C1, C8, C10, C14, plus your A6). All stalled, the oldest past due 26 days, on an eight-month negotiation where Wesco has hosted the Conductor in Azure without a contract since 07-17.
- **TCCC, 6 items** (C11, C12, C13, B18, B50, B51). Two land this week: PaaS-03W/04W validation on 08-27 and the maintenance-window email owed 08-25 or 08-26.
- **i3, 2 items**, both gated behind your A27.
- **Dell, 5 items** (B15, B37, B43, B54, B55). The SOC 2 response comes to you for review before it goes out.
- **WAM/ADM upstream data, 3 items** (B53, C32, plus B20 non-Critical). The live theme.
- **entroCIM AI, 4 items** (B58, C30, C31, C36). C36 is Sean's sponsor approval, confirmed today.

**Immediate, this week:** B51 (TCCC customer email, today or tomorrow), B50 and B52 (TCCC validation and Disney training users, both 08-27), B53 (Akansh's part number email, which fires or clears your A29).

## 4. Watch List — 20 Active, and the scale has stopped working

**19 of 20 are High.** One Medium, the new Dell SOC 2 row. A severity scale with effectively one value on it cannot rank anything, and the Analytics Standard names risk inflation as a failure mode in its own right.

Rising this week: Dell alarm reliability (new), WAM/ADM data integrity, ServiceNow Field Service, Louvre closeout, TCCC/AOC connectivity, entroCIM commercial performance, sales orders missing from EUDM/DDP.

Recommend a severity re-grade as a block at the monthly pass rather than row by row. The question to apply is not "is this serious" but "what would I drop everything for," and the answer cannot be nineteen things.

## 5. Decision Radar — 26, six over cap

Clusters rather than a list, since the themes are what matter:

- **FY27 and financial, 6** — entroCIM plan negative across the authorised range, WAM investment re-based, portfolio structure, assignee scope, financial assumptions with no approved budget, 2027 resourcing and headcount.
- **AI, 5** — entroCIM AI approval path (returned to the Radar today), AI roadmap direction, GitHub Copilot blocked on Vibe Guard, WAB approval for Claude code, the two-tier product ownership model.
- **WAM, 5** — MVP1 production gate, licence roadmap alignment, data-challenge remediation, operational hardening sequencing, renewal-notification attribution.
- **Portfolio ownership, 3** — CMP residence, Connected Safety adoption, support-model realignment. All three have been open since mid-July.
- **Operational, 7** — JCI to signature, release governance, Dell service management, Mapbox, AMI connector, new product concept, AI-enabled development pilot.

**Stalled, one item, and it is the important one:** WAM/DDP/EUDM data-model alignment, 30+ days of repeated discussion with no decision. It is the same root as the truncated part numbers, the catalogue leaf nodes and DDPTRK-6346. Four symptoms, one absent decision.

## 6. What the shape says

**The system is now accurate and still overloaded.** Register A halved today and is one item off its cap. The registers are no longer overstating what is yours, which was the 07-27 problem, and they are no longer failing to dispose, which was the 08-19 problem. What remains is genuine volume.

**Three things would move the most.**

First, re-audit the Critical tag on Other-Owned. Half the register is exempt from the only mechanism that clears it, and roughly a third of those exempt items are already past their gate.

Second, A27. It is eight days old on a proposed date, it blocks two other people, and it is the last step on the i3 work already logged as risk avoided in the Impact Ledger. That win is not banked until Legal has the text.

Third, force the upstream data decision. It appears once as a stalled decision, once as an Active risk, three times as Other-Owned items and once as a recurring theme. **Six register entries, one missing owner.** Thursday's Senthil meeting is the venue.
