# SkyFoundry (Ecosystem Partner)
As of: 2026-07-21 — enriched with Build 4.0.6 release notes (Paul Bergquist, SkyFoundry, 2026-07-21). Source email filed: `Reference/2026-07-21_SkyFoundry_Build_4.0.6_Woolly_Beta.pdf` (verified 07-22 — full text matches this summary).

## Relationship
Monthly Wesco/SkyFoundry coordination forum (Darryl owns). Ecosystem coordination around Xeto. SkySpark 4 surfaced 2026-07-13 in CSS Platforms AI discussion — potential roadmap/positioning implications alongside Wooly AI. **07-21: SkyFoundry shipped Build 4.0.6, the first production release of the 4.0 line**, sent directly to Chad Steger, Darryl, Keith Bishop, and Ron Snyder (cc Ross Schwalm, Roger Quesnel) — this is now a live release Darryl's team has, not a roadmap abstraction.

## What We Depend On Them For
**SkySpark is the platform underlying entroCIM** — core architecture dependency. SkyFoundry ecosystem evolution (including Xeto data-modeling work) directly affects entroCIM architecture and roadmap. Specific versions and roadmap dates must be validated before technical use.

## Build 4.0.6 — Release Summary (2026-07-21)

**Headline:** first production-quality release of the 4.0 Xeto-based architecture. Migration required (fandoc → markdown conversion of arc parts). Backward compatible over a cluster with 3.1 nodes (down to 3.0.24) with one exception: no live-mode replicas from 3.1 nodes (must set passive).

**Woolly (Beta) — the item with the most direct read on the CSS AI roadmap:**
- SkySpark's first LLM agent harness, ships in beta inside the `hx.ai` extension. Supports three model providers — Anthropic Claude, Google Gemini, OpenAI — using a customer-supplied API key per provider.
- Ships with an "extensive skills library": can perform most SkySpark tasks (help, writing functions, creating rules, building views) via natural language.
- **Free during beta; SkyFoundry plans to price Woolly and the Ion Creator tools separately from SkySpark**, with pricing detail promised at SkyPosium this fall — a real commercial-planning input, not yet a number.
- **By default, Woolly shares user transcripts back to SkyFoundry** "so we can make Woolly better." This is turned off with the `shareTranscript` flag on the settings page — a documented, one-step control, not an open gap. Set it before piloting against anything customer-facing or customer-data-adjacent.
- **SkyFoundry's release notes: "Woolly ships with no guardrails or plan mode... Woolly has full access to invoke any Axon function that your user account has permission to call... it is a very sharp tool."** Read correctly, this is SkyFoundry telling us how the beta works, not disclosing a defect: guardrails/plan mode (a propose-before-executing step) are beta features not yet built and are on their near-term roadmap. Access itself follows the same model as the rest of SkySpark/entroCIM — Woolly can only do what the signed-in user's own account is already permitted to do. Practical takeaway: pilot with an appropriately scoped account, and know that actions execute immediately (no confirmation step) until plan mode ships.
- Ion (the planned new UI) ships but is disabled in this build — SkyFoundry is still iterating on navigation/view design; only incomplete docs included.

**Other changes relevant to entroCIM's technical foundation (lower exec-priority, tracked for completeness):**
- Companion lib now supports partial compilation (an error in one func/spec no longer faults the whole lib) — reduces blast radius of authoring mistakes.
- Automated HTTPS certificate enrollment/rotation (RFC 7030 EST) — removes a manual cert-renewal task; WISP can rotate certs without a restart.
- New `ioHttp()` function, Xeto multi-file mixins, remote Xeto repo tooling (`xeto install/remote-*`), arcbeam crawl functions for large Niagara systems, spark "silencing" (suppress without disabling), and a wholesale fandoc→markdown documentation conversion.

## What They Get From Us
*(to be enriched)*

