# Copilot Intake Prompts

> **Attribution rule added 2026-07-27.** These prompts extract action items from meetings Darryl attended. Copilot cannot tell whose action it is, and previously everything it surfaced landed in Darryl's commitment list — 39 items when 10 were his.
>
> **When processing any output from these prompts, Claude applies the strict attribution test in `CLAUDE.md` before writing anything into Register A.** An extracted action becomes Darryl's only on his stated words, his confirmation, or as follow-through on a decision he owns with no other executor named. Everything else routes to Register B (named owner in his org), Register C (owed to Darryl), or is not tracked.
>
> Copilot output labeled "Inferred" never creates a Register A item. Surface it once as a confirmation question at the weekly closure check.
>
> When pasting evidence, Darryl does not need to pre-filter. The test is applied on the Claude side.
>
> **Prompts revised 2026-07-27 to fix the source of the problem.** The old sections were headed "Commitments I Made," which presumed the answer: Copilot was asked to find Darryl's commitments, so every action item from a meeting he attended came back as his. There was no Owner field and no way to report that someone else owned it. Replaced in all three prompts with a single **Action Items and Commitments** table carrying **Owner**, **Owed to**, **Attribution Evidence** (a quote of the words that assign it), and **Confidence** (Explicit / Implied / Inferred). A standing attribution rule was added to each output contract: attendance is not ownership.
>
> A **Completion and Closure Signals** section was also added to all three. Closure evidence was previously invisible to the intake, which produced a four-day false-overdue on the Shorenstein item (see `10_Pilot_Feedback_Log.md`) and three cycles of silence on the entroCIM release outcome. Surfacing what finished now matters as much as surfacing what started.
>
> **Prompts rewritten 2026-08-06, replacing the above directly, per `EOS_Value_and_Purpose_Review_2026-08-06.md`.** Darryl's finding: the intake was tuned to extract actions, decisions, and risks — the material that feeds the registers — with nothing asking for the two things he now says matter most day to day: durable product/initiative facts (which belong in `Products/`, not a follow-up list) and stakeholder signal (which belongs in `06_Stakeholder_Map.md` and feeds the Team interface now being piloted). Two new sections added to all three prompts: **Product / Initiative State Signals** and **Team and Stakeholder Signals**.
>
> **Rewritten again 2026-08-07 after reviewing the first real output** (`M365_Evidence_Daily_2026-08-07.md`). The two new sections structurally worked — correct headings, correct columns, real content, not "None found" — but four defects showed up in the content itself, all fixed below:
>
> 1. **Attribution Evidence was being filled with boilerplate** ("Meeting task assigned in notes") instead of an actual quote, on every row, which defeats the entire attribution rule from underneath it. Closed by requiring Inferred confidence when no quote exists, rather than letting a non-quote stand in for one.
> 2. **Team and Stakeholder Signals duplicated Team or Staffing Risks** instead of picking one home per fact — the same person's overload got written up in both sections. Closed with an explicit precedence rule.
> 3. **"Durable" was applied to things with no product file to update** (an internal AI-tooling access blocker tagged Durable, with no corresponding `Products/*.md`). Tightened the definition to mean specifically "belongs in a `Products/*.md` file."
> 4. **Coverage Gaps regressed to a generic statement** ("multiple emails... expired or truncated") instead of naming what was missed and which sections it affects, which the Baseline prompt already required and the Daily/Weekly prompts didn't consistently ask for. Aligned all three.
>
> Everything else — the attribution rule, the closure-signal section, the rest of the output contracts — is unchanged.
>
> **Revised 2026-08-25 after the first raw package was reviewed end to end** (`M365_Evidence_Weekly_20260825.md`, the 08-18 to 08-25 window). Two of Darryl's own ad hoc changes were made permanent and two defects were fixed.
>
> **What the review established first: section 6b works.** It returned twelve rows, correctly split Durable from Transient, with the entroCIM training-model change, the CDA two-tier service definition, and the DDP/EUDM source-of-truth position all captured as Durable, and Passport and the 62443 mapping correctly marked Transient. The 08-06 rewrite did its job. **The reason no `Products/` update ever traced back to a briefing is therefore on the Claude side, not the prompt side: 6b was being produced and dropped during briefing assembly.** Fixed in `CLAUDE.md`, not here. Do not "fix" this prompt again for that symptom.
>
> 1. **Weekly window moved from 7 to 8 days** (Darryl's change, made permanent). Guarantees the previous Monday is never lost between cycles. The cost is one day of deliberate overlap per week; those repeats are Echoes under the disposed-item check.
> 2. **Retrieval rules added to the Daily and Weekly prompts** (from Darryl's ad hoc transcript instruction, formalised and extended). Copilot must state whether it can reach transcripts and notes, and must resume retrieval from a truncation point rather than reporting it and moving on. The 08-25 package proved why: it reported the 08-19 deployment scrum truncated at line 226 of 284 and the 08-20 scrum at line 235 of 396, losing roughly 20% and 41% of two transcripts, and simply noted the fact. A tool that can name where it stopped can resume there.
> 3. **Sprint-task exclusion added to the Action Items section of both prompts.** The 08-25 package returned 30 action items, of which 16 were Inferred and every one of those was a developer task row lifted from Loop stand-up notes: donut-chart queries, JFrog artifact ports, manual test scenarios, monitoring UI fixes. Around 8 rows operated at Darryl's level. Inferred rows cannot enter Register A under the attribution test anyway, so this was extraction effort producing pure intake volume for a register system whose diagnosed problem is volume. Four exceptions preserve anything that blocks a customer commitment, a release gate, a dated external deadline, or an escalated item. **The rule reports its own exclusion count so it stays inspectable** and can be reversed if the next package shows something worth keeping was cut.
>
> **Revised again 2026-08-25 (second run), after reviewing the package the revised prompts produced.** All three of the previous changes fired correctly and are keepers: the retrieval statement appeared up front and named what was and was not reachable; truncation was retried and the outcome recorded (`DDP Backlog Entrance Call` returned lines 0–435 of 574, `Differentiation exercise` returned lines 0–583 of 952, both retried without success and reported as attempted rather than merely observed); and the sprint-task rule reported "Excluded under the sprint-task rule: 7 items," cutting Action Items from 30 rows to 13. Section 6b returned nine correctly classified rows including the FY27 AOP row properly marked Transient as portfolio governance. Three further changes were made:
>
> 4. **Portfolio scope filter added to the Daily and Weekly prompts.** Darryl's finding on reading the output: it carried substantial material from products he has no responsibility for, picked up in forums he attends as an optional invitee. The DDP Backlog Entrance Call alone seeded content into seven sections — credit-card refund handling, storefront redesign, QPM 3.4.4 scope, AccuTech tagging conventions, DDP tracker field administration, backlog hygiene — none of it his. **The filter is scoped by portfolio, not by meeting**, because a blanket exclusion of DDP would also have cut the things that genuinely matter: DDP/EUDM as WAM's asset-data source of truth, supplier and global attribute governance, and the VAS/WMX complex-build path into the WAM install base. So the prompt names the four owned products, names the out-of-scope products explicitly, and supplies a connection test with worked examples in both directions. The governing principle is a restatement of the one already in this file: **attendance is not ownership, and attendance is also not relevance.** Portfolio boundary taken from `Reference/Digital_Product_List.md`, where Darryl is Product Executive for entroCIM, WAM, and Ascent/Navigator, plus CDA which he owns as an initiative.
> 5. **Validation block added to both prompts.** Seven checks, reported Pass or Fail at the end of the report, covering section completeness, column conformance, attribution integrity, portfolio scope, the sprint-task count, coverage-gap specificity, and truncation retries. A failed check must be fixed and re-run before delivery.
> 6. **File output must now be verified, not just created.** The 08-25 run displayed correct results but produced a malformed file, and only a manual follow-up instruction from Darryl produced a good one. That instruction is now permanent: create the file, re-open and read it back, confirm all sections are present and match what was displayed, state the verification result, and regenerate if it does not hold. **A file that was generated is not the same as a file that was generated correctly** — the same distinction as the "declared executed versus verified running" rule in `CLAUDE.md`, applied to output rather than to mechanisms.
>
> **Retrieval diagnostic run 2026-08-25, and it closed a question open since 07-24.** `10_Pilot_Feedback_Log.md` recorded on 07-24 and 07-27 that "transcript availability is now the single largest evidence gap in the system," and it was treated as a tooling limitation for five weeks. It was not. A forced-choice diagnostic put to Copilot against nine named artifacts returned this:
>
> | Cause | Items | Meaning |
> |---|---|---|
> | **A — never transcribed** | WAM Product Leadership Sync, entroCIM Leadership Collaboration, PASS-06 Server Migration Cutover, Quest Migration Weekly Check-In | `isMeetingTranscribed:false` on all four. No artifact exists. **All four are Darryl's own organisation's forums** |
> | **B — permission denied** | **none** | There is no access problem. Nothing to request from IT |
> | **C — response size limit** | DDP Backlog Entrance Call, Differentiation exercise | Artifact retrievable, response truncated |
> | **E — not retrievable in session** | Weekly Sync recording | Recording surfaced, transcript existence unproven |
> | **Cannot determine** | Planner/To Do, Sent Items completeness | Never attempted, so never diagnosed |
>
> **Copilot self-corrected on the most important point:** items 1 to 4 had been filed as coverage gaps, implying retrieval failure, when the evidence showed no transcript was ever created. That misfiling pointed the diagnosis at the tool for five weeks when the cause was a meeting setting.
>
> **The operational finding: the largest evidence gap in this system is a switch on Darryl's own recurring meetings, not a limit of Copilot.** No permission change would have helped.
>
> **Revised 2026-08-25 (third pass) on the strength of that diagnostic:**
>
> 7. **Truncation continuation now specifies the same pass.** Copilot confirmed range retrieval works "in principle" but could not demonstrate it after the fact, because a transcript handle does not survive the retrieval session. Deferred continuation is therefore worthless: once the sweep moves on, the content is unrecoverable for that run even though the artifact still exists. The rule now requires continuation before moving to the next source, and requires the retrieved range to be stated against the source's total so partial coverage is quantified rather than described.
> 8. **"Not transcribed at source" separated from Coverage Gaps.** Filing a never-transcribed meeting as a coverage gap hides an operating signal inside a tooling complaint. It now gets its own block, which functions as a standing list of which forums have transcription switched off.
> 9. **Planner/To Do and Sent Items must be probed explicitly every run.** Both returned "cannot determine" because neither was ever actually attempted. An untested capability is not a limitation, and should not be reported as one.
>
> **Also confirmed by the 08-25 package:** zero of the thirty action items were attributed to Darryl. The 07-27 attribution fix is holding under a heavier package than it was designed against. And the Teams-thread expiry problem is a retention limit, not a prompt problem — nine threads returned expired bodies, including AOP Pending Items, Digital Products Portfolio Review, Quest Migration Weekly Check-In, and eCIM Leadership. No wording change reaches that.

Three repeatable prompts for Microsoft Copilot. Run the appropriate one, then paste the output into the Executive Operating System session. Claude interprets the evidence per `CLAUDE.md` and updates the living documents (03–06) and `Products/`.

- **Baseline** — run once (or after long absences) to seed the system. 30-day lookback.
- **Daily** — each working morning. 24-hour lookback.
- **Weekly** — end of week or Monday morning. **8-day lookback** (changed 2026-08-25), feeds the weekly review. The eighth day is deliberate overlap so a Monday is never lost between cycles; it means one day repeats each week, and those repeats are Echoes under the disposed-item check, not new evidence.

Copilot note: if output gets cut off or shallow, run the prompt in sections (e.g., "sections 1–4 only", then "sections 5–8").

---

## 1. Baseline Prompt (one-time, 30 days)

```
Review my Microsoft 365 activity from the last 30 days — email, sent email, Teams chats and channels, calendar, meeting recaps and transcripts, task assignments, and recently modified OneDrive/SharePoint documents.

I am building a strategic operating picture for my executive advisor, not a task list. Do not summarize my day-to-day activity. Produce a structured baseline evidence package in concise Markdown with these sections:

RETRIEVAL RULES — apply while gathering, before writing anything:

- **Transcripts and meeting notes: say what you have.** State up front whether you can access meeting transcripts and meeting notes for this window. If you cannot reach one you can see exists, try to resolve it before giving up, and say what you tried.
- **Truncation: continue immediately, in the same pass.** If a transcript, document, or thread comes back incomplete or cut off, resume retrieval from the point it stopped and get the remainder **before you move on to the next source**. Do not finish the sweep and come back to it, and do not defer it to a later message. A transcript handle does not survive the retrieval session: once you have moved past it, the range can no longer be requested, and the content is lost for this run even though the artifact still exists. Request successive ranges (for example lines 400 to 574, then 574 onward) until you reach the stated total, then continue the sweep.
- **Report the arithmetic.** When a source reports a total length, state the range retrieved against that total, for example "retrieved lines 0 to 574 of 574, complete" or "retrieved 0 to 435 of 574, two continuation attempts failed." A percentage recovered is more useful than the word "partial."
- Only after continuation genuinely fails does it become a Coverage Gap, and then say how many attempts were made and what happened.
- **Notes are not transcripts.** Where only meeting notes or a recap are available and no verbatim transcript, treat that as a retrieval limitation and record it in Coverage Gaps. It constrains attribution confidence and the report should show that it did.
- **Say whether content came from a transcript, from meeting chat, or from notes.** A meeting's chat messages and files are often retrievable when its transcript is not, and the two carry different attribution confidence. When you cite a meeting as a source, mark it `(transcript)`, `(meeting chat)`, or `(AI notes)`. Never cite a meeting as a source in a way that implies a transcript you did not read. If a meeting reports `isMeetingTranscribed:false` and you are drawing on its chat, say so explicitly on every row that uses it.
- **A meeting that did not happen is not a gap either.** A recording or calendar artifact can exist for an occurrence that was cancelled or that nobody attended; it returns media metadata and no usable transcript because nothing was said. Before listing any recording as unretrievable, check the calendar for whether that occurrence actually took place, and if it did not, say so and leave it out of Coverage Gaps entirely.
- **Distinguish "not transcribed" from "could not retrieve," and never file the first as a coverage gap.** If a meeting reports `isMeetingTranscribed:false`, no transcript exists and nothing was lost in retrieval. Do not list it as a coverage gap, which implies a failure on your side and hides the real cause. List those meetings in a separate short block titled **"Not transcribed at source"**, naming each meeting and its date. **Meetings only.** An email, a document, or a Teams thread cannot be untranscribed and must never appear in this block; if it could not be read, that is a Coverage Gap. Do not list a source here and also cite it elsewhere as a source you read. That block is an operating signal, not a retrieval problem: it tells me which of my own recurring forums have transcription switched off, which is something I can change.
- **Probe these two explicitly every run, because both have come back indeterminate before.** Attempt a Microsoft Planner and To Do task query, and attempt a Sent Items query bounded to the reporting window. Report the outcome of each attempt plainly: succeeded and what was found, or failed and the error or empty result. Do not skip the attempt and report the capability as unknown.


Focus on evidence that may affect: executive decision-making, product direction, portfolio health, customer satisfaction, delivery risk, commercial execution, Managed Services, AI strategy, cross-functional dependencies, team health, benefits realization, leadership follow-up. Avoid optimizing for inbox cleanup or task completion.

PORTFOLIO SCOPE — apply to every section; this is a relevance filter, not a topic list:

**In scope. These four products are mine:**
- **entroCIM** (smart-building intelligence platform)
- **Wesco Asset Management / WAM**, including ADM and the Strev/Revnue components
- **Ascent / Navigator**
- **Connected Device Assurance (CDA)**

Also in scope: my own organisation (team, staffing, capacity, AI strategy for my team), and partners, platforms, and customers where they materially affect those four — SkyFoundry/SkySpark, JCI/Airwall, i3 Alliance, Nozomi, and customer accounts running my products such as Dell, Ford, Federal Reserve, Coca-Cola/TCCC, Louvre Abu Dhabi, BAE, Stanford, DataBank.

**Out of scope. These are other people's products, and I am frequently an optional attendee in forums where they are discussed:**
QPM, Assortment, AutoBOM, ConstructTech Integrator, Digital FTTx, Intelligent Document Processing, Insight by Anixter, Monday.com, Prokeep, Proton.ai, Pull Logic, RecommEngine, Retrofit, VAS Configurator, WMI and eStock, and general DDP/storefront/order-management functionality such as credit-card processing, refunds, checkout, and backlog or tracker administration.

**Attending a forum does not make its contents relevant.** This is the same principle as the attribution rule below: attendance is not ownership, and attendance is also not relevance. I am an optional invitee to several forums — the DDP Backlog Entrance Call and Digital Products Portfolio Review among them — that spend most of their time on products I have no responsibility for. Do not report an item merely because I could have heard it.

**The connection test. Include an item about an out-of-scope product only if it changes something in the four products above.** Apply this test explicitly, do not guess:

| Include | Because |
|---|---|
| DDP/EUDM as the asset-data source of truth feeding WAM/ADM | It is WAM's data foundation |
| Global or supplier attribute governance, DDPTRK-6346 and successors | It determines WAM/ADM data quality |
| VAS Configurator or WMX where they sit on the complex-build path into the WAM install base | It is WAM's data path |
| IDP, Rhombus, or supplier-document work where it is a data source for ADM onboarding | It feeds ADM |
| WMI or eStock where the subject is how WAM is positioned or differentiated against them | It is WAM market positioning |

| Exclude | Because |
|---|---|
| QPM release scope and features, 3.4.x contents | Not my product |
| Credit-card processing, refunds, storefront redesign | Not my product |
| AccuTech tagging, DDP tracker fields, backlog hygiene and administration | Not my product, and administrative |
| Assortment, Pull Logic, Proton.ai, Prokeep, and the rest of the out-of-scope list, on their own terms | Not my products |

**Never drop silently, and break the count down by source.** At the end of the report, state the out-of-scope exclusions as a short table with one row per source: Source | Items excluded | What they were about. An aggregate count across many sources hides whether the filter took eighteen items from one forum or spread them thinly, and only the per-source view shows whether something in scope was cut by mistake. If none, say so. If an item is genuinely ambiguous, include it and mark it "Scope: uncertain" with one line saying which of my four products it might touch — I would rather judge a borderline item than lose it.


1. Active Initiatives and Workstreams — Each initiative or recurring topic I am actively involved in. For each: name, current state, my role (owner / decision-maker / escalation point / participant), key people, and apparent momentum (advancing, stalled, unclear).

2. Decisions Made in the Last 30 Days — Decisions that were clearly made, by whom, and where recorded.

3. Open or Emerging Decisions — Decisions that appear needed but not yet made. For each: the decision, apparent owner, options discussed, what seems to be blocking it, and how long it has been open.

4. Recurring Unresolved Topics — Topics discussed repeatedly across meetings or threads without resolution. Include how many times and over what span.

5. Action Items and Commitments — Every open action item or commitment surfaced in the period, REGARDLESS OF WHO OWNS IT. Do not assume an item is mine because I was present. Columns: Action | Owner (specific named person) | Owed to | Attribution Evidence (quote the words that assign it, and who said them) | Confidence (**Explicit** = owner said it themselves / **Implied** = assigned to them, not declined / **Inferred** = you deduced it) | Due date if stated | Source. If the owner is unclear, write "Owner unclear" — do not default to me. **If you cannot quote actual words assigning the action, you may not write Explicit or Implied. Write Confidence: Inferred and describe the basis in one phrase (e.g., "named as responsible in the recap, no verbatim assignment"). A generic phrase like "assigned in meeting notes" is not evidence and is not an acceptable substitute for a quote.**
   - **Exclude routine sprint-level engineering tasks (added 2026-08-25).** Individual developer or delivery-team task assignments lifted from stand-up notes, Loop task rows, or sprint boards — code fixes, test scenarios, UI tweaks, build and deploy chores, ticket creation, documentation tasks, local testing — are the delivery team's work, tracked in their own systems, and below the level this package serves. Leave them out.
   - **Four exceptions. Include such a task only if it meets one of these:** it blocks a customer commitment or a customer-visible date; it blocks a release gate or production promotion; it carries a dated external deadline that is regulatory, contractual, or customer-imposed; or it is the named next step on an item already escalated to leadership.
   - **Never drop them silently, and break the count down by source.** At the end of this section write one line per source: "Excluded under the sprint-task rule: N items from [source]," so the filter can be checked source by source rather than in aggregate. If the count is zero, write "Excluded under the sprint-task rule: none." This keeps the filter inspectable, and the exclusion is reviewed against that count.

6. Completion and Closure Signals — Evidence that something finished, shipped, was approved, resolved, or cancelled in the period. For each: item, what the evidence shows, who confirmed it, source, and whether closure is stated outright or only implied.

7. Product / Initiative State Signals — Facts about specific products or initiatives (e.g. WAM, entroCIM, JCI, Connected Safety, Connected Device Assurance, Navigator, SkyFoundry, or others that surface) that are worth keeping in a standing knowledge file rather than a follow-up list: a capability shipping or changing, a roadmap or timeline date, a commercial-position fact (pricing, pipeline, competitor move), a dependency forming or clearing, a benefits-realization signal (planned vs. actually realized). Mark **Durable** only if the item is a fact about a product or initiative that Wesco builds, ships, or sells, and that a standing knowledge file would actually be updated for. Internal tooling, AI-licensing, or governance threads (e.g., developer tool access, platform administration) are not products — mark those **Transient** even if they recur, since they belong in a risk or decision entry, not a product file. Distinguish from transient status generally — a one-off "release is on track" is not durable; a changed target date or a new dependency is. Columns: Product/Initiative | What Changed or Was Confirmed | Evidence | Durable or Transient | Source.

8. People Map — The people I interact with most. Group into: leadership above me, direct reports and team leaders, cross-functional partners, customers/external. For each: name, role if known, main topics between us, and anything they appear to be waiting on from me.

9. Team and Stakeholder Signals — Broader than who is waiting on me: workload concentration or overload on a specific person, single-person dependencies, morale or sentiment cues, a capability gap, a new stakeholder relationship forming, a reporting-line or role change. This is relationship and capacity signal for a standing team picture, not an action item. **If a person's workload, dependency, or overload is already fully captured as a risk in section 10, do not restate it here — write the person's name and "see section 10" instead of repeating the same fact.** Only use this section for signal that is not already a stated risk. Columns: Person | Signal | Evidence | Why It Matters | Source.

10. Risks and Escalations — Customer, delivery, commercial, staffing, or dependency risks visible in the last 30 days. For each: risk, severity (High/Medium/Low), evidence, trend if visible.

11. Cross-Functional Dependencies — Work blocked on or entangled with other teams (Sales, Sales Ops, Supplier Relations, Data Governance, MDM, Finance, Legal, Architecture, Cloud, Deployment, Support, Managed Services). For each: dependency, what is blocked, owning team, status.

12. Key Documents — The 10–15 most strategically significant documents modified in the period. For each: name, location, related initiative, why it matters.

13. Operating Cadence and Governance Forums — All recurring meetings on my calendar. Group into: (a) product/delivery/governance, (b) 1:1 and leadership alignment, (c) commercial/finance/customer/external. Table columns: Meeting | Frequency | Organizer | Primary purpose or strategic signal.

14. Coverage Gaps — Content you could not retrieve (expired messages, inaccessible files, truncated results) that may affect completeness. State what is missing and for which sections.

OUTPUT CONTRACT — follow exactly for repeatability:
- Use the section numbers and headings above, in order, every time. Do not add, merge, or renumber sections.
- Use Markdown tables with exactly the columns specified per section.
- If a section has no items, write "None found" — do not omit the section.
- Name sources by their real names (meeting title, email subject line, document filename). Do not use citation tokens or reference IDs.
- Use ISO dates (YYYY-MM-DD) everywhere.
- State facts only; mark anything inferred as "Inferred:".
- If the same person appears with a full name in one section and a first name only in another, use the full name in both once you've matched them within this report.

VALIDATION — run these checks before giving me anything, and report the result:

1. **Sections complete.** Every section present, in the specified order, with "None found" where empty. None omitted.
2. **Columns conform.** Every table carries exactly the columns specified for that section, no more and no fewer.
3. **Attribution integrity.** Every row marked Explicit or Implied carries an actual quote. Any row without a quote is marked Inferred. No paraphrase stands in for a quote.
4. **Portfolio scope.** Every row passes the connection test above, and the out-of-scope exclusion count is stated.
5. **Sprint-task rule.** The exclusion count is stated, even if zero.
6. **Coverage gaps are specific**, and contain only genuine retrieval failures. Named items and threads, with what was attempted on each. Meetings that were never transcribed are in the "Not transcribed at source" block instead.
6a. **The two probes ran.** Planner/To Do and Sent Items were both attempted, with the outcome of each stated.
7. **Retrieval.** Every truncated source was continued in the same pass until complete or genuinely exhausted, with the range retrieved stated against the source's total.

Report these as a short block titled "Validation" at the end of the report, one line per check, each reading Pass or Fail with a brief note. **If any check fails, fix it and re-run the check before delivering. Do not hand me a package with a failed check.** If something cannot be fixed, say so plainly and explain why rather than marking it Pass.


FILE OUTPUT — final step, do not skip, and verify it before handing it over:

1. Create a downloadable Markdown file named M365_Evidence_Baseline_YYYY-MM-DD.md (using today's date) containing the complete report.
2. **Re-open the file you just created and read it back.** Confirm: every section is present through the last one; the final table's final row is intact; no section is truncated or empty that should have content; and the file content matches what you displayed to me. A file that was generated is not the same as a file that was generated correctly.
3. State the verification result in one line: filename, number of sections found, and confirmation that the file is complete.
4. **If the file is incomplete, malformed, or does not match what you displayed, regenerate it and verify again before giving it to me.** Do not hand over a file you have not read back. If file creation fails twice, output the entire report inside ONE markdown code block instead so I can copy it losslessly, and say that is what you are doing and why.

Do not summarize or shorten the report when creating the file.
```

---

## 2. Daily Prompt (24 hours)

```
Review my Microsoft 365 activity from the last 24 hours, including: email, sent email, Teams chats, Teams channels, calendar, meeting recaps, meeting transcripts, facilitator notes, Loop components, task assignments, recently modified OneDrive and SharePoint documents, action items from meetings, and commitments made in conversations.

Do not provide a generic summary of my activity. Create a structured operational evidence package that I can provide to my executive advisor.

RETRIEVAL RULES — apply while gathering, before writing anything:

- **Transcripts and meeting notes: say what you have.** State up front whether you can access meeting transcripts and meeting notes for this window. If you cannot reach one you can see exists, try to resolve it before giving up, and say what you tried.
- **Truncation: continue immediately, in the same pass.** If a transcript, document, or thread comes back incomplete or cut off, resume retrieval from the point it stopped and get the remainder **before you move on to the next source**. Do not finish the sweep and come back to it, and do not defer it to a later message. A transcript handle does not survive the retrieval session: once you have moved past it, the range can no longer be requested, and the content is lost for this run even though the artifact still exists. Request successive ranges (for example lines 400 to 574, then 574 onward) until you reach the stated total, then continue the sweep.
- **Report the arithmetic.** When a source reports a total length, state the range retrieved against that total, for example "retrieved lines 0 to 574 of 574, complete" or "retrieved 0 to 435 of 574, two continuation attempts failed." A percentage recovered is more useful than the word "partial."
- Only after continuation genuinely fails does it become a Coverage Gap, and then say how many attempts were made and what happened.
- **Notes are not transcripts.** Where only meeting notes or a recap are available and no verbatim transcript, treat that as a retrieval limitation and record it in Coverage Gaps. It constrains attribution confidence and the report should show that it did.
- **Say whether content came from a transcript, from meeting chat, or from notes.** A meeting's chat messages and files are often retrievable when its transcript is not, and the two carry different attribution confidence. When you cite a meeting as a source, mark it `(transcript)`, `(meeting chat)`, or `(AI notes)`. Never cite a meeting as a source in a way that implies a transcript you did not read. If a meeting reports `isMeetingTranscribed:false` and you are drawing on its chat, say so explicitly on every row that uses it.
- **A meeting that did not happen is not a gap either.** A recording or calendar artifact can exist for an occurrence that was cancelled or that nobody attended; it returns media metadata and no usable transcript because nothing was said. Before listing any recording as unretrievable, check the calendar for whether that occurrence actually took place, and if it did not, say so and leave it out of Coverage Gaps entirely.
- **Distinguish "not transcribed" from "could not retrieve," and never file the first as a coverage gap.** If a meeting reports `isMeetingTranscribed:false`, no transcript exists and nothing was lost in retrieval. Do not list it as a coverage gap, which implies a failure on your side and hides the real cause. List those meetings in a separate short block titled **"Not transcribed at source"**, naming each meeting and its date. **Meetings only.** An email, a document, or a Teams thread cannot be untranscribed and must never appear in this block; if it could not be read, that is a Coverage Gap. Do not list a source here and also cite it elsewhere as a source you read. That block is an operating signal, not a retrieval problem: it tells me which of my own recurring forums have transcription switched off, which is something I can change.
- **Probe these two explicitly every run, because both have come back indeterminate before.** Attempt a Microsoft Planner and To Do task query, and attempt a Sent Items query bounded to the reporting window. Report the outcome of each attempt plainly: succeeded and what was found, or failed and the error or empty result. Do not skip the attempt and report the capability as unknown.


Focus on evidence that may affect: executive decision-making, product direction, portfolio health, customer satisfaction, delivery risk, commercial execution, Managed Services, AI strategy, cross-functional dependencies, team health, benefits realization, leadership follow-up. Avoid optimizing for inbox cleanup or task completion.

PORTFOLIO SCOPE — apply to every section; this is a relevance filter, not a topic list:

**In scope. These four products are mine:**
- **entroCIM** (smart-building intelligence platform)
- **Wesco Asset Management / WAM**, including ADM and the Strev/Revnue components
- **Ascent / Navigator**
- **Connected Device Assurance (CDA)**

Also in scope: my own organisation (team, staffing, capacity, AI strategy for my team), and partners, platforms, and customers where they materially affect those four — SkyFoundry/SkySpark, JCI/Airwall, i3 Alliance, Nozomi, and customer accounts running my products such as Dell, Ford, Federal Reserve, Coca-Cola/TCCC, Louvre Abu Dhabi, BAE, Stanford, DataBank.

**Out of scope. These are other people's products, and I am frequently an optional attendee in forums where they are discussed:**
QPM, Assortment, AutoBOM, ConstructTech Integrator, Digital FTTx, Intelligent Document Processing, Insight by Anixter, Monday.com, Prokeep, Proton.ai, Pull Logic, RecommEngine, Retrofit, VAS Configurator, WMI and eStock, and general DDP/storefront/order-management functionality such as credit-card processing, refunds, checkout, and backlog or tracker administration.

**Attending a forum does not make its contents relevant.** This is the same principle as the attribution rule below: attendance is not ownership, and attendance is also not relevance. I am an optional invitee to several forums — the DDP Backlog Entrance Call and Digital Products Portfolio Review among them — that spend most of their time on products I have no responsibility for. Do not report an item merely because I could have heard it.

**The connection test. Include an item about an out-of-scope product only if it changes something in the four products above.** Apply this test explicitly, do not guess:

| Include | Because |
|---|---|
| DDP/EUDM as the asset-data source of truth feeding WAM/ADM | It is WAM's data foundation |
| Global or supplier attribute governance, DDPTRK-6346 and successors | It determines WAM/ADM data quality |
| VAS Configurator or WMX where they sit on the complex-build path into the WAM install base | It is WAM's data path |
| IDP, Rhombus, or supplier-document work where it is a data source for ADM onboarding | It feeds ADM |
| WMI or eStock where the subject is how WAM is positioned or differentiated against them | It is WAM market positioning |

| Exclude | Because |
|---|---|
| QPM release scope and features, 3.4.x contents | Not my product |
| Credit-card processing, refunds, storefront redesign | Not my product |
| AccuTech tagging, DDP tracker fields, backlog hygiene and administration | Not my product, and administrative |
| Assortment, Pull Logic, Proton.ai, Prokeep, and the rest of the out-of-scope list, on their own terms | Not my products |

**Never drop silently, and break the count down by source.** At the end of the report, state the out-of-scope exclusions as a short table with one row per source: Source | Items excluded | What they were about. An aggregate count across many sources hides whether the filter took eighteen items from one forum or spread them thinly, and only the per-source view shows whether something in scope was cut by mistake. If none, say so. If an item is genuinely ambiguous, include it and mark it "Scope: uncertain" with one line saying which of my four products it might touch — I would rather judge a borderline item than lose it.


Use concise Markdown with these sections:

1. Important Changes Since Yesterday — change, source, why it may matter, people involved. Only items that could affect leadership attention, decisions, risk, delivery, customer satisfaction, commercial execution, or strategic progress.

2. Meetings Requiring Leadership Follow-Up — meeting, date/time, why it matters, decisions discussed or implied, follow-up needed, people involved, source. Ignore purely informational meetings unless they created a decision, risk, or commitment.

3. Action Items and Commitments — every action item, commitment, or deliverable that surfaced, REGARDLESS OF WHO OWNS IT. Do not assume an item is mine because I attended the meeting or was on the thread. Table columns: Action | Owner (the specific named person who will do it) | Owed to | Attribution Evidence (quote the actual words that assign it, and name who said them) | Confidence | Due date if stated | Source.
   - Confidence values, use exactly these: **Explicit** (the owner stated they would do it, in their own words), **Implied** (someone else assigned it to them and they did not decline), **Inferred** (you deduced the owner from context).
   - If the owner is genuinely unclear, write "Owner unclear." Do not default to me.
   - Include items owned by other people in the same table. I need the complete picture, not a filtered one.
   - Do not merge several actions into one row, and do not split one action across rows.
   - **Attribution Evidence must be an actual quote, not a description of one.** "Meeting task assigned in notes" or similar paraphrases are not acceptable and are not evidence. If you cannot find and quote the actual words, you may not mark Confidence as Explicit or Implied — mark it Inferred and write the basis in one short phrase instead (e.g., "named as owner in the recap summary, no verbatim assignment quoted").
   - **Exclude routine sprint-level engineering tasks (added 2026-08-25).** Individual developer or delivery-team task assignments lifted from stand-up notes, Loop task rows, or sprint boards — code fixes, test scenarios, UI tweaks, build and deploy chores, ticket creation, documentation tasks, local testing — are the delivery team's work, tracked in their own systems, and below the level this package serves. Leave them out.
   - **Four exceptions. Include such a task only if it meets one of these:** it blocks a customer commitment or a customer-visible date; it blocks a release gate or production promotion; it carries a dated external deadline that is regulatory, contractual, or customer-imposed; or it is the named next step on an item already escalated to leadership.
   - **Never drop them silently, and break the count down by source.** At the end of this section write one line per source: "Excluded under the sprint-task rule: N items from [source]," so the filter can be checked source by source rather than in aggregate. If the count is zero, write "Excluded under the sprint-task rule: none." This keeps the filter inspectable, and the exclusion is reviewed against that count.

4. Completion and Closure Signals — evidence that something finished, shipped, was approved, was resolved, or was cancelled. For each: item, what the evidence shows, who confirmed it, source, and whether the closure is stated outright or only implied. Include partial completions. This section exists because open items have previously been carried as overdue for days after they were actually resolved — surfacing closure evidence is as important as surfacing new work.

5. Product / Initiative State Signals — Facts about a specific product or initiative (WAM, entroCIM, JCI, Connected Safety, Connected Device Assurance, Navigator, SkyFoundry, or others that surface) that belong in a standing knowledge file, not a follow-up list: a capability change, a roadmap/timeline date, a commercial-position fact, a dependency forming or clearing, a benefits-realization signal. Mark **Durable** only if this is a fact about something Wesco builds, ships, or sells, and a standing product file would actually be updated with it. Mark **Transient** for a one-off status update, and also for internal tooling, AI-licensing, or governance threads (developer tool access, platform administration) that recur but aren't products — those belong in a risk or decision entry, not a product file; don't mark them Durable just because they keep coming up. Do not duplicate an item already fully captured in section 1 — if a change belongs here because it is durable knowledge about a product, put it here instead. Columns: Product/Initiative | What Changed or Was Confirmed | Evidence | Durable or Transient | Source.

6. People Waiting on Me — person, what they need, source, urgency, business context, suggested follow-up. Prioritize by business impact, not message volume. Only include items where the evidence shows the person is actually waiting on me specifically, not on my team or organization generally; if it is my organization rather than me, say so and name the person in my org.

7. Team and Stakeholder Signals — Broader than who is waiting on me: workload concentration or overload on a specific person, single-person dependencies, morale or sentiment cues, a capability gap, a new stakeholder relationship forming, a reporting-line or role change. This is relationship and capacity signal for a standing team picture, not something requiring my action today. **Precedence rule: if a person's workload, dependency, or overload is already going to be written up as a Team or Staffing Risk in section 10, it goes there, not here — write "see section 10" and the person's name here instead of restating the same fact in both sections.** Use this section only for signal that is not already a stated risk (a new relationship, a capability gap, a sentiment cue, a role change). Columns: Person | Signal | Evidence | Why It Matters | Source.

8. Decisions Needed or Emerging — decision, owner if known, context, options mentioned, information still needed, risk of waiting, source. Include decisions implied by repeated discussion, unresolved threads, or stalled work.

9. Customer or Delivery Risks — risk, customer/initiative affected, severity (High/Medium/Low), evidence, potential impact, recommended follow-up, source.

10. Team or Staffing Risks — risk, people/team affected, evidence, potential impact, suggested leadership action, source. Include overload, unclear ownership, recurring confusion, single-person dependency.

11. Cross-Functional Dependencies — dependency, what is blocked or affected, owning person/team if known, current status, risk trend, recommended next step, source.

12. Recently Modified Documents That May Matter — document name, location, why it may matter, related initiative, people involved, review priority (High/Medium/Low). Only documents that may affect decisions, risks, executive communication, product direction, commercial execution, or delivery.

13. Potential Executive Communication Needs — audience, topic, why communication may be needed, suggested message intent, urgency, source.

14. Coverage Gaps — content you could not retrieve (expired, inaccessible, truncated) that may affect completeness. **Name the specific items or threads affected and which section(s) they would have shown up in.** A generic statement like "multiple emails and files were expired or truncated" is not sufficient on its own — say which emails, files, or meetings, to the extent you can identify them, even if the content itself is unavailable.

OUTPUT CONTRACT — follow exactly for repeatability:
- Use the section numbers and headings above, in order, every time. If a section has no items, write "None found" — do not omit it.
- Use Markdown tables with exactly the fields specified per section.
- Name sources by their real names (meeting title, email subject, document filename) — no citation tokens.
- Use ISO dates (YYYY-MM-DD). Be concise. Prioritize business impact over volume.
- Exclude private or irrelevant personal content. No productivity advice. Do not simply summarize my day.
- State facts only; mark anything inferred as "Inferred:".
- **Attribution rule, applies throughout:** never assign an action, commitment, or decision to me solely because I was present, copied, or organizing. Attendance is not ownership. Where the record names someone else, name them. Where it names nobody, say so.
- If the same person appears with a full name in one section and a first name only in another, use the full name in both once you've matched them within this report.


VALIDATION — run these checks before giving me anything, and report the result:

1. **Sections complete.** Every section present, in the specified order, with "None found" where empty. None omitted.
2. **Columns conform.** Every table carries exactly the columns specified for that section, no more and no fewer.
3. **Attribution integrity.** Every row marked Explicit or Implied carries an actual quote. Any row without a quote is marked Inferred. No paraphrase stands in for a quote.
4. **Portfolio scope.** Every row passes the connection test above, and the out-of-scope exclusion count is stated.
5. **Sprint-task rule.** The exclusion count is stated, even if zero.
6. **Coverage gaps are specific**, and contain only genuine retrieval failures. Named items and threads, with what was attempted on each. Meetings that were never transcribed are in the "Not transcribed at source" block instead.
6a. **The two probes ran.** Planner/To Do and Sent Items were both attempted, with the outcome of each stated.
7. **Retrieval.** Every truncated source was continued in the same pass until complete or genuinely exhausted, with the range retrieved stated against the source's total.

Report these as a short block titled "Validation" at the end of the report, one line per check, each reading Pass or Fail with a brief note. **If any check fails, fix it and re-run the check before delivering. Do not hand me a package with a failed check.** If something cannot be fixed, say so plainly and explain why rather than marking it Pass.

FILE OUTPUT — final step, do not skip, and verify it before handing it over:

1. Create a downloadable Markdown file named M365_Evidence_Daily_YYYY-MM-DD.md (using today's date) containing the complete report.
2. **Re-open the file you just created and read it back.** Confirm: every section is present through the last one; the final table's final row is intact; no section is truncated or empty that should have content; and the file content matches what you displayed to me. A file that was generated is not the same as a file that was generated correctly.
3. State the verification result in one line: filename, number of sections found, and confirmation that the file is complete.
4. **If the file is incomplete, malformed, or does not match what you displayed, regenerate it and verify again before giving it to me.** Do not hand over a file you have not read back. If file creation fails twice, output the entire report inside ONE markdown code block instead so I can copy it losslessly, and say that is what you are doing and why.

Do not summarize or shorten the report when creating the file.
```

---

## 3. Weekly Prompt (8 days)

```
Review my Microsoft 365 activity from the last 8 days — email, sent email, Teams chats and channels, calendar, meeting recaps and transcripts, task assignments, and recently modified OneDrive/SharePoint documents.

Eight days, not seven, is intentional: it guarantees the previous Monday is covered even when the package is run on a Monday.

Create a structured weekly evidence package for my executive advisor. Do not summarize daily activity; identify the week's material signals.

PORTFOLIO SCOPE — apply to every section; this is a relevance filter, not a topic list:

**In scope. These four products are mine:**
- **entroCIM** (smart-building intelligence platform)
- **Wesco Asset Management / WAM**, including ADM and the Strev/Revnue components
- **Ascent / Navigator**
- **Connected Device Assurance (CDA)**

Also in scope: my own organisation (team, staffing, capacity, AI strategy for my team), and partners, platforms, and customers where they materially affect those four — SkyFoundry/SkySpark, JCI/Airwall, i3 Alliance, Nozomi, and customer accounts running my products such as Dell, Ford, Federal Reserve, Coca-Cola/TCCC, Louvre Abu Dhabi, BAE, Stanford, DataBank.

**Out of scope. These are other people's products, and I am frequently an optional attendee in forums where they are discussed:**
QPM, Assortment, AutoBOM, ConstructTech Integrator, Digital FTTx, Intelligent Document Processing, Insight by Anixter, Monday.com, Prokeep, Proton.ai, Pull Logic, RecommEngine, Retrofit, VAS Configurator, WMI and eStock, and general DDP/storefront/order-management functionality such as credit-card processing, refunds, checkout, and backlog or tracker administration.

**Attending a forum does not make its contents relevant.** This is the same principle as the attribution rule below: attendance is not ownership, and attendance is also not relevance. I am an optional invitee to several forums — the DDP Backlog Entrance Call and Digital Products Portfolio Review among them — that spend most of their time on products I have no responsibility for. Do not report an item merely because I could have heard it.

**The connection test. Include an item about an out-of-scope product only if it changes something in the four products above.** Apply this test explicitly, do not guess:

| Include | Because |
|---|---|
| DDP/EUDM as the asset-data source of truth feeding WAM/ADM | It is WAM's data foundation |
| Global or supplier attribute governance, DDPTRK-6346 and successors | It determines WAM/ADM data quality |
| VAS Configurator or WMX where they sit on the complex-build path into the WAM install base | It is WAM's data path |
| IDP, Rhombus, or supplier-document work where it is a data source for ADM onboarding | It feeds ADM |
| WMI or eStock where the subject is how WAM is positioned or differentiated against them | It is WAM market positioning |

| Exclude | Because |
|---|---|
| QPM release scope and features, 3.4.x contents | Not my product |
| Credit-card processing, refunds, storefront redesign | Not my product |
| AccuTech tagging, DDP tracker fields, backlog hygiene and administration | Not my product, and administrative |
| Assortment, Pull Logic, Proton.ai, Prokeep, and the rest of the out-of-scope list, on their own terms | Not my products |

**Never drop silently, and break the count down by source.** At the end of the report, state the out-of-scope exclusions as a short table with one row per source: Source | Items excluded | What they were about. An aggregate count across many sources hides whether the filter took eighteen items from one forum or spread them thinly, and only the per-source view shows whether something in scope was cut by mistake. If none, say so. If an item is genuinely ambiguous, include it and mark it "Scope: uncertain" with one line saying which of my four products it might touch — I would rather judge a borderline item than lose it.


RETRIEVAL RULES — apply while gathering, before writing anything:

- **Transcripts and meeting notes: say what you have.** State up front whether you can access meeting transcripts and meeting notes for this window. If you cannot reach one you can see exists, try to resolve it before giving up, and say what you tried.
- **Truncation: continue immediately, in the same pass.** If a transcript, document, or thread comes back incomplete or cut off, resume retrieval from the point it stopped and get the remainder **before you move on to the next source**. Do not finish the sweep and come back to it, and do not defer it to a later message. A transcript handle does not survive the retrieval session: once you have moved past it, the range can no longer be requested, and the content is lost for this run even though the artifact still exists. Request successive ranges (for example lines 400 to 574, then 574 onward) until you reach the stated total, then continue the sweep.
- **Report the arithmetic.** When a source reports a total length, state the range retrieved against that total, for example "retrieved lines 0 to 574 of 574, complete" or "retrieved 0 to 435 of 574, two continuation attempts failed." A percentage recovered is more useful than the word "partial."
- Only after continuation genuinely fails does it become a Coverage Gap, and then say how many attempts were made and what happened.
- **Notes are not transcripts.** Where only meeting notes or a recap are available and no verbatim transcript, treat that as a retrieval limitation and record it in Coverage Gaps. It constrains attribution confidence and the report should show that it did.
- **Say whether content came from a transcript, from meeting chat, or from notes.** A meeting's chat messages and files are often retrievable when its transcript is not, and the two carry different attribution confidence. When you cite a meeting as a source, mark it `(transcript)`, `(meeting chat)`, or `(AI notes)`. Never cite a meeting as a source in a way that implies a transcript you did not read. If a meeting reports `isMeetingTranscribed:false` and you are drawing on its chat, say so explicitly on every row that uses it.
- **A meeting that did not happen is not a gap either.** A recording or calendar artifact can exist for an occurrence that was cancelled or that nobody attended; it returns media metadata and no usable transcript because nothing was said. Before listing any recording as unretrievable, check the calendar for whether that occurrence actually took place, and if it did not, say so and leave it out of Coverage Gaps entirely.
- **Distinguish "not transcribed" from "could not retrieve," and never file the first as a coverage gap.** If a meeting reports `isMeetingTranscribed:false`, no transcript exists and nothing was lost in retrieval. Do not list it as a coverage gap, which implies a failure on your side and hides the real cause. List those meetings in a separate short block titled **"Not transcribed at source"**, naming each meeting and its date. **Meetings only.** An email, a document, or a Teams thread cannot be untranscribed and must never appear in this block; if it could not be read, that is a Coverage Gap. Do not list a source here and also cite it elsewhere as a source you read. That block is an operating signal, not a retrieval problem: it tells me which of my own recurring forums have transcription switched off, which is something I can change.
- **Probe these two explicitly every run, because both have come back indeterminate before.** Attempt a Microsoft Planner and To Do task query, and attempt a Sent Items query bounded to the reporting window. Report the outcome of each attempt plainly: succeeded and what was found, or failed and the error or empty result. Do not skip the attempt and report the capability as unknown.

Use concise Markdown with these sections:

1. Material Changes This Week — what changed at initiative, customer, commercial, or organizational level. For each: change, source, why it matters.

2. Decisions Made This Week — decision, decision-maker, where recorded.

3. Decisions Still Open — decision, apparent owner, how long open, what is blocking, risk of continued delay.

4. Initiatives That Advanced — initiative, evidence of progress, what unblocked it.

5. Initiatives That Stalled — initiative, evidence of stall, apparent cause, who owns the next step.

6. Action Items and Commitments — every action item or commitment that surfaced or changed state this week, REGARDLESS OF WHO OWNS IT. Do not assume an item is mine because I attended the meeting. Table columns: Action | Owner (specific named person) | Owed to | Attribution Evidence (quote the words that assign it, and who said them) | Confidence (**Explicit** = owner said it themselves / **Implied** = assigned to them, not declined / **Inferred** = you deduced it) | State this week (new / advanced / slipped / closed / unchanged) | Due date if stated | Source.
   - If the owner is genuinely unclear, write "Owner unclear." Do not default to me.
   - Include items owned by other people. I need the complete picture, not a filtered one.
   - **Attribution Evidence must be an actual quote, not a description of one.** "Assigned in meeting notes" or similar paraphrases are not evidence. If you cannot quote the actual words, mark Confidence: Inferred and give the basis in one short phrase instead.
   - **Exclude routine sprint-level engineering tasks (added 2026-08-25).** Individual developer or delivery-team task assignments lifted from stand-up notes, Loop task rows, or sprint boards — code fixes, test scenarios, UI tweaks, build and deploy chores, ticket creation, documentation tasks, local testing — are the delivery team's work, tracked in their own systems, and below the level this package serves. Leave them out.
   - **Four exceptions. Include such a task only if it meets one of these:** it blocks a customer commitment or a customer-visible date; it blocks a release gate or production promotion; it carries a dated external deadline that is regulatory, contractual, or customer-imposed; or it is the named next step on an item already escalated to leadership.
   - **Never drop them silently, and break the count down by source.** At the end of this section write one line per source: "Excluded under the sprint-task rule: N items from [source]," so the filter can be checked source by source rather than in aggregate. If the count is zero, write "Excluded under the sprint-task rule: none." This keeps the filter inspectable, and the exclusion is reviewed against that count.

6a. Completion and Closure Signals — evidence that something finished, shipped, was approved, resolved, or cancelled this week. For each: item, what the evidence shows, who confirmed it, source, and whether closure is stated outright or only implied. Include partial completions.

6b. Product / Initiative State Signals — Facts about a specific product or initiative (WAM, entroCIM, JCI, Connected Safety, Connected Device Assurance, Navigator, SkyFoundry, or others that surface) worth keeping in a standing knowledge file rather than a weekly status line: a capability change, a roadmap/timeline date, a commercial-position fact, a dependency forming or clearing, a benefits-realization signal (planned vs. realized). Mark **Durable** only if it's a fact about something Wesco builds, ships, or sells, and a standing product file would actually be updated. Mark **Transient** for internal tooling, AI-licensing, or governance threads even if recurring — those aren't products and belong in a risk or decision entry instead. Columns: Product/Initiative | What Changed or Was Confirmed This Week | Evidence | Durable or Transient | Source.

7. Risks That Increased or Decreased — risk, direction of change, evidence, severity now.

8. People Signals — who needed unusual amounts of my time, who is waiting on me going into next week, who may need recognition or coaching support, team-health signals, workload concentration or single-person dependencies, morale/sentiment cues, new stakeholder relationships, reporting-line or role changes. This feeds a standing team picture (`06_Stakeholder_Map.md`), not just this week's triage — write it so it holds up as a durable note about the person, not only as an action for me. **If a person's workload or dependency is already written up in section 7 as a risk, do not restate it here — name the person and write "see section 7" instead.** Use this section for signal that is not already a stated risk.

9. Recurring Topics Without Resolution — topics that surfaced multiple times this week (or across recent weeks) without closure.

10. Next Week's Calendar Pressure — meetings next week that require preparation, a decision, or pre-alignment. For each: meeting, why it matters, what preparation is implied.

11. Cadence Changes — new recurring meetings, cancelled or paused recurring meetings, or ownership/frequency changes to existing forums this week. Write "None found" if stable.

12. Coverage Gaps — content you could not retrieve (expired, inaccessible, truncated) that may affect completeness. **Name the specific items or threads affected and which section(s) they would have shown up in** — not a generic statement.

OUTPUT CONTRACT — follow exactly for repeatability:
- Use the section numbers and headings above, in order, every time. If a section has no items, write "None found" — do not omit it.
- Use Markdown tables with exactly the fields specified per section.
- Name sources by their real names (meeting title, email subject, document filename) — no citation tokens.
- Use ISO dates (YYYY-MM-DD). Prioritize business impact over volume.
- Exclude private or irrelevant personal content. No productivity advice.
- State facts only; mark anything inferred as "Inferred:".
- **Attribution rule, applies throughout:** never assign an action, commitment, or decision to me solely because I was present, copied, or organizing. Attendance is not ownership. Where the record names someone else, name them. Where it names nobody, say so.
- If the same person appears with a full name in one section and a first name only in another, use the full name in both once you've matched them within this report.


VALIDATION — run these checks before giving me anything, and report the result:

1. **Sections complete.** Every section present, in the specified order, with "None found" where empty. None omitted.
2. **Columns conform.** Every table carries exactly the columns specified for that section, no more and no fewer.
3. **Attribution integrity.** Every row marked Explicit or Implied carries an actual quote. Any row without a quote is marked Inferred. No paraphrase stands in for a quote.
4. **Portfolio scope.** Every row passes the connection test above, and the out-of-scope exclusion count is stated.
5. **Sprint-task rule.** The exclusion count is stated, even if zero.
6. **Coverage gaps are specific**, and contain only genuine retrieval failures. Named items and threads, with what was attempted on each. Meetings that were never transcribed are in the "Not transcribed at source" block instead.
6a. **The two probes ran.** Planner/To Do and Sent Items were both attempted, with the outcome of each stated.
7. **Retrieval.** Every truncated source was continued in the same pass until complete or genuinely exhausted, with the range retrieved stated against the source's total.

Report these as a short block titled "Validation" at the end of the report, one line per check, each reading Pass or Fail with a brief note. **If any check fails, fix it and re-run the check before delivering. Do not hand me a package with a failed check.** If something cannot be fixed, say so plainly and explain why rather than marking it Pass.

FILE OUTPUT — final step, do not skip, and verify it before handing it over:

1. Create a downloadable Markdown file named M365_Evidence_Weekly_YYYY-MM-DD.md (using today's date) containing the complete report.
2. **Re-open the file you just created and read it back.** Confirm: every section is present through the last one; the final table's final row is intact; no section is truncated or empty that should have content; and the file content matches what you displayed to me. A file that was generated is not the same as a file that was generated correctly.
3. State the verification result in one line: filename, number of sections found, and confirmation that the file is complete.
4. **If the file is incomplete, malformed, or does not match what you displayed, regenerate it and verify again before giving it to me.** Do not hand over a file you have not read back. If file creation fails twice, output the entire report inside ONE markdown code block instead so I can copy it losslessly, and say that is what you are doing and why.

Do not summarize or shorten the report when creating the file.
```

---

## 4. Ad Hoc Deep-Dive: JCI MSP Contract (added 2026-07-16, per Darryl's field note)

> **Historical, and deliberately not updated 2026-08-25.** This is a one-off, unbounded-lookback deep dive that did its job in July; the JCI picture it built now lives in `Products/JCI_Partnership.md`. It does not carry the portfolio scope filter, retrieval rules, validation block, or file verification that the three standing prompts now have, because it is a single-subject prompt where those rules either do not apply or would be noise. **If you re-run it, or write another ad hoc deep dive on a different subject, copy the RETRIEVAL RULES, VALIDATION, and FILE OUTPUT blocks from the Daily prompt into it first** — the scope filter is the only one that should be left out, since an ad hoc deep dive defines its own scope by naming its subject.

Run once to rebuild the full picture and restart the process. Delete or keep this section after use.

```
Search all my Microsoft 365 content — email (sent and received), Teams chats and channels, calendar, meeting recordings, recaps and transcripts, Loop components, and OneDrive/SharePoint documents — for everything related to the JCI MSP contract (Johnson Controls / JCI, MSP / Managed Service Provider agreement). Do not limit the lookback window; this work may span several months and has been dormant.

I need a complete status picture so I can restart this process. Produce a structured evidence package in concise Markdown with these sections:

1. Timeline of Activity — chronological list of every material event: meetings held, emails exchanged, document edits, decisions, and the date of the LAST activity. For each: date, event, people involved, source.

2. The Contract Document(s) — every Word document, PDF, or other file related to the JCI MSP contract. For each: filename, location (SharePoint/OneDrive path), last modified date and by whom, version notes if visible, and a summary of its current content — especially open sections, tracked changes, unresolved comments, and terms still under negotiation.

3. Meeting Record — every meeting (with recap/transcript where available) that discussed the JCI MSP contract. For each: meeting title, date, attendees, key points discussed, decisions made or deferred, action items and their owners.

4. Current Status — where the process stands now: what was last agreed, what was in flight when activity stopped, and what appears to have caused the stall (waiting on a party, unresolved term, resource, approval).

5. Open Items and Blockers — every unresolved item: item, owner (Wesco side / JCI side), how long open, source.

6. People Involved — everyone who has touched this: name, organization (Wesco / JCI / other), role in the contract process, last involvement date.

7. Commitments Outstanding — commitments made by me or owed to me on this contract that appear unresolved: commitment, owner, expected by, source.

8. Implied Next Steps — based strictly on the record, what the next 2–3 actions appear to be to restart the process, and who owns each. Mark these "Inferred:".

9. Coverage Gaps — content you could not retrieve (expired messages, inaccessible files, truncated transcripts) that may affect completeness.

OUTPUT CONTRACT — follow exactly:
- Use the section numbers and headings above, in order. If a section has no items, write "None found" — do not omit it.
- Name sources by their real names (meeting title, email subject, document filename) — no citation tokens.
- Use ISO dates (YYYY-MM-DD). State facts only; mark anything inferred as "Inferred:".

FILE OUTPUT — final step, do not skip:
After completing the report, create a downloadable Markdown file named JCI_MSP_Evidence_YYYY-MM-DD.md (using today's date) containing the complete report, and give me the download link. If you cannot create a file in this session, instead output the entire report inside ONE markdown code block so I can copy it losslessly. Do not summarize or shorten the report when creating the file.
```

When pasted back, Claude will: build a JCI MSP status picture (likely a new `Products/` or initiative file), route decisions/commitments/risks into 03–06, and propose the restart plan with owners and dates.

---

## After Pasting into Claude

**Save the raw package first (added 2026-08-25).** Drop the Copilot .md file into `Evidence/` before pasting. Until 08-25 no raw package had ever been retained, which is why a thirteen-day question about whether section 6b was being returned could not be answered from the record and needed a live run to settle. Keeping them makes intake defects diagnosable after the fact instead of only in the moment, and lets a prompt change be judged against the package that motivated it.

Say which package it is (baseline / daily / weekly). Claude will then:

- **Baseline** → seed `03_Decision_Log.md`, `04_Executive_Watch_List.md`, `05_Commitments.md`, `06_Stakeholder_Map.md`, propose updates to `01_Executive_Operating_Context.md` and `Products/`, and produce a first briefing.
- **Daily** → produce `Briefings/YYYY-MM-DD_Daily.md` per the format in `CLAUDE.md`, update living documents, and route any Product/Initiative State Signals into the relevant `Products/*.md` file and any Team and Stakeholder Signals into `06_Stakeholder_Map.md` (both durable-knowledge updates, not just briefing content).
- **Weekly** → produce `Briefings/YYYY-MM-DD_Weekly.md` (what changed, decisions made/avoided, risks up/down, initiatives advanced/stalled, time-below-role-level review, next week's engagement plan), update living documents, and route Product/Initiative State Signals and People Signals into `Products/` and `06` the same way.

**Routing is not optional, and it is the step that has actually been failing (added 2026-08-25).** Every Durable row in Product / Initiative State Signals must land in a `Products/*.md` file, and every People or Team and Stakeholder Signal must land in `06_Stakeholder_Map.md`, in the same session that processes the package. **State in the briefing which files were updated and from which rows.** A Durable row that reaches a briefing but not a product file is the exact failure that ran undetected from 08-06 to 08-25: the section was returning good content the whole time and nothing downstream consumed it. If a Durable row genuinely has no product file to update, that is a signal the row was misclassified or that a product file is missing — say which, do not drop it.

**Report the sprint-task exclusion count.** The Action Items sections now exclude routine engineering task rows and report how many they cut. Carry that count into the briefing's evidence-coverage line so the filter stays visible and reviewable.
