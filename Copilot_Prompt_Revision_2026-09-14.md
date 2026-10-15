# Copilot Intake Prompt Revision — 2026-09-14

**Status: APPLIED 2026-09-14.** All five edits are live in `02_Copilot_Intake_Prompts.md` across all three standing prompts. The header revision note is in that file; the log entry is in `10_Pilot_Feedback_Log.md`. Pre-change copies: `Archive/02_Copilot_Intake_Prompts_pre-2026-09-14.md` and `Archive/10_Pilot_Feedback_Log_pre-2026-09-14.md`. This memo is retained as the rationale record for the change.

Applies to all three standing prompts (Baseline, Daily, Weekly), consistent with the 2026-08-07 principle that the three are kept aligned. Machine-applicable patch: `Copilot_Prompt_Revision_2026-09-14.diff` in this folder.

## What prompted this

Two weekly runs were executed on 2026-09-14 against the same prompt, the same window, and the same tenant. Run 1 produced a 6 KB package with 2 action items and marked its own validation Pass on checks that had failed. The re-run produced a full package with complete transcript arithmetic on six sources. The prompt was not changed between them.

The review document Copilot produced in between (`M365_Prompt_Retrieval_Review_2026-09-14.md`) argued that same-pass continuation and line arithmetic are architecturally unreliable and should be removed from the contract. The re-run performed both. **Its central recommendations are therefore declined.** Four of its secondary recommendations are adopted below, plus one rule it did not identify.

## The five edits

**1. A search result is not a retrieval attempt.** New rule in RETRIEVAL RULES. This is the root cause and was not in the review document.

Run 1's own wording was "Transcript available but truncated in search results; continuation not retrieved," for `Weekly Sync` and `entroCIM Backlog Deep Dive`. The re-run opened both and reached 0–308 of 308 and 0–815 of 815. Run 1 never opened the items. It searched, got a ranked snippet, and reported the snippet's clipping as a transcript limitation. The prompt required continuation from a truncation point but never said that a search result is not a retrieval attempt.

Paired with it: check `isMeetingTranscribed` before using the word transcript. Run 1 reported `Wesco / SkyFoundry` as a truncated transcript and quoted two Explicit-confidence action items from it. The re-run shows that meeting has no transcript at all. Reporting a non-existent transcript as truncated manufactures a source, which is worse than reporting a gap.

**2. ISO reporting window stated at the top of every run.** Adopts review §9.6. The re-run did this unprompted.

**3. Retrieval and Source-Status Statement before section 1.** Adopts review §9.7. The re-run did this unprompted and it is the single most useful addition: it makes the recall of the whole run visible, including the sources that came back complete, which is exactly what run 1's thinness concealed. It carries no Pass or Fail and does not replace Coverage Gaps.

**4. Exclusion accounting: counting unit, separation of the two tables, and search noise is not an exclusion.** Adopts review §5.5 and fixes two defects the re-run itself demonstrated. The re-run counted the same sprint-task exclusions in both the section 6 line and the portfolio-scope table (Daily Stand Up 12, Daily Scrum 14, WAM Refinement 9, entroCIM Deep Dive 6), and counted 18 "exclusions" from a SharePoint search that were price lists, receipts, and tax files — never candidate signals.

**5. Deduplication across sources.** Adopts review §9.5.

Validation checks 7, 8, and 9 are updated or added so each new rule is inspectable rather than advisory.

## What was declined, and why

| Review recommendation | Decision | Reason |
|---|---|---|
| §5.6 Add a self-assigned "Not verifiable" validation status | **Declined** | The validation block is self-reported and already over-reports. Run 1 marked portfolio scope and attribution integrity Pass when both failed. A third status Copilot can assign itself removes a forcing function without adding a check. |
| §4.4 Remove line-range arithmetic | **Declined** | Performed correctly on 08-25, 09-09, and the 09-14 re-run. |
| §5.3 Replace continuation with a status vocabulary | **Declined as a replacement, partially adopted as an addition** | The status vocabulary is useful and now lives in the Retrieval and Source-Status Statement. It does not relieve the obligation to continue. |
| §5.2 Redefine "complete" relative to the evidence set | **Declined as prompt language** | True as a description, but as an instruction it licenses run 1. The honest version of this now lives in the acceptance gate, not in the contract. |
| §4.12 / §9.3 Narrow People Signals to observable evidence | **Deferred** | Sound in principle. Not bundled here so the next package is attributable to a single change. Revisit after two clean runs. |

