# CDA: Start Here

**Purpose:** the entry point for any new session (Claude or another LLM) continuing the Connected Device Assurance business case. Read this first, then `CDA.md` (newest entries at the top) for history and reasoning.
**Last updated:** 2026-10-02, after the sponsorship meeting (Bill Muczko accepted).
**Owner and decision-maker:** Darryl Benson, Senior Director, CSS Platforms, Wesco.

> **Status 2026-10-06: CDA was not approved as a standalone FY27 investment. It continues on the entroCIM roadmap, built by the entroCIM team, with its own FY27 numbers at zero. Market positioning is unchanged (CDA stands alone to customers).** Read the top section of `CDA.md` and `03` 2026-10-06 before doing any CDA work; the funding ask in the files below is now historical.

## Current files (all in `Deliverables/CDA/`)

| File | What it is |
|---|---|
| `2026-10-06_CDA_Sean_Exec_Brief.md` / `.docx` | Executive brief for Sean's 2026-10-06 walkthrough (Darryl's framing, 2026-10-05): status after the business case review (agreed to continue; Bob's and Peter's input), Bill Muczko's support, the FY27 funding question (fund CDA as a project, or fold the capability into the entroCIM roadmap), and slides 8 and 10 embedded as exhibits (images in `2026-10-06_CDA_Sean_Exec_Brief_slides/`). Supersedes the 2026-10-05 risk-led draft, kept as `SUPERSEDED_2026-10-05_CDA_Sean_Briefing`. |
| `2026-10-02_CDA_Pro_Forma_v4.6.xlsx` | The model. Current version. Its **Deck Figures** tab is the single list of every number the deck uses, each with a formula, display format, source cell and slide. |
| `2026-10-02_CDA_Product_and_Business_Case.pptx` | The 21-slide sales-and-executive deck, Wesco template, built entirely by the script below. |
| `build_scripts/build_cda_business_case_deck.py` + `build_scripts/template.pptx` | The deck generator (python-pptx) and the Wesco template it builds on. |
| `2026-10-02_CDA_Deck_Contact_Sheet.jpg` | All 21 slides on one image. |
| `2026-10-02_CDA_Sponsorship_Meeting_Summary.md` / `.docx` | Summary of the 2026-10-02 sponsorship meeting; transcript in `Products/CDA/05_Operating_Record/`. |
| `2026-10-02_CDA_Sponsor_Meeting_Readthrough.md` / `.docx` | Darryl's prep for the sponsorship meeting (Bill Muczko, Bob Caprise, Jay Maes, Peter Ferrell; Sridhar Loke also invited, saw the deck 2026-10-01). |
| `2026-10-01_CDA_Sponsorship_Invitation.md` | Final invite and private note to Bill, as Darryl wrote them. |
| `2026-10-02_CDA_Design_Prompt_Sites_in_the_Plan.md`, `2026-09-30_CDA_Design_Prompts.md` | Claude Design prompts used for slide concepts. |
| `SUPERSEDED_*` | Earlier versions, kept for the record. Do not use. |

## Where things stand

- **Plan (v4.6):** 871 sites and about 100,500 devices by 2031; $11.3M 2031 run rate; peak investment $3.1M in 2029; cash positive in 2031, ending at $2.1M; 2027 development $246,787, tied to the FY27 AOP submission.
- **Anchors:** Kroger (Large, 429 sites, engaged); Cisco Connected Real Estate (Medium, 187 sites, in the plan but still scoping; Bob is finding the Cisco-side owner); three placeholders by lane (pharma, automotive, third lane).
- **Fees:** $6,900 / $10,300 / $15,700 a year (Small / Medium / Large), held; about 40 percent margin; Wesco payback per site 12.4 / 14.3 / 15.5 months.
- **Deck order:** 1 Title, 2 After the initial sale, 3 The service, 4 Why Wesco, 5 Three platforms stronger, 6 How it sells, 7 What a seller earns, 8 One site, 9 Anchor accounts, 10 Sites in the plan (Gantt with yearly totals), 11 Plan 2027 to 2031, 12 Staffing, 13 Market, 14 Evidence and estimates, 15 What is needed, 16 Appendix divider, 17 Fee build, 18 Capital and cash, 19 Device coverage, 20 Slides by audience (internal; remove before the deck leaves Wesco), 21 End.
- **Sharing rule (Darryl, 2026-10-02):** the workbook does not go to Bob Caprise or anyone outside the team until Sean McCloskey has vetted the numbers. Figures may be shown in slide form, as an early pro forma, to foster a business decision (Darryl, 2026-10-02); the workbook itself stays internal.
- **Sponsor:** Bill Muczko accepted, 2026-10-02. Meeting summary: `Deliverables/CDA/2026-10-02_CDA_Sponsorship_Meeting_Summary.md`.
- **Next:** Sean walkthrough of the numbers, Tuesday 2026-10-06 (Sean informed by Teams 2026-10-02); send attendees the deck PDF (without slides 17 and 20); define the product scope so the sales enthusiasm lands on a defined offer; enterprise pricing construct (`03` Backlog 2026-10-02).

