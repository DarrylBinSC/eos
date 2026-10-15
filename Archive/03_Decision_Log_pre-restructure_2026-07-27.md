# Decision Log

> Maintained by Claude during briefings. Three sections: decisions made, decisions approaching, decisions being avoided. Newest first. Seeded 2026-07-13 from 30-day baseline.

## Entry Format

```
### YYYY-MM-DD — [Decision title]
- Status: Made / Approaching / Avoided-Stalled
- Owner:
- Context:
- Options considered:
- Decision / Recommended path:
- Risk of waiting (if open):
- Forum where this should be decided:
- Follow-up:
```

## Decisions Made

### 2026-07-24 — UWM entroCIM server migration cutover completed
- Owner: Syed Zaidi / Shawn Clark
- Event: server migration to the new environment is complete; old environment remains live pending customer sign-off before decommission.
- Follow-up: confirm UWM sign-off status (owed to Darryl by Syed Zaidi — see 05); track dual-environment carrying cost/risk until closed. See Key Product Due Dates.

### 2026-07-24 — NexusCon 2026 speaking slot accepted
- Owner: Darryl (presenter), with Nathan Kehr and Sarah Monteleone
- Event: "Overcoming On-Prem Controls Infrastructure Limits by Pivoting to a Cloud-Hosted OT Data Layer" accepted for NexusCon 2026 — external thought-leadership opportunity.
- Follow-up: conference date, registration deadline, and deck milestones not yet in evidence — confirm and add to Key Product Due Dates once known.

### 2026-07-17 — Managed Services optimization-services offering: ownership decided (Nathan Kehr)
- Owner: Nathan Kehr and his team.
- Decision (Darryl, field note 07-17): Nathan Kehr's team owns the Managed Services optimization-services offering for hosted entroCIM clients. Darryl's team supports during the pilot; longer-term direction is to automate parts of the services.
- Context: resolves the ownership gap flagged 07-16/07-17 (packaging, ownership, delivery model undefined for the hosted-client commercialization discussion involving Nathan Kehr, Leanne Gordon, Valli Poornakumar).
- Follow-up: define the support interface/scope for Darryl's team during the pilot; track automation roadmap as it forms.

### 2026-07-15 — Architect role: Shawn Clark internal move; David Blondel owns close-out
- Owner: David Blondel (Chad Steger on paternity leave 07/15–08/11); Darryl ratified.
- Decision: David spoke with Shawn Clark about moving into the architect role. **Update 07-15 PM (Anna Thornton, HR): no Canadian requisition needed — this can be done as a transfer.** Darryl directed Anna to coordinate and communicate details through David B for Shawn, **so Shawn can make his final decision.**
- Remaining: transfer details (Anna → David → Shawn); Shawn's acceptance.
- **Transition scope (Darryl, 07-15): the move includes his current position** — Shawn carries his existing responsibilities (UWM cutover lead, Panama Liberty backup) into the architect role. No succession gap; the watch item shifts to load: architect capacity is nominal until his current duties are backfilled or wound down.

### 2026-07-15 — Supplier attribute governance: ownership split inside the team
- Owner: Darryl (assignment decision).
- Decision: **Akansh Gangil owns the supplier attribute + data-governance track** — rallying the responsible data teams; next working session Jul 16. **David Blondel owns communication and coordination with Jarod Booth.** Darryl's role: executive escalation and involvement only.
- Stakeholders (Darryl, field note 07-15): Daniel Totino (GPO), Inder Gambhir (Global MDM team), Rishi Sanaka (BPM team), Gandhi Subramanian (IT Manager).
- Residual risk: attendance troubles and Akansh's work-hours vs. North American teams; and cross-org *accountability* (beyond Darryl's org) is still not formally named — rallying is not a RACI. Air-cover mention at Thu Sean meeting.

### 2026-07-15 — EOS: dashboard adopted (snapshot-at-briefing + locked HTML template)
- Owner: Darryl
- Options considered: script that parses living docs (rejected — brittle, counts without judgment), local web app (rejected — live re-parsing buys little), Cowork live artifact (deferred), no dashboard (rejected — prototype passed the "changes a decision" test on real data).
- Decision: Claude appends a metric snapshot to `Dashboard/snapshots.json` and regenerates `Dashboard/Dashboard.html` after every briefing. Five RAG indicators, no composite score. Design locked in `Dashboard_Template.html` (settled via Claude Design session, ported to a dependency-free template — the `Pandoc_Ref.docx` pattern). Rules in `Dashboard/README.md`; workflow in CLAUDE.md.
- Follow-up: 3 days of history backfilled 07-13→07-15; trends carry low confidence until ~2 weeks. Revisit at the 30-day EOS review: is it read, does it change decisions, cut if not.

### 2026-07-14 — EOS: Sean reporting via on-demand written updates; analytics and model standards added
- Owner: Darryl
- Decision: Sean progress reporting is on-demand written Teams/email updates (`Reference/Sean_Update_Standard.md`), not a recurring meeting. Added `Reference/EOS_Analytics_Standard.md` (weekly analytics block, monthly pass, quarterly retro), `Reference/EOS_Model_Selection_Standard.md` (Claude model per EOS function), and `09_Impact_Ledger.md` (wins capture).
- Follow-up: first Sean update on request; first analytics block with the next weekly briefing.

### 2026-07-15 — WAM/ALM metrics definition revised to include existing-customer growth
- Owner: stated on the WAM actuals deck (Finance-led with Brad Stevens as Business Sponsor); decision authorship to confirm.
- Decision: original ALM target focused on net-new revenue and was read as new-logo acquisition; the metric now includes incremental sales growth from existing customers using the ALM tool. Under the revised definition: YTD ~$16.7M vs $19M objective (87.23% by June).
- Chief of Staff note: this is the substantive fix to the underreporting problem, but redefinition can read as goalpost-moving at Engel/Hasting level. The narrative must state the rationale explicitly (original metric measured the wrong thing, not performance rescued by re-measurement).

### 2026-07 — Asset/product uploads transition to EUDM-driven processes
- Owner: Akansh Gangil / ADM team
- Decision: Future asset and product uploads move to EUDM-driven processes.
- Source: ADM connect with Natalie (transcript)
- Follow-up: **Correction 07-13 (Darryl via ChatGPT library): DDP/EUDM connection COMPLETED Jul 3.** Remaining work: MDM structures, supplier data, terms, metadata, stewardship, complex-asset sources — these external dependencies increasingly drive scale and timing.

### 2026-07 — Weekly renewal-notification email design finalized
- Owner: WAM product team
- Decision: CSV attachment model plus escalation distribution strategy.
- Source: ADM connect with Natalie
- Follow-up: **Go-live paused pending formatting (Darryl, 07-13); notification function lands in WAM Jul 17.** Backup distribution list needed before go-live resumes. Prior "Jul 9 go-live" from Copilot evidence was stale. **Update 07-16: rollout now tentative 2026-08-03 under the MVP1 release gate (see Decisions Approaching).**

