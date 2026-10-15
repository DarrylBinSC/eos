# Impact Ledger

> Added 2026-07-14. Running record of wins, benefits realized, and problems closed. The EOS tracks risks, commitments, and decisions well; this file closes the gap on successes. Claude adds entries during briefings and sessions; entries feed Sean updates (`Reference/Sean_Update_Standard.md`) and benefits narratives. Realized-vs-planned discipline applies: only evidenced outcomes go here, labeled with impact.

**Last Sean update drafted:** 2026-09-09 (`Deliverables/Exec_Briefs/2026-09-09_Sean_Update.md`), covering the delta from 2026-08-19 through 2026-09-09. Not yet sent; sending is Darryl's call. Prior draft (`2026-08-19_Sean_Update_v2.md`) was also never sent.
**Last Sean update sent:** none yet.

> **Cadence installed 2026-08-19.** The Sean update now generates with the first weekly briefing of each fortnight whether or not it is requested, per `CLAUDE.md` weekly briefing format §19. Before this, 41 entries had accumulated here with 32 marked "Communicated: not yet" and zero updates produced in the ledger's life. Report the delta since the drafted date above, not cumulative history, and move that date forward each time a draft is produced.

## Entry Format

`### YYYY-MM-DD — [Win]` with: what happened, business impact, evidence source, where it has been communicated (Sean update / deck / not yet).

## Entries

### 2026-09-17 — entroCIM cross-functional quality standard authored and delivered

- **What happened:** Ron Snyder delivered the entroCIM Team Quality Standard v2.0, commissioned by Darryl. Eleven sections covering the full delivery organization — Development, Application Specialists, Deployment/Integration/Graphics, IT Architecture, Product/Support/Leadership — with a complete-outcome definition, handoffs treated as shared control points, a readiness test before commitment, role-level expectations, and four operating checklists.
- **Business impact:** the delivery organization now has a single written definition of a complete customer outcome and of what a handoff must carry. It is a prerequisite for any claim that cross-team quality is managed rather than assumed, and it was produced by the development director rather than imposed on him.
- **Why it is recorded here with a hard boundary:** what is realized is that the document exists and is good. **Nothing is adopted.** No rollout owner, no binding to Jira or release gates, no first application, no measurement. This is intent, not control. Do not carry it into a Sean update or any upward narrative as evidence that quality is under control, and do not pair it with the `03` 2026-09-10 development-resource argument until it has produced observable output — the standing rule in `CLAUDE.md` on mechanisms that are declared executed and then quietly do not run applies to this document directly.
- **Evidence source:** `entroCIM_Team_Quality_Standard_v2.0_2026-09-17.pdf` and assessment at `Products/entroCIM/entroCIM_Team_Quality_Standard_2026-09-17.md`.
- **Communicated:** not yet.

### 2026-09-14 — Ford accepted the Premier Support package as complete and closed all open issues

- **What happened:** Darryl confirmed (explicit, 2026-09-14) that the Ford team accepted what Wesco submitted as complete and closed all of Wesco's open issues on their side. This covers the Premier Support SOW scope finalization and the Windows Server 2019 compatibility confirmation Ford had requested ahead of a 2026-09-13 development-server upgrade.
- **Business impact:** closes out the highest-urgency open customer thread in the portfolio. The Windows Server item was carried Critical and ownerless for five days against a fixed customer date and was resolved without escalation. Scope exposure on the SOW is bounded: optimization services excluded from base scope, on-premises administration placed with Ford, secure remote access made an explicit delivery dependency.
- **Why it counts as realized, with one boundary:** the customer-facing commitment is met and confirmed by the customer. It does **not** evidence that the UDAC platform baseline was audited (`05` B62) or that delivery capacity was validated against the accepted scope (`05` B69). Report the acceptance; do not report the trust gap as closed.
- **Evidence source:** Darryl, direct, chat, 2026-09-14. Supersedes the 2026-09-09 weekly position and the 2026-09-14 evidence package, which returned nothing on Ford.
- **Communicated:** not yet. Candidate for the next Sean update as a closed exception rather than as activity.

