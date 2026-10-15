# Design Brief: Navigator and entroCIM Deck Diagrams

**Portable handoff package. Self-contained by design.** Written 2026-08-28 for use in Claude Design or any other tool with no access to the originating conversation. Everything needed to explore visual alternatives for this deck's diagrams is in this document.

**Scope of the exploration: visual form only.** The content, the relationships between systems, the line-status meanings and the wording are settled and are not open for redesign. What is open is how the pictures look and lay out.

---

## 1. Context

Wesco's CSS Platforms group runs entroCIM, an OT and IoT telemetry, alarming and analytics platform. Ascent, a Wesco business delivering data centre and mission-critical facility services, runs its operations on Navigator. Navigator is being rebuilt: NavWork replaces IBM Maximo, and Navigator Intelligence is the live visibility and reporting layer.

The two platforms serve the same customer operation from opposite ends and do not connect today. A sequence has been agreed to connect them. A deck of eight pages explains this to Wesco executives (Dirk Naylor, Sean McCloskey). It is authored jointly by Darryl Benson, the Product Executive for both entroCIM and Ascent Navigator, and DJ Vaughn, who runs Navigator delivery.

**The deck's purpose, in the author's words: explain to executives how the systems work today and how they will work together. A picture is worth a thousand words.** The diagrams carry the message. Slide text is a headline and a handful of labels; the narrative lives in speaker notes.

---

## 2. Naming, exact and non-negotiable

Getting these wrong makes the deck wrong. They are not interchangeable.

| Term | What it is |
|---|---|
| **Navigator** | The platform, the product name overall |
| **NavWork** | The software replacing Maximo. Assets, work orders, budgets, forecasts. In development, MVP December 2026 |
| **Navigator Intelligence** | The live visibility and reporting layer over the operation. Sometimes abbreviated NavIntel in working notes, but spelled out on slides |
| **Maximo** | IBM's product, the current operational system of record, being replaced |
| **entroCIM** | Wesco's OT and IoT telemetry, alarming and analytics platform |
| **WAM** | Wesco asset management. Lifecycle, warranty, entitlement, install base |
| **CDA** | Connected Device Assurance. An on-premises appliance covering device risk, firmware and configuration |
| **Airwall** | Secure site connectivity appliance, already installed at the customer site |
| **Ascent Operations Team** | The people running the operation. Shortened to "Ascent Ops" |

Two rules that have already caused rework:

- **CDA is not built on entroCIM.** It uses the same underlying platform, tools and expertise. It exists in support of Navigator's redesign, not in competition with it.
- **Do not name a specific site.** An earlier version said "Ascent St. Louis"; the panel is now a generic customer site so the picture holds for any Ascent facility.

---

## 3. The core design principle

**Three frames of one picture.** Three diagram pages show the same system at three points in time. Same node positions, same colours, same visual vocabulary. Only the connections change, plus one node substitution and four additions.

| Frame | Caption | What changes |
|---|---|---|
| A | Today | Two clusters, nothing joins them |
| B | Now through 2027 | One new path appears, and it ends at people |
| C | From Q4 2027 | The full set of connections. Maximo becomes NavWork in place. Four elements appear |

**Frames A and B share an identical node set.** Frame C adds four elements into space deliberately left empty in A and B: the connected device estate, the CDA appliance, WAM, and a Managed Services band. **Reserve that space when laying out A and B.** If the additions are dropped into leftover gaps, the eye jumps between pages and the sequence breaks.

This principle is why the current build uses absolutely positioned native shapes rather than an auto-layout tool. An earlier Mermaid draft was abandoned because adding edges re-ranked the graph and frame B stopped lining up with frame A.

---

## 4. Line treatments, and why they are not styling

Four treatments. They are factual claims about status, not decoration.

| Treatment | Meaning | Current appearance |
|---|---|---|
| **Solid** | Exists and runs today | Dark slate, 1.5pt |
| **Dashed** | Committed and in build | Amber, 1.75pt |
| **Dotted** | Planned. Not designed or not funded | Purple, 1.25pt |
| **Human hand-off** | A person doing the integration work, not a system connection | Grey long-dash, with a small pill on the line reading "person" |

**Status is expressed as of today and held constant across all three frames.** It does not shift to each frame's own date. If it did, frame C would be entirely solid and would assert capability Wesco does not have.

Consequences worth knowing before redesigning:

- **Dashed appears exactly once in the whole deck**, on the Ascent Ops to NavWork to Navigator Intelligence path in frame C, because NavWork is the one thing genuinely under construction. That is correct and the eye should go there.
- **The human hand-off treatment is the deck's argument.** It appears in frames A and B and is visibly absent in frame C. Its disappearance is the change the deck exists to describe. Any redesign must keep that disappearance legible.
- A legend appears on every diagram page, labelled "Status today".

