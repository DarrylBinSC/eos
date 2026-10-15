> Created 2026-08-25. **Revised the same day to v2.0** after a scope correction from Darryl; see the changelog at the end. Durable reference for estimating LLM cost on Wesco development projects. Rates are list prices retrieved on the date shown and must be re-validated before reuse.

# AI Cost Model for Development Projects

**Version:** 2.0
**Last updated:** 2026-08-25
**Applies to:** any CSS Platforms project that consumes LLM tokens during development
**First applied to:** Woolly harness development and test. See `Deliverables/entroCIM/2026-08-25_Woolly_Dev_Test_API_Cost_Estimate.md` and the workbook alongside it.

## 1. Start here: there are two different workloads, and they price differently

Most cost questions about "AI on a development project" turn out to be one of two things, and confusing them produces an answer that is wrong by a wide margin. Establish which one is being asked before doing any arithmetic. **This is the mistake v1.0 of this file made.**

**Workload A, developer assist.** Engineers using a coding assistant such as Claude Code. Cost scales with **developer headcount and active days**. Sessions are long-lived, so cache reuse is high (roughly 85% of input tokens are cache reads). Anthropic publishes enterprise benchmarks for this, so any estimate can be validated externally. Adding a developer adds cost linearly.

**Workload B, harness or agent runtime.** An LLM-powered feature calling the model while it is being built and tested, such as Woolly inside SkySpark. Cost scales with **interaction volume and context size**, not headcount. Runs are short and often cold-start, so cache reuse is much lower (assume around 60%). No published benchmark exists, so the estimate can only be validated by measuring it. Adding a developer barely moves it; enlarging the test data model moves it a lot.

A project can have both. They usually sit on different access paths and different budgets, so estimate them separately and show the split rather than a single blended number.

## 2. Access paths (Wesco), and why they are not interchangeable

**Governance rule.** Wesco AI Council and IT practices require LLM access through **API keys, not individual accounts** (Darryl, 2026-08-25). Seat-based subscription plans (Team Standard, Team Premium, Max) are individual named accounts and are out of policy. Record them in a comparison so the cost of the policy is visible, and mark them excluded rather than offering them as options.

**Technical constraint, and it overrides the governance framing.** **Woolly does not support Azure AI Foundry at this point** (Darryl, 2026-08-25). For the harness, direct Anthropic API keys are the only path that works. The API-key practice is satisfied by this, but it is not the reason for it. Darryl's "at this point" qualifier is preserved deliberately: Foundry support may arrive, and the separate budget line goes away with it.

**Claude Code does run on Foundry.** The 2026-08-25 weekly evidence records Claude models enabled for the entroCIM and Ascent teams via the `entroCIM_Ops` AD group. Both statements are true at once: two workloads, two access paths, two budgets.

**Commercial consequence.** Anthropic API spend cannot be absorbed into an existing Azure commitment the way Foundry spend can. It needs its own budget line and its own owner. Console API keys do bring their own controls: a dedicated Claude Code workspace is auto-created on first authentication, workspace spend limits are available, and per-user reporting is built in. Foundry bills to the Wesco Azure account, puts spend control in Azure budget tooling, and needs OpenTelemetry or a gateway for per-user attribution.

**Do not conflate any of this with the entroCIM product position.** `Products/entroCIM/entroCIM.md` records that entroCIM AI customers supply their own LLM API keys. That is a commercial model for a product feature, and it usefully bounds Wesco's exposure to the development and test period. This file is about Wesco's own token consumption while building. Same phrase, different subject.

## 3. List prices, retrieved 2026-08-25

Per million tokens. Source: `platform.claude.com/docs/en/about-claude/pricing`.

| Model | Input | Output | Cache write (5-min) | Cache read |
|---|---|---|---|---|
| Claude Opus 5 | $5.00 | $25.00 | $6.25 | $0.50 |
| Claude Sonnet 5 | $2.00 | $10.00 | $2.50 | $0.20 |
| Claude Sonnet 4.6 | $3.00 | $15.00 | $3.75 | $0.30 |
| Claude Haiku 4.5 | $1.00 | $5.00 | $1.25 | $0.10 |

Cache write bills at 1.25x input on a five-minute TTL and 2x on a one-hour TTL. Cache read bills at 0.10x input. The Batch API is 50% of list; it does not apply to interactive use but **is worth evaluating for an offline nightly regression suite**, where latency does not matter.

Subscription list prices on the same date, for the excluded-options comparison: Team Standard $20 per seat per month billed annually, Team Premium $100, Max from $100, Enterprise $20 per seat plus usage at API rates.

## 4. Workload B method: harness or agent runtime

Cost the **interaction**, then multiply by volume. An interaction is one user request the harness resolves, usually across several internal tool-call turns.

Total input tokens per interaction = `turns x base_context + growth x (turns x (turns - 1) / 2)`. Every turn is a separate billed request carrying the whole accumulated context, which is why cost grows faster than linearly in loop depth.

Working assumptions used for Woolly, **none of them measured at Wesco**:

