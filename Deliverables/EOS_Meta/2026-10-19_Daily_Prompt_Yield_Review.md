# Daily Copilot Prompt: Yield Review and v2 Rationale

Date: 2026-10-19. Author: Claude, at Darryl's request, from the retained packages in `Evidence/`. Companion to the v2 Daily prompt in `02_Copilot_Intake_Prompts.md`, section 2.

## Question

Copilot shows response-size limits (truncated transcripts, a 6 KB run against a full re-run on 09-14, throttling at 13 forums, malformed file output). Before splitting the Daily prompt or cutting sections, measure what the daily packages actually carry, so the first change is the one with the most leverage.

## Method

Four retained daily packages (2026-08-27, 09-30, 10-01, 10-16), v1 prompt, 14 sections. Counted table rows per section and the number of distinct sources cited, then read the 10-16 package end to end to see what the rows contained. Weekly packages were not scored; they use a different section schema and are out of scope for this change.

## Findings

| Package | Size | Table rows (sections 1 to 13) | Substantive sources | "None found" sections |
|---|---|---|---|---|
| 08-27 | 41 KB | 88 | about 8 (Ford thread, four Teams chats, AI SOP review, T&E AOP email) | 0 |
| 09-30 | 24 KB | 58 | 4 (WAM connect, Agile staff meeting, commercialization doc, ADM AOP answers) | 0 |
| 10-01 | 26 KB | 62 | 6 (WAM connect Loop, Quest channel, SLA thread, cyber doc, VAS-WMX-WAM, WAM team chat) | 1 |
| 10-16 | 23 KB | 55 | 4 (Deployment Scrum transcript, Stand Up transcript, Ascent email, VAS-WMX agenda email) | 0 |

1. **Few sources, many rows.** Each substantive source is restated in 5 to 10 of the 14 sections. In the 10-16 package the Ascent onboarding request appears in sections 1, 3, 4, 5, 6, 9, 11 and 13; the Dell meter issues in 1, 2, 4, 8, 9, 11 and 13. The package carries about four underlying signals in 55 rows.
2. **The restatements are assessment, not evidence.** Sections 1, 2, 8, 9, 10, 11 and 13 add columns Copilot fills with its own judgment: Why It May Matter, Severity, Urgency, Risk of Waiting, Recommended Follow-Up, Suggested Leadership Action, Suggested Message Intent, Review Priority. None of this is retrieved from M365. All of it is redone on the Claude side under `CLAUDE.md` (attribution test, lane sort, register routing, Pulse severity).
3. **"None found" almost never occurs.** With 14 sections and an instruction to fill each, Copilot fills each. A section that is populated on every run from four sources is not measuring yield; it is measuring compliance.
4. **Teams coverage works when there is Teams content.** 08-27 cited four Teams chats as primary sources; 10-01 cited a Teams channel and a team chat; 10-16 found no independent qualifying Teams message in a 24-hour window and said so in the header. The prompts ask for Teams chats and channels explicitly and Copilot returns them; the gaps on record are retention expiry (08-25, nine threads) and throttling (10-19 Pulse catch-up), not wording.
5. **What Copilot does well is literal retrieval with arithmetic.** Since 09-14 the source-status statement, line ranges, the transcription flag and the probes have been reliable. The Pulse sweep prompts (10-19) already ask for extraction only (quote, speaker, source type, named owner) and produced usable packages on first run.

## Assessment

The binding constraint is the output Copilot is asked to produce, not the length of the instruction. Roughly two thirds of each daily package is commentary on a handful of statements, and the commentary competes for the same response budget as the transcripts it is commenting on. Splitting the prompt in two would double the number of runs to buy more room for the same commentary. Cutting low-yield sections (12, 13) would help at the margin. Removing the assessment layer from Copilot removes the duplication at its source, shrinks the package, and leaves the judgment where it is already being done.

## Change made (one variable)

Daily prompt v2, `02_Copilot_Intake_Prompts.md` section 2, served by the web app's Copilot prompts page from the same file. Copilot extracts statements into nine non-overlapping sections (commitments and requests; completions; decisions; problems, blockers and dependencies; product facts; statements about people; addressed to me; documents; coverage gaps), each row a quote with speaker and source type, with a rule that each statement appears exactly once. No assessment columns. Retrieval rules, portfolio scope, exclusion accounting, governed-forum label, header, validation and file output are unchanged in substance. v1 kept in section 2a.

Moved to the Claude side, with `CLAUDE.md` amended: Durable/Transient classification of product facts, Explicit/Implied/Inferred confidence on commitments, severity and urgency, lane sort, "people waiting on me", and executive communication needs.

## Not changed, and why

- Weekly prompt: different schema, lower run frequency; change it after the daily result is in.
- Splitting the daily into two passes: deferred; the dedup-across-sources argument favors one pass, and the extraction change should be measured first.
- Any wording aimed at run variance: the 09-14 finding stands; variance is handled by the acceptance gate, not the prompt.

## Acceptance test

Run v1 and v2 on the same window in separate Copilot chats, save both to `Evidence/` as `M365_Evidence_Daily_YYYY-MM-DD_v1.md` and `_v2.md`. v2 passes if it loses no source and no distinct underlying statement v1 surfaced, and Claude can produce the daily briefing and routing from v2 without needing anything v1 carried. Expected: smaller package, same or more distinct statements, more quotes per source, fewer truncations.

## Follow-on worth building in the EOS server (separate decision)

A mechanical package check on files dropped into `Evidence/`: header and source-status statement present, sections present and in order, every cited source listed in the statement, exclusion tables present and disjoint, Validation block present, each quoted source cross-checked against `Reference/Transcript_Register.md`. This is the acceptance gate the 09-14 revision said must live outside the prompt, and it is code, not AI.
