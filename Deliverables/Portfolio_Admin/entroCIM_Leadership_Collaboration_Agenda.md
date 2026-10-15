# entroCIM Leadership Collaboration — Rolling Agenda Register

**Maintained by:** Darryl Benson. Updated in place every week. Do not create a new file per session.
**Chaired by:** Ron Snyder
**Attending:** Ron Snyder, David Blondel, Chad Steger, Darryl Benson
**Format:** `Reference/Meeting_Agenda_Standard.md` v2.0
**Transcription:** On. Recording off. Open floor may run untranscribed by agreement.

**Next session:** assumed Monday 2026-09-08, based on the 2026-08-24 instance in the 09-01 weekly briefing. Confirm the actual slot.
**Last updated:** 2026-09-01

---

## Part 1 — Decisions required this session

**D1. The Federal Reserve 3.1.12.13 release is held and the customer has not been told. Two dates are needed, and they should not depend on each other.**

A bug blocks dev-to-prod promotion. Adam Slingerland and Ron are working it; Babu Papanna promotes once it clears. No customer communication has gone out. The same holding pattern was evidenced on 08-27 and again in the 08-31 window, so this is a continued stall, not a new item. FRBNY has a Cash Services Center presentation on 09-08 and 09-09.

Recommendation: decouple. FRB hears about the hold from Wesco this week whether or not the bug closes. The trust cost of FRB discovering it independently, days before a shortlisted presentation at the same account, exceeds the cost of telling them.
Decider: Ron on the fix date, Darryl on the communication call.

**D2. Does this forum become the decision route for a standard commercial support and SLA structure?**

The item sits in the Decision Backlog with no forum and no date. It surfaced through the Ford UDAC re-alignment, where Ford and Wesco aligned on renewing UDAC support, letting EDC support expire, and using an SLA for unplanned support with SOW and SME hours for planned scope. The 09-02 training catalog session was expected to resolve adjacent release-notes, webinar, SME-hours and Freshdesk ambiguity.

Recommendation: name this forum as the route and put a date on a first draft. It has now been discussed in three separate contexts without an owner.
Decider: Darryl.

**D3. Is a manual reset procedure an acceptable position on Dell alarming until the October release?**

Intermittent alarming failures traced to alarm-database corruption. No root cause identified. Preventive fix scheduled for the October release. The only current remedy is a manual live-reset.

Recommendation: tell the customer explicitly that alarming is unreliable until October, and name who says it. An alarming platform that intermittently stops alarming is a safety-adjacent claim, not a defect backlog entry.
Decider: Darryl, with Ron and Chad.

---

## Part 2 — Active register

Walked in full every session. Items at four weeks or more with no movement get disposed of in the session.

| ID | Item | Owner | Next step | Date | Status | Wks | EOS ref |
|---|---|---|---|---|---|---|---|
| E1 | FRB 3.1.12.13 held, customer not told | Darryl (communication), Ron Snyder (fix) | Customer-communication date from Sarah Monteleone, independent of the fix | 2026-09-08 | Open, escalated | 2 | `04` Active. No `05` entry: candidate A |
| E2 | FRB QA-1 non-VPN test and map-defect root cause, gating promotion | Adam Slingerland, Ron Snyder | Bug closure date | 2026-09-08 | Open, critical | 2 | `05` B24 |
| E3 | Dell alarm-database corruption, no root cause, October fix, manual reset only | Ron Snyder | Root cause, and a customer position for the interim | 2026-09-08 | Open | 2 | `04` Active. No `05` entry: candidate B |
| E4 | Standard commercial support and SLA structure for renewals and managed services | Darryl, Nathan Kehr | Name the forum, date a first draft | 2026-09-08 | Open | 2 | `03` Decision Backlog |
| E5 | ServiceNow Field Service dev-environment access rejected, blocks connector development | Ron Snyder | Escalation path, and whether it needs Darryl | 2026-09-15 | **Aged, disposition required** | 4 | `04` Active. Adjacent to `05` B11, B47, not the same item |
| E6 | Disney SSO onboarding failure, 7 Hudson, audience/metadata error after network changes | Shawn Clark | Confirm the JJ Watson working session happened and what it produced | 2026-09-08 | **Aged, disposition required** | 5 | `05` B36 |
| E7 | Louvre Abu Dhabi closeout, snag-list stall, items not confirmed tracked in Jira | Chad Steger | Confirm tracking and a closeout date | 2026-09-15 | **Aged, disposition required** | 5 | `04` Active. No `05` entry: candidate B |
| E8 | CrowdStrike overly permissive ingress rule, Azure VM in the entroCIM environment | Chad Steger | Remediation plan and a date | 2026-09-08 | **Aged, disposition required** | 6 | `05` A32 |
| E9 | FRB Maiden Lane capacity and scaling, three buildings, 60,000-plus points | Ron Snyder | Sizing recommendation to the customer | 2026-09-15 | **Aged, disposition required** | 5 | `04` Active. No `05` entry: candidate B |
| E10 | Dell FTE assessment reliability, Franklin, Apex, Hortolandia. Equipment findings unreliable until connector stability is addressed | Chad Steger | Connector and controller stability plan | 2026-09-15 | **Aged, disposition required** | 6 | `04` Active. No `05` entry: candidate B |
| E11 | October release 10-05, customer presentation 10-09 | Ron Snyder | Confirm on track and name the gate that would move it | 2026-10-05 | Open | 2 | Product due dates |
| E12 | Architect role move, Shawn Clark. Final decision is Shawn's. Babu Papanna's load in the FRB promotion path | David Blondel | Close out the move; assess Babu's capacity into the October release | 2026-09-15 | **Aged, disposition required** | 8 | `06` Stakeholder Map. Forum only |

---

## Part 3 — Parked

| ID | Item | Parked | Reason |
|---|---|---|---|
| E13 | Dell SOC 2 and security-evidence request, scope, requester and gating impact all unconfirmed | 2026-09-01 | Darryl's position is set: SOC 2 does not apply to a customer-hosted, customer-operated service. Returns to Active if Dell names a gating requirement. |
| E14 | Woolly AI Tech Review intake, then C2P | 2026-09-01 | Route and content owners named (Sourav Pradhan, Ron Snyder), no date. Returns to Active when a review date exists. |
| E15 | Project closeout process standard, including TCCC Quest-to-Azure closeout evidence | 2026-09-01 | A separate proposed forum exists for this. Returns to Active if that forum does not stand up by the October release. |

---

## Part 4 — Closed

| ID | Item | Closed | Resolution |
|---|---|---|---|
| | | | |

---

## Below the line: sent in writing, not read aloud

Sprint and stand-up detail, individual ticket status, deployment scrum content, and anything already covered in the entroCIM Backlog Deep Dive or the Deployment Daily Scrum.
