# EPMO Portfolio Review Slide Update: entroCIM and WAM Rows

Final text for the IoT Platforms and Wesco Platforms rows of the EPMO Portfolio Review slide ("Executive Summary and Material Changes (4 of 4)", PM column Chris Gazdic and David Blondel). The review is monthly, delivered by Rob Hayston to John Engel, as agreed with Darryl on 2026-11-09 after a QC pass. Health colors and trend arrows are Darryl's call on the slide. September YTD figures and targets as placed on the final slide by Darryl, taken from the October John Engel deep-dive financials; the YTD target lines were kept because the EPMO format carries them for every initiative. Final slide image: `2026-11-09_EPMO_Portfolio_Review_Slide_Final.png`.

## IoT Platforms

**Health Comment**
FY27 AOP sets reduced development capacity for 2027; roadmap reset to two major and two maintenance releases. 3.1.12.14 released to all customers; Q4 release (entroCIM 4.0) in development. Software sales below the 2026 objective.

**Benefit YTD Progress**
- Sept YTD direct software sales: $2.0M
- Sept YTD target: $4.6M
- Sept YTD product pull thru sales: $208K
- Sept YTD target: $2.2M

**Upcoming Milestones**
- Q4 release: entroCIM 4.0 platform update, entroCIM DC ver. 2 and entroCIM AI, releasing early January 2027
- Customer and sales enablement on release 3.1.12.14, Q4
- Remaining Customer Education courses released, Q4

**Accomplishments**
- 3.1.12.14 released to all customers: global search, Gridboard, graphics builder, batch point writer, security and platform updates.
- Issued the approved deployment strategy guide to Sales & Solutions (Wesco-Hosted standard, on-premises where customer policy requires).
- Secured AI governance approval for entroCIM AI, launching with entroCIM 4.0.
- Won the Merck Rahway renewal; Ford PO received; Federal Reserve floor projects closed out.
- Launched the Customer Education Program with a priced course catalog; courses releasing through Q4.

**Next steps**
- Deliver the Q4 release: entroCIM 4.0, entroCIM DC ver. 2 and entroCIM AI.
- Transition customer support from SME-hour arrangements to the standard support agreement.
- Plan the entroCIM and Ascent Navigator integration for the 2027 roadmap, targeting the Q4 2027 release in step with Navigator's release schedule.

## Wesco Platforms

**Health Comment**
Digital Products delivers ADM, the DDP asset-data tool, within this program; Intelligent Asset Lifecycle Management services is the business offering. License tracking is live for Sales Operations; Managed Services asset functionality arrives January and February 2027. Scaling depends on serial, MAC and supplier data not captured today.

**Benefit YTD Progress**
- Sept YTD sales: $29.7M
- Sept YTD target: $14.3M

**Upcoming Milestones**
- Additional ERP data and unconfigured-supplier order tracking through EUDM, November
- Bulk asset insert and update by file upload, November
- Core asset-data MVP 1, Jan 15, 2027; enhanced asset capabilities MVP 2, Feb 15, 2027

**Accomplishments**
- Delivered global warranty, license, delivery and software attributes into DDP production.
- License renewal tracking live for Sales: 35 suppliers, 6,900 license parts, 1,337 renewal notifications to 238 North American reps as of October.
- Data Enrichment for Managed Services live October 30, first delivery by extract.
- Narrowed the system-of-record options for complex-build asset capture; decision with the GPOs.

**Next steps**
- Align the 2027 roadmap to the reduced development capacity.
- Deliver the asset-data MVP releases (January and February 2027) and enrichment V2 for Managed Services (target December).
- Resolve the complex-build capture path and system of record with the GPOs.
- Set the serial and MAC capture points with the data owners across the business.

## Decisions and sources behind the text

- 2026-11-09 (later, Darryl direct, per Chris Gazdic and Sean McCloskey): from Digital Products' perspective WAM is ADM, a DDP tool; ADM progress continues to be reported within the Wesco Asset Management program (no reporting split). Intelligent Asset Lifecycle Management services is the business offering (Amy Aguirre), Strev-based, not built on ADM; the team continues technical support for Strev where needed. Health Comment rewritten as three sentences and the capacity statement moved to Next steps (Darryl, 2026-11-09: the appended sentence made it far too long), and the same bullet placed on the Engle deep-dive WAM slide. Darryl applies it to the EPMO slide; the final PNG predates this change.

- Quarterly releases are named for the development quarter and ship at its end, landing in the next quarter; January 11, 2027 is the Q4 2026 release, not a slip (Darryl, 2026-11-09; `Products/entroCIM/entroCIM.md`).
- Q4 release scope: entroCIM 4.0, entroCIM DC ver. 2, entroCIM AI (Darryl, 2026-11-09).
- Ascent Navigator integration planned in 2027 for the Q4 2027 release (Darryl, 2026-11-09).
- Deployment strategy guide: Copilot extract of the 2026-10-29 email (Valli Poornakumar); Darryl confirmed it was reviewed in a meeting.
- Merck Rahway: "won" accepted; close-won processing was in progress on 2026-11-02.
- Ford: PO received; 2027 plan approval was pending buyer, so the approval is not stated.
- Training phrased without a course count because the October course status was not confirmed.
- Marketing website bullet removed at Darryl's direction.
- The MDM reporting change (Data Strategy & Governance to Sean McCloskey, 2026-11-06) was removed from the Health Comment: it read as a WAM team move, which has not been decided or communicated (Darryl, 2026-11-09). The dependency stays in `Products/WAM/WAM.md` and `W101`.
- Docker containerization bullet dropped (removed from the Engel deck 2026-10-19 as a standalone claim). Stanford omitted while the license roll-back is open. Data center value proposition (`A58`) kept off as an internal deliverable.
- WACT bullet reworded for the CEO audience (no internal system names); Darryl applied it to the slide 2026-11-09.
- WAM milestones and MVP dates: `Products/WAM/2026-10-30_WAM_Roadmap_Akansh_Gangil.pptx`.
- Figures and targets: taken by Darryl from the October John Engel deep-dive deck (entroCIM software $2.0M against $4.6M; pull-through $208K against $2.2M; WAM $29.7M against $14.3M, all September YTD). Record basis: finance workbook (software $2,035,463; pull-through $208,270; WAM $29,782,741, January to September 2026); scorecard figures from the Sales Operations October deck. Health colors on the final slide: entroCIM all green except Benefits red; WAM Overall and Schedule yellow, rest green; both trends flat.