---

## 5. Exact node inventory and connections

Two panels. Left is the customer site, right is Wesco. A corridor between them carries cross-panel connections and, in frames A and B, a note box.

### Nodes

**Left panel, "Ascent Customer Site"**

| Node | Label | Frames |
|---|---|---|
| Metering and Building Automation | two lines | A, B, C |
| Airwall on site | one line | A, B, C |
| Connected device estate | "cameras, access control, network" | C only |
| CDA appliance | "on-premises device" | C only |
| Ascent Operations Team | people | A, B, C |
| Navigator Intelligence | "visibility and reporting" | A, B, C |
| Work system | "Maximo" in A and B, "NavWork" in C, both with "Assets, work orders, budgets, forecasts" | A, B, C |

**Right panel, "Wesco CSS Platforms"**

| Node | Label | Frames |
|---|---|---|
| entroCIM | "OT and IoT telemetry, alarming, analytics" | A, B, C |
| Wesco Operations and Support | people | A, B, C |
| WAM | "Lifecycle, warranty, entitlement, install base" | C only |

**Managed Services and Ascent-led delivery** is a band across the foot of frame C, not a node. It was tried as a node and produced lines crossing the entire diagram.

### Frame A connections

| From | To | Label | Treatment |
|---|---|---|---|
| Metering and BAS | Ascent Ops | observed by people | Human |
| Ascent Ops | Maximo | work entered by hand | Solid, routed under the row |
| Maximo | Navigator Intelligence | record, then dashboards and reporting | Solid |
| Navigator Intelligence | Ascent Ops | (same label) | Solid |
| entroCIM | Wesco Operations | telemetry, alarms, analytics | Solid |

Corridor note: "NO CONNECTION TODAY. Equipment condition is not visible in the work system. Work is not visible to the platform." **The absence of a cross-panel line is the point of the page.** Label the gap; do not leave it blank.

### Frame B connections

Everything in A except the Metering-to-Ops human link, which is replaced, plus:

| From | To | Label | Treatment |
|---|---|---|---|
| Metering and BAS | Airwall | metering and BAS data | Solid |
| Airwall | entroCIM | secure link | Solid |
| entroCIM | Ascent Ops | visibility and alarming / Swivel-chair | Human, with the person pill |
| Ascent Ops | Maximo | work orders unchanged, still raised in Maximo | Solid, under the row |

Corridor note: "ONE NEW LINK. Ascent Ops gains visibility now. Nothing in the operating model changes yet."

**The most important visual fact on this page: the new link ends at people, and the work system still has no connection to the platform.** An executive should see that Ascent gains visibility and nothing in their operating model changes yet.

### Frame C connections

| From | To | Label | Treatment |
|---|---|---|---|
| Metering and BAS | Airwall | metering and BAS data | Solid |
| Airwall | entroCIM | secure link | Solid |
| entroCIM | Wesco Operations | telemetry, alarms, analytics | Solid |
| Metering and BAS | CDA appliance | device data | Dotted |
| CDA | Connected device estate | risk, firmware, configuration | Dotted |
| CDA | entroCIM | device health and evidence, over the same secure connection | Dotted |
| CDA | NavWork | device risk becomes work | Dotted |
| entroCIM | NavWork | condition becomes work, API / asset and work status | Dotted, bidirectional |
| WAM | NavWork | warranty, entitlement, install base | Dotted |
| WAM | entroCIM | asset and lifecycle context | Dotted |
| Ascent Ops | NavWork | work entry | Dashed, under the row |
| NavWork | Navigator Intelligence | entroCIM data surfaced through NavWork | Dashed |
| Navigator Intelligence | Ascent Ops | (same path) | Dashed |

**There is deliberately no direct entroCIM to Ascent Ops link in frame C.** The swivel-chair is gone, which is the point of the page. Restoring that arrow would contradict the page's own headline.

**NavWork is the single integration point on the Navigator side.** entroCIM reaches Navigator Intelligence through NavWork, never directly. Every external connection lands on NavWork.

---

## 6. Current geometry and palette

The deck is built with python-pptx on Wesco's corporate template, 13.333 by 7.5 inches. Geometry follows an existing Wesco deck (a Connected Device Assurance executive brief) so the two sit together.

**Standing geometry, inches**

- Left margin 0.50, content width 12.33
- Title placeholder top 0.74, height 0.47
- Headline line top 1.20, height 0.34
- Left panel: left 0.50, top 1.72, width 5.00, height 4.30
- Right panel: left 8.33, top 1.72, width 4.50, height 4.30
- Corridor between panels: 5.50 to 8.33, centre 6.915
- Node rows: top row 2.08, middle row 3.02, bottom row 4.82. Node height 0.62
- Legend row at 6.10
- Full-width takeaway banner at 6.42, height 0.62

