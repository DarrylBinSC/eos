# EOS Analytics Standard

> Added 2026-07-14. Defines the recurring analyses Claude runs over the data the EOS accumulates (briefings, decision log, watch list, commitments, cadence, field notes). Purpose: turn accumulated records into trend signal about Darryl's leadership effectiveness, not more activity reporting. Lean by design; cut any metric that doesn't change a decision within two review cycles.

## Weekly Analytics Block (appended to every weekly briefing)

1. **Decision velocity** — decisions made this week vs. new approaching vs. total open; age of the three oldest open decisions; "sessions since last decision" for each Darryl-owned forum (WAM Data Challenges is the standing test case).
2. **Commitment load and aging** — open commitments by direction (Darryl owes / owed to Darryl), count taken vs. closed this week, oldest three. Flag any week Darryl absorbs more commitments than he closes (the 07-14 six-in-a-day pattern).
3. **Watch-list trend** — items ↑ / ↓ / flat vs. prior week; evidence-basis mix (what share of High items rests on Direct evidence vs. Inferred); **silence flags**: High items with zero evidence for 3+ days, named explicitly (silence is not resolution).
4. **Recurring-theme detection** — topics appearing in 3+ briefings without an associated decision-log entry. These are the "discussed repeatedly, decided never" candidates; each gets a proposed owner and forum.
5. **Time-at-role check** — By-exception forums attended, and any delegation opportunity that has now appeared in 3+ briefings (the system's signal that the delegation isn't happening).
6. **Impact capture** — wins added to `09_Impact_Ledger.md` this week. A week with zero entries triggers the question: nothing won, or nothing recorded?

## Monthly Pass (with first weekly briefing of the month, alongside the staleness pass)

- Decision-log hygiene: stalled items 30+ days old get a forced disposition proposal (decide, delegate, or consciously park with a revisit date).
- Watch-list calibration: items High for 30+ days without materializing get evidence re-graded; risk inflation is a failure mode too.
- Commitment balance trend across the month: is Darryl's open-commitment count trending toward or away from role level?
- Sean-visibility audit: anything material that never appeared in a Sean update.

## Quarterly EOS Retrospective (on request, Opus session)

- Which briefing sections Darryl actually reads and acts on; cut or shrink the rest.
- Prediction check: did flagged risks materialize? Did "quiet growth" items grow? Recalibrate.
- Prompt/output-contract tuning for the Copilot intake package.
- Standards drift: do this file, the Model Selection Standard, and the Sean Update Standard still match how the system is actually used?

## Principles

- Trends over snapshots: a metric only earns its place by moving and by someone acting when it moves.
- Counts are inputs, judgment is output: the analytics block ends with at most two sentences of interpretation, not a dashboard dump.
- Evidence discipline applies to analytics: mention-frequency is not severity, and metric deterioration is a prompt to investigate, not a conclusion.
