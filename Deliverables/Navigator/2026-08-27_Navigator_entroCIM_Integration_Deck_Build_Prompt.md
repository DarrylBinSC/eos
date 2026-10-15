# Build Prompt: Navigator / entroCIM Integration Deck (Lisa Orton, DJ Vaughn, Darryl Benson)

**Status:** Revision 3, audited 2026-08-28 against the round-one frames and the Wesco template, with contradictions between sections 4 and 5 resolved. Previously revised twice on 2026-08-27: first to make the diagrams carry the message, then to add the value case, the CDA on-premises correction, the NavWork/NavIntel naming, and the confirmed facts below.
**Deliverable due to Lisa:** Thursday 2026-09-03.
**Owner:** Darryl Benson (Product Executive, Ascent Navigator and entroCIM).

---

## 1. Context

On 2026-08-27 Darryl met Lisa Orton, DJ Vaughn and Chris Askew (Head of IT, Ascent team) on the future of entroCIM and Navigator. DJ, Ron Snyder and Darryl have been discussing integration for several months. The meeting fixed a sequence and Lisa asked for a shared DJ/Darryl deck covering four items by 2026-09-03.

**The sequence, as stated by DJ (governing dates for this deck):**

| Date | Milestone |
|---|---|
| December 2026 | NavWork MVP complete, UAT begins |
| March 2027 | UAT complete, integration and migration begin |
| June 2027 | Maximo replacement complete |
| After June 2027 | In-depth entroCIM integration begins (API connection) |
| Before June 2027 | Interim connectivity: entroCIM connects to Ascent equipment over the Airwall at Ascent's St. Louis offices |

**Lisa's four items:** current state; interim state; end state with entroCIM and potentially WAM; Navigator quarterly roadmap through deployment and beyond, with priority coding, handled by DJ.

### Confirmed by Darryl, 2026-08-27

- **Purpose: explain to executives how the systems work today and how they will work together.** A picture is worth a thousand words.
- **Naming, and this resolves the block on drawing.** Navigator is the product. **NavWork is the software replacing Maximo. NavIntel is the new name of the current operations platform** (corrected 2026-08-28).
- **The deck must carry the value of the integration:** the distinct strength of each package, and the strength of them together.
- **CDA is shown as an on-premises device**, not as a cloud service.
- **The Ascent HQ Airwall will be running shortly.** POC status is no longer a blocker on the interim story.
- **The NavWork API is undefined as of 2026-08-28 and sits with DJ Vaughn.** Do not describe it as in development.
- **Ascent equipment in scope for the interim connection: metering and building automation.**
- **Funding: current operational funding, as a deployment project, with AOP capability next year.** This closes the earlier open funding question.
- Open tasks, owners and dependencies are handled in the weekly call and do not appear on the slides.
- The three-frame overview page is approved, provided each frame stands on its own.
- Roadmap page stays mostly blank. Pre-populate only what is known about NavWork timing.

---

## 2. Diagram tooling: recommendation

**Recommendation: draft in Mermaid, build in native PowerPoint shapes. Do not ship Mermaid renderings in this deck.**

The reason is specific, not stylistic. The design principle in section 4 requires the same nodes to sit in the same positions across three frames so the reader sees connections appear rather than reading three unrelated pictures. **Mermaid auto-layouts.** Adding an edge changes node ranking and shifts the layout, so frame B will not line up with frame A and frame C will line up with neither. The tool actively fights the one thing the deck depends on.

Native shapes in python-pptx are absolutely positioned. Frame A is built once, duplicated, and connections are added on top. Position constancy is then guaranteed rather than hoped for. Native shapes are also editable by DJ and Lisa, which a rendered PNG is not, and they inherit the Wesco template's fonts and colours rather than importing a second visual language into the deck.

**Where Mermaid still earns its place:** settling what connects to what, quickly, before anyone spends time on layout. Round one uses Mermaid so Darryl can judge the relationships and the line-status calls cheaply. Round two rebuilds the agreed content as native shapes.

**Visual reference: `Products/CDA/CDA_Exec_Brief.pptx`.** Darryl confirmed those diagrams work. That deck already establishes the vocabulary this one should reuse, and it is all native shapes on the Wesco template:

