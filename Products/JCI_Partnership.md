# JCI (Johnson Controls) Partnership
As of: 2026-09-17 (competitive landscape added; partnership content as of 2026-09-01). Original build: built from M365 evidence package (`JCI_MSP_Evidence_2026-07-16.md`, unbounded lookback to 2025-10-07; last evidenced activity 2026-06-08), updated with Darryl's 07-22 field note on the Brian Miller "Legal review - restart" meeting.

## 2026-09-17 — MSP contract designated the baseline for Airwall and Conductor technology use (Darryl direct)

**Darryl, 2026-09-17: the MSP contract with JCI will be the new baseline on Airwall and Conductor technology use.**

This supersedes the recommendation made earlier the same day to record a standalone architectural rationale as the fix for the undocumented dependency. The contract, not a rationale document, becomes the authoritative record of what Wesco may do with Airwall and Conductor, how it is licensed, and who owns what operationally. It replaces a decade of undocumented practice, the pre-acquisition arrangements, and the verbal understandings from the 2026-07-15 JCI partner meeting.

**The operative consequence: a baseline is only as complete as what is captured in it at signature.** Anything still running on practice or verbal understanding at that point sits outside the baseline and stays undocumented. From the current record, the items that must land in the agreement text (or in a referenced document JCI cannot change unilaterally) to be inside it:

- **Licensing mechanics** — pool grant, pay-on-provisioning, monthly-in-arrears, true-down, licences as Wesco's movable asset. Darryl's 07-17 durability requirement: if these live in MSP Program Materials subject to the unilateral-change clause, the commercial flip is revocable post-signature and the baseline does not hold.
- **Express hosting rights** — confirmed drafting gap as of 07-17; the "Non-Hosted JCI Offerings" classification is a possible existing vehicle but has not been established as sufficient.
- **JCI support obligations to Wesco** — L3, escalation and SLA on the Conductor software. Per 07-17 this is the single open element of the hosting/support responsibility matrix, and the only genuinely negotiated content in the Order exhibit.
- **Metering API data scope** — the 07-15 verbal answer ("read-only, see your current license usage") is not a contractual definition.
- The roughly ten further contractual issues tracked in the 07-17 review (indemnity, liability carve-outs, unilateral changes, non-cancelable orders, customer flow-down, competing-offerings restriction).

**Conversion scope (Darryl, 2026-09-17): the entire existing estate converts at signature. Nothing is orphaned on the legacy model.** Read as covering both existing prepaid 12-month licence orders and the older Airwall hardware generations accumulated over roughly a decade, pre-acquisition Tempered-era units included. This makes the commercial flip estate-wide and immediate rather than phased in as legacy orders run to term, and it avoids administering two licensing models in parallel.

Three consequences follow, and all three are baseline-completeness items:

- **The conversion mechanism is a term, not an intention.** Unresolved in the record: unamortized prepaid balances on existing orders, whether existing licences transfer into the pool at current count, eligibility of older hardware generations under the new product definitions, the reconciliation method, and the effective date or conversion window. Outside the agreement text, "no orphaned products" is goodwill.
- **The 2026-05-26 notice-period decisions now carry more weight.** The 60-day product-change and 180-day EOL notice requests are what stop JCI converting legacy hardware generations in and then EOL-ing them out afterwards.
- **WAB approval of the metering API connection becomes path-critical to the commercial conversion**, not just a compliance step, because the agent's first reading is what establishes the conversion baseline in practice. Wesco also needs a clean current licence and device inventory to convert against, relays included (relay software is free, the underlying 300v licence is charged, per the 07-15 transcript). A decade of deployment plus the migration out of the pre-acquisition hosted environment means that count should be verified rather than assumed.

Whether conversion is a saving, neutral, or a cost depends on how much of the estate is provisioned but idle. Worth quantifying before signature; see `03`, 2026-09-17 entry.

**Status of the competitive work produced the same day:** it becomes the **pre-baseline record**. `Products/JCI_Airwall_Competitive_Landscape.md` and `Deliverables/JCI/2026-09-17_JCI_Airwall_Competitive_Analysis.md` document what was true before the contract reset the terms, including why Airwall holds and what the alternatives are. Retain both; do not treat them as superseded, and do not extend them.

**Not yet done, and deliberately deferred:** capturing the signed terms as a structured baseline in this EOS. Premature while the agreement is unsigned and JCI's response to the 08-31 markup has not arrived. Revisit at signature.

