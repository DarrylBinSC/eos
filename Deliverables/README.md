# Deliverables — Index

On-demand drafts, decks, analyses, and memos built in Cowork sessions with the EOS folder selected. Distinct from `Products/` (durable knowledge) and the living documents (03–10, tracking). This is the output, not the record.

**Reorganized 2026-08-06** into subfolders by initiative, per Darryl's decision to keep this modular — easy to focus, review, edit, and get replies that stay scoped rather than wandering across initiatives unless asked. Previously a flat folder of 24 files with no index.

## Subfolders

| Folder | Contents |
|---|---|
| `JCI/` | Johnson Controls MSP contract: issues/actions summary, Brian Miller refresh email, Airwall/MSP agreement review, one-page brief |
| `Exec_Briefs/` | Sean McCloskey pre-reads and meeting briefs, the Woolly AI update, and the Lisa Orton entroCIM/WAM brief — cross-portfolio executive communication that isn't specific to one product |
| `WAM/` | Asset-tracking data flow, WAM operational-hardening executive summary, FY27 AOP change log, and the 2026-08-13 AI part-taxonomy requirements package (lessons learned, requirements framework, drafting prompt). **Added 2026-10-23:** native PowerPoint rebuild of the 10-19 DDP Internal Data Collection markup for Alan Martin (ADM consume path), with build script |
| `entroCIM/` | Update slide content, AOP "risk of not doing" analysis, FY27 $1.44M reconciliation, and the 2026-08-10 commercialization v10.1-to-v11 comparison plus its v11 review-items action list **Added 2026-08-25:** the Woolly development and test API cost estimate (memo plus workbook), which prices the harness making LLM calls during dev and test. The first version of that estimate priced the wrong workload (developer coding assistance) and is retained as `SUPERSEDED_*` with a banner explaining what was wrong; read the banner before quoting anything from it. Method and rates in `Reference/AI_Development_Tooling_Cost_Model.md` v2.0. Also holds the 2026-08-19 FRB RFP section drafts and reviews. **Added 2026-10-07:** data center value proposition plan for Sean (A58). **Added 2026-10-12:** review of the Europe team's deployment strategy document (On-Premise or Wesco-Hosted, v0.1): the original as received, Darryl's tracked-changes markup, and the reply note with the open items raised. |
| `Vibe_Code_Productization/` | New 2026-10-07. Meeting briefs and working drafts for the vibe coding productization concept (A60), starting with the 2026-10-08 Mike Wassil brief. |
| `CSS_Platforms_2027_Ideation/` | Early (2026-07-23) ideation-phase drafts: ChatGPT addendum/joint workplan, first-pass ideation, new-product charter. **Flag:** these look like early precursors to the more developed `Products/CDA/00_Charter/` and `01_Phase_1_Divergence/` material. Left as-is, not merged — confirm with Darryl whether these are superseded drafts or a distinct thread before treating either copy as canonical |
| `Portfolio_Admin/` | Chad Steger handoff digest, a commitment-update spreadsheet, the CSS Platform Team 2027 headcount review deck, and the 2026-08-10 portfolio status slide cells for entroCIM and WAM (July cycle) — general portfolio/ops items that don't belong to one product |
| `Stakeholder_Map/` | **Added 2026-10-07. Source of truth: the private Miro board "Stakeholder Map 2026-10" in Darryl's personal Miro account.** Folder holds its data source (core stakeholder influence/alignment draft, 24 people, corrected by Darryl), the Mermaid structural draft (.mmd, and the .md that embeds it; not maintained in parallel with the board, per `Reference/Diagram_Register.md`), the Miro build prompt, and `build_scripts/` (Miro board generator; python-pptx builder for the retired deck). The influence grid deck and decision-rights PNG were superseded 2026-10-07 (`SUPERSEDED_2026-10-07_*`) and are not maintained. Private; not for distribution |
| `EOS_Meta/` | Material about the EOS itself rather than about Darryl's job: the Pandoc watcher resource-path proposal and its script (2026-10-15, adopted the same day), the Dashboard design spec, the use case review and open-decisions list (08-19), the register summary (08-25), the EOS concept prompt written for Ron (08-25), and **added 2026-09-02** the Architecture Canvas (`2026-09-02_EOS_Architecture_Canvas.html`), a self-contained HTML page holding the component and boundary view, the operating loop, and four use-case traces. Framing agreed with Darryl that day: for his own use, as used rather than as designed, tool-agnostic, clean structural view. The anchor diagram is hand-positioned SVG; the other views are Mermaid |

## Adding New Deliverables

Save into the matching initiative subfolder. If nothing fits, ask before creating a new one — the point of subfolders is to stay modular, not to fragment into a folder per file.


## 2026-08-19 — AOP material moved out

The four FY27 AOP change logs (CDA, Navigator, WAM, entroCIM) and two entroCIM supporting documents (the $1.44M reconciliation and the risk-of-not-doing note) moved to `AOP_FY27/`. They were spread across four initiative subfolders here, which made the AOP cycle impossible to see as one thing. `Deliverables/CDA/` and `Deliverables/Navigator/` are now empty; they stay for future non-AOP work on those initiatives. See `AOP_FY27/README.md` for the full index and for which workbook is live per product.

- `CLM/` — Contract Lifecycle Management (added 2026-09-28). **2026-10-01: CLM not adopted in the FY27 AOP; both documents carry a status note and are kept as reference.** `2026-09-28_CLM_Capacity_and_Skills_Assessment` (.md, .docx): capacity, skills gap, team scenarios and costed options as input to Sean's AOP decision. `2026-10-01_CLM_Product_Brief` (.md, .docx): Darryl's get-up-to-speed brief. Explains the product, decodes Chris Gazdic's 09-25 Copilot notes line by line, gives an independent read of Nanda's scope (gaps: volumes, baseline, contracts in force, content ownership, Word editing approach, external access, SOX), build-versus-license market context, an investigation plan, and a glossary. Does not repeat the assessment's team and cost terms.

- `Exec_Briefs/2026-10-22_CSS_Platforms_Portfolio_v3.pptx`: CSS Platforms portfolio slide, one card per live product (what it is, who it serves, 2027, sponsor, stage chip). Build script in `Exec_Briefs/build_scripts/`. Added 2026-10-22.

- `entroCIM/2026-10-26_O-Insights_Comparison.xlsx`: O-Insights Core, SkySpark and entroCIM comparison, draft for team validation (vendor sheet kept unchanged, our columns added, demo observations, vendor questions), with the vendor's source workbook (`..._SOURCE.xlsx`) beside it. The same-day .md/.docx narrative is `SUPERSEDED_` (Darryl: keep it in Excel; scope is competitive understanding and educating Supplier Relations). Added 2026-10-26.
