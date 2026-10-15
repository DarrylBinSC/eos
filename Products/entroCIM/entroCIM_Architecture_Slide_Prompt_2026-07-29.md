# Prompt: entroCIM One-Page High-Level Architecture Slide

Created 2026-07-29, revised same day with Darryl's confirmations: Airwall is used for entroCIM cloud connectivity (customer site to Wesco-hosted instances); on-premises deployments do not use Airwall; exactly two deployment options exist (on-premises and cloud); Arcbeam is used for services and support enablement for on-premises deployments; Quest migration is not surfaced, the slide says Azure only. Companion to the WAM ("One service, one platform: clear boundaries") and CDA ("Services delivered on platforms we own") slides. Decisions locked 07-29: audience = executive/AOP register; scope = current architecture with future items explicitly marked; SkySpark shown as named foundation layer per settled positioning; layout = CDA style (Customer Site vs Wesco split with secure links between).

---

# Context

entroCIM is a mature operational-technology and facility-intelligence platform, 10+ years in market with an established installed base. It is never positioned as new or experimental. In the portfolio, entroCIM provides operational intelligence; WAM provides asset-lifecycle and commercial intelligence.

Settled positioning language (do not deviate): entroCIM-developed UI, graphics, and workflow applications run on SkySpark's data-and-analytics foundation (database, time-series, semantic modeling, FDD). SkySpark is commercially licensed, open via APIs, protocols, and standards; it is not open-source and the UI is not "powered by SkySpark."

Deployment model (confirmed by Darryl 2026-07-29): two options, on-premises and cloud. Cloud deployments are Wesco-hosted instances in Azure; the customer site connects over an Airwall link. On-premises deployments run on customer infrastructure and do not use Airwall; Arcbeam provides services and support enablement for on-premises deployments.

The audience is executive (AOP register: Engel, McCloskey, Naylor tier). The AOP audience rule applies: anything reading as expansion draws pushback. Frame everything as sustaining a mature platform. Growth narrative belongs to Connected Device Assurance, not this slide.

Two reference slides define the visual language:

1. WAM slide: light gray side panels, white/dark platform blocks, green accent for the service layer, italic takeaway line at the bottom, Wesco logo bottom-left.
2. CDA slide (the structural model for this slide): left panel = CUSTOMER SITE (light gray), right panel = WESCO (light gray), vertical connection zone between them with labeled secure links (green lock icon motif), dark navy blocks for named components, slate blue for partner/supporting components, green for the highlighted Wesco capability, dashed-border boxes for future items, a full-width takeaway strip at the bottom, confidentiality footer if required.

# Task

Produce a single 16:9 slide, one page, titled for the executive read (working title: "entroCIM: one platform, two deployment options" — improve if a sharper sustaining-framed title emerges). Same visual language as the WAM and CDA slides.

## Slide content specification

**Left panel — CUSTOMER SITE**

- Building and OT systems block (dark): BAS/HVAC, metering, security, sensors, data center infrastructure. Subtitle: integrated through the entroCIM connector library (examples only if space allows: Hanwha, Panduit, SafeTrust, ServiceNow).
- On-premises entroCIM instance block (slate, current): full platform on customer infrastructure; same applications and SkySpark foundation as the cloud option. Label clearly as Deployment Option 1.
- Future item (dashed border): containerized entroCIM node on small PC or customer server. Label as direction, not capability. One line: extends the Docker containerization work already underway.

