# Decision Log

> Maintained by Claude during briefings. Three sections: decisions made, decisions approaching, decisions being avoided. Newest first. Seeded 2026-07-13 from 30-day baseline.
> **Restructured 2026-07-27** per `EOS_Redefinition_Proposal_2026-07-27.md` §4.9. Pre-restructure snapshot: `Archive/03_Decision_Log_pre-restructure_2026-07-27.md`.
> "Decisions Approaching" held 34 entries, which made it a backlog rather than a radar. Now split: **Decision Radar** (has a routing forum and a live date — surfaced weekly) and **Decision Backlog** (real but unforumed or undated — reviewed monthly, on demand, or when evidence shows it raised in a meeting). Four resolved or completed entries moved to Decisions Made.

> **Capped 2026-08-19** at Darryl's direction (`Deliverables/EOS_Meta/2026-08-19_EOS_Use_Case_Review.md`, recommendation 3). The Radar had regrown to 41 entries against the 24 it was set to on 07-27, which made it a backlog again. Rather than cut on priority, the Radar's own entry test was applied strictly, in two objective passes: (1) no named forum, or a forum recorded as unrouted/unnamed/unscheduled/unconfirmed, moved to Backlog (14 entries); (2) forum date already passed with no decision recorded and no forward date, moved to Backlog (5 entries). Three FY27 AOP entries caught by pass 2 were kept on the Radar deliberately: AOP runs to a fixed 08-21 date, so the correct action there is to re-set the forum date, not to demote the item. **Result: Radar 41 to 25, Backlog 14 to 30. No content was cut; every moved entry carries a note saying why and returns to the Radar as soon as a forum and date exist.** Closing the remaining 5 to reach the 20 ceiling would require an arbitrary priority cut on entries that are legitimately routed, which was left for Darryl rather than made silently.

## Entry Format

```
### YYYY-MM-DD — [Decision title]
- Status: Made / Approaching / Avoided-Stalled
- Owner:
- Context:
- Options considered:
- Decision / Recommended path:
- Risk of waiting (if open):
- Forum where this should be decided:
- Follow-up:
```

## Decisions Made

### 2026-10-20 — Registers app: live refresh by polling a file fingerprint, not server push
- Status: Made (Darryl, 2026-10-20)
- Owner: Darryl
- Context: Items Claude filed during the 10-20 briefing session did not appear in an open tab until Darryl reloaded. The page fetched once on open and after its own writes; the server watcher saw outside edits within seconds but had no way to tell the browser.
- Options considered: refresh on tab focus only; poll a cheap fingerprint and re-fetch on change; server-sent events from the watcher.
- Decision / Recommended path: both of the first two. New `/api/version` returns a fingerprint of Registers/**/*.md and Briefings/*.md modification times; the page checks it every 30 seconds and on tab focus, re-fetches only when it changes, and never while a drawer, sheet or text field is active. Server-sent events declined: the single-process `http.server` makes long-lived connections more code and more failure modes than the problem warrants. Previous server archived at `Archive/2026-10-20_pre_live_refresh/`.
- Follow-up: guide updated (`Reference/Registers_App_User_Guide.md`, "When something looks wrong"). Darryl to confirm the "Updated from the files" toast appears on the next session edit.
- **Same morning, second fix:** C72 showed the gap the refresh cannot close. Darryl saved a form opened before a session edit; the form sent every field, so it wrote the stale Critical tag and next action back over the newer values. The item form now sends only the fields the user changed. The refresh is deliberately suppressed while a form is open, so this is the fix that matters for concurrent editing.

### 2026-10-20 — Daily Copilot prompt v2 (extraction only): adopted after the side-by-side run
- Status: Made (2026-10-20, Darryl)
- Owner: Darryl
- Context: Yield review of the four retained daily packages found each 23 to 41 KB package carried 4 to 8 sources restated across 5 to 10 of 14 sections, with the restatements being Copilot's own assessments that Claude redoes under `CLAUDE.md`. Copilot's output budget was going to commentary rather than retrieval. `Deliverables/EOS_Meta/2026-10-19_Daily_Prompt_Yield_Review.md`.
- Options considered: split the Daily prompt into two passes (doubles runs, keeps the duplication); drop low-yield sections 12 and 13 (marginal); remove the assessment layer from Copilot and keep judgment on the Claude side (chosen, one variable).
- Decision / Recommended path: Adopted. Side-by-side on the 10-19 to 10-20 window: v2 opened 14 sources to v1's 9, captured the Teams chats v1 missed (including Darryl's shift to supporting the Stanford roll-back), and carried every material v1 item but one quoted commitment (extraction miss, watch next run). v1 retired from `02`; Weekly prompt unchanged until after 10-26. Original path: v2 is live in `02_Copilot_Intake_Prompts.md` section 2 and served by the web app; v1 kept in 2a. Run v1 and v2 on the same window in separate Copilot chats, save both to `Evidence/`, and compare. Adopt v2 and retire 2a if it loses no source or distinct statement; otherwise revert section 2 to v1. Weekly prompt unchanged until this result is in.
- Risk of waiting (if open): n/a.
- Forum where this should be decided: decided in the 2026-10-20 briefing session.
- Follow-up: separate decision on a code-side package check in the EOS server (acceptance gate outside the prompt, per the 09-14 revision).


<!-- GENERATED 2026-10-19 16:46 from Registers/ by Tools/eos_registers.py. Do not hand-edit this section; edit the item files under Registers/ or use the EOS web app. Pre-migration history is preserved verbatim in Archive/2026-10-15_pre_registers/. -->

*Generated view of `Registers/decision/` (tier radar). Radar requires a named forum with a live date; ceiling 20, overflow to Backlog with the reason. Count at generation: 14.*

### 2026-10-16 — Operational Pulse: team-governed forums leave the registers (lane model)
- Status: Made
- Owner: Darryl Benson
- Context: Issues from the Deployment Daily Scrum, the entroCIM Daily Stand Up and eleven other team-governed forums were entering the registers as Darryl's items; six of 27 Watch Active items on 10-16 cited the Daily Scrum. Darryl: he does not track those, each team's governance does; he wants visibility and the ability to lean in, in the web app.
- Options considered: keep filtering by the 08-25 sprint-task rule; exclude the forums; route them to a separate lane.
- Decision / Recommended path: a lane, not an exclusion. Signals from the 13 confirmed team-governed forums go to `Registers/pulse/` and reach the registers only when Darryl escalates on one of four tests (asked, boundary, stuck, gap). Dell health score, pinned in the web app; two weekly governance tracks (delivery: Chad Steger and Syed Jamshed Zaidi; development: Ron Snyder and David Blondel), Darryl-owned. Same day: P001, P004 and K005 left with the team; K002 and K003 resolved on Darryl's notes.
- Risk of waiting (if open): n/a.
- Forum where this should be decided: decided in session, 2026-10-16.
- Follow-up: schedule the first delivery and development governance sessions (`07`, "Weekly, to be scheduled"); calibrate Dell health at the first weekly (2026-10-19). Recorded here 2026-10-19; it was in `CLAUDE.md` but had not reached this log.

### 2026-10-15 — EOS registers moved to one item per file; LAN web app adopted with the "Ledger" (1a) design
- Status: Made
- Owner: Darryl Benson
- Context: the registers (`03` Radar/Backlog, `04`, `05`) were going stale because updating them meant opening large files and dictating changes. Darryl's diagnosis: visibility and a cheap update path, not another structural redesign (the 08-19 finding that overgrowth is a disposal-throughput problem stands).
- Options considered: (A) parse and rewrite the existing markdown tables in place; (B) one item per file with front matter, registers become generated views; (C) a Claude artifact with its own database. A rejected for parser fragility and no per-item notes; C rejected because files must stay the source of truth and it offered no LAN access.
- Decision / Recommended path: B. Items live in `Registers/<kind>/<ID>.md`; `04`, `05` and the Radar/Backlog sections of `03` are generated; a Python web app on Darryl's Mac serves the registers on the home network, writes edits back to the item files, regenerates, and commits to git; new items from the app arrive flagged for triage; every brief reads Darryl's changes first. Same day, after a usability and design review in Claude Design, the "Ledger" direction (1a) was adopted and deployed: triage bands by urgency, one-tap status, status and notes first in the item panel, docked panel on desktop.
- Deferred: LAN password (`EOS_PASSWORD`); cap sweep on Watch Active (27/20) and Radar (33/20), which the app now makes visible on every open.
- Follow-up: `Deliverables/EOS_Meta/2026-10-15_EOS_Registers_Build_Spec.md`, `2026-10-15_Registers_Migration_Report.md`, `2026-10-15_Registers_App_Design_Review/`.

### 2026-10-15 — Miro export inbox; deck rebuilds use the connector read-back
- Status: Made
- Owner: Darryl Benson
- Context: Miro has no API to export a frame as an image (developer forum, staff answers 2021 to 2024, still open January 2026), so full automation is not possible. The 2026-10-15 export test showed Miro's default file name carries board and frame, which makes the export matchable to the document comment, and showed that frame shape decides legibility. Reviewing the deck flow, the connector read-back (verified the same day) gives exact positions, text and connectors for hand-built sketches.
- Decision: (1) Darryl's only step is exporting the frame into `Pandoc/miro_exports/` with Miro's default name; Claude matches, renames, files, renders and checks. (2) Frames are named for what they show and built export-ready: page-shaped for documents, 16:9 for slides. (3) Deck graphics are rebuilt natively from the connector read-back of the chosen option, not from memory or a screenshot. (4) Browser automation of Miro's export UI not adopted.
- Recorded in: `Reference/Communication_Preferences.md` §7; `Reference/Deck_Construction_Standards.md` §3; `Pandoc/README.md`; `Pandoc/miro_exports/README.md`.
- Follow-up: revisit if Miro adds an export API; consider moving the matching step into the watcher once the inbox has been used a few times. Read-back to native slide tested end to end the same day (`Deliverables/EOS_Meta/2026-10-15_Miro_Readback_Slide_Test.pptx`, script in `Deliverables/EOS_Meta/build_scripts/`): endpoint and render checks passed; the test also surfaced that a board goes stale once the deck is revised, now a rule in §7.
- Source: session with Darryl, 2026-10-15.

### 2026-10-15 — Flowcharts use Miro's synced Mermaid widget; one code, two homes
- Status: Made
- Owner: Darryl Benson
- Context: Miro updated its Mermaid capability (Beta): a Mermaid flowchart becomes native, editable Miro shapes that stay in sync with the code both ways, and the connector can create the widget from code and read the current code back. Tested the same day on private board "Mermaid Sync Test 2026-10-15": (1) code written by Claude created the widget, and read-back matched exactly; (2) version 1 rendered correctly through the Word pipeline; (3) Darryl made visual edits (layout direction, spacing, a new node and connector, group colors) and every edit came back as code; (4) version 2 rendered through the Word pipeline with all edits, but Narrow spacing made group titles collide with boxes. Evidence: `Deliverables/EOS_Meta/2026-10-15_Mermaid_Sync_Test.md`, the two .docx renders and `2026-10-15_Mermaid_Sync_Test_diagrams/`.
- Options considered: keep the earlier promote-and-supersede rule for all diagrams; adopt the synced widget for flowcharts only; adopt it for all Mermaid types.
- Decision: For flowcharts, the Mermaid code is the source of truth in two homes, the EOS .md and the Miro widget. Darryl edits visually in Miro; Claude reads the code back before any change or send, and the board's code wins when it changed. No free-form switch, no PNG export, Regular or Wide spacing for anything headed to Word, Wesco colors restored in code for material leaving the team. Sequence, class and ER stay code-only until tested; hand-built boards keep the earlier rules.
- Supersedes in part: the "promote; never maintain both" rule from the earlier 2026-10-15 entry, for flowcharts only.
- Recorded in: `Reference/Communication_Preferences.md` §7; note in `Reference/Mermaid_Standards.md`; `Reference/Diagram_Register.md`.
- Follow-up: Miro labels the feature Beta; recheck behavior if the read-back ever differs from what is on the board. First real use is the next process or architecture flowchart.
- Source: session with Darryl and live test, 2026-10-15.

### 2026-10-15 — Miro and Mermaid integration: destination decides the tool, one declared source of truth, Word embedding convention
- Status: Made
- Owner: Darryl Benson
- Context: The 2026-10-07 tooling decision chose the tool by use case but did not say how the two work together. Gaps found in session: no convention for getting a Miro diagram into a Pandoc-built document; no EOS record of which Miro boards are live sources of truth (Miro is invisible to grep, to other LLMs and to sessions without the connector); no rule for moving a diagram between tools, which invites parallel copies that drift; the personal-account placeholder rule did not cover internal alignment ratings, which the stakeholder board holds; and image paths in the Word pipeline resolve from `Pandoc/`, not from the .md, with an unresolved path dropping the image and logging only a warning (verified in a test conversion 2026-10-15).
- Options considered: status quo (2026-10-07 rules only); Mermaid as the permanent source with Miro as a rendering surface only; destination-based choice with a declared source of truth and a promotion rule.
- Decision: (1) Choose by destination: Mermaid for Markdown, the Word pipeline, frequently changing and LLM-maintained diagrams; Miro where layout is the message, for hand markup and side-by-side options. (2) One declared source of truth per diagram; every Miro board used for EOS work is listed in the new `Reference/Diagram_Register.md`. (3) Promote, never maintain both: §24 limits trigger Mermaid to Miro, and the Mermaid version is then marked superseded; Miro to Mermaid only when a diagram must live in an LLM-maintained file. (4) Miro into Word as PNG, white, 2x, saved as `<deliverable>_diagrams/<name>_YYYY-MM-DD.png`, paths relative to `Pandoc/`, caption div after each image. (5) Personal-account placeholder rule extended to internal alignment and influence ratings and anything Darryl marks private. (6) Transfer packages carry Mermaid source or PNG plus a two-line description. (7) Watcher change adding `--resource-path` for the EOS root: drafted for review, then adopted and tested by Darryl's direction the same day.
- Supersedes in part: nothing in the 2026-10-07 decision is reversed; this adds the integration layer and widens its data boundary.
- Recorded in: `Reference/Communication_Preferences.md` §7 and "Markdown for the Word pipeline"; precedence note in `Reference/Mermaid_Standards.md`; `Reference/Diagram_Register.md` (new); `Reference/README.md`; proposal at `Deliverables/EOS_Meta/2026-10-15_Pandoc_Watcher_Resource_Path_Proposal.md`.
- Follow-up: (a) Watcher proposal adopted and tested 2026-10-15; closed. (b) Board "Stakeholder Map 2026-10": Darryl, 2026-10-15, leave the alignment ratings as they are for now; kept by exception. Closed. (c) Board "CSS Digital Products – Technical Architecture": Darryl, 2026-10-15, an old draft to be removed; retired in the register. Closed. (d) The 27 other boards in the personal account predate this rule and are not registered; add any that become live.
- Source: session with Darryl, 2026-10-15.

### 2026-10-14 — Written Sean updates retired as a default; meeting frame and close-out pattern adopted
- Status: Made
- Owner: Darryl Benson
- Context: four fortnightly drafts (08-19 to 10-13) never sent; Sean told Darryl he does not want written updates; Darryl's 30-minute meetings get hijacked or run on different priorities. Darryl, 2026-10-14, agreed with the diagnosis and asked for all four changes.
- Decision: (1) a three-line Teams frame the morning of each meeting with the numbered asks; (2) the asks on the first content slide of the deck; (3) a three-line close-out the same evening recording decisions and next dates; (4) the fortnightly generated update retired as a default, produced only on request. Standard: `Reference/Sean_Update_Standard.md`, "Meeting frame and close-out." Template: `Deliverables/Exec_Briefs/2026-10-14_Sean_Meeting_Frame_and_Closeout.md`. `CLAUDE.md` section 19 annotated.
- Refined the same day: slide 2 is "Takeaways" (one per product) rather than an ask list; three carry something from Sean (Akash status on WAM development, CDA approval to proceed, Launch Studio approval to proceed). WAM right-sizing is informing. Renewal flag: Darryl takes it to Dan Totino directly.
- Proving artifact (per the "not executed until observable" rule): the close-out message filed after the week-of-10-19 meeting, with decisions written into `03` and `05` the same day.
- Source: Darryl, chat 2026-10-14.

### 2026-10-14 — Woolly AI launch targeted for Q1 2027, with entroCIM 4 (SkySpark 4)
- Status: Made (target, not a committed date)
- Owner: Darryl Benson
- Decision: Woolly AI launches in Q1 2027 alongside entroCIM 4, the release built on SkySpark 4. In outside material, call the release entroCIM 4 (Darryl: "Call SkySpark 4, entroCIM 4"). Launch scope as Darryl describes it: 30+ built-in skills, bring-your-own API keys, skills callable through the API without the chat interface.
- Context: Darryl described a beginning-of-year launch to Matt Powers on 2026-10-14 before Sean had been fully briefed; the Sean deck v4 now carries it (entroCIM AI and entroCIM roadmap slides). The rest of the 2027 roadmap is being reconciled to the new staffing level (`05` A64, end of October).
- **AI Council has approved Woolly (Darryl, 2026-10-14); Ron Snyder has started C2P.** The Anthropic API budget line is still open.
- Source: Darryl, chat 2026-10-14.

### 2026-10-12 — entroCIM deployment model: Wesco-Hosted positioned as the standard for client-facing material
- Status: Made
- Owner: Darryl Benson
- Context: Darryl reviewed the Europe team's "entroCIM Deployment Strategy: On-Premise or Wesco-Hosted Cloud" preliminary document (v0.1, 2026-10-09) and the "Client-Facing entroCIM Deployment Discussion Framework" email thread (3-message thread, 2026-10-12). Wesco has hosted entroCIM clients in Wesco Azure for years; on-premises has been described as an equal alternative in outbound material, which this decision ends.
- Decision: Wesco-Hosted is the standard entroCIM deployment position; on-premises is reserved for client policy or architecture requirements, not offered as a co-equal option. Platform operations (entroCIM team), product support (software service agreement, no SME hours, see the support-model change below) and Monitor/Optimize/Operate managed services are kept as separate, named scopes in client-facing material.
- Open points raised to the Europe team, not yet resolved: default write-back position, EU data residency/GDPR/NIS2 positions, certification scope for hosted entroCIM, and support coverage hours for European clients. See `03` Decision Backlog, new entry below.
- Follow-up: Valli Poornakumar revising the client-facing framework with Darryl's tracked-changes comments; call targeted late week of 2026-10-12 or early the following week.
- Source: Darryl, direct, 2026-10-12; `Products/entroCIM/entroCIM.md`.

### 2026-10-06 — Ford interim support model: continue through year-end, defer upgrade recommendations to the October system audit
- Status: Made
- Owner: Ford/Wesco working group (Adam Lazare, confirmed in discussion)
- Context: Wesco & Ford - entroCIM Platform/Program Touchpoint Call, 2026-10-07 transcript (complete, 331 lines).
- Decision: use interim Ford support through year-end; transition to the defined SLA scope in Q1 2027; defer any upgrade recommendations until the October system audit has run.
- Follow-up: Chad Steger coordinates audit resources once Tim Scott schedules the audit (`05` Other-Owned, new row). Jacob Nicosia sending Ford account credentials and setting up a shared SharePoint exchange area. Adam Lazare to communicate PO receipt to the team.
- Source: Wesco & Ford - entroCIM Platform/Program Touchpoint Call (transcript), 2026-10-07; M365 weekly evidence 2026-10-13.

### 2026-10-06 — Strev cost ownership boundary: recurring platform fees are a business budget item, IT-funded ADM/API work stays separate
- Status: Made
- Owner: Darryl Benson, with Amy Aguirre acknowledging the budget implication
- Context: Strev questions (transcript), 2026-10-06 (complete, 208 lines). Extends, rather than contradicts, the 2026-09-17 boundary ("this is Amy's problem to deal with, not mine") by drawing the specific cost line.
- Decision: Strev's recurring platform operating fees are a business (Amy Aguirre) budget responsibility. IT-funded ADM/API enhancement work stays a separate line and does not absorb platform operating cost.
- Follow-up: Darryl resolving Strev pricing, invoices, and revised contract language with Sunny Sharma/Christina, copying Amy Aguirre (`05` A49 thread). Amy Aguirre reconciling the QA hosting charge, see Decision Backlog, new entry below.
- Source: Strev questions (transcript), 2026-10-06; M365 weekly evidence 2026-10-13.

### 2026-10-06 — entroCIM customer training priced: $250 per learner, named course, 5-learner minimum, 20-learner maximum
- Status: Made
- Owner: Maggie Becker, discussed with product/deployment leadership
- Context: entroCIM Backlog Deep Dive (transcript), 2026-10-06 (complete, 1099 lines).
- Decision: formal entroCIM courses are priced by named course at $250 per learner, 5-learner minimum, 20-learner maximum. One private Foundations offering up to 20 learners may be credited for new deployments.
- Follow-up: "entroCIM Training Course Pricing Framework Overview & Next Steps" meeting, 2026-10-16, confirm calculator treatment, proposal language, cost/margin handling, rollout sequence.
- Source: entroCIM Backlog Deep Dive (transcript), 2026-10-06; M365 weekly evidence 2026-10-13.

### 2026-10-05 — WAM Zapier: no change; Wesco does not fund Strev's $25,000 SOW
- Status: Made
- Owner: Darryl Benson, with Chris Gazdic agreeing
- Context: **Filed late.** This decision was reached and recorded in `Products/WAM/WAM.md` (2026-10-05 entry, "Zapier and Azure hosting positions") the same day it was made, from the complete Zapier reassessment meeting transcript (Darryl, Chris Gazdic, David Blondel, Akansh Gangil). It was never entered here or closed out in `05` Register A, a propagation gap of exactly the kind flagged in CLAUDE.md's "mechanism is not executed until it has produced observable output" section. Closing the gap now, eight days late. This week's fresh M365 evidence independently lists "decide whether Wesco should own a Zapier capability" as still open (WAM Leadership Sync transcript, same day); read as Copilot's sample of the earlier part of the same meeting day, not a reopening. `Products/WAM/WAM.md` carries the fuller transcript and the concluding call.
- Decision: the Strev-run Zapier integration continues as-is. Wesco does not fund Strev's $25,000 SOW for a Wesco-branded/owned Zapier capability. No end customers are known to use it; users are internal. If the business wants it Wesco-branded, the business funds and contracts Strev directly. Azure migration of Strev hosting is also not pursued at this time (no functional difference for users; adds internal Azure/DevOps effort); hosting fees belong in Amy Aguirre's BIR for the Meta renewal.
- Follow-up: Darryl to tell Amy Aguirre the outcome, not confirmed done in any evidence reviewed; carried into `05` as a new dated item.
- Source: Zapier reassessment meeting transcript, 2026-10-05; `Products/WAM/WAM.md`.

### 2026-10-07 — Diagram and deck-graphics tooling: Miro for relationship diagrams and graphic sketching, native PowerPoint for what ships
- Status: Made
- Owner: Darryl Benson
- Context: First Miro build through the connector (board "Stakeholder Map 2026-10", private, Darryl's personal Miro account), judged by Darryl much better than the Mermaid version. Discussed in session whether Miro should also supply PowerPoint graphics. A Miro graphic reaches a deck only as an image: not editable on the slide, off-template, re-export for every change.
- Options considered: Mermaid only; Miro graphics exported into decks; Miro as sketchpad with native PowerPoint rebuild.
- Decision: (1) Relationship diagrams are built in Miro when the connector is available; Mermaid is the fallback and stays the standard inside Markdown and the Word pipeline. (2) Deck graphics: Miro is the sketchpad (two or three layout options side by side), Darryl picks and marks up, and the chosen option is rebuilt natively in PowerPoint on the Wesco template; a Miro image goes in a deck only as an appendix or reference diagram. (3) Sketch in Miro first when a graphic has more than about 8 elements, connectors crossing between groups, an open layout question, or alternatives are wanted; standard patterns go straight to PowerPoint (tiebreaker: describable in one sentence before building). (4) Personal Miro account for now, boards private, placeholders for customer names, financials and anything under NDA; Darryl also holds a Wesco Miro license if this moves.
- Supersedes in part: the tooling call recorded under 2026-08-27 Navigator / entroCIM integration sequence ("Mermaid for drafting only, native PowerPoint shapes for the deck"); Miro now takes the drafting role where available, native PowerPoint for the deck is unchanged.
- Recorded in: `Reference/Communication_Preferences.md` §7 (governing text), pointers in `Reference/Mermaid_Standards.md` and `Reference/Deck_Construction_Standards.md`.
- Follow-up: first real use on a deck graphic is the test; revisit the 8-element threshold if the double build proves too costly.

### 2026-10-06 — CDA not approved in the FY27 AOP; development continues from the entroCIM team, on the entroCIM roadmap
- Status: Made
- Owner: Sean McCloskey (AOP outcome); Darryl Benson (build, team placement)
- Context: FY27 AOP update from Sean to Darryl, 2026-10-06 (Darryl, direct). CDA had been submitted as an Invest product carrying $246,787 of 2027 development (6.25 India + 0.25 NA FTE for eight months). Bill Muczko accepted business sponsorship 2026-10-02. The 10-06 exec brief had put the choice to Sean as fund CDA as a project or fold the capability into the entroCIM roadmap; the AOP outcome is the second.
- Decision: CDA is not approved as a standalone FY27 investment. CDA functionality is built from the entroCIM team and carried on the entroCIM roadmap; "CDA development can continue." **CDA's own FY27 numbers drop to zero.** The CDA development headcount is lost or redeployed: Darryl and Ron Snyder balance headcount across entroCIM, and headcount still without a product after that may have to be let go (Darryl).
- What does not change (Darryl, 2026-10-06): "How CDA is positioned in the market is separate from how it'll be built." CDA stays a distinct product, in the EOS and in the market. The 2026-09-18 customer-facing rule (CDA stands alone and must not read as an entroCIM add-on) holds. Bill Muczko's sponsorship, the commercial model and the pricing work are unaffected; only the build home and funding changed.
- Effect on the record: the "CDA to the entroCIM team" option logged 2026-09-28 and marked moot 2026-10-01 has effectively happened, for a different reason (AOP outcome, not CLM staffing). The 2026-10-02 decision tying the business case to $246,787 stands as the historical basis of the model; that figure no longer represents funded development.
- Follow-up: summary walkthrough for Sean after his PTO, week of 2026-10-19; a summary only, not a top priority for him (`05` A59).
- **Update 2026-10-14 (Darryl, direct):** entroCIM capacity is reduced from 2026 to 2027 (confirmed fact; the 10-06 call is not its source). CDA next step: business review of the services with TS (formerly TSS).
- **Update 2026-10-14 (Darryl, direct):** Ron Snyder, David Blondel and Darryl are reconciling the 2027 core entroCIM roadmap with the intent to build CDA in 2027; complete by end of October 2026 (`05` A64). The entroCIM roadmap is absorbing CDA. Email to Emily Munk due 2026-10-07 (`05` A56). Headcount balancing with Ron (`05` A57). `04` CDA commercial viability and entroCIM capacity rows updated.
- Source: Darryl, direct, chat 2026-10-06 (Sean's AOP update and Darryl's answers the same day).

### 2026-10-14 — Launch Studio: the onboarding review is a new body; existing approvals unchanged
- Status: Made
- Owner: Darryl Benson
- Decision: the inlet filter is an onboarding review, a new body made up of Launch Studio people as part of their work (David Blondel, Mike Wassil, an architect from Ron Snyder's team; Darryl and Ron at commit) with executive decision-makers such as Sean McCloskey and Lisa Orton where needed. It vets submissions that come with their business's endorsement and a payback. AI Council and intake, Security and WAB, Finance and the business sponsor still approve. Corrects the 10-13 "no new approval body" wording.
- Open: whether the executives are standing members or called in per decision.
- Source: Darryl, chat 2026-10-14. Deck v17; `Products/Vibe_Code_Productization/Vibe_Code_Productization.md`.

### 2026-10-13 — Position on Mike Wassil's Launch Studio proposal

- Decision-maker: Darryl (direct, session 2026-10-13, accepting Claude's review recommendations in full).
- Context: Mike's 2026-10-12 deck and report propose a six-step program (Find, Prove, Commit, Build, Pilot, Scale) with four gates owned by existing bodies, risk tiers T0 to T3, a build-route choice (reuse, extend, buy, harden, rebuild), a value contract and five-line benefit ledger with a Finance reviewer, and a roadmap to Q4 2027. Two elements move away from Sean's 10-06 ask and Darryl's 10-07 operating model: decision rights (Launch Studio "prepares evidence, does not decide"; Darryl and Ron never accountable in the RACI) and funding (suggested option 2, central discovery money, sponsor pays delivery).
- Decision: **Adopt** the scaffolding: tiers, build routes with common release tests, value contract and ledger, funnel reporting to the AI Council, the existing-approvals mapping, and the vocabulary (AI Builders Guild, AI-assisted building). **Line one, funding, revised by Darryl 2026-10-13 after the meeting with Mike and Ron:** the funding mechanism is a future decision. The shape to present to Sean: IT funds the standing team; each product is a business-funded project that reimburses the IT budget for productization and then for upkeep. Offer the business a menu (sandbox, pilot, sponsored product, shared product) so the decision is easy to make. Principle that holds now: no sponsor, no production. Open: whether "IT" base funding means Sean's digital products budget or corporate IT. **Hold line two, capacity:** Launch Studio decides what it takes into build against a work-in-progress limit Ron sets; the business decides what it funds; existing bodies decide what is approved. **Route to Sean (corrected by Darryl, 2026-10-13):** Darryl is the route to Sean; Launch Studio is a joint initiative with Mike. Darryl presents and owns the ask, Mike co-authors, week of 2026-10-19, pilot scope cut to Q4 2026 and Q1 2027. ~~Ask Mike for the recommendations brief~~ dropped by Darryl: the deck and report already carry the substance.
- Darryl's framing (2026-10-13): "I want to hold the strategy here, so let's adopt the best of what Mike and his research produced." He does not expect much alignment to be needed.
- Status: Darryl's position after a 2026-10-13 meeting with Mike and Ron. The 10-12 and 10-13 meeting outcomes are confirmed by Darryl as agreed in substance but are not yet recorded in detail; the 10-13 transcript file captured only the first 90 seconds before the Copilot facilitator took over.
- Corrections to our own record made the same day: CSA "5,600 apps" statistic was misattributed (vendor scan via VentureBeat, not a CSA scan); Gartner figures are a forecast from a secondary source. Detail in `Products/Vibe_Code_Productization/`.

### 2026-10-08 — Working name "Launch Studio"; IT carries governance for the vibe coders

- Decision-maker: Darryl (direct, session 2026-10-08).
- Decision: the vibe coding productization initiative goes forward under the working name **Launch Studio**, "to get the ball rolling," with feedback gathered over time. Positioning: the vibe coders are shielded from Wesco IT security and governance, which IT executes for them as part of the internal service ("if IT absorbs it, compliance goes up and friction goes down"). Governing principle carried with it: if IT touches an application, IT owns it (no business-owned middle tier).
- Status: working name, not final. Intranet check for existing "Studio" programs still to be done.
- Register `05` A60; detail in `Products/Vibe_Code_Productization/`.

### 2026-10-07 — Vibe coding productization operating model

- Decision-maker: Darryl (direct, session 2026-10-07).
- Decision: Mike Wassil is the conduit to the vibe coders (no ownership conflict). Darryl and Ron Snyder lead as a joint team. CSS team roles: David Blondel product owner; Ron's team developers and operators. Start with the current team; additional staffing addressed when needed.
- Effect: closes design questions on run ownership, team shape and the Mike boundary in `Products/Vibe_Code_Productization/`. Register `05` A60.

### 2026-10-06 — Two new product threads opened: Aris (paused) and vibe coding productization (exploration)
- Status: Made (opening the threads only; nothing about either product is decided)
- Owner: Darryl Benson
- Context: both came out of the brainstorm in Sean McCloskey's 2026-10-06 AOP update. Aris is a business process management platform currently under Prassada, moving to Sean. The vibe coding productization team was Sean's idea in the meeting.
- Decision: tracked as separate EOS threads, `Products/Aris/` and `Products/Vibe_Code_Productization/`. **Aris: paused until Darryl hears more.** **Vibe coding productization: Darryl's to stand up; status exploration; name still being ideated.**
- Source: Darryl, direct, chat 2026-10-06.

### 2026-10-05 — Pandoc reference template v3 and EOS filter adopted (`Pandoc/`)
- Status: Made
- Owner: Darryl Benson
- Context: Review found most Pandoc output styles (Body Text, First Paragraph, Compact, Block Text, Verbatim Char, Table) were undefined in the template, so content fell back to Nirmala UI 9 pt; footer printed a literal "DOCUMENT TITLE / Wesco" placeholder on every page after page 1; an unused 244 KB image was copied into every output.
- Decision: Applied review items A through E: Aptos throughout, 10.5 pt body (chosen over the 10 pt one-page compromise), 0.75 in margins, 1.1 line spacing, black bold heading scale (18/13/11 pt) with a rule under H2, all Pandoc styles defined, blockquotes as gray callouts, Plain Table 3 derived "Table" style with banded rows only, bold non-caps header, 9.5 pt cells, padding, rows kept together, and one footer on every page (current Heading 1 title left; "Wesco Confidential | Page X of Y" right).
- Effect: Typical output size drops from about 270 KB to about 27 KB. Previous versions retained as `Pandoc/SUPERSEDED_2026-10-05_Pandoc_Ref.docx` (original) and `..._interim.docx` (black headings and table style only). Before/after samples in `Pandoc/samples/`.
- Update, same day: F, G and H also applied (template v3). Named callouts (Bottom Line, Decision Required, Risk, Source Note); `Pandoc/filters/eos.lua` promotes the opening `#` heading to the document title, centers diagrams with caption-based alt text and sizes table columns to content; watcher adds native caption numbering and an opt-in table of contents (`toc: true`); inherited SharePoint, Grammarly and attached-template metadata and the legacy legal-numbering styles removed. Writing rules added to `Reference/Communication_Preferences.md`; pipeline documented in `Pandoc/README.md`. v2 retained as `Pandoc/SUPERSEDED_2026-10-05_Pandoc_Ref_v2.docx`, previous watcher as `Pandoc/SUPERSEDED_2026-10-05_pandoc-watch.command`.
- Wired into EOS authoring, same day: CLAUDE.md now requires the pipeline writing rules for every Pandoc-bound .md including briefings, sets a briefing callout rule (three per briefing at most: Decision Required, High-severity Risk; Source Note under Register Health; Bottom Line reserved for memos and Sean updates), and specifies the Register Health chart caption format. Caption rule added to `Reference/Mermaid_Standards.md`; restart note added to `00_README_Operating_Manual.md`.
- Open: the watcher must be restarted on Darryl's Mac to load the new script; until then, footers on new conversions show a field error in place of the title. Classification wording "Wesco Confidential" is a placeholder pending Wesco's official label.

### 2026-10-05 — entroCIM data-center brochure language: "DCIM" replaced with "Data Center" and "IT Asset"
- Status: Made
- Owner: Nathan Kehr
- Context: Sales-facing entroCIM brochure used "DCIM" (Data Center Infrastructure Management) language; Nathan Kehr directed a terminology correction for commercial positioning.
- Decision: Replace "DCIM" with "Data Center" and "IT Asset" framing. David Blondel to work with Natalia Shtern on the revision (`05` B95).
- Effect: Commercial-positioning correction only; no product or architecture change.
- Source: Fw: DCIM Brochure entroCIM (email), weekly evidence 2026-10-05.

### 2026-10-05 — i3 Alliance draft: Wesco's IP position returned to i3 after counsel review
- Status: Made
- Owner: Brandon Thompson (Legal), following Nikos Minas's IP review
- Context: Continuation of the i3 Section 8 / IP-chain exposure tracked on `04` (Active). Legal reviewed the draft for core-IP, reverse-engineering, and claimed-registration language.
- Decision: Counsel's targeted IP changes and questions were finalized and the marked-up draft was sent back to i3.
- Effect: Advances the i3 Alliance Agreement toward signature; does not resolve the underlying IP-chain risk on `04`, which stays open until i3's response is seen.
- Forum where this should be decided: i3 Alliance signature path (no standing forum in `07`).
- Source: FW: i3 Draft (email), weekly evidence 2026-10-05.

### 2026-10-05 — CDA commercial model: annual managed service, camera-first entry, outcome-based vertical selling (Inferred — no named approver)
- Status: Made (Inferred — surfaced for Darryl's confirmation, not yet an explicit decision in his own words)
- Owner: Not confirmed. Direction reflected in AI meeting notes from the 2026-10-02 CDA business-case/sponsorship review; Bill Muczko's sponsorship acceptance that session (`03` 2026-10-02) is Explicit, but the commercial-model framing itself carries no single named approver in the transcript.
- Context: CDA has been building toward a business case since the 08-06 CDA Phase 3/4 work. This session packaged it as a recurring-revenue managed service: inventory, patching, and security, led with known camera deployments, sold on outcomes using existing connectors (Axis/Hanwha, Airwall).
- Decision / framing adopted: CDA = Wesco-operated annual managed service, camera-first, outcome-based vertical selling.
- Risk of waiting: none from waiting on confirmation — the framing is already being used in sales/commercialization material (`Products/CDA/CDA.md`). Risk is in NOT confirming: enterprise pricing, willingness to pay, anchor accounts and TSS delivery capacity are all still open (see Decision Radar, CDA enterprise pricing).
- Follow-up: confirm with Darryl at next CDA touchpoint whether this framing is final or still being tested with buyers (Peter Ferrell's challenge this session went to pricing/scale, not to the model itself).
- Source: Connected Device Assurance business case review and sponsors.loop (AI notes); CDA Business Case - Site-Based Market.pdf; weekly evidence 2026-10-05.

### 2026-10-05 — WAM/ADM FY27 priorities narrowed to three buckets: DDP integration, core ADM development, required Strev integration only (Inferred — no signed decision record)
- Status: Made (Inferred — surfaced for Darryl's confirmation)
- Owner: Not confirmed; reflected in WAM leadership discussion (Akansh Gangil's forum), no signed record identified.
- Context: Continuation of the 2026-09-25 WAM strategy direction (Wesco-owned data, DDP/EUDM as primary foundation) and the 2026-09-16 "WAM strategy narrowed to attainable, data-supported outcomes" decision.
- Decision / framing adopted: Capacity concentrates on DDP integration, core ADM product development, and Strev integration work that is required (not discretionary). General Strev feature requests stay in Strev's own backlog unless integration funding is separately justified.
- Risk of waiting: if not confirmed as the actual planning basis, it collides with the open "Run + Complete" WAM/ADM 2027 planning-basis decision below, which is still unapproved.
- Forum where this should be decided: WAM Data Challenges (Darryl-owned, weekly) or the WAM Leadership Sync.
- Source: WAM connect.loop (AI notes), weekly evidence 2026-10-05.

### 2026-10-02 — CDA business sponsor: Bill Muczko accepts
- Status: Made
- Owner: Bill Muczko (decision); Darryl Benson (ask)
- Context: CDA was the only FY27 Invest product without a business sponsor; Sean McCloskey (09-15) set a committed sponsor as a condition before CDA advances; Nathan Kehr (09-18) advised waiting for a real sponsor. Nathan Kehr is an ally and champion of CDA, not a gatekeeper (Darryl, 2026-10-02); his 09-18 "let's wait until we get a real sponsor" was advice, not a condition. Nominated via Bob Caprise 09-18.
- Decision: Bill Muczko agreed to be CDA's business sponsor at the business case review, 2026-10-02 (Darryl, direct; not stated verbatim in the transcript).
- Effect: closes Backlog entry 2026-09-18 (CDA business sponsor). Satisfies the sponsor half of Sean's 09-15 conditions for the data-center track; the sized-market half stays open. The Digital Product List's "Business Sponsor: ?" for CDA can now be filled.
- Follow-up: reported to Sean by Teams 2026-10-02 (sent); Sean walkthrough of the numbers scheduled 2026-10-06; Sean review of the numbers before the workbook is shared (`05` A51 held). New open decision raised in the meeting: enterprise pricing construct (Backlog, 2026-10-02).
- Source: Teams transcript, 2026-10-02 (`Products/CDA/05_Operating_Record/2026-10-02_CDA_Sponsorship_Meeting_Transcript.docx`); summary `Deliverables/CDA/2026-10-02_CDA_Sponsorship_Meeting_Summary.md`.

### 2026-10-02 — CDA business case uses the FY27 AOP development figure, $246,787
- Status: Made
- Owner: Darryl Benson
- Context: the CDA deck gave two 2027 development figures: $246,787 (the FY27 AOP submission, B18) in one speaker note, and $261K (the pro forma, built on 6.75 India FTE from the later staffing plan) on the Plan, capital and audience slides. The gap is headcount only: the AOP costed 6.25 India + 0.25 NA FTE for eight months plus $45,000 Other IT Expense.
- Options considered: keep the model at $260,573 and label the AOP figure separately; tie the model to the AOP figure.
- Decision / Recommended path: tie the model to the AOP figure because it has backing in the AOP analysis (Darryl, 2026-10-02). Pro forma v4.6 Inputs C11 carries the AOP basis; the deck shows $247K (the AOP figure, rounded) throughout, and a check row fails the deck build if model and AOP diverge.
- Follow-up: none. The 2028 sustain-and-enhance team ($323,360, 7 FTE) is unchanged. Detail in `Products/CDA/CDA.md`, v4.6 entry.

### 2026-10-01 — CLM not adopted in the FY27 AOP; no build in 2027
- Status: Decided (reported to Darryl; decision maker and forum not stated)
- Owner: corporate AOP process (Sean McCloskey, Akash, Nanda Kumar Rajagopal were the named participants)
- Decision: CLM will not be built in 2027; it was not adopted in the AOP for next year.
- Effect: closes the 2026-09-28 Radar entry. The terms proposed in the v2 Capacity and Skills Assessment (funding transfer, 13-FTE team, discovery gate) are not needed for FY27. The option of moving CDA to the entroCIM team to free the CDA development team for CLM no longer has a reason; CDA's FY27 plan stands as it was unless Darryl decides otherwise.
- Not known: whether CLM is deferred to FY28 or dropped; whether Nanda's organization pursues it another way (licensed platform, own team); whether the intent to place it with Darryl's team carries forward; what happens to the $1.2M request.
- Source: Darryl, direct, 2026-10-01 14:29 ("I just heard"). Original source not stated.

### 2026-09-29 — CDA commission modelled on Nate Kehr's actual plan: 5 percent of three-year contract value, paid up front

- Status: Made
- Owner: Nate Kehr (the plan); Darryl Benson (the model)
- Context: the pro forma carried a placeholder of 3 percent of the annual fee paid for three years. Nate Kehr, 2026-09-29: "it's really simple. We pay 5% on the deal. The sales rep (outside sales representative or global account representative) gets 2%. The sales manager/director gets 2% and the inside sales rep gets 1%. We pay on the total contract value (first three years) up-front."
- What changed in the model: commission is 5 percent of three years of contract value, expensed in the year the site is sold, not spread across three years. In total that is 15 percent of one annual fee against the placeholder's 9 percent, and all of it lands at the point of sale.
- Why this matters: it is a cash-timing change more than a cost change. Peak cash in the plan is driven by the growth years, and front-loading commission deepens it. It also means a site that does not renew after three years was fully commissioned on revenue that did not all arrive.
- Follow-up: applied in `Deliverables/CDA/2026-09-29_CDA_Pro_Forma_v3.5.xlsx`, Inputs rows 25 and 26. The split between rep, manager and inside sales does not need modelling; only the 5 percent total does.
- Source: Nate Kehr, relayed by Darryl, 2026-09-29.

### 2026-09-29 — CDA is a single packaged service, not the two-tier Assure/Manage model from the August brief

- Status: Made
- Owner: Darryl Benson
- Context: The 2026-08-28 executive brief (`CDA_Exec_Brief_SHARE_2026-08-28.pptx`, slide 5) presented CDA as two commercial tiers, Assure as the base service and Manage as the advanced service, with Wesco Configuration Assurance on top. Pro forma v3.3 and the 2026-09-29 product and business case deck instead price one packaged annual fee per site, covering hardware, software and services, with size (Small, Medium, Large, plus a complexity uplift) as the only commercial variable. Asked to confirm which stands, Darryl, own words 2026-09-29: "it is NOT a two-tier model. Architecturally, we may have different modules, but that is not important."
- What this decides: the packaged single-fee model supersedes the August tiering. Assure and Manage are not commercial tiers and are not used in customer-facing or sales-facing material. Module structure inside the platform is an engineering matter and does not surface in pricing or positioning.
- Why this matters: sellers and executives who saw the August brief would otherwise ask which tier they are quoting. It also protects the pricing posture already set (published fee held, component cost not exposed, margin as the output), which a tiered model would reopen.
- Follow-up: no change needed to the 2026-09-29 deck, which already prices by site size only. Any reuse of August material should drop the Assure/Manage naming. See `Products/CDA/CDA.md` and `Deliverables/CDA/2026-09-30_CDA_Pro_Forma_v3.3.xlsx`.
- Source: Darryl, direct, 2026-09-29, in response to the conflict raised from the August brief.

### 2026-09-25 — Miller Electric PO approved and delivered
- Status: Made
- Owner: Nathan Kehr and Brad Stevens (approval); Mike Reed and Chad Steger (delivery)
- Context: **Field note, Darryl, 2026-09-28: "Outside of my communication channels, the Miller Electric license purchase was approved last Friday by Nate and Brad. Mike Reed and Chad delivered this AM."** This closes the pricing decision flagged Critical/Immediate in the 09-18 evidence (PO below the 50,000-point threshold while retaining the discounted flat SkyFoundry price). Per Darryl's own words, the approval happened 2026-09-25 through a channel outside the evidence record (email/Teams/M365 retrieval never captured it) and delivery executed 2026-09-28.
- What is not known: which of the four options considered (process as-is, enforce the minimum, reprice, or pause) was the actual basis for approval — Darryl's note confirms the purchase was approved, not the specific pricing mechanism. Do not infer one; ask if it matters for precedent on future sub-threshold Miller Electric orders.
- Why this matters: resolves a ten-day-old blocked order and an OEM-agreement pricing-risk question with no accountable owner, surfaced as the top same-day priority in this morning's briefing and the 2026-09-28 weekly.
- Follow-up: `04` Active row retired; `05` C56 closed; this Backlog entry (2026-09-18) marked resolved below. `Briefings/2026-09-28_Weekly.md` corrected in place.
- Source: Darryl, field note, 2026-09-28 (outranks the absent M365/Copilot evidence per standing evidence discipline — his word closes this regardless of what any future package shows).

### 2026-09-25 — Ford 2027 Support Services Agreement sent, separating baseline Maintenance & Support from a scoped Services agreement
- Status: Made
- Owner: Adam Lazare (decision), Leanne Gordon
- Context: 14-day evidence window (M365 Evidence Weekly, 2026-09-15 to 09-28). Adam Lazare: "Only outstanding assignment on our plate is getting the Services proposal sent out end of week." The proposal separates Ford baseline Maintenance & Support from a revised Services agreement, moving SME/T&M hours into Services. Sent by the required date, 2026-09-25.
- Why this matters: this is the commercial artifact the 2026-09-09 "Ford support/SLA commercial model" Decision Radar entry was tracking toward a forum decision (see that entry, now resolved by this event). It supersedes the entry rather than merely advancing it.
- What this does not resolve: it does not close `05` B62 (the UDAC platform audit — versions, licensing, integrations, data quality, system health) or B69 (Chad Steger's confirmation that delivery can support the finalized scope, due 2026-09-19 and unconfirmed). A sent proposal is not evidence the platform was audited or that Wesco can staff what it commits to. See `04` Ford watch item — do not retire that row on this event.
- Follow-up: `05` C35 (Ford support scope document) is very likely satisfied by this proposal; per closure discipline this is Potentially closed, not closed, until Darryl or Leanne Gordon confirms directly. `05` C43 (Ford pricing-model language) likewise very likely closed — the proposal is dated and carries three-year pricing.
- Source: Ford Tiger Team (Teams channel, 2026-09-15 through 09-25); `RE: entroCIM Release – Version 3.1.12.13` email.

### 2026-09-25 — WAM strategy: Wesco-owned data and DDP/EUDM as the primary foundation, not external data acquisition
- Status: Made
- Owner: Sean McCloskey, as relayed by Akansh Gangil (WAM - Product Team, 2026-09-25 — search-snippet evidence, no verbatim transcript)
- Context: WAM's data strategy is set to focus on data Wesco already owns, with explicit acknowledgment of data-quality limits, DDP/EUDM as the primary foundation, and ADM-to-Strev flow (enrichment and normalization run through Strev) rather than pulling renewal analytics or other capability from Strev as a data source. Competitor or non-Wesco data acquisition is explicitly not the baseline strategy.
- Why this is a decision and not a status update: it forecloses one direction (buy/license external data to fill WAM/ADM gaps) in favor of another (fix and scale what Wesco already collects), which changes the required skill set, the investment narrative, and the FY27 AOP scope for WAM/ADM.
- Evidence caution: this reaches the record as AI notes / meeting chat, not a verbatim transcript, and the decision-maker (Sean McCloskey) is relayed by Akansh Gangil rather than directly quoted. Treat as Stated, not independently confirmed, until corroborated.
- Risk of waiting: none — this closes a direction question rather than opening one. The open question it creates is resourcing: see Decision Backlog, "Finalize WAM/ADM resource needs and skill sets under the new data strategy."
- Follow-up: `05` B88 (Akansh Gangil to finalize resource/skill requirements); `Products/WAM/WAM.md`.
- Source: WAM - Product Team, 2026-09-25 (Teams channel, search-snippet evidence, two indexed chunks).

### 2026-09-18 — Prioritize the JACE connection first for the Ascent Airwall deployment
- Status: Made
- Owner: Darryl Benson, supported by Chad Steger
- Context: ascent airwall transcript, 2026-09-18 (complete, 289 lines). The Ascent Airwall device is now installed, online, and visible to the entroCIM team; the remaining dependency was framed as a choice between chasing multiple downstream BACnet devices at once or securing the JACE connection first and working outward from it. Darryl and Chad Steger set JACE first, then identify downstream BACnet devices once that connection exists.
- Why this matters: converts a multi-front integration effort into a sequenced one, and makes Chris Askew's JACE IP address and read-only credentials the single pacing item rather than one of several open threads.
- Follow-up: `05` B4 (Ascent POC, updated); `Products/Navigator/Navigator.md`.
- Source: ascent airwall (transcript, complete); `Re: Ascent airwall` (email).

### 2026-09-18 — entroCIM 2027 roadmap reset to a managed cadence on reduced development capacity under the covers; the Cisco real-estate opportunity is routed to both
- Status: Made
- Owner: Darryl Benson
- Context: Bob Caprise raised a Cisco Connected Real Estate opportunity (NetBotz replacement and power visibility across MDFs) during the CDA financials follow-up. Claude proposed routing it to entroCIM with CDA overlap. Darryl's answer, 2026-09-18: "Both. Under the covers, we're using SkySpark and a lot of the PODs that make up entroCIM, so if we can get our foot in the door based on this product, we should be able to make entroCIM work where CDA is the Data Collector."
- Decision: CDA is the land product; entroCIM is the expand product, with CDA as the data collector on the same SkySpark and POD foundation. Opportunities like Cisco CRE are pursued as CDA entry with an entroCIM path.
- Relationship to prior decisions: refines, does not reverse, 2026-08-26 and 2026-09-01. Customer-facing, CDA still stands alone and must not read as an entroCIM feature add-on. The land-and-expand logic is internal strategy and should be raised with Sean as a discussion point, not presented as a pitch.
- Follow-up: `Products/CDA/CDA.md` (2026-09-18 section); Sean discussion points 2026-09-18.
- Source: Darryl, chat, 2026-09-18.
- Update 2026-10-02 (Darryl, chat): the wedge framing is no longer held back for Sean alone. Darryl has explained CDA as the wedge for entroCIM to several people and will state it as deliberate strategy with internal audiences, including the Bill Muczko / Bob Caprise sponsorship review. Customer-facing rule unchanged. See `Products/CDA/CDA.md` (2026-10-02 section).

### 2026-09-17 — entroCIM 2027 roadmap reset to a managed cadence on reduced development capacity
- Status: Approaching
- Owner: Darryl Benson, with David Blondel and Ron Snyder; staffing confirmation owed by Darryl
- Context: 2027 entroCIM Roadmap Discussion, 2026-09-16 10:00-11:00 (verbatim transcript, complete). An estimated nine resources are moving out of entroCIM development. The three agreed rather than merely discussed: release cadence shifts to two major feature releases (Q2, Q4) plus smaller security/improvement releases (Q1, Q3); scope narrows to strategic integrations only; planning moves to requirements-based epics ahead of sprint planning, replacing sprint-level improvisation.
- Why this is a decision and not a status update: it commits the team to a materially smaller delivery envelope before any customer, Managed Services, AI, or integration commitment is made against it. This is the delivery-capacity consequence the 08-05 commercial-performance watch item modeled as a possibility (CSS Sales headcount-reduction request against 2027); it is now specific, named, and in motion rather than a scenario.
- What is not knowable today: the final staffing count and transition timing. Darryl, in session: "I'll recount it. I'll give you a number." Until that lands, "nine resources" is the planning estimate, not a confirmed figure.
- Risk of waiting: uncontrolled intake continues against a capacity baseline that leadership above Darryl has not been told is changing. Sean McCloskey, Nathan Kehr and Brad Stevens are all currently operating on the prior cadence assumption.
- Options considered: continue the aggressive roadmap and absorb the capacity loss as slippage (rejected, produces uncontrolled trade-offs); formally reset to a managed roadmap with published capacity assumptions and an intake rubric (adopted).
- Forum: no standing forum owns this; recommend it goes to Sean McCloskey as a direct communication ahead of any forum, given the exec-alignment urgency, then into the Digital Products Portfolio Review once a forum date exists.
- Follow-up: confirm final resource count and transition timing (Darryl, held for the 2026-09-18 Register A disposal sweep per the standing note on this register); publish the right-sized quarterly roadmap and intake rubric (David Blondel/Ron Snyder); executive communication to Sean McCloskey, Nathan Kehr, Brad Stevens.
- Source: 2027 entroCIM Roadmap Discussion, 2026-09-16 (transcript, complete, 914 lines); `Products/entroCIM/entroCIM.md`; `04` new Active row.

### 2026-09-17 — JCI MSP conversion: the entire existing Airwall estate moves to the new licensing structure at signature, with nothing left on the legacy model

- Status: Approaching (depends on signature; JCI has not responded to the 2026-08-31 markup)
- Owner: Darryl (commercial position); Brian Miller (agreement text)
- Context: Darryl direct, 2026-09-17: "We will convert all existing products into the new licensing structure when signed, so we will not be orphaning older products." Stated alongside his designation of the MSP contract as the baseline for Airwall and Conductor technology use (same date, see `Products/JCI_Partnership.md`).
- **Reading applied, and flagged for correction.** "Products" is taken to cover both dimensions of the existing estate: existing prepaid 12-month licence orders, and the older Airwall hardware generations accumulated across roughly a decade of deployment, including pre-acquisition Tempered-era units. Both are in scope for conversion; neither is left behind. If Darryl meant only one of the two, this entry narrows.
- **Why this is a decision and not a status update.** It sets the conversion as estate-wide and immediate at signature rather than prospective. The alternative shape, which is the default in most licensing transitions, is that only new provisioning goes onto consumption billing while existing prepaid orders run to term. That would phase the commercial benefit in over up to twelve months and would leave a two-model estate to administer in the interim. Estate-wide conversion realizes the benefit at signature across the whole installed base and keeps one operating model.
- **What this adds to the durability requirement (Darryl, 07-17).** The conversion mechanism is itself a term that must be captured, not an intention to be honored later. Specifically unresolved in the record: treatment of unamortized prepaid balances on existing orders (credited into the pool, written off, or run in parallel); whether existing licences transfer into the pre-granted pool at current count; whether older hardware generations are eligible under the new structure or excluded by product definition; the reconciliation method at conversion; and the effective date or conversion window. If these sit outside the agreement text, "no orphaned products" is goodwill rather than a right.
- **Connects to the 2026-05-26 decision on notice periods.** The 60-day product-change and 180-day EOL notice requests are the protection against JCI converting legacy hardware generations into the new structure and then EOL-ing them out of it afterwards. Those two terms carry more weight under estate-wide conversion than they did when they were agreed.
- **Operational dependency: Wesco needs an accurate current licence and device inventory to convert against.** A decade of deployment plus the migration out of the pre-acquisition hosted environment into Wesco Azure means the count is not self-evidently clean. Note that the JCI metering agent's first reading would in practice establish the conversion baseline, which makes **WAB approval of that API connection path-critical to the commercial conversion, not merely a compliance step**. Relays are in scope: relay software is free but the underlying 300v licence is charged (07-15 transcript).
- **Not yet quantified, and it should be before signature.** Whether conversion is a saving, roughly neutral, or a cost depends on how much of the estate is provisioned-but-idle. Provisioned and in use is broadly price-neutral but improves cash flow by removing the 12-month prepay. Unprovisioned pool licences become free under the new model. This is a number Darryl could put in front of Sean and a candidate `09_Impact_Ledger.md` entry once the agreement is signed and the inventory is established.
- Options considered: (a) estate-wide conversion at signature (chosen); (b) prospective conversion with legacy orders running to term; (c) conversion by exception or by customer. (b) and (c) both produce a two-model estate and defer the benefit.
- Risk of waiting: the markup is with JCI now. If the conversion mechanism is not in the text when the agreement closes, the position is unrecoverable without reopening negotiation.
- Forum: JCI legal exchange with Brian Miller; no standing forum exists for JCI (noted in `07_Operating_Cadence.md` as an open item).
- Follow-up: `Products/JCI_Partnership.md`, 2026-09-17 baseline entry and Next Steps rows.
- Source: Darryl direct, 2026-09-17 (session). No JCI confirmation; this is Wesco's position, not an agreed term.

### 2026-09-17 — Virtual Site Survey to be added as a feature of the existing white-label instance, priced per site
- Status: Approaching
- Owner: Amy Aguirre (business case and intake, with Wade Bursch); Darryl (entitlement and contract vehicle)
- Context: Site assessment / AI features call, Amy Aguirre and Darryl Benson, 2026-09-17 (transcript, complete). Strev built a Virtual Site Survey prototype in its own demo environment against Wesco TS/TSS requirements: an uploadable assessment checklist delivered to contractors in a mobile app, with LiDAR scanning on Apple devices and AI extraction of assets from cabinet photographs, feeding Wesco Asset Management for validation and enrichment. Built in about a month at no charge following a live demo to TS.
- **Why this is a decision and not a status update.** Three shape-setting choices are being made here, none of them yet contracted. The capability lands as another entity type inside the existing white-label instance ("sites" alongside assets, contracts and suppliers), not a separate instance, so it rides the existing agreement rather than opening a new tenant. The run model is **per site, explicitly not per asset**, which is a different revenue shape from every other WAM line. And the build is being finalized on Strev professional services, which means a development cost that nobody has yet claimed in an AOP.
- **What is not knowable today.** Strev has not provided either the professional services development price or the per-site rate; both were requested by Amy on or before 09-17. Whether the capability falls inside the $84,000 AI enablement or is priced separately is unresolved and is question C46/A43 material. The hardware architecture is open: the July TS document naming Avatore and the Pano XV2 camera is a solution brief, TS is still researching LiDAR options, and Strev has never spoken to Avatore.
- **Maturity is disputed in the record.** Sunny Sharma (09-16) described it as a real product with no Wesco integration and at least two months of partner work; Amy (09-17) describes a prototype built in a month with Wesco TS. Both accounts are filed. Do not present either as settled.
- Options considered: (a) treat as a Strev feature request riding the existing agreement; (b) treat as a separate product with its own commercial construct. The 09-17 conversation lands on (a) by default rather than by decision, which is worth making explicit before the amendment is drafted.
- Risk of waiting: the amendment Darryl will draft against the new entitlement document is the moment the commercial shape gets fixed. Drafting it before the site survey pricing exists either leaves the capability out or commits to it unpriced.
- Forum: Amy's UiPath intake and the requested demo (governance); FY27 AOP for the development and run cost, **owned by Amy**. Darryl's forum on this is the amendment, not the funding route.
- Follow-up: `05` A49 (amendment kickoff, dated 2026-09-24 — written as a dated action rather than a trigger, because the awaited entitlement document carries no vendor delivery date), A43 (question list, now extended to cover site survey pricing and the third AI feature), C46, C49, C50, C52, C53. **C51 (Amy's AOP request) was opened and dropped the same day at Darryl's direction — the funding side of this thread is Amy's, not his.** Product detail: `Products/WAM/WAM.md` § Virtual Site Survey.
- Source: Amy Aguirre / Darryl Benson call, 2026-09-17, `Products/WAM/Briefings/2026-09-17_Amy_Aguirre_Site_Assessment_AI_Features_Transcript.md`.

### 2026-09-16 — WAM strategy narrowed to attainable, data-supported outcomes
- Status: Approaching
- Owner: Darryl, with David Blondel and Akansh Gangil (drafting); Chris Gazdic and Govindaswamy (review)
- Context: Digital Products / Agile Staff Meeting, 2026-09-15 (transcript, complete). Sean McCloskey and Darryl agreed the WAM strategy needs to be reset around what the actual vendor, product, and license data can support, with explicit statements of what the solution will and will not accomplish — "limited in, limited value out." This continues the WAM reset thread already running in `03` (09-01, 09-03, 09-10 entries) rather than opening a new one; today's evidence is Sean formally asking for the next step.
- Why this is a decision and not a status update: it commits the team to narrowing customer-facing claims to what accessible data can actually support, ahead of the benefits-realization and renewal conversations already in flight (Ford, sales-ops renewal notifications). Getting the boundary wrong in either direction — overclaiming or underselling — has already cost credibility once (John Engel/Rob Hasting negative impression, `06`).
- Options considered: continue current broad positioning; narrow claims to attainable data coverage and measurable renewal impact. Recommended and adopted: narrow.
- Risk of waiting: none acute this week, but this needs to land before the 2026-09-18 Digital Products portfolio deep dive (the entroCIM financial-metrics slide is already flagged for a 09-17 update for that session, and WAM sits in the same deck).
- Forum: Digital Products / Agile Staff Meeting (Sean-owned) for review; feeds the 2026-09-18 portfolio deep dive.
- Follow-up: `05` A48 (advance the strategy draft with David Blondel/Akansh Gangil, then route to Chris Gazdic and Govindaswamy).
- Source: Digital Products / Agile Staff Meeting, 2026-09-15 (transcript, complete, 825 lines).

### 2026-09-15 — Strev AI Feature Pack: commercial evaluation opened, no decision taken
- Status: Approaching
- Owner: Darryl, with Lisa Orton (governance/intake) and Amy Aguirre (use case origination)
- Context: Amy Aguirre submitted two Strev AI use cases (Data enrichment, Smart import) through UiPath intake on Lisa Orton's instruction, 2026-09-15. Separately, Revnue's "Feature Entitlements, Expansion Roadmap, and AI Feature Pack Pricing Framework" v2.5 (May 2026) and a Wesco-built WAM cost model were filed into `Products/WAM/` on 2026-09-15. Full reconciliation: `Deliverables/WAM/2026-09-15_Strev_AI_Entitlement_Discrepancy_Review.md`.
- **Why this is a decision and not a feature request.** Per v2.5 §5.4, every AI add-on SKU requires an active AI Feature Pack on the same Authorized Tenant and draws from that tenant's credit pool. The closest catalog match to "Smart import" is LLM-based Data Upload, an add-on in private beta with no published pricing. So two use case approvals would in practice commit Wesco to a platform SKU at $84,000 per year per environment plus a $10,000 per-tenant annual credit minimum, with the vendor's own illustrative scenarios running $94,000 to $184,000 per year. The contract as amended is silent on all of it.
- **What is not knowable today.** v2.5 §6.3 publishes no credit conversion rates and states there is no standard method to translate a credit into token usage, while referencing "published per-feature conversion rates (see §6.3)" in five other places. The annual floor can be calculated; expected consumption cannot. Ingestion volume is what drives credit burn, which is exactly what these two use cases are.
- Options considered: (a) treat each use case as a discrete feature approval; (b) treat both as the first two use cases of a platform decision and decide the platform question explicitly. Recommended: (b).
- Risk of waiting: approving use cases individually arrives at an $84,000-plus annual commitment by accumulation rather than by decision, and does so before the duplication question against the Wesco AI team's file ingestion work has been answered.
- Forum: Lisa Orton's 2026-09-25 session with Greg's team, as the governance forum; FY27 AOP for the funding question.
- Follow-up: `05` A43 (Revnue written question list), A44 (IDP duplication comparison), C46 (Amy SKU confirmation). Brief to Lisa: `Deliverables/Exec_Briefs/2026-09-15_Lisa_Orton_Brief_Strev_AI_Use_Cases.md`.
- Source: Lisa Orton email 2026-09-15 14:26 forwarding the Amy Aguirre thread; Revnue v2.5; Wesco WAM cost model.

- **Update 2026-09-17 (Amy Aguirre call, transcript).** Four changes, one of which narrows the risk and three of which widen the scope.
  - **A funding request is forming; nothing is funded, and the distinction was corrected the same day.** Amy will include the $84,000 in the FY27 WAM AOP and will add the site survey development number once Strev provides it. **AOP inclusion is a request, not funding** (Darryl, direct, 2026-09-17): approval and a UiPath project are both still required before money exists behind it. The `04` no-funding exposure therefore stands. Recorded as a portfolio-wide test in `01` § Funding Governance, because the same error is available on every AOP-cycle item.
  - **The feature set is three, not two.** A third requirement appeared: **data normalization**, a field-capture cleanup feature that groups variant label spellings and normalizes the database on a selected value. It is not a name in v2.5 and has no catalog mapping. Data extraction and the site survey are the other two.
  - **Darryl's position that all three sit inside the $84,000 is an assumption, stated as one.** It is the load-bearing assumption in this thread: if normalization or site survey are add-on SKUs, the floor moves. Confirmation depends on the replacement entitlement document from Christina, which has not arrived and which supersedes v2.5 entirely (Sunny, 09-16).
  - **Ownership of intake settled.** Amy files the UiPath intake herself for the AI use cases; Darryl asked to be optional. This closes the question of who routes the governance and removes it from Darryl's list.

### 2026-09-15 — i3 Alliance Agreement: Wesco signature path resolved to Lee Osterman
- Status: Made
- Owner: Lee Osterman (signature); Legal (authority confirmation)
- Context: i3 Alliance Agreement email thread, M365 evidence 2026-09-14 to 2026-09-15. Legal confirmed a VP may sign without Finance input because the agreement itself is not expected to generate sales directly. Lee Osterman, explicit: "I will sign once it comes back." i3's side is already executed — Kirk Whittington confirmed the i3 team signed.
- Decision: Lee Osterman signs on Wesco's behalf once the document returns from the current review round.
- Why it matters: settles the mechanical signing question, but does not settle the broader question below (cross-BU ownership/sponsorship), which stays open.
- Follow-up: **the actual pacing item is `05` A41** (Section 12 redline to Brandon Thompson, due 09-11, currently overdue) — the document cannot return to Lee for signature until that round ships. See `Products/i3_Alliance.md`, `05` C45.
- Source: weekly evidence 2026-09-14 to 2026-09-15, i3 Alliance Agreement email thread.

### 2026-09-14 — Quest hosting continues month-to-month until the environment is decommissioned
- Status: Made
- Owner: Darryl
- Context: Quest Invoice email, weekly evidence 2026-09-14. With seven of eight environments migrated to Azure and only dev-01 outstanding, Darryl elected to keep Quest hosting on a month-to-month term rather than renew or commit to a longer period.
- Decision: continue month-to-month until decommissioning.
- Why it matters: it converts the remaining Quest spend into a variable cost that falls away when dev-01 cuts over, and it removes any commercial incentive to let the last environment drift. The cost stops when the cutover happens, so the cutover date is now the cost driver.
- Follow-up: dev-01 cutover is the gating event (`04`, Quest-to-Azure row; owners Babu Papanna and Chad Steger). Confirm the Quest audit and shutdown steps are scheduled behind it.
- Source: weekly evidence 2026-09-14, Quest Invoice email.

### 2026-09-14 — CSS Platforms All Hands pushed one week
- Status: Made
- Owner: Chad Steger and team leadership
- Context: eCIM Leadership chat, weekly evidence 2026-09-14. Holiday and availability.
- Decision: the session moves out one week. Recorded as a one-off reschedule, not a cadence change — the package's own cadence section returned none, and `07_Operating_Cadence.md` is unchanged.
- Source: weekly evidence 2026-09-14.

### 2026-09-11 — Strev under consideration as the system of record at complex-build sites, which would reverse part of the confirmed data architecture
- Status: Approaching
- Owner: GPO, with Darryl and Akansh Gangil
- Context: Darryl, direct, 2026-09-11, Confirmed, not transcribed. Strev is being considered for use at Wesco's complex-build sites as a system of record. If that holds, metadata would need to flow back from Strev into ADM, and from ADM into EUDM. Separately, the GPO is currently reviewing the Strev tool in the warehouse.
- **Why this matters beyond the tooling question.** The architecture Darryl confirmed on 2026-08-19 records DDP and EUDM as the single source of truth for asset data and the only route into ADM, with WMX and VAS delivering into DDP and ADM taking nothing directly from either. A Strev system-of-record role at the capture sites introduces a return path that the confirmed architecture does not contemplate, and it puts a vendor platform upstream of the enterprise data layer for a class of asset data. That is a governance question as much as an integration one, and it should be settled before the return path is designed rather than after.
- Second-order consequences to work through, none of them resolved: which system is authoritative when Strev and EUDM disagree on a serial or a parent-child relationship; whether the Strev SOW covers a write-back interface or whether it is new scope; how the return path is governed under the existing Strev QA and release governance obligations; and whether this changes the 2027 Strev priorities, where bulk parent-child asset mapping already assumes Wesco produces the hierarchy data first.
- Carried on the Sean deck as gate G7, "Strev as system of record at complex-build sites", owner GPO, under review, with the two return paths drawn as under-consideration lines.
- Risk of waiting: the complex-build data model is already open between Daniel Totino and Akansh Gangil. Settling the data model without settling this question means settling it twice.
- Forum: WAM Data Challenges, or the Level 4/5 Services Support Assessment where Manny Tracey's sites are represented.
- Source: Darryl, direct, 2026-09-11.

### 2026-09-10 — i3 Section 12: negotiate 12.4, not 12.2, and preserve freedom to partner as an operative term
- Status: Made
- Owner: Darryl
- Context: Section 8 edits returned fully accepted; Legal asked for a Section 12 review. Darryl's commercial question was whether Section 12 locks Wesco into i3 on a project where our contacts and i3's overlap, when tying the business to a different partner is to our advantage.
- **Finding, and it inverts the obvious read.** 12.2 and 12.3, the clauses that look like the constraint, are close to workable: project-scoped, six-month tail, explicit protection for pre-existing and independently sourced relationships. **12.4 is the constraint.** It sits inside a non-circumvention section but is not project-scoped, not time-limited, perpetual through §16.6, applies to "any third party," and attaches to the §6.2 Core IP definition claiming graph models, ontologies and schemas. That is a restraint on which other data center partners Wesco can work with, indefinitely, on a standard i3 defines and never has to prove. §15.2 removes the liability cap for IP claims.
- **Decision on where to spend the round:** hold §12.4 and §12.2(b); concede §12.1 reciprocity first if a concession is needed. §12.4 asks are burden of proof on i3 to identify actual Core IP used, exclusion of generally known and open-standard methods, an unaided-memory residual-knowledge carve-out, and a two-year post-termination term. §12.2(b) ask is a client-initiated carve-out, since as drafted a developer's own decision to change providers is Wesco's exposure.
- **Second decision: freedom to partner becomes an operative term.** §12.1 disclaims restriction on "general access to the market," which is a statement of intent. Proposed new §12.6 states affirmatively that Wesco may team with, subcontract to, or refer business to any party including i3 competitors, on any project including an i3 Project for scope i3 does not perform. This is the clause Darryl points to when a client relationship is shared.
- **Entity scope fixed inside Section 12 rather than waiting on §1.** If "and its affiliates" carries through, the covenant binds Wesco business units that cannot see the project. A sentence limiting §12.2 to the contracting entity and to personnel with actual knowledge resolves it whether or not §1 is narrowed this round.
- Options considered and rejected: pressing all eight items equally (dilutes the ask if i3 treats Section 12 as it treated Section 8); rejecting 12.2 wholesale (the section's stated principle is legitimate and the drafting mostly honors it); accepting 12.4 on the strength of its independent-development sentence (no burden of proof, no residual-knowledge treatment, "substantially similar methodology" undefined).
- Risk of waiting: none material this week. The risk is signing 12.4 as drafted, which is permanent and uncapped.
- Follow-up: A41 send the package; C-i3-3 five questions to Legal; `04` C-i3-2 updated with the second surfacing. Files in `Deliverables/i3_Alliance/`; product record in `Products/i3_Alliance.md`.
- **Scope narrowed same day, at Darryl's direction.** This is his final pass on the document. Review confined to the Digital Products question; reciprocity, remedy language, the §1 affiliate question, the consent standard and the 12.3 documentation mechanics are recorded in Part B of the memo and left to Brandon Thompson's judgment rather than argued. Six asks, priority-ordered, with a stated concession order: hold 12.4, 12.2(b) and new 12.6; trade items 4 to 6. Three questions only, led by whether 12.4 is movable, because if it is perpetual and immovable the decision is a product decision and not a legal one.
- Source: Section 12 text supplied by Darryl 2026-09-10; review session same day.
- **Update 2026-09-18 (M365 evidence, "i3 Agreement IP Question" email thread, retrieved complete):** the choice Darryl framed 09-10 is now visible as an actual drafting fork in front of Legal, not just Wesco's ask. Two approaches are being compared: broad mutual anti-replication wording (closer to i3's original 12.4) versus the narrower, burden-of-proof reverse-engineering restriction Darryl's redline proposes. Evidence frames the open question as needing "clear identification of each party's Core IP" before either wording can be finalized — which is the same §6.2 Core IP definition problem this entry already identified as the root cause. **This does not change the decision Darryl made 09-10; it confirms Legal is now working the fork he specified.** Still gated on A41 (redline to Brandon Thompson, overdue since 09-11) and C-i3-3 (Legal's five answers). No new action; reinforces urgency on A41. Source: i3 Agreement IP Question, M365 evidence 2026-09-18.

### 2026-09-10 — Sean deck argues velocity and defect burden, not the constraint analysis, and the complex-build capture requirement is confirmed mandatory
- Status: Made
- Owner: Darryl
- Context: slide-by-slide review of the six-page Sean deck. Two things emerged that change the argument rather than the layout.
- **The reasoning behind the resource question, stated directly.** Darryl, 2026-09-10, Confirmed, not transcribed: the motivation for taking on the development team is partly political and partly grounded in the last year and more of development. It has been slow, quality has been questioned by Darryl's own team, and the working view is that part of the problem is the resources' skills, the lack of control, and the team's motivation. Sean already believes results have not been good and Darryl agrees, so the deck defends no one; its job is to give Sean something he can defend upward when he spends political capital.
- **Decision on how hard to argue it:** argue velocity, defect burden and control on the page, and leave the skills argument to the conversation. Evidence selected, all from the record: four major data capabilities re-estimated 2026-08-06 to land 2026-10-08 through 2027-02-03; 29 defects confirmed still open on review 2026-07-30; a historical ADM bug backlog parked without a prioritization decision 2026-07-24; the seven-area data-quality stabilization plan running since the July go-live.
- **Recorded caution, raised and accepted rather than adopted as a page:** the record supports slow and defect-heavy well, and supports a skills claim thinly. The only skills evidence is the ADB-skilled data engineer replacing Vishal; everything else is data quality and upstream completeness rather than code quality. This does not withdraw the 09-09 finding that most blockers sit outside Digital Products. Both are true at once, and the pack carries both while the deck leads with velocity.
- **Serial and MAC capture is mandatory.** Darryl, 2026-09-10: mandatory for complex builds and for the type of networked assets Wesco sells. This settles the requirement; enforcement remains the open item from the 2026-08-19 architecture review. Owners on the page: GPO with Daniel Totino.
- **Manny Tracey and the Level 4 and 5 service and support centers.** Manny Tracey runs all of the sites, the centers are a strategic element for Wesco, and his organization needs the complex-build questions answered. Carried on the deck as a shared note under the two complex-build gates.
- **The two principal hurdles, in Darryl's words:** P360 attributes with their data population, and proper EUDM sync with ADM, where sync covers the completeness defects and the automation question together as one hurdle.
- Structural decisions: six pages; the two concerns move to page 2 on a begin-with-the-end-in-mind basis; the page sorting blockers by what a development team could close is deleted; the benefit moves to the value page; the closing page carries the ask with no blank fields.
- Follow-up: full record and the recorded cautions in `Deliverables/WAM/2026-09-10_Sean_Deck_Revision_Decisions.md`, Revision 3.
- Source: slide-by-slide review with Darryl, 2026-09-10.

### 2026-09-10 — WAM use cases redefined to three, and the Sean evaluation narrowed to the development-resource question
- Status: Made
- Owner: Darryl
- Context: the 2026-09-09 feasibility pack derived eleven use cases from the seven value propositions in the record. Darryl's correction in session: several of those were development-team tasks rather than use cases, and the pack was pitched below the altitude the meeting needs. Separately, Sean's own framing became clear for the first time.
- Decisions taken, all Darryl's:
  1. **Three user use cases, one enabler.** A, license and warranty management, internal sales triggers and lifecycle reporting, user Sales Operations. B, asset lifecycle tracking, meaning purchase history, current orders and status, user Managed Services. C, complex builds, work instruction, parent-child and metadata tracking including serial number and MAC address, users warehouse and field service and the customer. D, API integration to Strev, is an enabler with no direct user; it appears on the data-path diagram as the ADM to Strev connection and gets no further visibility.
  2. **Value to Wesco is shown as reaching it through Sales Operations and Amy Aguirre's Managed Services only.** The customer is the reason those two can sell it, not a third recipient column.
  3. **The evaluation is a single question:** does Digital Products take over development resources from the Platforms team. This replaces the four-option framing (status quo, take development, partial, stop ADM) that the 09-09 pack carried.
  4. **The three EUDM completeness defects and the measurement gap come off the standalone gates page** and are carried inside the use case each one blocks, in business terms rather than as defect codes.
  5. **The data-path diagram's left column is labelled DDP and Other Data Sources.** Darryl first asked for DDP applications, which conflicted with his own direct confirmation of 2026-08-19 that WMX is not a DDP application. The conflict was raised rather than resolved silently, and the 2026-08-19 architecture statement stands unchanged.
- New facts established, Confirmed, Darryl direct, not transcribed:
  - **The development resources are not part of Darryl's organization; they are supplied by the Platforms team in India.** This partially closes gap G2 in the 09-09 pack. Still open: whether that is Merwan Mereby's team specifically, who sets the backlog, and the funding line.
  - **Sean prompted the resource question out of concern that Wesco is not getting good results from the India Platforms team.** Closes gap G1. It names the concern as delivery performance, which is testable against evidence.
  - **Sean separately doubts ADM is recoverable**, on the basis of investment already made and the amount required going forward. This is a second and larger concern, and it is a sunk-cost and forward-cost question rather than a delivery one.
  - **The meeting is Sean and Darryl only.** Closes gap G4. No orientation content and no page built for a third reader.
  - **Warranty data needs to be added to P360**, with Supplier Relations and the supplier feeds populating it. First warranty path in the record.
  - **Asset lifecycle means purchase history, current orders and status**, not end-of-life or refresh signalling as the 09-09 pack read it.
- Risk carried, recorded because it was raised and not adopted as a page: a picture showing only externally held gates can read as blame-shifting to a sponsor deciding whether to keep the program. Mitigated by stating each blocker inside the use case it blocks, including the ones Digital Products owns, rather than by a separate self-criticism page.
- Follow-up: `Deliverables/WAM/2026-09-10_Sean_Deck_Revision_Decisions.md` holds the full record and the open items. Two open items are new and material: no Strev figure exists for the forward-cost half of Sean's recoverability concern, and P360 governance already declined a comparable global-attribute request on 2026-08-10, which is the same body and the same kind of ask that use case A's warranty half now depends on.
- Source: working session with Darryl, 2026-09-10.

### 2026-09-09 — Ford Premier Support SOW: optimization services excluded, on-premises administration placed with Ford, secure remote access made a delivery dependency
- Status: Made
- Owner: Adam Lazare, following team review
- Context: the Ford Premier Support SOW carried scope ambiguity risk (unbounded technical work, unclear administration ownership).
- Decision: optimization services are excluded from base support scope; on-premises user administration is Ford's responsibility, not Wesco's; secure remote access is named as an explicit delivery dependency rather than an assumed capability.
- This reduces but does not close the Ford renewal exposure tracked in `04` — the commercial model (SLA terms, SME-hours treatment, pricing language, guardrails) remains open, targeted for finalization at a 2026-09-09 meeting.
- Follow-up: Chad Steger to validate the delivery team can support everything in scope; Leanne Gordon to draft pricing-model language and preserve an administrative SOW copy with extended view access for Bill Rose, Lindsay Cotten, and Natalie Marquardt.
- Source: `RE: SLA Verbiage (Request for Ford entroCIM support renewal proposal/SOW)` (email), weekly M365 evidence 2026-09-02 to 09-09.

### 2026-09-08 — entroCIM 3.1.12.14 targeted for 2026-10-05
- Status: Made
- Owner: David Blondel
- Context: continuation of the entroCIM quarterly release cadence.
- Decision: target 2026-10-05 for release 3.1.12.14 (Batch Point Writer, Graphic Builder grouping, Tiles-Gridboard text widget, platform maintenance); package release messaging, notes, and possible webinar support around it. Sprint capacity deliberately shifted from Showcase work to testing/QA to hold the date.
- Follow-up: David Blondel to share the release deck and build sales messaging with Valli Poornakumar and Leanne Gordon before 2026-10-05.
- Source: entroCIM Backlog Deep Dive, 2026-09-08 (verbatim transcript).

### 2026-09-03 — WAM asset-upload epic deprioritized in favor of the new data-enrichment interrupt
- Status: Made
- Owner: Akansh Gangil
- Context: a new data-enrichment MVP (shipping data, transaction price from EUDM) was scoped as higher near-term value than continuing the asset-upload epic.
- Decision: deprioritize the asset-upload epic; prioritize the enrichment interrupt while supplier-ID work continues in parallel.
- Source: WAM - Product Backlog Refinement, 2026-09-03 (verbatim transcript).

### 2026-09-01 — WAM data-enrichment MVP scope: shipping and transaction price only, average-price logic deferred
- Status: Made
- Owner: Akansh Gangil, with Violet Moyer's agreement
- Context: the first WAM/ADM enrichment MVP needed a bounded scope to ship against EUDM sales-order and part-number matching.
- Decision: MVP accepts sales order, Wesco part number, and manufacturer part number; returns shipping fields and transaction price with not-found statuses. Average-price logic deferred until requirements are clearer.
- Source: WAM Product discussion, 2026-09-01, and WAM - Product Backlog Refinement, 2026-09-03 (verbatim transcripts).

### 2026-09-01 — Complex-build serial collection: WMX/VAS boundary — **RECLASSIFIED 2026-09-14 from Made to Approaching**
- Status: **Approaching. Not decided.**
- **Correction, Darryl direct, 2026-09-14: "Complex build data capture path has not been decided, it is very much in the air and being evaluated."** This entry was written as a Made decision from a verbatim transcript and was never confirmed with Darryl or Akansh Gangil, despite the entry's own instruction to do so. It then propagated: `05` A1 was marked "very likely answered," `Products/WAM/WAM.md` recorded a decided tool boundary, the 2026-09-09 weekly counted it among five decisions made, and the 2026-09-09 analytics block cited it as evidence the WAM Data Challenges forum was producing decisions elsewhere. All of that rested on an unconfirmed inference. **Darryl's word governs; the path is open.**
- **What is settled and what is not, kept separate:** the *requirement* is settled — serial and MAC capture is mandatory for complex builds and networked assets (Darryl, 2026-09-10). The *path* is not — which system captures, which is the system of record, and how data reaches DDP/EUDM are all under evaluation, now including the 09-11 Strev system-of-record question and with WACT eliminated 09-14.
- **Standing lesson, and this is the second instance.** A transcript stating a position in a meeting is evidence that a position was stated, not that a decision was taken. The entry format asks for a decision-maker, and a named participant describing an approach satisfies that field without satisfying the underlying test. Before logging a tool, architecture, or ownership choice as Made from a transcript alone, get the owner's confirmation, and hold it as Approaching until that arrives.
- Owner: Daniel Totino (position stated); decision owner not yet established
- Context: this is very likely the output of the same-week working session Daniel Totino offered on 2026-08-31 to walk Darryl and Akansh Gangil through his roadmap (`05` A1, open since 07-17). Confirm with Akansh Gangil that this is that session's product before treating A1 as closed.
- Position stated in the session (not a decision): WMX for standard serial collection; VAS governance for project-specific or ad hoc requests that map into the WMX process. Read as a working direction under evaluation alongside the 08-31 position (VAS for complex finished goods, WMX for simplified products) — the final data model (serial-number anchor, parent/room relationship, required attributes, VAS/WMX handoff) remains open between Daniel Totino and Akansh Gangil.
- Follow-up: **A1 stays open** (`05`). The confirmation this entry asked for was never obtained and the 09-09 "potentially closed" marking is withdrawn. Forum: WAM Data Challenges (Darryl-owned, weekly), or the Level 4/5 Services Support Assessment.
- Source: Requirements definition, 2026-09-01 (verbatim transcript).

### 2026-09-01 — CDA operating model: managed service, cameras first, hybrid deployment, customer validation before build
- Status: Made
- Owner: Darryl Benson
- Context: written in the CDA follow-up and materials sent to Chris Mooney and Bill Muczko's teams following the 2026-08-28 executive brief meeting.
- Decision: CDA is positioned as a Wesco-managed service that can be bundled with other Wesco services or sold standalone, with cameras first (Hanwha and Axis connectors already live via entroCIM), a hybrid cloud/on-premises deployment model, and customer validation (interviews, named pilot accounts) required before committing to the estimated eight-month 2027 build.
- This does not commit to the build. See the companion Decision Backlog entry below — the build/pilot question is explicitly still open.
- Follow-up: A37 (set up validation sessions with Suzanne Betterton's team and Bill Muczko's senior directors/GAMs, due 2026-09-02).
- Source: `Connected Device Assurance, follow-up and materials` (sent email), M365 weekly evidence 2026-08-24 to 08-31.

### 2026-09-01 — Warehouse integration system boundary: entroCIM is the reporting front end, not the operational control front end
- Status: Made
- Owner: Darryl Benson and Chad Steger
- Context: a prospective warehouse integration surfaced in the entroCIM Backlog Deep Dive. The question was which system acts as the front end for operational control versus reporting.
- Decision: entroCIM serves as the reporting front end only; it does not become the operational control front end for the warehouse system.
- Follow-up: none named in evidence; revisit if the warehouse integration advances to a scoping stage.
- Source: entroCIM Backlog Deep Dive (transcript), M365 weekly evidence 2026-08-24 to 08-31.

### 2026-09-01 — JCI MSP agreement: final legal markup sent to JCI
- Status: Made / Event confirmed
- Owner: Darryl (confirmed transmission); Brian Miller (Wesco Legal, markup preparation)
- Context: Brian Miller's contract review, rescheduled from the missed 2026-07-31 date to Friday 2026-08-28 (per the 08-26 record), evidently produced a result. Darryl confirmed directly, chat 2026-09-01: "I sent the agreement to JCI yesterday" (2026-08-31).
- This resolves the pacing stall tracked as Register C1 since 07-31 — over four weeks past the original committed markup date — and answers the test set on 08-26: Friday held and produced a deliverable, rather than the negotiation slipping a second time.
- What this does not confirm: JCI's response, its review timeline, or whether the roughly ten additional contractual issues (indemnity, liability carve-outs, unilateral changes, non-cancelable orders, flow-down, competing-offerings restriction) are addressed in this markup or remain open on JCI's side. The markup being sent is a milestone, not contract execution. Wesco continues hosting the Conductor in Azure with no signed contract in place until execution — that exposure is unchanged.
- Follow-up: track JCI's response; open a new Awaited item once/if JCI returns a review timeline. C1 closed as "sent" (`05` Archive — Closed).
- Source: Darryl, direct, 2026-09-01.

### 2026-08-28 — Navigator / entroCIM deck: Corridor design adopted, both versions kept
- Status: Made
- Owner: Darryl Benson
- Context: the deck's diagrams were explored in Claude Design against a self-contained brief. One option came back, "Corridor", with a build spec giving exact inch geometry and orthogonal vertex lists.
- **Decision: adopt Corridor as v2, and leave v1 untouched for comparison.** Both live in `Deliverables/Navigator/`. v2 is the recommended version.
- What Corridor changed: orthogonal routing throughout with a channel between the two panels, replacing diagonals that crossed the middle; four line treatments reduced to three plus a labelled token, so the hand-off is an object that visibly disappears in the end state rather than a line style that stops appearing; dotted reserved slots in the first two frames marking exactly where the later elements land; and a struck-through ghost token where the swivel-chair used to be.
- **Titles rewritten the same day** to Lisa's language, current state / interim state / end state, and to stop titles competing with the headlines beneath them. Rule filed to `Reference/Communication_Preferences.md` §2a.
- **Build-mechanics rulings, filed to `Reference/Deck_Construction_Standards.md`:** a routed connection is one continuous shape, never a chain of line segments; freeform where PowerPoint's elbow connector cannot make the route; connector endpoints verified programmatically against node rectangles before shipping.
- Worth remembering about the tooling: the imported spec contained a real defect, one connection specified clear of both nodes it joined, which the design tool's own render also showed. **Audit an imported spec, do not assume it.**
- Source: Cowork session 2026-08-28; `Deliverables/Navigator/2026-08-28_Claude_Design_Corridor_Handoff.zip`.

### 2026-08-27 — Navigator / entroCIM integration sequence set: interim connectivity before June 2027, API integration after it
- Status: Made (sequence agreed in the meeting; funding and ownership not yet settled)
- Owner: DJ Vaughn (Navigator delivery), Darryl Benson (Product Executive, both products)
- Context: Darryl met Lisa Orton, DJ Vaughn and Chris Askew (Head of IT, Ascent team) on 2026-08-27 on the future of entroCIM and Navigator. DJ, Ron Snyder and Darryl had been discussing integration for several months.
- Decision, DJ's stated sequence: **NavWork MVP complete and UAT begins December 2026; UAT complete and integration/migration begin March 2027; Maximo replacement complete June 2027; in-depth entroCIM integration (API connection) begins after June 2027.** Before June 2027, entroCIM connects to Ascent equipment over the Airwall already at Ascent's St. Louis offices, to build operational familiarity with the Ascent Ops team so that the later integration improves on what Ascent does today rather than replacing something never adopted.
- **The interim step is an operational adoption step, not a partial build of the end state.** Two returns from one action: usable visibility for Ascent Ops inside FY27, and an integration designed against the Ascent operation as it actually runs. This framing is mandatory in the deck; without it the obvious executive question is why two things are being done instead of one.
- **Deck purpose set by Darryl 2026-08-27: explain to executives how the systems work and how they will work together. A picture is worth a thousand words, so the diagrams carry the message and the slides carry a headline plus a few labels. Open tasks and responsibilities are handled in the weekly call and do not appear on the slides.** Design consequence: pages 1 to 3 are the same diagram at three points in time, with node positions held constant so the reader sees the picture change rather than reading three unrelated diagrams.
- Deliverable: Lisa asked for a shared DJ/Darryl slide deck by **2026-09-03** covering four items (current state, interim state, end state with entroCIM and potentially WAM, Navigator quarterly roadmap through 2028 with priority coding, which DJ handles). Register A36. Build specification: `Deliverables/Navigator/2026-08-27_Navigator_entroCIM_Integration_Deck_Build_Prompt.md`.
- **Airwall disambiguation, and it matters:** the unit in scope is the **Ascent HQ Airwall** (arrived 2026-07-21, POC owned by DJ Vaughn, Register B4). It is **not** the FRB SASTEC St. Louis customer device carried in `04` Passive. Two separate St. Louis Airwall threads exist in the record; do not conflate them.
- **Risk of waiting, and it is the sharpest thing on this item:** the whole interim argument rests on B4, which has been open since 2026-07-21 with a 2026-08-15 gate and no confirmed progress in three evidence packages. If the interim step does not run, the June 2027 integration starts cold. The deck should ask for a named owner and a date on B4 rather than describe the interim state as though it is in motion.
- **Assumption, labeled, not confirmed:** there is no funded FY27 line for the interim connectivity work. entroCIM/Navigator integration KPIs were deliberately excluded from the FY27 AOP because no production data flow exists. The interim work sits in FY27 while the integration it enables sits in FY28. Confirm before the deck implies funding exists.
- **Naming resolved same day (Darryl direct): Navigator is the product; NavWork is the software replacing Maximo; NavIntel is the current Navigator front end.** Open: whether NavIntel persists after NavWork lands. DJ to confirm.
- **Confirmations 2026-08-27 PM (Darryl direct), which close two of the three exposures raised earlier the same day:** the Ascent HQ Airwall will be running shortly, so the interim connectivity story no longer rests on an unevidenced POC; funding runs under **current operational funding as a deployment project, with AOP capability next year**, which answers the assumption that no FY27 line existed. Interim connection scope is **metering and building automation**, entroCIM's core competence. **The NavWork API is still being developed**, which is distinct from the integration itself and should not be drawn or described as the same thing. **CDA is shown as an on-premises device** at the customer site, not as a cloud service.
- **Deck scope grew on Darryl's direction:** it must carry the value of the integration, the distinct strength of each package and the strength of them together. Seven pages: title, three-frame overview, three state frames, value, roadmap. Visual vocabulary reused from `Products/CDA/CDA_Exec_Brief.pptx` (slide 10 architecture pattern, slide 7 value pattern, slide 13 timeline pattern) so the deck sits beside the CDA brief rather than importing a second visual language.
- **Tooling call: Mermaid for drafting only, native PowerPoint shapes for the deck.** Mermaid auto-layouts, so adding an edge shifts node positions and breaks the three-frames-of-one-picture principle the deck depends on. Native shapes are absolutely positioned, editable by DJ and Lisa, and inherit the Wesco template.
- Superseded: whether "NavWork" names the whole next-generation Navigator product or its work-management component. DJ's 2026-08-25 email was titled "Navigator 2.0 (NavWork)"; the record holds that the 2027 redesign and the Maximo replacement are the same project. One convention must be set before drafting.
- Forum: DJ Vaughn / Lisa Orton working session on the deck, by 2026-09-03.
- Follow-up: A36 (deck), A30 (same DJ conversation, pitches and metrics), B4 (POC status).
- Source: Darryl direct, 2026-08-27.

### 2026-08-26 — Intel SceneScape proof of concept: not pursued now
- Status: Made
- Owner: Ron Snyder (decision), acknowledged by Ajay Bhat
- Context: entroCIM will not pursue a SceneScape proof of concept at this time, on the basis that there is no clear customer-driven use case and capacity is constrained.
- Decision: hold; revisit if market demand appears. Not a closed door, no active tracking until a customer signal exists.
- Follow-up: none named. Not entered as a register item — no owner action pending.
- Source: `RE: Intel Scenescape`, M365 evidence 2026-08-27.

### 2026-08-26 — SkyPosium 2026: attend with three, Darryl not attending, no presenter submission
- Status: Made (Darryl's side); funding ask to Marketing pending
- Owner: Darryl; Marketing owns the SAR and the response to Finance
- Context: SkyPosium 2026, October 13-14, Park City, Utah. Marketing's Finance-approved SAR is $2,300, registration only, which its own arithmetic implies was scoped at two passes. Travel for three sits in the Digital Products budget. Marketing funded three registrations last year and asked Darryl to justify four. **The material finding is that the SAR does not cover three either, so the gap is against prior-year attendance, not an expansion.**
- Options considered: escalate the four-person case to Finance; reduce to three and absorb the shortfall; split funding across Marketing and Digital Products; drop to two.
- Decision: **ask Marketing for one additional pass to reach three (Ron Snyder, Keith Bishop, Chad Steger), framed as restoring last year's level.** Darryl withdraws his own attendance: it was the most expensive marginal seat (pass plus travel), the weakest against the Wesco-global-supplier-scale objection Marketing predicted Finance would raise, and defending it risked the three seats actually needed. **No presenter submission this year** — no team capacity on top of the migration and the Q3 release. Darryl removed a reference to the accepted NexusCon 2026 slot from the outbound message on 08-26; do not reintroduce it, in this thread or in future SkyPosium material. Capacity is the reason; naming a second conference invites the counter that time and budget for conferences exist.
- Justification basis used: 4.0/Xeto is a migration year (Build 4.0.6 shipped July 2026, migration required; connector and application migration in testing per 08-10, production deployed for early testing 08-12, rollout and training approved 08-17); Woolly and Ion Creator pricing is announced at this event and is an unbudgeted FY27 input; two concurrent tracks plus a staffed tabletop cannot be covered by two people; 4.0 knowledge should not concentrate in one engineer (`04`).
- Deliberately not used: entroCIM revenue scale or FY27 P&L position, which invites the counter that a negative plan cannot fund travel; and the "four in-depth experts" framing, already tried and rejected on 08-25/26 because it makes headcount the criterion.
- Follow-up: confirm actual per-pass price and any partner/reseller rate with the event POC; Marketing to provide tabletop assignment and floor map; decline the Call for Presenters explicitly. Detail in `Products/SkyFoundry.md`.
- **SUPERSEDED SAME DAY, 2026-08-26: attendance is two, not three.** Ron Snyder is unavailable that week (personal commitment). Attendees are **Keith Bishop and Chad Steger**, which fits inside the approved $2,300 SAR. **No additional pass is required and no Finance conversation is needed.** The funding ask is withdrawn, not refused. Everything above is retained because the reasoning still governs next year.
- **The live risk is now precedent, not funding.** Three attended in 2025, two attend in 2026 because of a scheduling conflict, and next year's SAR will be scoped from the 2026 actual unless the reason is on the record. That is the same mechanism that produced this year's shortfall. Darryl's message to Natalia states explicitly that two is a circumstance and not a right-sizing, and asks to be involved in sizing before the next SAR is submitted. **If that process ask is not honoured, the 2027 baseline starts at two.**
- **Secondary consequence, raised and CLOSED same day (Darryl, 2026-08-26).** Ron Snyder carries the deepest SkySpark platform concentration (`04`, standing watch item) and is not getting direct access to SkyFoundry engineering on 4.0. Resolved: Keith and Chad cover the sessions and will communicate to Ron, and **the proceedings are recorded and available for Ron to watch.** No further mechanism required.
- **One thing this creates for next year, flagged now:** the existence of recordings is the obvious argument for cutting attendance further in 2027. It should be answered before it is made. The value of attending is direct access to SkyFoundry engineering, the pricing follow-ups that only happen in person, and the relationship; recordings cover content and none of that. Recorded in `Products/SkyFoundry.md`.

### 2026-08-26 — Register A gets a forced disposition rule and an answered-elsewhere test

- Status: Made
- Owner: Darryl
- Context: A single disposal sweep on 2026-08-26 closed nine Register A items, taking the register from 16 to 6. **Five of the nine were not stalled work. They were questions already answered by another route:** A4 answered by Connected Device Assurance being built and submitted; A9 by the CMP tool staying with Merwan Mereby; A24 by SPA Engine staying with Maddy Taylor; A22 and A25 by the FY27 AOP submission completing on 08-21. Every one had been visible in the daily briefing for weeks under the existing Focus rule.
- Diagnosis, and it is not the obvious one: this is a mechanism gap rather than a discipline gap. The Focus rule surfaces aging Register A items daily, so they were never hidden. **Surfacing an item is not ruling on it**, and nothing forced a ruling. Meanwhile Other-Owned items age out automatically after 14 quiet days, while Register A was deliberately exempted on the reasoning that Darryl is the actor so silence is not evidence. That reasoning is correct for closure and wrong for prompting, and the exemption is where these items lived.
- Decision: two rules added to `05_Commitments.md` under How This File Works.
  1. **Answered-elsewhere test.** The closure check asks whether an item has been answered before it asks whether it has been done.
  2. **Forced disposition at 14 days.** A Register A item 14 days past its date with no movement is surfaced as a three-way question, done / re-date with a reason / kill. No fourth option, no silent carry, and the reason on a re-date is mandatory.
- Note on attribution: Darryl's own reading in session was "I need better discipline about reviewing and closing tasks." The evidence does not support that as the primary cause, and the rules above are written against the mechanism instead. Recorded so the diagnosis is not quietly restated as a personal failing later.
- Follow-up: first test is the next weekly closure check. If items still carry past 14 days after this, the diagnosis was wrong and it is worth revisiting.
- Source: Cowork session 2026-08-26.

### 2026-08-26 — Elevator pitches and monthly soft metrics defined for the four AOP products

- Status: Made
- Owner: Darryl
- Context: The four FY27 AOP products needed a single internal explanation each, plus a small set of non-financial measures reportable monthly. The AOP forms did not provide this. entroCIM and CDA carry Value KPI blocks at a quarterly cadence; **Navigator and WAM carry deliberately blank Value KPI blocks** because both submitted on the Financial Benefits path and the template instructs one of three. DJ Vaughn supplied a Navigator pitch draft on 08-25 with no measurable metrics.
- Decisions taken in session, all Darryl's:
  1. **Internal portfolio use only.** The AOP workbooks submitted 08-21 are unchanged. Nothing here is written back to a form without a separate decision and its own change-log entry.
  2. **Monthly internally, quarterly on the form.** The entroCIM and CDA quarterly commitments stand. The monthly set is the same measurement at a faster tempo, not a second promise.
  3. **Report what is measurable now.** A metric requiring capability that does not exist carries the date it begins rather than reporting zero.
  4. **Four metrics per product**, non-financial, and **none may depend on permission Darryl does not hold** (extends the 2026-08-17 rule on customer-dependent metrics).
  5. **Navigator rewritten to the common standard** from DJ Vaughn's draft. Darryl takes the first draft of the deck back to DJ for input.
  6. **CDA carries FY27 readiness metrics, not service metrics.** First report 2Q27 for all four; the service does not exist before then and the investment is not approved.
  7. **CDA metric 1 (device family qualification) is permanent**, not retired at pilot. Its meaning matures from launch readiness to the supply-side ceiling on expansion. **Metric 3 retires after pilot completion**, not at first connection, so build and performance measures run in parallel through the pilot window.
  8. **The five submitted CDA service KPIs are named on the slide**, with the date they begin, so the internal set and the AOP commitment read as one continuous plan.
  9. **Metric owners stay off the slides** and live in the backing document.
- Content corrections Darryl made to the drafts, all filed as durable product facts: WAM enrichment is performed by ADM **and the Managed Services team**, not ADM alone; MDM and VAS removed from the WAM pitch; complex builds added to the WAM pitch as a key company growth area; entroCIM connects **OT and IoT systems and devices**, not building systems; entroCIM carries planned connections to **WAM, Navigator and CDA**; **CDA is not built on entroCIM** but uses its underlying platform, tools and expertise, and must not read as an entroCIM feature add-on.
- Deliverables: `Deliverables/Portfolio_Admin/2026-08-26_Product_Pitches_and_Soft_Metrics.md` (agreed content), `..._Soft_Metrics_Backing_Document.md` (proposed owners, source systems, open confirmations), `..._Product_Pitches_and_Soft_Metrics.pptx` (five slides on the Wesco template).
- Follow-up: six open confirmations are carried in the backing document, not in the registers, because none has been asked of anyone yet. They become Other-Owned items when Darryl raises them.
- **Deck final 2026-08-26.** Six slides on the Wesco template: a definitions lead-in, one page per product, and a reportability matrix. Format decided across three review rounds and recorded in the working document §6b and §6c: pitch left, metrics right; light box with dark text; hybrid prose and bullets, with bullets held to genuinely parallel facts and the closing value paragraph always prose. Released for circulation; Darryl takes it to DJ Vaughn for Navigator input (A30).
- Source: Cowork session 2026-08-26; DJ Vaughn email "Navigator 2.0 (NavWork)", 2026-08-25.

### 2026-08-25 — Claude Code access standardised on API keys, not individual accounts

- Decision: Wesco AI Council and IT practices require Claude Code access through **API keys rather than individual accounts**, as a best practice. Applies to the entroCIM development project and, by implication, to any Wesco development project using the tool.
- Decision-maker: Wesco AI Council and IT. Stated to Claude by **Darryl, session 2026-08-25**; Darryl is reporting a decision made outside this record, not making it here.
- Options foreclosed: seat-based subscription plans (Team Standard, Team Premium, Max) are individual named accounts and are therefore out of policy.
- **What it costs.** Team Premium seats would have run $3,000 for 5 developers over 6 months against a central API estimate of $5,840, so the practice is roughly $2,840 more expensive over that window, and converts a fixed cost into a variable one. Small in absolute terms and defensible on governance grounds (per-user spend attribution, centrally revocable access tied to AD groups, no personal accounts holding company code, OpenTelemetry export). Recorded so the tradeoff is visible rather than assumed away.
- **What it avoids.** Seat allowances reset on rolling five-hour and weekly windows and a developer who exhausts one stops working until reset. API keys carry no such ceiling, which matters on a dated release path.
- **Consequence that needs an owner:** with seats excluded, nothing caps spend unless a workspace spend limit is set deliberately. ~~Recommended limit $1,460 per month for a 5-developer team, one sixth of the $8,760 recommended budget line.~~ **Figures superseded by the correction below: the recommended Anthropic Console workspace spend limit is $1,000 per month against a $6,050 budget line. Do not use the struck figures.**
- **Open, and it is not a contradiction of the above:** which API-key path is the standard. Darryl's direction is Anthropic Console API keys. The same day's weekly evidence records Claude models enabled for the entroCIM and Ascent teams through **Azure AI Foundry** via the `entroCIM_Ops` AD group. Both satisfy "API keys, not individual accounts," but Console bills direct to Anthropic with workspace spend limits and per-user reporting built in, while Foundry bills to the Wesco Azure account and needs OpenTelemetry or a gateway for per-user attribution. Confirm the standard and the paying budget before a budget line is committed. Route through the existing Claude Code Enablement thread (A28, C18, WAB Claude code Radar entry), not as a new initiative.
- Cost basis established the same session: roughly $195 per developer per month on a Sonnet-primary mix, $290 with contingency. ~~Full estimate in `Deliverables/entroCIM/2026-08-25_Claude_Code_API_Cost_Estimate.md`~~ **(renamed `SUPERSEDED_2026-08-25_Claude_Code_API_Cost_Estimate.md`; current estimate is `Deliverables/entroCIM/2026-08-25_Woolly_Dev_Test_API_Cost_Estimate.md`)**; reusable method and rates in `Reference/AI_Development_Tooling_Cost_Model.md` (v2.0); durable product note in `Products/entroCIM/entroCIM.md`.
- **Do not conflate** with the entroCIM AI (Woolly) commercial position that customers supply their own LLM API keys. That is a product pricing model; this is internal developer tooling. Same phrase, different subject.
- **CORRECTION, same session 2026-08-25, Darryl.** Two things above were wrong when written and are corrected here rather than overwritten, so the trail stays readable.
  - **The Console-versus-Foundry item was not an open governance choice.** **Woolly does not support Azure AI Foundry at this point.** Direct Anthropic API keys are therefore a **technical requirement** for the harness, not a preference that happens to align with the AI Council practice. Both facts in the evidence are true at once: Claude Code runs on Foundry (which is what the `entroCIM_Ops` enablement reflects), and Woolly cannot. Two workloads, two access paths, two budgets. The item is closed as a decision and survives only as "which budget carries the Anthropic spend."
  - **The cost figure quoted above priced the wrong workload.** It modelled developers using Claude Code as a coding assistant. **The API keys are for the Woolly harness making LLM calls during development and test**, which is driven by interaction volume and context size, not developer headcount. Corrected estimate: **$4,030 expected, $6,050 as a budget line, range $2,015 to $12,090** over six months. The developer-assist figure ($5,840, roughly $195 per developer per month) remains correct for what it measures and now sits against the Azure Foundry budget. Superseded memo retained as `Deliverables/entroCIM/SUPERSEDED_2026-08-25_Claude_Code_API_Cost_Estimate.md` with a banner; replacement is `2026-08-25_Woolly_Dev_Test_API_Cost_Estimate.md`.
  - **Consequence worth naming:** because Woolly cannot use Foundry, this spend cannot be absorbed into an existing Azure commitment. It needs its own budget line and owner. Darryl's "at this point" qualifier is preserved: if Foundry support arrives, the separate line goes away.
- Source: Darryl, Cowork session 2026-08-25; `Evidence/M365_Evidence_Weekly_2026-08-25_run2.md` for the Foundry enablement record.

### 2026-08-25 — FY27 AOP: reviewed product P&Ls used for the submission; CDA required no further input

- Decision: the reviewed product P&Ls for Ascent/Navigator, entroCIM and WAM are the basis of the FY27 AOP submission, and CDA needs nothing further.
- Decision-maker: John Erickson, following confirmation from Darryl. Recorded in a Teams conversation, 2026-08-24.
- Evidence: John Erickson stated CDA "is GTG and nothing is needed," and that the three product documents were uploaded to the IT/Digital AOP directory.
- **What this does not confirm: that the AOP submission itself completed.** The evidence covers the P&L basis and the uploads, not the submission. Given the 08-21 date, this is the single open question worth closing first. Raised at the next closure check.
- Source: weekly M365 evidence 08-25 (second run).

### 2026-08-19 — entroCIM AI evaluation scoped away from production and customer data

- Decision: the initial Woolly evaluation runs with no production data and no customer data, on developer machines or a development server.
- Decision-maker: Ron Snyder.
- Why it matters: it is the control that makes proceeding before full approval defensible, and it is the reason the near-term risk on this initiative is low despite the open governance questions.
- Source: `AI Council | Ice Breaker | Discussion on entroCIM AI`, weekly M365 evidence 08-25.


### 2026-08-17 — License-notification assignment logic restricted to ERP 12004 records
- Owner: Akansh Gangil
- Context (ADM connect with Natalie, weekly evidence): duplicate-customer-ID ambiguity was creating risk of misdirected license-expiry notifications. Akansh restricted the assignment logic to ERP 12004 records specifically to eliminate the ambiguity.
- Decision: proceed on the ERP 12004 restriction. Same-cycle, the notification suite plus notification analytics and an upload fix (underscore support in manufacturer part numbers) shipped to production — see `Products/WAM/WAM.md` for full detail and `04` for the updated MVP1 watch row.
- Follow-up: none named. Tactical fix, not a register item.

### 2026-08-17 — SkySpark 4 rollout preparation and training planning: proceed
- Owner: CSS Platforms leadership (CSS Platforms All Hands)
- Context: continuation of the SkySpark 4 migration tracked since 08-04/08-10/08-12 (nearly complete, testing underway, production version deployed for early testing). This cycle's evidence confirms leadership proceeding to rollout preparation and team training planning rather than a new decision point.
- Decision: proceed with rollout prep and training planning. Ron Snyder and Maggie Becker named on training-rollout preparation (`05`, new item).
- Follow-up: none named beyond the standing AI-roadmap thread above.

### 2026-08-12 — entroCIM containerization confirmed as the mandatory future deployment model
- Owner: Ron Snyder / David Blondel (product/architecture); Darryl consulted
- Context (entroCIM Backlog Deep Dive, 08-12): containerization — already advancing under approved CSRA security governance and named as the CDA design direction ("the container is the product," 07-23) — is now confirmed as the deployment model entroCIM moves to exclusively, not one option among several. Same session: Q3 release holds at early October (consistent with the 2026-10-05 date already tracked in `04`); **Q4 has slipped to early 2027** (new — the `entroCIM_Roadmap.md` Q4 2026 slide, last refreshed 07-15, is now stale on timing, not just scope). ServiceNow field-module integration remains blocked, reconfirmed same session.
- This is a customer-facing architecture decision on a 10+ year installed base, not an internal engineering choice — existing on-prem customers will need a migration path and message, and evidence flags a specific downstream ask: "client-facing roadmap clarification requested" for Sales leadership (source: 08-13 evidence package, Potential Executive Communication Needs).
- Decision: proceed on containerization as the sole forward deployment model.
- Follow-up: **customer-migration communication plan not yet commissioned** — no owner named in evidence. Recommend Darryl name one (natural fit: David Blondel/Ron Snyder for technical content, Nathan Kehr/Sarah Monteleone for customer-facing delivery) before this reaches Sales informally. `Products/entroCIM/entroCIM.md` and `Products/entroCIM/entroCIM_Roadmap.md` updated with the confirmed model and the Q4 slip.
- Forum: entroCIM Backlog Deep Dive (bi-weekly).

### 2026-08-06 — EOS reframed around Products/Deliverables as the primary surface; Dashboard cut
- Owner: Darryl
- Context: Darryl assessed the EOS's value as misallocated — the Dashboard unopened for days, the daily brief too dense, while the actual force-multiplier value comes from `Products/` (product knowledge) and `Deliverables/` (ad hoc drafting), neither of which had daily attention or a file-map entry. Full diagnosis in `EOS_Value_and_Purpose_Review_2026-08-06.md`.
- Decisions taken: (1) a pushed daily artifact survives but gets much simpler — the action-tracking closure mechanism itself is being redesigned, proposal pending sign-off (review doc §10); (2) Dashboard cut outright, regeneration removed from `CLAUDE.md`; (3) Team interface to be piloted as a chat capability before any standing file is built; (4) `Deliverables/` reorganized into subfolders by initiative, executed same day; (5) `02_Copilot_Intake_Prompts.md` rewritten and replaced directly, adding Product/Initiative State Signals and Team and Stakeholder Signals as first-class extraction categories — Darryl is running the rewrite and will bring the output back for review.
- This review supersedes the 2026-08-12 pilot verdict scheduled in `10_Pilot_Feedback_Log.md`; no second review needed on the same question.
- **Update 2026-08-06 (same day):** Darryl approved the §10 closure redesign. Implemented: `05_Commitments.md` Register B and C merged into one "Other-Owned" list (Type: Delegated/Awaited, Critical flag, 14-day presumed-closed aging for non-Critical items, new Archive — Aged Out table); `CLAUDE.md`'s Commitment Attribution and Focus Rules section carries the rule. Register A is unaffected.
- **Update 2026-08-06 (same day): core value metric named.** Darryl's own statement: the value he gets is Claude responding well out of the gate to requests about products, communications, or his role, with minimal edits. Added to `CLAUDE.md` Purpose and Optimize For sections, and to the Session-End Rule (draft corrections now explicitly route back into `Reference/Communication_Preferences.md`, `01`, or `Products/`, not just the one deliverable). This is now the standing lens for what the registers/briefings/knowledge base exist to protect.

### 2026-08-06 — i3 Alliance Agreement: Section 8 position set (surgical redline, entroCIM as peer system)
- Owner: Darryl (CSS Platforms), answering Brandon Thompson's Comment 115
- Context: Section 8 ("Data Fidelity, Digital Architecture & System Integration") is the gate to the Preferred and Strategic tiers under Sections 3.5 and 3.6, and it decides whether entroCIM is the system of record on Alliance projects or a downstream consumer of i3's model. The exposure is architectural and commercial, not a risk term, which is why a legal-only read found no issues. Evidence: Section 8 is the only substantive section with zero tracked changes from either party across a 171-change redline (Chuck Knight 132, Brandon Thompson 39), the only one designated non-negotiable, and the only one where i3 asked Wesco to draft the language.
- Options considered: full peer-system rewrite; surgical clause-by-clause redline; the two-edit falsifiable test from the 08-03 review notes.
- Decision: **surgical clause-by-clause redline**, preserving i3's structure and headings. Twelve items: one preamble insertion, seven replacements, one amendment (8.7), four additions (8.9–8.12). No edit touches i3's fees, methodology, tier economics, or role as lead client representative.
- Sub-decisions taken in the same session: i3's integration standards govern data delivered to i3 only, while Wesco's own standards, product requirements, and tagging models govern configuration and integration of Wesco platforms (Darryl's position, stronger than the options tabled); source of truth split by domain rather than by hierarchy; Client Data defined and excluded, with neither party obliged to route data it has no right to route; IP protection located inside Section 8 at new 8.10 rather than by amending Sections 6 or 12; ontology boundary stated twice, at 8.1 and 8.10, deliberately and not to be consolidated; security standard drafted as a relative reciprocal obligation rather than a named framework, to avoid asserting a compliance posture Wesco cannot presently evidence.
- **Negotiation floor:** 8.8 (strike all-or-nothing, bar unilateral expansion), 8.2 (strike the pre-validation bar and "downstream consumers"), 8.4 (domain split plus the right to rely on own records), 8.9 (Project Data and Client Data defined), 8.10 (no derivation plus residual knowledge). Below the floor the recommendation is to decline Section 8 and elect Approved. Deliberately tradeable: the 60-day standards notice (8.3), 10-business-day deemed consent (8.6), 72-hour breach window (8.11), 30-day re-election right (8.8).
- Follow-up: A27 to send; C-i3-1 (Brandon, Section 9.2 conflict), C-i3-2 (Nikos, 8.10 and 6.2), C-i3-3 (i3 diligence questions). Detail in `Products/i3_Alliance.md`; risks in `04`. **Cross-cutting observation worth carrying beyond i3:** in both the JCI MSP agreement (licensing mechanics in unilaterally changeable Program Materials) and here (§8.3 standards documentation, §8.8 Program materials), the operative obligation lives in material the counterparty controls. Recommend a standing review question on any partner or reseller agreement: identify every obligation whose content is set by counterparty-controlled material, and require it to be versioned, attached, or executed. Cheap at draft stage, effectively unfixable afterward.

### 2026-07-24 — UWM entroCIM server migration cutover completed
- Owner: Syed Zaidi / Shawn Clark
- Event: server migration to the new environment is complete; old environment remains live pending customer sign-off before decommission.
- Follow-up: confirm UWM sign-off status (owed to Darryl by Syed Zaidi — see 05); track dual-environment carrying cost/risk until closed. See Key Product Due Dates.

### 2026-07-24 — NexusCon 2026 speaking slot accepted
- Owner: Darryl (presenter), with Nathan Kehr and Sarah Monteleone
- Event: "Overcoming On-Prem Controls Infrastructure Limits by Pivoting to a Cloud-Hosted OT Data Layer" accepted for NexusCon 2026 — external thought-leadership opportunity.
- Follow-up: conference date, registration deadline, and deck milestones not yet in evidence — confirm and add to Key Product Due Dates once known.

### 2026-07-17 — Managed Services optimization-services offering: ownership decided (Nathan Kehr)
- Owner: Nathan Kehr and his team.
- Decision (Darryl, field note 07-17): Nathan Kehr's team owns the Managed Services optimization-services offering for hosted entroCIM clients. Darryl's team supports during the pilot; longer-term direction is to automate parts of the services.
- Context: resolves the ownership gap flagged 07-16/07-17 (packaging, ownership, delivery model undefined for the hosted-client commercialization discussion involving Nathan Kehr, Leanne Gordon, Valli Poornakumar).
- Follow-up: define the support interface/scope for Darryl's team during the pilot; track automation roadmap as it forms.

### 2026-07-15 — Architect role: Shawn Clark internal move; David Blondel owns close-out
- Owner: David Blondel (Chad Steger on paternity leave 07/15–08/11); Darryl ratified.
- Decision: David spoke with Shawn Clark about moving into the architect role. **Update 07-15 PM (Anna Thornton, HR): no Canadian requisition needed — this can be done as a transfer.** Darryl directed Anna to coordinate and communicate details through David B for Shawn, **so Shawn can make his final decision.**
- Remaining: transfer details (Anna → David → Shawn); Shawn's acceptance.
- **Transition scope (Darryl, 07-15): the move includes his current position** — Shawn carries his existing responsibilities (UWM cutover lead, Panama Liberty backup) into the architect role. No succession gap; the watch item shifts to load: architect capacity is nominal until his current duties are backfilled or wound down.

### 2026-07-15 — Supplier attribute governance: ownership split inside the team
- Owner: Darryl (assignment decision).
- Decision: **Akansh Gangil owns the supplier attribute + data-governance track** — rallying the responsible data teams; next working session Jul 16. **David Blondel owns communication and coordination with Jarod Booth.** Darryl's role: executive escalation and involvement only.
- Stakeholders (Darryl, field note 07-15): Daniel Totino (GPO), Inder Gambhir (Global MDM team), Rishi Sanaka (BPM team), Gandhi Subramanian (IT Manager).
- Residual risk: attendance troubles and Akansh's work-hours vs. North American teams; and cross-org *accountability* (beyond Darryl's org) is still not formally named — rallying is not a RACI. Air-cover mention at Thu Sean meeting.

### 2026-07-15 — EOS: dashboard adopted (snapshot-at-briefing + locked HTML template)
- Owner: Darryl
- Options considered: script that parses living docs (rejected — brittle, counts without judgment), local web app (rejected — live re-parsing buys little), Cowork live artifact (deferred), no dashboard (rejected — prototype passed the "changes a decision" test on real data).
- Decision: Claude appends a metric snapshot to `Dashboard/snapshots.json` and regenerates `Dashboard/Dashboard.html` after every briefing. Five RAG indicators, no composite score. Design locked in `Dashboard_Template.html` (settled via Claude Design session, ported to a dependency-free template — the `Pandoc_Ref.docx` pattern). Rules in `Dashboard/README.md`; workflow in CLAUDE.md.
- Follow-up: 3 days of history backfilled 07-13→07-15; trends carry low confidence until ~2 weeks. Revisit at the 30-day EOS review: is it read, does it change decisions, cut if not.

### 2026-07-14 — EOS: Sean reporting via on-demand written updates; analytics and model standards added
- Owner: Darryl
- Decision: Sean progress reporting is on-demand written Teams/email updates (`Reference/Sean_Update_Standard.md`), not a recurring meeting. Added `Reference/EOS_Analytics_Standard.md` (weekly analytics block, monthly pass, quarterly retro), `Reference/EOS_Model_Selection_Standard.md` (Claude model per EOS function), and `09_Impact_Ledger.md` (wins capture).
- Follow-up: first Sean update on request; first analytics block with the next weekly briefing.

### 2026-07-15 — WAM/ALM metrics definition revised to include existing-customer growth
- Owner: stated on the WAM actuals deck (Finance-led with Brad Stevens as Business Sponsor); decision authorship to confirm.
- Decision: original ALM target focused on net-new revenue and was read as new-logo acquisition; the metric now includes incremental sales growth from existing customers using the ALM tool. Under the revised definition: YTD ~$16.7M vs $19M objective (87.23% by June).
- Chief of Staff note: this is the substantive fix to the underreporting problem, but redefinition can read as goalpost-moving at Engel/Hasting level. The narrative must state the rationale explicitly (original metric measured the wrong thing, not performance rescued by re-measurement).

### 2026-07 — Asset/product uploads transition to EUDM-driven processes
- Owner: Akansh Gangil / ADM team
- Decision: Future asset and product uploads move to EUDM-driven processes.
- Source: ADM connect with Natalie (transcript)
- Follow-up: **Correction 07-13 (Darryl via ChatGPT library): DDP/EUDM connection COMPLETED Jul 3.** Remaining work: MDM structures, supplier data, terms, metadata, stewardship, complex-asset sources — these external dependencies increasingly drive scale and timing.

### 2026-07 — Weekly renewal-notification email design finalized
- Owner: WAM product team
- Decision: CSV attachment model plus escalation distribution strategy.
- Source: ADM connect with Natalie
- Follow-up: **Go-live paused pending formatting (Darryl, 07-13); notification function lands in WAM Jul 17.** Backup distribution list needed before go-live resumes. Prior "Jul 9 go-live" from Copilot evidence was stale. **Update 07-16: rollout now tentative 2026-08-03 under the MVP1 release gate (see Decisions Approaching).**

### 2026-07 — entroCIM Q2 release target held at July 20 — **RELEASED, CLOSED 2026-07-22**
- Owner: entroCIM leadership (Ron Snyder, David Blondel)
- Source: Daily Stand Up
- Follow-up: Release week now; go/no-go discipline. **07-17 (M365 evidence, Daily Stand Up 07-16):** two open items surfaced this close to the date — (1) data-table UI standardization approach undecided (Ron Snyder/David Blondel — move away from current MUI pattern vs. hold), (2) Dell PME connector work blocked on external Dell support/credentials. Neither evidenced as release-blocking yet, but both warrant a direct go/no-go check rather than assuming resolution.
- **Closed 07-22 (Darryl, field note): release 3.1.12.13 is complete and approved by Ron Snyder and the DCOE**, confirmed by email from Subhendu Mohapatra. This resolves both the release-outcome silence tracked across three evidence packages (07-20/21/22) and the separate DCOE compliance-hold entry below — that entry's "hold" reading was superseded by the actual approval. Data-table UI standardization and Dell PME connector status not independently reconfirmed; treat as closed with the release unless raised again.

### 2026-07-30 — Panama Liberty BACnet timeout resolved; proceed to submeter onboarding
- Owner: Syed Jamshed Zaidi (call), Scott Dunn (execution)
- Decision: the long-running BACnet connection timeout blocking Panama Liberty is resolved; Syed Zaidi directed the team to proceed to submeter onboarding in entroCIM, with Scott Dunn asked to assist and Shawn Clark/Chris Marva having validated the fix.
- Context: this closes the "unresolved Panama Liberty connectivity issue" that had Shawn Clark tagged as second-closest resource (06_Stakeholder_Map.md) alongside his UWM cutover load.
- Follow-up: submeter onboarding is now the open step, not yet complete. See `09_Impact_Ledger.md`.

### 2026-07 — Docker Hub / EntraSim approved with medium-risk posture; Risk 1660 retained at medium
- Owner: Security review participants
- Source: Cybersecurity CSRA: AEA-1792 Docker Hub - PROD
- Follow-up: Stable; monitor only.

### WAM/entroCIM executive reset framing
- Added: 2026-07-14 (Agile Staff). **Status 07-17 (Darryl): framing complete — being presented today to John Engel.** Darryl will report back if the presentation surfaces anything new.
- Owner: Darryl + **Sean McCloskey** (attribution corrected from Maddy Taylor); Brad Stevens sign-off
- Context: WAM financial-benefits underreporting left negative impression with John Engel and Rob Hasting. "True reset" requested by Sean; interest/pipeline slide question for Friday's Brad Stevens meeting.
- Progress 07-14 PM: pipeline slide approved by Brad Stevens + Nate ($32M, matches Dirk MBR); entroCIM update bullets in Engel deck. **Correction 07-15 (Darryl): that slide covers the entroCIM business only.** WAM financial actuals handled by Finance (YTD ~$16.7M vs $19M objective, 87.23%); Darryl's WAM contribution = completion/summary of the Update slide.
- Risk of waiting: resolved pending today's Engel presentation outcome — watch for any new reaction/follow-up from Engel or Hasting.
- Note: apply Benefits_Realization_Standards — the reset must separate realized capability (Jul 3 go-live) from planned benefits; the original impression likely came from exactly that confusion.

### Strev QA integration path (workaround vs. root-cause fix)
- Owner: Strev/Revnue + WAM engineering
- Risk of waiting: HIGH — blocking testing, SOW release validation, production readiness. Open since at least 2026-07-02.
- Escalated 07-14: Darryl → Sunny Sharma (founder), in-thread. Fix date requested within a day or two; Darryl decides workaround-vs-fix this week once the date lands.
- **Update 07-21 (M365 evidence, single-source, names unconfirmed):** Strev QA environment reported operational and APIM integration initiated (Chandana Buduru, Violet Moyer, with Akansh Gangil). Potentially resolves the blocker, but per pilot closure discipline this is **not** treated as closed from Copilot evidence alone — confirm directly with Akansh before updating status. Same day, a separate Strev-side risk surfaced (see new Watch List entry: invoice/Microsoft-suspension risk) — do not let one thread's good news mask the other's.

### PaaS-02 / entroCIM SSO authentication gap (new 2026-07-21) — **RESOLVED 2026-07-22**
- Owner: IAM/platform teams; Ron Snyder and Babu Papanna in the loop
- Added: 2026-07-21 (M365 evidence — Babu Papanna Teams chat; SAML configuration request thread; Migration Readiness Check meeting 07-20)
- Context: PaaS-02 migration completed successfully, but SSO is not functional on the new environment due to metadata/domain alignment. Part of the broader Quest-to-Azure migration track (Watch List — Sept 1 target, previously "on track"). **Update 07-22 (M365 evidence): specific symptom now evidenced — SAML response returning Username:null.** Narrows the fault to claims/attribute mapping rather than broad metadata mismatch; still no fix date.
- **Closed 07-22 (Darryl, field note): SSO is fixed and working, verified by the team and by Darryl personally.** No fix-date chase needed; downgrade from Watch List.
- Forum: Migration Readiness Check; raise directly in the Darryl–Ron 1:1.

### entroCIM release process — DCOE compliance hold (new 2026-07-22) — **RESOLVED 2026-07-22**
- Owner: unconfirmed — likely Ron Snyder's org and/or Balachandar Murali (DCOE & entroCIM Weekly forum owner)
- Added: 2026-07-22 (M365 evidence — Daily Stand Up)
- Context: evidence states entroCIM release process is on hold pending DCOE compliance evidence and reviews. **Possible explanation for the entroCIM Jul 20 release (3.1.12.13) outcome silence now three consecutive evidence packages running (07-20, 07-21, 07-22)** — worth testing directly with Ron rather than continuing to treat it as a pure evidence-coverage gap.
- **Resolved 07-22 (Darryl, field note): the "hold" read was not a block — release 3.1.12.13 is complete and approved by Ron Snyder and the DCOE**, confirmed by email from Subhendu Mohapatra. See the entroCIM Q2 release entry above (Decisions Made) for the closure record.

## Decision Radar

<!-- GENERATED 2026-10-20 15:00 from Registers/ by Tools/eos_registers.py. Do not hand-edit this section; edit the item files under Registers/ or use the EOS web app. Pre-migration history is preserved verbatim in Archive/2026-10-15_pre_registers/. -->

*Generated view of `Registers/decision/` (tier radar). Radar requires a named forum with a live date; ceiling 20, overflow to Backlog with the reason. Count at generation: 15.*

### 2026-10-20 — Stanford renewal: three licenses back to SkySpark-only, how Wesco supports the roll-back and what happens to the Commissioning App
- ID: D096
- Status: Approaching -- position moved, structure undecided
- Owner: Darryl Benson (Wesco position); Sarah Monteleone (customer call); Nikos Minas with Brandon Thompson (legal view)
- Forum: Internal alignment Tuesday 2026-10-20 (Keith Bishop, Mike Reed, Chad Steger, Sarah Monteleone, Nathan Kehr); Stanford call Thursday 2026-10-22 (Sarah leads); Legal meeting Monday 2026-10-26 08:30 ET (Nikos Minas, Brandon Thompson) (2026-10-20)
- Next action: Tuesday alignment: agree how the roll-back is done, pending Keith's pod-dependency answer and Mike's PO terms
- Context: Austin (Stanford LBRE) asked to roll three licenses back to SkySpark-only. Reason, relayed by Sarah Monteleone from Austin (Teams, 2026-10-19): "There has been reorganization within LBRE, and we've had our budget reduced, so we need to save in certain areas, such as licenses." Term expired 2026-08-31; renewal unsigned.
- Facts stated 2026-10-19 (Mike Reed, email): the three licenses began as SkySpark-only; two came from Altura, which bought them from Alper/BASSG; entroCIM licensing was added in 2023 at no upfront cost with maintenance charged at entroCIM pricing since; Wesco carries SkySpark-only maintenance on UNC Chapel Hill, Piedmont (CMS) and RTI. Renewal price lines (Mike Reed): Site SLA list $32,500, 18% maintenance $5,850; COOLER/Commissioning list $29,900, $5,382; Main Access Point list $29,800, $5,364. Darryl (Teams): "Stanford owns these SkySpark licenses and bought them before we were involved, and we already carry SkySpark-only maintenance on three other accounts."
- **Position moved during 2026-10-19.** Email, morning: "Until that review is complete, I do not recommend offering a SkySpark-only renewal option." Teams, later, after Mike's facts: "On that basis, I am open to supporting the roll-back, and Tuesday should be about how we do it." Also: "We don't know whether Stanford sees it differently. Let's hear their view before we state ours." The 2026-10-19 working-session brief for Thursday was written on the earlier position and should be read with this change.
- Options mentioned: support the roll-back and work the structure (point counts, dev instance, term); hold entroCIM-linked licensing pending contract and OEM review. The .pod delivery line in the 2022 scope (Keith Bishop) describes delivery, not ownership; nobody tells Stanford they lose the Commissioning App until the pod-dependency and PO-terms questions are answered (Darryl, email).
- Information still needed: C73 (Keith: Cx pod dependency, commissioning-report fix date), C74 (Mike: 2022/2023 POs and terms, Phase 2 in writing), C76 (Nikos/Brandon: carve-out, 18.5, PO term versions). Stanford's current PO terms, Article 18.2, give Stanford exclusive ownership of Work Product; 18.4 excludes pre-existing IP; 18.5 limits reuse; the 2022 and 2023 versions may differ (Darryl, Teams; near-verbatim).
- Risk of waiting: Thursday's call happens without an agreed structure, or a statement about the Commissioning App is made that the PO terms contradict. W005 (commissioning report fix) is the other half: Darryl, email: if it is still open Thursday "we have no standing to talk about the value of the app."
- **Update 2026-10-20 (Darryl, direct):** legal meeting moved from Friday 10-23 to Monday 2026-10-26, 08:30 ET, so that Nikos Minas can attend (A68 closed, C76 re-dated). The sequence is now customer call first, legal view second. Thursday's line on the Commissioning App and the scripts stays: the original agreements are under review and Wesco will respond in writing. Any statement on ownership waits for 10-26.

### 2026-10-07 — WAM/ADM reduced-capacity reset: what runs, completes, stops or defers
- ID: D001
- Status: Approaching -- needs decision output
- Owner: Sean McCloskey (final call), with Darryl Benson, Akansh Gangil, David Blondel preparing the plan
- Forum: WAM Leadership Sync (weekly, David Blondel, Darryl attends) or WAM Data Challenges (weekly, Darryl-owned) -- next live occurrence to be confirmed; this is also a candidate for the structured-agenda-register treatment already applied to two other forums (`07`).
- Context: Akansh Gangil quantified an eight-person minimum run model (two data engineers, three backend, one UI, two QA) against 15 current resources and the 19-FTE AOP draft, stating timelines would extend "by a great margin" under it. Darryl, own words, WAM Leadership Sync, 2026-10-05: "Let's talk about how we reset as a team over the next few days, then we can bring that to Sean as our plan moving forward and get his input." See `04` WAM/ADM row, `05` A61.
- Options mentioned: preserve the run team and sequence completion work; pause selected ADM work; extend timelines against the current roadmap.
- Information still needed: final staffing allocation and priority order (run vs. complete vs. stop vs. defer).
- **New input, 2026-10-13:** Sales Operations' October ADM scorecard (Natalie Marquardt) shows the license-notification path in active use: 35 suppliers, 6,927 license parts, 1,337 notification line items, 238 reps. It is the one ADM capability with a business-side consumer reporting monthly use, which argues for keeping it inside the run model. The $697K sales figure in the same deck (North America only, August and September) is not yet attributable to notifications; see `Products/WAM/WAM.md`, 2026-10-13, and `09` 2026-10-13.
- Risk of waiting: roadmap commitments already made may exceed the capacity the team actually has, creating unmanaged customer and stakeholder expectations.
- **Update 2026-10-13 (weekly evidence):** still not ready for the Sean McCloskey conversation. Staffing number and integration-skill mix remain unconfirmed; Akansh Gangil committed to confirm the MuleSoft/current integration architecture and prepare a WAM-limitations slide for Darryl before that discussion (no date stated). Risk direction: increased (see `04` WAM/ADM row, updated). `05` A61 (due 2026-10-10) is now 3 days overdue against this same unresolved output.
- **New input, 2026-10-14:** Akansh Gangil's ADM constraints slide lists six data constraints (trimmed part numbers, null enrichment shipping data, missing license/asset flag and durations, missing serial/MAC, no parent-child, unidentifiable renewal orders). All six required asks sit with other owners (EUDM/UDM, supplier data via Jarod Booth, GPO, VAS). Supports framing the reset as run plus workarounds, with upstream fixes carried as named dependencies on other owners rather than ADM roadmap items. Integration architecture already confirmed 2026-10-05 (ADB to EUDM, APIM to Strev; Darryl, 2026-10-14). See `Products/WAM/WAM.md`, 2026-10-14.
- **New input, 2026-10-14 (Akansh Gangil's written answers, prior week):** team today 15 (6 backend, 2 data engineers, 2 front end, 5 QA); minimum run team 8 (2 DE, 3 BE, 1 UI, 2 QA); Run/Complete by stream DDP 2/3, product development 3/3, Strev integration 1/2. At least 3 ADB people needed to advance DDP, against 2 today and 2 in the run team. Run owners on slide 2 confirmed (Sales Operations owns identifying renewals); Q1 2027 historical-data target withdrawn. Still missing: reconciliation of stream Run (6) to the run team (8), and the priority order of Complete items. Darryl: the integration tools (ADB, APIM) define the skill mix going forward. Options framed for Sean in `Deliverables/Exec_Briefs/2026-10-14_Sean_Update.md` (Run only 8; Run plus DDP 11; Run plus all Complete 14). Forum: Darryl's meeting with Sean, week of 2026-10-19.
- **Update 2026-10-14 (Darryl, review pass on the Sean update):** (1) Akansh's staffing numbers stay out of all Sean material until they reconcile; options carry resource types only, no quantities. (2) **WAM roadmap reconciliation next week** (Darryl, Akansh Gangil, David Blondel) to keep the team on features that are scalable and valuable; staffing per option comes out of it. Joint Teams draft `Deliverables/WAM/2026-10-14_Akansh_David_Staffing_Reconciliation_Teams.md`. (3) Recommendation Run plus DDP is now Darryl's. (4) Decision-rights note: the WAM dev team still sits in Merwan Mereby's Platforms team; the Sean ask is the status of Digital Products taking over WAM development (`05` C63), and agreement in principle on Run plus DDP. (5) Renewal-order flagging starts with Dan Totino (Darryl). (6) Serial/MAC capture: Alan Martin's cross-SBU GPO meeting 2026-10-15.
- **Update 2026-10-15 (daily evidence, Nitin Pandey): capacity assessment still pending, explicitly timed to Shubhayu's return.** Nitin Pandey, explicit: "Once Shubhayu returns next week, I will discuss this further with him and provide a more comprehensive update." Due week of 2026-10-19, consistent with the re-date above and with `05` A61 (not closed -- plan still not delivered). Same phased managed-services delivery question tracked in Decision Backlog below (2026-10-14 entry) -- see that entry for the 2027-01/02 phased dates. Source: WAM/ADM capacity-risk escalation evidence, M365 weekly package, reporting window 2026-10-14 to 2026-10-15.
- **New input, 2026-10-20 (daily evidence):** Nitin Pandey, quoted in the thread (Introducing new functionality for managed services - ADM/WAM email, 2026-10-19): "Chris has indicated the WAM team size may be reduced to seven resources effective January 2027" and "If this change is confirmed, it is likely to have an impact on our planned delivery timelines and overall execution capacity." Darryl Benson, reply: "Let's plan some time to discuss as soon as possible. Feel free to schedule the group as the plan comes together on your side." Seven is below Akansh Gangil's eight-person minimum run model. "Chris" is not identified in the words; do not assume. Nitin's fuller update after Shubhayu's return (filed 10-15) is unchanged.

### 2026-09-09 — WAM complex-build final data model: serial-number anchor, parent/room relationship, VAS/WMX handoff
- ID: D004
- Status: Approaching
- Owner: Daniel Totino and Akansh Gangil
- Forum: WAM Data Challenges (Darryl-owned, weekly) — track "sessions since last decision" per the standing observation in `07`.
- Context: the 2026-09-01 WMX/VAS tool boundary was **reclassified to Approaching on 2026-09-14** (Darryl: the capture path is not decided). Neither the tool boundary nor the underlying data model is settled; treat both as open.
- Risk of waiting: WAM cannot reliably automate complex-build onboarding or retire spreadsheet handling until the model is settled.
- Follow-up: `05` A1.
- **2026-09-30 update:** Akansh Gangil committed (WAM connect transcript, 2026-09-30) to schedule a requirements-definition call next week with Alan, Daniel and Ramesh covering serial/MAC capture, parent-child structure, photos and sales-order linkage. First concrete forum movement since the 09-14 reopening; exact date not yet set. See `05` A1, B90; `Products/WAM/WAM.md`.
- **2026-10-01 update — elevated to a formal cross-SBU effort, hard-dated.** A VAS-WMX-ADM-ALM working session (09-30, 15:30-16:00; Alan Martin, Amber Koons, Sean McCloskey, David Blondel, Akansh Gangil, Darryl Benson) established a cross-SBU effort to eliminate duplicate/conflicting capture of serial numbers, MAC addresses and related asset data across VAS, WMX, ADM and Strev, with consolidated use cases due **2026-10-16**. This is a distinct, higher-level track from the Ramesh/Daniel/Alan requirements call Akansh committed to (`05` B90, still not scheduled as of 10-01) — both feed the same underlying decision. Owner for the consolidated deliverable is not yet named; Darryl is a named participant, not confirmed as owner. Forum: VAS-WMX-ADM-ALM (new, cadence not yet confirmed). See `05` A1; `Products/WAM/WAM.md`.
- **Update 2026-10-05 (weekly evidence):** a follow-up working session is now shown on next week's calendar for **2026-10-08** ("Working Session VAS-WMX-ADM-ALM (maybe STREV)"). Likely the continuation of this cross-SBU track rather than the separate Ramesh/Daniel/Alan call (B90) -- the name matches this track, not that one -- but not confirmed; check attendee list when it is transcribed. The 09-30 session itself was not transcribed at source (isMeetingTranscribed:false), so this update rests on calendar metadata only.
- **Update 2026-10-15 (Working Session VAS-WMX-ADM-ALM, Alan Martin organizer, 11:00 to 12:00; Copilot-derived notes, partial: a 192-second opening recording transcribed, the 3,424-second main recording did not).** No ownership decision reached in the accessible evidence. The session reframed the problem as **data element, business use case, capture stage, responsible role, authoritative application**, and spent its visible portion establishing scope: Cordelia McMillan's data-element and use-case spreadsheet covers **CSS only**; EES and UBS requirements are not validated against it (Stephen Karpinski: they likely collect some elements, not every CSS field applies); legacy (Anixter) UBS captures serial numbers at receipt (John Bartolotti); WMX is already working on serial and MAC capture (Bartolotti, pre-meeting). Whether ADM, ALM or Strev received a defined role, and whether anything was decided after screen-sharing began, is unknown. The 09-30 commitment to consolidated use cases by **2026-10-16** was neither reaffirmed nor withdrawn in the accessible portion; treat as at risk. `05` A1 closed on Darryl's instruction; successor A67 (Darryl), C70 (Alan Martin: EES/UBS validation and the system-of-entry matrix), C71 (Cordelia: the spreadsheet). Forum still has no confirmed cadence or next date; this item remains on the Radar without a forum date, which fails the Radar entry test. Notes filed `Evidence/Meeting_Notes_VAS-WMX-ADM-ALM_2026-10-15.md`.

### 2026-08-28 — WAM integration into NavWork is unscheduled
- ID: D009
- Status: Approaching
- Owner: Darryl Benson
- Forum: the standing weekly call with DJ Vaughn; WAM roadmap ownership sits with David Blondel.
- Context: The integrated end state drawn for Dirk and Sean shows five connections into NavWork. **DJ's published roadmap through Q2 2030 covers exactly one of them, entroCIM. WAM appears in no quarter.**
- Assessment: part of the end state Wesco is about to show executives depends on work nobody has scheduled. That is not a reason to remove it from the diagram, per Darryl 2026-08-28 (DJ is likely not thinking about WAM, and the diagram is where that becomes visible), but it is a reason to get it onto a roadmap.
- **CDA is the opposite case and does not need scheduling.** Darryl, 2026-08-28: once the entroCIM connection to the site exists, the CDA connection is done, because CDA rides the same secure path. That turns CDA from an unscheduled dependency into a consequence of work already committed. WAM has no equivalent free ride.

*Every entry here has a routing forum per `07_Operating_Cadence.md`. Surfaced in the weekly briefing. A decision without a forum belongs in the Backlog below, not here.*

### 2026-08-28 — NavWork facility-data scope: does Q2 2028 duplicate entroCIM
- ID: D008
- Status: Approaching
- Owner: Darryl Benson to raise; DJ Vaughn to answer
- Forum: the standing weekly call with DJ Vaughn.
- Context: DJ's published three-year roadmap puts **"Integration expansion, meters, CM points, MOP data point gathering" in Q2 2028 under NavWork**. Meters and CM points are entroCIM's core competence and are precisely what the interim St. Louis connection delivers.
- **The question, and it is worth asking well before the quarter arrives:** is Q2 2028 NavWork *receiving* facility data from entroCIM, or NavWork *building its own* facility data collection. If the second, the same capability is being built twice inside one portfolio.
- Secondary, lower stakes, same conversation: **Q4 2028 "heat map, scorecard, operational outlook"** sits adjacent to entroCIM's analytics. Worth one question, not an escalation.
- Risk of waiting: the cost of discovering this in 2028 is a duplicated build and an awkward conversation about which one survives. The cost of asking now is one item on a weekly agenda.
- Deliberately kept off the deck. It is a question for DJ, not a slide for Dirk.
- **Reconfirmed open, 2026-09-28 (14-day evidence window):** the same question ("is NavWork receiving entroCIM's facility data or building its own") remains unanswered in the record — logged independently in this cycle's evidence as an open decision owned by DJ Vaughn with entroCIM leadership. No new information, but the standing-open duration is now roughly a month with no forum date attached. Consider raising directly at the next DJ Vaughn weekly rather than waiting for it to resurface again.

### 2026-08-19 — entroCIM AI (Woolly): approval path now named and owned (updated 2026-08-25)
- ID: D010
- Status: Approaching — architecture direction set for the evaluation phase; formal Tech and Tech Review approval not yet sought
- Owner: Darryl, with Ron Snyder (technical/vendor) and Sourav Pradhan (process coordination); sponsor approval owed by an unconfirmed "Shawn"
- Forum: AI Tech Review, routed by Sourav Pradhan, who committed to share the blank intake template immediately after the 08-19 session. C2P follows. This is the named forum the Radar test requires.
> *Returned to the Decision Radar 2026-08-25. It was demoted to the Backlog on 08-19 for having no named forum with a date, which was correct then. The 08-25 evidence supplies exactly what was missing: a named route (AI Tech Review, then C2P), a named process owner (Sourav Pradhan), and a gate list. Radar entry test now met.*

**Update 2026-08-25** (`AI Council | Ice Breaker | Discussion on entroCIM AI`, verbatim transcript, retrieved complete):
- **Woolly is now framed as embedded entroCIM product development, not a one-time proof of concept** (Darryl). This changes what approval is being sought for: a product capability, not an experiment.
- **Gates named:** AI Tech Review → C2P (still required) → sponsor approval → cybersecurity review, plus a SOX-impact check Sourav Pradhan committed to run with Stephen.
- **Evaluation constraints set (Ron Snyder):** no production data, no customer data, developer machines or a development server only. This is what keeps the risk of waiting low in the near term.
- **Commercial model stated:** customers supply their own LLM API keys; Wesco supplies the platform, tooling, and entroCIM-specific skills; AI components expected to carry incremental pricing. Filed as durable product knowledge in `Products/entroCIM/entroCIM.md`.
- **Open architecture question (Ron Snyder, Keith Bishop):** whether Woolly can run against Wesco Azure AI Foundry or a local/internal endpoint, and what an external LLM provider may retain. This is the gating question for Federal Reserve and any walled-off or on-premises customer, and it is unresolved.
- **PARTIALLY ANSWERED 2026-08-25 (Darryl, session), and the answer is the unfavourable one.** **Woolly does not support Azure AI Foundry at this point.** The Foundry half of the question is therefore settled as a current-state No, not merely unresolved. Two consequences follow. **Commercially, the segmentation risk is now live rather than theoretical:** Federal Reserve and other walled-off customers cannot take a capability that requires an external Anthropic endpoint, and no internal-endpoint option exists today. This does not change the near-term evaluation risk, which stays low because Ron Snyder scoped it to dev machines with no production or customer data, but it does change what can be promised in an RFP. Worth checking against the FRB RFP text already drafted (`Deliverables/entroCIM/2026-08-19_FRB_RFP_*`) before anything implying AI capability is submitted. **Operationally, it forces the access path and the budget:** direct Anthropic API keys, on their own budget line, not absorbable into Azure. The local/internal-endpoint half of the original question remains open and is now the one that matters for the secure-facility base. Darryl's qualifier 'at this point' is preserved: this is a current product limitation, not a permanent one.
- **Sponsor attribution resolved 2026-08-25 (Darryl, closure check): Sean McCloskey.** The transcript recorded "Yep, it'll be Shawn"; Copilot resolved it to Sean McCloskey and marked it Inferred; Shawn Clark is a real person in this org, so it was held out of every register until confirmed. Now tracked as **C36** (Awaited, Critical). **Worth noting the rule worked:** the garbling was caught, flagged, quarantined, and resolved by asking, rather than silently written in and later found wrong.
- Context (AI Council \| Ice Breaker \| Discussion on entroCIM AI, 08-19): this is the same Woolly AI evaluation thread already tracked in `04` (AI adoption governance row, four to five concurrent AI workstreams). This session moved it from open discussion to a defined approval path. Architecture: **bring-your-own-LLM-key** (customer supplies API keys, Wesco supplies skills/tooling), deployed in Wesco's Azure environment. Initial evaluation scope explicitly limited to **developer machines and a dev server — production and customer environments excluded.** Framed by Darryl in the session as an ongoing embedded product capability, not a one-time POC. A longer-term, not-yet-scoped thread also surfaced: local small-language-model deployment for customers with strict data-residency requirements (Federal Reserve cited as an example).
- Approval path as stated: completed one-pager (problem statement, benefits, cost/revenue estimate) → sponsor approval → SOX-impact confirmation → AI Tech and Tech Review → later C2P/cybersecurity review before any production path.
- **Two items the evidence names to Darryl are Copilot-Inferred, not stated in his own words: preparing the incremental-revenue estimate for the one-pager, and obtaining sponsor approval from "Shawn."** Per the attribution test, these are not written into Register A — surfaced here as confirmation questions. Separately, "Shawn" needs identity confirmation (name-collision risk against Shawn Clark, whose tracked scope doesn't include an AI-sponsor role).
- Risk of waiting: low this cycle — the evaluation is explicitly scoped away from production/customer environments. Risk rises if the one-pager and sponsor approval stall, since C2P/cybersecurity review and any production path depend on this package clearing first.
- Forum: AI Tech and Tech Review process (not yet scheduled); cross-reference the standing AI adoption governance row in `04` rather than tracking this as a separate initiative.
- Follow-up: confirm with Darryl whether he is taking the revenue-estimate and sponsor-approval actions before either is written to Register A.

### 2026-08-17 — entroCIM FY27: plan is negative across the full authorised revenue range (new)
- ID: D014
- Status: Form updated and submitted on the range; the value-path contradiction is carried deliberately
- Owner: Darryl, with Tom Boss (Finance) and Chris Gazdic; commercial cost-to-serve sits with CSS Sales
- Forum: Tom Boss (rate, capitalization label, Pro-Forma); Barbara Serdeczna (template defects); Brad Stevens and CSS Sales on cost-to-serve.
- Evidence: 2027 entroCIM Profit & Loss (DRAFT), provided by Darryl in session 08-17 as a screenshot. Finance authorised a $5M to $6M revenue range for entroCIM the same day, alongside the $32M to $38M range for WAM.
- **Fact: 2027 plans a loss of $897,778 at -18.0% net margin, and does not break even anywhere in the authorised range.** At $5M net is ($897,778); at $6M net is ($409,962), -6.8%. Breakeven at 48.8% gross margin and the current cost base needs approximately $6,840,403, which is $840,403 above the top of the range.
- **Fact, and the most decision-relevant line in the model: the loss is a sales-cost problem, not a development-cost problem.** Sales cost $2,539,774 is 50.8% of revenue and exceeds gross margin $2,439,080 by $100,694, so the plan is negative before Marketing and DEV. Eliminating the entire DEV line still leaves ($600,694); eliminating DEV and Marketing together still leaves ($100,694). **This is the arithmetic proof of the 08-05 position that reducing delivery capacity in response to a conversion problem treats the symptom.** The CSS Sales headcount-reduction request cannot close this gap, and the $857,052 investment requested on the AOP form is not its cause. Use this when the resourcing conversation resumes with Brad Stevens.
- Trajectory is improving and is the honest mitigation: the 08-05 model showed $4.8M revenue, 47% GM, net ($1,212,954) at -25.0%; this shows $5.0M, 48.8% GM, net ($897,778) at -18.0%. Loss narrowed $315,176, margin improved 7.0 points, on ~80% revenue growth over an implied 2026 base of ~$2,777,778.
- **Decision revised later the same day (Darryl, 08-17): populate the Value KPI block ALONGSIDE Financial Benefits rather than switching paths or leaving the KPI section empty.** Darryl's reasoning: the template says KPIs are not required where a financial case exists, but the entroCIM numbers are not good enough to carry the case alone. Carrying two value sections is a deliberate deviation from the template instruction and a defensible strengthening — if a reviewer challenges the payback claim, the KPI block carries the argument instead of the submission having nothing behind it. This materially reduces the exposure recorded below without giving up the higher priority band.
- **Four Value KPIs written to B26, cadence Quarterly (B27), materialization 12-2027 (B28).** A fifth, operational outcome at optimization engagements (plant efficiency or energy reduction against an agreed baseline, referenced to the Federal Reserve Bank chiller plant), was **removed before submission at Darryl's direction 08-17**: Wesco may not have the ability to share customer results and he will not promise what cannot certainly be delivered. Structural consequence, and the reason this matters beyond one field: the removed KPI was the only one in the customer-participation tier, so **the committed set is now entirely self-measurable from Wesco licensing systems and platform telemetry, with no dependency on customer permission.** The trade is that it was also the only KPI demonstrating value in dollars; the KPI block now proves adoption, reliability and durability, with financial outcome carried by the parallel Financial Benefits section. Principle captured to `Reference/Communication_Preferences.md` §3b. Original set: Set: (1) licensed point utilization, target 80%+, anchored on the Dell deployment at ~380,000 licensed points and ~80% utilization; (2) platform availability and data continuity, measured against the Managed Services service level; (3) functional adoption depth, percentage of sites using 3+ of five core functions (alarming, FDD, KPIs, dashboards, reporting); (4) operational outcome at optimization engagements, referenced to the Federal Reserve Bank chiller plant; (5) installed-base retention and expansion. **The design constraint was measurement access**: entroCIM deploys Wesco-hosted and on-premises, and Arcbeam/VPN give support a path into on-prem but not an automated metrics pipeline, so the KPIs report against a stated coverage denominator rather than assuming portfolio-wide telemetry. Decisions taken: report against stated coverage (no new product scope), name Dell and FRB as reference deployments, availability against the Managed Services service definition rather than a number on the AOP form. **Excluded deliberately:** WAM and Ascent Navigator integration KPIs (no production data flow exists; would be project execution not post-production performance) and AI-enabled analytics (per the 07-24 decision to keep AI out of AOP text).
- **New open item created by the KPI commitment:** portfolio-wide reporting on KPIs 1 to 3 would require on-prem instances to report telemetry back, which may not exist today. Current wording avoids it by stating coverage. If broader coverage is wanted, containerization (the mandatory deployment model per 08-12) is the natural carrier for a reporting agent, and that becomes FY27 scope rather than a reporting convention.
- **Superseded (recorded for the trail): earlier the same day the decision was to keep the Financial Benefits path and the 1-to-5-year payback score as they stand, and flag rather than switch to Value KPIs.** Recorded exposure: the form claims the highest-priority financial category and a 1-to-5-year payback against a submission-year loss that does not break even in range. A reviewer holding both documents will find it. B23 states the modelled loss factually; the mitigation if challenged is the trajectory plus the sales-cost finding. Switching to Value KPIs remains a contained change if the position becomes uncomfortable before 08-21.
- **B18 re-based $1,437,918 to $857,052** (DEV only per Darryl 08-17, plus $164,460 Other IT Expense): 3.50 FTE India x $22 + 3.10 FTE North America x $94, on the form's 1,880-hour basis, labor $692,592. The prior figure was $774,798 or 116.8% above the P&L's 6.60 FTE / $663,120 DEV plan, a 9.55 FTE roster gap. Correction to the 08-05 inference: the intent to exclude COGS was already correct per Darryl's own D18 note, so this is roster staleness rather than a category error, though the roster did carry individuals the P&L treats as COGS/SERV. Scoring B16 moved `$1-5 million` to `< $1 million`. Invalid `M&A` value in Investment Type corrected to `Carryover`.
- **Three defects now confirmed as common to both submissions, not per-file errors:** (1) both P&Ls label capitalization 65% while computing 80%, which points to one shared formula with a stale label — keep tab 2A at the 80% template default until Finance rules; (2) both files' 2B month headers read 2026 while 2A reads 2027; (3) the India rate differs between the P&Ls ($22) and the AOP rate card ($24). One conversation with Tom Boss and one with Barbara Serdeczna settles all three across both files.
- **Pattern worth acting on: both forms carried hardcoded totals that did not follow the resourcing model** — WAM 28.2% over, entroCIM 116.8% over. Two of two. Check Ascent/Navigator before 08-21 rather than assuming it is clean.
- Risk of waiting: four days to the gate. The unreconciled tab 2A roster (still 16.15 FTE against a 6.60 FTE plan) means B18 currently disagrees with what 2A would compute, and B17 In Scope still holds the template's own instruction text pending clarification from Darryl, David Blondel and Ron Snyder.
- **Update 2026-10-06 (Darryl, Sean's FY27 AOP update): the question has moved from the form to the product's future.** Much of the call was spent on products that are not financially successful at Wesco, entroCIM and WAM. Sean and Darryl discussed whether entroCIM has legs to go another year like this without sales at least breaking even, through the large cuts to the team; whether Sales can move the ball in the data center space; and how Nathan Kehr can succeed. Sean asked for the data center value proposition to be articulated: entroCIM's actual ability to move the needle there, what the competition is doing, services enablement, and a challenge to our thinking. Next forum: Darryl with Sean after his PTO, week of 2026-10-19, carrying a briefing deck (`05` A58). Risk home: `04` entroCIM commercial performance row.
- Follow-up: `Deliverables/entroCIM/2026-08-17_entroCIM_FY27_AOP_Change_Log.md`; companion WAM log; cross-reference the 2026-08-05 CSS Platforms 2027 resourcing entry, which this evidence materially informs.

### 2026-08-05 — AMI live connector: restore or stay on simulated data (new)
- ID: D026
- Status: Approaching
- Owner: Darryl / Ron Snyder, with product leadership
- Forum: entroCIM leadership / showcase environment governance (existing `04` row).
- Context: the AMI showcase integration is now covered by simulated points already configured (Jason Ganiatsas). Restoring the live connector would require a locally hosted DCM instance, a new connector, and point rebinding.
- Options: continue with simulated data; invest in local live integration if a named commercial opportunity supports it.
- Information still needed: whether a confirmed sales opportunity exists, and the value of live versus simulated fidelity in a showcase context.
- Risk of waiting: low in the near term. The real risk is either engineering effort spent without commercial return, or a future demo lacking live fidelity at the moment it matters.
- Follow-up: no register item created. This is a decision to hold until a commercial trigger appears, which is itself the decision. Revisit if a named opportunity surfaces.

### 2026-08-05 — FY27 financial assumptions with no approved 2027 budget (new)
- ID: D025
- Status: Approaching
- Owner: Darryl with Tom Boss / Finance
- Forum: entroCIM AOP / eCIM Budget track with Tom Boss and Chris Gazdic.
- Context: Tom Boss stated approved 2027 budget figures are not available and suggested using 2026-based estimates. The entroCIM 2027 AOP request asked Finance for planned revenue, sales costs, and marketing costs.
- Options: adopt a documented 2026-based estimation method with a named approver; wait for formal budget figures (not viable against 08-21); submit ranges with stated assumptions.
- Information still needed: agreed estimation basis and who approves it.
- Risk of waiting: every FY27 business case written in the next two weeks inherits an assumption no one has approved, and each becomes individually challengeable at review. This is a single upstream decision that de-risks three to five downstream submissions.
- Follow-up: Register C16. Recommend settling this before numbers go into any template.

### 2026-08-05 — WAM: align the license roadmap with where the business is actually being sold (new)
- ID: D016
- Status: Approaching — question surfaced, no decision taken
- Owner: Darryl, with Brad Stevens (WAM business sponsor) and Amy Aguirre (commercialization). Sales Operations stake: Debbie Hunter
- Forum: WAM Product Leadership Sync (David Blondel) for the product view; Brad Stevens for the sponsor decision; surfaced in the 08-05 Lisa Orton brief as an open question for Dirk Naylor.
- Context (Darryl, session 08-05): the current external WAM business is focused on supply chain programs, not license management. The license capability originally requested, and the entire arc of the 08-05 Backlog Deep Dive roadmap (license visibility → coverage beyond Wesco part numbers → expiry alerts to the owning rep → complete coverage view), is not what is being sold into those programs today.
- Why this matters beyond product planning: it breaks the evidentiary link between WAM's 2026 attainment and WAM's product investment. $16.7M YTD at 87% is real, but it is being earned through a different motion than the roadmap serves. Presenting attainment as validation of the license roadmap would repeat, in a new form, exactly the realized-versus-planned confusion that produced the original Engel/Hasting benefits impression.
- Direct consequence for the FY27 submission (A19, due 08-21): the WAM business case cannot rest the license investment on 2026 attainment. A reviewer can reasonably ask what the license capability has produced commercially, and the honest answer today is that the first governed renewal signal reaches Sales Operations this quarter and has not yet been converted. Decide the answer to that question before it is asked.
- Second consequence: Sales Operations expectations were set at Senior Director level (Debbie Hunter, 07-16) on the license notification capability. If the revenue is in supply chain programs, that audience may not be where the commercial return sits, and the notification launch is being judged by a stakeholder group adjacent to the actual business.
- Options, as framed: (a) bring the license capability into the supply chain program motion, making it a component of what programs sell; (b) let the roadmap follow the demand and re-weight toward supply chain program needs; (c) run both, which is the current de facto position and the one that most needs to be chosen deliberately rather than by default.
- Information still needed: what supply chain programs are actually buying and which WAM capabilities they consume; whether asset and warranty coverage (in flight this year) is the natural bridge between the two; Amy Aguirre's commercialization read.
- Risk of waiting: the FY27 case is written on a roadmap the market is not currently buying, and the gap is discovered at review rather than declared by Darryl.
- Follow-up: cross-reference `Products/WAM/WAM.md` framing correction (08-05) and `Products/WAM/WAM_Roadmap.md`, which is the license-track roadmap rather than the complete WAM plan.

### 2026-07-23 — New product concept for AOP 2027 funding proposal
- ID: D017
- Status: Approaching — initiative in Phase 3/4 (funding package and AOP intake)
- Owner: Darryl
- Forum: Sean 1:1 (concept endorsement), then BU/AOP process.
- **REGISTER CORRECTION 2026-08-05.** This initiative has run since 07-23 with **no Register A row**, appearing only in the weekly Key Product Due Dates, which is a generated view and not a register. The daily briefing, which is driven by Register A, has therefore been silent on Darryl's most active workstream for two weeks. Corrected: **Register A22** created 08-05. Root cause: the initiative was tracked here in `03` as a decision with rich phase detail, and the "single home per fact" rule was read as licence not to also carry the *action* in `05`. The rule separates decisions from actions; it does not exempt an action from the register. Worth checking whether any other `03` initiative carries the same defect.
- **DATE UNDER CHALLENGE 2026-08-05.** The recorded AOP input deadline is **2026-08-31** (Darryl, 07-23), with a backward plan of concept freeze ~08-14, Sean endorsement week of 08-17 (obtained early, 07-28), BU/AOP package ~08-28. The 08-05 FY27 AOP email sets **2026-08-21** for the products Darryl is assigned, including "a new product under discussion." **Inference, not confirmed: that new product is CDA.** If confirmed, the ~08-28 package target loses its seven-day buffer and lands on the same day as the entroCIM and WAM submissions. Note the concept freeze is **not** at risk: Checkpoint 2 closed early on 07-28 via Sean's endorsement, three weeks ahead of its ~08-14 plan date, which is what makes the compression survivable. Resolve the date with John Erickson before further package work. See the 2026-08-05 AOP scope entry above.
- **Governing documents (07-23 PM):** three files in `Products/CDA/00_Charter/` (Updated Ideation Thesis, Cowork Master Prompt, Joint Execution Plan) now govern the initiative. They supersede `Deliverables/2026-07-23_New_Product_Ideation_Charter.md`, the addendum/workplan deliverable, and the first ChatGPT prompt draft. Working thesis: **Device Lifecycle Assurance** managed service; firmware assurance as candidate wedge, not presumed winner. Initiative workspace: phase folders + `05_Operating_Record/` (Source_Index, Risk_and_Dependency_Log, Research_Log) — working detail only; this entry remains the master record.
- **CHECKPOINT 1 DECIDED 07-23 (Darryl): shortlist confirmed as recommended.** Umbrella adopted: **Connected Device Assurance as a Service**. Modules A (Firmware+Config Assurance, 3.75) and B (Remote Health+Recovery, 3.65) advance to Phase 2 together; Module C (Refresh/EOL) embedded as commercial signal, not sold standalone; Module D (Cyber-Hygiene) initially held — **amended same day (Darryl): D promoted into Phase 2 deep-dive scope.** Rationale: cyber is table stakes; major OT/IoT industry gap; multi-vendor deployments leave unowned risk. Reference point: Nozomi Networks Arc (competitor/analog/possible partner). Phase 2 distinguishes hygiene *visibility* (candidate MVP table stakes) from hygiene *remediation* (later sequencing); build/partner/buy assessed per capability gap (incl. SecuriThings/Viakoo as partner-vs-compete question). Basis: `01_Phase_1_Divergence/Consolidated_Shortlist.md`. Note: ChatGPT Phase 1 run skipped the divergence contract (no pain inventory/concept portfolio); divergence covered by Claude first pass — recorded as known limitation.
- **Update 07-23 PM (Darryl, corrected same day): "The container IS the product."** Product ships as a container; three deployment modes (refined 07-23): on-prem SFF Ubuntu PC, on-prem customer server, or fully remote (Azure container over Airwall L3 link, no on-prem compute). Arcbeam (entroCIM) connects/clusters distributed instances; Airwall also provides secure remote management of on-prem instances. Pods = internal entroCIM capability, not packaging. Basis: entroCIM containerization investment underway (CSRA-approved Docker work). Governing docs amended (Thesis + Master Prompt). Build/partner gap: container estate/fleet management. Phase 2 verify: containerized Airwall, Nozomi licensing, Navigator packaging rights, Arcbeam clustering readiness (Ron Snyder), SFF hardware.
- **Update 07-23 PM: ChatGPT Phase 2 dossier received and reviewed** (`02_Phase_2_Dossiers/`). Content strong; recommends **Connected Camera Assurance** MVP (hygiene visibility base + health/recovery primary + Axis-first firmware; Mode 3 land, Mode 1 expand; Hanwha qualifying). Two corrections by Claude (`Phase_2_Review_Timeline_and_Architecture.md`): (1) dossier's Aug gate dates unrealistic — gate actions reframed as the *content of the funded 90-day validation* (Oct–Dec 2026), pilot Q1–Q2 2027; thin pre-AOP lane defined (incident-data pull, Arcbeam/Ron Snyder conversation, pilot shortlist, RFI drafts). (2) Architecture diagram rebuilt per Mermaid standards (executive overview + controlled-action sequence). Citation-verification pass pending in Claude research track.
- **Update 07-27 (Darryl): product decomposition defined after Ron/David read-out (supportive, low feedback).** Three tiers → three containers: **A Cyber-Hygiene (Base) = partner on-prem agent** (host-based sensor, Nozomi-Arc profile, API-integrated — resolves the module-D build/partner question: partner senses, Wesco integrates and service-wraps); **B Base Wesco Connected Device Assurance tool** (entroCIM: connectors, DB, UI, API; health checks, validation, escalation, evidence, alerting incl. partner findings); **C Advanced Wesco Configuration Assurance tool** (entroCIM: firmware tracking/management, config status, telemetry, maintenance scheduling, lifecycle planning). Filed as Thesis amendment. **Sean high-level review moved up to 07-28 — objective: endorsement.** Slide narrative to be drafted from this structure.
- **Rulings 07-27 PM2 (Darryl, slide feedback):** (1) Slide 4 fit statement includes **entroCIM-enabled services** alongside WAM and Navigator. (2) Dossier §14 MVP language adopted verbatim in the narrative (pilot promise + profile). (3) Structure diagram: "Containerized Service Node" with four elements incl. **Navigator components (future)**; **two secure connections** — Airwall link (*manage the remote devices*) and **Arcbeam clustering** (*run entroCIM devices from the Wesco cloud*) — durable architecture semantics, now in diagrams and mermaid. (4) Sean ask = buy-in to proceed with AOP. (5) **CDA AOP justification uses the entroCIM "Risk of NOT Doing" format** (07-24 deliverable); its final bullet was the deliberate unnamed landing pad for CDA — claim it; audience-calibration rule applies (entroCIM = sustain, CDA = growth).
- **Rulings 07-27 (Darryl):** containerization repositioned as deployment/internal strategy, NOT product strategy — outward story leads with value proposition and feasibility. Data-fidelity ladder: partner discovers → C holds verified models, validates via direct device integration → C manages firmware; B may carry partner data only where integration incomplete. Base tier = partner sensor + Base entroCIM pod (B is the service-provider interface); Advanced tier = C. Navigator: connect when present; position CDA in support of Navigator's 2027 redesign integrations (mandatory framing; filed to Products/Navigator/Navigator.md). Slides: "partner sensor" only, no vendor names, no pricing.
- **07-27 PM5 (Darryl, value-prop language):** "Single platform for managing device firmware" and "one platform and interface for your Wesco firmware" — the consolidation argument vs. per-OEM tool sprawl; ties service to distribution relationship. Filed to Sean narrative talk track; carries into Phase 3 value-proposition and AOP language.
- **07-27 PM4 (Darryl, deck refinement):** cloud-enabled service is confirmed; the **fully-remote deployment (no on-site compute) is downgraded to a research/validation item**, not a decided capability — consistent with the dossier's §7.6 Mode 3 technical constraints. Slide language: "Fully remote option: research item." Also: three named service lines added to the fit slide (WAM → Intelligent Asset Management Services; Navigator → Ascent Data Center Services; entroCIM → Intelligent Facility Management Services); offer slide retitled "Connected Device Assurance Services - Platform"; ask moved above the timeline.
- **Rulings 07-28 (Darryl, node stack composition — Cowork session):** (1) **Sensing = Guardian container on the node**, local capture of the device segment (SPAN/tap); entroCIM integrates via Guardian's local API on the node; raw traffic stays on site. **Arc is NOT on the node** — repositioned as optional attach on customer serviceable hosts (VMS/badge servers), reporting into the node's Guardian. Rejected alternative recorded: Arc-at-edge to cloud Guardian (weaker sensing, breaks self-contained node, streams traffic off-site). This amends the 07-27 tier-A "Nozomi-Arc profile host agent" language: the sensing base is Guardian-class, which changes partner economics (appliance/throughput licensing, not per-endpoint). (2) **RMM is in the node stack** as a supporting element, not a central character: monitoring-as-a-service built into every node sold, OS patching, remote support, staged container-update execution; NinjaOne default candidate (category leader, Ubuntu agents, prior operating experience), selection in validation; RMM channel must ride the Airwall path or be documented explicitly. (3) **Container image distribution = Wesco Docker Hub service** (being enabled now); displaces the dossier's K3s + Azure Arc + Flux recommendation, which was never adopted and is not a team capability. Supporting doc: `02_Phase_2_Dossiers/RMM_Category_Review_2026-07-28.md`. Deck updated same day: slide 4 node stack now includes RMM; appendix added (partner sensing/Nozomi + RMM); backup `CDA_Sean_Review_Deck_backup_2026-07-28.pptx` in folder. Nozomi partner questions sharpened: Guardian container licensing for Wesco-provided nodes, multi-customer terms, Arc attach licensing, API version stability (logged in ideation Research Log).
- **07-27 PM3: full 5-slide Sean deck delivered** (`03_Phase_3_Funding/CDA_Sean_Review_Deck.pptx`, checksum-verified in folder): why-now / offer with data-confidence ladder / structure with containerized node + both links / portfolio fit (WAM, Navigator, entroCIM) / plan + ask. Speaker notes embedded per narrative, incl. verbatim pilot promise.
- **CHECKPOINT 3 OUTCOME, 07-28 (Darryl): SEAN BOUGHT IN.** Endorsement to proceed to the AOP obtained at the 07-28 review. MVP composition as presented (Connected Camera Assurance under the CDA umbrella) treated as confirmed by the endorsement — Checkpoint 2 closed. **Brad Stevens named Business Lead (Business Champion) for the business case.** Next artifacts: Wesco Business Case (in progress, cyber-first framing per Darryl 07-28), then the intake form; "IOP" gate referenced by Darryl, timing unknown — clarify.
- **Scope ruling 07-29 (Darryl): CDA covers the full IoT compliance wrapper**, not just oversight and remediation. Basis: SPARC/VOI white paper (commissioned by SPARC/VOI, authored by Cody Remmington of Wesco; Brad Stevens sits on a SPARC board) argues the compliance wrapper — intake, classification, approval, oversight, retirement — is the necessary foundation and that tools underperform without it. **Cody's team may deliver the process/consulting portion as professional services.** Strengthens "why Wesco": process plus platform plus managed service, which point-tool vendors cannot supply. Guardrail retained per the paper: the customer keeps policy ownership, asset ownership, and risk acceptance; Wesco helps design and operate the process, not own the governance. Analysis: `03_Phase_3_Funding/SPARC_White_Paper_Proof_Point_Analysis.md`.
- **Gate A progress 07-29 (Darryl):** Managed Services for CDA will **likely sit in the Sales organization**; Darryl meets the sales team 07-30 to confirm placement. Darryl is himself one of the resource managers for the investment, so the business case does not claim resource managers are unengaged. Closes the "who does the work" question Sean raised, pending confirmation.
- **Data-use provision 07-29 (Darryl):** business case nonfunctional requirement revised — customer device/posture/lifecycle data may be used to deliver the contracted service **and to enable connected Wesco services (WAM/IAMS, entroCIM-enabled services, Navigator) plus Sales refresh recommendations, under the customer agreement**. Original "no secondary use" wording would have prohibited the lead-in model. Protections retained: no sale, no third-party disclosure outside the delivery chain, de-identified benchmarking only. **New dependency: Legal review + matching customer and partner agreement language.**
- **Sean requirement 07-28 (post-endorsement note):** the business case must explicitly answer six questions — identify risk, monitor risk, manage upgrades, execute upgrades, **who does upgrades**, why us — in the description and carried through the whole document. Investment Description restructured to that chain. **Note: "who does upgrades" is Gate A (Managed Services owner function, still unnamed). Sean asking it is the prompt to close it — needs a name before the business case is submitted.** Darryl 07-28: execution is **Wesco or a Wesco partner** — Managed Services owns the service and SLA, delivering directly or via qualified partners under Wesco process, approvals, and evidence standards; accountability stays with Wesco either way. This preserves the delivery-partner model (Ascent precedent) without diluting ownership.
- **Ruling 07-28b (Darryl): CDA positioned as the LEAD-IN service for the CSS digital portfolio.** It establishes the secure connection, verified inventory, and operating relationship other services build on: integration with WAM enables Intelligent Asset Management Services; the same connection and device intelligence extend into entroCIM-enabled services (Intelligent Facility Management Services). Land-and-expand: contained cyber engagement first, portfolio expansion without a second discovery or onboarding. Must appear in the initial value statement.
- **Ruling 07-28 (Darryl): value focus shifts cyber-first** — under-managed/unmanaged devices, firmware currency, status, cyber posture degradation, device discovery, vulnerability. The business case leads with cyber and risk posture (health, security, staying current); commercial/accountability framing supports rather than leads.
- ~~**Next gate: Checkpoint 2 — MVP composition freeze (~08-14).**~~ Closed 07-28 via Sean endorsement. Sequence: ChatGPT Phase 2 run using the standalone `00_Charter/CSS_Platforms_2027_Phase_2_Brief.md` (created 07-23 PM after the first run against the older Master Prompt section missed the mark — decided state now consolidated in one brief) + Claude cited research → merge → Darryl selects MVP composition (modules, deployment modes, manufacturers).
- **Update 07-23 PM (Darryl, Phase 0 Q&A):** (1) **AOP input deadline: 2026-08-31.** Backward schedule: Checkpoint 1 ~08-01, Checkpoint 2 (freeze) ~08-14, Sean endorsement week of 08-17, BU/AOP package ~08-28. (2) Launch manufacturers: Hanwha + Axis (cameras), Dormakaba + HID (access control), Cisco (IT equipment); plus device-inclusion rule — open telemetry protocol + available API puts a device in play. (3) **Firmware-rights dependency reclassified:** per-vendor qualification hurdle, not a concept-level gate (market precedent: third-party solutions exist); formal Supplier Relations/Legal outreach deferred, resolved per vendor during Phase 2 validation.
- **Strategic driver (Darryl, 07-23 — internal only, never in outbound artifacts):** the goal of this entire project is to define a new tool to build for 2027 that assures his team stays intact and delivering value for Wesco. Team continuity through funded, valuable work is the underlying objective; outbound framing stays on customer/commercial value.
- Context: Darryl has been challenged to propose new product ideas for the CSS Platforms portfolio. Ideation charter and first pass drafted (Cowork session 07-23): `Deliverables/2026-07-23_Ideation_First_Pass.md` (first-pass scores not comparable to new scorecard; re-score at merge).
- Options considered: firmware assurance service (lead, scored 32/40), device cyber-hygiene service, install-base refresh/EOL intelligence, remote device health monitoring, productized Airwall access.
- Recommended path (first pass): staged "Device Lifecycle Assurance" service line — firmware-assurance MVP (Airwall + Azure entroCIM pod, 2–3 camera lines, first revenue 2027), expanding into WAM-fed refresh intelligence (hardware pull-thru) and later hygiene/monitoring modules. Audience sequence: Sean first, then Dirk/AOP.
- Risk of waiting: AOP 2027 cycle timing; concept needs research validation (competitive scan, firmware redistribution rights, Airwall commercial terms) before a funding conversation.
- Follow-up: phased joint workplan agreed 07-23 (`Deliverables/2026-07-23_ChatGPT_Addendum_and_Joint_Workplan.md`) — Phase 1 diverge (ChatGPT run + Claude merge → shortlist), Phase 2 deep dives + Claude competitive research → concept freeze, Phase 3 funding package → Sean 1:1, Phase 4 AOP submission. Checkpoint outcomes logged here. Make-or-break gate to start immediately: manufacturer firmware redistribution rights (informal supplier-relations/legal question, don't wait for Phase 2).

### 2026-07-20 — WAB approval for Claude code — AI-enabled assortment/QPM tooling
- ID: D028
- Owner: Prasada / Maddy (per Loop notes)
- Forum: Digital Products Portfolio Review.
- Added: 2026-07-20 (M365 evidence — Digital Products Portfolio Review)
- Context: Portfolio review flagged a task to take Claude code through Wesco Architecture Review Board approval "this Friday or next Friday" to enable assortment-tool and QPM usage, with possible board showcase.
- Risk of waiting: AI-enabled assortment/QPM development slips if approval isn't sequenced against the named Friday target.
- Note: distinct WAB approval track from the JCI API-connection WAB item above — do not conflate the two Architecture Review Board items.
- **Update 2026-08-25 (Darryl, session).** Two things this thread was missing now exist. **Access path is settled at policy level:** Wesco AI Council and IT practices require API keys rather than individual accounts (logged under Decisions Made, 2026-08-25), which forecloses seat-based plans. **A cost basis now exists:** roughly $195 per developer per month on a Sonnet-primary model mix, $290 with contingency, method and rates in `Reference/AI_Development_Tooling_Cost_Model.md`. Neither changes the WAB approval question itself, but both remove reasons a reviewer could send the package back. **Corrected later the same session:** the API-key-path question is not open. **Woolly does not support Azure AI Foundry at this point**, so direct Anthropic keys are technically required for the harness; Claude Code separately does run on Foundry, which is why the `entroCIM_Ops` enablement and Darryl's direction are both true. **What remains unrouted is narrower and still unowned:** which budget carries the Anthropic spend, given it cannot ride the Azure envelope; and whether anyone sets model policy for the automated Woolly test suite, which on the corrected model is 56% of interaction volume and the only line with no human deciding each call. Recommend both at the Digital Products Portfolio Review alongside the WAB item rather than as separate threads. Note the cost figure in the sentence above was superseded within the session: it priced developer coding assistance, not harness runtime. Corrected Anthropic API budget line is $6,050 for six months; see `Deliverables/entroCIM/2026-08-25_Woolly_Dev_Test_API_Cost_Estimate.md`.

### 2026-07-16 — JCI (Johnson Controls) MSP agreement — drive to signature
- ID: D019
- Status: Approaching — stalled on the agreement, momentum restored at account level. MSP model decided (not reseller) 2026-05-26; final markups blocked on unresolved technical/commercial questions. 07-17: 07-15 meeting transcript received and ingested — it was a JCI-initiated FY26 review / FY27 growth partner meeting, not a negotiation: none of the 5 blockers or contractual terms were discussed; no contract commitments made. New evidence from it: (a) JCI's account team described the MSP metering model assuming Wesco continues running/provisioning its own Conductor, with only a read-only license-usage agent added — verbally supportive of the self-host position, not contractual; (b) MSP billing = monthly in arrears on provisioned licenses (vs 12-month prepay today); (c) Wesco's Conductor/relay Azure migration is already in flight (2 Conductors, HA) — execution is running ahead of contract, sharpening urgency to paper hosting rights; (d) 443-only connectivity available now, removing the top deployment friction. Full outcomes: `Products/JCI_Partnership.md`. 07-17 PM corrections (Darryl): Wesco is hosting the Conductor as of today; the internal prerequisite is now specific — Wesco Architecture Review Board (WAB) approval of the JCI API connection (metering agent) from the Conductor, not a hosting-model review. Babu Papanna has no JCI/Conductor actions. HA failover is Wesco IT responsibility inside Wesco's Azure IoT subscription (resolved 07-17 PM) — JCI L3 is optional support, not a required engagement. Brian Miller refresh email SENT 07-17; meeting committed week of 07-20 (agenda: hosting redline, 5 open items, new terms, customer flow-down, markup schedule). Framing correction from Darryl's sent email: legal review ongoing since early June, Darryl owed Brian a response — the quiet period was partly Wesco-side. Hosting responsibility settled operationally (07-17 PM): Wesco is the hosting authority — environment owned by Wesco, application owned by Darryl's team; patching/backup/DR/SLA/security addressed. Sole open matrix element: JCI's support obligations to Wesco (L3/escalation/SLA), still owed by JCI. Value-thesis correction (Darryl, 07-17 PM): the deal's value is the whole MSP licensing flip (consumption billing), with hosting as the enabling change — signature condition now two-part: express hosting rights AND licensing mechanics codified in durable agreement text (not unilaterally changeable Program Materials).**
- Owner: Darryl (driving). JCI: Jonathan Gutierrez (sales/account lead, per evidence), Jeffrey McCorvey (account manager, per evidence), Priya Agarwal (MSP program, per evidence) — roles unconfirmed beyond evidence. Wesco Legal: Brian Miller.
- Forum: No standing forum currently in `07_Operating_Cadence.md`. Recommend Darryl establish one (JCI check-in with Gutierrez/McCorvey) once 07-15 meeting outcomes are captured.
- Added: 2026-07-16 (Darryl, via chat). Detail filled 2026-07-16 (M365 evidence ingestion — see `Products/JCI_Partnership.md`).
- **Update 07-22 (Darryl, field note): Brian Miller meeting held** (calendar showed "JCI Legal review - restart," no transcript retrieved by M365 evidence — field note fills the gap). Walked the full agenda: (1) hosting rights redline — expressly permit Wesco to host/manage the Conductor and MSP infrastructure in Wesco Azure, JCI limited to API-based license monitoring plus authorized support access; open question whether the existing "Non-Hosted JCI Offerings" definition covers this or new language is needed, and whether it belongs in the agreement body or the Order exhibit; (2) reconfirmed status of the 5 open items (hosting rights, API/license-monitoring data scope, customer agreement requirement, final MSP pricing, named JCI counsel contact); (3) new-terms position on indemnity, liability carve-outs, unilateral changes, non-cancelable orders, price-increase notice — flagged where Wesco accepts, counters, or needs Darryl's business input; (4) customer-contracting terms — JCI Customer Agreement flow-down and the termination-for-convenience prohibition, assessed against Wesco's standard customer terms, with the point that in Wesco's hosted model customers never interact with Airwall directly, so the customer-terms structure needs to accommodate that; (5) target markup schedule and what's needed from JCI. **Outcome: Brian will have a final markup ready to send to JCI next week.**
- **Update 07-24 (M365 evidence): markup target date now specific — 2026-07-31.** See Key Product Due Dates.
- Context: JCI's Airwall / Conductor / Relay product set connects Hosted entroCIM to customer-site systems and equipment, enabling live telemetry. Relationship momentum slipping per Darryl.
- **Update 2026-07-17 (agreement review summary, provenance unconfirmed):** the draft's Hosted vs Non-Hosted JCI Offerings structure may support a Wesco-hosted model but does not expressly grant Wesco the right to host/self-manage the Conductor or Relays — blocker #1 is now a confirmed drafting gap. Review also surfaced ~10 additional contractual issues (flow-down, unilateral changes, indemnity, liability carve-outs, non-cancelable orders, competing-offerings restriction, etc.). **Sharpened decision: does Wesco make express Azure self-hosting rights (JCI limited to API license monitoring + Wesco-authorized support access) a condition of signature?** Prerequisite: Cloud Architecture validation (unconfirmed). See `Deliverables/2026-07-17_JCI_Airwall_MSP_Agreement_Review_EOS_Update.md`.
- Options considered: (1) push JCI now for the 5 outstanding blockers (Azure hosting rights, API/license monitoring, customer agreement requirement, JCI counsel contact, pricing) and target signature on the current draft; (2) escalate through JCI account leadership if response lag continues; (3) hold at current stall — not recommended, see risk.
- Decision / Recommended path: Re-engage Jonathan Gutierrez + Jeffrey McCorvey this week on the outstanding blockers; in parallel confirm with Brian Miller whether legal issues are now limited to hosting + customer-agreement language, and confirm status of the Wesco Cloud Architecture review that was supposed to receive JCI's hosting proposal.
- Risk of waiting: Hosted entroCIM's site-connectivity path (live telemetry) depends on this partner stack; continued drift leaves the agreement unsigned indefinitely and weakens the Managed Services delivery story.
- Follow-up: Full detail, contacts, and dated next-steps list in `Products/JCI_Partnership.md`. Darryl to supply 07-15 meeting notes via `08_Field_Notes.md`.
- **Update 07-28 (M365 evidence, "Re: API Detail" thread): the WAB/API technical path sharpened.** Babu Papanna specified concrete requirements for the Airwall Conductor API/metering-agent access: static public IP allow-listing, an Azure NSG/firewall change scoped to a single REST endpoint, and TLS certificate validation. Darryl asked Babu Papanna and Shawn Clark directly to confirm whether this needs Azure Front Door, a static source IP, and what infrastructure/security changes are required — that confirmation has not landed yet (Register C14). Once confirmed internally, the outstanding ask to JCI (static IPs, API origination details, port/NAT/rate scope) still needs to go out — do not treat this as already sent. This is detail on the existing A6/C8 WAB submission path, not a new decision thread.

2026-10-19 (Darryl, web): - Sent Jeff some dates to have a joint meeting with Legal this week on Friday.

### WAM data challenge remediation approach
- ID: D024
- Status: problem-definition sessions active; no remediation decision yet. Update 07-23 (M365 evidence, WAM Data Challenges 07-23 08:00): first forward motion — session moved from problem definition toward AI/data-filtering POCs, AI Council review, and asset-data ROI focus. Darryl committed to review the AI pilot with Shawn and present it to the AI Council; Nitin Pandey's team to run small POCs on automated part identification; Neil asked for a direct benefits/ROI report on WAM. Darryl also owes: sharing the automated-part-ID output with the team, and discussing a needed license with Shawn and Merwan.
- Owner: WAM leadership group (Darryl chairs the forum)
- Forum: Hold — Problem Definition & Brainstorming WAM Data Challenges (weekly, Darryl-owned). First session (out of many) with concrete deliverables — watch whether the next session ships them or resets to discussion.
- Risk of waiting: data foundation is the recurring theme under most WAM risks; workshops without a decision deadline can run indefinitely. Downgraded slightly — this session produced named next steps and owners rather than another discussion-only pass, but none of it is a remediation decision yet.
- **Update 07-24 (M365 evidence): direction sharpening — deprecate third-party classification APIs, pursue an IDP + semantic-search + supplier-data-enrichment approach instead.** Owner for Council approval: AI Council / Keyur Patel / Shubhayu RoyChoudhury (per evidence; roles unconfirmed). Darryl owes: reconnect with the IDP team on expanding extraction capability, and review AI Council prep materials before the approval meeting (Nitin Pandey asked for this). No date evidenced for the approval meeting — flag as TBD in Key Product Due Dates. Separate team risk surfaced same session: large historical ADM bug backlog parked without disposition, and single-point dependency on Natalie Marquardt for supplier-data collection — both worth a capacity/ownership conversation, not just a data-strategy one.
- **Update 07-30 (M365 evidence, Hold - Problem Definition & Brainstorming: WAM Data Challenges, 08:00-08:30): still no remediation decision, but leadership scope sharpened again.** 29 bugs remain open (some prior "bugs" found resolved or not actual defects on review); major new functionality has not started. Named deliverables this cycle: quarterly roadmap deck with "big rocks" (David Blondel / Akansh Gangil), publish the big-rocks feature list in Teams (Akansh), design the Rhombus IDP integration with fallback mechanisms and present to Balasubramanian K (Akansh), evaluate a short-term AI/ADM item-classification approach (David/Akansh), obtain taxonomy terms and filtering criteria from the governance team (Akansh), and a prioritized WAM automation list from Akansh to Nitin Pandey's automation team (Sangram, Rajesh). Staffing: replacement for Vishal (ADB-skilled data engineer) — candidate finalized, offer expected (Nitin Pandey). **Third consecutive session with named deliverables rather than discussion-only — watch whether the roadmap deck actually ships next cycle.**

### Renewal-notification attribution model
- ID: D023
- Owner: Akansh Gangil
- Forum: ADM connect with Natalie.
- Options: continue manual attribution vs. automate via future DDP linkage.
- Risk of waiting: manual effort accumulates; low near-term risk.

2026-10-19 (Claude, session): Raised again by its owner, now as a request to Darryl. ADM connect with Natalie, 2026-10-13, Akansh Gangil: "We definitely have to do something about this renewal, automatic renewal marking because... It's not humanly possible... to keep doing this manually. We have to figure out a way with Dan. I'll talk to Darryl." Renewal metrics reported to sales management depend on it. Pulse P034. Source: `Evidence/M365_Evidence_PulseP2_2026-10-19.md` (transcript).

## Decision Backlog

*Generated view of `Registers/decision/` (tier backlog): raised, not yet routed to a forum. Count at generation: 78.*

### 2026-10-15 — Quest/Azure decommission: approve $245/hour T&M for secure data-removal validation (new, Decision Backlog)
- ID: D037
- Status: Approaching, unforumed
- Owner: Unclear. No named decision owner in evidence for approving the consultation spend.
- Context: secure data-removal validation on the Quest-to-Azure decommission requires a $245/hour time-and-materials consultation; a new cost gate on top of the already-tracked Quest exit inventory (`05` B81) and distinct from the migration-completion risk tracked in `04` (Quest-to-Azure migration, Passive).
- Risk of waiting: the decommission cannot close out cleanly (data removal unvalidated) while Quest hosting keeps running month-to-month (`03` Decisions Made, 2026-09-14); commercial exposure is the $245/hour rate itself and the timing of its approval relative to that recurring spend.
- Why Backlog: no forum or date named for approving the spend; owner not yet named either.

### 2026-10-14 — Confirm the WAM/ADM phased managed-services delivery plan and change-control implications (new, Decision Backlog)
- ID: D036
- Status: Approaching, unforumed
- Owner: unclear. Nitin Pandey supplied the dates; no named executive owner for confirming or committing to them.
- **Corrected 2026-10-14 (full thread read):** the plan is the asset functionality for Managed Services (asset upload, Asset Grid), re-estimated after Data Enrichment was accelerated; a delivery-team estimate to Akansh, not an executive commitment. Shown to Sean as January and February targets held until the roadmap reconciliation. See `Products/WAM/WAM.md`.
- Context: today's evidence names a two-phase production plan for WAM/ADM managed-services functionality -- core capabilities 2027-01-04 through 2027-01-08, remaining scope 2027-02-10 through 2027-02-12. Nitin Pandey stated major priority or scope changes could alter these dates. This intersects directly with the still-unresolved WAM/ADM reduced-capacity reset (Decision Radar, above; `05` A61) -- the phased dates assume a staffing and scope baseline that reset has not yet settled.
- Risk of waiting: portfolio leadership and Managed Services may treat these as committed executive-facing dates before the capacity reset confirms the team can deliver them, and before change-control is agreed for scope changes.
- Why Backlog: no forum or date named for confirming the plan.
- **Update 2026-10-15 (daily evidence): still unconfirmed; next update explicitly timed to Shubhayu's return.** Nitin Pandey, explicit: "Once Shubhayu returns next week, I will discuss this further with him and provide a more comprehensive update." Impact assessment on the phased dates (core capabilities 2027-01-04 through 01-08; remaining scope 2027-02-10 through 02-12) remains pending; due week of 2026-10-19. Still no named executive owner for confirming the plan. See `03` Decision Radar (WAM/ADM reduced-capacity reset, above) and `05` A61, both carrying the same due window.

### 2026-10-12 — entroCIM European client-facing commitments: write-back, certifications, data residency, support coverage (new, Decision Backlog)
- ID: D044
- Status: Approaching, unforumed
- Owner: unclear. Raised to the Europe team by Darryl; cross-functional security, legal, architecture and support agreement required.
- Context: Darryl's review of the Europe team's deployment-strategy document (v0.1, 2026-10-09) and the client-facing deployment framework (2026-10-12) raised four unresolved points: default write-back position, EU data residency/GDPR/NIS2 positions, certification scope for hosted entroCIM, and support coverage hours for European clients.
- Risk of waiting: Sales may use the new Wesco-Hosted-standard deployment framework (Decisions Made, 2026-10-12, above) before these commitments are actually approved.
- Why Backlog: no forum or date; owner not yet named on any of the four points.

### 2026-10-12 — Approve or revise the Strev QA hosting charge (new, Decision Backlog)
- ID: D043
- Status: Approaching, unforumed
- Owner: Amy Aguirre / Strev, with Robert Cooke as finance approver
- Context: a $36,000 annual QA hosting charge has no direct-cost detail or prior written approval behind it; challenged explicitly 2026-10-12. Darryl recommended carrying only the $36,000 production hosting charge in the Meta BIR until the QA charge is supported and approved; Robert Cooke's approval is still pending as of this evidence.
- Options: approve as quoted; request a direct-cost breakdown first; decline and keep QA on a different basis.
- Risk of waiting: BIR and AP processing stay exposed to an unsupported recurring cost; part of the same fragmented Strev contract/quote/invoice picture already tracked in the WAM Azure hosting entry above.
- Why Backlog: no forum or date; Amy Aguirre's next step (request a direct-cost quote or explanation) has no date stated in evidence.

### 2026-10-07 — Confirm the Ford system-audit schedule and subsequent upgrade plan (new, Decision Backlog)
- ID: D045
- Status: Approaching, unforumed
- Owner: Tim Scott (schedules the audit) / Chad Steger (coordinates resources once scheduled)
- Context: upgrade recommendations on the Ford account are deliberately paused until the October system audit runs (Decisions Made, 2026-10-06, above). Audit date and secure access path are not yet established.
- Risk of waiting: renewal value and upgrade recommendations stay paused the longer the audit goes unscheduled.
- Why Backlog: no date on the calendar yet.

### 2026-10-07 — CDA delivery organization in TSS: owner not yet named (new, Decision Backlog)
- ID: D038
- Status: Approaching, unforumed
- Owner: Not yet named. Emily Munk (Director, Strategic Initiatives, Global CSS HO/TSS) asked to identify who in Greg O'Brien's organization would own it.
- Context: CDA has a business sponsor (Bill Muczko) and go-to-market support, but no accountable delivery/support owner inside TSS. Darryl emailed Emily Munk, 2026-10-07 (`05` C65), on Nathan Kehr's suggestion, asking her to identify the owning organization, positioning and approach to bring to Greg O'Brien. This is distinct from the separate, already-tracked Backlog item on CDA service-hours pricing validation (2026-09-29 entry, below) -- that is a cost question once a deliverer exists; this is whether one does.
- Options mentioned: existing TSS team absorbs it; a newly named delivery/support function; another operating home.
- Information still needed: Emily Munk's assessment and Greg O'Brien's organization design.
- Risk of waiting: CDA cannot become an accountable managed service without a named operating owner; the commercial model (pro forma, pricing) continues to assume TSS delivery without confirmation.
- Why Backlog: no forum or date; reply awaited (Inferred -- no verbatim acceptance from Emily Munk in evidence).

### 2026-10-05 — WAM Azure hosting and DevOps ownership: Wesco-owned vs. continue on Strev (new, Decision Backlog)
- ID: D042
- Status: Approaching, unforumed
- Owner: IT leadership; specific final approver not named. Amy Aguirre is the pressing stakeholder.
- Context: a priced quote arrived to migrate WAM Production/QA hosting from Strev Azure to Wesco Azure with ongoing Wesco DevOps management. Surfaces alongside the Zapier/API-documentation decision above -- both are "what does Wesco own vs. Strev" questions on the same vendor relationship, and should be decided together where practical.
- Risk of waiting: delays environment-migration planning and the operating-model clarity Amy Aguirre needs to plan around.
- Why Backlog: no forum or date; IT decision not yet recorded.
- **Update 2026-10-07 (daily evidence): the question widens from hosting alone to the full Strev cost/contract picture.** Strev questions meeting, 2026-10-06: recurring platform costs described as business-funded, IT-funded ADM/API work meant to stay distinct, but invoices, entitlements and contract language are not reconciled across Amy Aguirre, Senthil Govindaswamy, Sunny Sharma, Kristina Isagunde and Tom Boss. Amy Aguirre, direct: "I have to sit down with Sunny and Christina to understand that"; Darryl, direct: "please invite me to that." Kristina Isagunde's 2026-10-06 commitment to send the revised amendment and current entitlement pricing "tomorrow" was missed as of this cycle (`06` Kristina Isagunde). Recommend one reconciliation session covering hosting, invoices and entitlements together rather than the two threads separately. Still Backlog: no forum or date set for that session yet.

### 2026-10-05 — Ford DPR funding model: consume remaining SME hours or create a separate PO/SOW (new, Decision Backlog)
- ID: D041
- Status: Approaching, unforumed
- Owner: Chad Steger, with Ford/account stakeholders
- Context: Ford's redesigned DPR file-processing flow requires SFTP retrieval from GSECHUB, which entroCIM does not currently support. Ford's prior agreement expired 2026-09-30; a renewal PO is pending. Chad Steger has open discussions with Keith (scope/lift estimate) and Atif (options).
- Options: (1) absorb the SFTP build in remaining SME hours; (2) require a separate PO/SOW before starting.
- Risk of waiting: work could start without funding, or the Ford file-processing change could be missed while the funding model is unresolved.
- Why Backlog: no forum or date yet; LOE estimate not complete.
- **Update 2026-10-07 (daily evidence): a staged action plan is now in place, ahead of the funding decision itself.** Chad Steger (with Keith Bishop, via Atif) to identify technical options, Ford's questions and Ford-side dependencies, due 2026-10-09; Leanne Gordon to turn that into draft requirements and confirm with Ford through Adam Lazare and Atif, due 2026-10-16; Adam Lazare to obtain Ford's GSECHUB cutover date and written acknowledgement that the work draws on SME hours; Chad Steger to provide the effort estimate once requirements are confirmed; Leanne Gordon to send the final SOW for signoff. The funding question itself (SME hours vs. separate PO/SOW) is not yet decided and still has no forum or date -- stays Backlog. All five steps are Implied (Darryl directing the team by email), routed to Other-Owned as Delegated, not Register A. See `05` Other-Owned (new rows), `04` Ford row (updated).

### 2026-10-02 — CDA enterprise pricing construct alongside the per-site packages (new, Decision Backlog)
- ID: D039
- Status: Approaching, unforumed
- Owner: Darryl Benson, with Bill Muczko as sponsor
- Context: at the 2026-10-02 sponsorship review Peter Ferrell said the per-site packages work as a land offer but enterprise deals will be negotiated: banks with thousands of branches under ten cameras each, flexible device counts as estates change, partner-level engagement, possibly an enterprise license; "Kroger's not going to pay you 10 bucks a device times 60,000." Bill: each location needs an appliance, so a site needs enough devices to justify one. Sridhar Loke: pricing reads as cost-plus; market size and willingness to pay may need more work.
- Why it matters: it tests two settled positions, the published held fee (2026-09-29) and one appliance per site. Small sites were already the weakest economics in the model (about 85 percent fixed cost).
- Options: (1) keep per-site packages only and negotiate discounts deal by deal; (2) add an enterprise agreement (volume tiers or enterprise license) on top of the per-site build; (3) add a small-branch delivery pattern served from a regional collector rather than an appliance per site (entroCIM's Dell pattern), priced per device or per branch.
- Information still needed: willingness-to-pay evidence from the first anchor conversations; whether a regional collector can reach branch devices securely at acceptable cost; volume terms on the per-node vendor stack (Nozomi, NinjaOne, Airwall).
- Why Backlog: no forum or date; the first steps are design and evidence.
- **Update 2026-10-05 (weekly evidence):** still unresolved; this is the same tension the weekly evidence package logs as "CDA sponsor, launch beachhead, enterprise pricing, service levels, and FY27 AOP position" (open, owner: Bill Muczko as sponsor, portfolio/AOP approval owner not fully named). No new information beyond the 10-02 session -- confirms this is a standing open question, not a one-meeting artifact.

### 2026-10-01 — Finalize the entroCIM commercial agreement model (new, Decision Backlog)
- ID: D046
- Status: Approaching
- Owner: Nathan Kehr and Darryl Benson named as approvers for parts; final accountable owner not stated
- Forum: entroCIM Support SLA Finality (new, cadence TBC; met 2026-09-30, not transcribed at source). (2026-09-30)
- Context: the 09-25 Ford Support Services Agreement (separating baseline Maintenance & Support from a scoped Services agreement) is being generalized into a standard contract stack — agreement components, pricing revision tied to entroCIM list price, an SME-hours scope template, warranty/commissioning-rework limits, and formal training options — for use across renewals, not just Ford. Leanne Gordon: "please add any other ones that I have missed... I would suggest using the Ford documents as a baseline." No individual document owners assigned yet.
- Risk of waiting: renewals proceed on inconsistent agreement terms; margin leakage and uneven customer commitments.
- Follow-up: assign document owners, approve the SME-hours template, identify near-term renewals lacking a governing agreement. See `Products/entroCIM/entroCIM.md`.

### 2026-10-01 — WAM Zapier app and API documentation site: accept the Strev SOW, take the docs site only, or continue on Strev's app (new, Decision Backlog)
- ID: D040
- Status: Approaching
- Owner: not named. Amy Aguirre raised it and carries Strev add-on funding (Darryl's 2026-09-17 boundary); Chris Gazdic made the prior decision not to invest; Darryl is convening the review.
- Context: Strev SOW dated 2026-09-24 (supersedes v2.0, 2025-10-07) and quote REV-2609-00053: $15,000 one-time plus $10,000/year, 12-month commitment, quote valid to ~2026-10-23. Quote and SOW disagree on trigger/action counts (26/28 vs 30/35). Copilot evidence: Zapier on the roadmap since at least 2025 for branding/control; Wesco holds Zapier licenses and a security/VMO approval (Chris Gazdic, May 2026); no evidence of current production use.
- Options: (1) continue on Strev's Zapier app; (2) accept the SOW in full; (3) docs site only, priced separately.
- Information still needed: current use of Strev's Zapier app; scope of the existing licenses and approval; whether the "Summary" actions invoke StrevAI; decision owner and funding source.
- Risk of waiting: quote lapses ~2026-10-23 (re-quotable; low cost of lapse).
- Why Backlog and not Radar: review meeting being scheduled by Darryl; no date yet.
- **Update 2026-10-05 (weekly evidence):** Strev's SOW is now fully priced ($25,000 year one: $15,000 one-time + $10,000/year, consistent with the 10-01 figures) and a Wesco hosting-migration quote arrived alongside it (Strev Azure to Wesco Azure, DevOps management, separate open decision below). Darryl convened the reassessment meeting mid-week; it slipped once on attendee availability and was rescheduled to Monday 2026-10-05 (`05` A55). Quote still valid to ~2026-10-23.
- **RESOLVED 2026-10-05.** The rescheduled Monday reassessment meeting ran and settled it: no change, Wesco does not fund the $25,000 SOW; the Strev-run app continues, business-funds-if-branded. See Decisions Made, 2026-10-05 (WAM Zapier), filed late during the 2026-10-13 reconciliation. Remove at the next Backlog review pass. The docs-site-only sub-option was not separately addressed and is not currently being pursued.

### 2026-09-29 — CDA per-site economics at the $94/hour delivery rate: validate service hours, or reprice
- ID: D047
- Owner: Darryl Benson, with TSS or whoever is confirmed to deliver the service
- **Resolved the same day by repricing (Darryl, 2026-09-29): "I believe $14,000 is too low for large," Inputs row 40 set to 1 so the fee is derived cost-plus at the 40 percent target. With the BOM sourced, indicative fees become $8,201 / $12,866 / $20,989 and all three sizes earn 40 percent. The service-hours question is not closed, it is simply no longer load-bearing for margin: validating the hours now moves the fee rather than the margin. Two new questions take its place, both in `Products/CDA/CDA.md` under v3.5: Small sites at about $17 per device per month, and per-node vendor software at roughly $1.8M a year by 2031 on list-level placeholders.**

- Context: pro forma v3.4 raises the service-delivery rate from a derived $58.51 to $94/hour, the unburdened budget rate for North American resources (Darryl, 2026-09-29). People cost now dominates the annual cost to serve, about 77 percent at a Large site. Per-site gross margin at the published fees falls to 36 / 31 / 22 percent against a 40 percent target, the cost-plus reference fee for a Large site rises to $18,269 against a published $14,000, 2031 gross margin falls to 28 percent, cash break-even moves to 2031, peak cash to -$2.7M, and Cisco turns loss-making across the plan.
- The decision: validate the placeholder service hours (1 / 2 / 4 per site per month, never tested) or reprice to the new cost-plus reference. Doing both without evidence would over-correct.
- Recommendation: validate the hours first. Four hours a month per site is generous for a largely automated monitoring service with remote remediation, and repricing on an unvalidated hours assumption sets a published fee that is hard to walk back. Burden on the $94 rate is also not yet applied, so the cost basis may move again.
- Risk of waiting: the deck and the pro forma both carry a 22 percent Large-site margin. That is the number a finance reviewer will challenge first, and it understates the offer if the hours are wrong.
- Why Backlog and not Radar: no named forum with a live date carries this today. It belongs in the walk-through of the pro forma with Bob Caprise and Bill Muczko (`05` A51).

### 2026-09-28 — Approve "Run + Complete" as the WAM/ADM 2027 planning basis
- ID: D049
- Owner: Sean McCloskey / AOP leadership
- Context: `ADM_2027_AOP_Questions_Answered 1.pptx` (7 slides, complete) proposes a "Run + Complete" framing for WAM/ADM's 2027 position: scale the working foundation, close targeted asset/history/automation gaps, and preserve permanent operating capacity, with any "Expand" scope treated as separately funded. This is a recommendation from David Blondel and Akansh Gangil, not yet an approved staffing or funding decision.
- Risk of waiting: the AOP may underfund either core development or durable product operations if the planning basis is not confirmed before resourcing decisions are made.
- Why Backlog and not Radar: no named forum with a live date is evidenced for this approval; the AOP review cadence that would carry it is not confirmed in `07`.
- **Update 2026-10-05 (weekly evidence):** leadership sign-off on the WAM 2027 pro formas, KPI plan and 12-month forecast was still outstanding as of today; original sign-off request dated 2026-10-01. This is the approval this Backlog entry is waiting on -- track together, not as two separate items. Separately, WAM leadership this week narrowed near-term capacity to DDP integration, core ADM development and required Strev integration only (`03` 2026-10-05, Inferred) -- consistent with "Run," not yet confirmed as the approved "Complete" scope.

### 2026-09-28 — ADM enrichment implementation approach: Java or ADB
- ID: D048
- Owner: unclear — Krishna, Bala and Praveen named as required contributors, no single accountable owner
- Context: the ADM data-enrichment implementation path is undecided between a Java-based approach and an ADB-based approach. Load, performance, and architecture criteria are unresolved.
- Risk of waiting: delays the 2026-10-30 enrichment commitment referenced in the ADM 2027 AOP material.
- Why Backlog and not Radar: no named forum with a live date carries this question today.

### 2026-09-18 — CDA business sponsor: Bill Muczko nominated, acceptance pending
- ID: D053
- Status: Approaching
- Owner: Darryl Benson (ask); Bill Muczko (decision)
- Forum: Darryl's sponsorship email to Bill, Bob Caprise copied (drafted 2026-09-18). No decision date; promote to Radar when Bill responds or a meeting is set. (2026-09-18)
- Context: CDA is the only FY27 product without a named business sponsor. Sean McCloskey (09-15) and Nathan Kehr (09-18) have each set a real sponsor as the bar before CDA advances. Bob Caprise (Senior Director, Sales, CSS) confirmed on 2026-09-18 that he believes Bill would accept a nominated-sponsor role, and that CDA aligns with Bill's goal of moving sales from pick-pack-ship to advanced services.
- Options: Bill accepts as sponsor; Bill supports but declines the formal role (then Chris Mooney is the fallback candidate); no sponsor yet, and CDA holds at validation.
- Why it matters beyond the title: a sponsor is the integrator for the three CDA commercial threads (Converging Technologies pilot accounts, data-center/TSS, Axis per-camera fee with Kroger), which should become one story before Sean or Chris Gazdic sees them separately. It also answers the committed-sales-partner condition Sean set on 09-15.
- **Evidence added 2026-09-19:** the August 2026 enterprise Digital Product List (`Products/digital-products-portfolio-aug26.pptx`) prints CDA's Business Sponsor as "?". Every other Invest product names a sponsor or an org-level owner (GPO, IT driven). The gap is visible at portfolio level, which strengthens the ask rather than merely restating it.
- **Resolved 2026-10-02: Bill Muczko accepted.** Moved to Decisions Made (2026-10-02, CDA business sponsor). Kept here as the record of the nomination.

### 2026-09-18 — entroCIM/Navigator cut-machine monitoring: a possible new industrial-equipment use case (new)
- ID: D051
- Status: Approaching, unforumed
- Owner: unclear — Aaron Hudson raised it; Ron Snyder and Nathan Kehr were on the call with Darryl
- Forum: none named.
- Context: M365 evidence 2026-09-18 (entroCIM Potential for Cut Machine Monitoring, meeting 09-18 09:00-09:15). Aaron Hudson, new stakeholder in Automation Sustainment, described responsibility for sustaining equipment and asked about machine-data discovery for cut machines, potentially via iQ360-adjacent data. Reads as an early-stage opportunity, not a scoped proposal.
- Options: open a formal product/technical discovery; decline for now given the CDA and WAM data-foundation work already in flight; park pending a named sponsor and value hypothesis (consistent with the discipline Sean McCloskey has already applied to the CDA data-center thread above).
- Information still needed: named business sponsor, data ownership, integration boundary, and a value hypothesis before this competes for engineering time against entroCIM's 2027 capacity reduction (`04`).
- Risk of waiting: low near-term; risk of moving too fast is adding a fifth concurrent product-discovery thread onto a team whose development capacity is already being reduced for 2027.

### 2026-09-17 — How the entroCIM Team Quality Standard becomes an operating control, or stays a statement of intent
- ID: D052
- Status: Approaching, unforumed
- Owner: Ron Snyder authors and owns adoption; Darryl decides whether it is held to as a control. Document itself names "entroCIM Leadership Team" as owner, which is not an individual.
- Context: Ron delivered the standard 2026-09-17 at Darryl's request (`Products/entroCIM/entroCIM_Team_Quality_Standard_2026-09-17.md`). The content is good. It defines complete customer outcomes, handoffs as shared control points, readiness before commitment, and role expectations across all five delivery groups. It assigns no rollout owner, binds none of its checklists to Jira, release gates, reviews or retros, names no first application, and does not address how its handoff and early-escalation rules work across a team split seven India / four North America with no managers underneath.
- The decision is not whether to approve the document. It is whether entroCIM adopts a small number of these as enforced gates, and accepts the throughput cost of doing so, or issues it as guidance and expects behavior to follow.
- Options: (1) issue as guidance, no gates — lowest cost, and on the evidence of every prior standard in this record, lowest effect; (2) bind the §11 checklists to two existing control points only (release readiness and cross-team handoff) and leave the rest as guidance; (3) full adoption across commitment, handoff, deployment and closure; (4) pilot it on one named release or customer deployment and review after.
- Recommended when it is taken: option 4 into option 2. The pilot produces the evidence that the gates are workable before they are imposed on a team already carrying release, migration and defect pressure.
- Why this sits in Backlog rather than Radar: no forum, no date, and Darryl has not yet returned feedback to Ron (`05` A50). That feedback is what should produce the adoption proposal this decision needs.
- Why it matters beyond Ron's team: `03` 2026-09-10 records Darryl's own position that development has been slow and that quality has been questioned by his own team, with Sean McCloskey already believing results have not been good. An adopted standard with measurable handoff and defect outcomes is evidence of control; an issued document is evidence of intent. Do not present it upward as the former until it is one.
- Risk of waiting: the document ages into the drawer, which is the failure mode the EOS has documented twice for its own mechanisms. Risk of deciding too fast: gates imposed without a pilot land on a team already at capacity and get worked around.

### 2026-09-16 — CDA data-center commercialization path, possibly through TSS virtual site-survey
- ID: D055
- Status: Approaching, unforumed
- Owner: unclear — Darryl, with Bill Muczko and Sridhar Loke as the near-term contacts
- Context: Digital Products / Agile Staff Meeting, 2026-09-15 (transcript). Darryl raised the data-center market as a faster-moving route for CDA than the current commercialization path, with possible alignment to Wesco's existing TSS virtual site-survey service. Sean McCloskey set explicit conditions before this advances: evidence of a growing/credible market and a committed sales partner, not a product-capability argument alone.
- Options mentioned: partner with TSS; pursue through data-center sales; proceed without a dedicated sales team; do not advance now.
- Why this sits in Backlog rather than Radar: no forum, no date, and the first steps are fact-finding (market size, sales sponsor) rather than a decision Darryl can make today. Darryl committed to following up with Bill Muczko and Sridhar Loke on 2026-09-16 (`05` A46) — that follow-up is what should produce the facts this decision needs.
- Risk of waiting: continued low CDA adoption and a missed market-timing window if the data-center angle is real and Wesco is slow to move; conversely, chasing an unvalidated market diverts attention from the pilot-account validation gate already open in `Products/CDA/CDA.md` (Chris Mooney/Bill Muczko track).
- Note the two CDA validation tracks are now running in parallel — Converging Technologies/Bill Muczko (existing, `05` C42/A37) and data-center/TSS (new, this entry) — and should be reconciled rather than treated as separate CDA strategies before either goes to Sean or Chris Gazdic again.
- **Update 2026-09-18 (Chat with Nathan Kehr, M365 evidence):** a second, independent voice sets the same condition Sean McCloskey set 09-15. Nathan Kehr, direct: "let's wait until we get a real sponsor." Two separate leaders now require a named sponsor before CDA advances further on this track — treat this as the standing bar for the decision, not a one-person preference. Does not change the recommended path (fact-finding via A46 first); reinforces it. **Correction 2026-10-02 (Darryl):** this reads Nathan as a gatekeeper, which mischaracterizes him. He is an ally and champion of CDA; the sponsor condition is Sean's.
- **Update 2026-09-18 (Darryl):** "Bill Musco" is Bill Muczko; the two CDA tracks share one sales contact, which makes reconciliation easier. The Bob Caprise follow-up the same day adds a third thread (Axis per-camera fee, Kroger as anchor) and a sponsor path (Bill Muczko nominated; see Backlog entry 2026-09-18). A46's Bill half is answered by that route; the Sridhar Loke half remains.

### 2026-09-16 — Returnable asset tracking: partner, hybrid, or build the full stack
- ID: D054
- Status: Approaching, unforumed
- Owner: unclear. Tom Mitchell is leading the effort and the vendor relationship; Hemant Porwal set the build-internally direction; Darryl owns the platform and development capability. Establishing decision rights and the funding route is itself an open item.
- Context: returnable asset tracking discussion, 2026-09-16 (machine transcript, proper nouns corrupted). A 200-tracker paired pilot (100 products, each with one Alesea and one Sensolus tracker; corrected 2026-09-18 by Darryl from an earlier reading of 200 of each) concluded in favour of Sensolus, and the IoT team independently selected Sensolus over Digital Matter and others. The business case, roughly $500,000 per year at about $5 per tracker per month over three years, was declined by Hemant Porwal on the Friday before the meeting on the grounds that Wesco should not rent a vendor application it could build. Next steps agreed: a technical session with Sensolus, a commercial discussion on unbundled pricing, and a conversation with DDP about asset tracking they have already built.
- Options: (0) vendor full stack as declined; (1) vendor keeps device, connectivity and device services, Wesco builds the application; (2) device vendor plus Wesco-owned connectivity and platform; (3) Wesco-owned stack including direct device ingest; (4) hybrid by asset class. Detail in `Products/CAT/00_Charter/CAT_Charter_2026-09-16.md`.
- Why this sits in Backlog rather than Radar: no forum and no date, and the next steps are fact-finding (asset baseline, unbundled pricing, technical feasibility) rather than a decision anyone can take today.
- The material point for when it is taken: the build thesis is being tested against application cost, and the application is the cheapest layer. The five layer frame (`Products/CAT/03_Architecture/CAT_Five_Layer_Model_2026-09-16.md`) separates device, connectivity, positioning and device services, data plane, and application. Wesco already owns the data plane and most of the application, evidenced by the completed entroCIM Sensolus connector, and owns none of the three layers that carry the recurring cost and the operating burden. **Correction 2026-09-18 (Darryl):** the connector pulls data in only; the operations interface needs new PODs and a retained team (CDA-scale, ~$323K/yr) for any option beyond Option 0. On the 09-21 model (`Deliverables/CAT/2026-09-21_CAT_Financial_Model.xlsx`), with POD development all India and half the team retained, five-year fully costed totals at the inferred fleet are Option 0 $2.49M, Option 1 $2.70M, Option 3 $4.67M. Option 0 is lowest, and the decision now turns on G2: below about $3.07 per tracker per month for data-only access, Option 1 wins.
- Risk of waiting: the asset baseline does not exist, so no option can be costed. Risk of deciding too fast: a build commitment made on an application estimate, with the device services and field operating burden discovered afterwards.
- **Update 2026-09-18 (Darryl):** the request originates with EES and may extend to UBS as it matures. Sponsor name confirmed as Hemant Porwal. Taken to Sean McCloskey as a discussion point on 2026-09-18, with the question of how to bring the cost findings back to Heman.

### 2026-09-15 — i3 Alliance: cross-BU ownership and executive sponsorship after signature
- ID: D057
- Status: Approaching, unforumed
- Owner: unclear — candidates named in evidence are the entroCIM organization, Federal/SLED leadership, or a broader EVP sponsor
- Context: i3 Alliance Agreement email thread, M365 evidence 2026-09-14 to 2026-09-15. The signature mechanics are resolved (Lee Osterman, see Decisions Made above), but the agreement spans business units and has no natural P&L home — the signature decision does not answer who owns the relationship afterward.
- Risk of waiting: ambiguous ownership could slow activation after signature — a signed agreement with nobody driving it is a worse outcome than a slower signature with a clear owner.
- No forum named; recommend raising alongside the Brad Stevens/Lisa Orton unified-platform conversation, since i3/data-center partnering touches the same portfolio-boundary questions.

### 2026-09-15 — Agentic AI into Darryl's team, and what "reducing reliance on Brad Stevens' organization" means
- ID: D056
- Status: Approaching, unforumed
- Owner: Sean McCloskey raising; Darryl to shape
- Context: direct Teams chat, M365 evidence 2026-09-14 to 2026-09-15. Sean raised bringing Agentic AI capability into Darryl's team directly, framed explicitly as reducing reliance on Brad Stevens' organization. No scope, desired outcomes, or timeline given in evidence — reads as an opening move from Sean, not a settled ask.
- Why this needs framing before it needs an answer: it touches two live threads from different angles. The AI adoption governance row (`04`) is currently a tooling-evaluation question (Woolly, Copilot, Claude Code) — this is an organizational-boundary question instead, and folding them together risks answering the wrong one. Separately, the unified-platform conversation with Brad Stevens (`03`, 2026-09-03; `05` A38/A39/A40) is already testing where CSS Platforms' boundary with Brad's org sits — a capacity move into Darryl's team is a second, related test of that same boundary, raised by Darryl's own manager rather than by Brad.
- Risk of waiting: none acute — Sean has not set a deadline. Risk of answering too fast: committing to a team-structure change before the unified-platform boundary question resolves could pre-empt or contradict whatever comes out of the Brad Stevens/Lisa Orton conversation.
- No forum named yet; recommend a short decision-framing note to Sean (desired outcomes, scope, how it relates to the Brad Stevens conversation) before this becomes a standing ask.

### 2026-09-09 — IDP-to-ADM production integration: whether and how to resource it
- ID: D059
- Status: Approaching, unforumed
- Owner: Ankit Chadha
- Context: the IDP/ADM proof of concept and architecture received WAB approval this week, but Ankit Chadha would not commit engineering resources against it, citing an October Oracle deadline and competing high-volume work. He is investigating options (John, Sathish, the Bangalore AI team) over one to two weeks.
- Risk of waiting: ADM continues relying on inflexible or manual document-ingestion paths despite an approved integration path.
- No forum named; Ankit's own one-to-two-week timeline is the next natural check-in point, not a standing forum.

### 2026-09-09 — Managed-services operating model and staffing for day-two entroCIM monitoring
- ID: D058
- Status: Approaching, unforumed
- Owner: Brad Stevens and Nathan Kehr
- Context: leadership expects commercial growth in managed monitoring/analytics but has not settled the operating location, required building-domain skills, NOC placement, training path, or headcount. Brad Stevens: "we'll work with Nate... start identifying people that can go do that. Or if we don't have them, you know, start looking at head count."
- Risk of waiting: commercial growth could outpace delivery capacity — the same shape of risk already carried on the Ford renewal and the unified-platform pitch.
- No forum named yet; recommend routing through CSS Platforms All Hands or a dedicated session once Brad and Nathan have a first pass.

### 2026-09-03 — Ascent third-party ALM to WAM: is WAM's coverage sufficient to displace it
- ID: D060
- Status: Approaching, unforumed
- Owner: unassigned
- Context: Brad Stevens, attributing to Ben Pesek, reports the Ascent team is running Navigator plus a third-party ALM product and wants them switched to WAM, conditional on WAM covering all services Ascent offers and all services Wesco wants to offer. **The specific third-party product is not named in evidence and neither is a gap analysis.** Displacing an incumbent tool inside a live 24x7 operation, during the Maximo replacement, is a materially different proposition from adding a new customer.
- Why it sits in Backlog rather than Radar: no forum and no date, and the first step is a fact (which product, covering what) rather than a decision. Promote once Ben Pesek confirms the product and scope.
- Related: the same question in reverse sits on the Radar as the NavWork facility-data scope entry (2026-08-28).

*Real decisions with no routing forum or no live date. Reviewed monthly, on demand, or automatically when evidence shows one raised in a meeting (per Q4, 2026-07-27). Not surfaced weekly.*

### 2026-09-03 — Internal-use funding model for WAM in the Service Center
- ID: D007
- Status: Approaching
- Owner: Darryl Benson to frame; Brad Stevens, Finance and Operations to decide
- Forum: Brad Stevens / Lisa Orton meeting, week of 2026-09-08. (2026-09-08)
- Context: Brad wants a WAM pilot through the Service Centers in Irving and Dacula, driven by Manny's fatigue with multiple tools and by customer demand (Microsoft AV named). His question, verbatim: "Do we charge Operations for this tool or is it a cost to IT or a cost to Commercial for using the tool internally?"
- **This is a precedent decision, not a pilot detail.** No platform in this portfolio has an internal-use charging model, and every WAM figure of record is external attainment. Whatever is decided here becomes the template for internal use of entroCIM, Navigator and CDA, and it determines whether internal adoption shows up as revenue, as cost recovery, or as unfunded support load on Darryl's team.
- Recommended path, offered not decided: fund the pilot centrally and defer the charging model until the pilot produces a measured internal benefit, so the pilot is not killed by a cost-allocation argument before it produces evidence. Decide the standing model on that evidence.
- Risk of waiting: the team absorbs internal support demand with no funding line, which is the failure mode the FY27 resourcing conversation is already exposed to.
- Follow-up: A40, retired 2026-10-05 (Darryl disposition: Retire, no reason stated) -- the Register A action tracking this is closed; the decision itself is not stated as resolved and stays in Backlog until Darryl says otherwise.

### 2026-09-03 — CX Connect: ownership, what it actually does, and whether it belongs in the CSS portfolio
- ID: D006
- Status: Approaching
- Owner: unassigned; Brad Stevens believes Ed, with Liberty, owns it
- Forum: Brad Stevens / Lisa Orton meeting, week of 2026-09-08. (2026-09-08)
- Context: CX Connect appears nowhere in this record. Brad believes it monitors and manages AV installs and flags it against new Converging Technologies opportunities, then asks whether it should be integrated into WAM/ADM and whether the NOC could run it as a managed service. His own wording carries the uncertainty: "which is what CX Connect does I believe?"
- **Three questions in a fixed order, and taking them out of order is how this becomes a commitment before it is understood:** what is it and who owns it; is the AV monitor-and-manage demand real and sized; only then, does it belong inside WAM or as its own service. The third question is currently the one being discussed and it is the one that cannot yet be answered.
- Note the overlap worth naming early: monitor-and-manage of installed devices behind a customer firewall, sold as a managed service, is the CDA thesis. If CX Connect does that for AV, the portfolio may be about to fund the same capability twice.
- Risk of waiting: an ownership vacuum plus live sales interest produces an ad hoc commitment against a product nobody in CSS owns.
- Follow-up: A39.

### 2026-09-03 — Unified platform: what problem is it solving, before any scope is drawn
- ID: D005
- Status: Approaching
- Owner: Brad Stevens raising; Darryl Benson and Lisa Orton to shape
- Forum: Brad Stevens / Lisa Orton meeting, week of 2026-09-08. (2026-09-08)
- Context: Brad is pushing a holistic platform ("Innovance / Storefront / Wesco Connect") where all Wesco software products reside and work together. His list of what is being commercialized: entroCIM, WAM, "AMD" (read: ADM, which is a WAM component, not a peer), Connected Safety, CX Connect, Navigator. CDA is absent from the list.
- **The decision that has to be made first is not what to build. It is which of four different things "unified platform" means**, because they carry different costs, owners and timelines: (a) one commercial front door and brand for the portfolio; (b) one customer experience, single sign-on and navigation across products; (c) one shared data and services layer the products draw on; (d) one merged product. Brad's own framing ("dreaming I know") suggests he has not fixed on one either.
- Risk of waiting: a scope debate opens before the objective is agreed, the answer defaults to (d) because that is what "unified platform" sounds like, and Navigator, which is funded by a dated IBM forcing function and operated by Ascent, gets pulled into a program it cannot join before June 2027.
- Follow-up: A38. Detail: `Products/Unified_Platform/Unified_Platform.md`.

### 2026-09-01 — Standard commercial support/SLA structure for entroCIM renewals and managed services (new)
- ID: D062
- Status: Approaching
- Owner: Darryl Benson and Nathan Kehr; document ownership unclear
- Forum: none named.
- Context: sales and technical leaders explicitly disagreed this week on whether current plan descriptions and SME-hours language constitute one approved, comprehensive customer-facing support agreement. This is broader than the Ford UDAC renewal (`04`, Ford entroCIM platform-trust gap), which is the sharpest current instance of the same underlying gap, not the whole of it — a recurring topic (see `Reference` / weekly evidence, "entroCIM customer support and training model," surfaced again this cycle after first appearing around Ford's renewal).
- Options: formalize one customer-facing support SOW/process covering scope, ticketing, and service boundary; continue managing renewals case by case.
- Information still needed: a named document owner and a decision on whether the Ford scope document (`05` C35) becomes the template or a one-off.
- Risk of waiting: Ford and other renewals use inconsistent scope, ticketing, and service boundaries, compounding the trust gap already open on Ford specifically.
- Follow-up: raise at the next Darryl/Nate 1:1.

### 2026-09-01 — CDA: is the 2027 build worth committing to, and which pilot accounts validate it (new)
- ID: D061
- Status: Approaching
- Owner: Chris Mooney, Bill Muczko, Darryl Benson
- Forum: none named yet — the validation sessions that would produce a forum (Suzanne Betterton's team, Bill Muczko's senior directors/GAMs) are still being set up (`05` A37, due 2026-09-02). Promote to Radar once scheduled. (2026-09-02)
- Context: sales leadership was asked, following the 2026-08-28 executive brief, to judge whether CDA is worth building and to help identify two or three pilot accounts. This is the evidence gate the 2026-09-01 CDA operating-model decision (above) deliberately did not cross.
- Options: proceed to build with named pilots secured; hold the build pending more customer evidence; scale back to a narrower pilot.
- Information still needed: customer interviews and named pilot candidates — neither secured as of this evidence window.
- Risk of waiting: build priority gets set without market evidence, or the 2027 investment window slips while validation drags.
- Follow-up: A37; `Products/CDA/CDA.md` Open Decisions.

### 2026-08-27 — FY2027 roster classification: Pradyumna Umarji, Aaron Nolet, Chad Steger (new)
- ID: D066
- Status: Approaching
- Owner: Finance and product/platform leadership; John Erickson raised
- Forum: none named — surfaced in a Teams chat with John Erickson, not a scheduled forum.
- Context: Finance's roster conflicts with planned team changes. Pradyumna Umarji is planned to move off entroCIM and leave the team (timing unknown); Aaron Nolet is on long-term disability with the position backfilled and should be excluded from FY2027 COGS/development plans, but Finance's roster still shows him active; Chad Steger's COGS-versus-leadership/run-bucket classification is unresolved.
- Options: move Pradyumna off entroCIM formally in the roster; exclude Aaron Nolet from FY2027 plans; classify Chad Steger as COGS or leadership/run.
- Information still needed: Finance guidance and final timing for each of the three.
- Risk of waiting: AOP misclassification and capacity ambiguity carried into the FY2027 submission.
- Follow-up: resolve each person's disposition with Finance before the roster is finalized. Route to `06_Stakeholder_Map.md` for Pradyumna and Aaron individually (people-level signal); this entry tracks the decision, not the people facts.
- **Reconfirmed 2026-09-01 (weekly evidence, same source relationship):** all three dispositions remain open — Pradyumna's departure timing and receiving team still unknown, Aaron's LTD/backfill status still not reflected in Finance's active roster view, Chad Steger's COGS-versus-People-Management/Run treatment still conflicting guidance. No new movement; Echo, not new evidence.

### 2026-08-27 — Rovo's role in product-management AI operating model (new)
- ID: D065
- Status: Approaching
- Owner: Jim Lenart, with "Shawn" named but final authority not stated (name-collision caution per the standing rule — confirm which Shawn before treating as owned)
- Forum: `Product Management AI SOP Review` — cadence not confirmed as recurring in `07`; do not treat as a Radar-eligible forum until cadence is confirmed.
- Context: Copilot is selected for story/epic creation. Rovo remains under consideration for Jira operational search, cycle-time questions, and use-case discovery; backlog review is becoming its own SOP meeting type.
- Options: retain Rovo for operational Jira use cases relying on the Teams/Jira connector for item-level access; broader strategy still open.
- Information still needed: final permission/strategy decision and the approved use-case list.
- Risk of waiting: SOP and tooling choices for the product-management group remain unsettled.
- Follow-up: confirm whether this SOP Review is a standing forum; if so, add to `07` and promote to Radar with a date.

### 2026-08-27 — Ford renewal: secure remote-access method (new)
- ID: D064
- Status: Approaching
- Owner: Ford and Wesco; named follow-up owners Tim Scott, Adam Lazare
- Forum: none named.
- Context: current Ford support is largely over-the-shoulder. Long-term SLA-based support needs an approved remote-access path.
- Options mentioned: existing supplier/vendor path, VDI, cloud PC, VPN, or another approved method.
- Information still needed: Ford cybersecurity requirements and supplier-code eligibility.
- Risk of waiting: limits support effectiveness and increases operational risk on an account already flagged for platform-trust concerns.
- Follow-up: convert into a Ford-owned decision with requirements and a target date once Ford's cybersecurity team responds.

### 2026-08-27 — Ford renewal: PO structure (new)
- ID: D063
- Status: Approaching
- Owner: Ford finance/accounting; named follow-up owners Tim Scott, Jeffrey Pizzo
- Forum: none named — informal follow-up from the 08-26 Ford call, not transcribed at source.
- Context: Ford and Wesco aligned 08-26 to renew UDAC support and let EDC support expire. The renewal proposal may carry separate funding-group breakdowns; Ford has not decided whether funding runs through one consolidated PO or separate POs.
- Options: one consolidated PO; separate POs per funding group.
- Information still needed: Ford's internal funding decision and quote structure.
- Risk of waiting: delays proposal acceptance and renewal execution; compounds with the platform-trust audit already gating this account (`04`).
- Follow-up: confirm with Tim Scott/Jeffrey Pizzo once the formal proposal (Adam Lazare/Leanne Gordon) is drafted.

### 2026-08-19 — CDA pilot scope reconciled and Value KPIs added (new)
- ID: D069
- Status: Applied to the submission
- Owner: Darryl
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- **Pilot scope ruling (Darryl, 08-19): site count does not matter; the camera count is the goal. 250 to 1,000 cameras across several pilot customers.** This resolves a contradiction that had entered the form: B17 said one strategic enterprise customer across two to five sites, B23 said an estate of 250 to 1,000 devices, and the KPI basis initially offered was three pilots of 50 to 100 cameras each. Both fields now carry the reconciled scope.
- **Value KPI block added to the CDA submission, reversing the 08-18 decision to leave it blank.** Five KPIs, all customer-site outcomes: device inventory completeness; firmware currency; advisory-to-remediation time; remote resolution rate (target 25 percent or above, the only documented target); service evidence completeness. Quarterly cadence, materialization 12-2027.
- **Why the earlier objection no longer applies.** The 08-18 reasoning against KPIs was that the template requires post-production measures and CDA has no production in 2027. That still holds for the investment year, and B28 is dated accordingly at the pilot. What changed is the purpose: these describe the value a customer receives once the service runs, which is what Darryl wanted the form to show, rather than attempting to measure 2027 delivery.
- **Structural point worth carrying to future CDA material: CDA's KPIs are self-measurable by construction.** A Wesco-operated service node sits on every covered site, so the platform delivering the service is also the platform measuring it. entroCIM needed a coverage denominator because on-premises instances are dark between support touchpoints; CDA has no equivalent gap, no customer tooling dependency and no permission dependency. This is a genuine differentiator when the service is sold, not only a reporting convenience.
- **KPIs rebuilt later on 08-19 at Darryl's direction: product-specific, not pilot-dependent.** The first set measured how the pilot went rather than what the product does, so a poorly-run or unlucky pilot would have made a working product look weak and results would not have been comparable between customers. Rebuilt set: device coverage depth (by tier), automated discovery yield, advisory correlation coverage, remote change success rate, service evidence completeness. **KPI 1 uses the data-confidence ladder already in the Exec Brief (DISCOVERED by sensor, VALIDATED by direct integration, MANAGED under controlled action)** — the product's own framing for what separates it from an inventory tool, now used as a measure. The 25 percent remote-resolution target was removed from the KPI block as the most pilot-dependent item; the avoided-visit economics it supported remain in B23 at $300 to $600 per visit against a 15 percent reduction target.
- Follow-up: `Deliverables/CDA/2026-08-18_CDA_FY27_AOP_Change_Log.md` section 0b. The pilot-scope change should also reach `CDA_Business_Case_Working.md` and the Exec Brief when those are next revised, since both still describe a single strategic customer.

### 2026-08-18 — FY27 P&L revision: added India headcount, plus a portfolio-wide hours-basis change (new)
- ID: D070
- Status: Applied to all affected submissions; one consequence needs action before 08-21
- Owner: Darryl, with Tom Boss (Finance)
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- Evidence: `CSS_Platform_Team.xlsx` re-read 2026-08-18 16:34. Darryl added **one split India resource (0.5 FTE)** to entroCIM and to CDA.
- **Second change, not stated but material: the hours basis moved 1,800 to 1,880 on the entroCIM and WAM P&Ls.** Navigator and CDA were already on 1,880, so all four now compute on the same basis as the AOP form's calendar. **This eliminates both reconciliation residuals previously carried on the forms** ($29,472 entroCIM, $33,440 WAM). Good outcome; confirm it was intended rather than incidental to the headcount edit.
- **entroCIM:** DEV 6.60 to 7.10 FTE (India 3.50 to 4.00). **Confirmed 08-19: the added 0.5 India FTE is a NEW Product Owner role** (Headcount r43, Digital Products & Business, $22 rate), not additional engineering capacity. It is already inside the P&L and B18, so the Product Owner ask is captured and no separate uplift is outstanding. Gross labor $663,120 to $713,272. **B18 $857,052 to $877,732.** Gross margin 48.8% to 47.3%; net revenue ($897,778) at -18.0% to **($982,960) at -19.7%**; **breakeven $6,840,403 to ~$7,079,000, now $1,079,000 above the top of the authorised $6M range.** The sales-cost finding strengthens: sales cost exceeds gross margin by **$175,846** (was $100,694); zeroing DEV and Marketing together still leaves a $175,846 loss.
- **CDA:** DEV 6.50 to 7.00 FTE (India 6.25 to 6.75). Gross labor $201,787 to $215,573. **B18 $246,787 to $260,573.** Net revenue ($85,357) to ($88,115).
- **ACTION REQUIRED: CDA now crosses the $250,000 intake threshold.** It was $3,213 under; it is now **$10,573 over**. Per the Intake deck that triggers the mandatory Project Financials form (slide 8: "must be completed for all projects with cost over $250k") and the business-case requirement for requests over $250K not in budget. The business case exists so the substance is covered, but the financial slide is no longer optional. This was flagged as a $3,213 headroom risk hours before the change; it has now materialised.
- **WAM:** headcount unchanged. The hours-basis move raised P&L gross labor $752,400 to $785,840, which now **exactly equals the B18 already on the form**. Net revenue $4,075,520 to $4,068,832 (10.7% unchanged). B18 unchanged; B23 figures corrected.
- **Navigator:** entirely unchanged. B18 $1,797,280 still exact. No action.
- Scoring impact: none. All four Implementation Cost bands remain correct.
- Risk of waiting: three days to the 08-21 gate. The CDA threshold crossing changes what the intake package must contain, not only a number on a form.
- **2026-08-19 additions (Darryl):** ecoInsight contractor (Ashray Hebbar, India, entroCIM Build only) removed from the project; entroCIM FY27 delivery is now internal only, and B34 on the form reads "Outsourced: none". No financial impact, since he was already carried at 0 FTE. Harsha E confirmed as owner of the entroCIM UI/UX redesign (Register B28). **Forward intent recorded: UI/UX work moves off dedicated developer capacity as Claude Design support lands at Wesco**, which is why the redesign is not being re-staffed after Hebbar's removal. That intent is deliberately not written into the AOP submission — it is a delivery-resourcing rationale rather than FY27 investment scope, and it is distinct from the customer-facing AI analytics content already on the form. It sits alongside the open AI-tooling governance threads (Claude-code WAB, GitHub Copilot / Vibe Guard).
- **WAM correction 2026-08-19:** WAM's B34 named ecoInsight as an outsourced resource. The financial model carries ecoInsight on entroCIM Build lines only, with none on WAM. The reference was inherited from the FY26 text and survived two rewrites of that field. Removed; Revnue Corp remains as WAM's sole outsourced resource. **Process point worth keeping: inherited text was preserved without testing the factual claim inside it.** The same check that caught the B18 overstatements would have caught this, namely reading each field against the resourcing model rather than against the previous version of the field.
- Follow-up: change logs updated for WAM, entroCIM and CDA; `Products/entroCIM/entroCIM.md` FY27 and resourcing sections revised; `05` Register B28 updated.

### 2026-08-17 — WAM FY27 AOP investment figure re-based against the 2027 WAM P&L (new)
- ID: D015
- Status: Applied to the form; two inputs still owed by Finance
- Owner: Darryl, with Tom Boss (CSS Finance) on rate basis and Pro-Forma; Sean McCloskey on the resource determination (A25)
- Forum: Tom Boss (rate basis, Pro-Forma, capitalization label); the 08-07 AOP alignment track with Lisa Orton, Brad Stevens, Gregg O'Brien as backstop.
- Evidence: 2027 WAM Profit & Loss (DRAFT), provided by Darryl in session 08-17 as a screenshot rather than a file. Stated basis: all named WAM resources assigned to DEV using % COGS Today, Region, Cost, and 1,800 annual hours.
- **Fact: the FY27 form figure was overstated by $212,040, or 28.2%.** `3. BUSINESS CASE!B18` carried a hardcoded $964,440, which implies 21.375 FTE at $24/hr on 1,880 hours, all at India rate. The P&L plans 19.00 FTE at $22/hr on 1,800 hours (Resources IN 19.00, Resources NA zero) for a gross of $752,400. The variance decomposes exactly: headcount 2.375 FTE = $107,160; rate $24 vs $22 = $71,440; hours 1,880 vs 1,800 = $33,440.
- **This is the same failure mode found on entroCIM on 08-05** ($1,437,918 on the form against a $727,200 2027 DEV plan). Both forms predate the resourcing model and neither followed it. Treat "the AOP form figure has not been updated to the 2027 plan" as a pattern across the portfolio submissions, not an entroCIM-specific defect, and check Ascent/Navigator before 08-21.
- **B18 set to $785,840** = 19.00 FTE x $22 x 1,880, carrying the P&L roster and rate onto the form's mandatory 1,880-hour calendar basis so B18 ties to what tab 2A will compute. Residual $33,440 versus the P&L is the hours-basis difference alone and is not reconcilable; it must be stated. If Finance rules the $24 rate card mandatory, B18 becomes $857,280. Both are under $1M so Scoring B16 (`< $1 million`) holds either way.
- **New finding, needs a Finance answer: the P&L capitalization label contradicts its own arithmetic.** The line reads CAPITALIZED LABOR (65%) but $601,920 on a $752,400 gross is 80.0%. At a true 65% the capitalized amount is $489,060 and DEV expense $263,340 rather than $150,480, a $112,860 swing that moves net revenue from $4,075,520 to $3,962,660 (10.4% vs 10.7%). Note 80% is the AOP template's own default capex %, so the formula matches the AOP default while only the label matches the 65% entroCIM convention. **Consequence: keep tab 2A at 80%, and correct the P&L label.** This reverses the 65% recommendation made earlier in the same session.
- **Corroboration of the 08-05 license-versus-supply-chain finding, now visible in Finance's own numbers.** Planned FY2027 gross margin is 15.2% ($5,776,000 on $38,000,000 revenue, COGS $32,224,000). That is a distribution margin, not a software margin. If WAM revenue were license and software driven the margin would be several times higher. The 08-05 finding is therefore not a single-session anecdote; it is evidenced in the P&L structure. Strengthens the case for deciding the roadmap alignment question rather than leaving it at (c) by default.
- **Revenue basis widened by Finance the same day (Darryl, 08-17): a planning range of $32,000,000 to $38,000,000 is permitted for 2027.** B23 now carries the range and its sensitivity rather than a single point. Holding the P&L's 15.2% gross margin and its fixed Sales, Marketing and DEV lines, net revenue runs $3,163,520 (9.9%) at $32M to $4,075,520 (10.7%) at $38M, a $912,000 spread. The $38M case reproduces the P&L exactly, so the sensitivity rests on the P&L's own structure. **Submission basis is the range itself, not a point estimate (Darryl, 08-17), because the CSS business does not yet have its actual 2027 forecast available;** Finance authorised the range as the interim planning basis and it will be replaced when the CSS forecast is issued. This supersedes an earlier in-session recommendation to submit at the $32M lower bound, which wrongly framed the range as a conservatism choice rather than an upstream forecast gap owned by CSS. The range is defensible because the case holds at every point in it: net revenue covers the $785,840 investment 4.0x at the bottom and 5.2x at the top, so "what if revenue lands low" does not change the decision. **Finance issued a second range for entroCIM the same day; values not yet captured — obtain and apply the same treatment to that submission.** Assumption to confirm with Tom Boss, labelled as such on the form: that gross margin holds at 15.2% as volume falls, since COGS is predominantly hardware and software pass-through.
- Revenue basis: $38,000,000 is stated as 2026 actuals +15%, planning only, not an approved budget. It implies a 2026 base of $33,043,478, which reconciles to $16.7M YTD through June annualized, but is 1.74x the recorded 2026 objective of $19.0M. A reviewer seeing $19M objective against a $38M plan will ask; the answer is that the objective and the run rate diverged, not the plan and the run rate.
- Secondary observation: Marketing is $50,000, 0.13% of planned revenue, labelled as the 2026 budget carried forward, against a product whose commercialization plan includes a broader marketing launch. The commercialization narrative and the marketing line do not agree.
- Open dependency: Resources NA is zero. If any North America resource is assigned to WAM the cost is understated at a 4.3x differential ($94 vs $22); the entroCIM equivalent exposure was 3.45 FTE carrying $583,740. Confirm against A25 (WAM resource determination with Sean McCloskey), overdue since 08-14.
- Risk of waiting: 08-21 is four days out. A submission carrying a figure 28.2% above the governing model inherits a field-by-field challenge, and the Pro-Forma attribution gap is the one a reviewer will find first.
- Follow-up: full reconciliation and reversible cell-by-cell change log in `Deliverables/WAM/2026-08-17_WAM_FY27_AOP_Change_Log.md`. Cross-reference the 2026-08-05 WAM license-roadmap alignment entry and the 2026-08-05 FY27 financial-assumptions entry (C16).

### 2026-08-12 — SPA Engine — retain, reassign, or retire (new 2026-08-12)
- ID: D082
- Forum: none named — likely folds into Digital Products Portfolio Review once a list exists.
- Owner if known: **Shawn Clark** (per evidence — unconfirmed beyond this mention; no reporting-line or product-scope basis given)
- Added: 2026-08-12 (M365 evidence — "SPA Engine discussion" meeting; ties to Register A24, opened 08-05 when Darryl said "more information next week")
- Context: A24 has run since 08-05 on no source material — the product's description in `Reference/Digital_Product_List.md` is provisional. This meeting is the "more information" Darryl was waiting on. Two outputs: (1) an action — **Maddy Taylor owes Darryl a clarified SPA Engine product-assignment list** (Copilot attribution: Inferred, not yet confirmed as her own words); (2) a framing — the ownership question itself is now posed as retain / reassign / retire, with Shawn Clark named as owner-if-known, not confirmed.
- **Open question worth putting to Darryl directly:** Maddy Taylor's tracked product list (`06`) doesn't include SPA Engine, and Shawn Clark is an entroCIM architect-track engineer, not a product-executive role — neither attribution fits the existing stakeholder map cleanly. Confirm both names before treating this as settled.
- Options: retain within current ownership, reassign to a named PE, or retire the product.
- Risk of waiting: Register A24 has now run 8 days on a provisional entry; a second cycle without the assignment list keeps `Reference/Digital_Product_List.md` inaccurate.
- Follow-up: Other-Owned item added for Maddy Taylor (`05`); A24 updated with this evidence.

### 2026-08-10 — Milestone renewal identification method (new 2026-08-10)
- ID: D085
- Owner: unclear in evidence
- Forum: none named — natural fit is ADM connect with Natalie, same forum as B20.
- Added: 2026-08-10 (weekly evidence, source unspecified beyond "new this week")
- Context: the method for identifying renewals from Milestone data lacks source-system linkage. Distinct from the existing B20 item (Natalie Marquardt — confirm why EUDM/DDP vendor part numbers are truncated; resend corrected Milestone Q2 data) — that is a data-quality/truncation defect, this is a methodology gap (how renewals get identified at all from Milestone). Related but not the same fact; do not merge.
- Options: not yet framed in evidence.
- Risk of waiting: renewal analytics accuracy — direct exposure given today's WAM/ADM notification release depends on renewal data being trustworthy.
- Follow-up: name an owner before the next ADM connect with Natalie.

### 2026-08-10 — P360 product-type governance: request declined, workaround stands
- ID: D075
- Status: Made (tactical) / Backlog (strategic)
- Owner: Akansh Gangil (workaround execution); P360 governance stakeholders (policy, unnamed)
- Forum: none named.
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- Context (weekly evidence, ADM connect with Natalie): **product type will continue to be collected outside P360 global attributes.** This is a governance refusal, not a deferral — P360 declined to add product type as a global attribute. Akansh's team continues the existing manual/workaround process.
- This is the tactical half of the standing "Supplier attribute data ownership (RACI)" Decision Backlog item below — the practical workaround is settled, but the underlying policy question (should product type ever become a P360 global attribute) remains unanswered after multiple weeks of escalation with no response. Do not read the workaround as resolving the governance question.
- Risk of waiting: continued manual process and data inconsistency — feeds the WAM/ADM data integrity watch row, not a new risk in itself.

### 2026-08-10 — Device Assurance (CDA): positioning refined; Nozomi partnership advances
- ID: D074
- Status: Advancing, no gate change
- Owner: Cody Remington (market validation/positioning), Darryl (initiative)
- Forum: none named — folds into the existing CDA initiative thread.
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- Context (weekly evidence, "IoT Compliance - your Paper"): Device Assurance strategy now stated as centering on **passive discovery and firmware validation, not direct firmware pushing** — consistent with the 07-27 "sensing = Guardian container, entroCIM does not push firmware" architecture rulings. Positioning confirmed **complementary to Nozomi Guardian, not competitive.**
- **Nozomi partnership: MNDA received; sandbox and license access offered pending execution.** First concrete step toward resolving the partner-licensing questions logged in the ideation Research Log 07-28 (Guardian container licensing, multi-customer terms, Arc attach licensing, API stability).
- New people (unconfirmed): **John Evans** — market feedback contact on Milestone/Genetec positioning, tasked to Cody Remington. **Nathan Haines** — separate thread, see ServiceNow entry below, not connected to CDA.
- **Spelling flag:** this evidence spells the name "Cody Remington"; the 07-29 SPARC/VOI entry spells it "Cody Remmington." Treat as the same person pending confirmation — do not create two stakeholder entries.
- Follow-up: two open action items, not dated — arrange the John Evans meeting; gather Milestone/Genetec market feedback. Neither gates A22 (CDA AOP package) directly, but both feed the business case's competitive-positioning section.

### 2026-08-06 — Digital Portfolio Review risk-target wording (new 2026-08-06)
- ID: D083
- Owner: Chris Gazdic / John Erickson, with Darryl's input
- Forum: none named — direct with Chris Gazdic/John Erickson.
- Next action: confirm today (08-06) whether the reframe was finalized before this risk appears in front of a wider audience again.
- Added: 2026-08-06 (M365 evidence — Teams conversation with John Erickson and Chris Gazdic, 08-05)
- Context: a long-horizon portfolio risk currently carries a full-resolution target of 3Q 2027. John Erickson: "we'll need to make any updates before EOD" (2026-08-05). Chris Gazdic proposed reframing the target to when a strategy/game plan will be in place, or splitting the risk into multiple risks with separate dates, rather than restating 3Q 2027 as-is.
- Options: set a nearer target for establishing the strategy; split into multiple risks; leave as stated.
- Information still needed: final wording, target date, and whether decomposition happened. **No confirmation in evidence that the 08-05 EOD deadline was met** — per closure/evidence discipline, absence is not proof either way.
- Risk of waiting: if unresolved, a long-horizon, weakly actionable risk statement may already be circulating in portfolio reporting under Darryl's name.

### 2026-08-06 — i3 Alliance: tier election, and whether to accept Section 8 (new)
- ID: D071
- Status: Approaching
- Owner: Sales owns the tier election; CSS Platforms owns the Section 8 position and holds a veto in substance, since the Section 3.6 gate turns solely on Section 8
- Forum: not yet routed. Needs Legal plus Sales in the same conversation, with the Exhibit B in-kind exposure raised there (see `04` Passive).
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- Context: Section 8.8 as drafted states acceptance is all-or-nothing and partial acceptance does not satisfy the section. If that stands, the twelve-item redline is moot, because Section 8 as amended would not be Section 8 and Wesco would be treated as declining. i3's own draft contradicts this: the note above Section 8 asks Wesco to propose language. That inconsistency should be put to i3 as a question rather than argued.
- Options: accept Section 8 as amended and elect Preferred or Strategic; decline Section 8 and elect Approved (zero cost in Year 1, no pipeline commitment, one certified individual, exitable on 60 days under §14.4); walk away.
- Recommended path: **Approved with Section 8 declined**, unless the five floor items are met. Section 8.7, written by i3, already defines how a declined-Section-8 relationship operates, so the fallback is contractual rather than argued.
- Risk of waiting: low on the agreement itself. The real risk is the SECO opportunity being used to compress the decision timeline before Section 8 is resolved.
- Follow-up: gated on Legal's response (C-i3-1) and i3's answer on 8.8.

### 2026-08-06 — FY27 AOP: portfolio structure set at the workshop; three Darryl-owned inputs now dated 08-14 (new)
- ID: D011
- Status: Complete
- Owner: Sean McCloskey / Chris Gazdic (portfolio structure); Darryl (three named inputs below)
- Forum: Product AOP Workshop thread; backstopped by the 2026-08-07 AOP alignment meeting (A5) and the entroCIM AOP / eCIM Budget track with Tom Boss. (2026-08-07)
> *Kept on the Radar 2026-08-19. The stale-forum-date pass flagged it, but FY27 AOP is on a fixed 08-21 date; the correct action is to re-set the forum date, not to demote the item. Forum date needs re-setting.*
- Context (Product AOP Workshop, 2026-08-05, evidence 08-06): Supplier RFQ confirmed as its own modular AOP line item with a separate budget rather than folded into an existing initiative; Assortment confirmed standalone. AOP naming will combine "industrial quoting and project management" if project management is included (Chris Gazdic). Open inputs across the workshop — KPIs, forecasts, AI costs, resource assumptions — are targeted for **2026-08-14**, ahead of the 08-21 Planview submission (A19/A21).
- **Three inputs are named to Darryl specifically, not the portfolio generally:**
1. estimate AI token usage/cost for Connected Device Assurance using data from Alpee and Ankit;
2. confirm Ascent resource levels hold for the next period and communicate the result to TJ;
3. with Sean McCloskey, determine WAM resource quantity, allocation, and possible team ownership.

Meeting-task notes tag each "(Darryl)" or "(Darryl, Sean)" — same attribution pattern already accepted for A19/A21 (named executive assignee, no other owner stated). Added to Register A as **A25**.
- Information still needed: whether the CDA AI-cost estimate is meant to feed the same CDA package under date pressure in A22; who owns consolidating all three inputs into the AOP working model before 08-14.
- Risk of waiting: 08-14 is 8 days out and sits inside an already-overloaded Register A (24 items against a 10-15 target); if these three slip, they compress directly into the 08-21 submission window with no buffer.
- Follow-up: Register A25 (new). Cross-reference A3, A4, A19, A21, A22 — this is the same FY27 AOP initiative, not a parallel one; do not restate the underlying submission mechanics here.

### 2026-08-05 — FY27 AOP assignee scope expanded; deadline unchanged (new)
- ID: D013
- Status: Approaching — decision required on scope, not on whether to submit
- Owner: John Erickson (scope), Darryl (execution)
- Forum: direct with John Erickson; natural venue is the A3 working session (overdue since 08-03). The 2026-08-07 AOP alignment meeting with Lisa Orton, Brad Stevens, and Gregg O'Brien is the backstop. (2026-08-07)
> *Kept on the Radar 2026-08-19. The stale-forum-date pass flagged it, but FY27 AOP is on a fixed 08-21 date; the correct action is to re-set the forum date, not to demote the item. Forum date needs re-setting.*
- Context: the 08-05 FY27 AOP email lists Darryl as executive assignee for **Ascent/Navigator, entroCIM, and WAM, with Connected Safety and a new product under discussion**. Submissions due on or before **2026-08-21**. Register A19 had been written on 08-03 for entroCIM and WAM only. Separately, Erickson asked the named assignees to update PO capacity expectations from `product-team_capacity.xlsx` (Register A21).
- **Fact vs. inference.** Fact: the assignee list and the 08-21 date are stated in the evidence. Inference, not confirmed: that the "new product under discussion" is CDA. If it is, CDA's AOP input date moves from 2026-08-31 (Darryl's date, 07-23) to 08-21, compressing the CDA backward plan by ten days and pushing the package date inside the concept-freeze window.
- Options: submit against three named products only; submit against all five; seek an extension for the conditional products.
- Information still needed: which products carry a required submission, whether the two "under discussion" products are in or out, and whether 08-21 applies uniformly across them.
- Risk of waiting: Darryl builds two business cases and discovers in week two that he owes five. The failure mode is weak cases on late-started products, not a missed date.
- Follow-up: registers A19 (rewritten), A21 (new), A22 (new, CDA package). Five meetings dated 08-04 produced no transcript, four of them AOP or portfolio relevant (AOP 2027, Connect on AOP - Darryl, eCIM Budget, Digital Transformation Discussion), so any scope clarification reached verbally on 08-04 is not in the record. Barbara Serdeczna appears against both the WAM and entroCIM AOP demand-collation templates and may be the faster route to the scope and deadline answers than waiting on Erickson.

### 2026-08-05 — CSS Platforms 2027 resourcing: Deployment and Development headcount reduction request (new)
- ID: D012
- Status: Approaching — modeling in progress, numbers expected final by end of week
- Owner: Darryl, with CSS Finance and CSS Sales. Business sponsor: Dirk Naylor (entroCIM). Brad Stevens holds a stated position on deployment capacity (see contradiction below)
- Forum: CSS Finance and Sales 2027 modeling sessions (in progress); Brad Stevens approval review this week; then the 2026-08-07 AOP alignment meeting called by Lisa Orton with Brad Stevens and Gregg O'Brien (Register A5). (2026-08-07)
> *Kept on the Radar 2026-08-19. The stale-forum-date pass flagged it, but FY27 AOP is on a fixed 08-21 date; the correct action is to re-set the forum date, not to demote the item. Forum date needs re-setting.*
- Context (Darryl, session 08-05): current sales performance has prompted CSS Sales to request headcount reductions in both Deployment and Development on the CSS Platforms team. Darryl is working with CSS Finance and Sales to model 2027, agree the path forward, and build the FY27 AOP on that basis. This is the resourcing input that the entroCIM FY27 business case (A19) now depends on, which means the previously recorded $1,437,918 total investment cost is provisional until the model lands.
- **Correction, same day (Darryl, 08-05).** An earlier version of this entry read the CSS Sales request as contradicting Brad Stevens's 07-28 position that deployment capacity must not be cut. That reading was wrong and is withdrawn. Governance is intact: the numbers are reviewed with Brad Stevens this week for his approval, and he can direct headcount to be restored. The first-pass model was deliberately aggressive, which is a modeling posture rather than a proposed outcome. Brad's 07-28 statement and this request are not in conflict; the request is an input, his approval is the decision point.
- Practical consequence of the aggressive first pass: the reviewed output, not the first pass, is the number that should reach any external or upward audience. Until Brad's approval lands, an aggressive internal working model circulating as if it were the plan would misrepresent both the capacity position and the FY27 ask.
- **Model received and analysed 08-05 (Darryl): `Products/entroCIM/CSS_Platform_Team_ P&L_Analysis_COPY_08AUG.xlsx` is the governing 2027 model.** It supersedes any inference drawn from the AOP form alone. Headline: 2026 plan 31.6 weighted FTE / $3,286,080 labor, 2027 plan 22.5 FTE / $2,446,200, a reduction of 9.1 FTE and $839,880. Split: COGS 14.5 → 11.5 FTE (-$151,200); DEV 17.1 → 11.0 FTE (-$688,680). The reduction is weighted to DEV, and within DEV to North America, where 3.45 FTE carries $583,740 on the $94 vs $22 rate differential. 2027 P&L outcome: revenue $4.8M (2026 actuals +76%), gross margin 47%, net -$1,212,954 (-25%), with the amortization toggle set Off, i.e. the cash-flow view preferred in the 07-28 session rather than a GAAP view. Capitalized labor 65%, consistent with the AOP form. Three scenarios modeled: current state; optimize/modernize under a new operating model; and an entroCIM + CDA split (the last intersects Register A22, since both AOP submissions would then draw on one roster).
- **Material conflict now open, and it is the reason this entry matters: the AOP form has not been updated to the 2027 plan.** The form states $1,437,918 for target year 2027. That figure sits within 1.6% of the *2026* DEV plan ($1,415,880) and is $710,718 above the *2027* DEV plan ($727,200). `3. BUSINESS CASE!B18` is a hardcoded value rather than a formula, so it will not follow a roster change. Full reconciliation: `Deliverables/2026-08-05_entroCIM_FY27_1.44M_Reconciliation.md`.
- **Resolves a long-open AOP question.** Whether $1,437,918 is at or below the 2026 run rate has been open since 07-24. It is marginally *above*, by $22,038. The "flat is a win" verbal position is not supportable on the form as it currently stands.
- Secondary discrepancies to settle: rate card differs between the two documents (India $22 in the P&L, $24 on the AOP with outliers at $21 and $38; North America $94 in both); and the populations differ, with the AOP carrying Clark, Papanna and Reed as DEV where the P&L treats them partly or wholly as COGS/SERV, while the P&L deliberately carries Darryl, Blondel and Snyder at zero FTE.
- Delivery-risk check: Harsha E and Ashray Hebbar are both absent from Scenario 2 and are the two developers assigned 07-30 to the entroCIM UI/UX table redesign (Register B28). Jason Ganiatsas is also removed, at 0.75 FTE / $132,540 on the AOP roster. Confirm reassignment or descope rather than assuming the work continues.
- Information still needed: Brad's approved position after this week's review; whether the agreed reduction is a 2027 plan assumption or an in-year action; and, if in-year, how reduced Deployment capacity interacts with the September 1 Quest-to-Azure completion and the committed October 5 release.
- Risk of waiting: the 08-21 AOP submission is mandatory and the model is the input to it. A submission built on an unresolved resourcing assumption inherits a challenge the reviewers can raise field by field. Second-order risk: reducing delivery capacity in response to a commercial-conversion problem treats the symptom, since the evidenced constraint is conversion and attach rather than delivery throughput.
- Follow-up: cross-reference `04` entroCIM commercial performance row (trend raised to worsening 08-05) and the WAM financial narrative row, which carries the same 07-28 Brad Stevens statement. Update the entroCIM FY27 investment figure in `Products/entroCIM/entroCIM_FY27_AOP_Findings_Import_Package_2026-08-04.md` once the model is final.

### 2026-08-03 — Product lifecycle-management direction — Ascent Navigator/Maximo, ALM, and related tools (new 2026-08-03)
- ID: D095
- Owner: unclear — no internal owner named in evidence
- Forum: none assigned.
- Added: 2026-08-03 (M365 weekly evidence)
- Context: a question raised 2026-08-01 and forwarded 2026-08-02 about enterprise direction for product-lifecycle-management tooling across Ascent Navigator/Maximo, ALM, and related platforms. No recorded enterprise decision or target operating model exists today.
- Options: not yet framed in evidence.
- Risk of waiting: Medium — duplicate platforms and fragmented sustainment data if left undecided; low urgency near-term.
- Follow-up: identify who raised this and why, before assigning an owner or forum — evidence gives no requester context.

### 2026-07-31 — FRBNY QA-1 rollout continuation — map defect after 3.1.12.13.0 update (new 2026-07-31)
- ID: D094
- Owner: Ron Snyder / delivery team
- Forum: Darryl / Ron weekly 1:1; also relevant to the entroCIM 3.1.12.13.0 deployment row in `04`.
- Next action: confirm the non-VPN test result before any further FRB server updates proceed. Register B24 added.
- Added: 2026-07-31 (M365 evidence — Re: Ticket Updated - Pod update Paas-02)
- Context: FRBNY QA-1 was updated to 3.1.12.13.0; most functions work but the HQ map fails to load. Team plan: have the customer test outside the VPN before deciding whether to proceed with updates to the remaining FRB servers.
- Options: proceed with remaining FRB server updates now vs. hold pending non-VPN test result and root-cause confirmation.
- Risk of waiting: if the defect reproduces outside the VPN and is pushed to other servers before root cause is understood, the release-rollout defect could replicate across FRBNY's broader environment.

### 2026-07-31 — TCCC (Coca-Cola) cyber-risk control closure — two controls overdue (new 2026-07-31)
- ID: D093
- Owner: unclear internally — Darryl named directly as the OneTrust-assigned approver on the returned risk treatment
- Forum: none assigned. Surfaced to Darryl 07-31, same-day — flagged in chat pending his confirmation of ownership; not written into Register A on system-assignment alone per the attribution test, given no internal owner is yet named for the technical evidence itself.
- Next action: Darryl to confirm in OneTrust whether he is the substantive owner or the routing/approval point only, and name the internal owner(s) for log-retention and assessment evidence.
- Added: 2026-07-31 (M365 evidence — Re: Cyber Risk Assessment Results: Wesco entroCIM; [Coca-Cola] Action Required - Approver Sent Back Risk Treatment)
- Context: five controls (SO-V.09.1, SD-V-HRD.03.2, SD-V-HRD.02.1, IAM-V.05.2, IAM-V.05.1) confirmed remediated by Yadu Nandan M (TCCC Cybersecurity TPRM). Two remain open: **SO-V.06.2 (log retention) is past its planned deadline**, and **OT-V.02.1 (ISA/IEC 62443 certification evidence) is unmet**. TCCC's OneTrust system returned the risk treatment to Darryl directly and separately requested a recent cybersecurity/vulnerability assessment report.
- This is distinct from the TCCC/AOC network-connectivity thread above — same customer, different workstream (formal cyber-risk compliance vs. network/controller dispute). Do not conflate.
- Options: extend the log-retention window with a remediation date; supply existing assessment evidence; state an accurate ISA/IEC 62443 position (compliant, in-progress, or not pursued) rather than let the gap sit unaddressed.
- Information still needed: who internally owns log-retention disk capacity and vulnerability-assessment evidence; whether a certification roadmap exists.
- Risk of waiting: customer-facing compliance gap with a named overdue control, at a marquee account already carrying an active technical dispute (AOC connectivity) — compounding exposure at the same customer on two fronts simultaneously.
- **Update 08-17 (weekly evidence, Re: Cyber Risk Assessment Results): count discrepancy, not yet reconciled.** Yadu Nandan is quoted stating "we have closed all the high risks," and the evidence separately characterizes **two remaining medium risks**. The tracked record here shows only **one** open control (OT-V.02.1, ISA/IEC 62443 certification evidence) since SO-V.06.2 was remediated 08-04/08-05. Two readings are possible: (a) OT-V.02.1 was reclassified from High to Medium severity and the "two" is an extraction artifact or miscount, or (b) a second, not-yet-identified medium risk exists that has not reached this record. **Do not restate "two remaining risks" as fact until confirmed with Mike Reed or Yadu Nandan directly** — same closure discipline as every other TCCC cyber item. OT-V.02.1 itself is unchanged: no internal owner, no certification roadmap, still the recurring topic without resolution (see `04`). This is now the fourth consecutive evidence cycle citing OT-V.02.1 as unresolved.
- **Update 08-17 (weekly evidence): 62443-4-1 response path reconfirmed still open as of 08-14** — owner unclear, blocked on acceptance criteria and certification evidence, per this cycle's evidence. Appears in Section 9 (Recurring Topics Without Resolution) of the weekly package. No register item exists for this despite Darryl being the named OneTrust approver — worth a deliberate decision on whether to create one rather than let it keep recurring unowned.

### 2026-07-28 — Dell enhancement-request process ownership (new 2026-07-28)
- ID: D092
- Owner: Darryl/leadership — unclear in evidence (Copilot attribution: Implied)
- Forum: none assigned — recommend Darryl decide directly rather than let it default.
- Added: 2026-07-28 (M365 evidence — FW: entroCIM enhancement request)
- Context: Shanti (surname not evidenced) transitioned out of the role that owned Dell enhancement-request communication; no successor named. Adam Lazare has asked for guidance on ownership.
- Options: Darryl names an owner within his team vs. routes to Adam Lazare's org vs. holds pending further scoping.
- Risk of waiting: customer roadmap requests lose visibility during the ownership gap.
- Follow-up: surfaced to Darryl 07-28 as a same-day flag. Per the attribution test, the Implied evidence does not create a Register A item on its own — confirm ownership intent first.

### 2026-07-28 — TCCC (Coca-Cola)/AOC connectivity requests — position and remediation path (updated 2026-07-28)
- ID: D091
- Owner: Scott Dunn (technical diagnosis, customer-facing), Sarah Monteleone (customer relationship/commercial), Syed Zaidi (tracking); Darryl directing internal position.
- Forum: Wednesday 2026-07-29 meeting with Matt Shepherd (TCCC), pursued by Sarah — not yet confirmed accepted. (2026-07-29)
- Added: 2026-07-28 (Sarah Monteleone forward of full email thread, 07-27; Darryl field note 07-28). Supersedes the earlier same-day placeholder entry built from the Copilot summary alone, which read this as a possible reopen of the 07-27 closed "Airwall reported offline" item — **confirmed distinct (Darryl, 07-28), not the same issue.**
- Context: escalating pattern of customer requests to reduce/disable entroCIM connectivity at TCCC's AOC campus, running 07-22 (test isolation request) to 07-27 (request to turn off all remaining routers, after "substantial improvement" from partial shutdowns "last week"). Full detail in `04_Executive_Watch_List.md`. Scott Dunn's own 07-27 reply shows Wesco previously worked with ALC contacts (Kevin, Jacob) to identify overloaded network areas on this campus, with several connectors already disabled pending hardware upgrades — this is a known, ongoing pattern, not a fresh surprise.
- Options considered: (1) agree to disable remaining connectors/Airwall at AOC as requested; (2) hold position, confirm root cause, and propose a capacity fix (right-sized equipment) instead of a full disconnect; (3) continue diagnostics (packet capture, updated Airwall traffic report, ALC coordination) while keeping current connectivity live.
- **DECIDED 2026-07-28 (Darryl) — position set and communicated to the team by email** (to Scott Dunn, Sarah Monteleone, Syed Zaidi; cc Chad Steger, Nathan Kehr). Options 2 and 3 combined. **Wesco does not agree to a full AOC disconnect until correlation data exists.** Stated position: this is a controller capacity limit, not an entroCIM defect. Mechanism as Darryl framed it: building controllers have finite capacity for simultaneous connections and requests, largely consumed by native control traffic; entroCIM polling competes for the remainder; past the limit requests fail and on some controllers the failure degrades other device functions rather than dropping the single request. Disconnecting relieves pressure, which reads as entroCIM causing the problem when it exposed a device already at its ceiling. Precedent: FRB Distech deployment earlier this year, same shape.
- **Key analytical point (Darryl, 07-28): this is not a bandwidth problem.** A controller can fail this way while moving very little traffic. Jesse Dougherty never claimed entroCIM is flooding the network; he reported improvement when disconnected, which is true. Any Wesco response built on demonstrating low traffic volume answers a claim the customer did not make and will not survive their engineers' scrutiny.
- **Shawn's Airwall traffic report: HELD (Darryl, 07-28).** Sarah proposed re-running it to show other campus traffic was the cause. Rejected as the wrong instrument: the Airwall sits at a single point in the NAT building and measures traffic across the tunnel, so it cannot characterize the customer's local network, and it measures volume where the failure mode is concurrency. Scott's offered packet capture is retained as supporting detail only, since it sees the NAT building segment alone.
- **Crux question identified (Darryl, 07-28), from Scott's own 07-27 email:** several connectors are already disabled pending "updated hardware... to handle the traffic." **Whether that hardware was ever installed is likely dispositive.** If it was not, Wesco and ALC documented undersized equipment on this campus a year ago and current behavior is exactly what would be predicted. Answerable internally, before any customer contact.
- Diagnostic sequence directed to Scott Dunn (five steps, in order): (1) list connectors disabled last week, buildings served, and when; cross-reference against areas flagged with ALC last year; (2) determine whether the scoped hardware upgrades were installed; (3) re-engage ALC (Kevin, Jacob) for prior overloaded-segment findings, controller connection/request capacity, native load, and upgrade status; (4) put the correlation question to Jesse Dougherty — was the improvement isolated to buildings where connectors were disabled, or campus-wide, and do the improved areas match the ALC-flagged areas; (5) pull Wesco's own polling configuration against affected controllers (interval, concurrency, point count), since over-polling is self-correctable and offering that beats defending.
- **Customer-approach ruling (Darryl, 07-28): Wesco does not tell Coca-Cola their network is the problem.** Wesco has been disconnected twice with improvement both times; asserting fault without device-level evidence from that position damages the relationship and will not persuade their engineers. The customer is led to the conclusion through the diagnostic questions, so their own data points at the controllers. The conversation then shifts from removing entroCIM to what equipment delivers both their control function and the data.
- Risk of waiting: customer proceeds toward a full AOC disconnect before Wesco confirms root cause and offers an alternative; loses entroCIM data continuity and cedes the narrative that entroCIM is the cause.
- Open items: Scott to confirm or correct the diagnosis before Wednesday (C11); correlation data and hardware-installation answer (C12); Sarah to land Wednesday and close out whether the Coca-Cola Cyber audit items raised with Mike Reed are related (C13); Syed tracking (B18).
- **Record-quality note:** this entry was first built 07-28 from the Copilot evidence summary alone, which characterized the issue as a customer-perception/reopen risk against the 07-27 closed Airwall item. The full email thread and Darryl's technical context reversed that reading entirely. Logged to `10_Pilot_Feedback_Log.md`.
- **Update 07-30 (M365 evidence): no confirmation in this package that the Wednesday 07-29 Matt Shepherd meeting occurred, or that C11/C12/C13 landed** — absence is not evidence it didn't happen (evidence-coverage discipline), but treat all three as still open pending direct confirmation. **New same-day thread: a commercial Managed Services opportunity has surfaced alongside the technical dispute** — Coca-Cola/CBRE raised "thousands of unmanaged alarms" while the network investigation continues. Nathan Kehr: "Definitely set up the meeting on alarm management services ASAP," and separately asked to connect with Scott Dunn on the KMC controller tie-in before contacting Jesse Dougherty; Sarah Monteleone and Scott Dunn to set up a recurring meeting with Dan Fife and Jesse Dougherty (including Matt Shepherd). **Keep the technical root-cause question and the commercial Managed Services conversation sequenced separately** — leading with a services pitch before the controller-capacity question is resolved risks undermining the technical position Darryl set 07-28. Register B21 added (Nathan Kehr / Sarah Monteleone / Scott Dunn).
- **Update 2026-08-03 (M365 weekly evidence): escalated, not resolved.** The customer's ask moved from a one-day isolation test (07-22) to turning off the remaining connections entirely — evidence classifies this as increased risk, now a "customer-confidence and service-continuity issue, not only a technical troubleshooting item." Wesco's position (hold until correlation data exists, no full disconnect) is reconfirmed as the current internal decision, with five concrete diagnostic actions assigned to Scott Dunn this week: list disabled connectors/buildings/timing against prior ALC findings; confirm whether previously scoped hardware upgrades were installed (still the likely-dispositive question, C12, unanswered); re-engage ALC; put the correlation question to Jesse Dougherty; pull Wesco's own polling configuration. Sarah Monteleone is steering the customer conversation toward this diagnostic path rather than a disconnect decision. **Still no confirmation that C11 (Scott's correction/confirmation) or C12 (hardware-installation answer) has landed** — both now open for a second consecutive week. Register B18 updated with the five-item task list.

### 2026-07-28 — WAM financial narrative and resource allocation: P&L view and development carve-back (new)
- ID: D072
- Status: Approaching — no forum with a confirmed date yet
- Owner: Sean McCloskey, with Brad Stevens / Tom (likely Tom Boss, unconfirmed) / Nate Kehr / Darryl input
- Forum: No standing forum yet — recommend Darryl confirm scope and date directly with Sean McCloskey/Tom this week.
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- Context: Sync: Dirk & Akash meeting 07-28 moved WAM's financial framing toward a cash-flow P&L (vs. GAAP/acquisition view), with a package intended for Rob Cook targeted "next week" (date not confirmed — do not read as 2026-07-31 or 2026-08-07 without confirmation). Brad Stevens was explicit that deployment capacity must not be cut; development resources may be carved back or reallocated instead. A separate but linked thread: how to explain the WAM net-new-logo shortfall given a delayed marketing launch (reportedly pushed to September) and Amy Aguirre as a single-person dependency on WAM sales/project execution.
- Options considered: cash-flow P&L without amortized charges; GAAP P&L; sales P&L (per evidence, options as framed in the 07-28 session).
- Information still needed: which P&L view Sean intends to use, the actual "next week" date, what specific input Darryl is expected to supply (resource allocation / development-deployment split), and confirmed marketing-launch timing.
- Risk of waiting: package goes to Rob Cook without Darryl's resourcing input, or the net-new-logo shortfall is read as a product-execution failure rather than a go-to-market timing dependency.
- Follow-up: cross-reference `04_Executive_Watch_List.md` (new Active row) and the existing "entroCIM commercial performance vs. 2026 objectives" and "WAM executive-narrative risk" rows — distinct thread (WAM-specific resourcing and P&L framing), not a duplicate.
- **Update 07-30 (M365 evidence, Quick Connect on 2027 P&L for EntroCIM, 12:30-13:00): package mechanics now moving.** Tom Boss delivered updated July bookings and June financials for 2027 scenario planning (reclassified bookings flagged, Aatmunn anomaly removed) — sent to Nathan Kehr first, then circulated to the group, completed same day. Nathan Kehr's task: flag reclassified bookings in the bookings file (completed same day). Remaining: Sean McCloskey and Darryl to prepare a first-pass 2027 scenario analysis (hold costs constant vs. evaluate development-cost reductions, normalized net-new bookings) and circulate before the Rob Cook meeting; **Darryl owes confirmation of whether the Rob meeting is Thursday or Friday** — still unconfirmed as of this evidence. Register A14 (Rob meeting day confirmation) and A15 (scenario analysis prep) added.

### 2026-07-27 — Coda entroCIM environment: customer demo vs. presentation-only (new)
- ID: D073
- Status: Approaching
- Owner: Nathan Kehr / sales leadership (Darryl consulted)
- Forum: Darryl / Nate weekly 1:1.
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- Context: event and customer showcase planning for the Coda account; talking points and demo-stage requirements circulating (Natalia Shtern, Sarah Monteleone). Ties to the NexusCon 2026 speaking slot already logged in Decisions Made.
- Options considered: live customer demo of the Coda entroCIM environment, vs. presentation-only.
- Information still needed: customer willingness, internal approval.
- Risk of waiting: Medium — event preparation has a fixed date once NexusCon dates confirm, and NexusCon dates remain unevidenced.
- Follow-up: separate open thread on the same account — whether Coda signed the 2024-2029 cloud hosting renewal (Natalia Shtern awaiting confirmation; attribution Implied across Nathan Kehr and Darryl, raised as a confirmation question 07-27, not yet assigned).

### 2026-07-27 — WMX fulfillment data capture behaviour (new)
- ID: D067
- Status: Approaching
- Owner: product/operations stakeholders; Darryl driving the complex-build path
- Forum: Discussing WMX As-Is Process for fulfillment — 2026-07-28 (Register A1). (2026-07-28)
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: the forum date carried on this item has passed with no decision recorded and no forward date, so it fails the Radar's forum-plus-date test in substance. Content unchanged. Returns to the Radar when a new forum date is set.*
- **Update 08-10 (weekly evidence, "Discussing WMX As-Is Process for fulfillment"): the session postponed again — "postponed until key participants return," rescheduling for "next week."** This confirms the 08-04 read that Akansh was rescheduling "for Tuesday," but "next week" is itself undated. **Trigger backstop applies:** per the dating rule, an undated "next week" is an undated item in disguise — the actual next action is Akansh naming the specific date, not waiting for the session to land. A1 in Register A updated accordingly: due date removed, next step reset to "get the confirmed date from Akansh."
- Context: session scheduled to understand the as-is fulfillment workflow — scan workflow, attributes captured, downstream visibility. Directly relevant to the complex-build asset attribute gap (WMX lacks serial/MAC capability through at least 2028 absent action).
- Information still needed: what the scan workflow captures today and what reaches CPQ/OMS/WMX downstream.
- Risk of waiting: Medium — the end-of-July target on the complex-build decision path is Darryl's own, and this session is the venue.
- Follow-up: treat the session as a decision forum on the complex-build path, not only an as-is walkthrough. Confirm John Barlolotti at working level.
- **Update 2026-08-05 (daily evidence, session held 08-04 09:00-09:30):** a working position emerged, **use VAS for complex finished goods and WMX for simplified products**. Treat this as the session's working position rather than a ratified decision; it was recorded in facilitator notes, and the session was rescheduled again before closing. Akansh Gangil agreed to reschedule "for Tuesday" accounting for time zones so Steve Leslie can attend (**exact ISO date not stated in the source; likely 2026-08-11, unconfirmed — do not treat as fixed**). Open questions carried forward: WMX versus VAS ownership, whether capture is mandatory, P360 configuration, and impact to non-DDP sites. Follow-up tasks named at working level: add a work-instruction field for MAC address and serial-number capture (Steven Leslie, Govardhan Shetty) and share the Jira link for WMX asset-tracking enhancements in the WMX chat (Steven Leslie, John Bartolotti). The end-of-July target Darryl set has now passed without the decision path closing; the session has moved at least twice.

### 2026-07-27 — AI-enabled development pilot approved — Copilot + Claude Design, Orlando workshop
- ID: D035
- Owner: Sean McCloskey (direction), Digital Products leadership (execution)
- Forum: Digital Products / Agile Staff Meeting.
- Next action: Sean owes Darryl's team (and Dj Vaughn) additional Claude Design licenses — track under Commitments Owed to Darryl (05).
- Added: 2026-07-27 (M365 weekly evidence — Digital Products / Agile Staff Meeting 07-21)
- Context: a pilot for a fully AI-enabled development cycle using GitHub Copilot and Claude Design was approved, including a planned two-day Orlando workshop for portal requirements and design (feeds the QPMSupport portal initiative). Moves AI adoption from concept into a live delivery-method experiment — connects directly to the standing "AI adoption governance + team assignment" watch item and to Darryl's owed deliverable (product ideas + AI-researched needs analysis for Sean).
- Risk of waiting: Claude Design license distribution and product-owner training are unresolved — the pilot could proceed unevenly across teams without them.

2026-10-19 (Claude, weekly brief): Moved from Decision Radar to Backlog at the register cap (Radar 25 against 20). Reason: fails the Radar entry test, no named forum with a live date; not touched since July and no forward date on record. Content unchanged. Returns to the Radar the moment a forum and date exist.

### 2026-07-27 — Product ownership model shift — two-tier structure (GPO peer + Claude Design owner)
- ID: D034
- Owner: Sean McCloskey (per evidence, Inferred — not independently confirmed)
- Forum: Digital Products / Agile Staff Meeting (weekly).
- Next action: confirm this reading directly — evidence marks the decision-maker as Inferred, and it materially changes product-owner role expectations across the portfolio.
- Added: 2026-07-27 (M365 weekly evidence — Digital Products / Agile Staff Meeting 07-21; decision-maker Inferred as Sean McCloskey)
- Context: product ownership model shifting toward a two-tier structure — a GPO peer role and a Claude Design owner role — with training and license distribution not yet resolved. Affects how product requirements, customer sessions, design artifacts, and handoffs get owned going forward; touches hiring/staffing expectations.
- Risk of waiting: the AI-enabled development pilot and new ownership model could stall or land inconsistently across teams without a license/training plan.

2026-10-19 (Claude, weekly brief): Moved from Decision Radar to Backlog at the register cap (Radar 25 against 20). Reason: fails the Radar entry test, no named forum with a live date; not touched since July and no forward date on record. Content unchanged. Returns to the Radar the moment a forum and date exist.

### 2026-07-27 — Dell/Wesco service management process — handoff model across Freshdesk and ServiceNow (new 2026-07-27)
- ID: D033
- Owner: Syed Jamshed Zaidi, with Darryl, Scott Dunn, Adam Lazare; Dell-side participants unconfirmed
- Forum: Dell Service Management Process — met 2026-07-27; add to `07_Operating_Cadence.md` once cadence/owner confirmed. (2026-07-27)
- Next action: bring the proposed current-state process map and the two recent process misses (Limerick, Non-DC) as concrete examples.
- Added: 2026-07-27 (M365 weekly evidence — Teams chat with Syed Jamshed Zaidi 07-24; Dell Service Management Process meeting 07-27)
- Context: current Dell support workflow is manual and unscalable (this is the same underlying gap flagged 07-21 as "Dell ServiceNow/Freshdesk support workflow redesign," now with a scheduled forum). Evidence states two recent Dell issues did not enter the established Wesco support process promptly — an operating-model gap, not a single-ticket problem. Directly relevant: this is the same team carrying Dell Limerick and Dell Non-DC HQ dashboard escalations (Watch List).
- Options: continue current workflow vs. document and redesign the current-state process (Dell internal support, Freshdesk, ServiceNow escalation, handoffs, ownership, closed-loop communication).
- Risk of waiting: customer experience degradation compounds with each new Dell escalation; this consolidates the prior "ServiceNow Field Services integration path" and "Dell workflow redesign" entries into one forum.
- **Update 07-28 (M365 evidence): two named owner commitments from the 07-27 meeting — Syed Zaidi to schedule a follow-up workshop with Drew Connorton (new name) and additional stakeholders; Scott Dunn to update ticketing/routing documentation.** Follow-up workshop is the next forum occurrence; cadence still not confirmed (A10). Separately, a third Dell thread surfaced same day: PC1 meters offline (ticket 3046, Robert Tefft) — Scott Dunn investigating; possibly the same underlying pattern as the Non-DC dashboard gap (A2), not yet confirmed distinct.

2026-10-15 (Darryl, web): 1. test text
2. COOL
- Bullet
-

### 2026-07-27 — entroCIM release governance tightened — DCOE-driven production controls (new 2026-07-27)
- ID: D032
- Owner: Ron Snyder
- Forum: Daily Stand Up (entroCIM).
- Next action: confirm with Ron that the new controls are applied consistently, not just discussed once; watch whether the shared-component/repo decision lands on the same governance model.
- Added: 2026-07-27 (M365 weekly evidence — Daily Stand Up 07-21)
- Context: distinct from the already-closed 07-22 DCOE compliance-hold entry (that one was about release 3.1.12.13 specifically and is resolved/approved). This is a **forward-looking process change**: production code now requires tagging, two reviewers, a GitHub commit, conventional-commit format with JIRA issue numbers, and documented testing evidence before release. Ron stated the standup-cycle release was on hold pending this sign-off discipline.
- Risk of waiting: inconsistent adoption across teams could leave DCOE evidence gaps recurring rather than resolved; a related open decision (shared UI component/helper repo and release-documentation strategy across front-end teams — Joseph Kusnir, Priyatosh Patra, Michael Pieschel, David Blondel, Ron Snyder) could keep release evidence inconsistent if not aligned to the same standard.

2026-10-19 (Claude, weekly brief): Moved from Decision Radar to Backlog at the register cap (Radar 25 against 20). Reason: fails the Radar entry test, no named forum with a live date; not touched since July and no forward date on record. Content unchanged. Returns to the Radar the moment a forum and date exist.

### 2026-07-24 — FY27 AOP resource allocation — Build vs. COGS
- ID: D080
- Owner: Darryl, with John Erickson and finance stakeholders
- Forum: not yet assigned — natural fit is the same Sean McCloskey AOP track. Don't run this as a separate thread from the Aug-21 alignment meetings already committed with Lisa, Brad, and Gregg O'Brien.
- Next action: Darryl to align financial goals, capacity model, and capabilities with John Erickson.
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- Added: 2026-07-24 (M365 evidence — entroCIM FY27 AOP package + Teams chat with John Erickson)
- Context: FY27 AOP demand-collation template and CSS_Platform_Team.xlsx resource file delivered — this is the planning-cycle mechanics feeding the Aug-21 AOP alignment deadline and Aug-31 AOP input deadline already tracked under the AI roadmap / Device Lifecycle Assurance entries above. Options: Build vs. COGS allocation model and capability-investment mix.
- Risk of waiting: planning-cycle delay; misalignment between capacity model and financial targets going into the Aug-21/Aug-31 gates.
- **Update 2026-08-03 (M365 weekly evidence, "FY27 AOP: VERY IMPORTANT AND TIME SENSTIVE" email): the mechanics sharpened to a mandatory, dated deliverable.** John Erickson named Darryl by role against both products — "entroCIM — Darryl" and "Wesco Asset Management — Darryl" — for FY27 AOP business-case and scoring submission, **due on or before 2026-08-21**. This is two business cases in one planning window, not one. A3 (today's working session with Erickson) is the input; the AOP submission itself is the dated gate — added to Register A as A19.

### 2026-07-22 — entroCIM commercialization model — short-term payback vs. strategic scale-up (new 2026-07-22)
- ID: D090
- Owner: not yet assigned — materials name this as the central leadership decision
- Forum: not yet assigned — natural fit is the Sean McCloskey / Akash Khurana track already carrying WAM/entroCIM reset and portfolio-strategy discussions.
- Next action: name a decision owner and executive sponsor; this pairs directly with the existing "entroCIM commercial performance vs. 2026 objectives" watch item — don't let the two threads run separately. Nearer-term: the send itself (Mike Wassil) is the gating event — until sent, no leadership decision clock is running.
- Added: 2026-07-22 (M365 evidence — updated commercialization/competitive-landscape materials: `Wesco_entroCIM_Commercialization_2026-07-22_v5`, `Wesco_entroCIM_Competitive_Landscape_Report_2026-07-22_v2`)
- Context: updated decks frame entroCIM as a live test of Wesco's services-led commercialization model. Path A: treat as a short-term payback problem. Path B: strategic scale-up with a sponsored-access/incubation structure, aligned incentives, and dual metrics (realized + option value).
- Options considered: Path A (short-term payback) vs. Path B (strategic scale-up with incubation contract, pilot accounts, scorecard, incentive model).
- Risk of waiting: materials flag "slow starvation" — option value erodes and side-of-desk selling continues if no owner is named.
- **Update 07-24 (Darryl + full-document analysis):** both source files analyzed directly (correcting the 07-22 evidence read — the companion is `Wesco_entroCIM_Commercialization_Report_2026-07-22_v5`, a 27-page report, not a separate "Competitive_Landscape_Report v2"; the landscape content is inside it). Built with **Nathan Kehr and Michael Wassil**; audience Engel/Khurana/McCloskey; **status: internal draft v5 — not sent until Mike Wassil sends.** Darryl classifies them as market positioning for entroCIM. Full summary: `Products/entroCIM/Wesco_entroCIM_Commercialization_Summary_2026-07-22_v5.md`. Detail now on record: Path B = incubation contract (12/18/24-month milestones, sponsored access, default-include, dual metrics); the ask is explicitly enablement (external MarComm refresh + internal incentive alignment), not headcount/capital; seven executive decisions listed with recommended directions, owners to be assigned; 90-day staged pilot with gates; report deliberately sets no deadline. Two framing-consistency flags for Darryl (deck's "no new capital" vs. the $1.44M AOP sustaining ask; Path B growth language vs. AOP "frame as sustaining" rule) — see the summary file.

### 2026-07-22 — AI-enabled workflow governance — WAB approval gate for IDP (corrected 2026-07-22)
- ID: D088
- Owner: Akansh Gangil (IDP integration value/scope); Scott Frost (governance contact)
- Forum: IDP/WAM Process Review.
- Next action: Darryl to set up an MDM attribute progress follow-up with the MDM team (committed 07-22, still open); Akansh to bring value/document-type scope to the next Process Review.
- Added: 2026-07-22 (M365 evidence — IDP/WAM Process Review)
- **Correction 07-22 (Darryl, field note): "WOB" was a naming error — it should read WAB (Wesco Architecture Review Board), the same board already tracked for the Claude-code and JCI API-connection approvals. There is no separate WOB body; retire that naming caution.**
- **Correction 07-22 (Darryl, field note): IDP integration is NOT blocked by WAB approval.** The team is working on the value case for IDP integration and which document types it covers; Akansh Gangil owns this. Re-scope from "governance-blocked" to "scoping in progress" — remove from the AI-governance escalation framing below.
- Context: IDP/WAM AI-document-extraction POC requires re-validation against current supplier documents before integration decisions proceed.
- Risk of waiting: value case takes longer to land if document-type scope isn't prioritized; no longer an approval-gate risk.

### 2026-07-22 — Mapbox token exposure remediation (new 2026-07-22)
- ID: D031
- Owner: Ron Snyder / Boris (security) / Priyatosh Patra / Shubham Kumar Singh
- Forum: Daily Stand Up; raise directly in the Darryl–Ron 1:1 if no rotation plan lands this week.
- Next action: Ron to confirm rotation timing and customer-impact plan with security (Boris).
- Added: 2026-07-22 (M365 evidence — Daily Stand Up 07-22)
- Context: a Mapbox token was exposed in git history. Immediate revocation could break customer-facing maps; team prefers a coordinated rotation with a grace period over relying on git-history filtering alone.
- Options: rotate with a grace period and customer-impact plan vs. immediate revocation vs. git-history filtering only.
- Risk of waiting: security exposure persists the longer rotation is deferred; conversely, an uncoordinated revocation breaks customer map functionality.
- **Update 07-27 (M365 weekly evidence, Daily Stand Up 07-22): sharper detail on the constraint — existing tokens are customer-facing, and revocation could disrupt maps specifically for on-premise customers who haven't received a pod update.** Stated team preference: token rotation over git-history filtering, coordinated with security. Commitments: Ron to meet with Boris on the leaked-token issue; Priyatosh Patra to rotate the exposed token and send the updated token to Boris. No rotation date confirmed yet — still open, not resolved.

2026-10-19 (Claude, weekly brief): Moved from Decision Radar to Backlog at the register cap (Radar 25 against 20). Reason: fails the Radar entry test, no named forum with a live date; not touched since July and no forward date on record. Content unchanged. Returns to the Radar the moment a forum and date exist.

### 2026-07-22 — GitHub Copilot enablement — blocked by Vibe Guard compatibility (new 2026-07-22)
- ID: D022
- Owner: AI leadership stakeholders (unconfirmed beyond evidence)
- Forum: Digital Products / Agile Staff Meeting.
- Next action: security direction needed before a path is chosen.
- Added: 2026-07-22 (M365 evidence — Digital Products / Agile Staff Meeting)
- Context: GitHub Copilot access blocked by Vibe Guard compatibility concerns. Distinct thread from the IDP/WOB governance item above and from the Claude-code WAB approval track — three separate AI-tooling governance questions now open at once.
- Options: SOP update vs. tooling change.
- Risk of waiting: developer productivity impact; AI-pace dissatisfaction (Sean, already tracked) compounds if multiple AI-tooling paths stall simultaneously.

2026-10-19 (Claude, weekly brief): Moved from Decision Radar to Backlog at the register cap (Radar 25 against 20). Reason: fails the Radar entry test, no named forum with a live date; not touched since July and no forward date on record. Content unchanged. Returns to the Radar the moment a forum and date exist.

### 2026-07-21 — Dell ServiceNow/Freshdesk support workflow redesign (new 2026-07-21)
- ID: D089
- Owner: unconfirmed — evidence infers Operations leadership
- Forum: none assigned yet — recommend folding into the existing "ServiceNow Field Services integration path" decision above rather than tracking as a separate initiative, given the overlap.
- Added: 2026-07-21 (M365 evidence — Three Amigos chat)
- Context: current Dell support workflow described as manual and unscalable. Directly relevant today: the Dell Limerick alarming escalation (see Watch List) is live evidence of this gap, not a hypothetical.
- Options: continue current workflow vs. redesign/integrate.
- Risk of waiting: customer experience degradation compounds with each new Dell escalation.

### 2026-07-21 — VOS/CPQ supplier PO handling — release 3.4.2 (new 2026-07-21)
- ID: D079
- Owner: Sean McCloskey and portfolio team
- Forum: Digital Products Portfolio Review (cadence/owner still unconfirmed — see existing entry in `07_Operating_Cadence.md`).
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- Added: 2026-07-21 (M365 evidence — Digital Products Portfolio Review, additional detail beyond the 07-20 entry)
- Context: integration design question for release 3.4.2 — include supplier PO information handling now vs. defer/workaround.
- Options considered: include now vs. defer/workaround (per evidence; dependency, testing, and backflow impacts not yet detailed).
- Risk of waiting: release delay or rework if the decision lands late.

### 2026-07-20 — QPM 3.4.3 / Charlotte go-live — cross-team release commitments (CPQ, Oracle, OMS)
- ID: D081
- Owner: Kiranmai (task owner per Loop notes) with CPQ, Oracle, and OMS teams; Anna/John named on Oracle capacity review. Roles unconfirmed — new names, not yet in `06_Stakeholder_Map.md` with confirmed reporting lines.
- Forum: Digital Products Portfolio Review (cadence to confirm — not yet in `07_Operating_Cadence.md`).
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- Added: 2026-07-20 (M365 evidence — Digital Products Portfolio Review)
- Context: QPM 3.4.1 complete; 3.4.2 focused on WMX integrations and customer-care connection; **3.4.3 carries the nested finished-good capability required for the Charlotte go-live** and is not yet committed by CPQ, Oracle, or OMS. Oracle capacity/requirements review also outstanding.
- Options considered: not yet specified in evidence — task is to obtain commitments and run the capacity review, not a scoped options set.
- Risk of waiting: Charlotte go-live readiness is exposed to three external teams' commitment timing with no confirmed dates yet.
- Follow-up: request a one-page 3.4.3 dependency map (owner, commitment date, risk status) from Kiranmai; disambiguate "Anna" and "John" against existing stakeholder-map entries (Anna Baker/Anna Thornton; John Engel/John Barlolotti) before attributing further actions to them.
- **Update 07-27 (M365 weekly evidence, Digital Products / Agile Staff Meeting + Digital Products Portfolio Review 07-20/21): status worsened — notes state the team is "significantly behind" on 3.4.3, with a decision expected at an upcoming report-out call.** Apparent owners named more specifically this cycle: **Sudhi Rao and Anna Baker**, target to finalize requirements and CPQ/QPMSupport alignment in the **first week of August**. Second open question: how a 3.4.3 delivery-date shift affects dependent Digital Products commitments — not yet assessed. **Name-collision note:** this evidence gives "Anna Baker" with surname (Loop notes, decision-maker inferred) — this may resolve the 07-20 "Anna" ambiguity, but treat as probable, not confirmed, until corroborated independently; her existing tracked scope (DDP/MDM, Monday Entrance Call) doesn't obviously overlap with QPM ownership.
- Risk of waiting (updated): Charlotte go-live exposure is now a schedule problem, not just an unconfirmed-commitment problem — "significantly behind" is a harder signal than the 07-20 read.

### 2026-07-20 — Connected Safety — take on as a digital product?
- ID: D030
- Owner: Darryl (recommendation) → Sean McCloskey
- Forum: Sean McCloskey discussion (same message as CMP).
- Added: 2026-07-20 (Darryl, Brad Stevens conversation)
- Context: Sean Gregg's replacement not yet named; program in limbo until then. Question: does Darryl's team take Connected Safety on as a digital product? Not the biggest business, but needed across customers and divisions. Pros and cons acknowledged, not yet enumerated.
- Options: take on as digital product / leave with the successor org once named / hybrid (platform support without program ownership) — to be worked before the Sean discussion.
- Risk of waiting: low near-term (program is parked), but limbo has no owner and no clock; a successor hire could foreclose the option.

2026-10-19 (Claude, weekly brief): Moved from Decision Radar to Backlog at the register cap (Radar 25 against 20). Reason: fails the Radar entry test, no named forum with a live date; not touched since July and no forward date on record. Content unchanged. Returns to the Radar the moment a forum and date exist.

### 2026-07-20 — CMP (Cellular Management Platform) — where does the tool reside?
- ID: D029
- Owner: Darryl + Sean McCloskey (portfolio placement); Brad Stevens driving the business side
- Forum: Sean McCloskey discussion (Teams message raising it drafted 07-20).
- Added: 2026-07-20 (Darryl, Brad Stevens conversation)
- Context: CMP manages any Wesco-sold product carrying a cellular plan (SIM). Built by Fanny Scargle (Dir. Business Development, UBS; cellular SME) with Merwan's team; the tool is the mechanism. Brad Stevens may pull Fanny into his team to own the business side, which leaves tool ownership/residence open.
- Risk of waiting: if Fanny moves before placement is discussed, the tool's home gets decided by default rather than by portfolio logic.

2026-10-19 (Claude, weekly brief): Moved from Decision Radar to Backlog at the register cap (Radar 25 against 20). Reason: fails the Radar entry test, no named forum with a live date; not touched since July and no forward date on record. Content unchanged. Returns to the Radar the moment a forum and date exist.

### 2026-07-20 — WAM/ADM operational hardening plan — sequencing and gate scoping
- ID: D027
- Owner: Akansh Gangil / WAM-ADM team (execution); Darryl sets the gate standard and sequencing expectations
- Forum: WAM Product Backlog Refinement (bi-weekly) + the one-page MVP1 gate view requested from Akansh — recommend expanding that gate view to cover cleanup sequencing, activation fixes, and scheduler investigation.
- Added: 2026-07-20 (verbose meeting dump, WAM Product Backlog Refinement — filed as `WAM_Product_Backlog_Refinement_Problems_Work_Plan_2026-07-20.md`; exec summary in `Deliverables/2026-07-20_WAM_Operational_Hardening_Executive_Summary.md`)
- Timing (Darryl, 07-20): the bugs surfaced after the 07-03 DDP/EUDM integration go-live — the most recent production update — and the teams have been finding and defining them since. The Backlog Refinement session consolidated that discovery work.
- Context: Backlog Refinement was a data-quality stabilization session — seven problem areas with work plans: (1) cancelled-order contamination (one-time hard delete + three tracks: data-layer status, UI exclusion, audit tab), (2) reported data loss (working conclusion: data intact, visibility defect — bug 7827), (3) license activation failures (null start dates / missing SO dates the main driver), (4) duplicate record creation in lower envs, (5) filter scalability (~50K records; architecture review before implementation), (6) ADM database growth (archival strategy needed), (7) end-user matching normalization. Items 1–3 overlap the MVP1 Aug 3 gate (tracked in that entry above).
- Open decisions: (a) **sequencing conflict — the one-time hard delete of cancelled records precedes the audit tab (Track C); without a pre-delete snapshot/export, traceability is lost, contradicting the plan's own intent**; (b) whether a new "removed" status is added to the data model (Tracks A/B depend on it); (c) which items are on the Aug 3 critical path; (d) named owners/dates per track — not yet in the record.
- Risk of waiting: hard delete runs unaudited; "data loss" perception hardens with Sales Ops (Natalie/Debbie Hunter) before the intact-data narrative is placed.
- Evidence note: transcript/Loop-sourced; speaker attributions (Akansh, Krishnanunni) unconfirmed per evidence discipline.
- **Update 08-05 (WAM Backlog Deep Dive deck):** two of the seven problem areas now show closure. The post-EUDM-integration defect and ADM UI slowness under large data volume are both marked complete in Sprint 26Q3 Sprint 2. License activation failures (item 3, null/missing SO dates) remain ongoing, as do cancelled-order removal and automatic identification of cancelled line license records (item 1). The deck does not address items 4 through 7 (duplicate creation, filter scalability, database growth/archival, end-user matching), so absence of mention is not closure. Open decisions (a) through (d) above remain open; in particular the hard-delete-before-audit-tab sequencing conflict is still not addressed in any artifact, and the Q4 roadmap item "removing cancelled license orders automatically" is where it will surface if unresolved.

2026-10-19 (Claude, weekly brief): Moved from Decision Radar to Backlog at the register cap (Radar 25 against 20). Reason: fails the Radar entry test, no named forum with a live date; not touched since July and no forward date on record. Content unchanged. Returns to the Radar the moment a forum and date exist.

### 2026-07-16 — ServiceNow Field Services integration path
- ID: D084
- Owner: Ron Snyder (intake) / Sean Comunale (Brady approval, backlog position); Darryl tracks the approval milestone only
- Forum: decision returns when intake approval + backlog position land; recommend Darryl or Ron raise the rejection directly rather than waiting on the standard backlog path.
- Added: 2026-07-16 (M365 evidence)
- Context: dev-environment path identified; production needs licensing + Infosys coordination; ServiceNow team backlog significant.
- **Update 07-22 (M365 evidence, Teams chat w/ Ron Snyder): Ron replied "Not yet" on ServiceNow module access** — still not unblocked; timing update Darryl asked for on 07-21 has not landed.
- **Update 08-10 (weekly evidence): escalated from delay to outright rejection.** The dev-environment access request was auto-rejected, not merely pending. New name in the approval chain: **Nathan Haines** (role unconfirmed). This blocks entroCIM connector development and any future ServiceNow-based customer offering — moved to `04` Watch List as a new Active row (High, New) given the harder signal. Risk reclassified below accordingly.
- **Update 08-12 (entroCIM Backlog Deep Dive): reconfirmed still blocked, second consecutive cycle.** No new information on the rejection itself; evidence characterizes the dependency trend as "Rising." No internal owner has responded to Nathan Haines / the approval chain since the 08-10 rejection — still a live gap, not just a slow one.
- Options: dev-only POC; production licensing path; customer-environment pattern; escalate the rejection directly with Nathan Haines / the approval chain rather than re-request.
- Risk of waiting: raised from low to Medium-High — a rejection needs a named response, not another status check. Now two cycles of silence on that response.

### 2026-07-16 — DDP/global attributes ownership (DDPTRK-6346)
- ID: D076
- Forum: Monday DDP Entrance Call (new — add to `07_Operating_Cadence.md` if it recurs).
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- Added: 2026-07-16 (M365 evidence). **Ownership decided 2026-07-16 (Darryl, field note):** Akansh owns the global-attribute issue itself (working the GPO/MDM teams to get attributes defined, decided, and worked). David Blondel owns the supplier-relations side — pushing Jarod Booth's team, then the Assortment team, to get data into the system over time.
- **Correction 07-16:** an earlier deliverable (Sean Meeting Brief) mislabeled David Blondel as being "in Jarod Booth's org." David reports to Darryl (confirmed in `06_Stakeholder_Map.md`); he is pushing Jarod's team, not part of it.
- Progress 07-16 (Darryl field note): second Data Requirements meeting didn't happen as scheduled, but Dan Totino called Darryl directly — got Priyambada Dash and Gandhi Subramanian on the line. They will action the 6 attributes in the ticket. Next: sync with the Governance team (dependency creation) — technical and governance classes in parallel. Gandhi will read the ticket and route questions to Dan and Darryl. **Anna Baker has invited Darryl to the Monday DDP Entrance Call** to keep DDPTRK-6346 tracking inside the broader DDP plan.
- Context: downstream impact — product classification, software/hardware differentiation, warranty/subscription handling, notification logic.
- Risk of waiting: reduced — attendance/ownership gap that stalled 07-15 is now addressed with named owners and a standing check-in (Monday Entrance Call).

2026-10-19 (Claude, weekly brief): DDPTRK-6346 marked completed in the Digital Products Portfolio Status Update. The ownership decision this entry records (07-16) has run its course; candidate to close with B12 on Darryl's confirmation. `Evidence/M365_Evidence_Weekly_2026-10-19.md`

### 2026-07-16 — WAM MVP1 notification rollout — production readiness gate
- ID: D018
- Owner: Akansh Gangil / Natalie Marquardt; Darryl sets the gate standard
- Forum: WAM Product discussion (weekly); WAM Product Backlog Refinement (bi-weekly); Darryl asked Akansh for a one-page gate view.
- **Update 08-10 (weekly evidence, ADM connect with Natalie): release confirmed for today — US and Canada rollout of the Notification to Sales Rep suite and Milestone/ExacQ data load.** Two gate items land the same day: (1) cancelled sales orders are being manually removed before release while automation is developed (the hard-delete-before-audit-tab sequencing risk flagged 07-20 still applies — confirm a pre-delete snapshot exists); (2) Akansh Gangil owes Natalie Marquardt the recipient list and sample notification data before deployment (Explicit, due today — new Register B item). This is the same date the 08-05 Backlog Deep Dive deck named as a target; today's evidence is the first confirmation rather than a target. Natalie separately owes Akansh the FAQ SharePoint URL and email text (not dated). Confirm with Akansh by end of day whether the release actually shipped — do not assume from the plan alone.
- Added: 2026-07-16 (M365 evidence: WAM Product discussion + license-expiration thread)
- Context: rollout shifted to tentative **2026-08-03** while feedback lands. Gate items: final supplier exclusion list (Natalie), cancelled-line cleanup validated (one-time tested; recurrent needs scheduler design), sender/format changes, SharePoint/FAQ live. Separately: EUDM license-order feed is delivered but **manually triggered daily** (clustering issues) — automation is not production-grade yet and must be stated honestly in exec framing.
- **Update 07-20 (M365 evidence, WAM Product Backlog Refinement):** cancelled-item cleanup scope sharpened — cancelled ADM items must be removed from the UI and excluded from analytics, exports, search, filters, and renewal views, with a **separate removed/cancelled orders tab**. Still undecided: whether a new "removed" status is needed. Separately, **missing SO dates are blocking license activation** (pending activations, perceived data loss though data remains in the database — bug 7827) and **some UDM records aren't being picked up by the DDP scheduler**; root cause and priority trade-off vs. other sprint items still open. Both are gate items, not yet scoped into the Aug 3 timeline explicitly — confirm with Akansh whether they're on the critical path.
- Risk of waiting: premature/inaccurate notices burn Sales/Sales Ops trust — direct hit to the WAM reset narrative. Missing-SO-date/scheduler gaps compound this: customers may perceive data loss even though none occurred.
- **Update 07-28 (ADM connect with Natalie): possible date-slip signal, not confirmed.** Akansh: "I'm not committing, let me come back on that. But yeah, most probably it will be 10th of August" — treat the 08-03 gate as at risk, not moved, until Akansh commits to a date. Full detail in `04_Executive_Watch_List.md`.
- **Update 08-05 (WAM Backlog Deep Dive deck, presented 08-06):** 2026-08-10 now appears as a named release date on a slide for the Notification to Sales Rep suite and the Milestone/ExacQ data load. Firmer than the 07-28 verbal, still a target rather than a confirmed release. UAT testing of the notification suite is marked complete; the post-EUDM-integration and ADM UI performance defects are marked closed; license activation remains open. **Gate-standard question now live for Darryl:** the deck's stated Q3 outcome is that expiry alerts route to the owning rep *and* that end dates are supplier-sourced and trustworthy (Milestone, ExacQ). Those were previously separable; pairing them in one quarter effectively raises the gate, because an alert on an untrusted date is the failure mode this gate exists to prevent. Worth confirming that the supplier-sourced dates are in place for the 08-10 send, or that the send is scoped to the products where they are.
- **Contested fact, unresolved 08-05:** this entry's statement that the EUDM license-order feed is manually triggered daily and "not production-grade" is contradicted by the deck, which marks an automated three-times-daily DDP/EUDM sync as Q2 complete. Not closed from the deck alone per closure discipline. Confirm with Akansh; the claim has already been used in outbound material (Lisa Orton brief, 08-05).
- **Update 08-06 (M365 evidence — Requirement Estimation: Asset Data Capture, Historical Data Migration & Order Capture Beyond Supplier ID, Nitin Pandey/Akansh Gangil):** new delivery estimates for four major data capabilities now span **2026-10-08 through 2027-02-03** — well past the notification-suite gate this entry tracks. This is a separate workstream (data capabilities, not the notification rollout) but the dates materially affect roadmap expectations and customer messaging. Do not let a Q3/Q4 notification narrative imply the underlying data capabilities land on the same horizon. See `04_Executive_Watch_List.md` (WAM/ADM data integrity row) for the customer/benefits-timing framing.

### 2026-07-14 — Supplier attribute data ownership (RACI)
- ID: D086
- Owner: not finalized — spans Supplier Relations, Data Governance, product content, WAM/ADM
- Added: 2026-07-14 (ADM connect + Vendor Data meetings). Updated 2026-07-15 (M365 evidence): vendor master-data strategy advanced — agreement to append new attributes and engage suppliers by revenue priority — but this is process progress, not an ownership decision. Third consecutive forum without a named accountable owner.
- Risk of waiting: supplier data stays incomplete/unmanaged — direct hit to WAM quality, renewals, tax attribution, benefits realization. This is the "data-model alignment unowned" pattern now concrete.
- Next action (Darryl, 07-15): name a decision forum and date — none currently assigned in `07_Operating_Cadence.md`.
- **Update 08-17 (weekly evidence, ADM connect with Natalie): global attribute prioritization routed into future sprint planning, apparent owner "Gandhi team."** David Blondel pinged Jared/Jarod Booth again to follow up (`05` B1, ongoing). This is the same unowned pattern reconfirmed — sprint prioritization is a scheduling mechanism, not an ownership decision, and the weekly evidence itself flags this topic as reappearing across ADM/WAM discussions without resolution. Now a standing candidate for the monthly Decision Backlog review rather than continued re-surfacing at the same unresolved state.

### 2026-07-14 — Complex-build asset attribute path (post-ACT: WMX vs VAS vs CPQ)
- ID: D078
- Owner: Akansh Gangil / Sudhi Rao; roadmap authority: GPO = John Barlolotti (Steve Leslie delegated the GPO role for WMX to him, per Darryl 07-17 — Steve remains a participant, not the decision authority).
- Next action: Wednesday 07-22 follow-up; confirm whether John Barlolotti (new GPO) needs to be brought into that session or a separate one for roadmap buy-in.
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- Added: 2026-07-14 (VAS Roadmap meeting). Updated 2026-07-15 (M365 evidence): gap **formally identified** — WMX lacks serial/MAC/complex-build capability "through at least 2028" absent action. Escalated to High on Watch List.
- Goal (Akansh's framing): track shipped-hardware asset details — asset tag, MAC address, serial number — including parent-child/finished-goods relationships, surfaced to customer/integrator on the Strev platform; must align with overall DDP strategy.
- Agreed decision path:
1. Akansh → Steve Leslie + Sid Sarna (WMX solution architect, Dir. Enterprise Applications): does WMX capture serial/MAC for complex builds? process + gap understanding;
2. bring in Alan for detail/opinion;
3. GPO buy-in for roadmap — now routes through John Barlolotti;
4. user buy-in (Troy Doyle) — Sudhi: users are the strongest lever but establish limitations first.
- **Update 07-17 (Darryl): follow-up on WMX scheduled Wednesday (2026-07-22) with Sid Sarna and Steve Leslie.** Target: decision path complete by end of July.
- Library lesson applies: validate source-data fitness before funding integration.

### 2026-07-14 — Which AI projects Darryl's team takes on
- ID: D077
- Owner: Darryl, at Sean McCloskey's request (attribution corrected from Maddy Taylor)
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: no named forum with a confirmed date, which is the Radar's entry test. Content unchanged. Returns to the Radar the moment a forum and date exist.*
- Added: 2026-07-14 (Agile Staff)
- Next: get Power BI access → shortlist by capability fit + CSS stakeholder synergy → bring candidates, dependencies, and realistic team ownership to Sean (Wednesday if access arrives in time).

### 2026-07-13 — CSS Platforms product strategy: team/org structure and resource alignment
- ID: D068
- Owner: Darryl (proposal) → Sean McCloskey (endorsement/decision)
- Forum: Sean meeting — moved to Thu 2026-07-16 (Sean at HQ through Wed). Also covers Akash/Dirk WAM meeting prep. (2026-07-16)
- Next action: confirm meeting acceptance; prepare strategy one-pager.
> *Moved from Decision Radar to Backlog 2026-08-19 at the register cap re-rank. Reason: the forum date carried on this item has passed with no decision recorded and no forward date, so it fails the Radar's forum-plus-date test in substance. Content unchanged. Returns to the Radar when a new forum date is set.*
- Added: 2026-07-13 (field note)
- Context: Broaden team scope across entroCIM, WAM, CSS AI backlog, and Navigator; align resources and costs with portfolio priorities; Product/Platforms/Deployment org structure.
- Risk of waiting: budgeting and ownership ambiguity persists across the expanded portfolio; this is the upward-alignment move the baseline flagged as missing.

### 2026-07-13 — Support-model realignment — scoped 07-15
- ID: D021
- Forum: (1) confirm CSS/TSS ownership when the MS conversation next surfaces at CSS level; (2)+(3) entroCIM Leadership Collaboration once Adam's internal CX alignment lands (post-coverage window realistically).
- Added: 2026-07-13 (All Hands). **Clarified 2026-07-15 (Darryl):** entroCIM team owns product support — SLA, effort, progress tracking, and pricing feedback to sales. The Managed Services piece will most likely be owned by CSS/TSS (not Darryl's team). Scott Dunn is delivery-focused; Amy Aguirre is not in Darryl's org (parallel to Nathan Kehr for WAM, with her own WAM delivery team).
- Remaining decisions: (1) formalize CSS/TSS ownership of Managed Services — outside Darryl's team; his role is confirming, not owning; (2) define the product-support ↔ Managed Services interface (escalation path, SLA boundary, pricing inputs); (3) internal CX-app ownership (first alignment attempt failed — Adam Slingerland leading redo with Keith Bishop/Prady, per Chad's handoff).
- Risk of waiting: reduced — the ownership shape is now understood; residual risk is the undefined interface surfacing as customer inconsistency (FRBNY is the live example).
- **Update 07-30 (M365 evidence, Re: 211 West Fort St - Tridium Info Request): second live test case — Colliers (211 West Fort St).** Customer has hosting only, no formal support agreement, and has received occasional free support in the past; the thread exposed conflicting CSM-vs-Support expectations. Mike Reed sent the immediate customer response but explicitly asked Darryl for leadership direction on the operating model (CSM-owned, Support-owned, paid T&M, or fixed-fee SLA). Register A16 added. This is the same undefined-interface risk as FRBNY, now with a second, independent instance — worth treating as a pattern rather than two one-off account issues.

2026-10-19 (Claude, weekly brief): Moved from Decision Radar to Backlog at the register cap (Radar 25 against 20). Reason: fails the Radar entry test, no named forum with a live date; not touched since July and no forward date on record. Content unchanged. Returns to the Radar the moment a forum and date exist.

### 2026-07-13 — AI roadmap direction — SkySpark 4, Wooly AI, Copilot enablement, DP AI Initiative
- ID: D020
- Owner: Darryl (team-assignment analysis); broader governance still unassigned.
- Forum: response to Sean — today's meeting (07-21) is the venue; CSS AI backlog already on its agenda.
- Added: 2026-07-13 (All Hands). **Updated 07-14: forcing function arrived** — leadership dissatisfaction with AI pace stated at Agile Staff **by Sean McCloskey** (attribution corrected 07-14: loop notes credited Maddy Taylor, but Sean was using her computer while traveling with her); Sean asked Darryl to analyze AI ideas his team could own (CSS synergies). Blocked on Power BI access (Ankit).
- **Update 07-21 (Darryl, SkyFoundry release email): SkySpark 4.0.6 shipped — first production release of 4.0, including the beta of Woolly**, SkySpark's own LLM agent harness (Anthropic/Gemini/OpenAI, customer-supplied API keys, free during beta). This turns the "Wooly AI" thread in this decision from a roadmap mention into a real, usable tool Darryl's team already has access to (sent directly to Chad Steger, Keith Bishop, Ron Snyder). **Correction 07-21 (Darryl):** the release notes' "no guardrails or plan mode" language is SkyFoundry describing a beta-stage feature gap (plan mode/guardrails are on their near-term roadmap), not a disclosed defect — access itself follows the standard SkySpark/entroCIM model, scoped to whatever the signed-in user's own account is already permitted to do. The transcript-sharing default is governed by a documented, one-step `shareTranscript` flag. Practical note for any pilot: use an appropriately scoped account and turn off `shareTranscript` if testing against anything customer-adjacent — normal setup discipline, not an open governance gap. Full detail: `Products/SkyFoundry.md`.
- **Timing note:** this lands the same day as Darryl's Sean meeting on the AI-project-ideas analysis — directly relevant input, not a coincidence to let pass unused.
- Risk of waiting: AOP planning proceeds without credible AI commitments; separately, an ungoverned Woolly pilot (default transcript sharing, no guardrails) could create a data-governance incident before any team formally decides to adopt it.
- **Update 07-22 (M365 evidence, Agile Staff Meeting 07-21): AOP planning accelerated — alignment deadline now Aug-21, and product investments require stronger business-case justification.** New commitment: Darryl to coordinate AOP alignment meetings with Lisa, Brad, and Gregg O'Brien before that deadline (Gregg O'Brien is a new name — not yet in `06_Stakeholder_Map.md`; "Lisa" and "Brad" read as Lisa Orton and Brad Stevens by context but not independently confirmed in this evidence — apply name-collision caution before treating as settled). Separately, GitHub Copilot enablement is now blocked by Vibe Guard compatibility concerns — a distinct AI-tooling governance thread alongside the Claude-code WAB track (see entries above/below). **Correction 07-22 (Darryl, field note): the IDP/WAM item is not a third governance path — "WOB" was a naming error for WAB, and IDP integration is not approval-blocked (see corrected entry above). AI-tooling governance is now two open threads (Claude-code WAB, GitHub Copilot/Vibe Guard), not three.**
- **Update 07-23 (Darryl, field note dated 07-22): Darryl owes Sean product ideas plus an AI-researched needs analysis for CSS** — this is the concrete deliverable that came out of the 07-21 Sean meeting's "analyze AI ideas" ask (see the linked commitment below, and the related entry two rows down). Separately, SkySpark/AI Council and WAM Data Challenges evidence (07-22/23) shows the AI-POC thread moving from problem-definition talk toward actual scoped pilots — first forward motion on the long-stalled "AI adoption governance" pattern.
- **Update 08-12 (entroCIM Backlog Deep Dive): SkySpark 4 production version deployed for early testing** — advances the migration tracked in `Products/entroCIM/entroCIM.md` (08-10: "nearly complete, testing underway") to an actual production deployment; still early-testing stage, not a completed cutover. Same session, the **Woolly AI / AI Council productization decision (approve, limit, or defer) was reconfirmed as still open** — no governance outcome evidenced; this is the same thread as the 07-27 "installation deferred pending Ion framework readiness review" entry above, not a new decision. Separately, a **Claude Code Enablement session (08-12)** scoped a controlled rollout model (approvals + AD groups) for Darryl's team and Digital Products more broadly — a third, more concrete AI-tooling governance thread alongside Woolly and GitHub Copilot/Vibe Guard. Darryl asked to check AD groups for Claude access (Copilot attribution: Inferred — surfaced as a confirmation question, not written to Register A); Nidhishree Sanam owes access documentation (`05`).

2026-10-19 (Claude, weekly brief): Moved from Decision Radar to Backlog at the register cap (Radar 25 against 20). Reason: fails the Radar entry test, no named forum with a live date; not touched since July and no forward date on record. Content unchanged. Returns to the Radar the moment a forum and date exist.

### entroCIM showcase environment strategy
- ID: D087
- Status: Open. 07-13: NOT decided at Leadership Collab (Darryl confirmed). 07-15: Teams message SENT to David/Ron — open-ended ask to discuss Showcase at Friday's (Jul 17) call: "any unresolved issues or decisions we need to make to make sure JG and Mike are moving?" Deliberately light: Darryl allows a decision may already have been made and not documented. Execution sits with Jason Ganiatsas (Application Engineer) and Mike Reed (Business Analyst), both reporting to David Blondel (confirmed 07-15). Expect resolution or a dated decision path out of Friday's call.
- Owner: Ron Snyder / David Blondel
- Forum: entroCIM Backlog Deep Dive or Showcase recurring — needs a decision date.
- Options: continue current showcase vs. separate development project vs. migration-process reversal.
- Scope note (07-15, Darryl): this is the **demo environment** — not tied to the Jul 20 product release. Drop release-deadline framing.
- Risk of waiting: recurring unresolved topic across multiple sprint/release reviews; drags demo-readiness and team attention.

### Resolved while on the Radar or Backlog (retained for the disposed-item check)

- D002 — CLM (Contract Lifecycle Management): build and development to Darryl's team, final decision at corporate AOP meetings — resolved 2026-10-01: Marked RESOLVED in the heading at migration (2026-10-01).
- D050 — Miller Electric PO: process as-is, enforce the 50,000-point minimum, reprice, or pause (new, urgent) — resolved 2026-09-25: Marked RESOLVED in the heading at migration (2026-09-25).
- D003 — Ford support/SLA commercial model: SME-hours treatment, pricing language, guardrails — resolved 2026-09-25: Marked RESOLVED in the heading at migration (2026-09-25).

## Decisions Being Avoided or Stalled

### WAM/DDP/EUDM data-model alignment
- Appears across WAM leadership meetings, data-challenge workshops, and ADM planning for 30+ days without resolution. No single named owner for the alignment decision itself.
- Chief of Staff note: this is the strongest "repeated discussion, no decision" pattern in the baseline.
