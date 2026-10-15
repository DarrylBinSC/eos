# EOS Use Case Review

**Date:** 2026-08-19
**Scope:** Every use the EOS has been put to since 2026-07-13, what the volume says about how it is actually used, what needs to change, and where to focus next.
**Method:** File-level census of the EOS folder plus register and ledger row counts, cross-checked against `10_Pilot_Feedback_Log.md`, `EOS_Redefinition_Proposal_2026-07-27.md`, and `EOS_Value_and_Purpose_Review_2026-08-06.md`.
**Relationship to prior reviews:** 07-27 fixed attribution. 08-06 fixed the primary surface. This one measures whether either fix held, and it finds that one did and one did not.

---

## 1. Conclusion First

The system has already become something different from what it was designed as. It was built as a briefing engine with a knowledge base attached. It is being used as a deliverable studio with a briefing engine attached. The 08-06 review predicted this shift and named it; five weeks of file evidence now confirms it, and the confirmation is strong enough to act on rather than to keep monitoring.

The single recommendation: **stop treating the register layer as a system that maintains itself through the daily loop, and stop investing effort proportional to its size.** The evidence is that intake into the registers runs continuously while disposal runs only when a special event forces it. Two forced events in five weeks account for every closure the system has ever recorded. Everything else in this document follows from that finding.

Second recommendation, smaller but with clearer payback: the Impact Ledger holds 41 evidenced wins and has produced zero upward communications in its entire life. That is the largest piece of built-but-unrealized value in the folder.

---

## 2. Use Case Inventory

Twenty distinct use cases are evidenced in the folder. Grouped by tier, using the 08-06 framework.

### Tier 3, Studio (highest output, highest value)

| # | Use case | Evidence | Volume | Status |
|---|---|---|---|---|
| 1 | Contract and agreement review | JCI Airwall MSP review (07-17), i3 Alliance §8 redline (08-06) | 2 major engagements, 7 files | **Highest value per unit of effort in the system.** The i3 review found a binary architectural exposure and an uncapped IP exposure that a prior legal review of an adjacent section had missed |
| 2 | RFP response drafting and review | FRB RFP sections 3.1 and 4.1 (08-19) | 5 files in one day | Newest use case, highest single-day output ever recorded |
| 3 | AOP and financial planning support | FY27 AOP change logs for entroCIM, WAM, CDA, Navigator; 4 IT demand collation templates; P&L analysis; headcount review deck | 4 change logs, 8 workbooks, 2 decks | **Currently the dominant workload.** Has no folder of its own |
| 4 | New product ideation through business case | CDA program, 5 phases, charter to AOP submission | ~40 files | Most developed body of work in the folder. Produced an intake deck, a business case, and a funded AOP line |
| 5 | Executive brief and pre-read drafting | 3 Sean briefs, Lisa Orton brief, Engel reset content | 7 files | Working, steady, low friction |
| 6 | Requirements engineering | Part Taxonomy ADM requirements v1 to v2, AI requirements framework, lessons-learned | 9 files | Heaviest single deliverable set. v1 came from ChatGPT, v2 was rebuilt here |
| 7 | Diagram production | Complex build asset flow (4 versions), Dell support process, 62443 mapping, CDA architecture | ~12 files | Working. `Reference/Mermaid_Standards.md` at 52 KB is the largest reference file, which is itself a signal of how much this is used |
| 8 | Slide and deck production | entroCIM architecture, CDA decks (7), headcount review, portfolio status | ~12 files | Working |
| 9 | Cross-LLM prompt authoring | ChatGPT ideation prompt, Copilot intake prompts, Part Taxonomy AI prompt, Tooling extraction prompts | 6 files | Distinctive use case. Not anticipated in the original design |
| 10 | Knowledge transfer and handoff | Chad Steger handoff digest | 1 file | One-off, worked |
| 11 | Escalation and troubleshooting support | Centremis RCA, TCCC Airwall vantage-point challenge, Dell Limerick | In-session, few artifacts | Value is evidenced in `09` and `10` rather than in files. The 07-28 Airwall challenge was adopted and changed the approach |

### Tier 1, Knowledge

| # | Use case | Evidence | Volume | Status |
|---|---|---|---|---|
| 12 | Product knowledge base curation | WAM, entroCIM, Navigator, CDA folders plus 6 root product files | ~75 files | Working, and the reason first-draft quality is holding |
| 13 | Stakeholder knowledge | `06_Stakeholder_Map.md`, 54 KB | Passive | Maintained, never surfaced as an interface. Team-interface pilot from 08-06 §7.3 has not been triggered |
| 14 | Standards and governance authoring | Mermaid standards, communication preferences, benefits realization, 62443 mapping template | 18 reference files | Working. `Communication_Preferences.md` is the one most often consulted |

