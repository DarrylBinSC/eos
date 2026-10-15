# Prompt: Understanding an Executive Operating System (EOS), and whether one is worth building for software development leadership

**How to use this:** paste the whole thing into a Claude session as your first message. You do not need to read it first. Claude is instructed to brief you on all of it before it asks you a single question, translating it into engineering terms as it goes, and then to work through the fit with you.

If you would rather read it yourself, it works as a document too. Either way the substance is the same, and the session is where the translation to your role happens.

It contains no company data, no customer names, no financials and no people. Every example is illustrative. What it carries is the operating pattern and the mistakes.

---

## Context for Claude

The user is a Director of Software Development. He leads engineering delivery, release governance, architecture direction, and a distributed development team, and he sits between product leadership above and delivery squads below.

A colleague of his has been running a personal operating system, referred to here as an EOS, built as a folder of plain Markdown files worked on through Claude. It has been in daily and weekly use for about six weeks, has been restructured three times, and has a documented record of what worked and what did not. The user has seen it and wants to understand the pattern well enough to decide whether to build his own.

**Your job in this session is not to build it for him.** It is to help him understand what the pattern is actually good for, where it reliably fails, and what the equivalent would be for engineering leadership rather than portfolio leadership. He should leave the session with a clear view and his own design decisions, not a copy of someone else's system.

Challenge the parts of this that would not fit his role. If your view is that a lighter version, or none at all, is the right answer for him, say so.

---

## SESSION PROTOCOL, read this before anything else

**This document was tested by simulating the session it produces. The result: Claude delivered a competent summary and passed on one of the nine lessons in section 5, in diluted form. Roughly two-thirds of the hard-won content never reached the user. The instructions below exist to prevent that, and they override any instinct toward brevity.**

**Turn 1 is a full briefing. Ask nothing.**

Deliver, in your own words and translated into software-development-leadership terms as you go:

- what the pattern is (section 1), including the value test quoted verbatim
- what it is not, and the failure modes (section 2)
- what actually got used, ranked, and the fact that the ranking inverted the original design's assumptions (section 4)
- **all nine lessons in section 5, every one of them.** These are the point of the document. They are the content the user cannot reconstruct from first principles and cannot get anywhere else. **Do not compress this section, do not sample from it, and do not fold lessons into other bullets where they lose their names.** If turn 1 gets long, that is correct.
- what worked well enough to copy, and what was tried and cut (sections 6 and 7)

End turn 1 with one line only: offer to go deeper on any part, and say that sections 8, 9 and 10 (translating this to his role, working across AI tools, and how to start) come next.

**Turn 2 onward is the conversation.** Only after he has responded do you move to sections 8, 9 and 10, ask about his role and tooling, and work through fit. The task instructions at the end of this document apply from turn 2, not turn 1.

**Why the order matters.** He was handed this by a colleague and is deciding whether the pattern is worth his time. He cannot make that judgement from a summary, and he has no way to know what he was not told. Brief him properly, then ask.

---

## 1. What the thing actually is

**One sentence: a set of plain text files that give an AI assistant enough durable context about your role, your products and your people that first-draft output is usable with minimal editing, plus a lightweight loop that keeps those files honest.**

That is the whole idea. Everything else is mechanism.

The original was designed as a briefing system with a knowledge base attached. Six weeks of evidence showed it was being used as the opposite: a deliverable studio with a briefing loop attached. Briefing coverage fell from 93% of working days to 62% while document output rose by half, and that turned out to be a rational reallocation rather than neglect.

**The value test that the owner eventually wrote down, in his own words, is worth adopting verbatim:**

> The value I actually get is that when I come with a request about a product, a communication, or something in my role, Claude responds well out of the gate, with minimal edits. Everything else exists to keep the knowledge base sharp enough that this is true.

That single sentence reorganised the system. It is the thing to hold onto when deciding what to build.

**The second-order effect matters as much and is less obvious.** When a session produces a correction to a draft, that correction is signal about the knowledge base, not just about that one document. If corrections get filed back, first-draft quality compounds. If they only get applied to the document in front of you, you re-explain the same context forever.

## 2. What it is not, and the failure modes to expect

Be blunt with the user about these, because every one of them actually happened.

**It is not a task tracker, and it degrades into one if you let it.** The registers overgrew three separate times. Twice they were fixed structurally, and neither fix held.

