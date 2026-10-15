> Imported 2026-07-14 from Darryl_Work_Context_Library_v1. EOS is master: update this file here; portable bundles are regenerated from EOS on demand.

# Master Prompt — Export Everything You Know About a Work Subject

## Purpose

Use this prompt in any work-approved LLM to create a detailed, portable Markdown context file for a product, project, program, customer, discipline, stakeholder group, or strategic topic.

Replace the bracketed fields before running it.

---

# Context

I am building a portable work-context library that can be used across multiple approved LLMs.

The subject is:

**[SUBJECT OR PROJECT NAME]**

The intended use of the resulting file is:

**[EXECUTIVE DECISION SUPPORT / PROJECT CONTINUITY / PRODUCT STRATEGY / TECHNICAL PLANNING / CUSTOMER PREPARATION / CROSS-LLM HANDOFF]**

The desired audience is:

**[DARRYL ONLY / EXECUTIVE LEADERSHIP / PRODUCT AND ENGINEERING / SALES / MIXED]**

# Task

Review all information about this subject that is legitimately available to you in the current environment, including where applicable:

- Current conversation
- Prior conversations or memory available to you
- Project instructions
- Uploaded project files
- Documents, notes, transcripts, or evidence supplied in this session
- Decisions, corrections, preferences, and lessons established through prior work

Create a **complete, portable Markdown context file** that explains what is known about the subject and how future LLMs should reason about it.

Do not merely summarize recent activity. Recover the durable knowledge, strategic framing, terminology, historical decisions, known dependencies, established preferences, unresolved questions, and lessons learned.

# Critical Rules

1. **Separate durable context from dated operating status.**
   - Durable context remains useful over time.
   - Dated status must include an `As of` date or be marked `Date unknown`.

2. **Separate facts from interpretation.** Label material statements as one of:
   - Confirmed fact
   - User-provided context
   - Prior decision
   - Established preference
   - Interpretation
   - Inference
   - Unknown or unverified

3. **Do not invent missing information.** State the gap and explain why it matters.

4. **Identify conflicts.** When sources disagree, show both positions, dates, and the recommended validation step.

5. **Preserve corrections and lessons learned.** Include framing Darryl rejected, terminology corrected, assumptions that proved misleading, communication patterns that work, and strategic insights that emerged.

6. **Distinguish current truth from historical context.** Do not present old release dates, roles, risks, pricing, architecture, or customer status as current without validation.

7. **Protect sensitive information.** Exclude credentials, secrets, unnecessary personal information, privileged material, and data that should not be transferred to the target environment.

8. **Optimize for reuse.** Write the file so a capable LLM with no prior history can use it accurately.

# Required Output Format

Return only a Markdown document using this structure:

# [SUBJECT OR PROJECT NAME] — Portable Context

**Generated:** [YYYY-MM-DD]  
**Knowledge window:** [state what sources or history were available]  
**Last known operating date:** [YYYY-MM-DD or unknown]  
**Confidence:** High / Medium / Low  
**Sensitivity:** Internal / Confidential / Other

## 1. Executive Orientation

Explain what it is, why it exists, why it matters, Darryl's role, and the primary decision lens.

## 2. Scope and Boundaries

Include in scope, out of scope, adjacent systems or teams, and ownership boundaries.

## 3. Durable Context

## 4. Historical Development and Key Decisions

| Date | Decision or Development | Owner | Rationale | Lasting Implication | Confidence |
|---|---|---|---|---|---|

## 5. Current or Last-Known State

Clearly mark the date of each material status statement.

## 6. Business Value and Benefits

Separate intended benefits, realized benefits, leading indicators, commercial impact, customer impact, operational impact, and benefits not yet demonstrated.

## 7. Product, Service, or Technical Model

## 8. Dependencies and Interfaces

| Dependency | Why It Matters | Owner or Team | Current/Last-Known State | Risk | Validation Needed |
|---|---|---|---|---|---|

## 9. Stakeholders

| Stakeholder | Role in Subject | Known Priorities | Decisions or Inputs Needed | Recommended Engagement | Confidence |
|---|---|---|---|---|---|

Do not make personal character judgments without direct evidence.

## 10. Risks, Constraints, and Failure Modes

Distinguish active risks from structural constraints and unverified concerns.

## 11. Open Decisions and Unresolved Questions

For each decision include the owner, options, information still needed, risk of waiting, forum, and date or trigger.

## 12. Established Terminology and Framing

Include preferred terms, terms to avoid, definitions, executive narrative, commercial narrative, and technical terminology.

## 13. Darryl's Established Preferences for This Subject

## 14. Lessons Learned and Corrections

## 15. What Another LLM Should Do

Include what to prioritize, what not to assume, what to validate, how to distinguish strategy from current status, and the quality standard.

## 16. Known Gaps

## 17. Recommended Source Package

## 18. Source Basis

List source names, conversation themes, or document names used. Do not fabricate citations.

# Quality Check

Before returning the file, verify:

- A new model could understand the subject without prior conversation.
- Dated status is clearly separated from durable knowledge.
- Facts and inferences are distinguishable.
- Contradictions and gaps are visible.
- The file captures strategic learning, not only activity.
- The result is detailed enough to reduce repeated explanation in future sessions.