### Tier 2, Radar

| # | Use case | Evidence | Volume | Status |
|---|---|---|---|---|
| 15 | Daily and weekly evidence-reconciliation briefing | 24 briefings | 07-13 to 08-19 | **Cadence declining.** See §3 |
| 16 | Decision, risk, and action registers | `03`, `04`, `05` | 41 radar + 14 backlog + 38 active risks + 91 actions | **Regrown past every threshold set for it.** See §4.1 |
| 17 | Field notes capture | `08_Field_Notes.md` | Inbox empty since 07-24 | **Dead channel.** 26 days |
| 18 | Impact and benefits capture | `09_Impact_Ledger.md`, 41 entries | 32 marked "not yet" communicated | **Built, never harvested.** See §4.4 |
| 19 | Sean update generation | `Reference/Sean_Update_Standard.md` | 0 generated | Never used |
| 20 | Dashboard | `Dashboard/` | Retired 08-06 | Correctly cut |

### Meta

EOS self-review is itself a recurring use case: the redefinition proposal (07-27), the register sort (07-27), the value and purpose review (08-06), and this document. Four structural reviews in five weeks is a high rate. It is not obviously wrong for a system this young, but it is worth noting that three of the four were triggered by the same underlying symptom.

---

## 3. What the Volume Says

**Briefing cadence is falling while deliverable production is rising.**

| Window | Working days | Briefings | Coverage | Deliverable files produced |
|---|---|---|---|---|
| 07-13 to 07-31 | 15 | 14 days covered (16 files) | 93% | 22 |
| 08-03 to 08-19 | 13 | 8 days covered | 62% | ~31 |

Deliverable production per working day is roughly 1.5 times the July rate. Briefing coverage is down by a third. These are not independent: the days without a briefing are largely the days with heavy deliverable work (08-18 and 08-19 produced the AOP change logs and the FRB RFP set with no daily briefing on 08-18).

**Assessment.** This is not drift or neglect. It is a rational allocation of a fixed session budget toward the output that produces more value, and it matches the core value metric named on 08-06 in your own words. The system should be reshaped to match it rather than pushed back toward daily briefing coverage.

**The one thing the 07-27 restructure fixed and kept fixed:** daily briefing size. It ran 7.9 KB on 07-13, peaked at 25.5 KB on 07-27, and has held between 7.1 and 9.9 KB on every daily since 07-28. That fix held. The register fix did not.

---

## 4. Material Findings

### 4.1 The registers have regrown past every threshold, for the third time

**Evidence, as of 08-19:**

| Register | Post-restructure baseline (07-27) | Today | Governing rule |
|---|---|---|---|
| Register A (My Actions) | 10 | 21 (19 dated, 2 triggered) | Target 10 to 15. "If it exceeds 20, the attribution test is being applied loosely, re-audit rather than expand" |
| Other-Owned (was B + C) | 22 | ~70 | Weekly surfacing, 14-day aging for non-Critical |
| Watch List, Active tier | 27 | 38 | Active means "needs attention" |
| Decision Radar | 24 | 41 | Radar means "has a forum and a date" |
| Decision Backlog | 6 | 14 | Monthly or on demand |

**Assessment.** The CLAUDE.md rule for Register A exceeding 20 has fired and has not been acted on. But the more useful reading is not that discipline lapsed. It is that the growth is structural. Look at where closures actually came from:

**Every register closure in the system's life happened on exactly two dates.** 07-27, the restructure, which closed nine items and dropped thirteen. And 08-07, the end-of-day check, which closed three, dropped one, and reassigned one. Archive rows carry no other dates. Twelve days have passed since the last closure of any kind, while items dated 08-10 through 08-19 were being added.

**Risk.** The registers do not fail loudly. They fail by becoming a list nobody can act on, which is precisely the symptom that triggered the 07-27 review ("commitments overstated, focus diluted"). This is the third occurrence of the same symptom with two different fixes already applied. A third structural fix of the same kind should not be expected to work either.

### 4.2 The one mechanism that demonstrably worked has stopped running