## 2026-09-17 Update — competitive landscape cataloged from a JCI-forwarded Gartner survey

JCI asked Darryl to participate in a Gartner survey. One question asked which vendors Wesco considered alongside Johnson Controls during vendor selection and which participated in a POC, listing twelve competitors: Ordr, Akamai, SideChannel, Zscaler, Cisco Systems, Broadcom, Elisity, Illumio, ColorTokens, Onclave Networks, Asimily, Zero Networks, plus "Other."

The twelve are cataloged with per-vendor detail in **`Products/JCI_Airwall_Competitive_Landscape.md`** (new, 2026-09-17). Wesco-lens analysis is in **`Deliverables/JCI/2026-09-17_JCI_Airwall_Competitive_Analysis.md`**.

Findings that bear on this file:

- **The survey list is the wrong market.** Gartner is surveying Network Security Microsegmentation. Wesco uses Airwall for secure remote connectivity from hosted entroCIM into customer networks Wesco does not administer. Eleven of the twelve solve a different problem. Only **Onclave Networks** is a genuine architectural peer, and the most likely real substitutes (Tosibox, a WireGuard-based service, Cisco Secure Equipment Access, conventional site-to-site VPN) are not on the list.
- **No Wesco vendor selection procedure occurred. Confirmed by Darryl the same day.** Airwall has been in the entroCIM deployment architecture for **approximately ten years**; any vendor consideration was completed **before Darryl joined the company**. Darryl separately holds **eight years of direct Airwall experience**, having used it for secure remote network connectivity at **Intelligent Buildings before May 2025**. The survey answer is therefore settled: "Not Considered" for all twelve, and the "if applicable" qualifier applies to the selection-procedure framing itself.
- **The dependency is sole-source, a decade deep, and its rationale is undocumented while the agreement is unsigned.** Risk downgraded to Moderate on Darryl's correction: the architecture has been independently validated at two organizations by an operator with eight years on it, so this is a documentation and currency gap rather than an unexamined dependency. It does not change the recommendation to stay with Airwall; the switching-cost assessment concludes firmly against moving. It does argue for recording the architectural rationale in `Products/entroCIM/entroCIM.md` and holding the durable-licensing-mechanics requirement firmly with Brian Miller.
- **Ordr and Asimily are adjacent to entroCIM's own asset inventory**, not to Airwall. Capability watch item for the product roadmap, not a connectivity competitor.

Recommended survey answer, now unblocked: **"Not Considered" for all twelve**, with a free-text note if the survey allows one, stating that Wesco's use case is secure remote connectivity for a hosted application rather than enterprise microsegmentation, that the platform predates the current ownership by approximately a decade, and that no competitive evaluation was conducted in this tenure.

## 2026-09-01 Update — final markup sent to JCI; current operating model named in the redline

**Darryl confirmed directly, 2026-09-01: "I sent the agreement to JCI yesterday" (2026-08-31).** This resolves the pacing stall open since the missed 2026-07-31 markup date; Brian Miller's contract review, rescheduled to Friday 2026-08-28, produced the deliverable. Corroborating evidence from the 2026-08-24 to 08-31 weekly package: Legal's review produced an updated Airwall MSP agreement ready to share, with linked customer terms converted into fixed exhibits and controlling-body language revised where Legal had concerns — consistent with the hosting-rights and customer-agreement-flow-down issues tracked below. The current operating model the redline is being aligned to: **Wesco-hosted Conductor in Azure, with JCI limited to read-only license metering.** Not yet confirmed: JCI's response, its review timeline, or resolution of the roughly ten additional contractual issues (indemnity, liability carve-outs, unilateral changes, non-cancelable orders, flow-down, competing-offerings restriction). See `03` Decisions Made 2026-09-01, `04`, `05` Archive — Closed (C1).

## 2026-07-22 Update — Brian Miller meeting held, markup coming next week
Darryl met with Brian Miller (calendar showed "JCI Legal review - restart," 07-22 14:00-14:45; no transcript retrieved by M365 evidence — captured via field note). Agenda covered: (1) hosting-rights redline — expressly permit Wesco to host/manage the Conductor and MSP infrastructure in Wesco Azure, JCI limited to API-based license monitoring plus authorized support access; open whether the existing "Non-Hosted JCI Offerings" definition already covers this or new language is needed, and whether it belongs in the agreement body or the Order exhibit; (2) status of the 5 open items (hosting rights, API/license-monitoring data scope, customer agreement requirement, final MSP pricing, named JCI counsel contact); (3) new-terms position on indemnity, liability carve-outs, unilateral changes, non-cancelable orders, price-increase notice; (4) customer-contracting terms — JCI Customer Agreement flow-down and termination-for-convenience prohibition, assessed against Wesco's standard customer terms, with the point that customers never interact with Airwall directly in Wesco's hosted model; (5) target markup schedule. **Outcome: Brian will have a final markup ready to send to JCI next week.**

