# Launch Studio (working name, Darryl 2026-10-08; formerly Vibe Coding Productization)
As of: 2026-10-06. Thread opened this date. **Status: exploration. Owner: Darryl Benson, who will stand it up. Origin: Sean McCloskey's idea in the 2026-10-06 FY27 AOP update.**

## The concept as stated (Darryl, direct, 2026-10-06)

A company-wide team that productizes vibe-coded ideas:

1. Review the ideas coming from the business units.
2. Select two or three.
3. Productize them at scale.

Darryl's reasons it works, in his framing:

- **Business alignment is built in,** because the ideas come from the business units.
- **It is funded by the business.**
- **It is politically difficult to say no to.**

## Why now (context already in the EOS; Claude's connections, not Darryl's statements)

- **The demand is already showing up, unmanaged.** On CAT, Hemant Porwal declined a vendor subscription and pointed the team at internal build, citing a GPS tracking prototype he built "in about two minutes" (`Products/CAT/CAT.md`). That is a business-unit vibe-coded idea with no route to production, support, or security review. This team is that route.
- **Sean has been pushing AI into Darryl's team.** On 09-15 he raised bringing agentic AI into the team directly, framed as reducing reliance on Brad Stevens' organization (`06` Sean McCloskey). This concept gives that a defined shape.
- **Sean wants AI benefits measured, not anecdotal** (09-16: missed requirements, rework, defects, cycle time). Any pitch for this team should carry a measurement design from the start.
- **The AI-enabled development proof point exists** (Ron Snyder's team: estimated effort from 80 hours to 10 on an HQ embedded-search build, 09-16, not yet measured).
- **Capacity question, hypothesis to test:** the AOP outcome leaves headcount without a product after the entroCIM and CDA balancing (`05` A57). A business-funded productization team may be a place for some of it. Not raised by Darryl; flagged here because the timing coincides.

## Status log

- **2026-10-07 (Darryl, direct):** meeting set for Darryl and Ron Snyder with Mike Wassil, who leads part of the Digital Products AI drive. Per `06`, Mike's remit since 09-16 already includes the vibe-coding group and idea-funnel visibility under Maddy Taylor, with resulting products transferring to the appropriate product owner (Sean, 09-15). **That makes Mike the most likely owner of the intake end of this concept, and the meeting the place to settle design question 7.** Meeting date: Thu 2026-10-08; brief in `Deliverables/Vibe_Code_Productization/`. The brief proposes a four-stage split (Mike: find and screen; joint: select; Darryl and Ron: productize; run: open) as a discussion position, not a decision.

- **2026-10-07 (Darryl, direct): operating model set, superseding the four-stage split Claude proposed earlier the same day.** (1) Mike Wassil is the conduit to the vibe coders; there is no ownership conflict and nothing is being taken from him. (2) Darryl and Ron Snyder lead it as a joint team. (3) The CSS team carries the full path: David Blondel as product owner, Ron's team as developers and as operators. Purpose in Darryl's words: take the vibe coders' concepts to actual business value, at the right scale. (4) Staffing: start with the current team; additional people are a bridge to cross when needed. This closes design questions 4 (run ownership: Ron's team operates), 6 (team shape) and 7 (boundary with Mike).

- **2026-10-07 (session):** Mike brief revised with the challenge evidence, job to be done, working service model and nine questions (three new: prototypes already in production, funding offers, good ideas nobody owns). Meeting deck built on the Wesco template: `Deliverables/Vibe_Code_Productization/2026-10-08_Mike_Wassil_Meeting_Deck.pptx` (generator in `build_scripts/`). Darryl asked that the deck's challenge and model visuals carry forward into the product's later materials (the case Sean takes to Akash).

- **2026-10-08 (Darryl, direct):** working name **Launch Studio** adopted for now, feedback to follow (`03` 2026-10-08). Darryl endorsed the line "if IT absorbs it, compliance goes up and friction goes down." Mike meeting postponed to **Mon 2026-10-12** (other conflicts). Next design topic, at Darryl's request: how the vibe coder is embedded in the process with the team.

