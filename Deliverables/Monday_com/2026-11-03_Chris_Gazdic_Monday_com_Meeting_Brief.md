# Monday.com Handover: Chris Gazdic Meeting Brief

Prepared 2026-11-03 for Darryl's meeting with Chris Gazdic. Internal working brief; not for distribution. Source basis: `Products/Monday_com/Monday_com.md`, the 2026-10-29 Company and Product Brief (audited), the 2026-10-29 Copilot deep dive, and `06_Stakeholder_Map.md`.

::: {custom-style="Bottom Line"}
**Bottom line:** Chris is the outgoing Product Executive and an ally. The meeting should establish what Darryl is taking over (scope, people, money, dates), confirm Chris's own read of the platform, and agree the handover mechanics. Everything else is already researched; what is missing is the facts only Chris, Procurement and the two owners hold.
:::

## Purpose of the Meeting

Three outcomes:

1. Confirm the transfer and its scope: whether Chris has heard it from Sean, what ownership covers (product-executive role, platform administration, licensing and renewal), and the effective date.
2. Settle the people question: whether Brittany Pearce and John Magee move with the product, stay under Jim Lenart and Chris, or go to Sridhar Loke's commercialization organization as Sean floated on 2026-09-01.
3. Agree the handover: what Chris hands across, who introduces Darryl to the owners and the vendor, and how the FY27 Run cost line is treated.

## What Is Known About the Product

Facts below are graded. "Reported" means found in a document or transcript but not confirmed against the primary record.

**Position and ownership.** Monday.com is one of five Run products on the August 2026 Digital Product List, with Chris as Product Executive alongside eProcurement and Prokeep. Sean told Darryl verbally on 2026-10-29 that he will add it to Darryl's portfolio. Nothing is in writing. Confirmed.

**Deployment.** 962 licenses in the August deck: CSS 485 (50%), Marketing 279 (30%), EES 168 (17%), EECOL 30 (3%). Sean said "850 or so" and Chris "just over 1,000" on 2026-09-01; licenses grew from 144 at the start of 2026. Half the seats are already in Darryl's own business unit. Reported, counts conflict.

**Role in the tool stack.** Planview for enterprise portfolio management, Jira for IT software development, Monday.com for task and workflow management, QPM and FTTX for transactional project work. Stated architecture: USD/CRM is the sales front door, Monday.com is the services workflow and project execution layer. Reported (August deck, CSS strategic update).

**Contract.** "Currently on a 3-year contract," Enterprise tier (TrackIt WAB deck, 2026). A prorated add-on quote implies about 2.75 years remaining in mid-2026, so a start around Q1 2026 and renewal around early 2029. That is Claude's arithmetic, not a found date. Not found anywhere in M365: the executed agreement, order form, renewal date, notice period, annual value, Guardian add-on, account executive or CSM. No Wesco contract owner identified; commercial terms sit with Procurement.

**Security.** Tenant-level encryption and BYOK approved by WAB September 2025 and implemented October 2025; transition to Wesco-managed keys targeted end of August 2026, completion not evidenced. File upload disabled 2026-08-17 for all groups except EECOL, which still depends on it for customer documents. L&D licenses to be consolidated into the managed tenant; completion not evidenced. Two security risk assessments in 2026 for the TrackIt add-on. Data on the platform classified Confidential. Reported; the program is largely executed, not complete.

**AI.** "Following AI Council guidance, we are no longer moving forward with Monday.com AI"; the pivot is a Copilot API integration so sales teams reach project updates without additional licenses. The stated reason (file upload could not be disabled) was addressed on 2026-08-17, so the position may be revisited. Confirmed in the August deck; the Copilot route's design and owner are not found.

**Integrations.** The only API connection is SharePoint file storage (February 2026). CRM/USD push-pull needs solution architecture, the MuleSoft pattern and WAB approval. Sean, 2026-02-12: no DDP release planned for Monday.com in 2026, likely 2027. The August deck then states DDP integration as the direction; status not stated. Reported.