## Relationship Summary
JCI is a strategic connectivity partner. Their Airwall / Conductor / Relay product set is the mechanism by which Hosted entroCIM connects to systems and equipment at customer sites, enabling live telemetry. Wesco has been negotiating a shift from JCI's standard reseller model to an MSP (Managed Service Provider) model since at least early 2026, reflecting how Wesco actually operates: hosted entroCIM, centrally managed Airwalls, customers do not interact directly with the Airwall platform. Negotiation has been active on and off since October 2025; legal review progressed substantially in late May 2026; evidence shows no activity after 2026-06-08. Darryl held a meeting with JCI on 2026-07-15 — **transcript received and ingested 2026-07-17** (see 2026-07-15 Meeting Outcomes below). The meeting restored account-level momentum but did not advance the agreement itself.

## Technical Role of Airwall / Conductor / Relay for Hosted entroCIM
- **Airwall Conductor**: central management plane for the Airwall network; Wesco's MSP model requires this hosted in Azure under Wesco's control rather than customer-managed.
- **Relay**: routes connectivity between Airwall endpoints at customer sites and the hosted Conductor.
- **Function for Hosted entroCIM**: this stack is the connectivity layer between customer-site equipment/systems and Hosted entroCIM, enabling live telemetry without requiring customers to operate or see the underlying Airwall platform. This is the technical basis for Darryl's 2026-02-27 pushback on JCI's standard reseller terms — Wesco's operating model doesn't fit a reseller-to-end-customer structure.

## MSP Agreement Status and Blockers
**Status: stalled, not signed.** Legal review is substantially progressed but final markups are blocked. **Framing correction (Darryl's sent email, 07-17): the review has been *ongoing* since early June and Darryl owed Brian Miller a response — the post-06-08 quiet period was at least partly Wesco-side, not JCI or Legal unresponsiveness.** Refresh meeting with Brian committed for the week of 07-20 (email sent 07-17).

Decided (2026-05-26 legal review, Darryl + Brian Miller):
- Pursue MSP model, not reseller-only.
- Solution stays JCI-branded (no white-label).
- Restrict affiliate purchasing / order controls on Wesco's side.
- Wesco absorbs tariff impacts.
- Request 60-day product-change notice and 180-day EOL notice from JCI.

**Open blockers** (all evidenced as open as of 2026-05-29 to 2026-06-08, no resolution found after):
1. **Azure hosting rights** — whether Wesco may host Airwall Conductor / MSP infrastructure in Azure is unresolved.
2. **API access and license monitoring** — JCI responded 2026-06-08 with some detail, but the same-date evidence also lists this as still outstanding. Treat as **partially resolved / ambiguous** — confirm directly with Jeffrey McCorvey rather than assuming closure.
3. **Customer agreement requirement** — unclear whether MSP customers need a separate agreement with JCI, Wesco, or both.
4. **JCI counsel / legal contact** — Wesco Legal (Brian Miller) has not been given a named JCI counterpart.
5. **Hosting/support responsibility matrix** — patching, backup, DR, SLA, and support-access ownership between Wesco and JCI is undefined.
6. **Wesco Cloud Architecture review** — hosting proposal was to be routed through internal Cloud Architecture review once JCI's hosting/API answers arrived; evidence does not confirm this review occurred or JCI's answers arrived. **Reframed 07-17 (Darryl): the Conductor hosting is operational in Wesco Azure; the required internal approval is the Wesco Architecture Review Board (WAB) approving the JCI API connection (metering agent) from the Conductor.**
7. **MSP pricing** — final pricing detail not confirmed as received.

## Agreement Structure and Contractual Risk (2026-07-17 review)
Source: agreement review summary provided by Darryl 2026-07-17 (provenance unconfirmed — not marked as Brian Miller work product or 07-15 meeting output; confirm). Agreement remains under legal review, not finalized. Full detail: `Deliverables/2026-07-17_JCI_Airwall_MSP_Agreement_Review_EOS_Update.md`.

- **Structure:** the agreement distinguishes **Hosted JCI Offerings** (on JCI-controlled systems) from **Non-Hosted JCI Offerings** (installed on Reseller or Customer systems). This may support a Wesco-hosted model, but the draft does **not clearly grant Wesco the right to host and self-manage the Conductor or Relays** — blocker #1 is now a confirmed drafting gap, with the Non-Hosted classification as a possible existing vehicle.
- **Wesco preferred position (redline-ready):** Wesco hosts/manages the Conductor and MSP infrastructure in Wesco Azure under Wesco cloud governance, security, monitoring, and support; JCI receives secure API access for concurrent license monitoring plus any support access Wesco authorizes.
- **Additional contractual issues raised (beyond the 5 tracked blockers):** customer flow-down to the JCI Customer Agreement; JCI unilateral changes to MSP Program Materials and customer terms; price increases with limited notice; non-cancelable/non-refundable Orders; prohibition on customer termination for convenience; Wesco L1/L2 support obligations; license-metering API data scope; broad reseller indemnity; liability-cap carve-outs; customer non-payment risk; potential competing-offerings restriction; undefined hosting/support responsibility matrix (patching, backup, DR, SLA, security, support access).
- Nothing in the review contradicts the 2026-05-26 decisions.
- **Value thesis (Darryl, 07-17 PM):** the deal's value is the MSP agreement as a whole — flipping Airwall licensing from 12-month prepaid orders to consumption billing (pool grant, pay-on-provisioning, true-down, licenses as Wesco's movable asset). Conductor hosting is the critical enabling change, not the whole point. **Durability requirement:** the licensing mechanics must be stated in the agreement text or a referenced document JCI cannot change unilaterally — if they live in MSP Program Materials subject to the unilateral-change clause, the commercial flip is revocable post-signature. Raise with Brian Miller as a priority interaction between the new terms and deal value.

