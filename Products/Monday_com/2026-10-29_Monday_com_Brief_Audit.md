# Monday.com Brief Audit

Audit of /home/claude/reports/2026-10-29_Monday_com_Company_and_Product_Brief_v2.md and the four designed pages (Main, Product, Wesco, Ownership) against the six research notes and the M365 evidence file, 2026-10-29. Line numbers refer to the brief file.

## Verdict

Fit to send after the listed corrections. The brief is well sourced: every financial figure, list price, credit rate, API limit, Gartner placement and Elevate date checked against the primary URLs matches, and the Wesco material tracks the M365 evidence closely, with the contract-term inference correctly labeled. What needs fixing before it leaves Darryl's desk is a small set of items that would be caught by a careful reader: one stock figure that is wrong on its face ($317 described as the 52-week high when the cited page says $210.49), a stale "80% below peak" figure that the body itself contradicts, two Wesco stack details on the designed Wesco page that appear in no source, a handful of inferences stated as fact (vendor will migrate the contract at renewal; AI Council position "retires" the agent risk; "completed" security program), one internal contradiction on the renewal timing (early 2029 renewal versus a "natural negotiating window" in December 2026), and a few pipeline and spelling items. None of these change the conclusions. Fourteen must-fix items follow, most of them single-sentence edits.

## Must fix

1. Line 91, Restructuring Timeline table, "still far below its $317 52-week high." Wrong figure. The cited Gotrade page (re-checked 2026-10-29) gives the 52-week range as $57.50 to $210.49. The $317 figure is the 52-week high reported by TIKR in May 2026; that window has rolled. Also in the same cell, "Up roughly 80% from its April low" is not on the Gotrade page ($97.82 against the $57.50 low is 70%); the roughly 80% figure comes from Globes, 2026-10-25, which is not in the Sources list. Corrected wording: "Up roughly 70% from its 52-week low of $57.50; still less than half its 52-week high of $210.49 and well below the $317 high of 2025."

2. Line 27, Summary, "Lost roughly 80% of its peak market value," and Main page six-number tile "-80%, Share price from peak." Stale as of the date of the brief. The "more than 80% from peak" statement is Globes on 2026-07-22, before the recovery; at the 2026-10-28 close of $97.82 the stock is about 69% below the $317 high of 2025 and 53% below the 52-week high. The body (line 91) does not support "80%" as a current figure. Corrected wording for the Summary bullet: "Fell more than 80% below its peak by July before recovering; still roughly 70% below its 2025 high." Corrected tile: "-70%" with caption "Share price below 2025 high; Q3 results due 2026-11-09."

3. Wesco page, stack diagram: "Planview: Project Place, Agile Place" and "Jira: metrics to DDP deliverables." Neither appears in the M365 evidence, wesco_internal_context.md or any research note. The evidence names only Planview for enterprise portfolio management and Jira for IT software development. Remove both sublabels. (ProjectPlace and AgilePlace are real Planview product names, which makes an unsourced claim that Wesco uses them more dangerous, not less.)

4. Line 281, Elevate '26: "there are repeated sessions on AI governance and AI cost management [monday.com IR, 2026-09-29]." Misattributed. The IR release (re-checked) names no governance or cost-management sessions; those come from the Elevate 2026 agenda page, which the brief cites elsewhere. Corrected citation: "[Elevate 2026 agenda]." Keep the "every attendee builds an agent" clause on the IR citation, but note the release says every attendee "will have the opportunity to build" one.

5. Line 256, Vibe and Agents: "full-page apps over up to 20 boards ... [monday.com support, Get started with vibe]." The cited support article says up to 5 boards; 20 boards is the Vibe Growth plan (25 apps, $250 per month) per the June 2026 community post and the Till Freitag blog. Corrected wording: "over up to 5 boards (20 on the Growth add-on)."

6. Line 243, Credit Pricing table: Enterprise agent usage "Exempt 'until a later transition date' that has not been announced." The quoted words are not on the support page, which says "Enterprise plans are currently exempt, and will transition to credit-based usage at a later date." Corrected wording: Exempt now; "will transition to credit-based usage at a later date" that has not been announced.