## Header revision note — paste into `02_Copilot_Intake_Prompts.md` after the 08-25 third-pass block

> **Revised 2026-09-14 after a controlled re-run, and the finding is different in kind from every previous revision.** Two weekly packages were produced on the same day, against the same prompt and the same window. Run 1 returned 6 KB, 2 action items, no out-of-scope exclusion table, no source-type markers, and a validation block reading Pass on checks that had plainly failed. The re-run returned a full package with six transcripts retrieved to their stated totals, continuation performed in the same pass on two of them, the exclusion table present, and source-type markers throughout. **No prompt wording changed between the two.** The defect is run-to-run variance, not contract design.
>
> In between the two runs, Copilot was asked to analyse its own performance and produced `M365_Prompt_Retrieval_Review_2026-09-14.md`, a fluent and well-structured argument that same-pass continuation and line arithmetic exceed what the retrieval layer can do and should be struck from the prompt. Its own next run did both. **Standing lesson: Copilot's account of its own capabilities is not evidence. Ask it what it retrieved and hold it to the arithmetic; do not ask it what it can retrieve.** The review document is retained as history, not as a specification.
>
> **The root cause, which the review document did not identify.** Run 1 described `Weekly Sync` and `entroCIM Backlog Deep Dive` as "truncated in search results." A search returns a ranked snippet; opening the item returns the artifact. Run 1 never opened them. The re-run did, and both were complete. Worse, run 1 reported `Wesco / SkyFoundry` as a truncated transcript and quoted two Explicit-confidence action rows from it; that meeting reports `isMeetingTranscribed:false` and has no transcript. Rule 1 below closes both.
>
> 10. **A search result is not a retrieval attempt**, and a meeting's transcription flag is checked before the word transcript is used. Added to the retrieval rules of all three prompts, with validation check 7 extended to make it inspectable.
> 11. **Report header added**: the ISO reporting window and a Retrieval and Source-Status Statement before section 1 (review §9.6 and §9.7, both of which the re-run adopted on its own). The statement reports what was retrieved, carries no Pass or Fail, and does not replace Coverage Gaps. It exists so that a thin run is visible as a thin run.
> 12. **Exclusion accounting added**: a counting unit, a prohibition on counting an item in both exclusion tables, and a rule that broad-search noise is not an exclusion. The re-run double-counted 41 sprint-task exclusions into the portfolio-scope table and counted 18 unrelated tenant files as scope exclusions.
> 13. **Deduplication rule added** to the output contract (review §9.5).
>
> **What was declined.** The review's central proposals were rejected: no self-assigned "Not verifiable" validation status, no removal of line arithmetic, no redefinition of completeness inside the contract. Relaxing the standard on the strength of the worse of two observed runs would have made run 1 compliant. The People Signals narrowing (§9.3) is sound but deferred, so the next package is attributable to a single change.
>
> **This revision does not fix the variance.** No wording can. The variance is addressed by an acceptance gate outside the prompt, recorded in `10_Pilot_Feedback_Log.md`, and by the transcript register in `Reference/Transcript_Register.md`, which converts Copilot's unfalsifiable access claims into checkable ones.

## Pilot feedback log entry — paste into `10_Pilot_Feedback_Log.md`

