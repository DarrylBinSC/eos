# JCI OpenBlue Airwall MSP Agreement Review — EOS Update (v2.1)
As of: 2026-07-17 (v2 — revised same day to incorporate the 2026-07-15 partner-meeting transcript, received from Jeff McCorvey and provided by Darryl; v2.1–v2.3 — same-day corrections from Darryl: Conductor hosted in Wesco Azure as of today; internal approval = Wesco Architecture Review Board (WAB) for the JCI API connection; Babu Papanna has no JCI/Conductor actions; HA failover is Wesco IT responsibility inside the Azure IoT subscription; hosting responsibility settled operationally — Wesco is the hosting authority, environment owned by Wesco, application owned by Darryl's team, with JCI's support obligations to Wesco the sole open element).

Sources: (1) agreement review summary provided by Darryl this session — **provenance still not stated**; not marked as Brian Miller work product; confirm before using externally. (2) Teams transcript, "Partner Meeting: FY26 Review & FY27 Growth Strategy," 2026-07-15, 43m — Darryl, Mike Reed (Wesco); Jeff McCorvey, Jonathan Gutierrez, Priya Agarwal (JCI). The agreement remains **under legal review, not finalized**.

---

## 1. Executive Summary

- **The hosting-rights blocker is confirmed in the contract text.** The draft distinguishes Hosted JCI Offerings (JCI-controlled systems) from Non-Hosted JCI Offerings (installed on Reseller or Customer systems) — a structure that *may* support a Wesco-hosted model — but does **not** clearly grant Wesco the right to host and self-manage the Airwall Conductor or Relays. Blocker #1 is now an identified drafting gap with a possible existing vehicle (Non-Hosted classification).
- **The 07-15 meeting evidence gap is closed — and it strengthens Wesco's position.** The meeting was a JCI-initiated FY26 review / FY27 growth discussion, not a negotiation: none of the 5 blockers were discussed and no contract commitments were made. But JCI's account team described the MSP model **assuming Wesco continues to run and provision its own Conductor**, with only a **read-only license-usage agent** added for monthly metering. That is verbal, account-level evidence that the self-host model is JCI's operational expectation — suggesting the express-hosting redline should face low commercial resistance. It is not a contractual grant.
- **Execution is running ahead of contract.** Wesco is **hosting the Conductor in Wesco Azure as of today** (Darryl, 07-17) — two Conductors in HA replication plus relay, migrated from the legacy pre-acquisition hosted environment — while there is **no contract at all** (Darryl on-call: "we're off the street buying product"). Not a breach of anything, but the to-be operating model is live before the agreement defines Wesco's rights, support entitlements, or responsibility split. This raises the cost of a wrong answer on hosting language. The remaining internal gate is specific: **WAB approval of the JCI API connection (license-metering agent) from the Wesco-hosted Conductor** — the hosting decision itself is settled and operational.
- **The risk picture is wider than the 5 tracked blockers.** The review surfaces ~10 additional contractual issues: customer flow-down, JCI unilateral changes to MSP Program Materials/customer terms, price increases with limited notice, non-cancelable/non-refundable Orders, no customer termination for convenience, Wesco L1/L2 support obligations, broad reseller indemnity, liability-cap carve-outs, customer non-payment risk, potential competing-offerings restriction.
- **Relationship momentum is restored.** JCI is leaning in for FY27 growth (Aug-15 Ascent POC follow-up planned; 443-only deployment simplification confirmed available; solution-consultant support offered). The account channel is warm — the remaining stall is on the agreement itself, and the window to convert goodwill into contract language is now.

Wesco's preferred position, redline-ready: Wesco hosts and manages the Conductor and MSP infrastructure in Wesco Azure under Wesco cloud governance, security, monitoring, and support; JCI receives secure API access for concurrent license monitoring plus any support access Wesco authorizes. Nothing in either source contradicts the 2026-05-26 decisions.

## 2. Current Status

**Classification: Active legal review with an embedded architecture/hosting decision** (combination — "Other"; closest single label: Active legal review).

Reasoning: not a new opportunity (8+ months of negotiation); not purely contractual risk. The binding constraint is agreement language; the pivotal issue underneath is a hosting model Wesco has decided in principle (05-26), is **already executing** (Azure migration in flight), and JCI's account team operationally expects — but which the draft does not grant and internal Cloud Architecture review has not confirmed. The 07-15 meeting restored account momentum without advancing the agreement, so the item is best read as: relationship active, contract stalled, evidence now favorable.

