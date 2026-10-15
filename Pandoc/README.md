# Pandoc pipeline: Markdown to Word

Drop a `.md` file into `inbox/`. `pandoc-watch.command`, running on Darryl's Mac, converts it to `.docx` in `output/` within seconds and moves the original to `processed/`. Design changes to Word output happen here, deliberately, never by hand in a generated file. Writing rules for Markdown headed into this pipeline are in `Reference/Communication_Preferences.md`, "Markdown for the Word pipeline."

## Files

| File | Role |
|---|---|
| `pandoc-watch.command` | The watcher. Runs Pandoc 3.1 with the reference template, mermaid-filter (when a file has Mermaid blocks), then `filters/eos.lua`, with native Word caption numbering. Adds a table of contents only when YAML front matter says `toc: true`. Resolves image paths from `Pandoc/` first, then the EOS root, and prints a console warning when an image path does not resolve (2026-10-15). **Restart it after any change to this file.** |
| `Pandoc_Ref.docx` | Reference template (v3, 2026-10-05). Pandoc takes styles, page setup and footer from it; its body text is ignored. |
| `filters/eos.lua` | Title promotion, figure centering and alt text, content-based table widths. Behavior described at the top of the file. |
| `miro_exports/` | Inbox for Miro frame exports (added 2026-10-15). Darryl exports here with Miro's default name; Claude renames, files beside the deliverable and empties it. Not read by the watcher. |
| `samples/` | Before and after renders from the 2026-10-05 redesign, and the 2026-10-15 image-path test (`2026-10-15_Watcher_Test_Resource_Path.docx`). Reference only. |
| `SUPERSEDED_2026-10-05_*` | Previous template versions and the previous watcher script. Never edit. |

## Template specification (v3)

- **Page:** US Letter, 0.75 in margins. One footer on every page: document title (left); "Wesco Confidential | Page X of Y" (right). The classification wording is a placeholder until Wesco's official label is confirmed.
- **Type:** Aptos throughout (Microsoft 365 default, identical on Mac and Windows). Body 10.5 pt, 1.1 line spacing, black on white.
- **Headings (bold, black):** Title 20 pt; Heading 1 14 pt with a thin gray rule beneath; Heading 2 12 pt; Heading 3 11 pt; Heading 4 10.5 pt italic. More space above a heading than below it.
- **Tables:** style `Table`, derived from Plain Table 3. Bold header with a dark rule, no all caps, banded rows only (never banded columns), 9.5 pt cells with padding, header row repeats, rows do not split across pages.
- **Pandoc styles defined:** Body Text, First Paragraph, Compact (list items and table cells), Block Text (blockquotes, gray note box), Title, Subtitle, Author, Date, Abstract, Figure, Captioned Figure, Image Caption, Table Caption, Caption, Source Code, Verbatim Char (Consolas, gray), Footnote Text, Definition Term, Definition, TOC Heading.
- **Named callouts** (applied with `::: {custom-style="..."}`): Bottom Line, Decision Required, Risk, Source Note.

## Why the template is built this way

Pandoc writes every paragraph with a fixed set of style names. Any name missing from the reference template falls back to Normal, which is how output came to be 9 pt Nirmala UI before 2026-10-05: five of the six most-used styles were undefined. Pandoc also switches on banded columns in every table it writes; the `Table` style has no column-band formatting, so that switch has nothing to apply. Font and size live in the document defaults rather than in Normal so the table style's smaller cell size is not overridden.

## Changing the template

Open `Pandoc_Ref.docx` in Word, change styles through the Styles pane (modify the style, never format text directly), and save. First save a copy as `SUPERSEDED_YYYY-MM-DD_Pandoc_Ref.docx`. Keep style names unchanged; Pandoc maps by name. Test by dropping a recent briefing into `inbox/`.

## Change history

| Date | Change |
|---|---|
| 2026-10-15 | Watcher resolves image paths from `Pandoc/` and the EOS root (`--resource-path`), so both `../Deliverables/...` and `Deliverables/...` embed; previously a root-relative path dropped the image silently into the log. Adds a console warning for unresolved images. Tested the same day: both path forms and a Mermaid diagram embedded, a deliberately broken path logged the warning. Previous script kept as `SUPERSEDED_2026-10-15_pandoc-watch.command`. Proposal: `Deliverables/EOS_Meta/2026-10-15_Pandoc_Watcher_Resource_Path_Proposal.md`. |
| 2026-10-05 | Watcher reads Markdown without dollar-sign math (`-f markdown-tex_math_dollars`), after "($M)" in two table cells of the CDA brief rendered as a formula. Live after the watcher restart the same day; verified with a test file. |
| 2026-10-05 | v3: named callouts, heading scale for title promotion, footer bound to Title, inherited SharePoint and template metadata removed. Watcher gains `eos.lua`, native caption numbering and opt-in table of contents. |
| 2026-10-05 | v2: Aptos 10.5 pt, 0.75 in margins, full Pandoc style coverage, new table style, footer fixed (was printing "DOCUMENT TITLE"), unused 244 KB image removed from every output. |
| 2026-10-05 | Interim: black headings; `Table` style added (Plain Table 3, banded rows only). |
| 2026-07-06 | Original template. |