**Evidence.** The `eos-end-of-day-check` scheduled task, installed 07-27 as the push half of the feedback loop, fired on 08-07 and produced five dispositions in a single pass, including two mis-attributions that had sat in Register A for nine and eleven days. `05_Commitments.md` records this and explicitly notes that "the push mechanism produced the closures the pull mechanisms had not." There is no evidence of it running since.

**Assessment.** The falsification test written into CLAUDE.md was "if the end-of-day check regularly goes unanswered, the problem was never the capture mechanism." That is not what happened. It was answered, it worked, and then it stopped firing. That is an operational failure, not a design failure, and it is the cheapest thing on this list to fix.

**This is the highest-return single action in this document.** One working mechanism, currently off.

### 4.3 The 08-06 aging rule has not yet had its first opportunity to fire

**Evidence.** 70 Other-Owned items, of which 27 are tagged Critical and 43 are not. The Aged Out archive is empty. The rule requires 14 days past an item's own gate with no referencing evidence, and the clock was deliberately started on 08-06 rather than retroactively.

**Assessment.** State this precisely rather than calling it a failure: the earliest possible roll-off date is 08-20, tomorrow. The rule has not failed, it has not yet run. Two things are worth flagging now, before it does. First, 27 of 70 items carry the Critical tag, which exempts them, so the rule can only ever act on 61% of the list. Second, because the clock is not retroactive, the pre-08-06 backlog, which is the material that actually motivated the redesign, is permanently immune to it.

**Recommendation.** Let the rule run for two weeks and count what it actually clears. If it clears fewer than ten items by 09-02, make the clock retroactive and re-audit the Critical tags, since a 39% exemption rate suggests the tag is being applied as "important" rather than as "expensive to be wrong about."

### 4.4 The Impact Ledger is the largest piece of unrealized value in the folder

**Evidence.** 41 entries covering realized wins across entroCIM, WAM, TCCC, JCI, i3, FRB, and the Quest-to-Azure program. 32 explicitly marked "Communicated: not yet." The file header still reads "Last Sean update sent: none yet." Zero Sean updates have been generated in five weeks, against a standard (`Reference/Sean_Update_Standard.md`) that was written specifically for this.

**Assessment.** The 08-06 review diagnosed this correctly ("the file isn't the problem, the trigger is") and then did not install a trigger. The content is genuinely strong: the i3 §8 finding, the WAM notification suite shipping with unscoped additions and no date slip, TCCC narrowing from seven controls to one, sprint completion moving 81% to 91% to 94% under disruption. This is exactly the material that supports a benefits and operating-maturity narrative with Sean, and none of it has been sent.

**Risk.** Wins that are not communicated do not exist for the purpose of executive perception, which is the specific problem the 07-14 Engel and Hasting episode created in the first place. The ledger was built as the answer to that and has not been used as one.

### 4.5 Field Notes is dead and should be retired rather than left in place

**Evidence.** Inbox empty. Last entry 2026-07-24, processed 07-27. Twenty-six days.

**Assessment.** It was already demoted on 07-27 to a channel behind chat `log:` and the end-of-day check. The `claude:` tag inside it did real work earlier (the EOS naming rule, the David Blondel org correction, the Copilot file-output fix all came through it), but that traffic has moved into direct chat. Keeping an empty channel in the file map creates a false impression that manual capture is covered by three mechanisms when it is covered by one.

### 4.6 The Studio, which produces the most value, is the least governed part of the folder

**Evidence.** 57 files in `Deliverables/` across nine initiative folders, plus roughly 75 in `Products/`. Observable issues: five near-duplicate Part_Taxonomy variants in `Deliverables/WAM/` with no version convention distinguishing working from final; markdown and docx pairs stored side by side with no rule about which is canonical; `Deliverables/CSS_Platforms_2027_Ideation/` was flagged on 08-06 as probably superseded by `Products/CDA/` and is still unresolved thirteen days later; AOP material, currently the dominant workload, is split across `Products/*/` and `Deliverables/*/` with four differently-named change logs and eight collation workbooks carrying COPY, BACKUP, and SUPERSEDED prefixes.

**Assessment.** The governance effort in this system is concentrated on the tier that produces the least value and absent from the tier that produces the most. That is a direct consequence of the daily briefing being the thing that runs on a cadence: whatever the briefing touches gets maintained.

**Risk.** Moderate and rising. The specific exposure is picking up the wrong version of an AOP workbook or a requirements document during the FY27 cycle, when several near-identical copies exist and the naming does not distinguish them.

---

## 5. Recommendations

Ranked by return on effort. Owner is Darryl for all decisions; execution as noted.

