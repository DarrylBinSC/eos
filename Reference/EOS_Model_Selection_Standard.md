# EOS Model Selection Standard

> Added 2026-07-14 at Darryl's request. Defines which Claude model to select (Cowork model picker) for each EOS function. Claude: if a session's model is mismatched to the task per this standard, say so at the start of the session. Review this file when Anthropic ships new model generations.

## Current Model Lineup (as of 2026-07)

| Model | Position | Use character |
|---|---|---|
| Haiku | Fastest, lightest usage | Mechanical, low-judgment work |
| Sonnet | Strong default, moderate usage | Structured analysis, routine synthesis, most drafting |
| Opus | High capability, heavy usage | Multi-source judgment, trend synthesis, high-stakes drafting |
| Fable | Top tier (Mythos-class), heaviest usage | Strategy, adversarial challenge, highest-stakes reasoning |

Usage economics: on a subscription plan, model choice governs how much work fits in a usage window, not a per-call bill. The cost of over-selecting is exhausting capacity before the week's high-value sessions; the cost of under-selecting is a briefing or deliverable that misses judgment calls. Bias rule: **under-select for mechanical work, over-select for anything Sean, Dirk, Engel, or a customer will see.**

## Function-to-Model Map

| EOS function | Default model | Escalate to | Escalation trigger |
|---|---|---|---|
| Field-note logging, closure answers, quick filing, "log: ..." | Haiku | Sonnet | Note requires reconciliation against living docs, not just filing |
| Daily briefing | Sonnet | Opus | Day carries a top-of-house event (exec narrative, escalation to Sean/Dirk level, customer crisis) |
| Weekly briefing | Opus | Fable | AOP season, reorg, or portfolio-strategy inflection in the week under review |
| Monthly staleness pass | Sonnet | — | — |
| Meeting prep ("prep me for X") | Sonnet | Opus | Forum carries an open decision with exec-leadership audience |
| Routine drafts (Teams nudges, internal emails, recognition notes) | Sonnet | — | — |
| Exec deliverables (Sean pre-reads, Engel/Dirk/Akash slides, reset narrative, benefits notes) | Opus | Fable | Narrative-defining artifacts: one-shot credibility events like the WAM reset |
| Sean update (on-demand, per Sean_Update_Standard) | Sonnet | Opus | Update lands in a charged context (post-Engel/Hasting signal, AOP asks) |
| Strategy / thought-partner sessions (org design, portfolio strategy, AOP, "challenge me") | Fable | — | — |
| Decision memos | Opus | Fable | Irreversible or org-structure decisions |
| Diagrams, spreadsheet builds, Pandoc/format mechanics | Sonnet | — | Content already decided; work is construction |
| Retrospectives / quarterly EOS review (per Analytics standard) | Opus | — | — |

## Selection Heuristics

1. **Judgment density, not document length**, drives model choice. A two-line reply to Sean can warrant Opus; a ten-page mechanical conversion needs only Sonnet.
2. **One-shot audiences get the strongest model.** Anything read by Engel, Hasting, Dirk, Akash, or an at-risk customer is a credibility event, not a document.
3. **Separate thinking from building.** Set strategy/narrative in an Opus or Fable session; execute the deck/doc mechanics in a Sonnet session against the decided content.
4. **Fable is for being challenged, not for being served.** Its marginal value is highest where Darryl wants assumptions attacked: org structure, portfolio bets, AOP positioning, "what am I missing."
5. **When mixed work lands in one session,** pick the model for the highest-judgment task in it.