## 2026-07-15 Meeting Outcomes (transcript ingested 2026-07-17)
Source: Teams meeting recording transcript, "Partner Meeting: FY26 Review & FY27 Growth Strategy," 2026-07-15, 43m. Attendees: Darryl, Mike Reed (Wesco); Jeffrey McCorvey, Jonathan Gutierrez, Priya Agarwal (JCI). Transcript garbles names throughout (entroCIM → "EntraSim/Intrisim/Intro SIM"; JCI → "BCI"; Airwall → "Agarwal" in places; Nathan Kehr → "Nate Kerr"; Babu Papanna → "Babu Papana"; Louvre → "Liou"; Tempered = legacy Tempered Networks/Airwall) — matched against known portfolio per transcript discipline.

**Character of the meeting: JCI-initiated FY26 review / FY27 growth discussion — not a contract negotiation.** The agreement was touched only in passing ("in the process of trying to get the agreement set up"); none of the 5 blockers or contractual terms were discussed, and no contract commitments were made. Darryl confirmed the MSP model is the direction and said he would "dig into" the agreement.

**Substantive outcomes:**
- **MSP mechanics described by JCI (verbal, not contractual):** JCI adds a **read-only "user agent" to Wesco's Conductor** to see current license usage; billing is monthly in arrears on *provisioned* licenses only (1/12 of annual cost), from a pre-granted license pool; unprovisioned pool = no charge. Contrast with today: prepay 12 months from order fulfillment. Hardware is still purchased/shipped; billing starts at provisioning. Multiple Conductors supported (per-customer separation), each metered, one consolidated monthly bill. Relay software is free but the underlying 300v license is charged.
- **JCI's account team described the MSP model assuming Wesco continues to run and provision its own Conductor** ("the current conductor that you're using... you're provisioning it... the only difference is we're going to put in an agent"). Verbal evidence consistent with Wesco's preferred self-host model — supportive, but not contract language.
- **443-only connectivity confirmed available now** for both tunnel and Conductor management (Priya) — removes the two-outbound-port friction that has been Wesco's biggest deployment obstacle with customer IT. Existing installs left alone; future installs to be configured 443-only.
- **Wesco Azure migration is in flight:** two Conductors in HA replication plus relay, migrating from the legacy pre-acquisition hosted environment to Wesco Azure. **Update 07-17 (Darryl): Wesco is hosting the Conductor as of today.** JCI advised engaging **JCI L3 support** for the Conductor migration/failover process. **Corrections 07-17 (Darryl): Babu Papanna has no JCI/Conductor actions; HA failover is Wesco IT responsibility inside Wesco's Azure IoT subscription — JCI L3 is optional support, not a required engagement.**
- **Internal approval path clarified 07-17 (Darryl):** the hosting decision itself is settled and operational; what requires approval is the **JCI API connection (license-metering agent) from the Wesco-hosted Conductor**, which must go through the **Wesco Architecture Review Board (WAB)**. This replaces the older, vaguer "Wesco Cloud Architecture review of the hosting proposal" framing.
- **Hosting responsibility settled operationally (Darryl, 07-17 PM):** the hosted environment with the Conductor is up and running; patching, backup, DR, SLA, and security are addressed under Wesco governance. **Wesco is the hosting authority — not JCI.** Wesco has taken responsibility for the environment; **Darryl's team owns the application.** The single open responsibility element is **JCI's support obligations to Wesco** (L3/escalation/SLA on the Conductor software), which JCI still needs to provide. Consequence: the Order exhibit documents existing operating reality rather than proposing a model — the only negotiated content is what support JCI commits to Wesco.
- **Ascent data-center POC:** Airwall shipping to Ascent HQ ~Fri 07-17 (Mike Reed); goal is embedding hosted entroCIM telemetry across Ascent's data-center portfolio with API integration back to Ascent's platform. JCI follow-up on the POC tentatively **Aug 15** (Jeff to send invite); Darryl asked for ~a month.
- **Commercial:** Darryl to introduce JCI (Priya) to **Nathan Kehr** re pipeline. No standalone Airwall sales strategy at Wesco — it's baked into hosted entroCIM proposals. JCI floated a parallel reseller angle for enterprise Airwall-to-Airwall deals (no commitment). Sensitive: possible FRB national expansion mentioned — Darryl flagged to keep quiet. Darryl's estimate on-call: entroCIM ~3X pre-acquisition revenue this year.
- Technical note: ~3 video cameras saturate an Airwall — not a video pass-through path.