| # | Recommendation | Why | Next action | Timing |
|---|---|---|---|---|
| 1 | **Restart the end-of-day check.** Confirm the scheduled task is live and firing weekdays at 16:30 | The only mechanism that ever produced routine closures. Off for 12 days. Near-zero cost to restore | Verify the task exists and is enabled; if not, recreate it | This week |
| 2 | **Install a Sean update trigger.** Generate one automatically with the first weekly briefing of each fortnight, from the Impact Ledger, whether or not it is asked for. Darryl edits or discards | 41 wins, 0 communicated, 5 weeks. The diagnosis was made 08-06 and the trigger was never built | Add to the weekly briefing workflow in `CLAUDE.md`; produce the first one from the current backlog | Next weekly, 08-24 |
| 3 | **Stop re-fixing the registers structurally. Cap them instead.** Hard ceilings, forced ranking, no exceptions: Watch List Active at 20, Decision Radar at 20, Register A at 15. Anything below the line moves to Passive or Backlog, not to a new tier | Two structural fixes in five weeks have not held. The third will not either. A cap does not require the intake discipline to improve, which is the variable that has not responded | Re-rank `03` and `04` at the next weekly and cut to the caps | Next weekly, 08-24 |
| 4 | **Give AOP and business-case work a first-class home and a naming convention.** One folder, one change-log format, one rule for which workbook is live | Currently the dominant workload, spread across two trees with COPY/BACKUP/SUPERSEDED prefixes, during the cycle where being wrong is most expensive | Consolidate the four FY27 change logs and eight workbooks under one structure | Before the next AOP gate |
| 5 | **Retire `08_Field_Notes.md` formally.** Remove from the file map, keep the archive | Empty 26 days. Its function moved to chat `log:` and the end-of-day check | One-line change to `CLAUDE.md` and `00_README` | This week |
| 6 | **Resolve the two flagged-and-unresolved items from 08-06.** Whether `Deliverables/CSS_Platforms_2027_Ideation/` is superseded by `Products/CDA/`, and whether to run the team-interface pilot | Both were decisions assigned to you on 08-06 and neither has been made. They are small, and leaving them open is what turns a folder into an archive | Answer both in one session | This week |
| 7 | **Let the aging rule run, then measure it.** Count what it clears by 09-02 | It has not yet had its first opportunity. Judging it now would be wrong | Review at the 09-02 weekly | 09-02 |

**Where to focus the work going forward.** Contract and agreement review, RFP response, and AOP and business-case support. These three share a profile: high stakes, document-heavy, dependent on product knowledge you have and the counterparty does not expect you to have applied, and each produced a finding or an artifact that would not otherwise have existed. The i3 §8 review is the clearest single example of the system's ceiling. That is the work to point it at.

---

## 6. What Should Not Change

- The four-register model and the attribution test. The problem is disposal throughput, not attribution, and re-opening attribution would repeat the 07-27 work for no reason.
- Evidence-basis discipline (Direct, Single-source, Repetition, Inferred) and the disposed-item Echo/Contradiction/Resemblance check. The Contradiction case has already earned its place twice.
- The daily briefing at one page and five sections. This is the one structural fix that held, and it has held for three weeks under load.
- `Products/` as the front door and the session-end filing rule. First-draft quality depends on it, and that is the named core value metric.

---

## 7. Counts as of 2026-08-19

For reference and for comparison at the next review.

- Briefings: 24 (16 in July window, 8 in August window). Daily coverage 93% then 62%
- Daily briefing size: 7.1 to 9.9 KB since 07-28, stable
- `Deliverables/`: 57 files, 9 initiative folders. WAM 23, entroCIM 11, Exec_Briefs 7, JCI 6, Portfolio_Admin 4, CSS ideation 3, CDA 1, Navigator 1, EOS_Meta 1
- `Products/`: ~75 files. CDA ~40 across 6 phase folders, entroCIM 20, WAM 7, Navigator 5, 6 root files
- `Reference/`: 18 files
- Register A: 21 (19 dated, 2 triggered). Ceiling 15, re-audit trigger 20
- Other-Owned: ~70 (27 Critical, 43 non-Critical). Aged Out: 0
- Watch List: 38 Active, 7 Passive, 11 Retired
- Decision Log: 22 Made, 41 Radar, 14 Backlog
- Impact Ledger: 41 entries, 32 uncommunicated, 0 Sean updates sent
- Field Notes: inbox empty, 26 days
- Register closure events: 2 (07-27, 08-07)