| Parameter | Value | Why it matters |
|---|---|---|
| Agentic turns per interaction | 4 | Loop depth drives the quadratic term |
| Base context per request | 25K tokens | System prompt, tool and skill definitions, and the data model the harness reasons over. **The dominant unknown** |
| Tool-result growth per turn | 8K tokens | Query results accumulate and are resent |
| Total input per interaction | 148K tokens | Calculated |
| Cache read / write / fresh | 60% / 15% / 25% | Lower reuse than developer assist. Short runs, and a five-minute TTL on API keys means a test cycling every ten minutes misses every time |
| Output per interaction | 6K tokens | Across all turns, including extended thinking |

Resulting cost per interaction: **Opus 5 $0.52, Sonnet 5 $0.21, Haiku 4.5 $0.10.**

Volume is then split by traffic source, because the sources behave differently and need different controls:

| Source | Character | Control |
|---|---|---|
| Manual developer testing | Human decides each call. Self-limiting | Model choice |
| Automated regression suite | No human in the loop. Grows with the feature set | Spend limit, Haiku, mocking |

Intensity cases for this workload: **0.5x low, 1.0x expected, 3.0x high.** The high case is wider than for developer assist because automated volume and context size can both scale without anyone deciding to spend more.

## 5. Workload A method: developer assist

Cost the **developer active day**, not the calendar or working day. An active day is one on which the developer actually runs the tool. Assume 18 active days per developer per month against roughly 21 working days. This assumption moves the total more than any other input: 18 to 22 changes the estimate by 22%.

| Line | Volume per developer per active day |
|---|---|
| Total input tokens | 15M |
| of which cache read | 85% |
| of which cache write | 10% |
| of which fresh input | 5% |
| Output tokens (incl. thinking) | 250K |

Resulting cost per developer per active day: **Opus 5 $25.75, Sonnet 5 $10.30, Haiku 4.5 $5.15.** Blended on a Sonnet-primary mix (10/70/20 Opus/Sonnet/Haiku): **$10.82 per active day, $195 per month.**

**Rule of thumb:** roughly $195 per developer per month, or $290 with 50% contingency for a budget line.

Intensity cases: 0.6x low, 1.0x expected, 2.0x high.

## 6. Validation, and the asymmetry between the two workloads

**Workload A can be validated externally.** Anthropic publishes, across enterprise deployments, an average of roughly $13 per developer per active day, $150 to $250 per developer per month, and costs below $30 per active day for 90% of users. Source: `code.claude.com/docs/en/costs`. The method above produces $10.82 per active day and $195 per month, which is 17% below the published daily average and inside the monthly range. A small team on a single codebase should sit modestly below a mixed enterprise fleet, so this reconciles. If a future estimate lands outside the published range, find the reason before presenting it.

**Workload B cannot.** No published benchmark exists for an embedded agent harness, and a web search on 2026-08-25 found no public documentation of Woolly's token profile. The only validation available is measurement. **Instrumenting roughly twenty representative interactions and capturing actual token counts per turn replaces every assumption in section 4 with a measured figure.** That is half a day of work and it is the single highest-value action for any Workload B estimate. Until it is done, present a range and not a point.

Say which workload an estimate covers and what validation it has. A Workload A figure and a Workload B figure carry very different confidence and should never be presented with equal weight.

## 7. Findings worth carrying

**Model selection moves the number less than expected, in both workloads.** Opus costs 2.5x Sonnet on identical token volume, but on developer assist an Opus-heavy mix raises a project total by roughly 48%, not 250%, because cache reads dominate and cache pricing scales proportionally with the model.

**What actually drives the number.** For developer assist: active days, then context size per request, then model mix, then thinking effort, then session hygiene. For harness runtime: context size, then interaction volume, then loop depth, then model choice. In both cases the variable most often debated (model choice) sits near the bottom.

**Automated test traffic is the distinctive risk of harness workloads.** It is usually the majority of volume, it has no human deciding each call, and it grows with the feature set. Three controls, in order of value: mock the LLM response for tests exercising plumbing rather than model quality, since a mocked test costs nothing; run remaining automated traffic on Haiku unless the test judges model quality; set a workspace spend limit, which is the only control that fails safe. Set it before the suite is automated, not after.

## 8. Re-validation triggers

Re-check this file when Anthropic publishes new model versions or changes list prices; when Woolly gains Azure Foundry support or the Wesco access path changes; when instrumentation produces measured token data for either workload; when the entroCIM AI commercial position on customer-supplied keys changes, since that is what bounds Wesco exposure to dev and test; or after 60 days without review.

## Changelog

**v2.0, 2026-08-25.** Restructured after Darryl corrected the scope of the estimate this file was built for. v1.0 covered only developer assist and treated it as the whole question. Three substantive corrections: the two-workload distinction in section 1 now leads the file; the Console-versus-Foundry question, which v1.0 recorded as an open governance choice between equivalent paths, is corrected to a technical constraint (Woolly does not support Foundry, Claude Code does); and section 6 now states plainly that only one of the two workloads can be validated against published data. The v1.0 rates, the developer-assist method, and its benchmark reconciliation are unchanged and carried forward in sections 3, 5 and 6.