- Slide 10 is the architecture pattern to adopt for frames A, B and C: two large site panels (left at L=0.50 W=4.75, right at L=8.08 W=4.75, both T=1.25 H=5.07) with a middle column of connection bands (L=5.25 W=2.83) built as a rule, an icon, a capitalised label, and a plain-language sub-label. **This is exactly the structure the three frames need**, and it already reads at executive level.
- Slide 7 is the pattern for the value page: one anchor card on the left, arrows to stacked platform cards, arrows again to outcome cards, with a full-width takeaway banner beneath.
- Slide 13 is the pattern for the roadmap page: phase cards left to right with chevrons between them.
- Standing geometry across that deck: 13.333 by 7.5 inches, left margin 0.50, content width 12.33, title placeholder at T=0.74 H=0.47, a one-line subhead at T≈1.18 H=0.30, small caps section labels at H=0.26, and a full-width takeaway banner at the foot around T=6.2 to 6.45. Layout name to use: `Blank-with-Title`.

Match that geometry. The deck should look like it belongs beside the CDA brief.

**Limit of the slide 10 pattern, found on audit 2026-08-28.** CDA slide 10 is two panels joined by two panel-to-panel connection bands. Frames A and B fit that pattern exactly. **Frame C does not**: it carries fifteen node-to-node connections, which bands cannot express. Frame C keeps the same two panels and the same node positions, but its connections are routed arrows between specific shapes. It will be the densest page in the deck and that is acceptable, because it is the only page whose job is to show a loop closing. Route the CDA and WAM lines deliberately rather than letting them cross the middle.

**Template base.** `Products/CDA/CDA_Exec_Brief.pptx` and `Deliverables/Portfolio_Admin/2026-08-26_Product_Pitches_and_Soft_Metrics.pptx` were verified on 2026-08-28 to carry an identical slide master and the same 33 layouts, so either can be the base. Use the CDA brief, since its slides are the visual reference.

---

## 3. Goal

**One executive should understand the whole thing from the pictures alone, in order, without reading a bullet.**

1. **Make the gap visible.** Today the two platforms serve the same operation from opposite ends and do not connect.
2. **Make the two-phase sequence obvious as a picture.** One link before June 2027, the full set after it.
3. **Make the value legible.** What each package is strongest at, and what only becomes possible when they are connected.

---

## 4. Design principle: three frames of one picture

**The most important instruction in this document.**

The current state, interim state and end state pages are the same diagram at three points in time. Same positions, same colours, same vocabulary.

**Node rule, corrected 2026-08-28.** An earlier version of this document said "only the connections change." That is no longer true and following it would produce the wrong deck.

- **Frames A and B share an identical node set.** Metering and building automation, Airwall, Ascent Ops, NavIntel, Maximo, entroCIM, Wesco Operations. Nothing is added or removed between them. Only connections appear.
- **Frame C adds four elements** into space deliberately left empty in A and B: the connected device estate, the CDA appliance, WAM, and the Managed Services band. Maximo becomes NavWork in place, same position.
- **Reserve frame C's space when building frames A and B.** If the additions are dropped into leftover gaps at the end, the eye jumps between pages and the sequence breaks.

**Line treatment carries the honesty of the deck.** Four treatments:

- **Solid:** exists and runs today
- **Dashed:** committed and in build
- **Dotted:** planned, not designed or not funded
- **Open arrow with a person marker:** a human hand-off, not a system connection

**Time reference, and the deck is unbuildable without deciding it.** Treatment expresses status **as of today**, held constant across all three frames. It does not shift to each frame's own date. If it did, frame C would be entirely solid and the page would assert capability Wesco does not have. Held as of today, frame C reads correctly: one live connection, a small number of things in build, and a set of planned connections. That is the true picture and it is the reason the page can go to Dirk and Sean without a caveat.

**The human hand-off is its own treatment, added 2026-08-28.** Drawing a person-mediated step with the same line as a data link is a category error, and it hides the thing the deck is arguing about. Frame A's "observed by people" and frame B's "visibility and alarming, swivel-chair" are both humans doing integration work. Give them a distinct treatment so that their **disappearance in frame C is visible as a change**, not just as a missing arrow.

**Status table, corrected 2026-08-28 to match the relationships in section 5. The earlier version of this table still referenced WAM to Navigator and CDA into Navigator, which the 08-27 PM corrections superseded.**

