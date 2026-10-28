# Register B (Other-Owned) and Pulse Reconciliation Worklist

Prepared 2026-10-28, on Darryl's question: how did most Register B items originate, and would today's lane model route them to the Pulse instead. Darryl disposes each line; nothing here is applied automatically. Same three tests as the 2026-10-27 Watch worklist: (1) Darryl's own commitment, stays on the register (Register A); (2) already escalated on a real test (asked / boundary / stuck / gap), or tied to a Decision or Register A trigger, stays as a pointer with detail in the Pulse; (3) team-level with no escalation basis, retire and move the substance to the Pulse.

**Scope and method.** All 110 `Registers/action/B*.md` files read directly (frontmatter + body), not sampled. 44 are `open`; 36 `aged_out`; 23 `closed`; 7 `dropped`. This worklist covers only the 44 open ones — the rest already left the register. Origin was read from each file's own body text and `due_note`, not inferred.

**Note on scope: "B" is Register C too.** Since 2026-08-06, Register B and C were merged into one Other-Owned list (`Type: Delegated` or `Awaited`); every item in this folder, B1-B110, is that merged list. There is no separate C register left to check.

## Headline answer

Most open Register B items (roughly 30 of the 44) are the same thing B108-B110 were on the morning of 2026-10-16, before the lane model existed: a named team member's own quoted commitment ("I will...", "Let me...") captured from a recurring internal meeting or an M365 evidence sweep, Attribution tagged Explicit or Inferred, with no Darryl commitment and no stated escalation. B108-B110 were dropped into Pulse P001-P003 that same morning because they were created after the cutover. Everything older just stayed, because the 2026-10-16 lane model and the 2026-10-19/10-27 re-sorts only moved items that were still **Critical-tagged** or that **literally named a tracked forum** in the file text. Most of this register predates 2026-10-13, when forum-by-forum evidence tracking began, so the body text was never written with a forum name in it even though the underlying evidence (a Daily Scrum, ADM connect with Natalie, WAM Product discussion, Quest Migration Weekly Check-In, or an unlabelled "weekly evidence" sweep) is the same kind of team-governed content the Pulse now exists to hold. That is the gap between CLAUDE.md's count ("2 Other-Owned" items re-sorted, `08`) and what a full read finds: the 2-item count is accurate for what matched on a literal forum name; the real population of lane-model candidates is several times that.

**Yes — if raised today, most of the open list would be a Pulse issue, not a register item.** A smaller set should not move: two are Darryl's own prior delegation decisions (`B85`, `B86`), one is a commercial approval that is Darryl's own decision in substance (`B102`), three are a personal/staffing 1:1 check-in that was never forum content (`B103`-`B105`), and a handful are already escalated in substance (tied to a Decision, a Watch row, or the `A29` trigger) and should become pointers, not retirements.

**Structural gap underneath this.** Watch and Pulse items carry a `links` field; Register A/B/C action items do not (confirmed on `B107`, which Pulse issue `P021` already lists as a link on *its own* side — `P021.links` includes `B107`, but nothing on `B107.md` points back). So even where a link already exists, it is currently one-directional and invisible from the register item itself. Closing that gap, so a register item can show its own Pulse link the way a Watch pointer does, is a schema change (`Tools/eos_registers.py` field list for `kind: action`), not a disposition decision — call it out separately if you want it done before running this list.

## Priority cluster: same defect, four register items, inconsistent linking

`B20` (Natalie Marquardt), `B49` (Priyambada Dash), `B106` (Natalie Marquardt) and `B107` (Akansh Gangil) are four separate Other-Owned items for what the bodies themselves say is one root issue: vendor/manufacturer part-number truncation in DDP/eUDM feeding WAM. `B107` is already linked from the Pulse side (`P021.links` includes `B107`); `B20`, `B49`, and `B106` are not linked anywhere. Recommend resolving these four together against `P021` (and check `P022`, the EDM source-data gap, for overlap) before working the rest of the list line by line, since any of them disposed separately risks re-raising the same issue a second time.

## Full list, 44 open items