**What this does NOT change:** all 5 agreement blockers and the 2026-07-17 contractual-risk set remain open. The express-hosting-rights redline is still required — the account team's verbal operating assumption is not a contractual grant.

## Next Steps

| Next step | Owner | Target date | Basis |
|---|---|---|---|
| ~~Capture 2026-07-15 meeting outcomes~~ | Darryl | — | **DONE 07-17** — transcript ingested; outcomes above |
| ~~Assign an owner for JCI L3 support engagement~~ | — | — | **Resolved 07-17** — HA failover = Wesco IT, Azure IoT subscription; JCI L3 optional |
| WAB approval of the JCI API connection (metering agent) from the Wesco-hosted Conductor | Darryl / WAB | Before contractual commitment to API access | Darryl 07-17 |
| Introduce Priya Agarwal to Nathan Kehr (pipeline discussion) | Darryl | ~2 weeks (recommended) | Transcript 07-15 |
| Confirm receipt of Tech Talk 443 video (owed by Jeff, to Shawn Clark + Babu) and push 443-only config standard for future installs | Darryl / Babu Papanna / Shawn Clark | ~1 week | Transcript 07-15 |
| Ascent POC update to JCI | Darryl | ~Aug 15 (tentative invite from Jeff) | Transcript 07-15 |
| Re-engage Jonathan Gutierrez + Jeffrey McCorvey for status on the 5 open blockers (hosting rights, API/license monitoring, customer agreement requirement, pricing, JCI counsel contact) | Darryl | 2026-07-23 (recommended — not evidenced) | Chief of Staff recommendation; evidence gives no committed dates |
| ~~Brian Miller refresh meeting — all open issues back on the table~~ | Darryl / Brian Miller | Wed 2026-07-22 | **DONE 07-22** — meeting held; see 2026-07-22 Update above |
| Brian Miller to send final markup to JCI | Brian Miller | Next week (from 07-22) | Darryl 07-22 (field note) |
| ~~Confirm status of Wesco Cloud Architecture review~~ | Darryl | — | **Superseded 07-17** — see WAB row above (hosting operational; approval scope = JCI API connection) |
| Finalize agreement markups once technical/hosting questions close | Brian Miller (Wesco Legal) | TBD — depends on above | Re: Agreement thread |
| Establish a standing forum for JCI (none currently in `07_Operating_Cadence.md`) | Darryl | TBD | No forum evidenced |
| ~~Confirm whether any Airwall vendor selection or POC occurred~~ | Darryl | — | **RESOLVED 2026-09-17** (Darryl direct): approximately ten years in the architecture, selection completed before he joined, no Wesco procedure |
| Submit the Gartner survey response with a free-text note distinguishing secure remote connectivity from microsegmentation | Darryl | Unblocked, ready now | Competitive analysis 2026-09-17 |
| ~~Record a standalone Airwall architectural rationale~~ | — | — | **SUPERSEDED 2026-09-17** (Darryl direct): the MSP contract is the baseline for Airwall and Conductor technology use |
| Verify at markup close that licensing mechanics, express hosting rights, JCI support obligations and metering API data scope are in the agreement text or a document JCI cannot change unilaterally, since only what is captured is inside the baseline | Darryl / Brian Miller | Before signature | Darryl 2026-09-17 |
| Confirm the conversion mechanism is in the agreement text: prepaid balance treatment, pool transfer at current count, older-hardware eligibility, reconciliation method, effective date | Darryl / Brian Miller | Before signature | Darryl 2026-09-17 |
| Establish a clean current Airwall licence and device inventory (all Conductors, all sites, relays and 300v licences included) to convert against | Darryl / deployment team | Before signature | Darryl 2026-09-17 |
| Quantify the conversion effect (saving, neutral or cost) from provisioned-versus-idle counts; candidate Impact Ledger entry at signature | Darryl | After inventory | Darryl 2026-09-17 |
| Capture the signed terms as a structured baseline in the EOS | Darryl / Claude | At signature (deferred; premature while unsigned) | Darryl 2026-09-17 |