## Strategic Options / Open Questions
- **SkySpark 4 adoption path and how it interacts with the CSS AI roadmap** (see `03_Decision_Log.md` — AI roadmap direction). Woolly's arrival makes this concrete: does Darryl's team pilot Woolly as part of the AI-project-ideas analysis owed to Sean, and if so, under what governance (transcript-sharing default, no-guardrails access)?
- Whether any pilot use warrants the same lightweight scoping discipline as other AI tools (appropriately scoped account, `shareTranscript` off) — a normal setup step, not the same category of review as the Claude-code WAB track (`03_Decision_Log.md`), which involves a different vendor and a different access model.
- Migration timing and cluster-compatibility planning for 4.0.6 across any mixed-version entroCIM clusters.
- Woolly/Ion pricing exposure once announced at SkyPosium (fall) — currently free, unbudgeted line item risk once priced.
- *(enrich: licensing posture, alternatives considered, partnership history)*

## Key People
- **Paul Bergquist** — SkyFoundry; sent the 4.0.6 release announcement directly to Chad Steger, Darryl, Keith Bishop, Ron Snyder (cc Ross Schwalm, Roger Quesnel). Role/relationship: unconfirmed beyond being the release-notes author/contact.
- **Ross Schwalm, Roger Quesnel** — SkyFoundry, cc'd on the release. Role/relationship: unconfirmed.
- **Keith Bishop** (Wesco, Senior Data Scientist, reports to Ron Snyder) — already tracked as an AI-strategy participant and candidate owner for AI governance framing (`06_Stakeholder_Map.md`); a direct recipient of this release, natural first evaluator of Woolly.

## SkyPosium 2026 (added 2026-08-26)

**Event.** October 13-14, 2026, Park City, Utah (SkyFoundry announcement). Two tracks relevant to Wesco: Developer, and Applications/Business. Call for Presenters open at skyfoundryevents.com; submission deadline not yet confirmed. Sits eight days after the entroCIM Q3 release date on record (2026-10-05).

**Why this year is materially different from a normal user conference.** Build 4.0.6 (first production release of the 4.0 Xeto architecture, July 2026) requires migration; entroCIM connector and application migration is in testing with rollout preparation and training approved 08-17. SkyFoundry has stated Woolly and Ion Creator will be priced separately from SkySpark, **with the pricing detail promised at SkyPosium** — an unquantified FY27 line item on a plan already negative across the authorised revenue range. The open Woolly endpoint question (no Azure AI Foundry support at this point, no internal/local endpoint option) is the gating item for the Federal Reserve and other secure-facility customers and can be put to SkyFoundry engineering directly at the event.

**Funding position as of 2026-08-26 (Darryl, direct). CORRECTED — an earlier version of this entry wrongly recorded travel as covering four.**

- Marketing SAR approved by Finance at **$2,300, registration only.** Marketing's own arithmetic (four "doubles that cost"; a 10% overage "does not cover the cost of 1 additional registration pass") implies the SAR was scoped at **two passes at roughly $1,150 each**. Per-pass price is **inferred, not confirmed** — get it from the event POC before relying on it.
- **Travel sits in the Digital Products budget and covers three people only.** Darryl has no reallocation headroom, and neither does Marketing.
- Marketing covered registrations for all three attendees last year.
- **Consequence, and it is the finding that matters: even the three-person floor is unfunded by one registration pass.** The SAR was scoped below last year's actual, so this is a shortfall against prior-year attendance rather than a request to expand. Frame any ask as restore-to-parity, never as an increase.

**Decision, 2026-08-26 (Darryl).** Attend with **three: Ron Snyder, Keith Bishop, Chad Steger.** Darryl is not attending; his own seat was the marginal one, needed both a pass and travel at roughly three times the marginal cost of a technical seat, and defending it would have put the three needed seats in play. Woolly and Ion Creator pricing, announced at this event, is picked up by the three attendees and through the monthly SkyFoundry coordination forum instead.

