# SkyFoundry (Ecosystem Partner)
As of: 2026-10-26 (SkyPosium 2026 debrief, combined notes from Chad Steger and Keith Bishop, filed `Evidence/SkyPosium_Notes_Chad_Steger_2026-10-26.pdf`; Build 4.0.7 release notes, 2026-10-23, circulated by Ron Snyder, filed `Reference/2026-10-23_SkyFoundry_Build_4.0.7_Release_Notes.md`). Prior: 2026-07-21 — enriched with Build 4.0.6 release notes (Paul Bergquist, SkyFoundry, 2026-07-21). Source email filed: `Reference/2026-07-21_SkyFoundry_Build_4.0.6_Woolly_Beta.pdf` (verified 07-22 — full text matches this summary).

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

## Build 4.0.7 release summary (released 2026-10-23, added 2026-10-26)

SkyFoundry shipped 4.0.7, the second production release of the 4.0 line, with Woolly plan mode, custom LLM providers, a Woolly price date (free until 2027-05-01, then a "server pro" add-on), Xeto declared feature complete, and a TLS hostname verification security fix.

Source: SkyFoundry release notes for Build 4.0.7 (23 Oct 2026), circulated by Ron Snyder; Ron has updated to 4.0.7 (Darryl, 2026-10-26; which environment is not stated). Verbatim text in `Reference/2026-10-23_SkyFoundry_Build_4.0.7_Release_Notes.md`. Assessment for entroCIM in `Products/entroCIM/entroCIM.md`, section dated 2026-10-26.

