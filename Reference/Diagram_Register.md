# Diagram Register

As of: 2026-10-15

Every Miro board used for EOS work, and what it is the source of truth for. Miro cannot be searched from this folder, read by other LLMs, or seen by a session without the Miro connector; this file is how they find it. Rules are in `Communication_Preferences.md` §7 ("Integrating Miro and Mermaid"). Mermaid diagrams are not listed here; their source is the file they live in.

## How to maintain

- Add a row when a board is created for EOS work. Update "Last export" whenever a frame is exported for a document.
- When a board is superseded, change Status and name what replaced it. Never delete a row.
- Exports are saved beside the deliverable as `<deliverable>_diagrams/<name>_YYYY-MM-DD.png` (PNG, white background, 2x).
- All boards are in Darryl's personal Miro account and private unless a row says otherwise.

## Boards

| Board | Purpose and source of truth | Generator and source data | Last export | Sensitivity | Status |
|---|---|---|---|---|---|
| [Stakeholder Map 2026-10](https://miro.com/app/board/uXjVEdM5q1g=/) | Decision-rights map and influence/alignment grid. Source of truth for both | `Deliverables/Stakeholder_Map/build_scripts/build_miro_stakeholder_board.py`; data `Deliverables/Stakeholder_Map/2026-10-07_Core_Stakeholders_Alignment_Draft.md` | None current (PNG superseded 2026-10-07) | Holds real alignment ratings in the personal account. Kept as is by exception, Darryl 2026-10-15; revisit if the board is ever shared or moved | Live. The `.mmd` in the same folder is a structural draft, not maintained |
| [Launch Studio Swimlane 2026-10](https://miro.com/app/board/uXjVEcvwZlg=/) | Layout options for how the vibe coder is embedded in Launch Studio. Sketch only | Session 2026-10-08; see `Products/Vibe_Code_Productization/Vibe_Code_Productization.md` | None | Private working sketch | Sketch |
| [Launch Studio Sean Deck 2026-10](https://miro.com/app/board/uXjVEaDAh84=/) | Layout options for the two executive slides (1A and 2A chosen). Sketch only; the deck is the deliverable | Rebuilt natively in `Deliverables/Vibe_Code_Productization/2026-10-13_Launch_Studio_Executive_Overview_Deck.pptx` | None | Private, no financials | Closed; deck built. **Stale against the deck:** the board keeps the 2026-10-13 wording ("Inlet filter"); the 2026-10-14 deck changed it. Option 1A tightly framed by Darryl 2026-10-15 ("Frame 2") for the export and read-back tests. Do not rebuild from it without checking the deck |
| [CSS Digital Products – Technical Architecture](https://miro.com/app/board/uXjVEa7Cw4Y=/) | Portfolio-level technical architecture, sourced from the older entroCIM Stack, Software Stack, Service Architectures, WAM connections and VAS-ADM boards. Dashed links and TBD labels need validation | No EOS record of how or when it was built | None | Private | **Retired 2026-10-15** (Darryl: old draft, to be removed). Not a source of truth. Board deletion is done by Darryl in Miro; the connector has no delete |
| [Mermaid Sync Test 2026-10-15](https://miro.com/app/board/uXjVEZ6XD1Q=/) | Test of a Mermaid diagram widget synced with EOS code. Source of truth: the Mermaid code, synced between the board and `Deliverables/EOS_Meta/2026-10-15_Mermaid_Sync_Test.md` | Widget "EOS diagram pipeline", built from code by Claude | Not needed; Word renders the code | None | Test complete 2026-10-15, round trip passed. Kept as the reference example |

## Not registered

The personal account holds 27 other boards (entroCIM, WAM, org chart and Azure sketches, several untitled) that predate this register. They are not EOS sources of truth. Add any that become live.