### 2026-07 — entroCIM Q2 release target held at July 20 — **RELEASED, CLOSED 2026-07-22**
- Owner: entroCIM leadership (Ron Snyder, David Blondel)
- Source: Daily Stand Up
- Follow-up: Release week now; go/no-go discipline. **07-17 (M365 evidence, Daily Stand Up 07-16):** two open items surfaced this close to the date — (1) data-table UI standardization approach undecided (Ron Snyder/David Blondel — move away from current MUI pattern vs. hold), (2) Dell PME connector work blocked on external Dell support/credentials. Neither evidenced as release-blocking yet, but both warrant a direct go/no-go check rather than assuming resolution.
- **Closed 07-22 (Darryl, field note): release 3.1.12.13 is complete and approved by Ron Snyder and the DCOE**, confirmed by email from Subhendu Mohapatra. This resolves both the release-outcome silence tracked across three evidence packages (07-20/21/22) and the separate DCOE compliance-hold entry below — that entry's "hold" reading was superseded by the actual approval. Data-table UI standardization and Dell PME connector status not independently reconfirmed; treat as closed with the release unless raised again.

### 2026-07 — Docker Hub / EntraSim approved with medium-risk posture; Risk 1660 retained at medium
- Owner: Security review participants
- Source: Cybersecurity CSRA: AEA-1792 Docker Hub - PROD
- Follow-up: Stable; monitor only.

## Decisions Approaching