**Center — connection zone** (two links, both current, visually parallel to the CDA slide's link pairs)

- Airwall secure link: cloud deployments; customer site systems to Wesco-hosted entroCIM instances. Applies to the cloud option only.
- Arcbeam link: services and support enablement for on-premises deployments. This is how Wesco reaches and supports Option 1 instances.
- SAML 2.0 SSO callout, one line: Wesco servers authenticate via SAML SSO; some customers use SSO as well.

**Right panel — WESCO**

- Wesco-hosted entroCIM in Azure (highlighted green block, the anchor of the slide). Label clearly as Deployment Option 2. Say Azure only; do not mention Quest or migration. Two internal layers mirroring the ADM/Strev split on the WAM slide:
  - entroCIM applications and experience layer (dark): entroCIM-developed apps, graphics, dashboards, workflows (Tiles/Gridboard, Collection, Bookmark, Connector apps).
  - SkySpark data-and-analytics foundation (slate): time-series database, semantic modeling, analytics, FDD. Commercially licensed.
- Services and support block (dark): remote monitoring, product support, and Managed Services enablement; platform foundation for Intelligent Facility Services. Word carefully: enablement, not an operating Managed Services business. Product support is owned by the entroCIM team; Managed Services operating ownership is an open decision, so do not draw an MS ownership box.
- WAM link block (outline style, like the CDA slide's Managed Services note): entroCIM operational intelligence sits alongside WAM's asset-lifecycle intelligence in the portfolio. One line only; this is a portfolio pointer, not an integration claim. [Do not draw a data-flow arrow between entroCIM and WAM unless Darryl confirms one exists.]

**Bottom takeaway strip**

Sustaining-framed, one sentence. Working version: "A mature platform, 10+ years in market, deployed on-premises or in the Wesco cloud: 2027 investment sustains reliability and converts the installed base into scalable services." Adjust wording but keep the sustaining frame and the current-vs-future honesty.

**Footer:** Wesco logo bottom-left. Confidentiality marking: [Darryl to confirm; default INTERNAL, not the CDA strictly-confidential strip].

# Goal

An executive reader understands in under a minute: what entroCIM is architecturally, the two ways it deploys, how Wesco connects and supports each, what SkySpark actually provides, and which elements are future direction rather than current capability. The slide supports the 2027 AOP sustaining narrative without implying expansion.

# Constraints

- No em dashes anywhere on the slide. Minimal bold in text blocks.
- Slide bullets one line each, never past two.
- Never present a future item as current. Dashed border plus a "future" or "direction" label on every non-shipped element. The only future item on this slide is the containerized node; Airwall and Arcbeam are current and drawn solid.
- Keep the two deployment options visually distinct; a reader must not conclude Airwall applies to on-premises deployments or that Arcbeam applies to cloud.
- No hype vocabulary (world-class, game-changer, best-in-class, leverage as a verb).
- Do not name this system (EOS) or reference internal working files on the slide.
- Do not import commercialization-deck language (Infrastructure Lifecycle Intelligence, incubation, scale-up); that vocabulary is out of AOP-register material by the 07-24 decision.
- Do not invent connectors, versions, dates, or mechanisms. Use [placeholders] where a fact is unconfirmed.
- Wesco visual identity per the reference slides: Wesco green accents, dark navy, slate blue, light gray panels, white background.

# Source Material

- `Products/entroCIM/entroCIM.md` (architecture section; positioning; support-ownership ruling 07-15; auth clarification 07-16; deployment and connectivity confirmations 07-29)
- `Products/entroCIM/entroCIM_Roadmap.md` (app names, integration names)
- `Products/entroCIM/Wesco_entroCIM_Commercialization_v7_Review_2026-07-28.md` (settled SkySpark positioning language)
- `Reference/Communication_Preferences.md` (slide standards, AI-tell rules, product framing)
- WAM and CDA reference slides (visual language)

# Required Analysis

Resolved 07-29 (Darryl): connectivity mechanisms (Airwall for cloud, Arcbeam for on-prem services/support), two deployment options, Quest not surfaced.

Resolved 07-29 (Darryl, second pass): no entroCIM-to-WAM data flow exists today, integration is on the roadmap (WAM shown as dashed roadmap block); confidentiality marking is on the Wesco template.

Closed 07-29 (Darryl): Arcbeam's services and support enablement role for on-premises deployments confirmed by Darryl directly; Ron Snyder review not required. No open items remain on this slide.

**Executed 2026-07-29:** slide built natively in `Products/entroCIM/entroCIM Architecture.pptx` (Wesco template, theme colors and Titillium Web/Source Sans Pro fonts), speaker notes included.

# Output Format

One-page 16:9 slide matching the WAM/CDA visual language. If a Wesco-template .pptx deck is provided, build the slide natively in that deck matching its theme fonts and colors; otherwise render standalone in the same medium as the reference slides. Plus:

- Speaker notes: 5 to 8 sentences covering the definition and nuance behind each block, including the SkySpark licensing point, the two deployment options with their distinct connectivity, and the current-vs-future distinction.
- Below a `---` line: editorial choices made, placeholders remaining, and the validation items still open with owners.

# Validation Criteria

- The two deployment options are unambiguous, and each connectivity mechanism is tied to the correct option.
- The only dashed/future element is the containerized node; everything else drawn is current capability with evidence in the source files.
- SkySpark described only with the settled language; nothing says or implies "powered by SkySpark."
- No Quest or migration references.
- Sustaining frame holds: no expansion vocabulary, no growth claims.
- Readable in under one minute; passes the AOP audience rule.
- No em dashes; bullets within length limits; no EOS references.