**No presenter submission for SkyPosium 2026** (Darryl, 2026-08-26): no team capacity to prepare a session on top of the migration and the Q3 release. The Call for Presenters was raised by Marketing and should be declined explicitly rather than left open. **Do not cite another conference as the reason** (Darryl, 2026-08-26, NexusCon reference removed): capacity stands on its own, and naming a second event invites the reply that time and budget for conferences evidently exist.

**FINAL POSITION, 2026-08-26: two attendees, Keith Bishop and Chad Steger.** Ron Snyder is unavailable that week (personal commitment). Two fits inside the approved $2,300 SAR, so no additional pass and no Finance escalation are required. The three-person case above is retained deliberately: it was never refused, it simply stopped being needed, and the reasoning governs next year.

**Precedent risk, and it is the reason the process ask matters.** Three attended in 2025; two attend in 2026 for a scheduling reason. Unless that reason is on the record, the 2027 SAR gets scoped from the 2026 actual and the same shortfall recurs one level lower. This is the identical mechanism that produced the 2026 gap. **Any future SkyPosium sizing conversation must start from "two in 2026 was a conflict, not a right-sizing."**

**Follow-ups from Ron's absence: both closed 2026-08-26 (Darryl).** Keith Bishop and Chad Steger are sufficient for session coverage and will brief Ron on return. **SkyPosium proceedings are recorded and will be available for Ron to watch**, which closes the knowledge-transfer gap without further action. No debrief mechanism needs to be built.

**But do not let the recordings become next year's sizing argument.** Session content being available on video is exactly the argument a reviewer will reach for to cut attendance further in 2027. It does not hold, and the reason is already on the record above: the value of attending is direct access to the SkyFoundry engineers who built the architecture, the follow-up questions on the Woolly and Ion Creator pricing that only get answered in person, and the relationship itself. Recordings cover the content. They do not cover any of that. **Carry this into the next sizing conversation before someone else raises it.**

**Positioning guidance, held for a future submission.** The entroCIM backlog discussion about pushing SkySpark back and bringing entroCIM forward is correct internal positioning, but a SkyFoundry audience responds to what Wesco built on top of SkySpark, not to a narrative that reads as displacing it. Pitch the application, deployment scale, or migration experience.

**Why three rather than two, for the record.** Migration to 4.0/Xeto is required and its timing is set by SkyFoundry, not by Wesco. The two tracks run concurrently across both days; the Woolly/Ion pricing session has to be covered while technical sessions run; and the three attendees cover different parts of the work (platform engineering, data and AI, deployment delivery). SkyFoundry sends its release announcements directly to Chad Steger, Keith Bishop and Ron Snyder, so these three are the named technical contacts in the relationship rather than an arbitrary selection. 4.0 platform knowledge should also not concentrate in a single engineer, which is a live watch item in `04`.

**Tabletop staffing is not a justification (Darryl, 2026-08-26).** SkyPosium is a user conference; the tabletop is light work and low value. It was drafted into the case and removed. Do not reuse it.

**Framing correction (Darryl, 2026-08-26).** The line "I would not make the same request in a normal year" was cut. It reads as a concession and invites the request to be treated as an exception. Assert the migration value instead: the required migration, the people executing it, and direct access to the engineers who built the architecture ahead of customer rollout.

**Forward ask, raised with Marketing 2026-08-26.** Darryl asked to be involved in sizing this event before next year's SAR is submitted. **This year's shortfall is a scoping gap, not a spending problem**, and giving Marketing the attendance number ahead of the submission removes it. Trigger has no date yet: Marketing's event SAR cycle timing is unknown, and per the trigger backstop the unknown is the action. Establish that date before this becomes a carried commitment.

**Open items.** Actual per-pass registration price (unconfirmed); whether SkyFoundry offers a partner or reseller rate (unanswered); tabletop space and floor map not yet assigned (Marketing POC to confirm); Marketing's answer on the third pass (pending as of 08-26).