### 2026-07-23 — New product concept for AOP 2027 funding proposal
- Status: Approaching — **initiative in Discovery (Phase 0 initialized 07-23 PM)**
- Owner: Darryl
- **Governing documents (07-23 PM):** three files in `Products/CSS_Device_Lifecycle_Ideation/00_Charter/` (Updated Ideation Thesis, Cowork Master Prompt, Joint Execution Plan) now govern the initiative. They supersede `Deliverables/2026-07-23_New_Product_Ideation_Charter.md`, the addendum/workplan deliverable, and the first ChatGPT prompt draft. Working thesis: **Device Lifecycle Assurance** managed service; firmware assurance as candidate wedge, not presumed winner. Initiative workspace: phase folders + `05_Operating_Record/` (Source_Index, Risk_and_Dependency_Log, Research_Log) — working detail only; this entry remains the master record.
- **CHECKPOINT 1 DECIDED 07-23 (Darryl): shortlist confirmed as recommended.** Umbrella adopted: **Connected Device Assurance as a Service**. Modules A (Firmware+Config Assurance, 3.75) and B (Remote Health+Recovery, 3.65) advance to Phase 2 together; Module C (Refresh/EOL) embedded as commercial signal, not sold standalone; Module D (Cyber-Hygiene) initially held — **amended same day (Darryl): D promoted into Phase 2 deep-dive scope.** Rationale: cyber is table stakes; major OT/IoT industry gap; multi-vendor deployments leave unowned risk. Reference point: Nozomi Networks Arc (competitor/analog/possible partner). Phase 2 distinguishes hygiene *visibility* (candidate MVP table stakes) from hygiene *remediation* (later sequencing); build/partner/buy assessed per capability gap (incl. SecuriThings/Viakoo as partner-vs-compete question). Basis: `01_Phase_1_Divergence/Consolidated_Shortlist.md`. Note: ChatGPT Phase 1 run skipped the divergence contract (no pain inventory/concept portfolio); divergence covered by Claude first pass — recorded as known limitation.
- **Update 07-23 PM (Darryl, corrected same day): "The container IS the product."** Product ships as a container; three deployment modes (refined 07-23): on-prem SFF Ubuntu PC, on-prem customer server, or fully remote (Azure container over Airwall L3 link, no on-prem compute). Arcbeam (entroCIM) connects/clusters distributed instances; Airwall also provides secure remote management of on-prem instances. Pods = internal entroCIM capability, not packaging. Basis: entroCIM containerization investment underway (CSRA-approved Docker work). Governing docs amended (Thesis + Master Prompt). Build/partner gap: container estate/fleet management. Phase 2 verify: containerized Airwall, Nozomi licensing, Navigator packaging rights, Arcbeam clustering readiness (Ron Snyder), SFF hardware.
- **Update 07-23 PM: ChatGPT Phase 2 dossier received and reviewed** (`02_Phase_2_Dossiers/`). Content strong; recommends **Connected Camera Assurance** MVP (hygiene visibility base + health/recovery primary + Axis-first firmware; Mode 3 land, Mode 1 expand; Hanwha qualifying). Two corrections by Claude (`Phase_2_Review_Timeline_and_Architecture.md`): (1) dossier's Aug gate dates unrealistic — gate actions reframed as the *content of the funded 90-day validation* (Oct–Dec 2026), pilot Q1–Q2 2027; thin pre-AOP lane defined (incident-data pull, Arcbeam/Ron Snyder conversation, pilot shortlist, RFI drafts). (2) Architecture diagram rebuilt per Mermaid standards (executive overview + controlled-action sequence). Citation-verification pass pending in Claude research track.
- **Next gate: Checkpoint 2 — MVP composition freeze (~08-14).** Sequence: ChatGPT Phase 2 run using the standalone `00_Charter/CSS_Platforms_2027_Phase_2_Brief.md` (created 07-23 PM after the first run against the older Master Prompt section missed the mark — decided state now consolidated in one brief) + Claude cited research → merge → Darryl selects MVP composition (modules, deployment modes, manufacturers).
- **Update 07-23 PM (Darryl, Phase 0 Q&A):** (1) **AOP input deadline: 2026-08-31.** Backward schedule: Checkpoint 1 ~08-01, Checkpoint 2 (freeze) ~08-14, Sean endorsement week of 08-17, BU/AOP package ~08-28. (2) Launch manufacturers: Hanwha + Axis (cameras), Dormakaba + HID (access control), Cisco (IT equipment); plus device-inclusion rule — open telemetry protocol + available API puts a device in play. (3) **Firmware-rights dependency reclassified:** per-vendor qualification hurdle, not a concept-level gate (market precedent: third-party solutions exist); formal Supplier Relations/Legal outreach deferred, resolved per vendor during Phase 2 validation.
- **Strategic driver (Darryl, 07-23 — internal only, never in outbound artifacts):** the goal of this entire project is to define a new tool to build for 2027 that assures his team stays intact and delivering value for Wesco. Team continuity through funded, valuable work is the underlying objective; outbound framing stays on customer/commercial value.
- Context: Darryl has been challenged to propose new product ideas for the CSS Platforms portfolio. Ideation charter and first pass drafted (Cowork session 07-23): `Deliverables/2026-07-23_Ideation_First_Pass.md` (first-pass scores not comparable to new scorecard; re-score at merge).
- Options considered: firmware assurance service (lead, scored 32/40), device cyber-hygiene service, install-base refresh/EOL intelligence, remote device health monitoring, productized Airwall access.
- Recommended path (first pass): staged "Device Lifecycle Assurance" service line — firmware-assurance MVP (Airwall + Azure entroCIM pod, 2–3 camera lines, first revenue 2027), expanding into WAM-fed refresh intelligence (hardware pull-thru) and later hygiene/monitoring modules. Audience sequence: Sean first, then Dirk/AOP.
- Risk of waiting: AOP 2027 cycle timing; concept needs research validation (competitive scan, firmware redistribution rights, Airwall commercial terms) before a funding conversation.
- Forum where this should be decided: Sean 1:1 (concept endorsement), then BU/AOP process.
- Follow-up: phased joint workplan agreed 07-23 (`Deliverables/2026-07-23_ChatGPT_Addendum_and_Joint_Workplan.md`) — Phase 1 diverge (ChatGPT run + Claude merge → shortlist), Phase 2 deep dives + Claude competitive research → concept freeze, Phase 3 funding package → Sean 1:1, Phase 4 AOP submission. Checkpoint outcomes logged here. Make-or-break gate to start immediately: manufacturer firmware redistribution rights (informal supplier-relations/legal question, don't wait for Phase 2).

### WAM MVP1 notification rollout — production readiness gate
- Added: 2026-07-16 (M365 evidence: WAM Product discussion + license-expiration thread)
- Owner: Akansh Gangil / Natalie Marquardt; Darryl sets the gate standard
- Context: rollout shifted to tentative **2026-08-03** while feedback lands. Gate items: final supplier exclusion list (Natalie), cancelled-line cleanup validated (one-time tested; recurrent needs scheduler design), sender/format changes, SharePoint/FAQ live. Separately: EUDM license-order feed is delivered but **manually triggered daily** (clustering issues) — automation is not production-grade yet and must be stated honestly in exec framing.
- **Update 07-20 (M365 evidence, WAM Product Backlog Refinement):** cancelled-item cleanup scope sharpened — cancelled ADM items must be removed from the UI and excluded from analytics, exports, search, filters, and renewal views, with a **separate removed/cancelled orders tab**. Still undecided: whether a new "removed" status is needed. Separately, **missing SO dates are blocking license activation** (pending activations, perceived data loss though data remains in the database — bug 7827) and **some UDM records aren't being picked up by the DDP scheduler**; root cause and priority trade-off vs. other sprint items still open. Both are gate items, not yet scoped into the Aug 3 timeline explicitly — confirm with Akansh whether they're on the critical path.
- Risk of waiting: premature/inaccurate notices burn Sales/Sales Ops trust — direct hit to the WAM reset narrative. Missing-SO-date/scheduler gaps compound this: customers may perceive data loss even though none occurred.
- Forum: WAM Product discussion (weekly); WAM Product Backlog Refinement (bi-weekly); Darryl asked Akansh for a one-page gate view.

### DDP/global attributes ownership (DDPTRK-6346)
- Added: 2026-07-16 (M365 evidence). **Ownership decided 2026-07-16 (Darryl, field note):** Akansh owns the global-attribute issue itself (working the GPO/MDM teams to get attributes defined, decided, and worked). David Blondel owns the supplier-relations side — pushing Jarod Booth's team, then the Assortment team, to get data into the system over time.
- **Correction 07-16:** an earlier deliverable (Sean Meeting Brief) mislabeled David Blondel as being "in Jarod Booth's org." David reports to Darryl (confirmed in `06_Stakeholder_Map.md`); he is pushing Jarod's team, not part of it.
- Progress 07-16 (Darryl field note): second Data Requirements meeting didn't happen as scheduled, but Dan Totino called Darryl directly — got Priyambada Dash and Gandhi Subramanian on the line. They will action the 6 attributes in the ticket. Next: sync with the Governance team (dependency creation) — technical and governance classes in parallel. Gandhi will read the ticket and route questions to Dan and Darryl. **Anna Baker has invited Darryl to the Monday DDP Entrance Call** to keep DDPTRK-6346 tracking inside the broader DDP plan.
- Context: downstream impact — product classification, software/hardware differentiation, warranty/subscription handling, notification logic.
- Risk of waiting: reduced — attendance/ownership gap that stalled 07-15 is now addressed with named owners and a standing check-in (Monday Entrance Call).
- Forum: Monday DDP Entrance Call (new — add to `07_Operating_Cadence.md` if it recurs).

### JCI (Johnson Controls) MSP agreement — drive to signature
- Added: 2026-07-16 (Darryl, via chat). Detail filled 2026-07-16 (M365 evidence ingestion — see `Products/JCI_Partnership.md`).
- Status: Approaching — stalled on the agreement, momentum restored at account level. MSP model decided (not reseller) 2026-05-26; final markups blocked on unresolved technical/commercial questions. **07-17: 07-15 meeting transcript received and ingested** — it was a JCI-initiated FY26 review / FY27 growth partner meeting, not a negotiation: none of the 5 blockers or contractual terms were discussed; no contract commitments made. New evidence from it: (a) JCI's account team described the MSP metering model **assuming Wesco continues running/provisioning its own Conductor**, with only a **read-only license-usage agent** added — verbally supportive of the self-host position, not contractual; (b) MSP billing = monthly in arrears on provisioned licenses (vs 12-month prepay today); (c) **Wesco's Conductor/relay Azure migration is already in flight** (2 Conductors, HA) — execution is running ahead of contract, sharpening urgency to paper hosting rights; (d) 443-only connectivity available now, removing the top deployment friction. Full outcomes: `Products/JCI_Partnership.md`. **07-17 PM corrections (Darryl): Wesco is hosting the Conductor as of today; the internal prerequisite is now specific — Wesco Architecture Review Board (WAB) approval of the JCI API connection (metering agent) from the Conductor, not a hosting-model review. Babu Papanna has no JCI/Conductor actions. HA failover is Wesco IT responsibility inside Wesco's Azure IoT subscription (resolved 07-17 PM) — JCI L3 is optional support, not a required engagement. Brian Miller refresh email SENT 07-17; meeting committed week of 07-20 (agenda: hosting redline, 5 open items, new terms, customer flow-down, markup schedule). Framing correction from Darryl's sent email: legal review ongoing since early June, Darryl owed Brian a response — the quiet period was partly Wesco-side. Hosting responsibility settled operationally (07-17 PM): Wesco is the hosting authority — environment owned by Wesco, application owned by Darryl's team; patching/backup/DR/SLA/security addressed. Sole open matrix element: JCI's support obligations to Wesco (L3/escalation/SLA), still owed by JCI. **Value-thesis correction (Darryl, 07-17 PM): the deal's value is the whole MSP licensing flip (consumption billing), with hosting as the enabling change — signature condition now two-part: express hosting rights AND licensing mechanics codified in durable agreement text (not unilaterally changeable Program Materials).**
- Owner: Darryl (driving). JCI: Jonathan Gutierrez (sales/account lead, per evidence), Jeffrey McCorvey (account manager, per evidence), Priya Agarwal (MSP program, per evidence) — roles unconfirmed beyond evidence. Wesco Legal: Brian Miller.
- **Update 07-22 (Darryl, field note): Brian Miller meeting held** (calendar showed "JCI Legal review - restart," no transcript retrieved by M365 evidence — field note fills the gap). Walked the full agenda: (1) hosting rights redline — expressly permit Wesco to host/manage the Conductor and MSP infrastructure in Wesco Azure, JCI limited to API-based license monitoring plus authorized support access; open question whether the existing "Non-Hosted JCI Offerings" definition covers this or new language is needed, and whether it belongs in the agreement body or the Order exhibit; (2) reconfirmed status of the 5 open items (hosting rights, API/license-monitoring data scope, customer agreement requirement, final MSP pricing, named JCI counsel contact); (3) new-terms position on indemnity, liability carve-outs, unilateral changes, non-cancelable orders, price-increase notice — flagged where Wesco accepts, counters, or needs Darryl's business input; (4) customer-contracting terms — JCI Customer Agreement flow-down and the termination-for-convenience prohibition, assessed against Wesco's standard customer terms, with the point that in Wesco's hosted model customers never interact with Airwall directly, so the customer-terms structure needs to accommodate that; (5) target markup schedule and what's needed from JCI. **Outcome: Brian will have a final markup ready to send to JCI next week.**
- **Update 07-24 (M365 evidence): markup target date now specific — 2026-07-31.** See Key Product Due Dates.
- Context: JCI's Airwall / Conductor / Relay product set connects Hosted entroCIM to customer-site systems and equipment, enabling live telemetry. Relationship momentum slipping per Darryl.
- **Update 2026-07-17 (agreement review summary, provenance unconfirmed):** the draft's Hosted vs Non-Hosted JCI Offerings structure may support a Wesco-hosted model but does not expressly grant Wesco the right to host/self-manage the Conductor or Relays — blocker #1 is now a confirmed drafting gap. Review also surfaced ~10 additional contractual issues (flow-down, unilateral changes, indemnity, liability carve-outs, non-cancelable orders, competing-offerings restriction, etc.). **Sharpened decision: does Wesco make express Azure self-hosting rights (JCI limited to API license monitoring + Wesco-authorized support access) a condition of signature?** Prerequisite: Cloud Architecture validation (unconfirmed). See `Deliverables/2026-07-17_JCI_Airwall_MSP_Agreement_Review_EOS_Update.md`.
- Options considered: (1) push JCI now for the 5 outstanding blockers (Azure hosting rights, API/license monitoring, customer agreement requirement, JCI counsel contact, pricing) and target signature on the current draft; (2) escalate through JCI account leadership if response lag continues; (3) hold at current stall — not recommended, see risk.
- Decision / Recommended path: Re-engage Jonathan Gutierrez + Jeffrey McCorvey this week on the outstanding blockers; in parallel confirm with Brian Miller whether legal issues are now limited to hosting + customer-agreement language, and confirm status of the Wesco Cloud Architecture review that was supposed to receive JCI's hosting proposal.
- Risk of waiting: Hosted entroCIM's site-connectivity path (live telemetry) depends on this partner stack; continued drift leaves the agreement unsigned indefinitely and weakens the Managed Services delivery story.
- Forum where this should be decided: No standing forum currently in `07_Operating_Cadence.md`. Recommend Darryl establish one (JCI check-in with Gutierrez/McCorvey) once 07-15 meeting outcomes are captured.
- Follow-up: Full detail, contacts, and dated next-steps list in `Products/JCI_Partnership.md`. Darryl to supply 07-15 meeting notes via `08_Field_Notes.md`.

### ServiceNow Field Services integration path
- Added: 2026-07-16 (M365 evidence)
- Owner: Ron Snyder (intake) / Sean Comunale (Brady approval, backlog position); Darryl tracks the approval milestone only
- Context: dev-environment path identified; production needs licensing + Infosys coordination; ServiceNow team backlog significant.
- **Update 07-22 (M365 evidence, Teams chat w/ Ron Snyder): Ron replied "Not yet" on ServiceNow module access** — still not unblocked; timing update Darryl asked for on 07-21 has not landed.
- Options: dev-only POC; production licensing path; customer-environment pattern.
- Risk of waiting: low near-term — customer ticketing-integration requests stay uncommitted.
- Forum: decision returns when intake approval + backlog position land.

### CSS Platforms product strategy: team/org structure and resource alignment
- Added: 2026-07-13 (field note)
- Owner: Darryl (proposal) → Sean McCloskey (endorsement/decision)
- Context: Broaden team scope across entroCIM, WAM, CSS AI backlog, and Navigator; align resources and costs with portfolio priorities; Product/Platforms/Deployment org structure.
- Forum: Sean meeting — **moved to Thu 2026-07-16** (Sean at HQ through Wed). Also covers Akash/Dirk WAM meeting prep.
- Risk of waiting: budgeting and ownership ambiguity persists across the expanded portfolio; this is the upward-alignment move the baseline flagged as missing.
- Next action: confirm meeting acceptance; prepare strategy one-pager.

### AI roadmap direction — SkySpark 4, Wooly AI, Copilot enablement, DP AI Initiative
- Added: 2026-07-13 (All Hands). **Updated 07-14: forcing function arrived** — leadership dissatisfaction with AI pace stated at Agile Staff **by Sean McCloskey** (attribution corrected 07-14: loop notes credited Maddy Taylor, but Sean was using her computer while traveling with her); Sean asked Darryl to analyze AI ideas his team could own (CSS synergies). Blocked on Power BI access (Ankit).
- **Update 07-21 (Darryl, SkyFoundry release email): SkySpark 4.0.6 shipped — first production release of 4.0, including the beta of Woolly**, SkySpark's own LLM agent harness (Anthropic/Gemini/OpenAI, customer-supplied API keys, free during beta). This turns the "Wooly AI" thread in this decision from a roadmap mention into a real, usable tool Darryl's team already has access to (sent directly to Chad Steger, Keith Bishop, Ron Snyder). **Correction 07-21 (Darryl):** the release notes' "no guardrails or plan mode" language is SkyFoundry describing a beta-stage feature gap (plan mode/guardrails are on their near-term roadmap), not a disclosed defect — access itself follows the standard SkySpark/entroCIM model, scoped to whatever the signed-in user's own account is already permitted to do. The transcript-sharing default is governed by a documented, one-step `shareTranscript` flag. Practical note for any pilot: use an appropriately scoped account and turn off `shareTranscript` if testing against anything customer-adjacent — normal setup discipline, not an open governance gap. Full detail: `Products/SkyFoundry.md`.
- **Timing note:** this lands the same day as Darryl's Sean meeting on the AI-project-ideas analysis — directly relevant input, not a coincidence to let pass unused.
- Owner: **Darryl** (team-assignment analysis); broader governance still unassigned.
- Forum: response to Sean — today's meeting (07-21) is the venue; CSS AI backlog already on its agenda.
- Risk of waiting: AOP planning proceeds without credible AI commitments; separately, an ungoverned Woolly pilot (default transcript sharing, no guardrails) could create a data-governance incident before any team formally decides to adopt it.
- **Update 07-22 (M365 evidence, Agile Staff Meeting 07-21): AOP planning accelerated — alignment deadline now Aug-21, and product investments require stronger business-case justification.** New commitment: Darryl to coordinate AOP alignment meetings with Lisa, Brad, and Gregg O'Brien before that deadline (Gregg O'Brien is a new name — not yet in `06_Stakeholder_Map.md`; "Lisa" and "Brad" read as Lisa Orton and Brad Stevens by context but not independently confirmed in this evidence — apply name-collision caution before treating as settled). Separately, GitHub Copilot enablement is now blocked by Vibe Guard compatibility concerns — a distinct AI-tooling governance thread alongside the Claude-code WAB track (see entries above/below). **Correction 07-22 (Darryl, field note): the IDP/WAM item is not a third governance path — "WOB" was a naming error for WAB, and IDP integration is not approval-blocked (see corrected entry above). AI-tooling governance is now two open threads (Claude-code WAB, GitHub Copilot/Vibe Guard), not three.**
- **Update 07-23 (Darryl, field note dated 07-22): Darryl owes Sean product ideas plus an AI-researched needs analysis for CSS** — this is the concrete deliverable that came out of the 07-21 Sean meeting's "analyze AI ideas" ask (see the linked commitment below, and the related entry two rows down). Separately, SkySpark/AI Council and WAM Data Challenges evidence (07-22/23) shows the AI-POC thread moving from problem-definition talk toward actual scoped pilots — first forward motion on the long-stalled "AI adoption governance" pattern.

