# Woolly Development and Test: Anthropic API Key Cost Estimate

**Date:** 2026-08-25
**Prepared for:** Darryl Benson
**Supersedes:** `SUPERSEDED_2026-08-25_Claude_Code_API_Cost_Estimate.md` (same day, wrong workload)
**Workbook:** `2026-08-25_Woolly_Dev_Test_API_Cost_Estimate.xlsx` (this folder)
**Method:** `Reference/AI_Development_Tooling_Cost_Model.md`

## Recommendation

Budget **$6,050** in Anthropic API consumption for six months of Woolly development and test. That is the expected case of roughly $4,030 plus 50% contingency.

Set an Anthropic Console workspace spend limit at **$1,000 per month**, and set it before the regression suite is automated rather than after.

**Present this figure with its range, not as a point.** The modelled range is $2,015 to $12,090, a sixfold spread. That spread is the honest state of the estimate, not a hedge around a confident number. See "Why confidence is low" below.

## What this prices, and what it does not

The Anthropic API keys fund **the Woolly harness itself making LLM calls while it is being developed and tested.** Cost is driven by how many interactions the harness handles and how much site-model context each one carries. Developer headcount barely affects it. Enlarging the test site model affects it a great deal.

This is a correction. The first version of this estimate priced Wesco developers using Claude Code as a coding assistant, at roughly $195 per developer per month. That model is sound and reconciles to Anthropic's published enterprise benchmarks, but it answers a different question. It now sits on its own tab of the workbook and bills to Azure Foundry, not to these keys.

Production and customer usage is out of scope by design. Per the entroCIM AI commercial position already recorded in `Products/entroCIM/entroCIM.md`, customers supply their own LLM API keys. Wesco's exposure is therefore bounded to development and test. If that commercial position changes, this model does not cover the consequence, and the consequence would be large.

## The access path is a technical constraint, not a governance preference

**Woolly does not support Azure AI Foundry at this point** (Darryl, 2026-08-25). Direct Anthropic API keys are the only path that works for the harness. The Wesco AI Council and IT practice of API keys rather than individual accounts is satisfied by this, but it is not the reason for it.

The earlier record framed Console versus Foundry as an open reconciliation between two equivalent options. That was wrong and has been corrected in `03_Decision_Log.md`. Both facts in the evidence are true simultaneously: Claude Code runs on Foundry, which is what the 2026-08-25 enablement of the `entroCIM_Ops` AD group reflects, and Woolly cannot. Two workloads, two access paths, two budgets.

The commercial consequence is that this spend cannot be absorbed into an existing Azure commitment the way Claude Code cost can. It needs its own budget line and its own owner.

Darryl's qualifier "at this point" is preserved deliberately throughout the record. Foundry support may arrive, and if it does this constraint and the separate budget line both go away.

## Estimate

Cost of one Woolly interaction, at 2026-08-25 list prices, on the modelled profile (4 agentic turns, 148K total input tokens, 6K output tokens, 60/15/25 cache read/write/fresh split):

| Model | $ per interaction |
|---|---|
| Claude Opus 5 | $0.523 |
| Claude Sonnet 5 | $0.207 |
| Claude Haiku 4.5 | $0.104 |

Project totals over 108 active development days, as configured (Sonnet for manual testing, Haiku for the automated suite):

| Traffic source | Interactions per day | Over the project | Model | Cost | Share |
|---|---|---|---|---|---|
| Manual developer testing | 80 | 8,640 | Sonnet 5 | $1,791 | 44% |
| Automated regression suite | 200 | 21,600 | Haiku 4.5 | $2,238 | 56% |
| **Total** | **280** | **30,240** | | **$4,029** | |

By intensity: Low (0.5x) $2,015, Expected $4,029, High (3.0x) $12,087.

Running everything on Sonnet instead would cost $6,268; everything on Haiku, $3,134.

## Assessment

**The automated suite is the risk line, not the developers.** It is 56% of interaction volume and it runs without a human deciding each call. A suite that grows with the feature set, or that gets left on a nightly schedule against a paid endpoint, produces spend nobody notices until the invoice arrives. This is the specific failure mode of a harness workload and it has no equivalent in developer tooling, where every call follows a human keystroke.

