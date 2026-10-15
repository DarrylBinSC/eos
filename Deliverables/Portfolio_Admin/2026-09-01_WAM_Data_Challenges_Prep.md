# WAM Data Challenges — Meeting Prep

**Prepared:** 2026-09-01
**Forum:** Hold - Problem Definition and Brainstorming: WAM Data Challenges. Weekly, Darryl chairs.
**For:** the next session, if there is one. See section 1.

---

## 1. The finding that changes what this prep is for

**No session has been evidenced since 2026-07-30. That is five weeks.**

The record, stated as evidence rather than inference:

- The 2026-08-17 weekly briefing states directly: "WAM Data Challenges (Darryl-owned): no session evidenced this cycle; still counting from the 07-30 named-deliverables session."
- No session appears in any evidence package between 08-03 and 08-31.
- Commitment B7, "export the ADM database for the WAM Data Challenges team," was dropped on 2026-08-25 with the reason "forum-gated, no reference in three consecutive packages." A forum-gated item aged out because the gate stopped opening.
- `07_Operating_Cadence.md` still lists the forum as weekly and Darryl-owned.
- The 09-01 weekly's "not transcribed at source" list covers 08-24 and 08-25 only and does not include this forum, so absence from the record is not explained by absence of transcription in that window.

Three explanations fit. The forum lapsed. It ran without producing any evidence trail at all. Or its content migrated into the newer WAM forums that stood up in August, including the Wesco Asset Manager Backlog Deep Dive that started 08-05.

**So the first item is not an agenda. It is whether this forum should exist.** Building a structured agenda for a forum that has quietly stopped running would produce a well-organized meeting nobody attends, and it would count as progress in the operating record while changing nothing.

Confirm which of the three explanations is true before anything below is used.

---

## 2. What the forum was chartered to do, and what it produced

Purpose per `07`: data quality, P360/DDP/EUDM alignment, AI POC. Engagement level Own, annotated "needs decision output, not just discussion."

Four evidenced sessions, and the arc across them is real but incomplete:

| Session | What it produced |
|---|---|
| 07-22 and 07-23 | First forward motion. Moved from problem definition toward AI and data-filtering POCs, AI Council review, and asset-data ROI. Darryl committed to review the AI pilot with Shawn and present it to the AI Council. Nitin Pandey's team to run small POCs on automated part identification. Neil asked for a direct benefits and ROI report on WAM. |
| 07-24 | Direction sharpened: deprecate third-party classification APIs, pursue IDP plus semantic search plus supplier-data enrichment instead. Two team risks surfaced separately: a large historical ADM bug backlog parked without disposition, and a single-point dependency on Natalie Marquardt for supplier-data collection. |
| 07-30 | 29 bugs open, some earlier "bugs" found resolved or not defects. Major new functionality not started. Six named deliverables assigned. |

The decision log entry for this thread still reads "no remediation decision yet," which was true on 07-30 and has not changed since.

**Assessment.** The forum was working. Three consecutive sessions each sharpened scope and produced named owners. It was one or two sessions away from a remediation decision when it stopped appearing in the record. That is a different failure from the one `07` warns about; the risk was workshops running indefinitely, and what appears to have happened instead is that the workshop stopped without landing the decision it had been building toward.

---

## 3. Deliverables named in the forum and never closed

None of these have a recorded closure. Ask about each by name.

| From | Deliverable | Named owner | Register |
|---|---|---|---|
| 07-30 | Quarterly roadmap deck with the "big rocks" | David Blondel, Akansh Gangil | `05` B22 |
| 07-30 | Publish the big-rocks feature list in Teams | Akansh Gangil | `05` B22 |
| 07-30 | Rhombus IDP integration design with fallback mechanisms, presented to Balasubramanian K | Akansh Gangil | `05` B22 |
| 07-30 | Short-term AI/ADM item-classification approach evaluated | David Blondel, Akansh Gangil | `05` B22 |
| 07-30 | Taxonomy terms and filtering criteria from the governance team | Akansh Gangil | `05` B22 |
| 07-30 | Prioritized WAM automation list to Nitin Pandey's team | Akansh Gangil | Not in `05` |
| 07-23 | AI pilot reviewed with Shawn, then presented to the AI Council | Darryl | Not in `05` |
| 07-23 | Automated part-ID output shared with the team | Darryl | Not in `05` |
| 07-23 | License discussion with Shawn and Merwan | Darryl | Not in `05` |
| 07-23 | Direct benefits and ROI report on WAM, requested by Neil | Unassigned | Not in `05` |
| 07-24 | Reconnect with the IDP team on expanding extraction capability | Darryl | Not in `05` |
| 07-24 | AI Council prep materials reviewed ahead of the approval meeting | Darryl | Not in `05`, no meeting date evidenced |

