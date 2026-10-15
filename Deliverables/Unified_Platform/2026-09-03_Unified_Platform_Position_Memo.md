# Unified Platform — Position and Recommended Path

**For:** Brad Stevens, Lisa Orton · **From:** Darryl Benson · **Date:** week of 2026-09-08 · **Status:** Darryl's position for discussion, not a decision taken

## Recommendation

Adopt a **common commercial front door** now, name a **shared identity spine** as the architectural direction and fund one small first step, and **rule out a merged product**. Run the four adoption plays below in parallel on their own owners and dates rather than holding them behind the platform question. The platform decision that matters this week is not what to build; it is agreeing which of four different things "unified platform" means.

## The inventory, corrected

| On the list | Correction | Commercialized today |
|---|---|---|
| entroCIM | — | **Yes.** In market 10+ years, established install base |
| WAM | — | **Yes.** Production and selling |
| "AMD" | Read **ADM**. ADM and Strev are the two components *of* WAM, not a peer platform | Counted inside WAM; do not count separately |
| Connected Safety | Strategic placeholder. Boundaries, architecture and deployments unvalidated; program in limbo pending a leadership replacement | **No** |
| CX Connect (Liberty) | Not held anywhere in the CSS record. Ownership, function, install base and commercial model all unconfirmed | **Unknown** |
| Navigator | Operations platform running Ascent's own managed services business. Not a Wesco software sale | **No.** Internal |
| *Missing* | **Connected Device Assurance.** FY27 AOP line of $246,787, and the only platform in the portfolio carrying fresh external sales validation (Mooney and Muczko, 2026-08-28) | Not yet. 2027 build and validation year |
| *Also in scope* | Spanr, CMP | No |

**Two of the six named are commercialized.** That is the sequencing argument: unification is premature for four of them, and the effort spent unifying an unvalidated placeholder is effort not spent converting the two that are already in market.

## Four things "unified platform" can mean

They are not variations of one another. They carry different costs, owners and timelines.

| | What it is | What it costs | Verdict |
|---|---|---|---|
| **1. Commercial front door** | One name, one portfolio story, one way to sell and package the set | Marketing and sales enablement. No product change | **Do now** |
| **2. Common experience** | Single sign-on, shared navigation, consistent interface across products | Per-product front-end work. Moderate, and it can be sequenced | Opportunistic, product by product |
| **3. Shared identity and services layer** | The same customer, site, asset and device identified the same way in every platform, over shared services for identity, connectivity and entitlement | Real engineering, but incremental, and it makes the integrations already on the roadmap cheaper rather than competing with them | **Adopt as the direction. Fund one step** |
| **4. Merged product** | One codebase | Three business cases | **Rule out** |

**Why a merged product fails, on three facts.** entroCIM is a ten-year install base built on a commercially licensed SkySpark data and analytics platform, deployed both on customer infrastructure and in Wesco Azure. Navigator's entire case is a dated IBM Maximo renewal falling due March or April 2027 and roughly $3.98M avoided, funded and operated by Ascent, and it cannot join a merge before the replacement completes in June 2027. WAM's customer-facing layer is Strev, a white-labeled third-party platform we do not own. A merge destroys three funded business cases to produce one unfunded one.

## What to build instead: the identity spine

What the portfolio is missing is not a platform. It is agreement on **how a customer, a site, an asset and a device are identified.** Today each platform answers that differently, and every integration on the roadmap pays that cost separately: entroCIM into NavWork from Q4 2027, WAM into NavWork, CDA into both. Paid once, it makes each of them cheaper, and it is the precondition for a common experience later without a merge.

**First step, small, fundable now, no product roadmap changes.** One cross-platform identity definition for customer, site, asset and device, agreed by the four product teams, with WAM's ADM as the reference implementation since normalization and enrichment already live there. Sixty days to a written definition and a named owner. If we cannot agree that, we certainly cannot agree a platform.

## The four plays, which do not wait on the platform question

| Play | First step, and it is a fact rather than a decision | Owner | By |
|---|---|---|---|
| **CX Connect** | Establish what it is, who owns it, its install base and commercial model. Then size the Converging Technologies AV monitor-and-manage demand. The WAM integration and NOC managed-service questions cannot be answered before those two | Darryl, with Ed (Liberty) | 2026-09-19 |
| **Integrated FM / DC service pitch** | Agree a written capability boundary, current versus planned with dates, before the integrated story goes in front of a customer. The 2026-08-26 pitch package already carries the agreed language | Darryl and Brad | Before first customer use |
| **Ascent third-party ALM** | Name the product and the coverage gap before proposing displacement. Ascent runs a live 24x7 operation in the middle of the Maximo replacement | Ben Pesek, DJ Vaughn | 2026-09-19 |
| **WAM in the Service Center** | Scope the Irving and Dacula pilot on central funding. Decide the internal charging model on measured benefit, not before it exists | Darryl, Manny, Finance | Pilot scoped by 2026-10-03 |

## Two risks worth naming in the room

**The integrated pitch is ahead of the build by roughly eighteen months.** No production data flows between any two of these platforms today. entroCIM integration support in NavWork begins Q4 2027 on DJ Vaughn's published roadmap and facility connectivity lands Q2 2028, both gated on the Maximo replacement completing June 2027. A deal closed in 2026 on integrated capability lands as unfunded custom work or as a swivel-chair the customer was not told about.

**CX Connect and CDA may be the same bet.** Monitoring and managing installed devices behind a customer firewall, sold as a managed service, is the CDA thesis. If CX Connect does that for AV, the portfolio is about to fund one capability twice. This is worth establishing before either is sold against a Converging Technologies opportunity.

## What I need from this group

1. **Agreement on which definition we are pursuing.** Recommendation: front door now, identity spine as the direction, merged product ruled out explicitly so it stops being the default reading of the phrase.
2. **An owner for the unified platform work, with stated authority.** I will co-own the architecture answer. What I cannot do is carry an architecture obligation across products I do not fund.
3. **Central funding for the Service Center pilot**, with the internal charging model deferred until the pilot produces a measured benefit.

*Source record: `Products/Unified_Platform/Unified_Platform.md`. Open items tracked in `03` Decision Radar, `04` Active, and `05` Register A38 to A40.*