**Vendor.** Healthy balance sheet ($1.4B run rate, $1.07B cash, Gartner Leader 2026) in a turbulent year (20% workforce cut, withdrawn 2027 target, class action, shift to seats-plus-AI-credits pricing from May 2026). Q3 results due 2026-11-09. Vendor viability is not the risk; the renewal moving onto consumption pricing without caps is. Public sources, audited 2026-10-29.

## What Is Known About the People

| Person | Role in the record | What Chris can settle |
|--|--|--|
| Brittany Pearce | Senior Manager, Portfolio, Digital Products and Business Models. Monday.com lead, "historically reporting to Chris" (Sean). Author of the access SOP. Product/Application owner on the TrackIt WAB deck. Sits under Jim Lenart on the org chart | Does she move with the product, and where was the Sridhar Loke discussion left |
| John Magee | Senior Developer, Brittany's one direct report. "Part project manager, part developer" for CSS implementations; CSS-only and CSS-funded (Sean) | Does the CSS funding line move with him; what is his time allocation |
| Jim Lenart | Manager, Agile Practice, between Chris and Brittany on the chart | Any role in Monday.com, or chart order only |
| Sridhar Loke | Commercialization organization Sean discussed moving Brittany into (2026-09-01) | Whether that is still live; it conflicts with the move to Darryl |
| Graham Russ | Authored the TrackIt WAB deck; Technical Services time and capacity use case for 140+ engineers | Who owns the TrackIt add-on going forward |
| Procurement (unnamed) | Holds the commercial terms; no named contract owner found | Who the contract owner and the vendor account team are |

Both owners were at Monday.com Elevate '26 (New York, 2026-10-28 and 29). First contact with them follows this meeting; eight questions for them are already drafted in the research brief.

## Questions for Chris

Only the questions whose answer depends on Chris's knowledge; the research is done.

1. Has Sean spoken with you about moving Monday.com to my portfolio, and what did he say the reason is?
2. What does ownership cover in your mind: the product-executive seat only, or administration and the commercial relationship as well?
3. What is the effective date, and what happens to the FY27 Run cost line and budget?
4. Do Brittany and John move with the product? Where did Sean's September discussion about Sridhar Loke's organization land?
5. Who holds the contract today, who is the vendor account executive or CSM, and do you know the renewal date and annual value?
6. What is unfinished that you would want me to know: the Wesco-managed-key transition, the L&D tenant consolidation, EECOL's document path, the DDP integration, the Copilot API route?
7. What are the governance gaps as you see them? Sean named use-case approval, adoption measurement, training, security and DDP migration on 2026-09-01.
8. How would you like the handover to run: a joint session with Brittany and John, your introduction to the vendor team, and anything you want to keep?

## Proposed Next Steps

| Step | Owner | Timing |
|--|--|--|
| Confirm scope, date and people with Sean in writing after this meeting | Darryl | This week |
| Introductory session with Brittany Pearce and John Magee (Elevate debrief, current-state walkthrough) | Darryl, Chris to introduce | Week of 2026-11-09 |
| Obtain the order form and executed agreement from Procurement: term, renewal, notice, annual value, tier, pricing model | Brittany, via Procurement | Before 2026-11-30 |
| License and usage census: member, viewer and guest mix by group; active users; API and automation consumption | John Magee | Before 2026-11-30 |
| Add Monday.com to the Copilot intake prompts and the Products roster once Sean confirms | Claude | On confirmation |

::: {custom-style="Decision Required"}
**Decision required (Sean McCloskey, not Chris):** scope of ownership, effective date, and whether Brittany and John transfer. Chris's answers inform the ask; Sean makes the call. Target: before the first session with the owners.
:::

## Handling Notes

- Chris is an ally (Darryl, 2026-10-07) and was Product Executive for this product through the security program and the AI Council decision. Frame the meeting as continuity, not takeover; ask what he wants preserved.
- Do not present the early-2029 renewal date as fact. It is inferred from a prorated quote.
- The license count conflicts in the record (850, 962, just over 1,000). Ask for the authoritative source rather than choosing one.
- The 2026-09-01 Sridhar Loke thread is the one point where Sean's stated intentions may not line up. Raise it neutrally; Chris may know more than the transcript shows.
- Name spelling: the record carries "Gazdic" from his email signature and the org chart.