## How to rebuild the deck

1. Copy the workbook, `build_scripts/build_cda_business_case_deck.py` and `build_scripts/template.pptx` into one working folder.
2. Edit the `WB=` line near the top of the script to point at the workbook's path in that folder. (In the original session it pointed at `/mnt/user-data/outputs/...`, which will not exist elsewhere.)
3. If the workbook was edited, recalculate it first (LibreOffice headless recalc) so Deck Figures holds values; the script reads recalculated values only.
4. Run `python3 build_cda_business_case_deck.py` from that folder. It writes the deck there and stops with an assertion error if any check fails (for example `aop_tie_check`, `equation_check`, `installed_check`, `bar_check`). A failed assertion means the text and the numbers no longer agree; fix the cause, do not delete the assertion.
5. Validate the .pptx, render it, and look at every changed slide before delivering. Diff the slide text against the previous deck to confirm only intended changes.
6. Save the new deck and script back to `Deliverables/CDA/` and log the change at the top of `CDA.md`.

## Working rules (settled; do not reopen without Darryl)

- **The script is the source of truth for wording.** If Darryl edits the deck by hand, diff his file against the build and fold the edits into the script, or the next rebuild drops them.
- **No figure is typed into the script.** Every number comes from a Deck Figures key. Model inputs are linked; outside figures (AOP figure, Kroger's $15 per camera, Bob's three-to-five anchors) are reference rows that name their source. Bill's "about 85 percent of the Fortune 200" stays as quoted text.
- **Workbook edits:** never insert or delete rows or columns; append below the last used row. Blue text or yellow fill = input; black = formula; green = link. Bump the version for model changes, mark the old file `SUPERSEDED_`, and add a README log line.
- **Colors:** Mechanical Blue (004986) and its tints for data; Steel Grey tints with a dashed Granite Grey outline for placeholders; Wesco Green only for what Wesco gains, never for a loss or an ask.
- **Language:** US English; no em dashes; slide titles are short noun phrases; no subtitles; tell the reader only what they need; say "entroCIM licensing" or "entroCIM components," never "PODs," in anything that leaves the team; "entroCIM" with a lowercase e.
- **Evidence:** keep confirmed facts, Bob's and Bill's working figures, and placeholders visibly distinct. Every data slide carries an "Illustrative" marker; every slide has speaker notes.
- **Walmart is a potential, not a plan input (Darryl, 2026-10-02).** It may be mentioned as a potential account; do not add it to the pro forma, the anchor accounts or any planning document.
- Darryl decides. Discuss before changing anything substantive; he often asks for review before edits.

## Open items

- **Enterprise pricing (raised 2026-10-02 by Peter Ferrell, Bill Muczko, Sridhar Loke):** per-site packages as the land offer; enterprise agreement and small-branch delivery (fewer than ten devices, no appliance per site) still to design. Willingness to pay not yet tested with a customer.
- **Seller value proposition:** CDA versus VMS/Genetec comparison and vertical outcome plays, one page, before sellers use it.

- **Body font:** the brand guide calls for Source Sans; the deck uses Arial. Check the template's theme font and do a scratch render before switching, since every text box is sized for Arial.
- **Contrast:** white text on the lightest Mechanical Blue tint (slide 10, go-live segments) is 3.8:1. Labels are 12 pt bold; darken the tint if it reads poorly on a projector.
- **Cisco:** owner on the Cisco side not yet identified (Bob). Its 187 sites and 80 devices per site are Bob's working figures.
- **Pricing inputs Darryl owns:** Nozomi, NinjaOne and JCI (Airwall) pricing still to refine.
- **Sean review of the numbers:** Tuesday 2026-10-06; required before the workbook is shared (holds `05` A51).
- **Kroger per-camera fee:** one-time or annual, and on Kroger only or all Axis sales; questions for Bob and Bill.
- **Staffing:** TSS to review the service-delivery heads and hours (18 TSS heads by 2031 in v4.5/v4.6).
- **Workbook README:** the log is newest-first, but the v4.4, v4.5 and v4.6 entries sit at the bottom (rows are never inserted). Move them up by hand.