> ### 2026-09-14 — Run-to-run variance is the failure mode, not retrieval capability
>
> **What happened.** Darryl reported sustained disappointment with the daily and weekly packages, specifically Copilot's inconsistent claims about access to meeting notes and transcripts: sometimes it says it cannot reach them, sometimes it plainly can. He asked Copilot to analyse its own performance; it produced `M365_Prompt_Retrieval_Review_2026-09-14.md`, recommending that the retrieval contract be relaxed. Before acting on it, the 09-14 weekly was re-run with the prompt unchanged as a control.
>
> **Result.** Run 1: 6 KB, 2 action items, 56 table rows, no out-of-scope exclusion table, no `(transcript)` / `(meeting chat)` / `(AI notes)` markers, validation Pass on portfolio scope and attribution integrity, both of which had failed. Re-run: full package, six transcripts retrieved to stated totals, continuation in the same pass on two, exclusion table present, markers throughout. Baseline for comparison: 08-25 36 KB, 08-31 35 KB, 09-09 29 KB with 134 rows.
>
> **Root cause.** Run 1 stopped at the search layer and reported snippet clipping as transcript truncation. It never opened the items. The re-run opened them: `Weekly Sync` 0–308 of 308, `entroCIM Backlog Deep Dive` 0–815 of 815. This is a run-quality defect, not a platform boundary, and it explains the pattern Darryl described: the variable is whether Copilot performs the open-and-continue step, not whether access exists.
>
> **Second finding, more consequential.** Neither run is a superset of the other. Run 1 carried the FRBNY descope thread as a material change and a High customer-delivery risk; the re-run has no FRB row anywhere. Run 1 carried two Wesco/SkyFoundry actions; the re-run has none. The re-run carried the entroCIM 3.1.12.14 release date, Strev ownership, i3 Section 12, the Harsha E AOP removal, and six closure signals that run 1 missed entirely. **A High risk on a named in-scope customer appeared in one run and vanished in the other.** No single run can be treated as complete, and the 09-14 package fed to the registers is the merged union of both (`Evidence/M365_Evidence_Weekly_2026-09-14_ACCEPTED.md`).
>
> **Third finding: fabricated attribution.** Run 1's two action rows were quoted at Explicit confidence from `Wesco / SkyFoundry`, a meeting that reports `isMeetingTranscribed:false`. There was no transcript to quote. This is the 2026-08-07 boilerplate-attribution defect returning in a harder form: not a paraphrase standing in for a quote, but a quote attributed to a source that does not exist. Attribution integrity was marked Pass. Both rows are carried into the accepted package downgraded to Inferred with the quotation marks removed.
>
> **Acceptance gate, effective immediately.** No package feeds Registers A–D until it passes four checks. Any failure means re-run, not repair.
>
> 1. **Source integrity.** Every Explicit or Implied row's source appears in the Retrieval and Source-Status Statement as a retrieved transcript. No row quotes a meeting listed under "Not transcribed at source."
> 2. **Structural completeness.** The out-of-scope exclusion table is present, the sprint-task counts are present and do not duplicate it, and the retrieval statement's own count matches its own list.
> 3. **Volume floor.** Below roughly 15 KB, or fewer than about 60 table rows, against a 21–36 KB and 100+ row baseline, the run is treated as failed. A quiet week does not produce a package a quarter the usual size; a failed sweep does.
> 4. **Continuity.** Any in-scope customer or initiative thread carried in the prior package and absent from this one is named and explained, not silently dropped.
>
> Run 1 fails three of the four in under a minute. This gate is Claude's to run on receipt of each package, before any register update.
>
> **Standing lesson.** Copilot's self-assessment of its own capabilities is not evidence and must not drive prompt design. It produced a confident, well-structured capability ceiling that its own next run cleared within the day. Ask what it retrieved; hold it to the arithmetic.
>
> **Related actions.** Prompt edits drafted in `Copilot_Prompt_Revision_2026-09-14.md`. Transcript register created at `Reference/Transcript_Register.md`. The daily prompt has not been run since 2026-08-27, which removes the independent second look that would have caught the FRB thread.

## The patch

