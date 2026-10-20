# Operating Cadence and Governance Forums

> The map of recurring forums that run the portfolio. Seeded 2026-07-13 from 30-day baseline. Claude updates when cadence changes surface (weekly prompt captures new/cancelled/restructured forums).

## How This File Is Used

1. **Decision routing** — every open decision in `03_Decision_Log.md` gets a target forum and date. Decisions without a forum drift; this file is the routing table.
2. **Meeting preparation** — briefing section 6 (Meeting Preparation) prioritizes forums from this list that fall in the next 1–2 days and carry an open decision, risk, or commitment.
3. **Delegation and time audit** — each forum has an engagement level (below). When Darryl attends "By exception" forums routinely, that is time below Senior Director level; briefings should flag it.
4. **Cadence drift** — new recurring meetings are a signal of new workstreams or governance gaps; cancelled ones can signal stalls. Meeting frequency is never proof of risk.
5. **Written before meetings** — before adding another executive meeting, consider whether a written portfolio update serves better (library principle).

## Governance Lane (added 2026-10-16)

Forums marked **By exception** that run on a team's own governance (a project process or a sprint cycle) are **team-governed**: their issues go to the Operational Pulse (`Registers/pulse/`), not the registers, and reach Darryl only by escalation. The classification lives in `Registers/pulse/_forums.json`. **All thirteen confirmed by Darryl, 2026-10-16**: he attends some of these forums and is invited to all of them on purpose, to keep his finger on the pulse. Attendance is awareness, not ownership; an Attend engagement level below does not make a forum Darryl-owned.

**Darryl's two weekly governance meetings** (2026-10-16) are where the Pulse is worked. Each team-governed forum belongs to one track, and the web app produces one weekly agenda per track across all its forums.

| Track | Leads | Forums |
|---|---|---|
| Delivery governance | Chad Steger, Syed Jamshed Zaidi | 2026 Deployment Daily Scrum; Quest Migration Weekly Check-In; Deployment Team Knowledge Share |
| Development governance | Ron Snyder, David Blondel | entroCIM Daily Stand Up; entroCIM Backlog Deep Dive; DCOE & entroCIM Weekly; Showcase recurring; WAM Product Backlog Refinement; WAM Sprint Review; WAM India Dev Team weekly; WAM Product discussion; ADM connect with Natalie; Product Team / Platform Team connect |

## Engagement Levels

- **Own** — Darryl chairs; his presence is the forum.
- **Attend** — decision or alignment value requires him.
- **By exception** — team-run; attend only when a decision or escalation needs him. Default: delegate.

## Core Product, Delivery, and Governance

