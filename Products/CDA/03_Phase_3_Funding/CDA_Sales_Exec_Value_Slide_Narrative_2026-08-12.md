# CDA — Sales Executive Slides: narrative, talk track, and build notes
Created 2026-08-12 | Deliverables: `CDA_Customer_Value_Slide.pptx` and `CDA_Why_Wesco_Slide.pptx` (standalone, deck template applied) | Audience: sales executives, non-technical, no entroCIM background | Purpose: give them a customer story they can carry, plus the credibility argument, in support of a commitment to sell 2 to 3 pilots

Sequence when both are used: value slide first (what the customer gets), credibility slide second (why we can deliver it). The ask stays verbal on both.

## Design decision

One slide, two registers. The top row answers "what actually happens at the customer's site" in four plain steps. The bottom row answers "what does their business get," which is the position Darryl wants staked out. A closing band answers "why us and not a tool vendor." Pricing is off the slide and out of the talk track. entroCIM, Airwall, Arcbeam, RMM, and the partner sensor are not named; they carry no meaning for this audience and invite technical questions the slide is not built to answer.

Rules applied from the 07-27-28 rulings: no pricing, partner sensor unnamed, targets stated as targets. New for this audience: no platform names, no architecture, no internal program language.

## Slide text as built

Title: What the customer gets, and how it works
Kicker: The connected devices we sell them stay under control after the sale, and Wesco is accountable for it

ON THEIR SITE: WHAT WESCO DOES

1. We connect once. A small Wesco-managed appliance on their network, or a secure remote connection. Nothing for their team to install, learn, or staff.
2. We find every device. Cameras, access control, and network gear inventoried automatically: model, firmware version, support status, known vulnerabilities.
3. We watch it continuously. Security posture and device health tracked daily, not sampled once a year. Issues reach them as prioritized work, not raw alerts.
4. We fix it, on approval. Firmware and configuration changes run remotely, validated and documented. Anything needing hands on the device becomes a field visit.

WHAT THEIR BUSINESS GETS

- Less downtime, fewer truck rolls. Faults surface before failure, and eligible ones are cleared remotely. Target is 25 percent or more resolved without a site visit; the pilot sets the real baseline.
- A security answer they can defend. A current device inventory, continuous posture, and evidence of every action taken. This is what CISA asset-inventory guidance asks owners and operators to produce.
- One accountable owner, not five tools. Each manufacturer's utility is free only if someone runs it. They get one interface, one service level, and Wesco answerable for the outcome.
- A funded plan for the estate. What is out of support, what keeps failing, what to replace and when. Refresh becomes a budgeted plan instead of an emergency.

Closing band: Why they buy it from us: we sell the devices, we hold the manufacturer relationships, and we can carry a problem from detection through remediation to replacement and installation. No tool vendor spans that path.

## Talk track (also in the slide's speaker notes)

Open on the relationship, not the technology: they already sell these devices, and today the relationship ends at installation. This service extends it for the operating life of the device and pays recurring.

The consolidation argument, for the objection that the manufacturer tools are free: five free tools nobody operates cost more than one interface someone is accountable for. Say it plainly; it is the strongest counter in the room.

Plain-language definitions if pressed. The appliance is a small managed computer that sits on the customer network and talks to the devices. It can also run from the Wesco cloud over a secure link with nothing on site. Do not name the underlying platform.

What not to promise. The 25 percent remote-resolution figure and the avoided-visit savings are planning targets to be calibrated in the pilot, not results. Say target, and say the pilot sets the baseline. No pricing, on the slide or verbally.

The expansion point, useful on strategic accounts: the secure connection and verified device inventory this service establishes are the same ones Wesco asset management and facility services need, so the customer can expand later without a second onboarding.

The ask, delivered verbally: their support to name and sell 2 to 3 pilot accounts, with a commercial sponsor for each. Scope per pilot is camera-led, 2 to 5 sites, 250 to 1,000 devices, 16 weeks.

## Slide 2 — Why us (credibility)

Title: Why us: the hard parts already exist
Kicker: The platform, the team, the device integrations, and the secure site connections exist today. The new build is the box in the middle.

WHAT WE ALREADY HAVE (four cards)

- An established platform. entroCIM serves real customers today, on a quarterly release cadence, with a mature connector library.
- Device integration is the day job. Connecting other manufacturers' devices and getting data out of them is this team's normal work.
- Secure customer connections. We reach into customer sites securely today, and the containerized delivery work is funded and underway.
- Install base and service delivery. WAM carries lifecycle and warranty visibility. Managed Services already operates recurring services for customers.

ALREADY BUILT, IN PRODUCTION

- Hanwha camera connector, live in entroCIM today
- Axis camera connector, live in entroCIM today
- The two camera lines the pilot targets are already connected. The device conversation is proven, not theoretical.

WHAT WE NEED TO BUILD (three-part diagram)

Customer devices (cameras first, then access control and network gear) to the CDA box (one small managed node per site, or run from the Wesco cloud; this is the new build) to Wesco service delivery (operators, approvals, work queue, evidence and reporting, plus refresh signals to Sales).

Under the box, what it delivers: device connection and inventory; cyber assurance, posture and vulnerabilities; firmware tracking and controlled updates; health monitoring, alerting, service evidence.

Right-hand close: what the box delivers is the whole product. Everything to its left and right is already ours.

Claim discipline on this slide. The connector claim is device connection and data retrieval in production entroCIM (confirmed by Darryl 2026-08-12; note that the transcribed entroCIM roadmap slide lists Hanwha only, so a reviewer working from that slide may query Axis). Per-manufacturer firmware update rights remain in qualification, so "already connected" is supportable and "already updating firmware" is not. Say the connectors are live; do not imply the firmware workflow is.

## Two things to resolve before these slides are used in front of sales

1. **Pilot count.** The record carries one pilot customer, then three to five accounts in production (`CDA_Business_Case_Working.md`, Expected Benefit). A commitment to sell 2 to 3 pilots changes delivery load, partner terms, and the account-sponsor ask. Decide whether 2 to 3 becomes the plan of record, or whether the sales commitment is "2 to 3 qualified candidates, one contracted pilot."
2. **Timing.** The corrected timeline (Darryl, 2026-08-11) puts development and validation across the first eight months of 2027, with an approval gate in August 2027 and the pilot following. Slide 7 of `CDA_Sean_Review_Deck.pptx` still shows the superseded sequence (AOP August 2026, funded validation Q4 2026, pilot H1 2027). Do not put pilot dates in front of sales executives, or in front of a customer, until that slide is corrected and the gate is reflected.

---

*Editorial notes: title shortened to fit the template's single-line title box. Body copy held to four lines per card at 9.5pt to match the deck's density. The CISA reference is stated as what guidance asks owners and operators to produce, per the accuracy note in the business case; NIST and the EU CRA are deliberately absent because neither places a duty on the customer.*