## 3. Key Decision Required

**Primary: Does Wesco make express Azure self-hosting rights a condition of signature?** I.e., direct Brian Miller to redline the agreement (or its Order/exhibit) to expressly permit Wesco to host and manage the Conductor and related MSP infrastructure in Wesco Azure, with JCI access limited to secure API-based license monitoring (the "read-only agent" JCI described on 07-15) and Wesco-authorized support access — and hold signature until that language lands.

Nature of the decision — a combination, in this order:

1. **Legal language issue (primary):** the right doesn't clearly exist in the draft; it must be granted somewhere (body, Order, or exhibit). The 07-15 verbal evidence lowers expected negotiation friction but substitutes for nothing.
2. **Technical architecture issue (prerequisite, narrowed 07-17):** the hosting model itself is settled and operational (Conductor live in Wesco Azure today). The internal approval that must precede contractual commitment is the **Wesco Architecture Review Board (WAB) approving the JCI API connection (metering agent) from the Conductor** — the exact access the agreement would grant JCI.
3. **Support / operating model issue (consequence):** self-hosting drives the undefined responsibility matrix (patching, backup, DR, SLA scope, security obligations, L1/L2 split, JCI L3 escalation — which JCI itself recommended using for the Conductor migration) and intersects the open CSS/TSS Managed Services ownership question.
4. **Commercial model issue (secondary):** MSP billing mechanics are now understood verbally (monthly in arrears on provisioned licenses from a pre-granted pool, vs. 12-month prepay today — commercially favorable); confirm the contract text matches, and whether self-hosting changes fees, SLA, or liability.

Secondary decision: Wesco's acceptable-risk position on the broader terms (indemnity breadth, liability carve-outs, unilateral change rights, non-cancelable Orders, customer-contracting restrictions) — a Legal + Darryl risk-appetite call to settle before final markups.

## 4. Risks and Dependencies

**Legal / contractual** (priority order)

1. No express Wesco right to host/self-manage Conductor/Relays — the core gap (fact, per review). Sharpened by the in-flight Azure migration: operational reality will precede contractual right unless the language lands.
2. JCI unilateral change rights over MSP Program Materials and customer terms — undermines offer stability (issue raised by review; severity pending exact language).
3. Broad reseller indemnity + liability-cap carve-outs — risk transfer to Wesco; acceptability unassessed.
4. Non-cancelable/non-refundable Orders — hardware commitment risk persists (hardware is still purchased and shipped under MSP; only licenses move to consumption billing, per 07-15 transcript).
5. Potential restriction on competing offerings — Darryl acknowledged on 07-15 that Wesco "probably competes with OpenBlue a little bit" (FDD, unified alarming) even while not meeting in bids, and Priya noted entroCIM "looks very similar to what we sell" as OpenBlue. A broad non-compete clause could bite the core entroCIM value proposition — scope this clause carefully.
6. Price increases with limited notice.

**Technical / hosting**

- WAB approval of the JCI API connection not yet obtained; Conductor already live in Wesco Azure (07-17).
- Whether Conductor/Relays are contractually available as Non-Hosted JCI Offerings — unknown; potentially the cleanest path.
- Hosting responsibility matrix **settled operationally (Darryl, 07-17): Wesco is the hosting authority — environment owned by Wesco, application owned by Darryl's team; patching, backup, DR, SLA, and security addressed under Wesco governance.** Sole open element: **JCI's support obligations to Wesco** (L3/escalation/SLA on the Conductor software) — still owed by JCI; the exhibit documents existing reality and negotiates only this.

**Security / data access**

- License-metering agent described by JCI as "read-only... see your current license usage" (verbal, 07-15). Contractual definition of API/agent data scope still needed — verbal assurance is not a data boundary. The WAB review of this connection (07-17) is the internal control point; its findings should feed the contractual scope language directly.
- Support-access boundaries (Wesco-authorized only, per preferred position) not yet contractual.

**Commercial / billing**