| Forum | Cadence | Owner | Purpose / Signal | Engagement |
|---|---|---|---|---|
| Delivery governance (new 2026-10-16) | Weekly, to be scheduled | **Darryl Benson**, with Chad Steger and Syed Jamshed Zaidi | Work the Pulse for the delivery track from its weekly governance agenda: stuck, decisions, new, quiet, escalated. Readout format: Chad and Syed report on the health of the deployment business, Darryl questions from the Pulse. Standing agenda: `Deliverables/Portfolio_Admin/Delivery_Governance_Agenda.md` (2026-10-16) | Own |
| Development governance (new 2026-10-16) | Weekly, to be scheduled | **Darryl Benson**, with Ron Snyder and David Blondel | Work the Pulse for the development track (entroCIM and WAM) from its weekly governance agenda | Own |
| WAM Product Leadership Sync | Weekly | David Blondel | WAM leadership alignment, product direction. **Structured format imposed 2026-09-01** (`Reference/Meeting_Agenda_Standard.md` v2.1): Darryl maintains and publishes a rolling agenda register (`Deliverables/Portfolio_Admin/WAM_Product_Leadership_Sync_Agenda.md`), David chairs to it, transcription on and recording off, summary to the chat inside 24 hours. Format reviewed at six sessions, roughly 2026-10-20 | Attend |
| ADM connect with Natalie | Weekly | Akansh Gangil | ADM/WAM execution, supplier data, renewal notifications | By exception — **raise to Attend while the truncated part number and leaf-node dependencies are open.** Cadence reconfirmed 2026-08-25 by the facilitator. This is where WAM's data-foundation defects actually surface, and both current blockers were first evidenced here |
| WAM Product discussion | Weekly (cadence being adjusted 08-03 evidence — likely to avoid conflict with the new Wesco Asset Manager Backlog Deep Dive) | Akansh Gangil | WAM product + commercial/operational alignment | By exception |
| WAM Data Challenges (Problem Definition) | Weekly | **Darryl Benson** | Data quality, P360/DDP/EUDM alignment, AI POC | Own — needs decision output, not just discussion |
| DDP Entrance Call | Weekly (Monday) | Anna Baker | DDPTRK-6346 and broader DDP plan tracking | Attend — new 07-16, keep DDPTRK-6346 visible |
| WAM Product Backlog Refinement | Bi-weekly | Sakshi Mathur | Backlog grooming, sprint sequencing | By exception |
| WAM India Dev Team weekly (reinstated 07-20) | Weekly | TBC — confirm owner and exact meeting name | Operational-hardening execution tracking (7-problem stabilization plan, Aug 3 gate items) | Attend while hardening plan is live; revisit engagement level once stabilized |
| WAM Sprint Review | Bi-weekly | Sakshi Mathur | Sprint progress, stakeholder visibility | By exception |
| Daily Stand Up (entroCIM) | Daily | Ron Snyder | Execution, blockers, release readiness | By exception |
| 2026 Deployment — Daily Scrum | Daily | Chad Steger | Deployment execution and escalation | By exception |
| entroCIM Backlog Deep Dive | Bi-weekly | David Blondel | Backlog governance, roadmap tradeoffs | Attend |
| entroCIM Leadership Collaboration | Weekly | Ron Snyder | David/Ron/Chad/Darryl alignment. **Correction 2026-09-01 (Darryl, chat):** the 08-17 "priorities, blockers, personnel, messaging" framing recorded here came from weekly Copilot evidence months old and was never used in practice. It is retained as history, not as the forum's live purpose. The forum has run free-form. **Structured format imposed 2026-09-01** (`Reference/Meeting_Agenda_Standard.md` v2.1): Darryl maintains and publishes a rolling agenda register (`Deliverables/Portfolio_Admin/entroCIM_Leadership_Collaboration_Agenda.md`), Ron chairs to it, transcription on and recording off, summary to the chat inside 24 hours. Format reviewed at six sessions, roughly 2026-10-20 | Attend |
| Quest Migration Weekly Check-In | Weekly | Chad Steger | Migration governance | By exception |
| Showcase recurring | Bi-weekly | David Blondel | Showcase environment governance, demo readiness | By exception — until showcase decision made, then delegate |
| Deployment Team Knowledge Share | Periodic (4th session evidenced 07-23) | TBC — confirm owner | Platform deployment standardization, tooling/automation ideas | By exception |
| DCOE & entroCIM Weekly | Weekly | Balachandar Murali | Digital COE coordination | By exception |
| CSS Platforms All Hands | Periodic (cadence TBD) | Leadership | Portfolio-wide: commercial pipeline, AI strategy, delivery, migration, governance initiatives | Attend — decision-rich; 07-13 session raised 2 unowned decisions |
| Digital Products Portfolio Review | Periodic (cadence TBD) | Owner unconfirmed (Sean McCloskey and Chris Gazdic both present 07-20) | Cross-portfolio release updates (QPM/WMX), Charlotte go-live dependency, AI/IDP strategy follow-ups, WAB approvals | Attend — new 07-20, decision-rich (QPM 3.4.3 cross-team commitments, WAB approval for Claude code); confirm cadence and owner before next occurrence. **07-27: calendar conflict with Wesco Asset Management / External BIR: 2517699 Actuals — decide which to attend or pre-align.** |
| Dell Service Management Process | Cadence TBC — held 2026-07-27 | Owner TBC (Syed Jamshed Zaidi driving) | Dell/Wesco support handoff model across Freshdesk and ServiceNow — process documentation, ownership, closed-loop communication | Attend — new 07-27, decision-rich; confirm cadence and true owner before next occurrence  **Ownership confirmed 2026-08-25 (Darryl): Syed Jamshed Zaidi and Chad Steger own this as ongoing work, not a single action.** Former Register A10 closed as a mis-scoped standing duty. Darryl's role is escalation, not execution |
| Dell Program Delivery Alignment | New — first session 2026-08-03 | Owner TBC | Regain Dell confidence; align delivery resources, priorities, governance across the concurrent Dell threads (Limerick, Non-DC, FTE Franklin/Apex/Hortolandia, Service Management Process). Likely the consolidating forum for A10 | Attend — new, decision-rich; confirm whether this absorbs Dell Service Management Process or runs alongside it |
| Wesco Asset Manager Backlog Deep Dive | New — bi-weekly, starts 2026-08-05 | Owner TBC | WAM priorities, risks, ownership, action items — new cross-functional forum; Amy Aguirre unable to attend the first session | Attend — new; pre-align priorities and capture Amy Aguirre's input separately before the first session |
| [Placeholder] EntroCIM Project Closeout Process Review | New — unconfirmed cadence, 2026-08-04 | Owner TBC | Proposed repeatable closeout standard: gates, ownership, evidence, customer acceptance, financial closure, handoff criteria | Attend — new, could resolve the recurring "resolution detail not documented" pattern seen on several closed items (TCCC Airwall, FRB SASTEC) |

