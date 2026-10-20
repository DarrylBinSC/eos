# FY27 AOP — Working Home and Index

**Created 2026-08-19** at Darryl's direction (`Deliverables/EOS_Meta/2026-08-19_EOS_Use_Case_Review.md`, recommendation 4). AOP and business-case work is currently the dominant workload in this system and had no home of its own: four change logs sat in four different `Deliverables/` subfolders, and eight collation workbooks sat under `Products/` behind COPY, BACKUP, and SUPERSEDED prefixes with no rule saying which was live.

**Submission date: 2026-08-21.** Two days out at the time this folder was created, which is why the reorganisation was deliberately partial. See "What was not moved, and why" below.

---

## 1. Which workbook is live

This is the question this index exists to answer. Verified by modification time on 2026-08-19.

| Product | Live workbook | Last modified | Location |
|---|---|---|---|
| entroCIM | `COPY_entrocim_build_it-demand-collation-template.xlsx` | 2026-08-19 19:46 | `Products/entroCIM/` |
| WAM | `COPY_wam_build_it-demand-collation-template.xlsx` | 2026-08-19 19:56 | `Products/WAM/` |
| CDA | `COPY_connected-device-assurance_build_it-demand-collation-template.xlsx` | 2026-08-19 20:24 | `Products/CDA/04_Phase_4_AOP/` |
| Navigator | `COPY_ascent-navigator_build_it-demand-collation-template.xlsx` | 2026-08-18 10:21 | `Products/Navigator/` |

**The live file is the one without a prefix qualifier.** In every case it is also the smaller file, around 370 KB, where the backups run around 440 KB. If you ever open one and are unsure, that size signature is the tell.

**Not live, retained deliberately:**

| File | Status |
|---|---|
| `..._BACKUP_2026-08-17.xlsx` (WAM), `..._BACKUP_2026-08-18.xlsx` (entroCIM, CDA, Navigator) | Point-in-time backups. Do not edit |
| `SUPERSEDED_2026-08-17_entrocim_op-2027_...xlsx` and `..._ORIGINAL.xlsx` | Superseded entroCIM templates, retained for the trail |

**One item needs your decision.** `Products/CDA/04_Phase_4_AOP/Copy of COPY_connected-device-assurance_build_it-demand-collation-template.xlsx`, modified 2026-08-19 16:03, 444 KB. It is not the live file (the live CDA workbook was modified four hours later) and it is not named as a backup. Its size matches the backup signature, so it is most likely an accidental Finder duplicate made while you were working. It was left in place rather than moved or renamed, because guessing wrong on an AOP workbook two days before submission is not a risk worth taking. Confirm and it gets cleared after the 21st.

## 2. Contents of this folder

**`Change_Logs/`** — one per product, consolidated here from four separate `Deliverables/` subfolders.

- `2026-08-17_entroCIM_FY27_AOP_Change_Log.md`
- `2026-08-17_WAM_FY27_AOP_Change_Log.md`
- `2026-08-18_CDA_FY27_AOP_Change_Log.md`
- `2026-08-18_Navigator_FY27_AOP_Change_Log.md`

**`Supporting/`**

- `2026-08-05_entroCIM_FY27_1.44M_Reconciliation.md`
- `2026-07-24_entroCIM_AOP_Risk_of_Not_Doing.md`

## 3. Where the rest of the AOP material lives

Left in place on purpose; this section is the map.

| Material | Location | Why it stays there |
|---|---|---|
| The four live collation workbooks and their backups | `Products/<product>/` | Actively open two days before submission. Moving a file out from under an open workbook is how you lose an afternoon |
| CDA business case, appendix, intake drafts | `Products/CDA/04_Phase_4_AOP/` | The CDA phase structure is the initiative's own record and predates this folder |
| CDA risk-of-not-doing | `Products/CDA/03_Phase_3_Funding/CDA_AOP_Risk_of_Not_Doing_2026-07-28.md` | Belongs to the CDA funding phase narrative |
| entroCIM AOP findings import package | `Products/entroCIM/entroCIM_FY27_AOP_Findings_Import_Package_2026-08-04.md` | Product-level source material |
| CSS Platform team P&L analysis | `Products/entroCIM/CSS_Platform_Team_ P&L_Analysis_COPY_08AUG.xlsx` | Misfiled under entroCIM; it is portfolio-level. Move it here after the 21st |
| 2027 headcount review deck | `Deliverables/Portfolio_Admin/2026-08-07_CSS_Platform_Team_2027_Headcount_Review.pptx` | Portfolio administration, feeds AOP but is not an AOP artifact |

## 4. Naming convention, applying from now

1. **The live file carries no qualifier.** `<product>_<artifact>.xlsx`. If it has a prefix, it is not the working copy.
2. **Backups carry the date they were taken**, at the end: `..._BACKUP_YYYY-MM-DD.xlsx`. Never edit a file with BACKUP in the name.
3. **Superseded files carry `SUPERSEDED_YYYY-MM-DD_` at the front**, so they sort away from the live file and read as dead at a glance.
4. **No "Copy of".** If the operating system generates one, either rename it to a dated backup or clear it the same day. An unqualified duplicate is the one failure mode this convention exists to prevent.
5. **Documents are dated at the front**, `YYYY-MM-DD_`, as everywhere else in this system.

## 5. What was not moved, and why

The collation workbooks. They are the live artifacts of a submission due in two days, at least three of them were modified within hours of this folder being created, and the value of tidier paths does not come close to the cost of breaking a file reference during the AOP window. The index above closes the actual gap, which was not knowing which file is live.

**After the 21st:** move the four live workbooks and their backups into `AOP_FY27/Workbooks/`, move the CSS Platform team P&L analysis out of `Products/entroCIM/`, and clear the stray CDA duplicate once you have confirmed it.

## 6. Rule going forward

FY28 and any subsequent cycle gets its own `AOP_FY<nn>/` folder created at the start of the cycle, not partway through. Product-specific source material stays in `Products/`; anything cross-product, any change log, and any submission artifact belongs here from the first day.

## Status note, 2026-10-20 (Sean McCloskey, Agile Staff Meeting transcript)

"We're in the tail side of AOP, which means I think we understand the budgets that we're getting." Later the same day Sean expected to have "shown how we've maintained both headcount and cost from last year." Reported, not confirmed by Darryl; no product-level figures in the words. Source: `Evidence/M365_Evidence_Daily_2026-10-20_AgileStaff.md` (transcript, 732 of 732 lines).