### 2026-09-08 — Quest-to-Azure migration: seven of eight environments complete
- Only dev-01 remains after Wesco IT mounted the dev-03 volume to unblock dev-03. All customer-facing environments are now migrated.
- Impact: **realized.** Closes out customer-facing migration exposure entirely, on top of the TCCC-specific completion logged below. Named credit: Babu Papanna (led the migration, per Chad Steger's public recognition), Ron Snyder.
- Source: entroCIM Backlog Deep Dive, 2026-09-08 (verbatim transcript). Communicated: not yet.

### 2026-09-02 — IDP/ADM proof of concept validated with WAB approval
- The IDP-to-ADM integration architecture and POC output were validated, and the integration path received Wesco Architecture Review Board approval.
- Impact: **realized on the design gate only.** The approval answers `05` B8 (reconnect with IDP on expanding extraction capability), but production resourcing stalled the same week (Ankit Chadha, capacity constraint) — do not present this as a delivered capability. See `04` new Active row.
- Source: IDP/WAM Use Case Discussion, 2026-09-02 (verbatim transcript). Communicated: not yet.

### 2026-09-02 — entroCIM customer education formalized into a repeatable, sellable process
- A course catalog, signed-SOW requirement, four-week readiness review, and two-week scheduling lead time were established. Foundations is live now; APAC Sales and Disney have received delivery; Tiles Gridboard is in development for October.
- Impact: **realized.** Converts a previously ad hoc training motion into a repeatable commercial process — a durable capability change, not a one-time delivery.
- Source: entroCIM Customer Training Catalog & Process, 2026-09-02 (verbatim transcript). Communicated: not yet.

### 2026-08-27 — TCCC (Coca-Cola) Quest-to-Azure migration completed, ahead of target
- Both target servers (PaaS-03W, PaaS-04W) completed transfer; SAML worked and DNS resolved during cutover. Completed 2026-08-27, ahead of the 2026-09-01 target, closing the migration thread tracked as `05` C6/B50/B51.
- Impact: **realized.** Removes a customer-hosting migration risk on a major entroCIM account and is the fourth demonstrated instance of the Quest-to-Azure playbook holding (after PaaS-05, PaaS-06, and the 08-17 dry runs). No further action requested by Sales.
- Named credit: Chad Steger (confirmation), Babu Papanna, Ron Snyder (after-hours execution).
- Source: `Re: TCCC Fin Migration` (email), `PASS-06 Server Migration Cutover` (Teams channel), weekly M365 evidence 2026-08-24 to 08-31. Communicated: not yet.

### 2026-08-31 — JCI MSP agreement: final legal markup sent to JCI
- Brian Miller's contract review, rescheduled from the missed 2026-07-31 date to Friday 2026-08-28, produced an updated Airwall MSP agreement; Darryl confirmed it was sent to JCI 2026-08-31. Linked customer terms were converted into fixed exhibits and controlling-body language revised where Legal had concerns.
- Impact: **realized as a milestone, not yet as an outcome.** Resolves a pacing stall open since 07-31 on an 8+ month negotiation. Does not yet evidence JCI's response or resolution of the roughly ten remaining contractual issues.
- Source: Darryl, direct, 2026-09-01; corroborated by `RE: JCI OpenBlue Airwall MSP Agreement — restarting legal review; meeting next week` (email), weekly M365 evidence 2026-08-24 to 08-31. Communicated: not yet.

### 2026-08-28 — CDA: sales-leadership engagement secured, next evidence gate set
- Following the executive brief meeting, Chris Mooney (Converging Technologies) and Bill Muczko (Global Enterprise, ~200 Fortune 200 accounts) both validated the customer problem CDA addresses and agreed to help identify two or three pilot accounts before an eight-month 2027 build is committed. Bill Muczko's estimate: roughly 85% of his account base is not managing camera assets effectively today, mostly via spreadsheets.
- Impact: **realized as a validation milestone.** Moves CDA from internal concept packaging into customer-validation planning with named sales-leadership sponsors, without committing build resources ahead of evidence.
- Source: `Connected Device Assurance, follow-up and materials` (sent and received email), weekly M365 evidence 2026-08-24 to 08-31; `06_Stakeholder_Map.md` (Chris Mooney, Bill Muczko entries, added 08-28). Communicated: not yet.

### 2026-08-25 — Quest-to-Azure: PaaS-05 migrated and PaaS-06 SAML restored, DNS follow-ons cleared
- PaaS-05 reported fully migrated and sanity-tested. PaaS-06 SAML login restored after correcting the configuration to send the group name rather than a UUID, verified by logs showing users logging in with projects and connectors healthy. Portman confirmed good on PaaS-06; Oak Grove corrected to PaaS-05 and verified.
- Impact: **realized.** Third independent confirmation the migration pattern holds, after the 07-28 runbook and the 08-17 dry runs. Named credit: Babu Papanna, Shawn Clark, Chad Steger, with Darryl verifying the SAML fix personally.
- Source: `Quest Migration – Weekly Check-In`, `PASS-06 Server Migration Cutover`, weekly M365 evidence 08-25 (second run). **Attribution caveat: both meetings were reported `isMeetingTranscribed:false` in the 08-25 retrieval diagnostic, so this content most likely came from meeting chat rather than a transcript.** Substance is sound; treat verbatim quotes as unconfirmed. Communicated: not yet.

### 2026-08-25 — ADM supplier data: ~5,000 missing records inserted, Exact data 90 to 95 percent present
- About 5,000 previously missing records inserted; the targeted Exact dataset reported roughly 90 to 95 percent complete. Remaining updates depend on the pending-activation fix targeted for the 2026-09-01 release, plus MAC ID and end-date cleanup.
- Impact: **partial, realized on the insertion only.** Material progress on the supplier-data onboarding that has constrained ADM completeness since July. Do not upgrade until the 09-01 release confirms.
- **Held back deliberately:** this sits alongside a newly evidenced data-foundation defect — upstream truncation of manufacturer part numbers — which causes ADM to miss orders regardless of how complete the supplier data is. Reporting the percentage without that caveat would overstate the position.
- Source: `ADM connect with Natalie` 2026-08-25, verbatim transcript. Akansh Gangil. Communicated: not yet.

### 2026-08-24 — CDA FY27 AOP input confirmed complete; product P&Ls uploaded
- John Erickson confirmed CDA "is GTG and nothing is needed," and that the reviewed product P&Ls for Ascent/Navigator, entroCIM and WAM were uploaded to the IT/Digital AOP directory.
- Impact: **realized as a submission milestone.** Closes the CDA half of work that ran from the 07-23 ideation charter to a funded submission in roughly five weeks.
- **What this does not evidence is that the AOP submission itself completed** — only the P&L basis and the uploads. Open question at the next closure check.
- Source: Teams conversation with John Erickson, weekly M365 evidence 08-25. Communicated: not yet — candidate for the next fortnightly Sean update.

### 2026-08-17 — WAM/ADM notification suite shipped to production, with two additions beyond plan
- The MVP1 notification capability tracked since mid-July shipped to production this cycle: automated license expiry notifications, notification analytics reporting (new, not previously scoped), and a product-upload fix (underscore support in manufacturer part numbers). Confirmed directly by Akansh Gangil.
- Impact: **realized.** Closes the "confirm with Akansh whether it actually shipped" question the 08-10 entry left open, and the analytics-reporting addition is incremental scope delivered without a corresponding date slip. Downgrades the WAM MVP1 watch row from High to Medium.
- Source: ADM Prod Release Update, weekly M365 evidence 08-17. Communicated: not yet in a Sean update — candidate, since it closes a gap Sales Ops (Debbie Hunter's org) has been watching since 07-16.

### 2026-08-17 — Quest-to-Azure: dry runs completed successfully, cutover now being scheduled
- Dry runs for the Azure cutover completed without issue; Babu Papanna and Chad Steger are named to schedule and execute the official cutover against the Sept 1 target.
- Impact: **realized on the dry run, planned on the cutover itself.** Adds a second, independent piece of direct evidence (beyond the 08-12 dev/prod-moves confirmation) that the migration approach holds under test conditions. C6 stays open until the cutover executes.
- Source: CSS Platforms All Hands Meeting, weekly M365 evidence 08-17. Communicated: not yet.

### 2026-08-17 — Federal Reserve: guide-specification adoption and RFP integration advance pipeline expansion
- Federal Reserve expansion activity advanced through guide-specification adoption and integration into RFP processes, read as a pipeline-expansion opportunity across multiple FRB districts (Nathan Kehr).
- Impact: **planned, not yet realized.** No booked pipeline change yet; this is a positioning/process win that widens the addressable FRB opportunity beyond the existing FRBNY and SASTEC St. Louis relationships. Do not fold into the approved $32M pipeline figure without a Nathan Kehr/Brad Stevens sign-off, per the existing approval pattern for that number.
- Source: CSS Platforms All Hands Meeting, weekly M365 evidence 08-17. Communicated: not yet.

### 2026-08-12 — Sprint 37 completion held at 94% despite unplanned work; Quest-to-Azure approach validated on dev and prod
- entroCIM Backlog Deep Dive (08-12): Sprint 37 landed at 94% completion despite unplanned work absorbed mid-sprint (David Blondel, stated outright). Separately, Darryl and Syed Zaidi directly confirmed the Quest-to-Azure migration approach is validated based on successful dev and production moves — the first non-inferred confirmation on the long-open C6 production-readiness question.
- Impact: **realized, on both counts.** Sprint discipline holding at 94% under disruption is a data point for the same operating-maturity story as the 07-28 sprint-completion entry (81%→91%→93-95%). The migration-validation statement is Direct evidence from Darryl himself, not an inference from a meeting existing — upgrades the Quest-to-Azure "on track" read from inferred to confirmed for the approach, though C6 itself stays open until the remaining environments are done.
- Source: entroCIM Backlog Deep Dive, daily M365 evidence 08-13 (covering 08-11/08-12). Communicated: not yet.

### 2026-08-10 — Nozomi partnership: MNDA received, sandbox/license access offered
- The MNDA with Nozomi has been received, and Nozomi has offered sandbox and license access pending execution — the first concrete step on the partner-licensing questions (Guardian container licensing, multi-customer terms, Arc attach-only) sharpened during the 07-28 CDA node-stack session.
- Impact: **planned, not yet realized.** Enables technical evaluation once executed; does not itself constitute a signed partnership or commercial term. Upgrade this entry when the MNDA is executed and sandbox access is actually in use.
- Source: weekly M365 evidence 08-10 ("[NOZ|WES] MNDA/Next Steps" email). Communicated: not yet.

### 2026-08-06 — i3 Alliance Agreement: architectural and IP exposure found and closed before signature
- Legal's ask was narrow: review "one technical section" of the i3 Alliance Agreement. The section, Section 8, turned out to determine whether entroCIM is the system of record on Alliance projects or a downstream consumer of i3's data model, and to create a perpetual, uncapped IP exposure through the interaction of §§8.1, 6.2, 12.4, 16.6, and 15.2. Neither is visible from the clause language, which is why the legal review of Section 6 returned no issues. Output: a twelve-item redline, edits inline in the document, a clause-level memo, and a plain-language rationale for the team.
- A second finding came out of Darryl's own question during the session rather than the analysis: customer data integrated into entroCIM. As drafted, Section 8 would have had Wesco promising i3 a routing obligation over data Wesco has no independent right to route, putting the i3 agreement in direct conflict with Wesco's own customer agreements on sub-processors, residency, and disclosure. The Client Data definition added at §8.9 closes it, and protects i3 equally.
- Impact: **realized as risk avoided, not as revenue.** Nothing is signed and nothing is conceded. The measurable outcome is that a binary architectural decision affecting entroCIM's position on every Alliance project, and an uncapped IP exposure with no expiry, were identified before signature rather than after, with a documented negotiation floor and a contractual fallback (§8.7, drafted by i3) if i3 will not move.
- Also worth carrying: the same structural pattern now appears in two partner agreements, JCI and i3, where the operative obligation lives in material the counterparty can change unilaterally. Recommended as a standing review question on any partner or reseller agreement (`03`, 08-06).
- Source: `CDK- 0728.26Master -WESCO revision 7-30.docx`, clause text and tracked changes; Comment 115. Detail: `Products/i3_Alliance.md`. **Communicated: sent to Legal ~2026-08-11** (confirmed by Darryl 08-25, closure check). The redline, the clause-level memo and the plain-language rationale are with Brandon Thompson and Nikos Minas. **This win is banked, not pending** — the record carried it as "pending send" for two weeks after it had gone. Legal has not responded in roughly two weeks (C-i3-1, C-i3-2).

### 2026-08-05 — WAM quarterly roadmap delivered; leadership's standing ask answered
- The WAM Backlog Deep Dive deck (presented 08-06) delivers a quarterly roadmap with named milestones and an outcome arc: license visibility → coverage beyond Core and Anixter part numbers → reps see what's expiring → one complete coverage view. This directly answers the 07-30 leadership ask for a roadmap with named milestones in place of continued problem-definition sessions, a forum that had run at least five sessions without a decision output.
- Alongside it: UAT testing of the Notification to Sales Rep suite is complete, and two defects raised after the 07-03 go-live are closed (post-EUDM-integration behavior, ADM UI performance under data volume). Q1 and Q2 roadmap phases are marked complete.
- Impact: **realized, as an artifact.** Converts the longest-running "discussion without decision output" item in the portfolio into something reviewable, and gives WAM an executive-usable roadmap for the FY27 AOP window and the Dirk Naylor / Sales Operations audience. Deck: `Products/WAM/WAM_Backlog_Deep_Dive_2026-08-05.pdf`; transcription and executive read: `Products/WAM/WAM_Roadmap.md`.
- Caveats held deliberately, not counted as realized: the 08-10 release date is a stated target rather than a confirmed release, and the deck's automated-sync claim is contested against the July record (see `04`).
- Source: deck provided by Darryl, 08-05 session. Communicated: used in the 08-05 Lisa Orton brief; not yet in a Sean update.

### 2026-08-04 — TCCC cyber-risk: SO-V.06.2 remediated, leaving one open control
- The log-retention control (SO-V.06.2), previously past its planned deadline, was moved to Remediated by TCCC's own reviewer (Yadu Nandan M). Six of seven controls in the OneTrust risk treatment are now closed.
- Impact: **realized.** A marquee-account compliance exposure narrows from a broad finding set to a single named gap (OT-V.02.1, ISA/IEC 62443 certification evidence). That remaining item is a product-certification question rather than an evidence-submission one, so this is a genuine narrowing, not a near-finish.
- Source: daily M365 evidence 08-05 (Re: Cyber Risk Assessment Results: Wesco entroCIM). Communicated: not yet.

### 2026-08-04 — WAM SOW Batch 2: the major license-type defect resolved and packaged
- Revnue reported the "Missing default License Type in list" defect resolved and included in the 08-05 release package; Batch 2 deployed to WAM QA. Two remaining defects deferred by the vendor to the next release.
- Impact: **partial, planned not realized.** The defect fix is evidenced; production deployment is not. The release also slipped from 08-03 to 08-05, so this is progress against a moved date. Upgrade this entry when production is confirmed.
- Source: daily M365 evidence 08-05 (Re: Connect for bugs - SOW 3). Communicated: not yet.

### 2026-08-04 — Louvre Abu Dhabi: production access, server setup, and the occupancy KPI formula landed
- Shawn Clark, Adam Slingerland, and Pradyumna Umarji confirmed to have production-server access with the server set up; a usable occupancy KPI formula established (David Ochoa, with Elias Brewer and Valli Poornakumar credited); a route to resolving the missing AQI and people-counting data identified.
- Impact: **realized on the enablement items.** Worth recording precisely because the same evidence reports the snag list stalled for two weeks. The team is not idle; the closeout is unsequenced. Reading only the stall would misattribute the problem to effort rather than to plan and ownership.
- Source: daily M365 evidence 08-05 (Re: IoT Consolidation Platform - Project Deployment Meeting). Communicated: not yet.

### 2026-08-04 — SkySpark 4 connector and application migration reported complete
- Migration complete with testing nearly finished and pod setup underway (Nihar Ranjan Sahu).
- Impact: **partial.** Removes a platform-version dependency ahead of the Woolly/SkyFoundry evaluation track. Testing completion not yet confirmed.
- Source: daily M365 evidence 08-05 (Daily Stand Up 08-04). Communicated: not yet.

### 2026-08-02 — TCCC cybersecurity remediation: five controls closed in one week
- Five of seven OneTrust risk-treatment controls (SO-V.09.1, SD-V-HRD.03.2, SD-V-HRD.02.1, IAM-V.05.2, IAM-V.05.1) confirmed remediated by TCCC's own reviewer (Yadu Nandan M); Mike Reed also submitted IAM-V.06.2 evidence.
- Impact: narrows a marquee-account compliance exposure from a broad finding set to two named, scoped gaps (SO-V.06.2, OT-V.02.1) — material progress even though the account carries an active technical dispute (AOC connectivity) at the same time.
- Source: weekly M365 evidence (Re: Cyber Risk Assessment Results: Wesco entroCIM; Re: TCCC Hi Risk Items). Communicated: not yet in a Sean update.

### 2026-07-30 — Panama Liberty BACnet timeout resolved after a long-running stall
- The connectivity blocker that had Shawn Clark tagged as backup resource is fixed; work moved directly to submeter onboarding in entroCIM the same day.
- Impact: closes a multi-week technical blocker without executive escalation; frees Shawn Clark's residual load ahead of his architect-role transition.
- Source: weekly M365 evidence (Re: Panama Liberty Project: Run Cable to MDF Room to Sub-Meter). Communicated: not yet.

### 2026-07-29 — BAE MQTT data flowing in the broker; latest build deployed
- Required protobuf connector and track-and-trace pods updated to the latest build; MQTT data visible in the broker for the first time.
- Impact: moves BAE from a connectivity/data-ingress problem to a data-quality/decoding problem — a materially different (and lower-risk) class of issue on a High-severity delivery account.
- Source: weekly M365 evidence (Re: BAE MQTT system). Communicated: not yet.

### 2026-07-31 — FRB SASTEC St. Louis Lab proposal fully executed (second pilot signal)
- All parties completed the Lab proposal via DocuSign, corrected after the earlier Lab/QA mix-up — a likely trigger for a second pilot purchase order.
- Impact: converts a live commercial-risk item (wrong-environment signature) into forward motion, pending PO confirmation and site readiness (see the new St. Louis Airwall watch row — the device is not yet online).
- Source: weekly M365 evidence (Fw: Completed: CW208131 - entroCIM FRB_SASTEC St Louis_LAB May 1 2026_Final.pdf). Communicated: not yet.

### 2026-07-29 — entroCIM architecture slide built and used same day with the DCOE team
- One-page entroCIM high-level architecture slide (two deployment options, Airwall/Arcbeam connectivity, SkySpark platform layering, settled positioning language) built in the Wesco template and used the same day by Darryl to brief the DCOE team (Balachandar Murali) on entroCIM and WAM architecture and roadmap, packaged with the WAM value-chain slide and the entroCIM and ADM/Strev roadmaps.
- Impact: DCOE now has an accurate, current architecture baseline for both platforms; first artifact to state Arcbeam's on-prem services/support role explicitly. Deck: `Products/Architectures_and_Roadmaps_2026-07-29.pptx`.
- Source: Darryl, 07-29 session; deck provided. Communicated: DCOE briefing; not yet in a Sean update.

### 2026-07-28 — entroCIM sprint completion up from 81% to 91% Q2; last two sprints 93-95%
- Q2 average sprint completion improved from 81% (Q1) to 91%; Sprint 36 and the most recent two-week window ran 93-95% completion.
- Impact: evidence of improved planning discipline and backlog governance under David Blondel/Ron Snyder — candidate proof point for benefits realization and team operating-maturity narratives (ties to the knowledge-sharing/definition-of-done watch item).
- Source: Daily Stand Up, entroCIM Backlog Deep Dive, M365 evidence 07-28. Communicated: not yet.

### 2026-07-28 — UWM migration substantially complete; first Quest-to-Azure production server (PaaS-02) moved with a repeatable runbook
- UWM wholesale mortgage server migration completed, in closeout (Syed Zaidi). Separately, PaaS-02 became the first production server officially moved off Quest to Azure, with a documented, repeatable migration runbook now in use for the next servers (Coke servers, replication underway).
- Impact: de-risks the remaining Quest-to-Azure program (Sept 1 target) with a proven pattern; UWM closeout reduces the dual-environment cost once customer sign-off (C5) lands.
- Source: entroCIM Backlog Deep Dive, M365 evidence 07-28. Communicated: not yet. Note: does not itself satisfy C6 (production-readiness validation) — that remains open.

### 2026-07-28 — Strev License Manager Milestone 2 invoice approved
- Milestone 2 invoice approved and progressing to AP payment processing. Distinct from the 07-20/21 invoice-payment risk (INV-2606-00014, resolved 07-21) — a different milestone, no suspension risk attached.
- Impact: continued forward motion on the Strev commercial relationship, alongside the already-improving technical/QA thread.
- Source: M365 evidence 07-28 (Strev Invoice Submission for approval/payment). Communicated: not yet.

### 2026-07-27 — FRB SASTEC St. Louis: entroCIM installed successfully
- Federal Reserve Bank SASTEC St. Louis LAB project: software/licenses delivered via Intralinks 07-16, ongoing support questions transferred to the operations team (Adam Slingerland, Syed Zaidi) 07-21, and **installation completed successfully**, confirmed by Darryl 07-27.
- Impact: federal customer deployment closed out cleanly with support routed to the standing operations model rather than staying on Darryl's desk — a working example of the product-support ownership pattern being formalized elsewhere in the portfolio.
- **Name to reconcile:** Darryl's confirmation names "Jarod from Sastec"; the prior record named the customer counterpart as Jerald Moore. Treat the customer-side name as unconfirmed until validated.
- Source: Darryl 07-27 (register sort); Re: Federal Reserve Bank SASTEC St. Louis LAB Project Follow-Up. Communicated: not yet in a Sean update — candidate.

### 2026-07-27 — EOS restructured mid-pilot: commitment register cut from 39 to 10
- Darryl identified that commitments were being overstated and mis-attributed, diluting focus. Diagnosis found three structural causes: no attribution test at intake, a schema with no Owner column ("Expected By" held a counterparty, not a date), and no single home per fact. A single 07-23 meeting had generated seven items recorded as his personal commitments; six items belonged to other people entirely.
- Action: four-register model adopted (My Actions / Delegated / Awaiting Others / Standing Responsibilities), strict attribution test applied, 62 open items re-sorted, watch list cut from 48 rows to 27 active with a Passive tier, decision log split into a 24-item radar and a 6-item backlog.
- Impact: Register A at 10 items, all dated or triggered. Daily briefing scoped to five sections. Reduces the risk of executive attention being spread across items that were never Darryl's to carry.
- Source: `EOS_Redefinition_Proposal_2026-07-27.md`, `EOS_Register_Sort_2026-07-27.md`. Communicated: internal to the EOS; not a Sean update item.

### 2026-07-14 — entroCIM pipeline slide approved for executive use ($32M, matches Dirk MBR)
- Approved by Brad Stevens and Nathan Kehr; entroCIM update bullets included in Engel deck.
- **Corrected 07-15 (Darryl): scope is the entroCIM business only, not WAM.** WAM financial actuals were handled by others (mostly Finance).
- Impact: consistent entroCIM commercial numbers across executive venues.
- Source: 07-14 field notes / decision log; corrected 07-15. Communicated: Engel deck path; not yet in a Sean update.

### 2026-07-15 — WAM Update slide completed for the WAM actuals deck
- Darryl's contribution to the WAM slides: completion and summary of the Update slide (product: production-ready and sellable, DDP/EUDM complete, MDM/GPO work defined; commercial: selling underway, marketing launch Aug 2026, Managed Services progressing; metrics: ALM target definition revised).
- Context from the Finance-built metrics slide: WAM YTD ~$16.7M vs $19M objective (87.23% attainment by June), tracking ahead of linear target under the revised metric definition.
- Impact: WAM executive narrative now pairs a disciplined update with strong attainment numbers — direct input to the Engel/Hasting reset.
- Source: Darryl 07-15, slides provided. Communicated: WAM actuals deck; not yet in a Sean update.

### 2026-07-03 — DDP/EUDM connection completed for WAM
- Realized capability (not planned benefit): asset/product upload path to EUDM-driven processes live.
- Impact: foundation for install-base visibility, renewal tracking, and the WAM benefits story; remaining scale drivers are external dependencies (MDM, supplier data).
- Source: Darryl correction 07-13. Communicated: reset narrative in progress; not yet in a Sean update.

### 2026-07-15 — Centremis field-access issue resolved (48-hour cross-org RCA)
- The "Zscaler blocking" issue impacting WAM training at the Centremis site (new opportunity) closed in ~48 hours across five organizations (Wesco IT security, Zscaler support, Strev, Managed Services, field team). Root cause: stale group policy / DNS suffix on one field laptop, not the platform. Darryl's structured RCA ask (07-14) split the device issue from transient backend noise and drove parallel workstreams to answer by deadline.
- Impact: customer-facing exposure at a new opportunity contained; platform exonerated (relevant for WAM credibility); corrective actions issued to prevent recurrence (field laptop policy hygiene, pre-site readiness checks, documented diagnosis path).
- Source: full email thread 07-15 + closure note. Communicated: closure to the thread; candidate for next Sean update as an operational-discipline example.

### 2026-07-15 — Operating discipline evidenced: 13-project handoff with named ownership
- Chad Steger's pre-leave handoff covered 13 active projects with named primaries, escalation paths, honest risk flags, and per-project next steps (filed: `Reference/2026-07-13_Chad_Steger_Handoff_Plan.pdf`). A 4-week director absence opens with zero customer-facing ownership gaps.
- Impact: continuity across 8 active customers during the Jul 15–Aug 11 coverage window; direct evidence for the operating-model maturity story in the org discussion with Sean.
- Source: handoff email 07-13, filed 07-15. Communicated: referenced in Sean meeting brief; recognition note to Chad drafted.

### 2026-07-17 — WAM/entroCIM executive reset framing completed, presented to John Engel
- Reset content finished (pipeline slide, entroCIM update bullets, WAM Update slide) and presented to John Engel today, closing the loop opened 07-14 when Sean McCloskey called for a "true reset" after WAM benefits underreporting soured Engel and Rob Hasting.
- Impact: direct repair of a named executive-narrative risk; outcome of today's presentation still pending (Darryl to report back if anything new surfaces).
- Source: Darryl 07-17. Communicated: this is the presentation itself; strong candidate for the next Sean update once Engel's reception is known.

### 2026-07-16 — FRB SASTEC St. Louis lab delivery completed
- entroCIM 3.1.12 software and license packages delivered to FRB SASTEC St. Louis via Intralinks; support path established with Jerald Moore.
- Impact: customer deployment milestone met for an active Federal Reserve pilot; downstream support/installation confirmation is the remaining open thread.
- Source: M365 evidence 07-17 (Re: Federal Reserve Bank SASTEC St. Louis LAB Project Follow-Up). Communicated: not yet in a Sean update — candidate alongside the Centremis resolution as evidence of operating discipline across customer threads.

### 2026-07-20 — QPM 3.4.1 released
- Digital Products Portfolio Review confirmed QPM 3.4.1 complete; 3.4.2 (WMX integrations, customer-care connection) and 3.4.3 (nested finished-good capability for Charlotte go-live) now in planning.
- Impact: modest, evidenced delivery milestone within the QPM roadmap — flagging for completeness rather than as a headline win; the larger story is 3.4.3's cross-team commitment risk (see 04 Watch List).
- Source: M365 evidence 07-20 (Digital Products Portfolio Review_7-20-2026.loop). Communicated: not yet.

### 2026-07-21 — Strev invoice resolved; Microsoft-suspension risk lifted
- Natalie Marquardt escalated and resubmitted invoice INV-2606-00014 multiple times and engaged AP contacts directly; ACH payment made 2026-07-20.
- Impact: removes a vendor-relationship and hosting-continuity risk that surfaced the same day the underlying technical relationship (QA/APIM integration) showed its first signs of improvement — protects both threads at once.
- Source: Darryl 07-21 (commitment status update). Communicated: not yet in a Sean update; candidate given the same-day contrast with the technical thread.

### 2026-07-21 — Dell Limerick alarming issue provisionally resolved same day
- Escalated as the highest-priority Dell customer issue on 07-20; Eli Brewer and Keith Bishop traced a potential rule-roster issue and cleared the error via a forced roster refresh within about a day, now monitoring with added logging.
- Impact: a live customer escalation that landed on an already-stretched coverage team (also carrying BAE and FRBNY) was resolved without dropping either of the other two — direct evidence the 07-15 coverage plan can absorb a third concurrent fire, at least this time. Root cause not fully confirmed; don't treat as a closed loop until the monitoring window passes.
- Source: Darryl 07-21 (commitment status update, quoting the ticket). Communicated: not yet.

### 2026-07-21 — Technical CSM pilot hosted-environment access delivered
- Both access tickets for the Technical CSM and Managed Services pilot (Valli Poornakumar, Leanne Gordon) completed by Eli Brewer same day.
- Impact: removes a stated blocker to Managed Services pilot momentum.
- Source: Darryl 07-21. Communicated: not yet.

### 2026-07-17 (recorded 07-21) — Shorenstein Nashville Moore Building customer response closed
- Sarah Monteleone's password reset and the requested user-list sharing were completed 2026-07-17 — four days before this was corrected in the record. Two prior briefings (07-20, 07-21 AM) carried it as open/overdue based on an evidence-package gap, not an actual delay.
- Impact: customer follow-up was never actually stalled; the EOS's own evidence lag created a false "overdue" read. Logged as a record correction (see `10_Pilot_Feedback_Log.md`) as well as a win.
- Source: Darryl 07-21 (commitment status update). Communicated: not yet.

### 2026-07-22 — entroCIM 3.1.12.13 release shipped and approved
- Release confirmed complete and approved by Ron Snyder and the DCOE, per confirming email from Subhendu Mohapatra. Closes three consecutive evidence packages (07-20/21/22) of outcome silence and the separate "DCOE compliance hold" misread.
- Impact: removes the largest open release-governance question on the entroCIM side; clears the path to normal cadence on data-table UI standardization and the Dell PME connector item (neither reconfirmed as blocking).
- Source: Darryl 07-22 (field note, email evidence). Communicated: not yet in a Sean update.

### 2026-07-22 — PaaS-02 SSO authentication gap fixed
- SAML Username:null issue on the post-migration PaaS-02 environment resolved; verified by the team and by Darryl personally.
- Impact: removes a live customer-login-disruption risk on production entroCIM infrastructure that had been open since 07-20.
- Source: Darryl 07-22 (field note). Communicated: not yet.

### 2026-07-22 — JCI MSP agreement: Brian Miller legal review restarted, markup committed
- Full legal-review meeting held covering hosting-rights redline, the 5 open blockers, ~10 new contractual issues, and customer flow-down terms. Brian Miller committed to a final markup to send to JCI next week.
- Impact: first concrete forward motion on the 8+ month JCI negotiation since the 07-17 email; converts an open ask into a dated deliverable.
- Source: Darryl 07-22 (field note). Communicated: not yet — natural candidate once the markup ships.

### 2026-07-24 — UWM entroCIM server migration cutover completed
- Server migration to the new environment completed (Syed Zaidi/Shawn Clark); customer acceptance sign-off pending before the legacy environment is decommissioned.
- Impact: major customer infrastructure milestone executed cleanly; full benefit (retiring dual-environment carrying cost) awaits confirmed sign-off.
- Source: M365 evidence 07-24. Communicated: not yet.

### 2026-07-21 — entroCIM release governance codified into concrete controls
- In response to DCOE pressure, Ron Snyder translated the compliance requirement into named production-release controls: tagging, two reviewers, GitHub commits, conventional-commit format with JIRA issue numbers, and documented testing evidence.
- Impact: converts a compliance pressure point into a repeatable team-wide standard rather than a one-time scramble; direct evidence of the release-discipline maturity story ahead of any future DCOE review.
- Source: M365 weekly evidence (Daily Stand Up 07-21). Communicated: not yet in a Sean update.

### 2026-07-21 — Quest-to-Azure migration: PaaS-02 cutover completed
- PaaS-02 migrated from Quest to Azure (Ron Snyder, Babu Papanna, Shawn Clark), reconfirmed in this week's evidence alongside the earlier SSO fix.
- Impact: closes a major leg of the Sept-1 Quest-to-Azure migration target with named execution credit; supports the "on track" read with direct evidence rather than inference.
- Source: M365 weekly evidence (Daily Stand Up 07-21). Communicated: not yet.

### 2026-07-21 — WAM/ADM notification path clarified (supplier list, Rhombus exclusion, milestone ingestion)
- Akansh Gangil and Natalie Marquardt converted open WAM/ADM data-quality questions into concrete configuration decisions: supplier list for notification configuration, Rhombus excluded from notifications for the first 30 days pending end-user data, milestone "pink line" ingestion, and cancelled-order validation approach.
- Impact: moves the Aug-3 MVP1 gate from open questions to configured decisions on several fronts at once — direct input to closing that gate cleanly.
- Source: M365 weekly evidence (ADM connect with Natalie, 07-21). Communicated: not yet.

### 2026-07-14 — Strev escalation path activated at founder level
- Darryl escalated the QA/API blockage directly to Sunny Sharma, who is personally working the issue in the field.
- Impact: top execution risk moved from stalled to actively owned at the right level. Outcome (fix date) pending; upgrade this entry when the date lands.
- Source: 07-14 session. Communicated: not yet.