## 1:1 and Leadership Alignment

| Forum | Cadence | Owner | Purpose | Engagement |
|---|---|---|---|---|
| Darryl / Nate Weekly 1:1 | Weekly | Nathan Kehr | Customer/commercial positioning, key accounts | Attend |
| Darryl – Ron 1:1 | Weekly | Darryl | entroCIM delivery, backlog, release | Own |
| Darryl – Chad 1:1 | Weekly | Darryl | Deployment, operating execution | Own |
| Weekly Sync (Amy Aguirre) | Weekly | Darryl | IAM strategy, value proposition | Own |
| Digital Products / Agile Staff Meeting | Weekly | Chris Gazdic | Portfolio/leadership context. **Standing expectation from Sean (10-20, transcript): keep the team updated on Launch Studio as it progresses**; Register D, no completion state. Transcripts have been retrievable (09-08, 09-15, 09-29, 10-20); not a Pulse forum | Attend |
| Product Team – Platform Team connect | Weekly | Keyur Patel | Product/platform coordination | By exception |

## Commercial, Finance, Customer, External

| Forum | Cadence | Owner | Purpose | Engagement |
|---|---|---|---|---|
| entroCIM Sales Ops/Finance Sync | **Twice-monthly (changed 2026-08-05, was Weekly)** | Tom Boss | Commercial and cost alignment | By exception |
| WAM / External BIR: 2517699 Actuals | Monthly | John Erickson | WAM actuals/reporting | Attend |
| Wesco / SkyFoundry | Monthly | Darryl | Ecosystem coordination (Xeto) | Own |
| BAE/Wesco Weekly | Weekly | Kevin Cochran | External customer cadence | Attend |
| Smart Buildings Issues Log Catch-Up | Bi-weekly | Raj Ramroop | External issue-log forum | By exception |
| Weekly Time Report Reminder | Weekly | John Erickson | Admin | Ignore (admin) |

## Standing Responsibilities (Register D)

> Moved here 2026-07-27 from `05_Commitments.md` per `EOS_Redefinition_Proposal_2026-07-27.md` §4.1. These are recurring role duties with no completion state. Tracking them as commitments permanently inflated the register and diluted items that could actually be closed. They are not commitments and are not counted as such.

| Responsibility | Nature | Where it shows up |
|---|---|---|
| Leadership oversight of the WAM data challenges initiative | Standing ownership of a Darryl-owned forum | WAM Data Challenges (weekly). Track "sessions since last decision," not completion |
| Participate in the WAM executive product review process | Standing participation in portfolio governance | WAM executive product review cycle |
| Sean McCloskey strategic touchpoints | Standing leadership relationship | On-demand written updates per the 2026-07-14 decision (`Reference/Sean_Update_Standard.md`), not a recurring meeting |

Specific, dated deliverables arising from any of these still enter Register A normally. The standing duty itself does not.

## Standing Observations

- **New meeting artifact, 2026-10-05 (weekly evidence): "WAM Leadership Sync" email/Teams/Loop files created or modified today.** Possibly a new leadership-level WAM cadence forming, distinct from the existing WAM Product Leadership Sync (David Blondel, weekly). Recurrence not established in retrieved metadata — confirm before adding as a standing forum; do not assume it duplicates or replaces the existing Sync.

- **Forum structure, added 2026-09-01.** Two forums now run on rolling agenda registers rather than free-form discussion: the WAM Product Leadership Sync and entroCIM Leadership Collaboration. Darryl owns the register, the forum owner chairs to it. Standard and reconciliation model in `Reference/Meeting_Agenda_Standard.md`. Candidate forums for the same treatment, in priority order: WAM Data Challenges (Darryl-owned, weekly, no decision output to date, the strongest candidate), Wesco Asset Manager Backlog Deep Dive, entroCIM Backlog Deep Dive.

- Darryl owns or attends ~15 recurring forums/week at listed cadence. The daily stand-up and daily scrum alone are ~10 slots/week of execution-level content — highest-value delegation target.
- Decision forums without decision output: WAM Data Challenges (Darryl-owned) has run weekly with problem-definition status only. Briefings should track "sessions since last decision."
- No recurring forum currently exists for: WAM benefits realization review or portfolio-level (cross-product) review. Gaps worth deliberate choices rather than accidents.
- **Darryl ↔ Sean structured update: resolved deliberately 2026-07-14** — on-demand written updates (`Reference/Sean_Update_Standard.md`) rather than a recurring meeting, per the written-before-meetings principle. The monthly Sean-visibility audit (`Reference/EOS_Analytics_Standard.md`) guards against under-reporting.