**Three controls address it, in order of value.** Mock the LLM response for any test exercising Woolly's plumbing rather than the model's answer: tests of Axon query construction, tool dispatch, error handling and response parsing do not need a real completion, and a mocked test costs nothing. Point the remaining automated traffic at Haiku unless the test is specifically judging model quality. Set the workspace spend limit, which is the only control that fails safe.

**Context size is the dominant unknown, not model choice.** The model assumes 25K tokens of base context per request covering the system prompt, tool definitions, and the site model Woolly reasons over. A real site model with a full Haystack point list could plausibly be four times that. If it is, the estimate roughly triples on that input alone. This is why the High case is set at 3x rather than the 2x used for developer tooling, and why the range matters more than the point estimate.

**The absolute number is small relative to the decision it supports.** At $4,000 to $6,000 over six months, this will not decide whether Woolly proceeds. The value of the estimate is that it makes the exposure inspectable, gives a defensible figure for the AI Tech Review one-pager, and identifies the runaway risk before the suite is automated. Heavy optimization effort is not warranted; the three controls above are.

## Why confidence is low, and what would fix it

The Claude Code component could be validated. Anthropic publishes enterprise benchmarks and the model lands 17% below the average per active day, inside the published monthly range, in the expected direction for a small team on one codebase.

**The Woolly component cannot be validated the same way.** No published benchmark exists for an embedded agent harness, and a web search on 2026-08-25 returned no public documentation of Woolly's token profile. Every figure in the interaction profile, the turn count, the base context size, the tool-result growth, the cache split and the output volume, is a reasoned assumption with no Wesco measurement behind it. So is the test volume.

**One action fixes this.** Instrument roughly twenty representative Woolly interactions on the dev server and capture actual token counts per turn. That replaces every assumption in the model with a measured figure and would reveal within an afternoon whether the base-context estimate is off by a factor of four in either direction. Ron Snyder owns the evaluation environment. This is half a day of work, not a project, and nothing else available would improve the estimate as much.

Until it is done, quote the range.

## Total AI cost of the project, for the portfolio view

| Workload | Access path | Expected | With contingency |
|---|---|---|---|
| Woolly harness runtime (dev and test) | Anthropic API keys | $4,029 | $6,044 |
| Claude Code developer assist | Azure AI Foundry | $5,840 | $8,760 |
| **Total** | | **$9,869** | **$14,804** |

These are two budgets, not one approval ask. The Claude Code line is real cost but behaves like ordinary per-seat tooling inside an existing Azure envelope and does not need this estimate to be managed. The Woolly line is the one needing an owner, a limit, and a decision on which budget carries it.

## Next actions

| Action | Owner | Why |
|---|---|---|
| Instrument ~20 real Woolly interactions and capture token counts | Ron Snyder | Replaces every unmeasured assumption. Half a day. Highest-value step available |
| Set the Console workspace spend limit at $1,000/month | Darryl / eng lead | Only control that fails safe, and the automated suite has no human in the loop |
| Mock LLM responses for plumbing tests; run remaining automated traffic on Haiku | Eng lead | Largest controllable lever in the model |
| Confirm which budget carries the Anthropic spend | Darryl / Finance | Cannot ride the Azure envelope, because Woolly cannot use Foundry |
| Feed the cost basis into the entroCIM AI one-pager | Darryl | The one-pager requires a cost and revenue estimate for the AI Tech Review gate. This is the cost side |

None of these is tracked in `05_Commitments.md` yet. Register A stands at 15, at its ceiling, and no one has accepted any of these in their own words. They are logged as confirmation questions for the next closure check.

## Sources

- Anthropic list prices: `platform.claude.com/docs/en/about-claude/pricing`, retrieved 2026-08-25
- Claude Code enterprise benchmarks (Claude Code component only): `code.claude.com/docs/en/costs`, retrieved 2026-08-25
- Woolly Foundry limitation, API-key practice, and workload scope: Darryl, session 2026-08-25
- Foundry enablement for Claude Code: `Evidence/M365_Evidence_Weekly_2026-08-25_run2.md`
- Woolly evaluation constraints and entroCIM AI commercial position: `Products/entroCIM/entroCIM.md`; `03_Decision_Log.md` Decision Radar, 2026-08-19 entry
