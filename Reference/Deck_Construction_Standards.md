# Deck Construction Standards
As of: 2026-08-28

Build-mechanics standards for PowerPoint decks produced in this workspace, particularly architecture and flow diagrams built programmatically with python-pptx. This file covers **how a deck is constructed**, not what it says. Voice and content rules live in `Communication_Preferences.md`; Mermaid-specific guidance lives in `Mermaid_Standards.md`.

Established 2026-08-28 by Darryl during the Navigator / entroCIM integration deck build.

---

## 0. Default template: Wesco, unless Darryl specifies otherwise

**Standing rule, Darryl, 2026-10-05.** Every deck or slide built in this workspace goes on the Wesco slide template unless Darryl names a different one, including when the source material arrives on another template (e.g. a teammate's working deck). Copy: `Reference/Templates/Wesco_Slide_Template.pptx` (copied from `Deliverables/CDA/build_scripts/template.pptx`). Working layout `Blank-with-Title`; title placeholder at 0.73, 0.74 in; content between x 0.73 and 12.59 in and above y 6.5 in (section 7). Brand palette and Arial as used in the CDA build script. Origin: the 2026-10-05 ADM AOP slides were first rebuilt on the source deck's plain layout and had to be redone.

## 1. Connectors: one shape per connection

**Standing preference, Darryl, 2026-08-28.** Every logical connection on a diagram is **one continuous PowerPoint shape**, never a chain of separate line segments.

- **Straight connection:** a single straight connector.
- **Any connection with a bend:** a single **freeform shape** with a multi-vertex path (`shapes.build_freeform(...)` then `add_line_segments(...)` and `convert_to_shape()`).

**Why this matters, and it is not cosmetic.** A routed path drawn as three or four separate connectors is three or four objects. One click selects a fragment rather than the connection. Moving a node leaves orphaned pieces behind. Dash pattern and arrowhead have to be applied to each fragment and drift apart. And endpoint errors hide inside the chain, because a segment that stops short still looks joined to the segment beside it. As one shape, the connection moves, restyles and is checked as a unit.

**Do not fall back to segments when PowerPoint's elbow connector cannot make the route.** A bent connector produces a Z shape only. Any route that leaves a node, dodges around an obstruction and reverses direction, a U rather than a Z, or that needs three or more bends, is beyond it. That is the case for a freeform, not for a chain of connectors.

**Label tokens sit on top of the line, they do not break it.** Where a marker or pill is placed mid-path, give it a solid white fill and let it mask the line beneath. The path stays continuous underneath. Visually identical to a break; structurally one object carrying a label, which is what the picture actually means.

## 1a. Text: one block per group, not one box per line

**Standing preference, Darryl, 2026-09-11.** A group of bullets that belongs together is **one text frame with one paragraph per bullet**, never a separate text box per line.

The failure it prevents is the same one section 1 describes for connectors, in a different medium. Three bullets built as three boxes are three objects. Each can be dragged independently, so they drift out of alignment the first time someone edits the slide. Spacing between them is a position rather than a property, so it does not survive a text edit: shorten the first bullet and the gap grows, lengthen it and the next bullet is overwritten. Restyling means selecting three things and hoping they match. And the group cannot be moved as a unit, which is the operation an editor actually wants.

As one frame, the group reflows when the text changes, the spacing is paragraph spacing and holds, one click selects the whole block, and one style change applies to all of it.

**How to build it.** One text frame, `word_wrap` on, zero margins. One paragraph per bullet. The bullet character is a paragraph property, not typed text: set `marL` and a negative `indent` on `a:pPr`, then append `a:buClr`, `a:buSzPct`, `a:buFont` and `a:buChar` in that order, because the schema enforces it. Space between bullets is `a:spcBef` on each paragraph after the first, not a blank line and not a y offset.

**Sub-lines belong in the same frame.** Where a bullet carries a smaller caption beneath it, an owner name or a status, that caption is another paragraph in the same frame with `a:buNone` and an indent that aligns it under the bullet text. Splitting it into its own box reintroduces the drift the pattern exists to prevent.

**Where a table is better.** Any content that is genuinely a grid, rows of label and value, a matrix, a roadmap, is a native table rather than a text block, per section 8. A borderless table with the first column styled bold reads identically to a hand-laid list and is far easier for a recipient to edit. If a text block is starting to need column alignment, it wanted a table.

**What stays as its own box.** Titles, headlines, section captions, labels sitting on a connector, and anything positioned against a diagram node rather than against other text. Those are anchored to geometry, not to each other.

## 2. Verify endpoints before shipping

Every connector endpoint must land on a node's rectangle. Check it programmatically rather than by eye: for each path, test whether the first and last vertex lie on the edge of some node rectangle within tolerance.

- An arrowhead standoff of roughly **0.07 in** is expected and correct; the line stops just short so the arrow tip meets the box.
- Anything further out is a **floating line**: it reads as a connection but attaches to nothing.

This is cheap and catches a class of error that is genuinely hard to see in a diagram carrying a dozen or more connections. It found a real defect on the Navigator deck, a WAM to entroCIM line specified 0.77 in clear of both boxes, which had survived a design pass, a render and a review.

## 3. Native shapes over auto-layout, for diagram sequences

Where the same diagram is shown at several points in time and node positions must stay constant across pages, build with absolutely positioned native shapes. Auto-layout tools re-rank the graph when connections are added, so a later frame will not line up with an earlier one. Mermaid remains the right tool for **drafting** relationships quickly, before layout matters. **Updated 2026-10-07:** when the Miro connector is available, sketch uncertain layouts in Miro instead (two or three options side by side), then rebuild the chosen option natively here; thresholds and the placeholder rule are in `Communication_Preferences.md` §7. **Updated 2026-10-15:** rebuild from the connector's read-back of the chosen option (positions, sizes, text and connector endpoints for hand-built sketches; nodes, edges and labels for synced Mermaid flowcharts), not from a screenshot or memory; procedure in the same §7.

## 4. Render every page and look at it before shipping

**The highest-value practice in this file.** A programmatically built deck must be rendered and viewed, page by page, before it goes anywhere. Convert to PDF with LibreOffice, rasterise with pdftoppm, and look at every page:

```
soffice --headless --convert-to pdf deck.pptx --outdir render
cd render && pdftoppm -png -r 110 deck.pdf page
```

Defects that only appear on render, all of them found this way during the Navigator build: labels landing on top of connectors, a title placeholder overlapping the headline beneath it, legend items overrunning each other, node text overflowing its box, phase bands sitting out of alignment with the columns they described, and content colliding with the master's logo. None of these raise an error and none are visible in the code.

## 5. Start from a real on-brand deck, not from a blank presentation

Open an existing deck that is already on the corporate template, delete its slides, and keep the master. That inherits the theme, fonts, colours, layouts, logo, footer and confidentiality stamp without reconstructing any of it.

Before choosing the base, confirm the layouts are what you expect, and confirm two candidate decks actually share a master rather than assuming it. Read the layout names and the placeholder geometry programmatically; do not guess. The Wesco template's working layout for built content is `Blank-with-Title`.

**Check the template's own layouts before hand-building a page.** The Wesco template ships `Roadmap with Stages`, `Roadmap with Icons` and `Timeline with Numbers`. All three are stage-based with a fixed number of steps and no lane structure, so none of them can carry workstreams by quarter, which is why the Navigator roadmap was built as a styled table instead. That is a two-minute check that either saves the work or justifies it.

## 6. Type metrics do not transfer between tools

Geometry imported from a design tool will be authored in that tool's font. Corporate fonts are usually wider. Expect text that fitted in the source to overflow its box or collide with a connector, and expect to re-place labels and drop type by around half a point after import.

Node and connector geometry transfers exactly. Text placement does not. Treat an imported spec as authoritative on structure and provisional on anything text-sized.

## 7. Keep clear of the master's furniture

The corporate master owns the bottom of the slide. On the Wesco 13.333 by 7.5 in template the logo sits bottom left at roughly y 6.55 to 7.10, the confidentiality stamp runs centred near y 7.15, and the footer and slide number sit at y 7.14 to 7.26.

**Content must end above about 6.5 in.** A legend or takeaway line placed lower will collide with the logo, which is not visible in the code and only appears on render. Read the master's placeholder positions rather than assuming them.

## 8. Build for whoever has to edit it

When a page will be completed or maintained by someone else, editability is a requirement of the deliverable, not a nicety.

- **Grids, roadmaps and matrices: use a native table.** The recipient edits by typing into cells. Style it so it reads as a timeline or a matrix rather than as a table.
- **Diagrams: use native shapes**, positioned absolutely, one shape per connection per section 1.
- **Never SmartArt, and never a rendered image** where the content is expected to change. Both are close to unmaintainable in someone else's hands.
- A page handed to a named person should be mostly empty where their content goes, with the structure and any fixed anchors supplied, so they fill a frame rather than argue with a draft.

## 9. Working with Claude Design, or any external design tool

The pattern that worked on 2026-08-28, and is worth repeating.

**Send a self-contained brief, not a conversation summary.** The tool has no access to the originating session. It needs the exact node inventory, every connection with its label and status, the naming discipline, the current geometry in inches, the palette in hex, the constraints that hold regardless of visual approach, and validation criteria. Template: `Deliverables/Navigator/2026-08-28_Navigator_entroCIM_Diagram_Design_Brief.md`.

**Scope the exploration explicitly.** State what is settled and what is open. Content, relationships and status meanings were closed; layout, routing and treatment were open. Without that boundary a design tool will redesign the argument.

**Send the current deck as both PDF and PPTX, and say it is the problem statement rather than the target.** The PDF is what it judges; the PPTX lets it read the corporate template and export back onto it. Showing the current design anchors the tool on it, so say plainly not to iterate on that layout.

**Ask for a PPTX export back.** Claude Design can export PPTX, which means exact geometry can be read out of the file rather than eyeballed from an image. Ask for a rendered image alongside it, plus one paragraph on what the option does better and what it gives up. Two or three genuinely different approaches beat several variations on one.

**No model selector.** Anthropic's Claude Design documentation exposes no model choice; output quality is driven by the context supplied. Reached through Claude Code's `/design` skill instead, the model is whatever that session is set to.

**Audit what comes back before building it.** A spec can be internally wrong. The Corridor spec placed one connection 0.77 in clear of both nodes it was meant to join, and the design tool's own render showed the same floating line. Run the section 2 endpoint check against an imported spec, not just against your own work.

---

## Deliberately not in this file

**Content and voice rules** live in `Communication_Preferences.md`: headline plus a few labels on the page, narrative in speaker notes, no owners or asks on slides, no em dashes.

**Deck-specific design decisions** are recorded where they are used rather than promoted here, because they have been proven once and not yet beyond that: line treatment as a status claim rather than decoration, status expressed as of today and held constant across a sequence of frames, frame-to-frame node position constancy, labelling only where a connection's meaning is not obvious from the two nodes it joins, and greyscale survivability. They sit in: `Deliverables/Navigator/2026-08-27_Navigator_entroCIM_Integration_Deck_Build_Prompt.md` and `Deliverables/Navigator/2026-08-28_Navigator_entroCIM_Diagram_Design_Brief.md`. Promote any of it here if it proves to apply beyond that deck.
