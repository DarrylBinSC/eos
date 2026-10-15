# Sean WAM Program Update — Preparation and Work Plan

**Created:** 2026-09-01
**Revised:** 2026-09-02. v1 treated the internal data-collection question and the Strev product enhancement track as one topic. Corrected by Darryl: they are separate tracks with different owners, different constraints and different decisions. Restructured accordingly, and the Strev priorities document has been added at `Products/WAM/Strev_2027_Priorities.md`.
**Purpose:** organize the work with Akansh Gangil and David Blondel ahead of a WAM program update to Sean McCloskey.
**Meeting date:** not set.

---

## 1. What Sean asked for

**Evidence basis: reported, not direct.** Sean's input was verbal and rapid fire, captured from Darryl's account on 2026-09-01. No transcript, no email. The two headings are accurate; surrounding detail is reconstruction.

1. **Usable license data in the system, and how serial numbers and other metadata are provided for the business.**
2. **Strev enhancement costs required for 2027.**

**The material fact that shapes everything below: the program has never been updated to Sean.** This is a first program update, not a status refresh. It establishes the frame and will be re-shared upward. `06_Stakeholder_Map.md` records that WAM benefits underreporting already left a negative impression with John Engel and Rob Hasting, so every claim has to survive that audience.

---

## 2. Two tracks, deliberately kept apart

| | Track A: internal data collection | Track B: Strev product enhancements |
|---|---|---|
| The question | How does the business capture serial numbers and other asset metadata, and get them into usable form | What does Strev build in 2027, and what does it cost |
| Nature | Internal Wesco process and IT problem | Vendor product roadmap and funding decision |
| Constrained by | IT systems and process ownership: WMX, VAS, GPO, MDM, DDP, EUDM, Supplier Relations, Sales Ops | Strev's own product plan, SOW structure, and Wesco's 2027 funding |
| Owners | Process owners and IT, several outside Darryl's organization | Akansh, with Sunny Sharma's organization |
| What Sean needs | Where the capability actually stands and what is blocking it | A number, and where it sits in the plan |

**The interface between them is narrow.** Bulk parent-child asset mapping in the Strev list consumes parent-child hierarchy data, and "support for complex asset and build structures" in the API expansion does the same. Wesco has to be able to produce that data before Strev can ingest it in bulk, so the dependency runs Wesco to Strev in one direction and covers one item. Nothing else in the Strev list depends on the internal collection question.

Keeping them apart matters for the update itself. Track A is a problem Darryl is working through with people outside his organization. Track B is a funding ask. Presenting them as one thing invites the response that the money should wait for the process, which would be the wrong conclusion for most of the Strev list.

---

## 3. Track A: internal collection of serial numbers and metadata

### Current state from the record

**Simple products.** WMX captures serial numbers at shipment against the order and propagates them to DDP. MAC address capture is unconfirmed. WMX 5.7 is expected to add MAC address and asset tag fields beyond serial number.

**Complex builds.** Serial-to-VAS association does not happen today. From 2026-08-27, warehouse personnel are instructed to capture MAC address, serial number and asset tag inside VAS as part of standard work and labor instructions, which makes the capture point explicit but is five weeks old and not yet proven at volume. Govardhan Shetty's proposed mechanism, pulling serial numbers back from WMX under the shipped order's part number and mapping them onto the VAS parent-child template, is a candidate future state rather than a decision.

**Direction reaffirmed, not changed:** VAS for complex finished-goods attribute capture, WMX for simplified products, pending architecture finalization.

**License data.** Real delivered capability in ADM: license order data from DDP/EUDM by vendor part number and supplier ID (03 Jul), export and audit trail, license detail editing via UI, end-user project name from IAP where records lack it, automated sales-rep notifications for 60-day expirations (17 Jul). Not yet true: identifying all license part numbers and software in master data with license term and clean descriptions is Active and flagged red, with the dependency named as MDM and DDP. License activation failures remain open.

### Where the constraints actually sit

This is the part of Track A that is above Darryl's line, and it is what Sean should hear.