Four of the twelve are Darryl's own. That is the part of this worth sitting with: the forum's owner carries four unclosed deliverables from the last session it held, and the forum then stopped meeting.

Two structural items also surfaced on 07-24 and were never dispositioned: the parked historical ADM bug backlog, and the single-point dependency on Natalie Marquardt for supplier-data collection. Both are capacity and ownership questions rather than data questions, which is probably why a data forum did not resolve them.

---

## 4. What has changed underneath the forum since 07-30

The problem the forum existed to work on got worse, not better, and it moved to other rooms.

- Truncated manufacturer part numbers: still no named fix owner. Register A29 is written to fire on exactly this and has not been pulled. Four weeks.
- Sample orders absent from EUDM, requiring NetSuite hydration: a second, distinct completeness defect, surfaced in the 08-31 window.
- Core ERP sales orders missing from the EUDM table, INC5456198: open since 07-27.
- The 09-01 weekly names upstream data ownership as a recurring theme at its fourth occurrence without a named owner or a decision-log entry.
- The September WAM/ADM release shipped 09-01 onto that foundation.

All three defects are now carried on the WAM Product Leadership Sync register as W1, W2 and W3. That is the practical argument for the consolidation option in section 5.

---

## 5. Decisions for the session

**D1. Does this forum continue?**

Options: restart it weekly with a rolling register and a decision deadline; fold its content into the WAM Product Leadership Sync register, which already carries the three live data defects; or close it deliberately and record that the data-challenges work now runs through the Backlog Deep Dive and the Product Leadership Sync.

Recommendation: fold it in, and say so out loud rather than letting it lapse. The three defects it was chartered to fix are already tracked on another register with named owners and dates. A second weekly forum on the same subject splits attention and gives both rooms a reason to assume the other one owns it. The exception that would change this recommendation is the AI and IDP track, which has no other home; see D3.

Decider: Darryl. This is entirely his call, since he owns the forum.

**D2. The remediation decision that never landed.**

The decision log has carried "WAM data challenge remediation approach" with status "no remediation decision yet" since July. Whatever happens to the forum, that entry needs to close or move.

Recommendation: state the remediation approach as decided, on the direction the 07-24 session already reached (deprecate third-party classification APIs, pursue IDP plus semantic search plus supplier-data enrichment), and record it. The direction was set. It was the recording that never happened, and an undecided entry in the log for six weeks is not evidence that the thinking is unfinished.

Decider: Darryl.

**D3. The AI and IDP track needs an owner and a forum.**

The AI Council approval meeting has no evidenced date. The Rhombus IDP design, the part-classification approach, the taxonomy criteria and the automation list are all sitting on Akansh through B22, with no forum reviewing them since 07-30.

Recommendation: name a single owner for the AI and IDP track and a forum that reviews it, before deciding D1. If that forum is not this one, D1's recommendation to fold in is straightforward. If nothing else can hold it, that is the argument for keeping this forum alive with a narrowed charter of AI, IDP and classification only, and moving the defect work permanently to the Product Leadership Sync.

Decider: Darryl, with David and Akansh.

---

## 6. Questions to ask, in order

1. Has this meeting run since 07-30, and if it has, why is there no record of it?
2. Of the six deliverables named on 07-30, which are done? Ask by name; B22 bundles four of them and a bundle can look alive while every strand inside it is stalled.
3. Has the AI Council approval meeting happened, or been scheduled?
4. Who owns the WAM benefits and ROI report Neil asked for on 07-23? It has never had a named owner.
5. What happened to the parked historical ADM bug backlog, and is Natalie Marquardt still the single point for supplier-data collection?

---

## 7. If the forum continues

Say "seed the WAM Data Challenges register" and it gets the same structure as the other two: rolling items with owner, next step, date and weeks open, reconciled weekly against `05` and `03`. The twelve unclosed deliverables in section 3 are the seed, and eight of them would open at more than four weeks, which means the first session would be a disposition session rather than a working one.

If the forum is folded in instead, the AI and IDP items move onto the WAM Product Leadership Sync register as new entries, and the decision-log thread closes with the D2 recommendation.
