> **SUPERSEDED 2026-08-25, same day, by `2026-08-25_Woolly_Dev_Test_API_Cost_Estimate.md`.**
>
> **This memo priced the wrong workload.** It modelled Wesco developers using Claude Code as a coding assistant. Darryl corrected the scope the same day: the Anthropic API keys are for the **Woolly AI harness built into SkySpark** making LLM calls during development and test, which is a different consumption profile driven by interaction volume and context size rather than by developer headcount.
>
> **It also framed the Foundry question wrongly.** This memo recorded Anthropic Console versus Azure AI Foundry as an open governance choice between two equivalent paths. It is not a choice: **Woolly does not support Azure AI Foundry at this point** (Darryl, 2026-08-25), so direct Anthropic API keys are technically required. Claude Code does run on Foundry, which is why both statements in the evidence are true at once.
>
> **What survives and is still correct:** the list prices, the cache multipliers, the Claude Code developer cost model and its reconciliation to Anthropic's published benchmarks (roughly $195 per developer per month, 17% below the published average), and the finding that model selection moves a total far less than the utilization assumption does. That component now lives on its own tab of the replacement workbook, billing to Azure Foundry rather than to the Anthropic keys.
>
> Retained unedited below for the decision trail. Do not quote figures from it as the API key budget.

# entroCIM Development Project: Claude Code API Cost Estimate

**Date:** 2026-08-25
**Prepared for:** Darryl Benson
**Basis:** Anthropic list prices retrieved 2026-08-25; Wesco access-path constraint stated by Darryl the same day
**Workbook:** `SUPERSEDED_2026-08-25_entroCIM_Claude_Code_API_Cost_Estimate.xlsx` (this folder, also superseded)
**Method:** `Reference/AI_Development_Tooling_Cost_Model.md`

## Recommendation

Budget **$8,760** for Claude Code API consumption across the entroCIM development project, on the basis of 5 developers over 6 months. That is roughly **$292 per developer per month**. The figure is the central estimate of $5,840 plus 50% contingency.

Set a Console workspace spend limit at **$1,460 per month**, one sixth of the budget line. This caps exposure without blocking developers, and Claude Code auto-creates a dedicated workspace on first Console authentication, which is where the limit belongs.

Treat this as a planning estimate, not a measured one. See "What would make this defensible" below.

## Current state

Claude Code enablement for Digital Products is an active workstream. AD-group identification is tracked as A28 (Alpee, John Erickson, proposed 2026-08-24), rollout documentation is owed by Nidhishree Sanam (C18), and WAB approval for Claude code remains open on the Decision Radar (Prasada, Maddy). Separately, the 2026-08-25 weekly evidence records Claude models enabled for the entroCIM and Ascent teams through Azure AI Foundry via the `entroCIM_Ops` AD group, with one user confirmed working.

No cost estimate existed for any of it. This memo supplies one.

## Material change

**Wesco AI Council and IT practices require Claude Code access through API keys rather than individual accounts** (Darryl, 2026-08-25). This is a governance decision made outside this analysis, and it changes the commercial conclusion rather than the token estimate.

It removes the cheaper option. Team Premium seats would cost $3,000 for 5 developers over 6 months, roughly $2,840 less than the central API estimate, and would convert a variable cost into a fixed one. Seats are individual named accounts, so they are out of policy. The cost of the practice is therefore real and should be stated rather than hidden; it is not large in absolute terms and is defensible on governance grounds.

It also removes a real operational risk. Seat allowances reset on rolling five-hour and weekly windows, and a developer who exhausts one stops working until reset. API keys carry no such ceiling, which matters on a dated release path.

## Estimate

Cost per developer per active day, identical token volume applied to each model, at 2026-08-25 list prices:

| Model | $ per developer per active day | 6-month project if used exclusively |
|---|---|---|
| Claude Opus 5 | $25.75 | $13,905 |
| Claude Sonnet 5 | $10.30 | $5,562 |
| Claude Haiku 4.5 | $5.15 | $2,781 |

Project totals by model mix, at expected usage intensity, over 540 developer active days (5 developers x 6 months x 18 active days):

| Mix | Blended $ per dev per active day | Low | Expected | High |
|---|---|---|---|---|
| Sonnet-primary (10/70/20) | $10.82 | $3,504 | **$5,840** | $11,680 |
| Opus-heavy (40/50/10) | $15.97 | $5,173 | $8,621 | $17,242 |
| Cost-optimized (5/55/40) | $9.01 | $2,920 | $4,867 | $9,734 |