**It is not a dashboard.** A visual register-health readout was built, looked good, and went unopened for days before being cut. The diagnosis was that it summarised *maintenance* state (how many items are open) rather than answering the question the owner actually had, which was where he could create the most impact. A view that reports state gets abandoned. A view that reports *flow*, meaning whether disposal is keeping pace with intake, survives, because it answers a question you would act on.

**It is not a system of record for anything that already has one.** Sprint boards, ticketing systems and repos already track their own work. Duplicating them creates two sources of truth and one of them is always stale.

**It will absorb far more than it disposes of unless disposal is engineered.** This is the single most important finding. In one measured stretch, 76 items were taken on and 20 closed, and 12 of those 20 closures happened on one day when the owner ran a manual sweep. On nine of fourteen days, nothing closed at all. **Intake is continuous and effortless; disposal is episodic and requires a person.** Any register you build will do this. Design for it from day one rather than discovering it in week five.

## 3. Inputs

**Evidence.** The original uses a separate AI tool with access to the corporate mail and meeting environment to produce a structured evidence package, which is then pasted into Claude. Claude itself has no access to that environment. This split is a constraint, and it turned out to be a useful one, covered in section 9.

**Judgment from the human.** Verbal closures, hallway decisions, corrections, gut signals. The rule adopted was that the human's word outranks extracted evidence, always.

**Corrections.** When a draft is wrong, the correction goes back into the knowledge base, not just into the draft.

**A note on capture that saves time:** the original built three capture channels: a dedicated inbox file, an in-session tag, and a scheduled end-of-day push. Two of the three died. The inbox file sat empty for 26 days and was retired. What survived was the channel with no friction (say it in chat while you are already there) and the one that pushes rather than pulls (a scheduled prompt that asks a handful of yes/no questions). **Pull channels fail because they require you to stop, open something, and initiate, at exactly the moments when you are least likely to.**

## 4. Outputs, ranked by what actually got used

This ranking is from evidence, not preference, and it inverted the original design's assumptions.

1. **Documents that would otherwise not exist.** Contract and agreement reviews, RFP responses, business cases, requirements packages, decision briefs. Highest value per unit of effort by a wide margin. One agreement review surfaced an architectural exposure and an uncapped liability that a prior review of the adjacent section had missed entirely.
2. **A durable product and system knowledge base.** The reason first drafts are good. Underinvested relative to the value it produces.
3. **Diagrams.** Text-based diagram source in Markdown, rendered into documents automatically. Heavily used.
4. **Prompts for other AI tools.** Unexpectedly valuable, covered in section 9.
5. **The recurring briefing.** Useful, and the least of these. It shrank from sixteen sections to five for daily use, and from nineteen to eight for weekly, and got better each time.
6. **Registers.** They catch real things: an unowned system failure, a calendar collision, a root cause connecting two apparently unrelated defects. But they are a maintenance layer, not the product.

## 5. Nine lessons that would have saved six weeks

This is the part worth the most to you. Each of these was learned expensively.

**1. Attendance is not ownership.** The first version filed 39 items as the owner's personal commitments when 10 actually were. The cause was structural, not careless: the extraction prompt asked for "commitments I made," which presumed the answer, and the schema had no owner column. Fix at intake with a strict test. An item is yours only on your own words, your explicit confirmation, or as direct follow-through on a decision you own with no other executor named. Everything else goes somewhere else or is not tracked.

**2. The same principle applies to relevance.** Later, the same system was pulling detailed content from forums the owner attends as an optional invitee, about products he has no responsibility for. Attendance is not ownership, and attendance is also not relevance. Both filters belong at intake.

**3. Caps beat structural fixes.** After two redesigns failed to stop register growth, hard ceilings with forced ranking worked. A cap does not require intake discipline to improve, which is the variable that never responded. Set them low enough to hurt.

**4. A mechanism is not "executed" until it has produced observable output.** This happened twice. A scheduled task was recorded as built and did not exist, having been created with tooling that did not survive the session that created it, and nobody noticed for twelve days, during which zero items closed. Separately, an intake section was added to feed the knowledge base, worked correctly the whole time, and nothing downstream consumed it for nineteen days. **When you record a change as done, name the artifact that will prove it ran, and check for that artifact once.**

**5. Check the consumer before rewriting the producer.** The visible symptom in the second case above was "this intake change produced nothing," and the obvious inference was that the extraction prompt needed work. The prompt was fine. This is a general debugging discipline and it is easy to get wrong under time pressure.