7. Line 440, AI: Already Decided: "This retires the agents-and-vibe-apps governance risk the public research raised, as long as the AI Council position holds." Overstated and inconsistent with the brief's own first-90-day question 4, which asks whether any Sidekick, agent or vibe usage exists in the tenant despite the position. The evidence records a decision not to move forward with Monday.com AI; it does not record that AI features were disabled at account or workspace level, and Sidekick is free on Enterprise. The stated reason for the decision (inability to disable file upload) has since been addressed by disabling uploads on 2026-08-17, so the premise may be revisited. Corrected wording: "This sets the governance risk the public research raised to one side for now. The AI Council position is a decision, not a technical control; whether native AI is disabled in the tenant has not been evidenced, and the reason given for the decision (file upload could not be disabled) was addressed on 2026-08-17, so the position may be revisited."

8. Line 537, Conclusion: "Wesco's completed security program." Not evidenced as complete. The BYOK transition to Wesco-managed keys (targeted end of August 2026) and the L&D tenant consolidation have no completion evidence (brief lines 431, 432; M365 evidence section 4). Corrected wording: "Wesco's largely executed security program."

9. Lines 8 (Bottom Line, "a renewal that migrates the contract to consumption pricing on the vendor's terms"), 29 (Summary, "existing customers will be moved onto over 'a couple of years'") and 537 (Conclusion, "will treat Wesco's renewal as a chance to move the account onto its new model"). Inference stated as fact, and contradicted by line 234, which correctly says earlier customers "are not auto-migrated and opt in through their account team." The source (support article; Q1 2026 call) says existing customers can opt in, with incentives, over a couple of years. Corrected wording: Bottom Line, "a renewal at which the vendor will push the account toward consumption pricing"; Summary, "a seats-plus-AI-credits model that existing customers are being encouraged to opt into over 'a couple of years'"; Conclusion, "and can be expected to use Wesco's renewal to move the account onto its new model." Main page "What is changing" bullet 1 carries the same "migrate" wording; change to "are being moved to opt in."

10. Line 537, Conclusion: "The November 9 results and December quarter-end create a natural negotiating window," against line 499 (Implications): the contract "appears to run to about early 2029" so "the near-term exposure is the add-on and expansion quotes rather than the base renewal." These conflict as written. Corrected wording for the Conclusion: "The November 9 results and December quarter-end create a natural window for the add-on and expansion quotes that are live now, and for any early restructuring of the base agreement, if the contract dates confirm what the WAB quote implies." The Ownership page already hedges this ("negotiating window if a renewal is near"); the brief should match.

11. Line 185: "No FedRAMP authorization exists [monday.com Trust Center FAQs]." The source is absence of evidence (no FedRAMP Marketplace entry; the FAQ makes no statement). Corrected wording: "No FedRAMP authorization was found; the Trust Center makes no government-authorization statement."

12. Line 528, Questions for the Owners: "the mandatory agent-building session." The IR release says every attendee "will have the opportunity to build" an agent. Corrected wording: "the agent-building session offered to every attendee."

13. Line 420: the backtick-wrapped role name `Monday.com_Viewer` is in the body, which the pipeline rules do not allow outside Sources. Corrected wording: "a Monday.com_Viewer role for read-only access" in plain text (or "a dedicated viewer role").

14. Line 451: "Use-case catalogue" is UK spelling. Corrected: "Use-case catalog."

## Should fix

1. Line 98: "would not recover because AI-generated search had damaged it." CTech reports executives said the SMB segment "won't recover soon." Add "soon."

2. Line 120: "A user who needs edit rights in two products consumes two paid seats [monday.com support, User types]." The support article defines product non-members; the two-seat consequence is the researcher's inference (product_pricing.md, Inferences). Corrected: "The product non-member definition implies that a user who needs edit rights in two products consumes two paid seats."

3. Line 159: "the account is almost certainly on Enterprise plus Guardian for at least the managed tenant." The only basis is a third-party hardening guide stating BYOK sits in Guardian, and the M365 search for Guardian returned nothing. Corrected: "Wesco has implemented tenant-level encryption and BYOK on AWS, which a third-party hardening guide places in the Guardian add-on, so the account is probably on Enterprise plus Guardian for the managed tenant. Nothing in Microsoft 365 confirms Guardian."