Dates above are Chief of Staff recommendations to restore cadence, not commitments JCI or Wesco Legal have made — none are evidenced with specific due dates.

## JCI Contacts
*(Roles as stated in the evidence package — correspondence/signature context, not confirmed by Darryl or an org chart. Treat as unconfirmed per Stakeholder Map discipline.)*

| Name | Role (per evidence) | Last involvement |
|---|---|---|
| Jonathan Gutierrez | Airwall sales/account lead | 2026-05-29 |
| Priya Agarwal | MSP program leadership | 2026-05-29 |
| Jeffrey McCorvey | Airwall account manager — self-described 07-15: brought on to help Jonathan on current deals + expansion | 2026-07-15 (partner meeting) |
| Domenic Busa | Solution consultant; runs monthly Tech Talks (incl. 443 capability) | Referenced 07-15 — session offered via booking link |
| Mark Hill | Agreement document author/editor | 2026-02-17 |
| Brent Pelphrey | Technical architecture support | 2025-11-10 |

Wesco-side: Brian Miller (Wesco Legal, supplier-agreement review), Brandon Thompson (Wesco Legal, routed review to supplier counsel), Ron Snyder and David Blondel (stakeholders copied on negotiations).

## Open Questions
- ~~What was decided/committed at the 2026-07-15 meeting?~~ **RESOLVED 07-17** — transcript ingested; partner/growth meeting, no agreement content (see Meeting Outcomes).
- Is Azure hosting of Airwall Conductor/MSP infrastructure actually approved, or still contested? *(07-15 transcript: account team verbally assumes Wesco keeps running its Conductor — supportive but not contractual.)*
- Did JCI's 2026-06-08 response fully close the API-access/license-monitoring question, or only partially? (Evidence is internally ambiguous. 07-15 transcript adds a verbal answer: metering agent is "read-only... see your current license usage" — contractual data-scope definition still needed.)
- Who is JCI's counsel, and has Brian Miller been connected to them?
- Was the hosting proposal ever routed through Wesco Cloud Architecture review, and what was the outcome?
- What is current, final MSP pricing?
- ~~Did any Airwall vendor selection or POC occur?~~ **RESOLVED 2026-09-17, Darryl direct.** Approximately ten years in the entroCIM deployment architecture; selection completed before he joined; no Wesco procedure. Raised and closed the same day.
- Contract documents referenced (agreement template, MSP program PDF, Loop notes) — are these still the latest versions, and do redlines/tracked changes exist anywhere outside what the evidence package could access? (Protected-document limitation noted in evidence Coverage Gaps.)

## History and Lessons
Negotiation has run 8+ months (Oct 2025 start) with a legal-review high point in late May 2026, then a 5+ week evidence gap before Darryl's 07-15 meeting. The pattern matches other stalled items in this EOS: a real decision (MSP model, branding, notice periods) got made, but execution stalled on unresolved technical/commercial questions with no named forum or deadline to force resolution. Treat the 07-15 meeting as the reset point — but only once its outcomes are actually captured.