| Constraint | Who holds it |
|---|---|
| WMX roadmap and mandatory attribute capture | John Barlolotti as GPO for WMX (delegated from Steve Leslie), Sid Sarna as solution architect |
| EUDM and DDP data model, and the truncation defect | Daniel Totino and the EUDM team. No named fix owner as of 09-01 |
| Product and license master data completeness | MDM, with Inder Gambhir and Gandhi Subramanian named in the record |
| Supplier attribute data | Jarod Booth's organization, via David Blondel |
| Supplier data collection in practice | Natalie Marquardt, and the record flags her as a single point of dependency |

Five constraint holders, four of them outside Darryl's organization. That is the honest characterization of Track A: not a build problem, an ownership problem across organizational boundaries.

### The three defects underneath it

Truncated manufacturer part numbers with no named fix owner, sample orders absent from EUDM requiring NetSuite hydration, and Core ERP sales orders missing from the EUDM table under INC5456198. Carried as W1, W2 and W3 on the WAM Product Leadership Sync register.

Judgment: put them in the update. A first program update describing license data as usable while three known completeness defects sit unowned is what a reviewer finds later, and Sean is the person who would be embarrassed by it. They are also the concrete evidence for what cross-functional support Darryl needs, which is a legitimate ask to make of a VP.

---

## 4. Track B: Strev product enhancements for 2027

Source: `Products/WAM/Strev_2027_Priorities.md`. Three investment areas: asset data management (bulk parent-child asset mapping, automated warranty end date calculation), tenant deployment and scalability (tenant configuration cloning and template management), and API and integration platform (API modernization and expansion).

### Three findings

**1. This is a portfolio investment, not a WAM one.** The named primary integration targets are entroCIM and Ascent. Two of the three areas, tenant cloning and API modernization, deliver value well beyond WAM. If the 2027 cost lands inside the WAM FY27 P&L, the attribution will not survive review, and WAM will be carrying spend that benefits two other products.

This is the single most useful thing to put in front of Sean, because it is a funding-structure decision only he and Finance can make, and it is easier to make before the AOP number is set than after.

**2. The document has no costs.** It is a priorities list. Sean asked for 2027 costs, and the answer today is that there is not a number yet. Getting one requires Strev to size the work, which is Akansh's path through Sunny Sharma's organization.

**3. No Strev line is visible in the FY27 WAM P&L.** DEV labor is 19.00 FTE, all India, zero North America, $752,400 gross, capitalized to $150,480 of expense. COGS is stated as People plus HW plus SW. Strev works under SOWs, with SOW 3 active and Milestone 2 invoiced. So Strev spend is either inside the COGS software line without separate identification, or it is not in the plan. **Labeled assumption: I cannot tell which from the record here.** Either answer clears Sean's threshold: unbudgeted is a funding case that does not hold up, buried in COGS is an attribution problem a reviewer will find.

### Two questions to settle before the list is presented as a portfolio position

Have Ron Snyder and the Navigator owners been consulted on the entroCIM and Ascent integration targets? Neither appears in the record on this. If the API roadmap names their products as integration targets and they have not been asked, the first question in the room will be whose requirement this is.

And is there a Strev entry in the FY27 AOP cycle at all? `AOP_FY27/Change_Logs/` holds change logs for WAM, entroCIM, CDA and Navigator, and none for Strev.

### The margin context, if a number is quoted

FY27 shows a 15.2% gross margin, which is a distribution margin rather than a software margin, corroborating the 08-05 finding that current WAM revenue is earned through supply chain programs rather than the license capability. A Strev funding request cannot lean on WAM's existing revenue, because that revenue is not earned by the capability the money improves. Three FY27 items are already open with Finance and will be quoted back if any 2027 figure is: the capitalization label contradicts its own arithmetic (65% stated, 80% computed, $112,860 swing), the India rate basis differs between the P&L at $22 and the AOP rate card at $24, and Resources NA is zero so any North America assignment is unbudgeted at a 4.3x differential.

---