4. Line 73 and its Source Note: "Guided to about 108% by year-end" is from the Q2 call (MarketBeat summary), not the Q2 release (re-checked: the release does not state 108%). Add [MarketBeat, Q2 2026 call summary] to the Source Note.

5. Line 444 and Wesco page: "The only API connection today is SharePoint file storage [Kayla Steward, email, 2026-02-09]." "Today" overstates a February 2026 statement framed as her understanding. Corrected: "As of February 2026 the only API connection, by Kayla Steward's account, was SharePoint file storage."

6. Line 35 (Summary) and Wesco page "What Wesco's records already settle" bullet 3: "two security risk assessments in 2026" are listed as tenant hardening. Both assessments (2026-05-29, 2026-06-22) were for the TrackIt add-on, as line 433 says. Corrected: "two security risk assessments in 2026 for the TrackIt add-on."

7. "Sevenfold" (lines 501, 537; Main page "about sevenfold"). The arithmetic is 144 to 962 (6.7x), to "850 or so" (5.9x) or to "just over 1,000" (6.9x), all on reported, unreconciled counts. Corrected: "grew roughly sixfold to sevenfold in 2026 on the counts reported" or simply "grew from 144 to about 1,000."

8. Main page, "Leadership turnover: ... five VP departures reported October 2026." CTech names four VP-level people and one Senior Director, and one of the VPs left in September. Corrected: "five senior departures reported October 2026, four at VP level."

9. Wesco page footer: "Wesco facts: August 2026 Deep Dive, slides 17 and 18." The 17 and 18 are line references in the Copilot evidence file's citation markers, not confirmed slide numbers. Drop the slide numbers.

10. Ownership page, "Day 90: Governance owner and credit budget set." Two problems: the brief (line 470) says a credit budget is needed only if the AI Council position changes, and Darryl's stated preference is that a briefing does not carry deliverable dates assigned to him. Corrected: "Day 90: contract facts, usage facts and governance owner settled," or remove the Day 90 row.

11. Main page header: "Public sources as of 2026-10-29 and the August 2026 Wesco deck." The page also uses the 2026-09-01 transcript and the WAB quote, which came from the M365 deep dive. Match the brief's line 11.

12. Line 79: "management has stopped pretending otherwise." Editorial; reads as commentary rather than briefing. Corrected: "and management now says so."

13. Lines 488 and 489: "holds a favorable position" and "means implementation help is a negotiable inclusion" are the notes' inferences ("likely in a favorable position"; "negotiable inclusions"). Corrected: "likely holds a favorable position"; "suggests implementation help is a negotiable inclusion."

14. Line 424, Ownership: the brief never states that the August deck names Christopher Gazdic as Product Executive for Monday.com, which is the role Darryl is taking over; the Wesco page does. Add a first bullet: "The August deck names Christopher Gazdic as Product Executive for Monday.com, with all SBUs impacted [August Deep Dive deck]."

15. Lines 38 to 40 and 499: the commercial decisions are framed as the owner's. The M365 evidence lists the Wesco contracting or procurement owner as not found. Add "with Procurement" to the commercial-terms decision so the brief does not imply Darryl signs.

16. Line 145: "Anything above 40 users requires a quote." The pricing page says "If you want to sign up more than 40 users, you can request a quote." Corrected: "Quotes are offered above 40 users; Enterprise is quote only."

17. Product page: "Not PCI-DSS" appears on the page but not in the brief. The notes support it (Trust Center FAQ: billing via a certified third-party processor). Either add to line 183 of the brief or drop from the page; the two must agree.

18. Line 333: "no independent case of a large enterprise replacing Monday.com or Asana with Planner was found [Forrester blog, Q2 2025 Wave]." The Forrester blog supports only the first clause (Microsoft not among the eleven vendors). Move the citation after "Wave" and leave the second clause uncited as a research finding.

## Observations

