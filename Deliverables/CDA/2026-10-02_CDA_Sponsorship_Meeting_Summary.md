# CDA Business Case Review and Sponsorship: Meeting Summary

**Date:** 2026-10-02, 53 minutes (Teams)
**Attendees:** Darryl Benson; Bill Muczko (Global Enterprise); Bob Caprise (Senior Director, Sales, CSS); Peter Ferrell; David Fisher; Sridhar Loke (commercialization lead, Digital Products); Jay Maes (joined, no substantive remarks in the transcript)
**Source:** Teams transcript, `Products/CDA/05_Operating_Record/2026-10-02_CDA_Sponsorship_Meeting_Transcript.docx`
**Deck shown:** `2026-10-02_CDA_Product_and_Business_Case.pptx` (pro forma v4.6 figures, as an early pro forma)

## Outcome

Bill Muczko agreed, in the meeting, to be the business sponsor for CDA. This meets the condition Sean McCloskey set on 2026-09-15 before CDA advances. Darryl, who was in the room, states this directly and without qualification: Bill's agreement is not open to interpretation. The automated transcript capture ends shortly after Bill's "I think so too" and does not carry a cleaner closing quote; that is a gap in the recording, not a doubt about what was agreed. **Confirmed 2026-10-05 (Darryl, direct, chat).**

The room accepted the problem and the multi-vendor value. The challenges were about how CDA is priced at enterprise scale and how sellers explain it, not about whether it is worth doing.

## What was said, by theme

### Problem and value proposition

- No challenge to the core problem: devices degrade, drift out of support and accumulate cyber risk after the sale, and nobody is accountable for them.
- Bob's strongest framing, and the one most usable with sellers: customers bought a multi-vendor video platform (Genetec) because their estate is mixed, so they need a multi-vendor assurance service, not one manufacturer tool per brand. Axis and Hanwha each have their own; SecuriThings is the open alternative.
- Bob described three data layers per device: procurement and licensing, technical capacity (storage, compute, room for added analytics, power and cooling budget), and cyber. Different departments own each, and CDA joins them.
- Additional use cases raised by Bob: onboarding an acquired company's OT estate after a merger (Home Depot and SRS as his example), and Wesco's own branch estate.

### Seller readiness and the "what is the hook" question

- Peter Ferrell asked the question sellers will be asked: what does CDA do that the customer's VMS, Genetec or camera platform does not already do? Bob's answer: the VMS reports a camera offline; it does not report that the camera is two years past life cycle, out of license, or short of capacity, and it does not cover other vendors' devices.
- Peter's concern, in his words: if he is asking these questions, he is worried about what sellers will try to sell. Darryl committed to building the answers with the team and agreed a CDA versus VMS feature comparison could be created.
- Bob and Darryl agreed CDA has to be sold on outcomes, not technology. Bob's outcome examples, by vertical: grocery cold storage, pharma chain of custody for freezers (video, door hardware and temperature), hospitality "room ready" conditions, store closure and door status ahead of storms.

### Pricing at enterprise scale

- Peter Ferrell: the per-site packages work as a proof of concept or land offer, but enterprise deals will be negotiated. His example: banks with thousands of branches and fewer than ten cameras each, which do not fit a per-site package. Kroger will not pay about $10 a device across 60,000 devices.
- Enterprise buyers will expect a partner engagement, flexible device counts as estates grow and shrink, possibly an enterprise license, and clarity on whether service levels differ by alarm volume. Darryl's position on the last point: one service level for every customer.
- Bill: each location needs an appliance, so a site must have enough devices to justify one.
- Sridhar Loke: the pricing reads as cost-plus, and he wants to know whether market size and willingness to pay need more work before going further. He also asked whether Wesco can sell managed services at the scale the plan needs, since it has historically found that hard.
- Bob on the year-four choice (drop the fee, hold the margin percentage, or raise margin): "yes to the last."

### Accounts and channels

- Bill raised Walmart as a larger potential account than Kroger, with many more systems. David Fisher suggested refrigeration and produce systems as the entry point, reached through Wesco's MRO relationship, and offered to tee it up. Darryl's assessment after the meeting: a longer-term opportunity; it is too early in the development cycle to take CDA to Walmart.
- Bob proposed choosing anchor accounts from data: search for the accounts Wesco has shipped the largest volumes of edge devices to, since those estates are largely already reachable.
- Peter Ferrell covers banks.
- Bob named a new Universal contact, Luis Avello, whose program combines an asset-management platform with a DSIM component and a Datadog connector. If that pattern spreads, CDA may need to feed customer platforms such as Datadog as well as stand alone.

### Competition

- Homegrown tools built by customer DevOps teams (Bob: "Raspberry Pis"), Meraki in networking-led accounts, and SecuriThings. Bob's advice: understand each customer's DevOps position early, and aim CDA at the security, retail and building stacks rather than straight networking.
- Liberty AV device manager (Bob's suggestion to review): Darryl believes it is going away.

## Assessment

- **Sponsorship is secured. Product definition is the next risk.** The meeting produced more applications than CDA can carry at launch. Several of Bob's outcomes (cold chain, freezer chain of custody, room readiness) are entroCIM-scale integrations, not CDA's laser-focused service. Darryl's read: Bob is an excellent advocate whose enthusiasm needs to be channeled into a defined product. That definition needs to be written before the sales conversations set expectations.
- **Peter's pricing challenge is the most material finding.** It tests two settled positions: the published, held fee, and the per-site appliance. Small sites with few devices were already the weakest economics in the model. A small-branch estate needs a different delivery pattern, for example branches served from a regional collector rather than an appliance each, which is how entroCIM is deployed at Dell. That is an architecture decision as much as a pricing one.
- **Sridhar's willingness-to-pay question is fair.** The fees are set off a cost-built reference. No customer has yet been asked to pay them. The first anchor conversations are where that evidence comes from.
- **The seller answer exists in pieces.** "Multi-vendor assurance, not 17 tools" and the life-cycle, license and capacity gap the VMS does not report are the core of it. It needs to be one page before sellers use it.

## Decisions and open items

- **Decided:** Bill Muczko is CDA's business sponsor.
- **Open, Darryl:** enterprise pricing construct (volume, enterprise agreement, small-branch delivery without an appliance per site) to sit alongside the per-site packages.
- **Open, Darryl with the sponsor:** a seller value proposition with the CDA versus VMS comparison and two or three vertical outcome plays.
- **Open:** willingness-to-pay evidence from the first anchor conversations.
- **Open:** data-driven anchor selection from edge-device shipment volumes (Bob's suggestion; no owner named).

## Actions

| Action | Owner | Status |
|---|---|---|
| Send the deck as a PDF to attendees | Darryl ("I'll send you guys the PowerPoint") | Done 2026-10-02 |
| Walmart conversation (refrigeration entry via MRO) | David Fisher ("I'll tee this up") | Longer term; not before development matures |
| Report the sponsor to Sean McCloskey and set a review of the numbers | Darryl | Teams message drafted 2026-10-02 |