| Connection | Treatment | Basis |
|---|---|---|
| Metering and BAS to Airwall to entroCIM | **Solid, runs today** | Darryl, 2026-08-28. Connecting to metering and building automation over an Airwall is entroCIM capability in production today, so it is drawn as running rather than as being built. What is new on frame B is that it reaches Ascent equipment, not that the capability is new. Superseded the earlier dashed call. |
| entroCIM to Wesco Operations and Support | **Solid** | Runs today. The only fully live connection anywhere in the three frames. |
| Ascent Ops to NavIntel to the work system | **Solid** in frames A and B (Maximo), **dashed** in frame C (NavWork is in build) | NavWork does not exist yet. **This is now the only dashed connection in the deck**, which is correct: it is the one thing genuinely under construction. |
| entroCIM to Ascent Ops, swivel-chair | **Human hand-off** | The person is the integration in the interim. Present in frame B, absent in frame C. |
| entroCIM to NavWork, condition becomes work over the API | **Dotted** | Begins after June 2027. Not designed. The NavWork API itself is in build, which is a different thing; that distinction lives in speaker notes, not on the diagram. |
| NavWork to entroCIM, asset and work status | **Dotted** | Same basis. |
| NavWork to NavIntel, entroCIM data surfaced through NavWork | **Dotted** | Same basis. |
| WAM to NavWork, and WAM to entroCIM | **Dotted** | No production data flow exists. Must never read as current. |
| CDA to entroCIM, and CDA to NavWork | **Dotted** | Pre-funding. |
| Metering and BAS to CDA, and CDA to the connected device estate | **Dotted** | Pre-funding. |

**Removed from this table on 2026-08-28: a row for "NavWork API surface, dashed."** No such element exists in the drawing; the API is a label on a dotted link. Promising an element the diagram does not contain is how a build goes wrong. The API-in-build versus integration-not-designed distinction is carried in the frame C speaker notes instead, where it belongs.

---

## 5. Page-by-page specification

Seven pages. Speaker notes on every page carry the narrative and the nuance; slide text is a headline and a small number of labels.

**Page count note for Darryl.** Lisa asked for four items and this is seven pages: title, overview, three frames, value, roadmap. The two additions are the approved overview and the value page. If seven is too many, the overview is the one to cut, not the value page, because the three frames still tell the sequence without it.

### Page 0. Title

- Title: Navigator and entroCIM: How the Systems Work, and How They Will Work Together
- Subtitle: Joint working draft, DJ Vaughn and Darryl Benson, for Lisa Orton
- One line on how to read it: three pictures, before and after, then the value, then the Navigator delivery roadmap.

### Page 1. Overview: the picture in three frames

**Purpose:** the executive summary page. For this audience it is likely the page that does the work.

Three small panels across the page, left to right: Today, Before June 2027, After June 2027. Each is a simplified frame carrying only the clusters and the connections, no detail labels. Beneath each panel, one short caption. Beneath all three, a single takeaway banner in the CDA slide-7 style.

**Each panel must read on its own**, per Darryl's condition. Test: cover the other two and the remaining panel still says something true and complete. If a panel only makes sense in sequence, simplify it until it does not.

Captions: "Two platforms, one operation, no connection." / "One link, and it reaches the Ops team." / "One connected portfolio, closing the loop."

### Page 2. Today

**Headline:** the two platforms serve the same operation from opposite ends, assets and work on one side, equipment and telemetry on the other, and today they do not connect.

**Frame A.** Two panels, nothing between them.

- Left, Ascent operated facilities: metering and building automation equipment; **the Airwall, already on site and not yet carrying entroCIM**; the Ascent Ops team; NavIntel as the Navigator front end; Maximo holding asset records, work orders, budgets and forecasts.
- The path from equipment to work runs through people: someone observes a condition, then enters it. Draw it with the human hand-off treatment, because its removal is what the deck is about.
- Right, Wesco CSS Platforms: entroCIM with OT and IoT connectors, telemetry, alarming, analytics; on premises and Wesco-hosted in Azure; Wesco operations and support.
- Middle column: empty, and **labelled rather than left blank**. Proposed: "No connection today. Equipment condition is not visible in the work system. Work is not visible to the platform."