1. Contract-term inference (line 404). The arithmetic is right ($26,812.50 / $9,750 = 2.75) and the brief labels it an inference. Two caveats worth knowing: the WAB deck is dated only "2026" (the SRAs on 2026-05-29 and 2026-06-22 suggest June), so the end date could fall anywhere from early to mid 2029; and the proration may be to a co-term date rather than to contract end, in which case the inference collapses. The "confirm against the order form" instruction already covers this.

2. Line 427, "No Microsoft 365 artifact records the handoff to Darryl." Sean McCloskey will have context for this, but if the brief goes to him it reads as a note that his verbal decision is undocumented. Consider cutting, per Darryl's preference to omit items the reader has no context for or that raise a question they never had.

3. Line 398 explains the Copilot deep-dive method. Darryl's preference is to cut methodology from executive material; a single clause ("from Wesco's own Microsoft 365 records") would do.

4. Line 21 states the Gartner positioning ("highest on both axes") as fact; the Wesco page correctly says "per the vendor reprint." The Gartner report is paywalled and the wording is monday.com's. Not wrong, but the Summary could carry the same qualifier.

5. Items per board (10,000 and 100,000, line 165) come from the support article "Item and subitem limits per board," which is not in the Sources list; the table's Source Note cites the pricing page and the Administration article. The figures are correct.

6. Boards per dashboard (20 and 50, line 168) are not on the current work-management pricing page (re-checked); they are in the notes from the pricing page's product tabs and the developer platform-limits page. Figures correct.

7. Line 111 attributes "which became the Harmony voice-sales product" to the SEC 6-K; the link from OneAI to Harmony is from The Next Web, 2026-10-19 (not in Sources). Figures correct.

8. Line 90 lists four roles for five departures. The fifth is a Senior Director, Global IT and Workforce Technology; one VP R&D left in September.

9. The 2.75-year inference and the "early 2029" renewal, if confirmed, mean the "AI Transformation Package promotional rate" (line 518) and the "special offer" discount (line 250) matter for add-on quotes rather than the base renewal. The brief's Implications section already draws this distinction.

10. "Darryl" first-name usage and the "Prepared for Darryl Benson" line are fine for a document that may be shared upward.

11. No instances of "PODs," prospect names, or entroCIM styling issues. US spelling is otherwise consistent ("license," "organization," "analyze," "allowlisting").

12. The designed pages otherwise agree with the brief on every checked figure (prices, credit rates, limits, license split, security dates, Gartner placement, Elevate dates).

## Primary-source re-check table