```diff
--- orig.md	2026-09-14 15:00:36.947026499 +0000
+++ new.md	2026-09-14 15:01:17.819026518 +0000
@@ -79,6 +79,8 @@
 RETRIEVAL RULES — apply while gathering, before writing anything:
 
 - **Transcripts and meeting notes: say what you have.** State up front whether you can access meeting transcripts and meeting notes for this window. If you cannot reach one you can see exists, try to resolve it before giving up, and say what you tried.
+- **A search result is not a retrieval attempt, and a snippet limit is not a truncated source.** Search returns a ranked excerpt of an artifact, not the artifact. An excerpt that stops mid-sentence is a limit of the search layer and must never be reported as a truncated transcript, document, or thread. Before you describe any source as truncated, incomplete, or unavailable, open the item itself and attempt continuation on the opened item. Then say which you did, in these words: "opened and continued," "opened, no continuation needed," or "search snippet only." A statement that content was "truncated in search results" describes the search layer, not the artifact, and is not admissible as a Coverage Gap.
+- **Check the transcription flag before you use the word transcript.** Read `isMeetingTranscribed` for the meeting before describing its transcript in any way. If it is false, no transcript exists, nothing about it can be truncated, and nothing may be quoted from one. Reporting a transcript that does not exist as truncated is a worse error than reporting a gap, because it manufactures a source.
 - **Truncation: continue immediately, in the same pass.** If a transcript, document, or thread comes back incomplete or cut off, resume retrieval from the point it stopped and get the remainder **before you move on to the next source**. Do not finish the sweep and come back to it, and do not defer it to a later message. A transcript handle does not survive the retrieval session: once you have moved past it, the range can no longer be requested, and the content is lost for this run even though the artifact still exists. Request successive ranges (for example lines 400 to 574, then 574 onward) until you reach the stated total, then continue the sweep.
 - **Report the arithmetic.** When a source reports a total length, state the range retrieved against that total, for example "retrieved lines 0 to 574 of 574, complete" or "retrieved 0 to 435 of 574, two continuation attempts failed." A percentage recovered is more useful than the word "partial."
 - Only after continuation genuinely fails does it become a Coverage Gap, and then say how many attempts were made and what happened.
@@ -125,6 +127,20 @@
 
 **Never drop silently, and break the count down by source.** At the end of the report, state the out-of-scope exclusions as a short table with one row per source: Source | Items excluded | What they were about. An aggregate count across many sources hides whether the filter took eighteen items from one forum or spread them thinly, and only the per-source view shows whether something in scope was cut by mistake. If none, say so. If an item is genuinely ambiguous, include it and mark it "Scope: uncertain" with one line saying which of my four products it might touch — I would rather judge a borderline item than lose it.
 
+EXCLUSION ACCOUNTING — applies to both exclusion tables, so the counts stay comparable run to run:
+
+- **Counting unit.** One excluded item means: email, one unique message; chat or channel, one unique message or reply; meeting, one distinct candidate signal, never one utterance; file, one distinct candidate signal or task row; Planner or private task, one task object. Apply the unit consistently, and name it where a source is ambiguous.
+- **The two filters are separate and their tables must not overlap.** Portfolio-scope exclusions are candidate signals that failed the connection test. Sprint-task exclusions are in-scope signals removed for sitting below the level this package serves. No item is counted in both. Where a source appears in both tables, the two counts must refer to different items.
+- **Search noise is not an exclusion.** Unrelated tenant documents returned by a broad file search, price lists, invoices, receipts, personal files, and site assets were never candidate signals and must not be counted. If a search returned mostly noise, say so in the Retrieval and Source-Status Statement rather than inflating an exclusion count.
+
+
+REPORT HEADER — the first lines of the report, before section 1:
+
+1. **Reporting window in ISO format**, calculated from today's date and stated as an inclusive range covering this prompt's lookback. For a weekly 8-day run on 2026-09-14 the window is 2026-09-07 through 2026-09-14.
+2. **Retrieval and Source-Status Statement.** One line per material source: source name, artifact type (transcript / meeting chat / AI notes / email / Teams channel / file / task query), what was actually done (opened and continued / opened, no continuation needed / search snippet only), and the range retrieved against the source's total where the interface supplies one. State the outcome of the Sent Items probe and the Planner/To Do probe here as well.
+
+This block reports what was retrieved. It carries no Pass or Fail, it is not Coverage Gaps, and it is not the Validation block. Coverage Gaps remains a list of genuine failures; this statement is the inventory that makes the recall of the whole run visible, including the sources that came back complete.
+
 
 1. Active Initiatives and Workstreams — Each initiative or recurring topic I am actively involved in. For each: name, current state, my role (owner / decision-maker / escalation point / participant), key people, and apparent momentum (advancing, stalled, unclear).
 
@@ -164,6 +180,7 @@
 - Name sources by their real names (meeting title, email subject line, document filename). Do not use citation tokens or reference IDs.
 - Use ISO dates (YYYY-MM-DD) everywhere.
 - State facts only; mark anything inferred as "Inferred:".
+- **Deduplicate across sources.** Where one underlying signal appears in an email, a meeting recap, a transcript, and a chat, report one substantive row and name the strongest primary source first. Add a second source to that row only where it adds attribution, timing, or state-change evidence. Do not report the same signal as separate rows, and do not count its duplicates as separate actions or separate exclusions.
 - If the same person appears with a full name in one section and a first name only in another, use the full name in both once you've matched them within this report.
 
 VALIDATION — run these checks before giving me anything, and report the result:
@@ -175,7 +192,9 @@
 5. **Sprint-task rule.** The exclusion count is stated, even if zero.
 6. **Coverage gaps are specific**, and contain only genuine retrieval failures. Named items and threads, with what was attempted on each. Meetings that were never transcribed are in the "Not transcribed at source" block instead.
 6a. **The two probes ran.** Planner/To Do and Sent Items were both attempted, with the outcome of each stated.
-7. **Retrieval.** Every truncated source was continued in the same pass until complete or genuinely exhausted, with the range retrieved stated against the source's total.
+7. **Retrieval.** Every truncated source was opened and continued in the same pass until complete or genuinely exhausted, with the range retrieved stated against the source's total. No source is reported as truncated or unavailable on the basis of a search snippet, and no meeting reporting `isMeetingTranscribed:false` is described as having a truncated transcript or quoted as one.
+8. **Report header.** The ISO reporting window and the Retrieval and Source-Status Statement are both present before section 1, and every material source cited in the report appears in the statement.
+9. **Exclusion accounting.** Both exclusion tables use the defined counting unit, no item is counted in both, and search noise is not counted as an exclusion.
 
 Report these as a short block titled "Validation" at the end of the report, one line per check, each reading Pass or Fail with a brief note. **If any check fails, fix it and re-run the check before delivering. Do not hand me a package with a failed check.** If something cannot be fixed, say so plainly and explain why rather than marking it Pass.
 
@@ -202,6 +221,8 @@
 RETRIEVAL RULES — apply while gathering, before writing anything:
 
 - **Transcripts and meeting notes: say what you have.** State up front whether you can access meeting transcripts and meeting notes for this window. If you cannot reach one you can see exists, try to resolve it before giving up, and say what you tried.
+- **A search result is not a retrieval attempt, and a snippet limit is not a truncated source.** Search returns a ranked excerpt of an artifact, not the artifact. An excerpt that stops mid-sentence is a limit of the search layer and must never be reported as a truncated transcript, document, or thread. Before you describe any source as truncated, incomplete, or unavailable, open the item itself and attempt continuation on the opened item. Then say which you did, in these words: "opened and continued," "opened, no continuation needed," or "search snippet only." A statement that content was "truncated in search results" describes the search layer, not the artifact, and is not admissible as a Coverage Gap.
+- **Check the transcription flag before you use the word transcript.** Read `isMeetingTranscribed` for the meeting before describing its transcript in any way. If it is false, no transcript exists, nothing about it can be truncated, and nothing may be quoted from one. Reporting a transcript that does not exist as truncated is a worse error than reporting a gap, because it manufactures a source.
 - **Truncation: continue immediately, in the same pass.** If a transcript, document, or thread comes back incomplete or cut off, resume retrieval from the point it stopped and get the remainder **before you move on to the next source**. Do not finish the sweep and come back to it, and do not defer it to a later message. A transcript handle does not survive the retrieval session: once you have moved past it, the range can no longer be requested, and the content is lost for this run even though the artifact still exists. Request successive ranges (for example lines 400 to 574, then 574 onward) until you reach the stated total, then continue the sweep.
 - **Report the arithmetic.** When a source reports a total length, state the range retrieved against that total, for example "retrieved lines 0 to 574 of 574, complete" or "retrieved 0 to 435 of 574, two continuation attempts failed." A percentage recovered is more useful than the word "partial."
 - Only after continuation genuinely fails does it become a Coverage Gap, and then say how many attempts were made and what happened.
@@ -248,6 +269,20 @@
 
 **Never drop silently, and break the count down by source.** At the end of the report, state the out-of-scope exclusions as a short table with one row per source: Source | Items excluded | What they were about. An aggregate count across many sources hides whether the filter took eighteen items from one forum or spread them thinly, and only the per-source view shows whether something in scope was cut by mistake. If none, say so. If an item is genuinely ambiguous, include it and mark it "Scope: uncertain" with one line saying which of my four products it might touch — I would rather judge a borderline item than lose it.
 
+EXCLUSION ACCOUNTING — applies to both exclusion tables, so the counts stay comparable run to run:
+
+- **Counting unit.** One excluded item means: email, one unique message; chat or channel, one unique message or reply; meeting, one distinct candidate signal, never one utterance; file, one distinct candidate signal or task row; Planner or private task, one task object. Apply the unit consistently, and name it where a source is ambiguous.
+- **The two filters are separate and their tables must not overlap.** Portfolio-scope exclusions are candidate signals that failed the connection test. Sprint-task exclusions are in-scope signals removed for sitting below the level this package serves. No item is counted in both. Where a source appears in both tables, the two counts must refer to different items.
+- **Search noise is not an exclusion.** Unrelated tenant documents returned by a broad file search, price lists, invoices, receipts, personal files, and site assets were never candidate signals and must not be counted. If a search returned mostly noise, say so in the Retrieval and Source-Status Statement rather than inflating an exclusion count.
+
+
+REPORT HEADER — the first lines of the report, before section 1:
+
+1. **Reporting window in ISO format**, calculated from today's date and stated as an inclusive range covering this prompt's lookback. For a weekly 8-day run on 2026-09-14 the window is 2026-09-07 through 2026-09-14.
+2. **Retrieval and Source-Status Statement.** One line per material source: source name, artifact type (transcript / meeting chat / AI notes / email / Teams channel / file / task query), what was actually done (opened and continued / opened, no continuation needed / search snippet only), and the range retrieved against the source's total where the interface supplies one. State the outcome of the Sent Items probe and the Planner/To Do probe here as well.
+
+This block reports what was retrieved. It carries no Pass or Fail, it is not Coverage Gaps, and it is not the Validation block. Coverage Gaps remains a list of genuine failures; this statement is the inventory that makes the recall of the whole run visible, including the sources that came back complete.
+
 
 Use concise Markdown with these sections:
 
@@ -295,6 +330,7 @@
 - Exclude private or irrelevant personal content. No productivity advice. Do not simply summarize my day.
 - State facts only; mark anything inferred as "Inferred:".
 - **Attribution rule, applies throughout:** never assign an action, commitment, or decision to me solely because I was present, copied, or organizing. Attendance is not ownership. Where the record names someone else, name them. Where it names nobody, say so.
+- **Deduplicate across sources.** Where one underlying signal appears in an email, a meeting recap, a transcript, and a chat, report one substantive row and name the strongest primary source first. Add a second source to that row only where it adds attribution, timing, or state-change evidence. Do not report the same signal as separate rows, and do not count its duplicates as separate actions or separate exclusions.
 - If the same person appears with a full name in one section and a first name only in another, use the full name in both once you've matched them within this report.
 
 
@@ -307,7 +343,9 @@
 5. **Sprint-task rule.** The exclusion count is stated, even if zero.
 6. **Coverage gaps are specific**, and contain only genuine retrieval failures. Named items and threads, with what was attempted on each. Meetings that were never transcribed are in the "Not transcribed at source" block instead.
 6a. **The two probes ran.** Planner/To Do and Sent Items were both attempted, with the outcome of each stated.
-7. **Retrieval.** Every truncated source was continued in the same pass until complete or genuinely exhausted, with the range retrieved stated against the source's total.
+7. **Retrieval.** Every truncated source was opened and continued in the same pass until complete or genuinely exhausted, with the range retrieved stated against the source's total. No source is reported as truncated or unavailable on the basis of a search snippet, and no meeting reporting `isMeetingTranscribed:false` is described as having a truncated transcript or quoted as one.
+8. **Report header.** The ISO reporting window and the Retrieval and Source-Status Statement are both present before section 1, and every material source cited in the report appears in the statement.
+9. **Exclusion accounting.** Both exclusion tables use the defined counting unit, no item is counted in both, and search noise is not counted as an exclusion.
 
 Report these as a short block titled "Validation" at the end of the report, one line per check, each reading Pass or Fail with a brief note. **If any check fails, fix it and re-run the check before delivering. Do not hand me a package with a failed check.** If something cannot be fixed, say so plainly and explain why rather than marking it Pass.
 
@@ -366,10 +404,18 @@
 
 **Never drop silently, and break the count down by source.** At the end of the report, state the out-of-scope exclusions as a short table with one row per source: Source | Items excluded | What they were about. An aggregate count across many sources hides whether the filter took eighteen items from one forum or spread them thinly, and only the per-source view shows whether something in scope was cut by mistake. If none, say so. If an item is genuinely ambiguous, include it and mark it "Scope: uncertain" with one line saying which of my four products it might touch — I would rather judge a borderline item than lose it.
 
+EXCLUSION ACCOUNTING — applies to both exclusion tables, so the counts stay comparable run to run:
+
+- **Counting unit.** One excluded item means: email, one unique message; chat or channel, one unique message or reply; meeting, one distinct candidate signal, never one utterance; file, one distinct candidate signal or task row; Planner or private task, one task object. Apply the unit consistently, and name it where a source is ambiguous.
+- **The two filters are separate and their tables must not overlap.** Portfolio-scope exclusions are candidate signals that failed the connection test. Sprint-task exclusions are in-scope signals removed for sitting below the level this package serves. No item is counted in both. Where a source appears in both tables, the two counts must refer to different items.
+- **Search noise is not an exclusion.** Unrelated tenant documents returned by a broad file search, price lists, invoices, receipts, personal files, and site assets were never candidate signals and must not be counted. If a search returned mostly noise, say so in the Retrieval and Source-Status Statement rather than inflating an exclusion count.
+
 
 RETRIEVAL RULES — apply while gathering, before writing anything:
 
 - **Transcripts and meeting notes: say what you have.** State up front whether you can access meeting transcripts and meeting notes for this window. If you cannot reach one you can see exists, try to resolve it before giving up, and say what you tried.
+- **A search result is not a retrieval attempt, and a snippet limit is not a truncated source.** Search returns a ranked excerpt of an artifact, not the artifact. An excerpt that stops mid-sentence is a limit of the search layer and must never be reported as a truncated transcript, document, or thread. Before you describe any source as truncated, incomplete, or unavailable, open the item itself and attempt continuation on the opened item. Then say which you did, in these words: "opened and continued," "opened, no continuation needed," or "search snippet only." A statement that content was "truncated in search results" describes the search layer, not the artifact, and is not admissible as a Coverage Gap.
+- **Check the transcription flag before you use the word transcript.** Read `isMeetingTranscribed` for the meeting before describing its transcript in any way. If it is false, no transcript exists, nothing about it can be truncated, and nothing may be quoted from one. Reporting a transcript that does not exist as truncated is a worse error than reporting a gap, because it manufactures a source.
 - **Truncation: continue immediately, in the same pass.** If a transcript, document, or thread comes back incomplete or cut off, resume retrieval from the point it stopped and get the remainder **before you move on to the next source**. Do not finish the sweep and come back to it, and do not defer it to a later message. A transcript handle does not survive the retrieval session: once you have moved past it, the range can no longer be requested, and the content is lost for this run even though the artifact still exists. Request successive ranges (for example lines 400 to 574, then 574 onward) until you reach the stated total, then continue the sweep.
 - **Report the arithmetic.** When a source reports a total length, state the range retrieved against that total, for example "retrieved lines 0 to 574 of 574, complete" or "retrieved 0 to 435 of 574, two continuation attempts failed." A percentage recovered is more useful than the word "partial."
 - Only after continuation genuinely fails does it become a Coverage Gap, and then say how many attempts were made and what happened.
@@ -379,6 +425,14 @@
 - **Distinguish "not transcribed" from "could not retrieve," and never file the first as a coverage gap.** If a meeting reports `isMeetingTranscribed:false`, no transcript exists and nothing was lost in retrieval. Do not list it as a coverage gap, which implies a failure on your side and hides the real cause. List those meetings in a separate short block titled **"Not transcribed at source"**, naming each meeting and its date. **Meetings only.** An email, a document, or a Teams thread cannot be untranscribed and must never appear in this block; if it could not be read, that is a Coverage Gap. Do not list a source here and also cite it elsewhere as a source you read. That block is an operating signal, not a retrieval problem: it tells me which of my own recurring forums have transcription switched off, which is something I can change.
 - **Probe these two explicitly every run, because both have come back indeterminate before.** Attempt a Microsoft Planner and To Do task query, and attempt a Sent Items query bounded to the reporting window. Report the outcome of each attempt plainly: succeeded and what was found, or failed and the error or empty result. Do not skip the attempt and report the capability as unknown.
 
+REPORT HEADER — the first lines of the report, before section 1:
+
+1. **Reporting window in ISO format**, calculated from today's date and stated as an inclusive range covering this prompt's lookback. For a weekly 8-day run on 2026-09-14 the window is 2026-09-07 through 2026-09-14.
+2. **Retrieval and Source-Status Statement.** One line per material source: source name, artifact type (transcript / meeting chat / AI notes / email / Teams channel / file / task query), what was actually done (opened and continued / opened, no continuation needed / search snippet only), and the range retrieved against the source's total where the interface supplies one. State the outcome of the Sent Items probe and the Planner/To Do probe here as well.
+
+This block reports what was retrieved. It carries no Pass or Fail, it is not Coverage Gaps, and it is not the Validation block. Coverage Gaps remains a list of genuine failures; this statement is the inventory that makes the recall of the whole run visible, including the sources that came back complete.
+
+
 Use concise Markdown with these sections:
 
 1. Material Changes This Week — what changed at initiative, customer, commercial, or organizational level. For each: change, source, why it matters.
@@ -423,6 +477,7 @@
 - Exclude private or irrelevant personal content. No productivity advice.
 - State facts only; mark anything inferred as "Inferred:".
 - **Attribution rule, applies throughout:** never assign an action, commitment, or decision to me solely because I was present, copied, or organizing. Attendance is not ownership. Where the record names someone else, name them. Where it names nobody, say so.
+- **Deduplicate across sources.** Where one underlying signal appears in an email, a meeting recap, a transcript, and a chat, report one substantive row and name the strongest primary source first. Add a second source to that row only where it adds attribution, timing, or state-change evidence. Do not report the same signal as separate rows, and do not count its duplicates as separate actions or separate exclusions.
 - If the same person appears with a full name in one section and a first name only in another, use the full name in both once you've matched them within this report.
 
 
@@ -435,7 +490,9 @@
 5. **Sprint-task rule.** The exclusion count is stated, even if zero.
 6. **Coverage gaps are specific**, and contain only genuine retrieval failures. Named items and threads, with what was attempted on each. Meetings that were never transcribed are in the "Not transcribed at source" block instead.
 6a. **The two probes ran.** Planner/To Do and Sent Items were both attempted, with the outcome of each stated.
-7. **Retrieval.** Every truncated source was continued in the same pass until complete or genuinely exhausted, with the range retrieved stated against the source's total.
+7. **Retrieval.** Every truncated source was opened and continued in the same pass until complete or genuinely exhausted, with the range retrieved stated against the source's total. No source is reported as truncated or unavailable on the basis of a search snippet, and no meeting reporting `isMeetingTranscribed:false` is described as having a truncated transcript or quoted as one.
+8. **Report header.** The ISO reporting window and the Retrieval and Source-Status Statement are both present before section 1, and every material source cited in the report appears in the statement.
+9. **Exclusion accounting.** Both exclusion tables use the defined counting unit, no item is counted in both, and search noise is not counted as an exclusion.
 
 Report these as a short block titled "Validation" at the end of the report, one line per check, each reading Pass or Fail with a brief note. **If any check fails, fix it and re-run the check before delivering. Do not hand me a package with a failed check.** If something cannot be fixed, say so plainly and explain why rather than marking it Pass.
 
```