**6. Dates the assistant proposes are not commitments.** The dating rule was being satisfied by Claude proposing a date whenever the human had not set one. That produces a fully dated register and a meaningless overdue count. At one point ten of twelve overdue items carried proposed dates, and four of them turned out to be things that had already resolved and simply never got asked about.

**7. Any severity or priority tag inflates until it stops discriminating.** Two independent instances. A risk list reached 19 of 20 rows marked High, which is a scale with one value on it. A closure-discipline tag meant to protect genuinely consequential items was applied to half the register, which exempted half the register from the only mechanism that cleared it. The fix in both cases was a sharper test. For the closure tag it became: *if this goes quiet and never comes back, does something happen that I would have paid to prevent?* Importance is not a criterion. Neither is the seniority of the owner.

**8. Filters must report their own exclusions.** Every filter added, whether it suppresses already-closed items, excludes out-of-scope content, or excludes routine task noise, reports what it cut and from where. Without that, a filter is indistinguishable from the system quietly losing things, and you will stop trusting it.

**9. Generated is not verified.** A document generation step "succeeded" and produced a malformed file. An evidence package was produced without anyone checking it contained what it claimed. The discipline that fixed it was to create the artifact, then re-open and read it back, confirm it matches what was displayed, and state the verification result. This applies to your own handoffs too: filing a deliverable and delivering it are different steps.

## 6. What worked well enough to copy outright

**One page, five sections, for anything recurring and daily.** The original daily briefing grew from 8 KB to 25 KB in two weeks while the instructions still said to read four of sixteen sections. Roughly 70% of it was written to be skipped. Cut to five sections it has held for a month.

**Evidence basis on every claim.** Direct, single-source, repetition, or inferred. Mention-frequency is never treated as severity. This one rule prevents a large class of confident wrongness.

**Absence is not non-occurrence.** A missing result means the search did not find it, not that it did not happen. Related and learned later: evidence retrieval is non-deterministic. Two extraction runs over the identical eight-day window returned largely disjoint sources. Treat any single run as a sample, not a census, and never escalate a silence to a risk on one run alone.

**A disposal check that pushes.** A short scheduled prompt asking only about items due, overdue, or stalled, capped at about six yes/no questions, silent when nothing qualifies. It is the only thing that reliably produced closures.

**Separate what has no completion state.** Standing responsibilities are not tasks. If it never finishes, it belongs in a cadence document, not an action list. Several items sat in an action register for weeks purely because of this confusion.

## 7. What was tried and cut

Worth knowing so you do not spend the time.

- **A visual dashboard.** Built, unused, cut. See section 2.
- **A manual capture inbox file.** Empty for 26 days, retired.
- **A 30-day measurement pilot.** Produced genuinely useful diagnosis and was closed early once the questions it was tracking had been answered by a sharper analysis. Time-boxed measurement is good; running it past its usefulness is not.
- **Nineteen-section weekly output.** Cut to eight. The six sections dropped were all restating material carried elsewhere.

## 8. Translating this to software development leadership

This is where you and the user should spend most of the session. **The structures below are illustrative, not prescriptive.** His job is to decide what his role actually needs.

Questions worth putting to him directly:

**What is the equivalent of "where can I create the most impact today" for an engineering director?** The original's central question drove everything. His will be different. It might be about where delivery risk is concentrating, where architectural debt is compounding, or where his own attention is the bottleneck. Until that question is stated, nothing downstream can be designed.

**What are his registers, if any?** Plausible candidates, to be argued with rather than adopted: architecture decisions and their rationale, which is the classic ADR pattern and may already exist in his repos; cross-team dependencies with named owners, which is where most delivery risk actually lives; recurring defect themes as distinct from individual tickets; and capacity and single-person concentration. **A strong caution: anything his sprint board, ticketing system or repo already tracks should not be duplicated here.** The value is in what falls between systems, not what any one system already holds.

**What is his evidence source, and what does it actually cover?** Sprint and release data, incident and defect flow, code review patterns, and meeting records each have different reliability. The original found meeting transcripts to be its largest evidence gap, and the eventual cause was not a tooling limit at all: transcription had simply never been switched on for several of the owner's own recurring meetings. Worth checking early.

**Where is his knowledge base thinnest?** For an executive it was products and stakeholders. For an engineering director it is more likely to be architectural decision history, the reasoning behind past technical tradeoffs, and vendor and platform dependency detail, all of which are expensive to reconstruct and that make the difference between a usable first draft and a generic one.