- Customer non-payment risk appears to sit with Wesco.
- Billing mechanics (07-15, verbal): monthly in arrears on provisioned licenses, pre-granted pool, no charge until provisioning; multiple Conductors metered to one consolidated bill; relay software free but underlying 300v license charged. Favorable vs. today's 12-month prepay — **confirm the draft says this**.
- Final MSP pricing still not confirmed received (blocker #5).

**Operational / support**

- Wesco L1/L2 obligations: undefined against the entroCIM product-support model and the unresolved CSS/TSS Managed Services ownership question.
- HA failover: **Wesco IT responsibility inside Wesco's Azure IoT subscription** (Darryl, 07-17) — no ownership gap; JCI L3 is optional support. This is the first settled row of the hosting/support responsibility matrix — carry it into the Order exhibit (action #5).

**Customer-contracting**

- Flow-down of the JCI Customer Agreement and no termination for convenience — potentially at odds with the hosted-entroCIM model where customers never see Airwall (reconfirmed 07-15: every hosted proposal embeds Airwall; customers interact only with entroCIM). **Gap:** EOS has no record of Wesco's standard customer terms to compare against — Legal input needed, not assumption.

**Dependencies:** JCI counsel contact for Brian Miller (still unnamed); JCI's 06-08 hosting/API answers (ambiguously resolved); final pricing. ~~07-15 meeting transcript~~ — received and ingested 07-17.

## 5. Recommended Next Actions

| # | Owner (likely) | Action | Why it matters | Timing |
|---|---|---|---|---|
| 1 | Darryl | Confirm provenance and completeness of the agreement review (whose analysis, which draft version) | Everything downstream cites it | Immediate |
| 2 | Darryl → Brian Miller | Brief Brian: issue set + express-hosting redline as the priority ask + the 07-15 evidence that JCI's account team already operates on the self-host assumption | Converts review + meeting into a negotiating position from strength | This week (aligns with existing 07-24 check-in) |
| 3 | Darryl (with JCI re-engagement) | Ask JCI whether Conductor/Relays are available as Non-Hosted JCI Offerings | May resolve the hosting gap via existing structure instead of bespoke drafting | With the 07-23 re-engagement of Gutierrez/McCorvey |
| 4 | Darryl → WAB | Submit the JCI API connection (metering agent) from the Wesco-hosted Conductor to the Wesco Architecture Review Board for approval | The exact access the agreement grants JCI should be internally approved before it's contractually committed; WAB findings feed the data-scope language (Q4) | This week — before final markups |
| 5 | Darryl's team + Legal | **Document the existing hosting model as the Order exhibit** — the responsibility matrix is settled operationally (Wesco = hosting authority; environment: Wesco; application: Darryl's team; patching/backup/DR/SLA/security under Wesco governance). The exhibit's single negotiated element: **JCI's support obligations to Wesco** (L3/escalation/SLA), which JCI still owes | Wesco describes what already runs; JCI reacts — and the one ask flips to JCI's side of the table | Next 1–2 weeks |
| 6 | Brian Miller | Assess customer flow-down + no-termination-for-convenience against Wesco standard customer terms; scope the competing-offerings clause against entroCIM/OpenBlue overlap | Post-signature discovery of either conflict would be far costlier | Before final markups |
| 7 | — | ~~Name an owner for the JCI L3 engagement~~ **Resolved 07-17:** HA failover is Wesco IT responsibility inside the Azure IoT subscription; JCI L3 optional | Feeds the responsibility matrix (action #5) as its first settled row | Done |
| 8 | Darryl | Relationship actions from 07-15: Nathan Kehr ↔ Priya Agarwal intro; confirm Jeff's deliverables arrive (443 Tech Talk video to Shawn Clark + Babu, booking link, Aug-15 POC invite) | Keeps the restored account momentum compounding while the contract closes | ~2 weeks; Aug-15 POC call |

## 6. Suggested EOS File Updates

| File | Section | Content | Type | Status |
|---|---|---|---|---|
| `Products/JCI_Partnership.md` | "Agreement Structure and Contractual Risk (07-17)" + rewritten "2026-07-15 Meeting Outcomes" + contacts + next steps | Review detail; full transcript outcomes; Domenic Busa added | Update | **Applied** |
| `03_Decision_Log.md` | Decisions Approaching → JCI entry | Sharpened decision; transcript evidence (self-host assumption, execution-ahead-of-contract) | Update (decision) | **Applied** |
| `04_Executive_Watch_List.md` | JCI row | Transcript ingested; account momentum vs. agreement stall; execution-ahead-of-contract flag | Update (risk) | **Applied** |
| `05_Commitments.md` | Transcript commitment closed; new made/owed commitments (Babu/L3, Kehr intro, JCI deliverables, Ascent shipment) | | Update + new | **Applied** |
| `06_Stakeholder_Map.md` | JCI entry, Jeff McCorvey, new Domenic Busa, Babu Papanna detail | | Update | **Applied** |

## 7. Questions for Legal / JCI

Priority order:

1. **Can the agreement be updated to expressly permit Wesco to host and manage the Airwall Conductor and related MSP infrastructure in Wesco Azure, while limiting JCI access to secure API-based license monitoring and any support access authorized by Wesco?** *(To JCI, via Legal — the anchor ask. Supporting fact: JCI's own account team described the MSP model on 07-15 assuming exactly this arrangement.)*
2. Are the Conductor and Relays available as Non-Hosted JCI Offerings under the existing definitions? If yes, does that classification achieve the Wesco-hosted model without new drafting? *(JCI)*
3. If drafting is required, where should it live — agreement body, the Order, or a hosting exhibit — and should the Order/exhibit define the full hosting model (responsibility matrix: patching, backup, DR, SLA scope, security obligations, L1/L2/L3 support split, support access)? *(Legal + JCI)*
4. Exactly what data does the license-metering agent/API expose? JCI stated verbally it is "read-only" license usage — can that scope be contractually defined and limited, and does the agent's presence in Wesco's Azure environment carry any additional access? *(JCI technical + Legal + Wesco cloud governance)*
5. Does Wesco self-hosting change SLA commitments, support boundaries, fees, or liability allocation? And does the contract text match the billing model described 07-15 (monthly in arrears on provisioned licenses, pre-granted pool, no charge until provisioning, consolidated multi-Conductor billing, relay free / 300v license charged)? *(JCI)*
6. Are the customer-contracting terms (flow-down to the JCI Customer Agreement, no termination for convenience, JCI unilateral changes to customer terms) workable against Wesco's standard customer agreements and the hosted-entroCIM model where customers never interact with Airwall? *(Wesco Legal first, then JCI)*
7. Are the broad reseller indemnity and liability-cap carve-outs acceptable as drafted, and what is Wesco's counter-position? *(Wesco Legal)*
8. Does the competing-offerings restriction, as drafted, constrain entroCIM's FDD/alarming value proposition given the acknowledged functional overlap with OpenBlue? *(Wesco Legal + Darryl)*
9. Can price-increase notice be extended and the non-cancelable/non-refundable Order terms be softened (consistent with the 05-26 asks for 60-day product-change / 180-day EOL notice)? *(Legal + JCI)*
10. Who is JCI's counsel for this agreement? *(JCI — still unanswered; Brian Miller has no counterpart.)*

## 8. Executive Briefing Version

> The JCI OpenBlue Airwall MSP agreement remains under legal review. Our review of the draft confirms the central open issue: the agreement distinguishes JCI-hosted from reseller/customer-hosted offerings but does not yet expressly permit Wesco to host and manage the Airwall Conductor and MSP infrastructure in Wesco's Azure environment — our preferred and operationally intended model, with JCI receiving secure API access for license monitoring. Encouragingly, in our July 15 partner meeting JCI's account team described the MSP operating model on exactly that basis: Wesco continues to run and provision its own Conductor, with a read-only metering agent supporting monthly consumption-based license billing. We are asking JCI to confirm this can be reflected contractually, either through the agreement's existing non-hosted offering structure or targeted language in the order exhibits. The review also identified standard commercial terms requiring legal positioning — indemnity scope, liability carve-outs, order cancellation, unilateral change rights, and customer flow-down terms — which Wesco Legal is assessing. The Conductor is now hosted in Wesco Azure; in parallel, we are routing the JCI license-monitoring API connection through the Wesco Architecture Review Board for approval, defining the hosting and support responsibility split to attach to the agreement, and continuing partner-level engagement with JCI on deployment simplification and joint growth opportunities. No signature timeline is committed until the hosting language and priority terms are resolved.

---

*Facts vs. interpretation: the Hosted/Non-Hosted structure, absence of an express hosting right, and listed issue areas are stated by the review document. Meeting statements (read-only agent, billing mechanics, 443 availability, L3 recommendation) are from the 07-15 transcript — AI-generated, names garbled throughout (entroCIM→"EntraSim", JCI→"BCI", Nathan Kehr→"Nate Kerr", etc.), matched against the known portfolio; speaker attribution consistent with Darryl's presence on the call. Conductor-hosted-today, the WAB approval scope, the Babu correction, and Wesco IT ownership of HA failover (Azure IoT subscription) are direct from Darryl (07-17). All verbal JCI statements are account-team positions, not contractual commitments. Severity rankings, the "execution ahead of contract" framing, likely owners, and target timings are Claude interpretation/recommendation.*