**Speaker notes carry:** the Maximo forcing function (IBM ends on-premises support, Application Suite points model modelled at roughly ten times current subscription, approximately $3.98M avoided against a March or April 2027 renewal); the single-instance multi-tenant constraint; that the 2027 redesign and the Maximo replacement are the same project; entroCIM's two deployment modes and the Airwall and Arcbeam support paths; containerization as the confirmed forward deployment model.

**Author note.** The record carries no Navigator current-state architecture detail, customer base, or work-order and workflow boundaries, and NavIntel is a new fact with no supporting detail yet. Draw the Navigator side only as far as DJ has supplied it. Leave a shape out rather than invent it.

### Page 3. Before June 2027

**Headline:** entroCIM connects to Ascent's metering and building automation in St. Louis over the Airwall already on site, so the Ops team gets operational visibility now and the later integration is designed against how the operation actually runs.

**Label the entroCIM to Ops link "visibility and alarming, Swivel-chair"** (Darryl, 2026-08-27). Naming the swivel-chair is deliberate: in the interim the person is the integration, and saying so makes the end state's value measurable rather than rhetorical. Frame C's caption closes the loop on it with "No swivel-chair."

**Frame B.** Frame A plus exactly one new path, dashed.

- Ascent metering and building automation, to Airwall, to entroCIM. Label what it carries: telemetry, alarms, analytics.
- entroCIM to the Ascent Ops team, labelled **visibility and alarming, Swivel-chair**, drawn with the human hand-off treatment. **This link ends at people, not at a system.**
- Maximo unchanged and still unconnected. Work orders continue to be raised by existing process.

**The most important visual decision on this page:** the new link reaches the Ops team while Maximo still has no arrow. An executive should see that Ascent gains visibility and nothing in their operating model changes yet.

**Speaker notes carry:** that this is an operational adoption step and not a partial build of the end state; the two returns, usable visibility for Ascent Ops inside FY27 and an integration designed against the real operation; that this runs under current operational funding as a deployment project, with AOP capability next year.

### Page 4. After June 2027

**Headline:** a condition on equipment becomes visible, becomes work, and becomes an updated asset record, across one connected portfolio.

**Frame C.** Frame B, with Maximo replaced by NavWork in place, four elements added into reserved space, and the remaining connections added. Trace the flow; do not inventory the systems.

**Relationships corrected by Darryl 2026-08-27 PM. These are the durable target-state semantics, not draft choices.**

- Equipment to entroCIM over the Airwall: telemetry, alarms, analytics. Live by this point.
- **NavWork is the single integration point on the Navigator side.** entroCIM reaches NavIntel **through NavWork**, not directly. The front end stays a front end, and there is one interface to build, govern and support rather than several.
- entroCIM to NavWork: condition becomes work, over the API. Dotted.
- NavWork to entroCIM: asset and work status. Dotted.
- NavWork to NavIntel: entroCIM data surfaced through NavWork. Dotted.
- **CDA connects both ways and to both platforms:** device health and evidence into entroCIM, device risk into NavWork as work. Dotted.
- **Metering and building automation also feeds CDA**, alongside the connected device estate. CDA's coverage is not limited to cameras, access control and network gear at this site. Dotted.
- **WAM connects to both:** warranty, entitlement and install-base context to NavWork, asset and lifecycle context to entroCIM. Dotted.
- **CDA as an on-premises device at the Ascent site** (Darryl, 08-27): a small managed node on site, run from the Wesco cloud, covering the connected device estate for risk identification, monitoring, and firmware and configuration updates, feeding work into NavWork. Dotted. Draw it inside the site panel, alongside the equipment and the Airwall, not in the Wesco panel. The CDA Exec Brief slides 6 and 10 already carry this shape as the CDA appliance and the containerized service node.
- **The direct entroCIM to Ascent Ops link is removed in frame C.** Recommendation, needs Darryl's word: the Ops team sees entroCIM data in NavIntel, surfaced through NavWork, and the loop between the platforms is machine to machine. Keeping a direct "visibility and alarming" arrow would contradict the page's own caption, "No swivel-chair." If operators are expected to keep working directly in entroCIM for deep telemetry alongside the integration, say so and the arrow returns with a different label.
- Managed Services and the Ascent-led delivery model drawn as a band across the foot of the page, operating the whole thing, not as another box in the chain. Ascent-led service delivery, powered by CSS Platforms. **Drawing it as a node was tried in round one and produced lines crossing the entire diagram.**

