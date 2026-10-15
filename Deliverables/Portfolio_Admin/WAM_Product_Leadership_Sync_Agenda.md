# Wesco Asset Manager Product Leadership Sync — Rolling Agenda Register

**Maintained by:** Darryl Benson. Updated in place every week. Do not create a new file per session.
**Chaired by:** David Blondel
**Attending:** David Blondel, Akansh Gangil, Darryl Benson
**Format:** `Reference/Meeting_Agenda_Standard.md` v2.0
**Transcription:** On. Recording off. Open floor may run untranscribed by agreement.

**Next session:** assumed Monday 2026-09-08, based on the 2026-08-24 instance in the 09-01 weekly briefing. Confirm the actual slot.
**Last updated:** 2026-09-02 (W12, W13, W14 added)

---

## Part 1 — Decisions required this session

Maximum three. Each is a question with a recommendation and a named decider.

**D1. The truncated manufacturer part number defect has no named fix owner. Does Darryl escalate now, or does Akansh's route get one more cycle?**

DDP/EUDM selects truncated part numbers while WAM/ADM holds full ones, so exact matching fails and orders are missed. Live since at least 08-12, when the same 15-character vendor part-number limitation was reconfirmed and escalated. Akansh committed on 08-25 to send a documented escalation to the DDP/UDM team copying Darryl. No owner named as of the 08-31 evidence window. Register A29 is written to fire on exactly this condition.

Recommendation: escalate this week, to Daniel Totino and the EUDM team by name. Four weeks without an owner on a defect sitting underneath every order-matching claim WAM makes is past the aging threshold.
Decider: Darryl.

**D2. Two data-completeness defects or one escalation?**

Sample orders are confirmed absent from EUDM outright, requiring NetSuite hydration. That is distinct from truncation, and adjacent to the open INC5456198 thread on Core ERP orders missing from the EUDM table.

Recommendation: one escalation, one owner, all three symptoms named. Separate threads into the same upstream team produce separate partial answers.
Decider: Darryl, with Akansh.

**D3. WAM forum consolidation.**

Seven recurring WAM forums sit on the cadence map. On 09-01, Requirements definition and WAM Product discussion conflicted with each other and with Daily Stand Up.

Recommendation: David brings a consolidation proposal to the session rather than resolving it live. Name which forums merge, which are delegated, and which Darryl stops attending.
Decider: Darryl, on David's proposal.

---

## Part 2 — Active register

Walked in full every session. One line each: moved, did not move, closed. Items at four weeks or more with no movement get disposed of in the session.

| ID | Item | Owner | Next step | Date | Status | Wks | EOS ref |
|---|---|---|---|---|---|---|---|
| W1 | Truncated manufacturer part numbers, DDP/EUDM vs WAM/ADM, exact matching fails | Akansh Gangil, escalating to Darryl | Named fix owner in the EUDM team | 2026-09-08 | **Aged, disposition required** | 4 | `05` A29, B53 |
| W2 | Sample orders absent from EUDM, NetSuite hydration required | Akansh Gangil | Confirm scope and fold into the W1 escalation | 2026-09-08 | Open | 1 | `04` WAM/ADM data integrity. No `05` entry: candidate B |
| W3 | Core ERP sales orders missing from EUDM table, INC5456198 | Akansh Gangil | Upstream cause from BI_Wesco_Integration_Support_L2 | 2026-09-15 | **Aged, disposition required** | 6 | `04` Active. No `05` entry: candidate B |
| W4 | WMX complex build: WMX vs VAS ownership, mandatory capture, P360 configuration, non-DDP site impact | Darryl | Confirm the Daniel Totino session happened; Centremis RFI 09-02 is the decision forum | 2026-09-08 | **Aged, disposition required** | 8 | `05` A1 |
| W5 | Supplier attribute requirements into Jarod Booth's organization | David Blondel | Confirm still needed as tracked, or close | 2026-09-08 | **Aged, disposition required** | 8 | `05` B1 |
| W6 | September release production validation: default end-user assignment, bulk edit, cancelled-order handling, pending-activation fix | Akansh Gangil | Confirm production behavior, report any regression | 2026-09-08 | Open | 1 | Forum only |
| W7 | Legacy record disposition, roughly 13,000 to 13,500 records pending the 09-01 release | Akansh Gangil | Current count and a disposal plan | 2026-09-15 | Open | 1 | Forum only |
| W8 | Part taxonomy AI pilot requirements, Akansh as ADM Product Owner and acceptance authority | Akansh Gangil | Requirements to acceptance-ready state | Not dated | **Aged, needs a date** | 4 | `05` B22 (taxonomy criteria strand) |
| W9 | WAM financial narrative: cash-flow P&L, package for Rob Cook, possible development carve-back | Darryl | Current state of the package, and whether anything needs saying before it lands | 2026-09-15 | **Aged, disposition required** | 6 | `04` Active. No `05` entry: candidate A |
| W10 | WAM forum consolidation and calendar conflicts | David Blondel | Proposal to this forum | 2026-09-08 | Open | 1 | Candidate `03` decision |
| W11 | WAM benefits realization: no recurring forum exists for it | Darryl | Decide whether this forum absorbs it or a separate review is stood up | 2026-09-15 | Open | 1 | `07` known gap. Candidate `03` decision |
| W12 | Sean program update: license data usability, serial numbers and metadata to the business. No program update has been given to Sean to date | Darryl | Confirm scope and timing with Sean; issue the information requests to Akansh and David | 2026-09-08 | New | 0 | Candidate A. Prep: `Deliverables/WAM/2026-09-01_Sean_WAM_Program_Update_Prep.md` |
| W13 | Strev 2027 product enhancement priorities and cost. Three areas: asset data management, tenant cloning, API modernization. No costs in the source; no Strev line visible in the FY27 WAM P&L; entroCIM and Ascent named as integration targets | Akansh Gangil | Sizing from Strev by area; confirm where SOW spend sits in the plan; confirm whether a Strev FY27 AOP entry exists | 2026-09-08 | New | 0 | Candidate A. Source: `Products/WAM/Strev_2027_Priorities.md` |
| W14 | Internal collection of serial numbers and asset metadata. Five constraint holders, four outside Darryl's organization. Serial-to-VAS association does not happen today; VAS standard work capture in place since 08-27, unproven at volume | Darryl | Coverage numbers from Akansh; confirm WMX 5.7 field delivery; name the owner for the complex-build path | 2026-09-08 | New | 0 | Candidate A. `04` complex-build attributes row |

**Aging note.** Six of fourteen items are at four weeks or more. That is the pattern this register exists to make visible, and the first session should expect to spend most of the register walk disposing of them rather than reviewing them.

---

## Part 3 — Parked

Nothing parked yet. Items move here when the active list exceeds twelve, annotated with date and reason. Never deleted.

---

## Part 4 — Closed

| ID | Item | Closed | Resolution |
|---|---|---|---|
| | | | |

---

## Below the line: sent in writing, not read aloud

Sprint status, backlog counts, ticket-level detail, defect narratives not blocking a decision, and anything already covered in Backlog Refinement or Sprint Review.