**Palette, hex**

| Role | Fill | Line |
|---|---|---|
| Equipment | EEF6FF | 4B83C4 |
| Work systems (NavWork, Navigator Intelligence, Maximo) | F4F7F2 | 6A8F4E |
| People | F2F2F2 | 777777 |
| Airwall and secure | FFF4E5 | C47F00 |
| entroCIM platform | F1F5FF | 5B6EE1 |
| WAM data | F7F1FB | 8A63A8 |
| CDA service | ECEFF4 | 6B7280 |
| Panel | FFFFFF | C8CDD4 |
| Band and banner | F5F7FA | D8DDE5 |
| Text | 1B2B3A | Muted text 5A6672 |

Line colours: solid 3D4B5C, dashed C47F00, dotted 8A63A8, human 6B7280.

---

## 7. What is actually open for exploration

The current diagrams work but are not the only answer. These are the live problems.

1. **Frame C is dense.** Fifteen connections in a two-panel layout, with several long diagonals crossing the corridor. It is the only page whose job is to show a loop closing, so some density is earned, but the routing could be better. Alternatives to straight point-to-point lines are welcome: orthogonal routing, a bus or corridor metaphor, grouped connections, layered reveal.
2. **The human hand-off marker.** A small pill reading "person" on the line. It works but is inelegant. Anything that makes a person-mediated step obviously different from a data connection, and makes its removal in frame C obvious, is worth trying.
3. **Four line treatments may be one too many.** They are all doing real work, but a design that carries the same four meanings with less visual machinery would be an improvement.
4. **The overview page.** Three simplified panels side by side showing the progression, with captions and a takeaway banner. Each panel must stand alone when the other two are covered. This page often does most of the work for an executive audience, and it is the least developed.
5. **The corridor note boxes** in frames A and B are dashed rectangles with centred text. Functional, plain.
6. **Reserved space.** Frames A and B currently have visible empty regions where frame C's additions will appear. Honest, but it reads as sparse. A treatment that makes reserved space feel intentional rather than empty would help.

---

## 8. Constraints that hold regardless of visual approach

- **No em dashes anywhere.** Commas, semicolons, parentheses or separate sentences.
- Minimal bold in slide text.
- One headline sentence per page, no more than four short labels, nothing past one line. Narrative goes in speaker notes.
- **No owners, dates for people, asks, or open-item lists on any slide.** Those are handled in a weekly call.
- Never state or draw a planned capability in the present tense.
- Nothing may imply a connection exists when it does not. This is the deck's central integrity requirement.
- Must render legibly when printed in greyscale, so status must not depend on colour alone.
- Corporate template, corporate fonts, restrained palette. This is an internal executive deck, not a marketing piece.

---

## 9. Output format needed back

The deck is built programmatically as native PowerPoint shapes on the Wesco corporate template, so exploration output has to be translatable into that.

For each option, please provide:

1. **A PPTX export**, if the tool supports it. That is the most useful form by far, because the exact geometry can be read straight out of the file and rebuilt. Keep the 13.333 by 7.5 inch canvas.
2. **A rendered image** of the frame or page, so the visual can be judged directly without opening anything.
3. **If PPTX export is not available**, a layout specification instead: node positions and sizes in inches on a 13.333 by 7.5 canvas, or as proportions, plus connection paths and label placements, and colour and line values as hex and point weights where they differ from section 6. Enough to rebuild it exactly.
4. **One paragraph** on what the option does better than the current version, and what it gives up.

Two or three genuinely different approaches are more useful than several variations on one. If an approach only works for frame C and breaks the three-frame constancy, say so; that trade may still be worth making, but it needs to be visible.

**On the reference material supplied with this brief.** The current deck is provided as the problem statement and the constraint set, not as the target. Do not iterate on its layout. Section 7 lists what is wrong with it; sections 2 to 5 list what must survive any redesign.

## 10. Validation criteria

An option succeeds if all of these hold.

- The three frames read as one picture changing, not as three separate diagrams.
- An executive can follow the story from the pictures alone, without reading a bullet.
- Every connection carries a deliberate status treatment, and the treatments are legible in greyscale.
- Frame B's new link visibly ends at people, and the work system still has no platform connection.
- The human hand-off is visibly present in A and B and visibly absent in C.
- In frame C, every path into Navigator goes through NavWork.
- Nothing is drawn in the present tense that does not exist today.
- No owners, dates, asks or open items appear on any page.