**Woolly (the items with the most direct read on the entroCIM AI thread).**
- **Plan mode now exists.** Three modes: plan (no side-effect functions), confirm (asks before side-effect functions), auto (full access under the user's account permissions). Every SkyFoundry function that commits, writes files or makes network calls carries a new `sideEffects` meta tag; SkyFoundry asks developers to tag their own functions the same way. This closes the "no guardrails or plan mode" gap recorded against 4.0.6.
- **Custom providers.** A Woolly | Providers tab connects Woolly through LLM gateways, other providers and local LLMs, provided they speak the OpenAI protocol. This is the first stated route to a non-Anthropic, non-public endpoint and bears directly on the Azure AI Foundry and secure-facility question (see entroCIM file).
- **AiRoutines:** autonomous background agents triggered by observable events (time of day, a new spark), running a prompt and evaluating Axon. New multi-threaded background engine runs several agents at once.
- Chat view shows inline tables and charts, expandable tool calls, and running agents. Many new skills; `know-perf` runs a full server performance diagnostic.
- **Pricing:** "We are offering Woolly at no charge until 1-May-2027, after which a 'server pro' add-on will be required." Mechanism named (a per-server add-on), price not stated.

**Xeto: declared feature complete.** xeto.dev is live as the community repository for libs and docs (beta for a few weeks, then the site is wiped and opened for public accounts). New Namespace | Install view installs from xeto.dev and other remote repos. Sugar specs (nominal anchor spec plus tag constraints; `ph.equips.x`, `ph.points.x`, `ph.elec.x`). New validation engine with custom rules in Fantom or Axon; `fits` and `fitsExplain` are removed and replaced by `validate()`. Mixins can declare globals; new packaging rules (`include`, `publish` tags) and a `libMaturity` flag (alpha, beta, stable). Initial RDF export (RDFS, SHACL Core, QUDT) via `ioWriteRdf()`; the Haystack 4 legacy RDF format, `ioWriteTurtle` and `ioWriteJsonLd` are deprecated.

**Jeto and HTTP API v5.** Jeto is a new Xeto-typed JSON flavor with JSON Schema generation. A new HTTP API v5 (opt in with header `Xeto-Version:5`), fully backward compatible, publishes a Swagger/OpenAPI schema at `/api/proj/openapi` using Jeto. `ph` and `ph.api` are now boot-level libs in every SkySpark system. Haystack client gains OAuth support. Legacy JSON v3 is deprecated and the global `jsonVersion` setting is removed; v3 is reachable only by explicit mime type or the `{v3}` option.

**Model app.** New app for Xeto-based tools: Composer (builder), Point Mapper (bind points to connectors from Xeto equip templates), Fit (check entities against specs and rule bindings). Using them requires adding the `spec` tag to recs per the Haystack 5.0 ontology.

**Security.** HTTP and arcbeam hardening, plus "one very important security fix for TLS hostname verification" (SkyFoundry post 9113). All Folio read/commit security checks moved into the Folio base class; per-spark access filtering removed. Whether 3.1 nodes are affected by the TLS fix is not stated in the notes.

**Breaking or migration-relevant changes for anyone building on 4.0.** `readAll()` loses the `{trash}` option (new `readTrash()`); third-party extension web URLs change from `/ext/{proj}/{lastName}` to `/ext/{proj}/{fullLibName}` and project extensions can no longer override route names; `ConnExt.modelName` overrides must use the `connFeatures` name; Filetype redesigned without defs; `WebOpUtil` and `sys.template` removed; a migration must be run if rule tuning records exist (adds the `hx.rule::RuleTuning` spec). Cluster compatibility with 3.1 nodes (down to 3.0.24) is preserved, except live-mode replicas from 3.1 nodes, which must be set passive.

**Other.** Modbus points can now be defined from a Xeto spec (`ModbusAddr`) instead of a register map, with fixes for block gap and max handling, scaling expressions and TCP connection handling, and frame-delay support. Demogen generates central plants and water loops. `sqlInsert` batches; `hisWrite` can skip the `onHisWrite` callback; project import improved for large projects.

**What the notes do not say.** The server pro add-on price; whether the custom-provider path has been tested against Azure OpenAI or Azure AI Foundry endpoints; whether the TLS fix applies to 3.1; Ion status (not mentioned in 4.0.7 at all, after shipping disabled in 4.0.6).

## What They Get From Us
*(to be enriched)*

## Strategic Options / Open Questions
- **SkySpark 4 adoption path and how it interacts with the CSS AI roadmap** (see `03_Decision_Log.md` — AI roadmap direction). Woolly's arrival makes this concrete: does Darryl's team pilot Woolly as part of the AI-project-ideas analysis owed to Sean, and if so, under what governance (transcript-sharing default, no-guardrails access)?
- Whether any pilot use warrants the same lightweight scoping discipline as other AI tools (appropriately scoped account, `shareTranscript` off) — a normal setup step, not the same category of review as the Claude-code WAB track (`03_Decision_Log.md`), which involves a different vendor and a different access model.
- Migration timing and cluster-compatibility planning for 4.0.6 across any mixed-version entroCIM clusters.
- Woolly/Ion pricing exposure once announced at SkyPosium (fall) — currently free, unbudgeted line item risk once priced. **Update 2026-10-26: 4.0.7 notes set the date and mechanism (free until 2027-05-01, then a "server pro" add-on); the price is still not stated. Tracked as `D097`.**
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

## SkyPosium 2026 debrief: Chad Steger and Keith Bishop's combined conference notes (added 2026-10-26)

The combined SkyPosium 2026 notes from Chad Steger and Keith Bishop (Park City, 10-13 to 10-14) confirm the 4.0 roadmap order (Xeto and Woolly first, Ion later), name a second Woolly pricing tier ("User Pro", per user) alongside the per-server "Server Pro" tier, put Ion in beta in 4.0.7 with tooling targeted for production by year end, and carry the attendees' own assessment of what each thread means for entroCIM (filed in `Products/entroCIM/entroCIM.md`, section dated 2026-10-26).

Source: `Evidence/SkyPosium_Notes_Chad_Steger_2026-10-26.pdf` (compiled by Chad Steger from his and Keith Bishop's notes; Darryl, 2026-10-26; appendix of two Ion screenshots). Everything below is their record of what SkyFoundry presented; where it reads as their judgment it is marked as such. Individual statements are not attributed to one or the other.

**Roadmap and timeline (as presented).** 4.0.4 Dec 2025 (first public beta), 4.0.5 Feb 2026 (second beta, new rule engine), 4.0.6 Jul 2026 (first production, Woolly), 4.0.7 Nov 2026 (Xeto and Woolly maturity), 2027 and beyond "everything else, when ready." SkyFoundry said priorities shifted toward Xeto and Woolly; the roadmap content is unchanged, only the order. Note the presented 4.0.7 date was November; it shipped 2026-10-23. Fresco (`/ui/`) continues alongside Ion (`/ux/`) with no firm Ion release date; the Builder app is replaced by the Model app only after Ion ships. The next Haystack Connect conference was announced for May 24-26, Denver (year not stated in the notes; 2027 assumed).

**Ion, which the 4.0.7 release notes did not mention.** In beta in 4.0.7; new tooling targeted for production by end of 2026. Demonstrated: relational one-line diagrams generated from the model (site to equipment to sensor) when tagging is correct, and a widget library for dashboards without line-by-line coding. Not demonstrated but on the roadmap: block-based coding that translates to Axon.

**Woolly: concepts, architecture, roadmap, pricing.**
- Concepts: Providers, Models, Agents, Conversations (Folio records), Routines (observable listeners running agents in the background), Tools, Skills (documentation bundles), Memory (persists snippets across sessions).
- Architecture: an "Axon Sandbox" behind an effect guard; functions tagged `noSideEffects`, unmarked, or `sideEffects`, gating what Woolly touches without confirmation. Woolly has the same functional reach as the signed-in user. Described as particularly strong at writing Axon and Xeto. Ion-based UI generation was not enabled in the demo build.
- Demonstrated: querying and analyzing site data, writing and debugging Axon, designing Xeto specs, creating and updating Folio records with a confirmation step before destructive actions, building Fresco views.
- Near-term roadmap (SkyFoundry asked for customer feedback): conversation compaction, decision-model integration, stemming-aware search, multi-agent cooperation, enhanced memory, and hx.dev (tooling for Xeto libs and Fantom pods, explicitly so customers can extend Woolly).
- **Pricing, early and subject to change:** bring-your-own API key supported for most providers (most speak the OpenAI protocol). Two planned subscriptions: **"Server Pro" (per server; unlocks hx.ai and autonomous routines)** and **"User Pro" (per user; unlocks AI views and other power-user tools)**. No numbers. The 4.0.7 release notes name only the server pro add-on; the per-user tier is new information from the conference.
- Opening-session framing, quoted in the notes: "the days of humans slinging code are pretty much over."

**Xeto language and tooling.** Globals (one definition per tag, in `ph::PhEntity`), mixins (one lib extends another's spec without editing it), choices (exactly one tag from a set), sugar specs (`ph.points.sugar`, `ph.equips.sugar`; predefined spec-plus-tag combinations that act like filters), templates for repetitive equipment, multi-refs in 4.0.7, Jeto (typed JSON compiled from the schema, three boxing levels, `ioReadJeto()` / `ioWriteJeto()`), RDF mapping (Xeto specs to RDF classes and SHACL shapes, units to QUDT, for alignment with 223p, Brick, REC, IFC), and the new validation engine (`xeto validate` replaces `fits`; one consolidated report per record naming slot, type, unit or ref; rules per spec in Fantom or Axon). Existing connectors need a `connFeatures` tag in their meta (`hx.haystack` is the reference).

**xeto.dev and self-hosted repos.** xeto.dev is positioned as npm for Xeto libs, live once 4.0.7 ships, with the publish and pull pipeline in 4.0.7 (`fan xeto help`). Attendees' note: a Wesco/entroCIM org appears to be registered already, but real access and user association will probably need a request to SkyFoundry. The IDE's Lib Repos dialog shows the default dev repo and custom repos (a GitHub-hosted repo was shown), so teams can register their own; Haxall's `sys.repo` is a self-hosted alternative or complement.

**Model app.** Three tabs: Composer (Builder replacement), Point Mapper (points to connector positions), Fit (validates installed records). A "Compion Status" view over a project's Xeto lib was flagged by the attendees as worth reviewing for the team's QA process. Community tooling mentioned: "Ion Flux" (open-source Fantom IDE, reportedly on GitHub), `fan xeto gen-fan`, hx.dev, icon library at `/dev/icons/`.

**HTTP API v5.** Additive and backward compatible; opt in per request with `Xeto-Version: 5`. Every endpoint is a Xeto function carrying an `<op>` tag (an Axon function annotated `<op, noSideEffects>` became a typed GET endpoint in the live demo). Default wire format Jeto; OpenAPI 3.1 document served per lib. Failures return real HTTP status codes with a typed `sys.api` error payload, replacing v4's "200 OK with a Zinc grid." OAuth being added as an authentication option; v5 also defines the SkySpark-to-xeto.dev protocol.

**Haystack 5 ontology.** Standard point descriptions for every Modbus and BACnet point type; equip templates set `modbusAddr` through a single 6-digit extended-Modicon address with slots from the `ph.protocols::ModbusAddr` global. Motors and VFDs: speed always a percent of full speed (ASHRAE Guideline 36-2024 section 5.1.13) with new standard points. One modulating Sensor/Cmd pattern (0 to 100%) reused across valves, dampers and capacity points; a separate two-position open/close pattern. `EvseConnector` renamed from `EvseCoupler`. Open questions raised at the session: further normalization (negative AC RMS current), representation of some electrical switches.

**Security.** `hx.oauth`: an OAuth 2.0 authorization server (aligned to the 2.1 draft) built into SkySpark as client and server, on RFC 6749, 6750, 7009, with PKCE (7636), native-app practice (8252), dynamic client registration (7591) and server metadata (8414). Automated certificate management (EST, RFC 7030) and hot-reload of the HTTPS certificate without restart.

**Rule engine (4.0.5 onward).** `defcomp`-based rule components replaced by plain typed Axon functions. `ruleBindPoint` resolves parameters to points under the target equip by Xeto type at roster refresh (no hand-written `{{target->id}}` filters for the common case); `ruleBind`, `ruleBindOptional`, `List<of:Point>` binding; unbound parameters become tuning values, overridable per target with `RuleTuning` records. Gotcha recorded in the notes: a plain Xeto default is silently ignored for tuning parameters; an `axon:` default is required. Outputs via `ruleToCurVal` and `ruleToWriteLevel`; debug via `ruleTest`, `ruleBindings`, the Model > Fit gap view, Rule > Debug, `ruleErrs(null)`.

**What the notes do not say.** Any price for Server Pro or User Pro; whether the custom-provider path was tested against Azure OpenAI or Azure AI Foundry, or whether the secure-facility question was put to SkyFoundry at all (absence in the notes is not evidence it was not asked); the TLS fix and 3.1 exposure.