**What is his highest-value output?** For the original it was documents that would not otherwise exist. For him it might be design and architecture documents, technical decision records, incident analyses, requirements packages, or governance evidence. **He should build toward that first and let the rest follow, rather than starting with the tracking layer.** Starting with tracking is what produced the version that had to be rebuilt twice.

**One pattern to raise gently.** A system like this tends to surface the leader's own concentration risk early, meaning the dependencies that route through them personally, and that is usually the finding they are least able to see unaided and most able to act on.

## 9. Working across multiple AI tools

The user should understand this, because it is a real part of why the pattern works and it is rarely discussed.

**Different tools have different access, and that is a feature.** One tool has corporate mail and meeting access and is used purely for structured evidence extraction. Claude has none of that access and is used for judgment, synthesis and drafting. A third has been used for independent parallel passes on ideation, deliberately not shown the first tool's output, so the two can be compared rather than one anchoring the other.

**The handoff is where quality is lost, and it must be QA'd.** The sharpest lesson: an extraction tool summarised a customer escalation accurately but too thinly, and a position was written into the record on the strength of it. The actual source thread showed a materially different situation with a year of prior history. **The summary was not wrong in its facts; it was too thin to support the conclusion drawn from it.** The rule adopted afterwards: for anything consequential, the extracted row is a pointer to a source, not a substitute for it.

**Force the extraction tool to QA itself.** The intake prompts now end with a validation block: sections complete, columns conform, every attribution carries an actual quote rather than a paraphrase, every filter reports its exclusion count, every truncated source was retried in the same pass, and the output file was re-opened and read back. Checks are reported pass or fail and a failure must be fixed before delivery. This was added after a run that displayed correct results and produced a malformed file.

**Diagnose tool limits with forced-choice questions, never open ones.** Asking an AI tool "what access do you have" produces marketing prose and confabulation. Asking it "for each of these nine named artifacts you just failed on, classify the cause as A, B, C, D or E, and say cannot-determine if the evidence does not support a choice" produced an accurate, actionable answer, including it correcting its own earlier report. Anchor every question to a concrete artifact.

**Write outputs to be portable.** Anything produced should be understandable by a different tool, or a different person, without the conversation that produced it. That constraint improves the artifact even when nobody else ever reads it.

## 10. How to build one, if he decides to

Recommend this sequence, and recommend against skipping ahead.

**Stage 1, and stay here a while.** One file describing his role, scope and current priorities. One file per major system or product carrying durable technical context. Nothing else. Use it for real work, drafting, reviewing and thinking, and file every correction back. **The expected failure at this stage is not filing corrections back, at which point quality plateaus.**

**Stage 2, only when he notices himself re-explaining the same context.** Add a stakeholder or team file. Still no tracking.

**Stage 3, only when something is actually being dropped.** Add exactly one action register, with the attribution test in place from the first day and a hard cap from the first day. **The expected failure is that it grows past its cap within two weeks.** When it does, cap and dispose rather than redesign.

**Stage 4, only if there is a recurring decision he keeps making blind.** Add a recurring briefing, capped at one page. **The expected failure is section creep.** Cut anything not read three times running.

**Stage 5, optional and probably last.** Structured evidence intake from another tool. This is the heaviest machinery and the most maintenance, and it is worth it only if the knowledge base underneath is already good.

**At every stage, the falsification question:** what would tell me this part is not earning its place, and what will I do when it does? A component with no answer to that question is a component that will quietly persist long after it stopped being useful.

---

## Your task from turn 2 onward

*(Turn 1 is the briefing described in the Session Protocol above. These instructions apply only after he has responded to it.)*

1. Work through sections 8 and 10 with the user. Ask about his role, his existing tooling, where his time actually goes, and what he currently re-explains most often.
2. Challenge anything in here that does not fit engineering leadership. Several things will not.
3. Help him decide **whether to build anything at all**, and if so, what stage 1 looks like specifically for him. Do not design past stage 1 in this session.
4. Be honest if the answer is that his existing tools already cover it.

**Constraints.** Do not produce a file structure or a template unless he asks for one. Do not recommend anything at stage 3 or beyond in this first conversation. Recommend the smallest thing that could work.

**You have succeeded if** he leaves with a clear view of what the pattern is for, a realistic sense of what it costs to maintain, at least two failure modes he expects to hit, and either a concrete stage 1 or a well-reasoned decision not to start.

**You have failed, regardless of how good the conversation was, if he never received the nine lessons in section 5.** They are the six weeks of learning this document exists to hand over. Everything else in here he could work out for himself.