| Figure | Brief value | Source value (re-checked 2026-10-29) | URL | Result |
|---|---|---|---|---|
| Q2 2026 revenue and growth | $364.6M, up 22% | $364.6M, 22% YoY | ir.monday.com Q2 2026 release | Match |
| Non-GAAP operating margin, Q2 2026 | 17% | 17% ($61.1M) | ir.monday.com Q2 2026 release | Match |
| Adjusted FCF, Q2 2026 | $52.3M | $52.3M, 14% margin | ir.monday.com Q2 2026 release | Match |
| RPO | $937M, up 34% | $937M, up 34% | ir.monday.com Q2 2026 release | Match |
| Cash and securities | $853M plus $219M | $853.4M plus $219.4M ($1,072.8M) | sec.gov exhibit_99-2 | Match |
| H1 2026 buybacks; authorization | $735M; exhausted | $734.97M; full $870M used | sec.gov exhibit_99-2; IR release | Match |
| NDR overall and enterprise | 109%; 115% | 109%; 115% for >$100K | ir.monday.com Q2 2026 release | Match |
| NDR year-end guide | about 108% | Not in release (from call summary) | ir.monday.com Q2 2026 release | Attribution only |
| Customers >$100K, >$500K | 2,019 (+37%); 114 (+68%) | 2,019 (+37%); 114 (+68%) | ir.monday.com Q2 2026 release | Match |
| FY2026 and Q3 guidance | $1,466M to $1,474M, 19 to 20%; 16 to 17% | Same | ir.monday.com Q2 2026 release | Match |
| Layoff size | 620 to 630, 20%, 350 in Israel | About 620 (body), about 630 (letter), 20%, about 350 Israel | en.globes.co.il article-1001550113 | Match |
| Co-CEO quotes | "most painful decision ..."; "not the organization that is suitable ..." | Verbatim | en.globes.co.il article-1001550113 | Match |
| Stock close 2026-10-28 | $97.82 | $97.82 | heygotrade.com MNDY | Match |
| 52-week high | $317 | $210.49 (low $57.50) | heygotrade.com MNDY | Discrepancy (Must fix 1) |
| Q3 results date | 2026-11-09 | November 9, 2026 | heygotrade.com MNDY | Match |
| OneAI acquisition | $14.1M cash, May 2026 | $14.1M cash, May 11, 2026; goodwill $9.85M | sec.gov exhibit_99-2 | Match |
| Goodwill at 2025-12-31 | Zero | None | sec.gov exhibit_99-2 | Match |
| List prices | $9 / $12 / $19 / quote | $9 / $12 / $19 / custom | monday.com/pricing | Match |
| Minimum users; quote threshold | 3; above 40 | "start from 3 users"; "more than 40 users, you can request a quote" | monday.com/pricing | Match (wording, Should fix 16) |
| Actions per month, Pro and Enterprise | 25,000 each; 250,000 each | 25,000; up to 250,000 | monday.com/pricing | Match |
| AI credits included, Pro | 3,000 | 3,000 | monday.com/pricing | Match |
| Enterprise SLA | 99.9% | 99.9% uptime SLA | monday.com/pricing | Match |
| Credit model effective date | 2026-05-06 | Joined on or after May 6, 2026 | support.monday.com 35277848309394 | Match |
| Credit rates | 8; 120 per hour; 10 to 250+; 10 to 500 | 8; 8; 120; 10 to 250+; 10 to 500 | support.monday.com 35277848309394 | Match |
| Sidekick | Free, "will be monetized in the future" | "currently does not consume credits, but it will be monetized in the future" | support.monday.com 35277848309394 | Match |
| Enterprise agent exemption | "until a later transition date" | "currently exempt, and will transition to credit-based usage at a later date" | support.monday.com 35277848309394 | Quote not verbatim (Must fix 6) |
| Vibe apps included, Enterprise | 5 | 5 live apps | support.monday.com 35277848309394 | Match |
| Credit alerts | 80% and 100% | 80% and 100% | support.monday.com 35277848309394 | Match |
| API daily calls, Enterprise | 25,000, failures count | 25,000; "All requests count ... even those that fail" | developer.monday.com rate-limits | Match |
| Queries per minute; concurrency | 5,000; 250 | 5,000; 250 | developer.monday.com rate-limits | Match |
| Gartner CWM | Leader, fourth year, furthest Vision, highest Execute | Same; three of seven use cases highest; top three in all seven | ir.monday.com 2026-10-08 | Match |
| Elevate '26 dates and venue | Oct 28 and 29, Javits Center | October 28 to 29, 2026, Javits Center | ir.monday.com 2026-09-29 | Match |
| Governance and cost sessions | Attributed to IR release | Not in release (agenda page) | ir.monday.com 2026-09-29 | Attribution (Must fix 4) |
| Done Awards criteria | time saved, errors reduced, output scaled | "hours saved, errors reduced, and output scaled" | ir.monday.com 2026-09-29 | Match |
| "monday Frontier" | Announced at Elevate, investor Q&A, scale through 2027, mid-market and enterprise | Same, via Elevate investor Q&A | marketbeat.com 2026-10-28 | Match |
| Zinman hybrid-model quote; 3x enterprise adoption | As stated | Verbatim; three times, relative basis | marketbeat.com 2026-10-28 | Match |

## Statistics

- Word count (brief, including front matter and Sources): 7,389
- Em dashes (U+2014): 0 in the brief; 0 across the four designed pages
- En dashes (U+2013): 0 in the brief; 0 across the four designed pages
- H1 count: 1
- Headings: all noun phrases (one with a colon, "AI: Already Decided," which is acceptable)
- Tables: 14; maximum columns 4; tables without a following Source Note: 0
- Bottom Line callout: 1 occurrence
- Risk callouts: 3
- Backticks or file paths in the body outside Sources: 1 (line 420, Must fix 13)
- UK spellings found: 1 ("catalogue," line 451, Must fix 14)