| Item | Owner | Origin (date, evidence) | Forum / account | Pulse cross-ref | Proposed | Needs Darryl |
|---|---|---|---|---|---|---|
| B1 | David Blondel / Akansh Gangil | 08-17, weekly evidence | ADM connect with Natalie (confirmed forum) | - | Already queued in the 2026-10-27 worklist for the 11-02 read-back: move commitment to Pulse, close here | no, already decided |
| B2 | Akansh Gangil | Not recorded | Unknown; body empty | - | No evidence in the file to classify; confirm at the weekly closure check rather than reconcile here | yes |
| B3 | Akansh Gangil | Not recorded | Unknown; body empty | - | Same as B2 | yes |
| B4 | Chad Steger / Chris Askew | 09-15 to 10-16, M365/vendor email (Ascent) | Not a governed forum; account email thread | - | Not lane-model content; leave on register, the file's own standing question ("Has Chad sent Ascent the checklist?") is a closure-check candidate | yes (one line) |
| B10 | Akansh Gangil | 10-19, Digital Products Portfolio deck | Not a forum; status deck | - | Already "Potentially closed, confirm" since 10-19, 9 days unanswered — resolve that first; if reopened, team-level, retire to Pulse | yes |
| B12 | Akansh Gangil | 10-19, same deck | "DDP Entrance Call (weekly)" — not in `_forums.json` | - | Same as B10; if DDP Entrance Call is a real recurring team meeting, add it to `_forums.json` going forward | yes |
| B18 | Scott Dunn | Pre-10-15, thin stub ("08-03") | Unknown | - | Stale, no activity since migration; confirm-close or drop rather than reconcile | yes |
| B20 | Natalie Marquardt | 08-12, weekly evidence | ADM connect with Natalie (confirmed forum) | Same issue as B49/B106/B107 — see priority cluster | Resolve as part of the four-item cluster against P021 | yes |
| B21 | Nathan Kehr / Sarah Monteleone / Scott Dunn | Pre-10-15, thin stub, dependent on B18 | Unknown | - | Resolve together with B18 | yes |
| B24 | Ron Snyder / Babu Papanna / Adam Slingerland | 09-01, weekly evidence | Likely deployment-scrum/FRB evidence; due_note says "Darryl / Ron weekly 1:1" | Body says "Escalated in `04`" | Check whether a Watch row already exists for the FRB release block; if so, pointer (test 2); if not, confirm whether the 1:1 makes this Darryl's own item | yes |
| B25 | Sarah Monteleone / Lindsay Cotten | Pre-10-15, thin stub | FRB SASTEC pilot follow-up; forum not named | - | Team-level, thin on detail; confirm still live before moving | yes |
| B31 | Syed Zaidi | Pre-10-15, thin stub | Unknown | Body says "Escalated LAD row in `04`" | Likely already a Watch pointer; confirm the cross-link exists and close here if so | yes |
| B32 | Marjan Fathima / Valli Poornakumar; Adam Slingerland / Pradyumna Umarji | 08-04, thin stub | LAD snag-list review; forum not named | - | Team-level, old; confirm still relevant, then retire to Pulse | yes |
| B42 | Darryl Benson | 08-17, superseded | n/a — owner is Darryl himself | - | Says it was promoted to `A28`; "Potentially closed, confirm" since 10-19, 9 days unanswered. Pure closure-check, not a lane question | yes |
| B49 | Priyambada Dash | 08-19, email (Anixter P360 CORE) | Not a forum; parallel to B20 | Same issue as B20/B106/B107 | Resolve as part of the four-item cluster | yes |
| B53 | Akansh Gangil | 09-01, weekly evidence | DDP/UDM escalation email | Feeds `A29` trigger directly | Already has its own escalation mechanism (A29); leave as the A29 trigger-watcher, not a plain retirement | yes (confirm) |
| B58 | Ron Snyder | Pre-10-15, thin stub | Gates AI Tech Review; tied to Decision Radar (`03`) | - | Decision-linked; pointer candidate (test 2) | yes |
| B60 | Chad Steger | 08-27, email follow-up list, Inferred | Ford Re-Alignment; forum not named | - | Team-level, stale since migration; confirm still relevant, then retire to Pulse | yes |
| B61 | Chad Steger | 08-27, Inferred | Ford Re-Alignment; forum not named | - | Same as B60 | yes |
| B62 | Chad Steger / Tim Scott | 08-27, Inferred | Ford platform-trust audit; tied to `04` Ford watch row | - | Decision-adjacent; confirm whether the Ford watch row already covers it (test 2) before retiring | yes |
| B72 | David Blondel | 09-09, "Potentially closed, confirm" since 10-19 | Release communication; forum not named | - | 10-19 evidence already shows the release went out; close now rather than wait for a lane answer | yes |
| B73 | Brad Stevens / Nathan Kehr | 09-09, thin stub | Managed-services operating model; tied to Decision Backlog (`03`) | - | Decision-linked; pointer candidate (test 2) | yes |
| B74 | Ankit Chadha | 09-09, advanced 10-05 weekly evidence | IDP/WAM capacity; tied to a Watch Active row (`04`) | - | Already tied to a Watch row; confirm pointer treatment (test 2) | yes |
| B82 | Babu Papanna | 09-16, "Potentially closed, confirm" since 10-19 | Quest dev-01 closure | - | 10-19 evidence already shows the migration done; close now | yes |
| B85 | Nathan Kehr | 09-18, moved from Register A (A7) by Darryl's own disposal-sweep decision | n/a | - | Not forum intake — Darryl's own prior decision to delegate. Leave as-is unless he wants to revisit | no (exclude) |
| B86 | Ron Snyder | 09-18, moved from Register A (A32) by Darryl's own disposal-sweep decision | n/a | - | Same as B85 | no (exclude) |
| B88 | Akansh Gangil | 09-28, weekly evidence, Explicit | WAM/complex-build resourcing | - | Team-level; retire to Pulse (test 3), check against existing WAM Pulse issues first | yes |
| B89 | Adam Lazare + platform leads | 09-28, weekly evidence, Implied | Dell EMS / Executive FM Summit content | - | Team-level; retire to Pulse | yes |
| B90 | Akansh Gangil | 10-01, M365 evidence, Explicit | Complex-build data model | - | Team-level, stalled since a 09-30 "next week" target; retire to Pulse | yes |
| B91 | Sridhar Loke + product owners | 10-01, weekly evidence, upgraded to Explicit 10-05 | Digital Products leadership deck access | - | Team-level (Darryl's own review of the same deck was deliberately kept as a separate Implied item, never on Register A); retire this one to Pulse | yes |
| B92 | Akansh Gangil | 10-01, M365 evidence | Complex-build cross-SBU data points | - | Darryl is quoted directly here ("Make sure you share data points...") but to Akansh, not as his own commitment; team-level, retire to Pulse | yes |
| B93 | Babu Papanna | 10-01, weekly evidence, Explicit | Quest Migration / production MQTT path | Quest Migration Weekly Check-In is a confirmed forum | Retire to Pulse (test 3) | yes |
| B96 | Chad Steger | 10-07, daily evidence, Explicit | Ford audit scheduling; tied to Decision Backlog (`03`) | - | Decision-linked; pointer candidate (test 2) | yes |
| B97 | Jacob Nicosia | 10-13, weekly evidence, Explicit | Ford/Wesco working team, password/SharePoint handoff | - | Team-level; retire to Pulse | yes |
| B98 | Violet Moyer | 10-13, weekly evidence (transcript, 10-08) | WAM Product discussion (confirmed forum) | - | Already queued in the 2026-10-27 worklist for the 11-02 read-back | no, already decided |
| B99 | Akansh Gangil | 10-13, weekly evidence, Explicit | WAM team quick-turn ask | - | Team-level; retire to Pulse | yes |
| B100 | Akansh Gangil | 10-13, weekly evidence; heavily worked since | WAM Leadership Sync; tied to `A61`, the Sean McCloskey deck, and Darryl's own confirmation asks | - | Already escalated in substance; pointer, not retirement (test 2). Note: the file's last line is a cut-off Darryl web entry ("Confirm deck is updated -\> Darryl B-"), worth your own look regardless of the lane question | yes |
| B101 | Valli Poornakumar | 10-13, weekly evidence, Explicit | Owed to Darryl, Babu Papanna and Chad Steger jointly | - | Joint ownership including Darryl — does that satisfy the attribution test for Register A, or is it still Other-Owned? Needs your call, not a mechanical one | yes |
| B102 | Akansh Gangil | 10-13 through 10-22, email + invoice thread | Strev SOW3 invoice ($14,226, Milestone 3) | - | The substance is Darryl's own approval decision (hold or release the invoice), not a team commitment from a forum. Candidate to re-home to Register A rather than retire to Pulse | yes |
| B103 | Ankit Chadha | 10-13, "Quick check in" transcript | Not a governed forum; 1:1-style check-in | - | Staffing/personnel content (Ron tickets), not delivery/development issue content. Recommend your own call rather than mechanical Pulse routing | yes |
| B104 | Ankit Chadha | 10-13, same transcript | Same | - | Staffing content (India-office work arrangement); same recommendation as B103 | yes |
| B105 | Naveen Kumar / Ankit Chadha | 10-13, same transcript | Same | - | Coverage assignment; same recommendation as B103 | yes |
| B106 | Natalie Marquardt | 10-13/14, email (global attributes) | Same issue as B20/B49/B107 | Same issue as B20/B49/B107 | Resolve as part of the four-item cluster | yes |
| B107 | Akansh Gangil | 10-13/14, email (full mfr part number enhancement) | Same issue as B20/B49/B106 | Already linked from `P021` (one-directional) | Resolve as part of the four-item cluster; add the missing reverse link once the schema supports it | yes |

## Recommended next step

Given the volume, suggest working this in three passes rather than one: (1) the four-item part-number cluster against P021/P022, since it is the one place today's register is at risk of duplicate tracking; (2) the five already-stale "potentially closed, confirm" items (B10, B12, B42, B72, B82), which are a closure-check backlog independent of the lane question; (3) the remaining ~25 team-level items, which can be swept to the Pulse in a batch once you have confirmed the three exclusions (B85, B86, B102) and the three staffing items (B103-B105) should stay off it.

## Reconciliation executed, 2026-10-28

Darryl closed the priority cluster and the five stale confirm-close items himself via the EOS web app before this ran: `B20`, `B49`, `B106`, `B107` (vendor part-number cluster, now tracked on Watch `W016` and Pulse `P021`/`P060`/`A29`) and `B10`, `B12`, `B42`, `B72`, `B82` (stale confirm-closes). Darryl: "I believe it would have been a Pulse type issue had we been built this way."

With his go-ahead, Claude then ran the rest of this list:

**Dropped as redundant with an existing Watch or Decision item** (no information lost; nothing new to move): `B24` (-> `W021`), `B31` (-> `W019`), `B58` (-> `D010`), `B62` (-> `W008`/`D045`), `B73` (-> `W023`), `B74` (-> `W022`), `B96` (-> `D045`).

**Dropped and moved to new Pulse issues** (test 3, team-level, no escalation basis): `B88` -> `P095`, `B89` -> `P096`, `B90` -> `P097`, `B91` -> `P098`, `B92` -> `P099`, `B93` -> `P100`, `B97` -> `P101`, `B99` -> `P102`.

**Left untouched, not part of this reconciliation:**
- `B1`, `B98` — already queued in the 2026-10-27 worklist for the Monday 11-02 Pulse Review read-back; left on that schedule rather than pulled forward.
- `B85`, `B86` — your own 09-18 disposal-sweep delegation decisions, not forum intake.
- `B53` — feeds the `A29` trigger directly; a live mechanism, not a plain register item.
- `B100` — already escalated in substance (`A61`, the Sean McCloskey deck); stays as-is. Note its last line is a cut-off web entry ("Confirm deck is updated -\> Darryl B-") worth your own look.
- `B101` — owed to you jointly with Babu Papanna and Chad Steger; whether joint ownership meets the attribution test for Register A is your call, not a mechanical one.
- `B102` — the Strev SOW3 invoice approval is your own decision in substance; recommend moving it to Register A rather than retiring it, but that is a Register A change and needs your explicit yes.
- `B103`, `B104`, `B105` — sourced from a 1:1 check-in, not a governed forum; staffing content. Recommend your own call.
- `B2`, `B3`, `B18`, `B21`, `B25`, `B32`, `B60`, `B61` — too thin or stale to safely classify (several have empty or near-empty bodies). Recommend the ordinary weekly closure check ("still open?") rather than a lane-model disposition, since there isn't enough evidence to retire them responsibly.

Register A open count after this run: 10 of 15 (room for `B102` if you approve the move). `Tools/eos_registers.py` regenerated: action 269, watch 99, decision 98, pulse live 81 / quiet 20 / resolved 1 / knowledge 3.