## 5. What Akansh and David need to supply

### Track B, the critical path

| # | Request | Owner | Needed by |
|---|---|---|---|
| 1 | Is Strev SOW spend inside the FY27 WAM P&L, and if so on which line? If not, what is the 2027 requirement? | Akansh | Before drafting |
| 2 | Sizing from Strev for each of the three investment areas, separated by area rather than as a single total | Akansh, with Sunny Sharma's organization | Before drafting |
| 3 | Which items are Wesco-driven requirements versus Strev's own product direction. This decides how much of it Wesco should be funding at all | Akansh | Before drafting |
| 4 | Whether a Strev AOP entry exists for FY27, and where it sits | Akansh | Before drafting |
| 5 | Whether Ron Snyder and the Navigator owners have been consulted on the entroCIM and Ascent integration targets | David | This week |

### Track A

| # | Request | Owner | Needed by |
|---|---|---|---|
| 6 | Serial number and metadata coverage today: proportion of shipped assets with serial number, MAC address and asset tag captured, split simple products versus complex builds, since the 08-27 VAS standard work change | Akansh | Before drafting |
| 7 | License master data completeness: how many license part numbers carry a license term and a clean description, against the total. Converts the red MDM and DDP dependency into a number | Akansh, with MDM and DDP | Before drafting |
| 8 | License activation failure position and the state of the null and missing sales-order date root cause | Akansh | Before drafting |
| 9 | Current owner and expected fix date for each of the three completeness defects, or a statement that none exists | Akansh | Before drafting |
| 10 | Functional overview in business terms: license, asset, serial and metadata, entitlement, renewal | David | Before drafting |
| 11 | Build plan with sequence, dependencies, resourcing and dates for the Next items, marked funded versus needing 2027 money | David and Akansh | Before drafting |

---

## 6. Shape of the update to Sean

A caution on the pack as originally framed. A high-level functional overview followed by detailed build plans is the right material to build with Akansh and David. It is the wrong thing to lead with in front of Sean. `Reference/Sean_Update_Standard.md` is explicit that shipped features, sprint completion and delivery milestones do not clear the bar, because delivery competence is assumed and reporting it implies it was in doubt.

Two artifacts:

**A. The update.** Position first. Where the license and asset capability stands, what is blocking it and who holds the constraint (Track A), then the 2027 Strev requirement and the funding-structure question (Track B), then what Darryl needs from Sean. The ask is most likely cross-functional air cover on Track A and a funding-attribution decision on Track B, not an opinion on the roadmap.

**B. The backing pack.** Functional overview, current-state numbers, build plan, costed 2027 requirement by investment area, defect position. Built by Akansh and David. This is the proof, not the presentation.

---

## 7. Work plan

The meeting date is not set, and the sequence only works backwards from one.

| Step | Owner | Timing |
|---|---|---|
| Confirm scope and timing with Sean | Darryl | This week |
| Send the information requests | Darryl | Immediately |
| Confirm whether entroCIM and Navigator have been consulted on the Strev API targets | David | This week |
| Working session with Akansh and David | Darryl, David, Akansh | Once requests 1 to 4 and 6 to 9 are answered |
| Draft the update | Darryl | After the working session |
| Review against the realized versus planned standard | Darryl | Before sending |

Carried on the WAM Product Leadership Sync register as W12, W13 and W14.

---

## 8. Open questions for Darryl

1. Is the meeting Sean alone, or a wider audience? A pack re-shared to Dirk or Engel is built differently from a one-to-one.
2. Did Sean give any timing?
3. Is "Strev enhancement costs" his phrase? If so he may already believe a number exists, and the honest answer this week is that it does not.
4. Should the Strev 2027 priorities be positioned as a CSS Platforms investment rather than a WAM one? That is the recommendation, and it is a decision to make before the AOP number is set.

---

## Appendix: draft message to Akansh and David

Send: Teams, group chat with both. Voice per `Reference/Communication_Preferences.md`. Not sent.

---

David, Akansh,

