# WAM Portfolio Status Slide: Accuracy Review and Talking Points

**Prepared:** 2026-09-14
**Inputs:** Digital Product Portfolio Status Update, WAM slide (page 13); M365 weekly evidence package 2026-09-14; EOS registers `03`, `04`, `05`, `06`; `Products/WAM/`.

---

## 1. Bottom Line

The slide is substantially accurate. Two items need to change before you present, one of them non-negotiable.

1. **"Data leakage from EUDM to ADM" is wrong and should be corrected.** The defect is truncation, not leakage.
2. **The mitigation column understates the blocker.** "Working with AMS, EUDM team" reads as an engaged partner team. The tracked position, five cycles running, is that there is no named EUDM or DDP owner at all. That distinction is the entire reason to put this slide in front of leadership.

Nothing on the slide has closed since it was written apart from the two items already marked Completed, both of which are correct. Three rows carry material updates that post-date the slide.

---

## 2. Evidence Package Review (process first)

### Coverage: treat this package as a thin sample

The 2026-09-14 package is 6.1 KB against 21 to 41 KB for the four prior packages, and its own Validation block returns **"Retrieval continuation: Fail."** It returned nothing on Ford, the IDP/ADM resourcing thread, the unified-platform positioning question, or the entroCIM 3.1.12.14 release, all of which led last week's briefing.

Under the standing one-run-is-not-coverage rule, that silence is not evidence those threads went quiet. One consequence needs action rather than filing:

> **The Ford Windows Server 2019 confirmation carried a customer deadline of 2026-09-13 and had no named owner as of 09-09 (`05` B71, Critical).** That date has now passed. This package's silence does not close it. Check directly today.

### New to the record

| Item | Detail | Filed |
|---|---|---|
| Ron Snyder, pending surgery | Capacity signal only. No dates, no scope of absence, no statement from Ron in the evidence | `06` |
| Chethan GR departure extended | Now 2026-10-08. Roughly four more weeks of overlap on the Dell FTE assessment (`05` B23) and India-side deployment support | `06` |
| Quest hosting set to month-to-month | Your decision, until decommissioning. Makes the dev-01 cutover the cost driver as well as the schedule one | `03` |
| Yotta data-center conference | Appears nowhere else in the EOS. An action to notify marketing is attributed to you | `05` A42 |
| PaaS-DEV-01 SAML SSO onboarded | Identity step on the last outstanding Quest environment | `04`, `Products/entroCIM` |
| Azure Foundry authentication requirements to Ross | Ron Snyder, explicit quote | `05` B75 |

**On the Yotta item, two cautions.** The attribution is marked Explicit, but the transcript it came from is listed in the package's own Coverage Gaps as truncated, so the quote is unverified in context. And the 2026-08-26 SkyPosium precedent applies: you removed the NexusCon reference from that outbound message because naming a second conference invites the counter that time and budget for conferences exist. Yotta would be a third. Filed as A42 with a 09-19 confirm-or-drop date rather than actioned.

### Accuracy problems in the package itself

**1. The TCCC closure claim should not be accepted.** The package reports "all open risk items remediated and closed," attributed to Chad Steger, marked Explicit. The tracked position is that one control remains open: **OT-V.02.1, ISA/IEC 62443 certification evidence, with no named internal owner since 07-31.**

This is the second cycle carrying an unreconciled "all closed" quote. On 08-17 it was Yadu Nandan saying "we have closed all the high risks" against a count discrepancy that was never reconciled. Now it is the same shape in a different voice. Two reasons to hold:

- OT-V.02.1 is a **product-certification gap, not an evidence-submission gap.** Nothing in the record shows certification evidence produced or a documented risk acceptance signed. A customer marking their audit complete is not the same as the certification question being answered, and the certification question recurs at the next account.
- **Commercial consequence.** CDA's core proposition is that Wesco takes accountability for connected-device compliance posture. An unanswerable 62443 question at the largest reference account is a live counterargument, and it is better found by us than raised by someone else.

Marked **Potentially closed, confirmation required.** Confirm with Mike Reed or Yadu Nandan whether OT-V.02.1 was remediated, reclassified, or formally risk-accepted, and get the artifact.

**2. Internal contradiction on PaaS-DEV-01.** The package lists it as both advanced (SAML onboarding complete) and stalled (cutover paused pending SAML and app-gateway completion). Reconciled and filed as: identity configuration done, cutover date not set. Consistent with the 09-09 position of seven of eight environments complete.

**3. "Azure migration governance and funding delays WAM architecture decisions" is not supported.** The record does not carry that linkage. Your own words on 09-10 name the two principal hurdles as P360 attributes with data population, and proper EUDM sync with ADM. Do not adopt the package's framing here.