### Which AI projects Darryl's team takes on
- Added: 2026-07-14 (Agile Staff)
- Owner: Darryl, at **Sean McCloskey's** request (attribution corrected from Maddy Taylor)
- Next: get Power BI access → shortlist by capability fit + CSS stakeholder synergy → bring candidates, dependencies, and realistic team ownership to Sean (Wednesday if access arrives in time).

### WAM/entroCIM executive reset framing
- Added: 2026-07-14 (Agile Staff). **Status 07-17 (Darryl): framing complete — being presented today to John Engel.** Darryl will report back if the presentation surfaces anything new.
- Owner: Darryl + **Sean McCloskey** (attribution corrected from Maddy Taylor); Brad Stevens sign-off
- Context: WAM financial-benefits underreporting left negative impression with John Engel and Rob Hasting. "True reset" requested by Sean; interest/pipeline slide question for Friday's Brad Stevens meeting.
- Progress 07-14 PM: pipeline slide approved by Brad Stevens + Nate ($32M, matches Dirk MBR); entroCIM update bullets in Engel deck. **Correction 07-15 (Darryl): that slide covers the entroCIM business only.** WAM financial actuals handled by Finance (YTD ~$16.7M vs $19M objective, 87.23%); Darryl's WAM contribution = completion/summary of the Update slide.
- Risk of waiting: resolved pending today's Engel presentation outcome — watch for any new reaction/follow-up from Engel or Hasting.
- Note: apply Benefits_Realization_Standards — the reset must separate realized capability (Jul 3 go-live) from planned benefits; the original impression likely came from exactly that confusion.