Sean has asked for an update on WAM. Two things specifically: usable license data in the system and how serial numbers and other metadata get to the business, and the Strev enhancement costs required for 2027. We have not given him a program update before, so this one sets the frame and it will get re-shared upward.

I want to treat these as two separate tracks, because they are. The internal question of how the business collects serial numbers and asset metadata is a process and IT ownership problem across WMX, VAS, MDM, DDP and Supplier Relations. The Strev 2027 priorities are a vendor product investment. They touch in one place, the parent-child hierarchy data that bulk asset mapping would consume, and nowhere else.

Akansh, on Strev the critical path is cost. I cannot see a Strev line in the FY27 WAM P&L, so the first question is whether SOW spend sits inside the COGS software line or is not in the plan at all. Then sizing from Strev for each of the three areas separately rather than as one total, and a view on which items are our requirements versus Strev's own product direction, because that decides how much of it we should be funding. Also whether a Strev entry exists in the FY27 AOP cycle, since there is a change log for WAM, entroCIM, CDA and Navigator and none for Strev.

On the internal track I need numbers rather than descriptions. Serial number, MAC address and asset tag coverage today, split between simple products and complex builds, since the VAS standard work change in late August. License master data completeness, meaning how many license part numbers carry a license term and a clean description against the total. And the current license activation failure position.

David, I need the functional overview in business terms across license, asset, serial and metadata, entitlement and renewal, and then the build plan with Akansh: sequence, dependencies, resourcing and dates, marked clearly as what is funded versus what needs 2027 money. Separately, please check whether Ron and the Navigator side have been consulted on the Strev API work, since entroCIM and Ascent are named as the primary integration targets and I have not seen either of them in that conversation.

One more thing for the session. The truncated part numbers, the EUDM sample orders and INC5456198 all sit underneath the completeness of the license data Sean is asking about. I would rather put those in front of him ourselves, as the evidence for the cross-functional support we need, than have them found later. Bring the current owner and expected fix date for each, or tell me there is not one.

I will confirm timing with Sean this week. Tell me what is realistic on the numbers and we will set the working session around that.

Darryl


---

## Correction, 2026-09-09: audience position

**Source: Darryl, direct, 2026-09-09. Recorded during the WAM / ADM feasibility and ownership evidence pack session.**

The statement in section 1 above, that the program has never been updated to Sean and that this is a first program update, is wrong. Sean has been involved with WAM and ADM since the project began, over a year ago, and became involved again earlier this year when the portfolio was assigned to Darryl. He is current at concept and structure level. What he does not have is the detail of the last several months, because Darryl and Sean have not discussed the project in specifics in that time.

The original statement is left in place so the decision trail is preserved. What it changes about this document:

- The frame is the delta since roughly the spring, not an introduction. Orientation content on what WAM, ADM, Strev or IAM are does not belong in front of Sean.
- Specifically new to him: the Akansh Gangil and Violet Moyer enrichment work including the MVP scope decision and the asset-upload deprioritization; the VAS and WMX complex-build capture path including the 2026-08-19 architecture confirmation, the 08-27 VAS standard work change and the 2026-09-01 tool boundary decision; the three completeness defects and their ownership position; and the DDP and EUDM integration read as an operating reality rather than a milestone.
- The two-track structure in section 2 still holds, and the Track A constraint analysis still holds. Both are carried forward into `2026-09-09_WAM_ADM_Feasibility_Evidence_Pack.md`.
- The information requests in section 5 are not superseded. They are merged into Part 7 of that pack rather than duplicated, with the sent status recorded against each.

**Superseded in scope as well as in framing.** Sean's message of 2026-09-09 is broader than the two headings recorded in section 1. It asks for use cases, a data plan, an organizational feasibility judgment, an assessment of Digital Products taking ADM development over, and a go or no-go placeholder. The work of record is now `Deliverables/WAM/2026-09-09_WAM_ADM_Feasibility_Evidence_Pack.md`. The Strev 2027 funding-attribution question in section 4 remains live and is a separate decision, deliberately kept out of the ownership discussion.
