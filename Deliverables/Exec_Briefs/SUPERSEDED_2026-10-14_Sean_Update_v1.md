# Sean Update, week of 2026-10-19 (DRAFT 2026-10-14)

> Supersedes `SUPERSEDED_2026-10-13_Sean_Update.md`, whose WAM row said the integration architecture and limitations slide were still owed. Both are in hand. **Do not send until Akansh reconciles the staffing numbers** (see notes). Bring to the meeting with Sean the week of 2026-10-19; also covers the CDA summary owed under `05` A59.

---

Sean,

WAM/ADM can keep today's production capability running on half the team. At that level, the work that lets it scale slows sharply, and most of what limits it sits outside the team. I need your call on the capacity level, and your help on two upstream process changes.

**Portfolio position**

| Product | Position |
|---|---|
| entroCIM | Executing the reduced-capacity FY27 roadmap from your 10-06 call. No change. |
| WAM | 2027 capacity reset ready for your decision (below). The story needs resetting with it: scale depends on data Wesco systems don't yet hold. |
| Ascent Navigator | No change. |
| CDA | Carried on the entroCIM roadmap with no FY27 line, as you set 10-06. Bill Muczko's sponsorship holds; enterprise pricing still being tested. |

**WAM/ADM capacity**

The team is 15 today (6 backend, 2 data engineers, 2 front end, 5 QA), against 19 in the AOP draft. The skill mix follows the integration tools: EUDM integration runs on Azure Databricks, Strev on APIM.

| | Run only | Run plus DDP | Run plus all completion |
|---|---|---|---|
| Team | 8 | 11 | 14 |
| License sync, renewal notifications, production support | Kept | Kept | Kept |
| Enterprise data (DDP/EUDM) | Held below the three Databricks engineers needed to advance it | Advances | Advances |
| Product development and Strev integration completion | Extended substantially | Extended substantially | Planned pace |

Recommendation: Run plus DDP. Every constraint now limiting ADM is upstream data, and your 09-25 direction puts the foundation on Wesco-owned data through DDP/EUDM. The historical-data target of Q1 2027 comes off the plan; there is no committed date at any of the three levels.

**Expectations to reset**

- Asset data can sync from ADM to Strev only when it already exists in Wesco systems such as IAP, EUDM and WMX. Many asset programs today run on Excel files built by warehouse and supply chain teams (sales order, serial number, MAC ID), which Managed Services uploads into Strev. ADM can't automate data the enterprise doesn't hold.
- Near term, the team is helping Managed Services automate preparing those uploads. The long-term fix is capturing the data in Wesco systems, which is a process change outside WAM.
- Renewal revenue can't be measured closed-loop yet. Nothing in DDP marks an order as a renewal, so Sales Operations marks them by hand in ADM, which won't hold at volume.

**Decisions needed from you**

1. Capacity level for 2027. Recommend Run plus DDP (11). I need your answer to finalize the plan with David and Akansh.
2. Support with the GPOs on two process changes: flagging renewal orders when the rep creates them, and capturing serial and MAC data in Wesco systems. The second is already in the cross-SBU effort you joined 09-30; the first is not yet on anyone's agenda.

**Ask**

30 minutes next week: WAM/ADM capacity first, then a short CDA summary.

Darryl

---

## Editorial notes

- **Staffing numbers must reconcile before this goes.** Akansh's stream Run figures (DDP 2, product development 3, Strev integration 1) sum to 6 against his 8-person run team; Run plus Complete sums to 14 against 15 today. The option sizes above assume the run team is 8 and "Run plus DDP" adds DDP's 3 Complete (11). Confirm both with Akansh (Teams draft 2026-10-14) and correct the table if needed.
- **The recommendation is Claude's, built from the record** (09-25 Wesco-owned-data direction, all six constraint asks upstream, ADB floor of 3). Change it if your read differs; the table works with any of the three.
- **Priority order of Complete items is not in the record.** Sean may ask which completion items slip under Run plus DDP. Akansh has not provided the ordered list; it is in the Teams ask.
- **Left out on purpose:** the six-row constraints slide (detail behind "upstream data"), the Strev API failure (no dependent workflows affected), Zapier (settled 10-05), the $697K scorecard figure (not attributable to notifications), and the 10-30 enrichment date. Bring the constraints slide as backup if Sean wants the detail.
- **Akansh's asset-sync message** is in the second section, as he asked, compressed to Sean's altitude.
- No em dashes.