**Mandatory framing, visible in the drawing and not only in the notes:** CDA is in support of Navigator's redesign integrations, in solidarity with the product, not competing with it. CDA is not built on entroCIM; it uses the same underlying platform, tools and expertise.

**Speaker notes carry:** which connections exist today, stated once and plainly. Current answer: none of them.

### Page 5. Value: each package, and the packages together

**Purpose:** the page Darryl added. Executives need to know why the integration is worth doing, not only what connects to what.

**Pattern: CDA Exec Brief slide 7.** Left column, the packages stacked with their distinct strength. Right, the outcomes that only exist when they are connected. Full-width takeaway banner at the foot.

**What each package is strongest at, one line each:**

- **NavWork** is where work is planned, assigned, costed and closed. The system of record for assets, work orders, budgets and forecasts.
- **NavIntel** is how the operation is seen. The Navigator front end for the Ops team. *(Detail to be confirmed by DJ; this is a new fact with no supporting record. An earlier draft said "and the customer," which Darryl never stated. Removed 2026-08-28.)*
- **entroCIM** is the only package that touches the equipment directly and knows its condition now. Metering, building automation and wider OT and IoT telemetry, alarming and analytics, with secure site connectivity already solved.
- **WAM** knows what the asset is, what it is entitled to, and when that runs out. Lifecycle, warranty, entitlement and install-base visibility.
- **CDA** keeps the connected devices themselves trustworthy and current. Risk identification, continuous monitoring, and controlled firmware and configuration updates, delivered from an on-premises device.
- **Managed Services and Ascent-led delivery** is what makes someone accountable for the outcome rather than for a tool.

**What they produce together, framed as target outcomes and not as realized benefits:**

- The swivel-chair goes away. Equipment condition becomes scheduled work without a person reading one screen and typing into another.
- Asset records stay current, because the work that touched the asset and the telemetry coming from it both update the same record.
- Refresh and renewal become evidence-based rather than calendar-based, because condition, entitlement and failure history finally sit together.
- The connected device estate stays trustworthy, because firmware and configuration are managed rather than assumed.
- One accountable operating layer, rather than four tools and the people who reconcile them.

**Takeaway banner, the line the page exists to deliver:** each package is useful on its own; connected, they close the loop from a condition on a piece of equipment through to work completed, the asset record updated, and the next refresh decision informed. **No one of them closes that loop alone.**

**Discipline on this page.** These are planned outcomes. Do not attach numbers, do not imply any of it is running, and do not let a benefit statement drift into a commitment. Separate planned from realized, per the standing rule.

### Page 6. Navigator roadmap

DJ's page. **Mostly blank by design** (Darryl, 08-27). Darryl supplies the frame and the NavWork timing; DJ supplies the lanes and the priority coding.

**Frame: the three phases DJ named**, which is also the deck's spine used a fourth time.

- **Phase 1, MVP:** through December 2026
- **Phase 2, UAT, integration and migration:** December 2026 through June 2027
- **Phase 3, post-cutover:** after June 2027, where the entroCIM API integration sits

**Checked on audit 2026-08-28:** the Wesco template does ship roadmap layouts, `Roadmap with Stages`, `Roadmap with Icons` and `Timeline with Numbers`. All three are stage-based with a fixed number of steps and no lane structure, so none of them can carry workstreams by quarter. That confirms the styled-table approach below rather than leaving it as an assertion.

**Form: a swimlane timeline, not a table.** Build it as a styled PowerPoint table so DJ edits by typing into cells, with the timeline reading coming from styling rather than from drawn objects. **No SmartArt and no free-floating shapes**; both are close to unmaintainable in someone else's hands. Phase bands across the top in the CDA slide-13 style, milestone markers beneath them, then lanes.

**Time axis, with declining precision stated rather than faked:** quarters from Q4 2026 through Q4 2027, then halves for H1 and H2 2028. A uniform quarterly grid across two years would read as eight equally firm commitments.

**Pre-populate only NavWork timing:**

- MVP build through Q4 2026, MVP complete December 2026
- UAT from December 2026, complete March 2027
- Integration and migration from March 2027
- Maximo replacement complete June 2027
- IBM Maximo renewal decision point, March or April 2027