- **2026-10-08 (session):** vibe coder embedding designed (embedded in the product work, shielded from the compliance work; role at Submit, Screen, Assess, Build, Launch, Run; originator advises and accepts, David decides; sponsor commits funding and the originator's time; product survives the originator leaving). Three layout options sketched in Darryl's private Miro board "Launch Studio Swimlane 2026-10" (A swimlane with line of visibility, B two bands, C the loop); generator `Deliverables/Vibe_Code_Productization/build_scripts/build_miro_launch_studio_swimlane.py`. Darryl picked B for the deck with A as backup (2026-10-08); rebuilt natively in `2026-10-12_Launch_Studio_Mike_Wassil_Meeting_Deck.pptx` (slide "The vibe coder" and "Backup: roles by stage"); brief updated to match; 10-08 versions marked SUPERSEDED. Open: is the originator's time a hard requirement at Commit or a strong expectation.

- **2026-10-13 (session, Fable):** Mike Wassil's package received the day after the meeting: "Wesco Launch Studio" deck (25 slides plus 17 appendix) and 52-page report, dated 2026-10-12, authored "Michael Wassil, Digital Products, with the original Launch Studio model from Darryl Benson," built from a "recommendations brief prepared for Michael Wassil" (its source 2, not yet seen) and about 130 sources. It records Darryl's ask that measurable success be core to the process. Files: `Deliverables/Vibe_Code_Productization/Wesco_Launch_Studio_Deck_2026-10-12 1.pptx` and `..._Report_2026-10-12 1.pdf`. **Review filed in chat; Darryl accepted all recommendations (see `03` 2026-10-13).** Darryl confirms (10-13) that what was agreed on 10-12 stands and that he met Mike and Ron again on 10-13; neither meeting's detail is on record yet (the 10-13 transcript file holds 90 seconds). Route to Sean corrected: Darryl presents, joint initiative with Mike. Request for Mike's brief dropped. Our 10-12 deck and brief are left as they are (Mike's package cites them as source 1) and are superseded as the working model by his package plus the positions in `03`.
- **Terminology change (from Mike's report, 2026-10-13):** Wesco leadership materials use **AI Builders Guild** for the community and **AI-assisted building** for the practice. Use those from now on in anything that leaves the team; "vibe coder" and "vibe coding" only where a source uses them.

- **2026-10-13 (later):** Darryl: full alignment with Mike; capacity row goes in the Sean paper, Mike reviews first. **Darryl (same day): do not rule out an AOP ask; the capacity changes from the 10-06 AOP conversation may make Launch Studio the home for otherwise unassigned people.** **Darryl (same day): Launch Studio fronts the on-ramp; it owns the inlet filter that grades business value and prototype viability with tools and process.** Added to the overview as its own section (two grading questions, tools, four outcomes with reasons, 30-day target; the grade becomes the value contract and the reimbursement project). Note: Mike's package put the first gate ("worth proving") with the Guild lead; the overview puts grading with the Studio. Show Mike alongside the capacity section. Overview revised accordingly (closing section "What this needs to start"; fourth decision for Sean on an FY27 AOP line). Executive overview for Sean drafted: `Deliverables/Vibe_Code_Productization/2026-10-13_Launch_Studio_Executive_Overview_for_Sean.md` (three lanes, four principles, capacity, funding shape and menu, pilot, three asks, no budget or headcount request).

- **2026-10-13 (later still):** Sean deck built on the Wesco template: `Deliverables/Vibe_Code_Productization/2026-10-13_Launch_Studio_Executive_Overview_Deck.pptx` (two executive slides from Miro options 1A "the path" and 2A "decisions lead", plus six backup slides: who does what, the on-ramp, funding menu, the builder, pilot plan, evidence base). Layout options sketched first in Darryl's private Miro board "Launch Studio Sean Deck 2026-10"; generators in `build_scripts/`. Mirrors the executive overview document of the same date.

- **2026-10-20 (Digital Products / Agile Staff Meeting, transcript; Claude classified Durable):** Sean McCloskey named the work to his staff as Darryl's: "The one area that Darryl is going to work on, and I think I really like this, is he's going to continue to work with the Mike and the Vibe coding to see if product ideas coming out of there should become digital products." Then, to Darryl: "please keep the team updated as you go through that, because I think that's perfect." Sean's endorsement is now on record in his own forum, which is the first time it has been stated outside the Darryl-Mike-Sean line. Related in the same meeting: Maddy Taylor said Mike is "reaching out to each of the leaders under Akash to figure out if there are products within their groups that they would like this training running on" (AI-assisted building training widening beyond Digital Products); Sean raised the hand-over risk directly, "if Dan does something and he can't hand it over to the product owner, it's a problem" (Claude Design context), which is the Launch Studio gate problem stated by the sponsor; Sean asked for a mechanics meeting "later this week" on where documents reside, MCP servers and moving data, no owner named. Source: `Evidence/M365_Evidence_Daily_2026-10-20_AgileStaff.md` (transcript, 732 of 732 lines).

## Onboarding review: a new body, with existing approvals unchanged (Darryl, direct, 2026-10-14; corrects "no new approval body")

The 10-13 executive overview and Mike's package said "three lanes and no new approval body." Darryl, 2026-10-14: that contradicts the model. **A new body reviews submissions from builders that come with their business's endorsement and offer payback and value to the company; Wesco needs an onboarding process to vet tools coming from the broader company.** The two statements reconcile as: the onboarding review is new; the approvals are not. The inlet filter is renamed **onboarding review** in all material from v17 of the Sean deck.

- **Who sits on it (Darryl):** people from the Launch Studio team as part of their work (David Blondel as product owner, Mike Wassil for the Guild, an architect from Ron Snyder's team, Darryl and Ron at the commit step), with executive decision-makers such as Sean McCloskey and Lisa Orton on the calls that need them. Whether the executives are standing members or called in per decision is not yet settled.
- **What it vets:** business endorsement and payback; can it become a product (data, systems, build route, cost to run). Four outcomes with a reason: take it in, fold into an existing product, defer, return to the sandbox.
- **What stays with existing bodies:** AI Council and intake, Security and WAB, Finance, the business sponsor approve as today.
- **Applied 2026-10-14:** the executive overview deck and document were rebuilt as `Deliverables/Vibe_Code_Productization/2026-10-14_Launch_Studio_Executive_Overview_Deck.pptx` and `..._for_Sean.md` (.docx via Pandoc). Changes: inlet filter renamed onboarding review on the path slide and the on-ramp backup; "no new approval body" replaced; a new "Onboarding review (new)" lane on the who-does-what slide and in the document table, with the Decide lane renamed Approve; sentence subtitles under titles removed; the next-steps slide no longer dated to the week of October 19, since that session depends on Sean's read. The 10-13 versions are SUPERSEDED_. The 10-12 Mike meeting deck is left as the record of that meeting.

## Sean portfolio deck, 2026-10-14: two awareness slides (Darryl direct)

Launch Studio is in the same 30-minute portfolio meeting with Sean (week of 2026-10-19), as awareness that the team is making progress on his idea, not as the decision session. Darryl: assigned to him and his team with Mike as partner; reporting back with a framework collaborated on, building on Sean's idea; very early. Two slides after CDA in `Deliverables/Exec_Briefs/2026-10-14_Sean_Portfolio_Deck_v13.pptx`: "Launch Studio" (the path graphic and four principles from the 10-13 executive overview, subtitle removed, credit line "your idea from October 6, built out with Mike Wassil and Ron Snyder") and "Where it stands" (agreed with Mike and Ron; shape of the pilot; still open for a separate session, including **whether Launch Studio is the home for capacity freed by the 2027 reductions**, kept as the last bullet at Darryl's decision). Launch Studio is not on the Portfolio table (a service, not a product); the cover note carries one paragraph. **Darryl, 2026-10-14: no request for a follow-up session on the slide. A separate session with Mike happens only if Sean supports the direction; if not, the open items stay unworked.** Deck v14. The 10-13 executive overview deck remains the material for that session.

## Problem definition (Darryl, direct, brainstorm 2026-10-07)

- Of five candidate problem framings, Darryl chose the **capacity vehicle** as the best fit: a business-funded home for CSS team capacity.
- Scalability and security concerns roll up into one statement of the problem: **the business has the expertise and ability to define problems; Darryl's team has the ability to launch them professionally and maintain them for the business.**
- **"At scale" means production-grade quality** for whatever segment or segments need it. A product may serve one business (CSS, ESS, UBS) or span them.
- No concrete candidate ideas are known yet; the first look is expected from the Mike Wassil meeting, postponed from 2026-10-08 to Mon 2026-10-12.
- **Terminology (Darryl, 2026-10-07, second pass): "the business" is CSS. Launching and sustaining production-grade software is the job of Darryl's team, which is IT (CSS Platforms).** Do not write "CSS can launch it" meaning Darryl's team; CSS is the customer of this service.
- **Job to be done (Claude's draft, Darryl accepted):** "When my team has built a prototype that solves a real problem, I want it running reliably, securely and supported for my segment, so I get the business result without building a software organization."
- **Internal managed service (Claude's framing, Darryl: "spot on").** Caveat from Darryl: the definition of managed service may need adjusting, because Wesco is looking at managed services as a company. Keep the term from colliding with the customer-facing CSS Managed Services model (`Reference/Managed_Services_Operating_Model.md`) until that is settled.
- **Audience beyond Sean (Darryl):** Sean has not scoped this to Akash Khurana yet. This work builds the case Sean takes to Akash, so every output needs a clear C-level explanation. A funded, managed-service model suits the funding limits. All of it is pending Sean's approval.
- **Funding mechanism exists (Darryl):** IT already has a chargeback mechanism into the businesses. This answers the first-order version of the riskiest assumption (can a business pay a run fee); whether a business will choose to pay for a given product is still untested.

## Service model (brainstorm 2026-10-07, working positions, not decisions)

Seven options were generated. Darryl's reactions:

| # | Option | Darryl's view |
|--|------|------|
| 1 | Product studio: select a few, build, run | Keep. May be the umbrella for the whole model rather than a stand-alone option |
| 2 | Funding as the filter: an idea qualifies when a business commits to fund build and run | Good; take to the team |
| 3 | Tiered service: Register, Harden, Run (mirrors CSA risk tiers), priced by tier | Good; take to the team |
| 4 | Sanctioned template and hosting standard for vibe coders | Interesting; may change given little definition behind current work; likely best practice for vibe coders going forward |
| 5 | Prototype as spec: the product owner treats the prototype as requirements, IT rebuilds to standard | Good; take to the team |
| 6 | Embedded originator joins the productization sprint | No reaction recorded |
| 7 | Retirement desk: formal decline and retirement with a published reason | No reaction recorded |

**Correction, Darryl, 2026-10-07 (round 3): the Harden tier is potentially unviable.** The business cannot own applications; if IT touches an application, IT has to own it. A middle tier where IT secures something and hands it back therefore does not exist. Principle to carry into every later output: **if IT touches it, IT owns it.** Mike deck and brief revised 2026-10-08 to the two-zone model below.

## Two zones and one gate (brainstorm 2026-10-08; Darryl agreed to explore the gate and to route existing prototypes through it)

- **Prototype zone, owned by the business:** sandbox, no production data, registered so it is visible. IT does nothing here.
- **Product zone, owned by IT:** rebuilt to standard, hosted, secured, supported, retired at end of life. Funded by a build charge plus an annual run charge through the existing IT chargeback.
- **The gate (working design, Claude's proposal, not decided):** *Screen* (Mike and David: named sponsor, clear problem, overlap with an existing product, data class); *Assess* (David plus an architect from Ron's team: read-only review of the prototype, ownership estimate for build and run); *Commit* (Darryl and Ron with the sponsor: funding through chargeback, success measure with baseline, review date). Four outcomes, each returned with a reason: accept, fold into an existing product, defer, return to the sandbox.
- **Existing prototypes (Darryl, 2026-10-08: yes):** go through the same gate; anything not accepted comes off production data. IT does not absorb them by default.
- Open gate questions are listed in the brainstorm thread of 2026-10-08 (who represents the business at Commit, Sean's threshold, work-in-progress limit, AI Council one-pager alignment, decision time limit).

Working shape: **a product studio (1) that selects by funding commitment (2), delivers by rebuilding from the prototype (5), and runs products in priced tiers through the existing IT chargeback (3), with a template and hosting standard (4) as the forward practice.** Status: for team review (David Blondel, Ron Snyder's team) and Sean's approval.

## Funding model (Darryl, direct, 2026-10-13; future decision, shape agreed)

- Mechanism is a future decision with Finance. Shape: **IT funds the standing team; the business funds a project that reimburses the IT budget for productization, then for upkeep.** Reimbursement can take a few forms, so present a **menu** to make the business decision easy. Aligns with the existing IT chargeback.
- Working menu (Claude's draft from Mike's three funding options, Darryl's route and the risk tiers): Sandbox (no charge, no production data); Pilot (bounded project reimburses a limited pilot, 90-day decision); Sponsored product (project reimbursement for productization plus annual upkeep charge; IT owns end to end); Shared product (co-funded across segments; shared parts from the IT platform budget).
- Principle that holds regardless of mechanism: no sponsor, no production.
- Open before the Sean paper: whether the team's base funding is Sean's digital products budget or corporate IT.

## External evidence (kept to justify the team's work; Darryl, 2026-10-07)

- **Gartner, "Govern Vibe Coding for Citizen Developers With Self-Service Platforms"** (Nitish Tyagi, 2026-06-29): by 2028, **60% of vibe-coded applications will be retired because they fail to deliver predictable business value**, and **30% of software engineering teams will experience material capacity strain from maintaining vibe-coded applications built by citizen developers.** Recommends development controls with pre-deployment validation, plus an adaptive framework deciding which use cases belong to citizen developers and which to professional engineering. Source: Gartner abstract https://www.gartner.com/en/documents/8068765; summary via Tray.ai https://tray.ai/guides/gartner-govern-vibe-coding/ (secondary; read the Gartner original before quoting externally).
- **Cloud Security Alliance research note, "The Vibe Coding Governance Gap"** (2026-06-02). **CORRECTION 2026-10-13 (Claude, verified against the page; first caught in Mike Wassil's change log):** the "none of 5,600 production vibe-coded apps had CSRF protection, security headers or scoped access" figure is **not a CSA scan.** The CSA note cites a VentureBeat article (October 2025) about a scan by Escape.tech, a security vendor; the article headline says 5,000 apps and the body 5,600, and no primary Escape.tech report is named. Earlier versions of this file, the 10-08 brief and the 10-12 deck attributed the scan to CSA. **Do not use the figure as a CSA finding. If used at all, say "a vendor scan reported by VentureBeat" and treat as company-reported, not independent.** What CSA itself contributes and still stands: no major AI security framework (NIST AI RMF, OWASP LLM Top 10, CSA MAESTRO, CSA AICM) gives dedicated guidance for citizen developers; recommend lightweight registration over gatekeeping and three risk tiers (non-sensitive internal; PII or regulated; AI or agentic). The IBM 2025 shadow-AI breach-cost figure (about $670,000 more) is IBM's, cited by CSA. Source: https://labs.cloudsecurityalliance.org/research/csa-research-note-vibe-coding-ai-governance-gap-20260602-csa/
- **Gartner figures: treat as a labeled forecast from a secondary source until the licensed original is read** (2026-10-13). They appeared on the 10-12 deck as statistics with a source line; the caveat was in the speaker notes only.
- **How this supports the case (interpretation, not source):** the industry problem is not too few prototypes; it is too many that never deliver value and then land on engineering to secure and maintain. A team that selects, launches professionally and runs a small number under a defined standard addresses both Gartner findings directly.

## Design questions to work through

1. **Intake and selection:** who submits, what qualifies as "productizable," who scores, and how often. Criteria candidates: business value, reuse across business units, data access, security exposure, and support load after launch.
2. **Funding model:** *(IT chargeback into the businesses exists, Darryl 2026-10-07; tiered run fee proposed, see Service model)* chargeback per product, a pooled business-unit contribution, or seed funding with business-unit run cost. What "funded from the business" means in AOP terms.
3. **What "productize" means:** *(working position: rebuild to standard from the prototype as spec, see Service model)* hardening, security review, identity and SSO, hosting (containerized, per the entroCIM standard), data integration, documentation, and support handoff.
4. **Run ownership after launch:** does the team keep the products, or hand them to the requesting business unit? This decides whether the team becomes a growing support organization.
5. **Governance fit:** AI Council, the WAB approval track for Claude Code, the Vibe Guard compatibility issue that blocked GitHub Copilot, and the AI-enabled development pilot (`03` Radar). The team needs a path through these, or it stalls where earlier AI tooling stalled.
6. **Team shape:** a small product and engineering core using AI-assisted development, plus business-unit product owners for each selected idea.
7. **Boundary with Brad Stevens' and Lisa Orton's organizations, and with corporate IT:** who else believes they own this.

## Naming

Still open (Darryl, 2026-10-06: keep ideating). Candidates so far: Launchpad, Proving Ground, Catalyst, BU Forge. Avoid "Foundry" (collides with SkyFoundry and Azure Foundry). The name should say "business idea to supported product," not "AI experiment," since the political advantage depends on it reading as a business service.

**2026-10-08 (Darryl, direct):** considering "Product Studio" or something along those lines. Intent: the vibe coders should feel included in something modern and fast, not bogged down by cumbersome process. Wesco IT security and governance still apply, but the vibe coders are shielded from them: **IT executes that work for them as part of the internal service.** This is a positioning principle as well as a naming brief (front stage for the vibe coder, governance backstage with IT).

Claude's notes on "Product Studio" (for Darryl's decision): at Wesco "product" also means catalog items and product data, so the name may read as a catalog or product-content team; Microsoft "Copilot Studio" is a likely tool name in a Microsoft shop and could blur. Alternatives offered: Launch Studio (recommended), Build Studio, Studio W, Wesco Garage (better suited to the vibe-coding community than to the IT service). Check the intranet for existing "Studio" programs before adopting any of them.

## Risks seen so far

- It becomes a dumping ground for every business-unit prototype unless the selection gate is strict and public.
- Productized apps carry support, security and lifecycle cost that business units may not expect to fund after launch.
- "Hard to say no to" cuts both ways: it is also hard to stop a selected idea that is not working. Exit criteria are needed at selection.

## Related

- Register A: `05` A60.
- Decision of record: `03` 2026-10-06 (threads opened).
- Source log: `Source_Log.md`.