**4. The package generalizes where the register is specific.** It lists "Strev long-term architecture and ownership, product leadership, undefined target operating model." The record holds something sharper: the 09-11 question of whether Strev becomes the system of record at complex-build sites, gate G7, owner GPO, with named second-order consequences. Prefer the register.

---

## 3. Slide Review, Row by Row

### Must fix

**"Data leakage from EUDM to ADM"** (Risks, row 1, Impact column).

The defect is that DDP and EUDM select **shortened** manufacturer part numbers against a 15-character limit, while WAM and ADM hold the full values, so exact matching fails and orders cannot be matched reliably. The impact is failed matching and incomplete records. It is not leakage.

"Data leakage" is a security and privacy term. In a portfolio forum with IT and security people in the room it invites a question you do not want, cannot answer, and should not have raised, because it is not what is happening.

Replace with: **"Part numbers do not match between EUDM and ADM; orders cannot be matched reliably."** Also correct "trimmer" to "truncated."

**"Working with AMS, EUDM team"** (Risks, row 1, Mitigation column).

The tracked state is that after five consecutive evidence cycles **there is still no named EUDM or DDP owner.** Akansh Gangil's escalation has not produced one; `05` A29 is the further escalation you hold in reserve if it does not. "Working with" reads as a partner team engaged and progressing, which is the opposite of the problem.

Replace with something that names the ask: **"Requires a named EUDM/DDP data owner. None assigned since July."**

### Should change

**The slide shows two EUDM defects. The record carries three.**

1. Truncated manufacturer part numbers (on the slide)
2. Supplier license attributes incomplete or unavailable (on the slide)
3. **Sales orders missing from EUDM outright, requiring NetSuite hydration** (confirmed 08-31, Active and High in `04`, not on the slide)

The third is a different failure mode: records absent rather than degraded. If the purpose of this slide is to secure a data owner, three defects make a case that two do not.

**"Feasibility analysis of Asset data to be pulled from WACT (for complex builds)" is behind two decisions.**

**Corrected 2026-09-14, Darryl direct: the complex-build data capture path has not been decided. It is very much in the air and being evaluated.** The 09-01 WMX/VAS boundary was logged as a decision from a transcript and never confirmed; it is reclassified to Approaching in `03`, and `05` A1 is reopened.

What is settled, and the distinction matters on the slide: the **requirement** is settled (serial and MAC capture is mandatory for complex builds and networked assets, Darryl 09-10), and **WACT is eliminated** (Darryl 09-14: not a mature tool, holds little data). The **path** is open, and now includes the 09-11 question of whether Strev becomes the system of record at complex-build sites, under GPO review.

**Retire the WACT row green with the finding stated**, and replace it with a row that shows an open evaluation rather than a chosen direction. Do not report a decided capture path.

**"SOW 3 Implementation for enhanced sync to Strev, June, Aug, Oct (Phased approach)."**

Two issues. The June and August phases carry no status on a mid-September slide, so the audience cannot tell whether two of three phases landed. And the 09-11 question is live: Strev is under consideration as the system of record at complex-build sites, which would require metadata to flow back from Strev into ADM and from ADM into EUDM. Your confirmed 08-19 architecture places DDP and EUDM as the single source of truth with no return path.

Recommendation: raise it yourself in one sentence rather than be asked. It is a governance question you already own and surfacing it first reads as being ahead of it.

**Accomplishments are July and August on a mid-September slide.**

Nothing listed is wrong, but the newest item is August and audiences read recency as momentum. September material is available: notification analytics reporting and the product-upload fix shipped with the August release; personalized views, bulk selection and edit, uppercase end-user handling and part-number upload confirmed in production on 09-09; the WAM data-enrichment MVP scoped and prioritized on 09-03. Add one September line.

### Correct as written

- **DDPTRK-6346, Completed.** Consistent with the record. Ownership decided 07-15, progress tracking reassigned to Akansh Gangil 07-27.
- **Assigning default end user in ADM, Completed, 1 September.** Consistent. September release scope confirmed by Akansh on 08-31 included default end-user assignment, with related end-user items confirmed in production 09-09.
- **J. Booth supplier-relations row, In progress.** Accurate. David Blondel owns that communication and pinged Jarod Booth again on 08-17. Worth a check with David before you present: a row that has read "In progress, TBD" since July starts to cost credibility on its own.
- **30 October and 10 November targets.** Fine as targets.

### Prep item before you walk in

