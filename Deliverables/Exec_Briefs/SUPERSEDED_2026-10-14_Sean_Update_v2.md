# Sean Update, week of 2026-10-19 (DRAFT v2 2026-10-14)

> v2 2026-10-14 after Darryl's review pass. Supersedes `SUPERSEDED_2026-10-14_Sean_Update_v1.md`. Changes: no staffing quantities anywhere (resource types only) until Akansh and David reconcile the numbers; Strev API outage left out (resolved 10-14, below Sean's line); entroCIM and Navigator rows reset to their real positions; capacity ask reframed around Digital Products ownership of WAM development; renewal ask starts with Dan Totino. This is the cover note and pre-read for a 30-minute meeting; the condensed deck is the meeting.

---

Sean,

WAM/ADM keeps today's production capability running at any staffing level we choose. The real choice is how fast the enterprise data foundation moves, and most of what limits ADM sits outside the team. For our 30 minutes I'd like to start with WAM, then walk you briefly through entroCIM's AI and Ascent position and where CDA stands.

**Portfolio position**

| Product | Position |
|---|---|
| entroCIM | Absorbing CDA. Ron, David and I are reconciling the 2027 core roadmap with CDA, complete by the end of October. Woolly AI and the Ascent Navigator position are the two commercial levers I want to show you. |
| WAM | Capacity reset in progress, with a roadmap reconciliation next week so the team works only on features that scale and carry value. Scale depends on data Wesco systems don't yet hold. |
| Ascent Navigator | Deploying entroCIM at Ascent's office and bringing their team up to speed on its value, so they can position it as UUI across their data center contracts. |
| CDA | Built from the entroCIM team, no FY27 line. Bill Muczko sponsoring. TSS engagement under way: Emily Munk is supportive and connected me with Matt Powers. Enterprise pricing still being tested. |

**WAM/ADM capacity**

The integration tools set the skill mix: Azure Databricks data engineers for EUDM integration, APIM integration for Strev, plus backend, front end and QA. Akansh, David and I are finalizing the staffing at each level next week; I'll bring the numbers once they reconcile.

| | Run | Run plus DDP | Run plus all completion |
|---|---|---|---|
| License sync, renewal notifications, production support | Kept | Kept | Kept |
| Added capacity | None | Databricks data engineers to the level DDP needs to move | Plus backend, front end and APIM integration for product and Strev completion |
| Enterprise data (DDP/EUDM) | Held | Advances | Advances |
| Product development and Strev integration | Extended substantially | Extended substantially | Planned pace |

Recommendation: Run plus DDP. The 09-25 direction puts the foundation on Wesco-owned data through DDP/EUDM. The DDP engineers build the path that data takes into ADM, so it is the one stream where added people turn directly into that foundation. The data itself is owned outside the team, which is why the process change below matters as much as staffing. The Q1 2027 historical-data target comes off the plan; there is no committed date at any level.

Renewal notifications stay in every option. They are the one ADM capability with business-side evidence of use: Sales Operations' October scorecard shows 35 suppliers configured and 1,337 renewal notifications sent to 238 reps.

**Expectations to reset**

- Asset data can sync from ADM to Strev only when it already exists in Wesco systems such as IAP, EUDM and WMX. Many asset programs today run on Excel files built by warehouse and supply chain teams (sales order, serial number, MAC ID), which Managed Services uploads into Strev. ADM can't automate data the enterprise doesn't hold.
- Near term, the team is helping Managed Services automate preparing those uploads. The long-term fix is capturing serial and MAC data in Wesco systems; Alan Martin's cross-SBU session with the GPOs on 10-15 is working that.
- Renewal revenue can't be measured closed-loop yet. Nothing in DDP marks an order as a renewal, so Sales Operations marks them by hand in ADM, which won't hold at volume. Until that changes, we can report notification activity but not the renewal revenue it produces.

**What I need from you**

1. Where Digital Products taking over WAM development stands after your conversation with Akash. It decides whether this reset is our plan or our input to Merwan's team.
2. Agreement in principle on Run plus DDP. Staffing follows next week's roadmap reconciliation.
3. Your support with Dan Totino's team on flagging renewal orders when the rep creates them. I'll bring the requirement.

Darryl

---

## Editorial notes

- **No quantities by design.** Akansh's stream figures don't reconcile (stream Run 6 vs run team 8; run team plus all Complete would be 16 against 15 today). Joint Teams message to Akansh and David: `Deliverables/WAM/2026-10-14_Akansh_David_Staffing_Reconciliation_Teams.md`. Add numbers only after the roadmap reconciliation, and on one basis.
- **"Databricks data engineers to the level DDP needs to move"** stands in for Akansh's "3 needed, 2 today." Keep it unquantified in anything Sean sees until reconciled.
- **Recommendation is now Darryl's** (agreed 2026-10-14).
- **"The 09-25 direction"** is softened from "your 09-25 direction"; the record holds it secondhand (Akansh relaying Sean).
- **Scorecard counts are Natalie Marquardt's (Sales Operations), not Akansh's**, so they stay. The $697K is out: North America, Aug to Sep, 88% Milestone, not attributable to notifications.
- **Left out on purpose:** Strev API outage (resolved 2026-10-14; no dependent workflow for Amy Aguirre's team, though ADM needs it running), the six-row constraints slide (bring as backup), Zapier, the 10-30 enrichment date.
- **Timing risk:** if the Sean meeting falls before the WAM reconciliation, ask 2 is the right size. If after, replace it with the reconciled staffing.
- **30 minutes, WAM sensitive.** Suggested split: WAM 15, entroCIM AI and Ascent 10, CDA 5. CDA row to refresh after the Matt Powers meeting (2026-10-14, 12:30).
- No em dashes.