### Complex-build asset attribute path (post-ACT: WMX vs VAS vs CPQ)
- Added: 2026-07-14 (VAS Roadmap meeting). Updated 2026-07-15 (M365 evidence): gap **formally identified** — WMX lacks serial/MAC/complex-build capability "through at least 2028" absent action. Escalated to High on Watch List.
- Owner: Akansh Gangil / Sudhi Rao; **roadmap authority: GPO = John Barlolotti** (Steve Leslie delegated the GPO role for WMX to him, per Darryl 07-17 — Steve remains a participant, not the decision authority).
- Goal (Akansh's framing): track shipped-hardware asset details — asset tag, MAC address, serial number — including parent-child/finished-goods relationships, surfaced to customer/integrator on the Strev platform; must align with overall DDP strategy.
- Agreed decision path: (1) Akansh → Steve Leslie + Sid Sarna (WMX solution architect, Dir. Enterprise Applications): does WMX capture serial/MAC for complex builds? process + gap understanding; (2) bring in Alan for detail/opinion; (3) GPO buy-in for roadmap — now routes through John Barlolotti; (4) user buy-in (Troy Doyle) — Sudhi: users are the strongest lever but establish limitations first.
- **Update 07-17 (Darryl): follow-up on WMX scheduled Wednesday (2026-07-22) with Sid Sarna and Steve Leslie.** Target: decision path complete by end of July.
- Next action: Wednesday 07-22 follow-up; confirm whether John Barlolotti (new GPO) needs to be brought into that session or a separate one for roadmap buy-in.
- Library lesson applies: validate source-data fitness before funding integration.

### Supplier attribute data ownership (RACI)
- Added: 2026-07-14 (ADM connect + Vendor Data meetings). Updated 2026-07-15 (M365 evidence): vendor master-data strategy advanced — agreement to append new attributes and engage suppliers by revenue priority — but this is process progress, not an ownership decision. Third consecutive forum without a named accountable owner.
- Owner: **not finalized** — spans Supplier Relations, Data Governance, product content, WAM/ADM
- Risk of waiting: supplier data stays incomplete/unmanaged — direct hit to WAM quality, renewals, tax attribution, benefits realization. This is the "data-model alignment unowned" pattern now concrete.
- Next action (Darryl, 07-15): name a decision forum and date — none currently assigned in `07_Operating_Cadence.md`.

### Support-model realignment — scoped 07-15
- Added: 2026-07-13 (All Hands). **Clarified 2026-07-15 (Darryl):** entroCIM team owns product support — SLA, effort, progress tracking, and pricing feedback to sales. The Managed Services piece will most likely be owned by CSS/TSS (not Darryl's team). Scott Dunn is delivery-focused; Amy Aguirre is not in Darryl's org (parallel to Nathan Kehr for WAM, with her own WAM delivery team).
- Remaining decisions: (1) formalize CSS/TSS ownership of Managed Services — outside Darryl's team; his role is confirming, not owning; (2) define the product-support ↔ Managed Services interface (escalation path, SLA boundary, pricing inputs); (3) internal CX-app ownership (first alignment attempt failed — Adam Slingerland leading redo with Keith Bishop/Prady, per Chad's handoff).
- Risk of waiting: reduced — the ownership shape is now understood; residual risk is the undefined interface surfacing as customer inconsistency (FRBNY is the live example).
- Forum: (1) confirm CSS/TSS ownership when the MS conversation next surfaces at CSS level; (2)+(3) entroCIM Leadership Collaboration once Adam's internal CX alignment lands (post-coverage window realistically).

### entroCIM showcase environment strategy
- Owner: Ron Snyder / David Blondel
- Options: continue current showcase vs. separate development project vs. migration-process reversal.
- Scope note (07-15, Darryl): this is the **demo environment** — not tied to the Jul 20 product release. Drop release-deadline framing.
- Risk of waiting: recurring unresolved topic across multiple sprint/release reviews; drags demo-readiness and team attention.
- Forum: entroCIM Backlog Deep Dive or Showcase recurring — needs a decision date.
- Status: Open. **07-13: NOT decided at Leadership Collab (Darryl confirmed).** 07-15: Teams message SENT to David/Ron — open-ended ask to discuss Showcase at Friday's (Jul 17) call: "any unresolved issues or decisions we need to make to make sure JG and Mike are moving?" Deliberately light: Darryl allows a decision may already have been made and not documented. Execution sits with Jason Ganiatsas (Application Engineer) and Mike Reed (Business Analyst), both reporting to David Blondel (confirmed 07-15). Expect resolution or a dated decision path out of Friday's call.

### Strev QA integration path (workaround vs. root-cause fix)
- Owner: Strev/Revnue + WAM engineering
- Risk of waiting: HIGH — blocking testing, SOW release validation, production readiness. Open since at least 2026-07-02.
- Escalated 07-14: Darryl → Sunny Sharma (founder), in-thread. Fix date requested within a day or two; Darryl decides workaround-vs-fix this week once the date lands.
- **Update 07-21 (M365 evidence, single-source, names unconfirmed):** Strev QA environment reported operational and APIM integration initiated (Chandana Buduru, Violet Moyer, with Akansh Gangil). Potentially resolves the blocker, but per pilot closure discipline this is **not** treated as closed from Copilot evidence alone — confirm directly with Akansh before updating status. Same day, a separate Strev-side risk surfaced (see new Watch List entry: invoice/Microsoft-suspension risk) — do not let one thread's good news mask the other's.

### PaaS-02 / entroCIM SSO authentication gap (new 2026-07-21) — **RESOLVED 2026-07-22**
- Owner: IAM/platform teams; Ron Snyder and Babu Papanna in the loop
- Added: 2026-07-21 (M365 evidence — Babu Papanna Teams chat; SAML configuration request thread; Migration Readiness Check meeting 07-20)
- Context: PaaS-02 migration completed successfully, but SSO is not functional on the new environment due to metadata/domain alignment. Part of the broader Quest-to-Azure migration track (Watch List — Sept 1 target, previously "on track"). **Update 07-22 (M365 evidence): specific symptom now evidenced — SAML response returning Username:null.** Narrows the fault to claims/attribute mapping rather than broad metadata mismatch; still no fix date.
- **Closed 07-22 (Darryl, field note): SSO is fixed and working, verified by the team and by Darryl personally.** No fix-date chase needed; downgrade from Watch List.
- Forum: Migration Readiness Check; raise directly in the Darryl–Ron 1:1.

### entroCIM release process — DCOE compliance hold (new 2026-07-22) — **RESOLVED 2026-07-22**
- Owner: unconfirmed — likely Ron Snyder's org and/or Balachandar Murali (DCOE & entroCIM Weekly forum owner)
- Added: 2026-07-22 (M365 evidence — Daily Stand Up)
- Context: evidence states entroCIM release process is on hold pending DCOE compliance evidence and reviews. **Possible explanation for the entroCIM Jul 20 release (3.1.12.13) outcome silence now three consecutive evidence packages running (07-20, 07-21, 07-22)** — worth testing directly with Ron rather than continuing to treat it as a pure evidence-coverage gap.
- **Resolved 07-22 (Darryl, field note): the "hold" read was not a block — release 3.1.12.13 is complete and approved by Ron Snyder and the DCOE**, confirmed by email from Subhendu Mohapatra. See the entroCIM Q2 release entry above (Decisions Made) for the closure record.

### AI-enabled workflow governance — WAB approval gate for IDP (corrected 2026-07-22)
- Owner: Akansh Gangil (IDP integration value/scope); Scott Frost (governance contact)
- Added: 2026-07-22 (M365 evidence — IDP/WAM Process Review)
- **Correction 07-22 (Darryl, field note): "WOB" was a naming error — it should read WAB (Wesco Architecture Review Board), the same board already tracked for the Claude-code and JCI API-connection approvals. There is no separate WOB body; retire that naming caution.**
- **Correction 07-22 (Darryl, field note): IDP integration is NOT blocked by WAB approval.** The team is working on the value case for IDP integration and which document types it covers; Akansh Gangil owns this. Re-scope from "governance-blocked" to "scoping in progress" — remove from the AI-governance escalation framing below.
- Context: IDP/WAM AI-document-extraction POC requires re-validation against current supplier documents before integration decisions proceed.
- Risk of waiting: value case takes longer to land if document-type scope isn't prioritized; no longer an approval-gate risk.
- Forum: IDP/WAM Process Review.
- Next action: Darryl to set up an MDM attribute progress follow-up with the MDM team (committed 07-22, still open); Akansh to bring value/document-type scope to the next Process Review.

### GitHub Copilot enablement — blocked by Vibe Guard compatibility (new 2026-07-22)
- Owner: AI leadership stakeholders (unconfirmed beyond evidence)
- Added: 2026-07-22 (M365 evidence — Digital Products / Agile Staff Meeting)
- Context: GitHub Copilot access blocked by Vibe Guard compatibility concerns. Distinct thread from the IDP/WOB governance item above and from the Claude-code WAB approval track — three separate AI-tooling governance questions now open at once.
- Options: SOP update vs. tooling change.
- Risk of waiting: developer productivity impact; AI-pace dissatisfaction (Sean, already tracked) compounds if multiple AI-tooling paths stall simultaneously.
- Forum: Digital Products / Agile Staff Meeting.
- Next action: security direction needed before a path is chosen.

### VOS/CPQ supplier PO handling — release 3.4.2 (new 2026-07-21)
- Owner: Sean McCloskey and portfolio team
- Added: 2026-07-21 (M365 evidence — Digital Products Portfolio Review, additional detail beyond the 07-20 entry)
- Context: integration design question for release 3.4.2 — include supplier PO information handling now vs. defer/workaround.
- Options considered: include now vs. defer/workaround (per evidence; dependency, testing, and backflow impacts not yet detailed).
- Risk of waiting: release delay or rework if the decision lands late.
- Forum: Digital Products Portfolio Review (cadence/owner still unconfirmed — see existing entry in `07_Operating_Cadence.md`).

### Dell ServiceNow/Freshdesk support workflow redesign (new 2026-07-21)
- Owner: unconfirmed — evidence infers Operations leadership
- Added: 2026-07-21 (M365 evidence — Three Amigos chat)
- Context: current Dell support workflow described as manual and unscalable. Directly relevant today: the Dell Limerick alarming escalation (see Watch List) is live evidence of this gap, not a hypothetical.
- Options: continue current workflow vs. redesign/integrate.
- Risk of waiting: customer experience degradation compounds with each new Dell escalation.
- Forum: none assigned yet — recommend folding into the existing "ServiceNow Field Services integration path" decision above rather than tracking as a separate initiative, given the overlap.

### Renewal-notification attribution model
- Owner: Akansh Gangil
- Options: continue manual attribution vs. automate via future DDP linkage.
- Risk of waiting: manual effort accumulates; low near-term risk.
- Forum: ADM connect with Natalie.

### WAM data challenge remediation approach
- Owner: WAM leadership group (Darryl chairs the forum)
- Status: problem-definition sessions active; no remediation decision yet. **Update 07-23 (M365 evidence, WAM Data Challenges 07-23 08:00): first forward motion — session moved from problem definition toward AI/data-filtering POCs, AI Council review, and asset-data ROI focus.** Darryl committed to review the AI pilot with Shawn and present it to the AI Council; Nitin Pandey's team to run small POCs on automated part identification; Neil asked for a direct benefits/ROI report on WAM. Darryl also owes: sharing the automated-part-ID output with the team, and discussing a needed license with Shawn and Merwan.
- Risk of waiting: data foundation is the recurring theme under most WAM risks; workshops without a decision deadline can run indefinitely. Downgraded slightly — this session produced named next steps and owners rather than another discussion-only pass, but none of it is a remediation decision yet.
- Forum: Hold — Problem Definition & Brainstorming WAM Data Challenges (weekly, Darryl-owned). First session (out of many) with concrete deliverables — watch whether the next session ships them or resets to discussion.
- **Update 07-24 (M365 evidence): direction sharpening — deprecate third-party classification APIs, pursue an IDP + semantic-search + supplier-data-enrichment approach instead.** Owner for Council approval: AI Council / Keyur Patel / Shubhayu RoyChoudhury (per evidence; roles unconfirmed). Darryl owes: reconnect with the IDP team on expanding extraction capability, and review AI Council prep materials before the approval meeting (Nitin Pandey asked for this). No date evidenced for the approval meeting — flag as TBD in Key Product Due Dates. Separate team risk surfaced same session: large historical ADM bug backlog parked without disposition, and single-point dependency on Natalie Marquardt for supplier-data collection — both worth a capacity/ownership conversation, not just a data-strategy one.

### FY27 AOP resource allocation — Build vs. COGS
- Added: 2026-07-24 (M365 evidence — entroCIM FY27 AOP package + Teams chat with John Erickson)
- Owner: Darryl, with John Erickson and finance stakeholders
- Context: FY27 AOP demand-collation template and CSS_Platform_Team.xlsx resource file delivered — this is the planning-cycle mechanics feeding the Aug-21 AOP alignment deadline and Aug-31 AOP input deadline already tracked under the AI roadmap / Device Lifecycle Assurance entries above. Options: Build vs. COGS allocation model and capability-investment mix.
- Risk of waiting: planning-cycle delay; misalignment between capacity model and financial targets going into the Aug-21/Aug-31 gates.
- Forum: not yet assigned — natural fit is the same Sean McCloskey AOP track. Don't run this as a separate thread from the Aug-21 alignment meetings already committed with Lisa, Brad, and Gregg O'Brien.
- Next action: Darryl to align financial goals, capacity model, and capabilities with John Erickson.

### QPM 3.4.3 / Charlotte go-live — cross-team release commitments (CPQ, Oracle, OMS)
- Added: 2026-07-20 (M365 evidence — Digital Products Portfolio Review)
- Owner: Kiranmai (task owner per Loop notes) with CPQ, Oracle, and OMS teams; Anna/John named on Oracle capacity review. Roles unconfirmed — new names, not yet in `06_Stakeholder_Map.md` with confirmed reporting lines.
- Context: QPM 3.4.1 complete; 3.4.2 focused on WMX integrations and customer-care connection; **3.4.3 carries the nested finished-good capability required for the Charlotte go-live** and is not yet committed by CPQ, Oracle, or OMS. Oracle capacity/requirements review also outstanding.
- Options considered: not yet specified in evidence — task is to obtain commitments and run the capacity review, not a scoped options set.
- Risk of waiting: Charlotte go-live readiness is exposed to three external teams' commitment timing with no confirmed dates yet.
- Forum: Digital Products Portfolio Review (cadence to confirm — not yet in `07_Operating_Cadence.md`).
- Follow-up: request a one-page 3.4.3 dependency map (owner, commitment date, risk status) from Kiranmai; disambiguate "Anna" and "John" against existing stakeholder-map entries (Anna Baker/Anna Thornton; John Engel/John Barlolotti) before attributing further actions to them.
- **Update 07-27 (M365 weekly evidence, Digital Products / Agile Staff Meeting + Digital Products Portfolio Review 07-20/21): status worsened — notes state the team is "significantly behind" on 3.4.3, with a decision expected at an upcoming report-out call.** Apparent owners named more specifically this cycle: **Sudhi Rao and Anna Baker**, target to finalize requirements and CPQ/QPMSupport alignment in the **first week of August**. Second open question: how a 3.4.3 delivery-date shift affects dependent Digital Products commitments — not yet assessed. **Name-collision note:** this evidence gives "Anna Baker" with surname (Loop notes, decision-maker inferred) — this may resolve the 07-20 "Anna" ambiguity, but treat as probable, not confirmed, until corroborated independently; her existing tracked scope (DDP/MDM, Monday Entrance Call) doesn't obviously overlap with QPM ownership.
- Risk of waiting (updated): Charlotte go-live exposure is now a schedule problem, not just an unconfirmed-commitment problem — "significantly behind" is a harder signal than the 07-20 read.

### WAM/ADM operational hardening plan — sequencing and gate scoping
- Added: 2026-07-20 (verbose meeting dump, WAM Product Backlog Refinement — filed as `WAM_Product_Backlog_Refinement_Problems_Work_Plan_2026-07-20.md`; exec summary in `Deliverables/2026-07-20_WAM_Operational_Hardening_Executive_Summary.md`)
- Owner: Akansh Gangil / WAM-ADM team (execution); Darryl sets the gate standard and sequencing expectations
- Timing (Darryl, 07-20): the bugs surfaced after the 07-03 DDP/EUDM integration go-live — the most recent production update — and the teams have been finding and defining them since. The Backlog Refinement session consolidated that discovery work.
- Context: Backlog Refinement was a data-quality stabilization session — seven problem areas with work plans: (1) cancelled-order contamination (one-time hard delete + three tracks: data-layer status, UI exclusion, audit tab), (2) reported data loss (working conclusion: data intact, visibility defect — bug 7827), (3) license activation failures (null start dates / missing SO dates the main driver), (4) duplicate record creation in lower envs, (5) filter scalability (~50K records; architecture review before implementation), (6) ADM database growth (archival strategy needed), (7) end-user matching normalization. Items 1–3 overlap the MVP1 Aug 3 gate (tracked in that entry above).
- Open decisions: (a) **sequencing conflict — the one-time hard delete of cancelled records precedes the audit tab (Track C); without a pre-delete snapshot/export, traceability is lost, contradicting the plan's own intent**; (b) whether a new "removed" status is added to the data model (Tracks A/B depend on it); (c) which items are on the Aug 3 critical path; (d) named owners/dates per track — not yet in the record.
- Risk of waiting: hard delete runs unaudited; "data loss" perception hardens with Sales Ops (Natalie/Debbie Hunter) before the intact-data narrative is placed.
- Forum: WAM Product Backlog Refinement (bi-weekly) + the one-page MVP1 gate view requested from Akansh — recommend expanding that gate view to cover cleanup sequencing, activation fixes, and scheduler investigation.
- Evidence note: transcript/Loop-sourced; speaker attributions (Akansh, Krishnanunni) unconfirmed per evidence discipline.

### WAB approval for Claude code — AI-enabled assortment/QPM tooling
- Added: 2026-07-20 (M365 evidence — Digital Products Portfolio Review)
- Owner: Prasada / Maddy (per Loop notes)
- Context: Portfolio review flagged a task to take Claude code through Wesco Architecture Review Board approval "this Friday or next Friday" to enable assortment-tool and QPM usage, with possible board showcase.
- Risk of waiting: AI-enabled assortment/QPM development slips if approval isn't sequenced against the named Friday target.
- Forum: Digital Products Portfolio Review.
- Note: distinct WAB approval track from the JCI API-connection WAB item above — do not conflate the two Architecture Review Board items.

### CMP (Cellular Management Platform) — where does the tool reside?
- Added: 2026-07-20 (Darryl, Brad Stevens conversation)
- Owner: Darryl + Sean McCloskey (portfolio placement); Brad Stevens driving the business side
- Context: CMP manages any Wesco-sold product carrying a cellular plan (SIM). Built by Fanny Scargle (Dir. Business Development, UBS; cellular SME) with Merwan's team; the tool is the mechanism. Brad Stevens may pull Fanny into his team to own the business side, which leaves tool ownership/residence open.
- Risk of waiting: if Fanny moves before placement is discussed, the tool's home gets decided by default rather than by portfolio logic.
- Forum: Sean McCloskey discussion (Teams message raising it drafted 07-20).

### Connected Safety — take on as a digital product?
- Added: 2026-07-20 (Darryl, Brad Stevens conversation)
- Owner: Darryl (recommendation) → Sean McCloskey
- Context: Sean Gregg's replacement not yet named; program in limbo until then. Question: does Darryl's team take Connected Safety on as a digital product? Not the biggest business, but needed across customers and divisions. Pros and cons acknowledged, not yet enumerated.
- Options: take on as digital product / leave with the successor org once named / hybrid (platform support without program ownership) — to be worked before the Sean discussion.
- Risk of waiting: low near-term (program is parked), but limbo has no owner and no clock; a successor hire could foreclose the option.
- Forum: Sean McCloskey discussion (same message as CMP).

### entroCIM commercialization model — short-term payback vs. strategic scale-up (new 2026-07-22)
- Added: 2026-07-22 (M365 evidence — updated commercialization/competitive-landscape materials: `Wesco_entroCIM_Commercialization_2026-07-22_v5`, `Wesco_entroCIM_Competitive_Landscape_Report_2026-07-22_v2`)
- Owner: not yet assigned — materials name this as the central leadership decision
- Context: updated decks frame entroCIM as a live test of Wesco's services-led commercialization model. Path A: treat as a short-term payback problem. Path B: strategic scale-up with a sponsored-access/incubation structure, aligned incentives, and dual metrics (realized + option value).
- Options considered: Path A (short-term payback) vs. Path B (strategic scale-up with incubation contract, pilot accounts, scorecard, incentive model).
- Risk of waiting: materials flag "slow starvation" — option value erodes and side-of-desk selling continues if no owner is named.
- Forum: not yet assigned — natural fit is the Sean McCloskey / Akash Khurana track already carrying WAM/entroCIM reset and portfolio-strategy discussions.
- **Update 07-24 (Darryl + full-document analysis):** both source files analyzed directly (correcting the 07-22 evidence read — the companion is `Wesco_entroCIM_Commercialization_Report_2026-07-22_v5`, a 27-page report, not a separate "Competitive_Landscape_Report v2"; the landscape content is inside it). Built with **Nathan Kehr and Michael Wassil**; audience Engel/Khurana/McCloskey; **status: internal draft v5 — not sent until Mike Wassil sends.** Darryl classifies them as market positioning for entroCIM. Full summary: `Products/entroCIM/Wesco_entroCIM_Commercialization_Summary_2026-07-22_v5.md`. Detail now on record: Path B = incubation contract (12/18/24-month milestones, sponsored access, default-include, dual metrics); the ask is explicitly enablement (external MarComm refresh + internal incentive alignment), not headcount/capital; seven executive decisions listed with recommended directions, owners to be assigned; 90-day staged pilot with gates; report deliberately sets no deadline. Two framing-consistency flags for Darryl (deck's "no new capital" vs. the $1.44M AOP sustaining ask; Path B growth language vs. AOP "frame as sustaining" rule) — see the summary file.
- Next action: name a decision owner and executive sponsor; this pairs directly with the existing "entroCIM commercial performance vs. 2026 objectives" watch item — don't let the two threads run separately. Nearer-term: the send itself (Mike Wassil) is the gating event — until sent, no leadership decision clock is running.

### Mapbox token exposure remediation (new 2026-07-22)
- Added: 2026-07-22 (M365 evidence — Daily Stand Up 07-22)
- Owner: Ron Snyder / Boris (security) / Priyatosh Patra / Shubham Kumar Singh
- Context: a Mapbox token was exposed in git history. Immediate revocation could break customer-facing maps; team prefers a coordinated rotation with a grace period over relying on git-history filtering alone.
- Options: rotate with a grace period and customer-impact plan vs. immediate revocation vs. git-history filtering only.
- Risk of waiting: security exposure persists the longer rotation is deferred; conversely, an uncoordinated revocation breaks customer map functionality.
- Forum: Daily Stand Up; raise directly in the Darryl–Ron 1:1 if no rotation plan lands this week.
- Next action: Ron to confirm rotation timing and customer-impact plan with security (Boris).
- **Update 07-27 (M365 weekly evidence, Daily Stand Up 07-22): sharper detail on the constraint — existing tokens are customer-facing, and revocation could disrupt maps specifically for on-premise customers who haven't received a pod update.** Stated team preference: token rotation over git-history filtering, coordinated with security. Commitments: Ron to meet with Boris on the leaked-token issue; Priyatosh Patra to rotate the exposed token and send the updated token to Boris. No rotation date confirmed yet — still open, not resolved.

### entroCIM release governance tightened — DCOE-driven production controls (new 2026-07-27)
- Added: 2026-07-27 (M365 weekly evidence — Daily Stand Up 07-21)
- Owner: Ron Snyder
- Context: distinct from the already-closed 07-22 DCOE compliance-hold entry (that one was about release 3.1.12.13 specifically and is resolved/approved). This is a **forward-looking process change**: production code now requires tagging, two reviewers, a GitHub commit, conventional-commit format with JIRA issue numbers, and documented testing evidence before release. Ron stated the standup-cycle release was on hold pending this sign-off discipline.
- Risk of waiting: inconsistent adoption across teams could leave DCOE evidence gaps recurring rather than resolved; a related open decision (shared UI component/helper repo and release-documentation strategy across front-end teams — Joseph Kusnir, Priyatosh Patra, Michael Pieschel, David Blondel, Ron Snyder) could keep release evidence inconsistent if not aligned to the same standard.
- Forum: Daily Stand Up (entroCIM).
- Next action: confirm with Ron that the new controls are applied consistently, not just discussed once; watch whether the shared-component/repo decision lands on the same governance model.

### Dell/Wesco service management process — handoff model across Freshdesk and ServiceNow (new 2026-07-27)
- Added: 2026-07-27 (M365 weekly evidence — Teams chat with Syed Jamshed Zaidi 07-24; Dell Service Management Process meeting 07-27)
- Owner: Syed Jamshed Zaidi, with Darryl, Scott Dunn, Adam Lazare; Dell-side participants unconfirmed
- Context: current Dell support workflow is manual and unscalable (this is the same underlying gap flagged 07-21 as "Dell ServiceNow/Freshdesk support workflow redesign," now with a scheduled forum). Evidence states two recent Dell issues did not enter the established Wesco support process promptly — an operating-model gap, not a single-ticket problem. Directly relevant: this is the same team carrying Dell Limerick and Dell Non-DC HQ dashboard escalations (Watch List).
- Options: continue current workflow vs. document and redesign the current-state process (Dell internal support, Freshdesk, ServiceNow escalation, handoffs, ownership, closed-loop communication).
- Risk of waiting: customer experience degradation compounds with each new Dell escalation; this consolidates the prior "ServiceNow Field Services integration path" and "Dell workflow redesign" entries into one forum.
- Forum: **Dell Service Management Process** — met 2026-07-27 (today); add to `07_Operating_Cadence.md` once cadence/owner confirmed.
- Next action: bring the proposed current-state process map and the two recent process misses (Limerick, Non-DC) as concrete examples.

### Product ownership model shift — two-tier structure (GPO peer + Claude Design owner)
- Added: 2026-07-27 (M365 weekly evidence — Digital Products / Agile Staff Meeting 07-21; decision-maker Inferred as Sean McCloskey)
- Owner: Sean McCloskey (per evidence, Inferred — not independently confirmed)
- Context: product ownership model shifting toward a two-tier structure — a GPO peer role and a Claude Design owner role — with training and license distribution not yet resolved. Affects how product requirements, customer sessions, design artifacts, and handoffs get owned going forward; touches hiring/staffing expectations.
- Risk of waiting: the AI-enabled development pilot and new ownership model could stall or land inconsistently across teams without a license/training plan.
- Forum: Digital Products / Agile Staff Meeting (weekly).
- Next action: confirm this reading directly — evidence marks the decision-maker as Inferred, and it materially changes product-owner role expectations across the portfolio.

### AI-enabled development pilot approved — Copilot + Claude Design, Orlando workshop
- Added: 2026-07-27 (M365 weekly evidence — Digital Products / Agile Staff Meeting 07-21)
- Owner: Sean McCloskey (direction), Digital Products leadership (execution)
- Context: a pilot for a fully AI-enabled development cycle using GitHub Copilot and Claude Design was approved, including a planned two-day Orlando workshop for portal requirements and design (feeds the QPMSupport portal initiative). Moves AI adoption from concept into a live delivery-method experiment — connects directly to the standing "AI adoption governance + team assignment" watch item and to Darryl's owed deliverable (product ideas + AI-researched needs analysis for Sean).
- Risk of waiting: Claude Design license distribution and product-owner training are unresolved — the pilot could proceed unevenly across teams without them.
- Forum: Digital Products / Agile Staff Meeting.
- Next action: Sean owes Darryl's team (and Dj Vaughn) additional Claude Design licenses — track under Commitments Owed to Darryl (05).

## Decisions Being Avoided or Stalled

### WAM/DDP/EUDM data-model alignment
- Appears across WAM leadership meetings, data-challenge workshops, and ADM planning for 30+ days without resolution. No single named owner for the alignment decision itself.
- Chief of Staff note: this is the strongest "repeated discussion, no decision" pattern in the baseline.