**25 September is eleven days out and is your nearest deliverable.** The EOS record carries no confirmed status on it. Get that from Akansh Gangil before the meeting, because it is the most likely question and the only one where silence would be visible.

### Not on the slide, and arguably should be

**IDP/ADM production integration: approved but unstaffed.** The proof of concept and integration architecture received WAB approval, and resourcing was declined the same week. Ankit Chadha would not commit engineering, citing an October Oracle deadline, and asked for one to two weeks from 09-02 to investigate capacity. **That window closes around 09-16.** An approved-but-unstaffed integration is a different class of item than an unapproved one. Whether it belongs on the slide depends on whether this forum can unblock it.

---

## 4. Answering Your Question Directly

**Has anything on the slide closed?** No, apart from the two rows already marked Completed, both of which stand.

**What has a material update?**

| Row | Update |
|---|---|
| WACT feasibility analysis | Superseded in direction by the 09-01 WMX/VAS decision and your 09-10 mandatory-capture ruling |
| SOW 3 enhanced sync to Strev | Now carries the 09-11 Strev system-of-record question, which would reverse part of the confirmed data architecture |
| EUDM truncated part numbers | Substantively unchanged for five cycles. That is the update, and it is why the mitigation wording should change |
| Supplier license attributes | Unchanged. A third, distinct EUDM defect exists and is not shown |

---

## 5. Talking Points

Built for two minutes. One position, three points, one ask.

### Open with the position

> "WAM is shipping on schedule. The constraint is not development. It is enterprise data ownership upstream of us."

### Point 1, what shipped

> "Sales reps now get automated 60-day license expiration notifications, live in the US and Canada, with analytics reporting behind it. Default end-user assignment completed 1 September. Next is supplier license data with accurate renewal dates, 25 September."

### Point 2, the constraint, said once and plainly

> "Two EUDM data defects are holding renewal accuracy back. Part numbers arrive truncated, so they do not match our records. Supplier license attributes are incomplete. There is a third: some sales orders are missing from EUDM entirely. None of these are development issues. They are enterprise data issues, and after two months there is still no named EUDM or DDP owner to work them with."

### Point 3, the ask

> "I need a named data owner on the EUDM and DDP side. That is the single thing that moves these dates."

### Close

> "Everything else on this slide is on track."

### If you have more time, two optional adds

**Complex builds:**
> "On complex builds, the requirement is settled: serial and MAC capture is mandatory. The capture path is still being evaluated. We have eliminated WACT, it is not mature enough and does not hold the data. WMX and VAS are both in scope, and there is an open governance question on whether Strev becomes the system of record at those sites, which would put a vendor platform upstream of EUDM. GPO owns that review. I am tracking it and I am not going to settle the data model until the system of record is settled, or we settle it twice."

**IDP/ADM:**
> "The IDP integration is architecturally approved and unstaffed. If this forum can help with engineering capacity, that is where it would matter."

---

## 6. Likely Questions

| Question | Answer |
|---|---|
| Is the TCCC audit closed? | "The audit items are reported closed. One control, the 62443 certification evidence, I am confirming separately before I call it done." Do not say closed. |
| What is the actual impact of the part-number issue? | "Orders cannot be matched reliably between the data lake and ADM, so renewal and install-base records are incomplete. It is a matching failure, not a data exposure." |
| Why is the WACT item marked complete? | "We evaluated it and we are not pursuing it. It is not a mature tool and it does not hold the data. That closes the option; it does not close the question, which is still being evaluated." |
| So what is the capture path? | "Not decided. The requirement is decided, serial and MAC capture is mandatory. The path is under evaluation and the system-of-record question sits with GPO." Do not name a chosen tool. |
| Is 25 September at risk? | Get this from Akansh Gangil before the meeting. The record does not carry a confirmed status. |
| Where is the revenue? | Do not rest the license investment on the $16.7M YTD / 87% attainment figure. That revenue comes from the supply chain motion, not the license capability, and the 15.2% gross margin in the FY27 P&L corroborates it. Use the renewal-signal-yield metric instead. |

## 7. What Not to Say

- **"Data leakage."** Not what is happening, and it invites a security conversation you did not intend.
- **"The TCCC audit is closed."** One control remains open on the tracked record.
- **That the three-times-daily DDP/EUDM sync is automated and production-grade.** The 08-05 discrepancy between the Backlog Deep Dive deck and the 07-16/07-20 record is still unresolved.
- **That the complex-build capture path is decided.** It is not. The requirement is decided; the path is under evaluation. Naming WMX or VAS as chosen overstates the record and would have to be walked back.
- **That attainment proves the license roadmap is converting.** It does not, and a reviewer can reasonably ask what the license capability has produced commercially.
