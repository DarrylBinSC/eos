# Reference — Durable Background Knowledge

Deep-dive context exported from ChatGPT history and other sources. One subject per file.

## Trust rule

Reference files are **dated background knowledge**. They rank below field notes and current operational evidence. When a reference file conflicts with newer evidence, the evidence wins and Claude flags the file for update. Every file must carry an "As of" date in its header.

## What belongs here

- Org history, portfolio scope evolution, past reorgs and rationale
- Managed Services operating model thinking
- AI strategy history and lessons
- Customer/account histories
- Leadership themes, preferences, recurring challenges
- Domain knowledge (asset management market, competitive landscape, etc.)

**Standards files are the exception to the trust rule above.** `Deck_Construction_Standards.md`, `Mermaid_Standards.md`, `Communication_Preferences.md` and the other standards carry Darryl's standing preferences rather than dated background. They are authoritative until Darryl changes them.

Product-specific deep dives go in `Products/` instead. Anything currently in motion belongs in living documents 03–06, not here.

## ChatGPT Export Prompt (run once per subject)

```
Based on everything you know about me and my work from our conversation history, write a durable knowledge file about: [SUBJECT].

This will be reference material for my executive advisor, so accuracy and honesty about uncertainty matter more than completeness.

Structure it as Markdown:

# [Subject]
As of: [today's date]

## Current State
What is true now, as best you know.

## History and Context
How this evolved, key turning points, why past decisions were made.

## Key People
Who matters on this subject and their roles/stakes.

## Decisions Made
Significant decisions along the way, with rough dates.

## Open Questions and Tensions
What was never resolved, recurring debates, known tradeoffs.

## Lessons and Preferences
What I've learned, what I prefer, what I've explicitly rejected.

Rules:
- Distill — do not recount conversations.
- Only include what is durable. Exclude anything that was time-sensitive when we discussed it unless it shaped a lasting decision.
- If your information about something may be outdated, say so inline: "(as of [date], may have changed)".
- If I corrected or reversed something over time, reflect the final position, not the journey.
- Be specific with names, systems, and numbers where you have them; mark uncertainty honestly.

File output:
- Create the result as a downloadable Markdown file (.md), not just a chat response.
- Name it with the subject in title case, underscores for spaces, no dates in the filename: e.g. Org_and_Portfolio_Evolution.md, Managed_Services_Model.md.
- The first line under the title must be: As of: [today's date in YYYY-MM-DD].
- Give me a download link to the .md file.
```

## Saving Export Files

1. In ChatGPT, copy the full Markdown output (or download if offered).
2. Save as a plain `.md` file directly into this `Reference/` folder — TextEdit/Notepad works; make sure the extension is `.md`, not `.txt` or `.docx`.
3. Filename: subject with underscores, no dates in the name — `Org_and_Portfolio_Evolution.md`. The "As of" date lives inside the file (first line under the title); update the same file rather than creating dated copies.
4. No further processing needed — Claude reads these on demand. Easier path: paste the export into a chat session and say "file this in Reference" — Claude will name, date, and save it correctly.

## Current Contents (imported 2026-07-14 from context library v1)

- `Managed_Services_Operating_Model.md` — phased model (IFS-first), Ascent-led framing, ownership questions, failure modes
- `AI_Strategy_and_Use_Cases.md` — WAM-oriented use cases, evaluation framework, pilot principles, dated pricing context
- `Benefits_Realization_Standards.md` — benefit structure, register fields, slide standard, reporting errors
- `Engineering_Delivery_Governance.md` — operating model, release management, escalation, vendor management, delegation standard
- `Communication_Preferences.md` — Darryl's voice, email/slide/benefit-note/Mermaid standards — **consult before drafting any deliverable**
- `Known_Gaps_and_Validation_Questions.md` — what the context does NOT cover; validation checklist for new projects
- `Tooling_Context_Extraction_Prompt.md` / `Tooling_Reconciliation_Prompts.md` — for extracting context from other LLMs and reconciling multiple exports

## Added since (not part of the 2026-07-14 import)

- `EOS_Analytics_Standard.md`, `EOS_Model_Selection_Standard.md`, `Sean_Update_Standard.md`, `Mermaid_Standards.md`, `Digital_Product_List.md`, `EOS_ChatGPT_Audit_Prompt.md`, `Engel_Executive_Voice_Guide.md` — operating standards for the EOS itself
- `AI_Development_Tooling_Cost_Model.md` (added 2026-08-25, **v2.0 same day**) — how to estimate LLM cost on any Wesco development project. **Start with section 1:** there are two workloads (developer coding assistance, and a product harness calling the model at runtime), they price completely differently, and only the first can be validated against published benchmarks. Also holds list rates, both methods, the Wesco API-key practice, and the Woolly Azure Foundry limitation. **Rates are dated and must be re-validated before reuse.** Distinct from `AI_Strategy_and_Use_Cases.md`, which is about AI inside the products; this one is about the cost of tokens consumed while building them.

- `Diagram_Register.md` (added 2026-10-15) — every Miro board used for EOS work, what it is the source of truth for, last export and sensitivity. Read before working on any diagram that may already exist in Miro

## Still-valuable future exports

1. `Org_and_Portfolio_Evolution.md` — how CSS Platforms scope grew and why (history depth beyond the library)
2. `Key_Accounts.md` — customer histories and relationship context
3. `Leadership_Themes.md` — recurring priorities, preferences, growth edges (best done carefully — sharpens coaching)