**Everything else stays blank.** Name the lanes so DJ knows the shape of the answer without inheriting anyone's guesses. Proposed lanes: NavWork delivery; data and migration; entroCIM connectivity and integration; Ascent Ops adoption; commercial and portfolio. Detail gets added once DJ fills in his part.

**Priority coding** is applied by DJ, per Lisa. Supply the legend: three levels, shown as a marker inside the cell as well as by colour, so the page survives printing and colourblind readers.

---

## 6. Constraints

- **No em dashes anywhere.** Minimal bold in slide text.
- **Text discipline is tight because the diagrams carry the message.** One headline sentence per page, no more than four short labels, nothing past one line. Narrative lives in speaker notes.
- Never state or draw a planned capability in the present tense.
- No owners, dates, asks or open-item lists on any slide.
- Do not name this system, the Executive Operating System, anywhere in the deck or in any outbound message.
- Build on the Wesco template, `Blank-with-Title` layout, matching the CDA Exec Brief geometry in section 2.
- Do not invent dates, metrics, names or outcomes.
- Mermaid drafts follow `Reference/Mermaid_Standards.md` and use the Intent, Assumptions, Validation Items, Exclusions template.

---

## 7. Author validation items (weekly call, not the deck)

1. ~~Does NavIntel persist after NavWork lands?~~ **Closed 2026-08-28: it persists.** NavIntel is the renamed current operations platform, reached through NavWork in the target state.
2. **What will the NavWork API expose, and when is that design fixed?** **Confirmed undefined as of 2026-08-28 and in DJ's court.** Until it is defined, the frame C link stays dotted and the speaker notes say undefined rather than in build. **DJ.**
3. **Which metering and building automation systems are in scope, and by make?** Determines whether the frame B equipment node can be named or stays generic. **DJ, with Chris Askew on the connection path.**
4. **Confirm the funding characterisation before it reaches Dirk or Sean:** current operational funding as a deployment project, AOP capability next year. Stated by Darryl 08-27; worth one confirmation given it will be quoted back.
5. **Navigator current-state detail** remains thin in the record. Anything drawn on the Ascent side of frame A should be DJ's, not inferred.

---

## 8. Output format

**Round one, for Darryl's review, no PowerPoint:**

- Three Mermaid frames presented together so the progression is judged as a sequence, each with Intent, Assumptions, Validation Items, Exclusions.
- Headline sentence and label set for each page.
- Page 1 overview described as a layout sketch.
- Page 5 value content in full, since it is text-led and needs wording review.
- Page 6 roadmap as a Markdown grid standing in for the timeline.
- Speaker notes drafted in full.

**Round two, after sign-off:**

- `Deliverables/Navigator/2026-08-28_Navigator_entroCIM_Integration_Working_Deck.pptx`, built with python-pptx as native shapes on the Wesco template, matching CDA Exec Brief geometry. Reissue with a new date on each substantive revision.
- Frames A, B and C built once and duplicated so node positions are identical by construction.
- Page 6 as a native editable table.
- Speaker notes embedded on every page.
- A short covering Teams message to DJ and Lisa in Darryl's voice: what is drafted, what is DJ's, what the weekly call picks up.

---

## 9. Validation criteria

- **The three frames read as one picture changing**, not as three diagrams. Frames A and B share an identical node set; frame C adds four elements into space reserved in A and B. Positions and colours are constant throughout.
- Each overview panel stands on its own when the other two are covered.
- An executive can follow the story from the pictures alone.
- The line-status key appears on every frame and every connection has a deliberate treatment matching the table in section 4.
- Frame B's new link ends at people, drawn with the human hand-off treatment, and Maximo still has no arrow.
- Human hand-offs are visually distinct from data links on frames A and B, and are visibly absent from frame C.
- Line treatments express status as of today on all three frames, not status as of each frame's date.
- CDA appears as an on-premises device inside the site panel, and the in-support-of-Navigator framing is visible in the drawing.
- The value page separates each package's strength from the combined outcome, and every combined outcome reads as planned rather than realized.
- Page 6 is mostly blank, carries only NavWork timing, and DJ can edit it by typing.
- Nothing is drawn or written in the present tense that does not exist today.
- No owners, dates, asks or open items on any slide. No em dashes. No reference to this system by name.