Full modelled range across all mixes and intensities: $2,920 to $17,242.

## Assessment

**The estimate reconciles to published enterprise experience.** Anthropic reports roughly $13 per developer per active day and $150 to $250 per developer per month across enterprise deployments, with 90% of users below $30 per active day. The model produces $10.82 per active day and $195 per month, which is 17% below the published daily average and inside the published monthly range. A five-person team on a single codebase should sit modestly below a mixed enterprise fleet, so the variance is in the expected direction. A bottom-up token model that did not reconcile would not be worth presenting.

**Model selection matters less than expected, and utilization matters more.** Opus costs 2.5x Sonnet on identical token volume, but an Opus-heavy mix raises the project total by only 48%, because cache reads dominate the input line and cache pricing scales with the model. By contrast, changing the utilization assumption from 18 to 22 active days per developer per month moves the total by 22% on its own. The utilization assumption is also the one most likely to be wrong, because it is the only input not anchored to a published figure.

**The absolute numbers are small relative to the decision they support.** At roughly $5,800 expected, or $8,760 with contingency, this is not a line item that will decide the entroCIM development plan. The value of the estimate is that it makes the exposure inspectable and gives a basis for a spend limit, not that it identifies savings worth pursuing. The corollary is that heavy optimization effort here is not warranted; setting a model policy and a spend limit is.

## Risk

**The token volumes are calibrated, not measured.** They are set so the blended result reconciles to Anthropic's published average, which is a reasonable basis for planning and an insufficient one for a committed budget. If Wesco's usage pattern differs materially, the whole estimate shifts with it. This is the largest uncertainty in the memo.

**Scope is narrower than the likely reality.** CI/CD and automation usage, agent teams (roughly 7x tokens when teammates run in plan mode), and non-developer users are not in the model. Automation in particular can exceed interactive developer usage.

**Variable cost is now uncapped by default.** With seats excluded, nothing limits spend unless a workspace limit is set deliberately. The High case of $17,242 is not a forecast; it is what happens with no model policy and no context discipline, and it is three times the central estimate.

## Open decision

**Which API-key path is the standard, and which budget carries the spend.** Darryl's direction is Anthropic Console API keys. The 2026-08-25 evidence shows Azure AI Foundry enablement for entroCIM and Ascent. Both satisfy the practice, so this is a reconciliation rather than a contradiction, but they are not equivalent: Console bills direct to Anthropic with workspace spend limits and per-user reporting built in, while Foundry bills to the Wesco Azure account, puts spend control in Azure budget tooling, and needs OpenTelemetry or a gateway for per-user attribution. The spend-control mechanism recommended above assumes Console. Confirm before committing the budget line.

Owner: Darryl, with IT and the AI Council. Route through the existing Claude Code Enablement thread rather than opening a separate one.

## What would make this defensible

Run a two-week pilot with two developers on the actual entroCIM codebase and read per-user spend from the Console usage page. That converts every assumption in the model into a Wesco-specific figure and is Anthropic's own recommended approach. Nothing else available would improve the estimate as much.

Alongside it, document the model policy (Sonnet default, Haiku for subagents, Opus by exception). It is the single largest controllable variance and it costs nothing to set.

## Reuse

The method, rates, and calibration are recorded in `Reference/AI_Development_Tooling_Cost_Model.md` so the next estimate does not start from a blank page. Two commitments already need it: **A25** carries an AI token-usage and cost estimate for Connected Device Assurance, and the entroCIM AI (Woolly) one-pager requires a cost and revenue estimate for the AI Tech Review gate. Use the same model for both rather than building parallel approaches, so the figures presented across the portfolio are consistent and traceable to one source.

Note that the Woolly cost question is a different question from this one. This memo prices Wesco developers using a coding assistant internally. Woolly prices an embedded product capability where, per the position recorded in `Products/entroCIM/entroCIM.md`, the customer supplies their own LLM API keys. The rates table is shared; the cost incidence is not.

## Sources

- Anthropic list prices: `platform.claude.com/docs/en/about-claude/pricing`, retrieved 2026-08-25
- Enterprise cost benchmarks and cost-reduction guidance: `code.claude.com/docs/en/costs`, retrieved 2026-08-25
- Subscription plan prices: `claude.com/pricing`, retrieved 2026-08-25
- Access-path constraint: Darryl, session 2026-08-25
- Foundry enablement evidence: `Evidence/M365_Evidence_Weekly_2026-08-25_run2.md`
