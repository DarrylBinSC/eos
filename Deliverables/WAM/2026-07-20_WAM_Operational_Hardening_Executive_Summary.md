# WAM/ADM Operational Hardening: July 20 Backlog Refinement

**Prepared:** 2026-07-20 | **Source:** WAM Product Backlog Refinement (India team), meeting transcript and Loop notes

## The Message

This was not a feature-planning session. The team spent the meeting on operational hardening: seven data-quality and reliability problems in WAM/ADM, with a remediation plan for each. Two of the seven sit directly on the August 3 notification release path. The most important finding is positive: the reported "data loss" is almost certainly a visibility defect, not lost data. The records are in the database; activation defects and missing SO dates keep them from surfacing.

## The Seven Problems in One View

| # | Problem | Business Impact | Root Cause | Fix Direction | On Aug 3 path? |
|---|---|---|---|---|---|
| 1 | Cancelled orders polluting ADM | Wrong notifications to sales reps, contaminated analytics, exports, renewal calculations | No separation of active, cancelled, and removed line items | One-time hard delete now; then three tracks: data-layer status handling, UI exclusion everywhere, dedicated removed/cancelled audit tab | Yes, explicitly a prerequisite |
| 2 | Reported data loss / missing records | Users believe data is disappearing; trust erosion | Data exists but does not surface as activated (bug 7827); UI-only vs. DB loss still being confirmed | File-vs-UDM comparison, DEV-vs-EUDM analysis, scheduler investigation | Yes, feeds perceived quality |
| 3 | License activation failures | Records stuck in Pending Activation; the main driver of perceived data loss | Null license start dates and missing SO dates block activation logic, plus query and row-update failures | SO date handling, DDP code changes, activation logic fix; track as dedicated bug stories | Yes, feeds perceived quality |
| 4 | Duplicate record creation | Data integrity degradation in lower environments | Duplicate master integrator/vendor combinations; job logic permits duplicates | Bug report, path analysis, code fix, validation | No |
| 5 | Filter performance at scale | Load times, dropdown latency, page blocking at ~50K records; production failure risk as data grows | Filters attempt to load full datasets | Server-side pagination, type-ahead, independent filter loading; architecture review first | No, but grows with data volume |
| 6 | ADM database growth | Inactive data degrading performance | No archival strategy | Identify and archive inactive records | No |
| 7 | End-user matching inconsistency | Same user treated as multiple entities (case and format variants) | Case-sensitive matching, no normalization | Case-insensitive matching, uppercase conversion, corrective script on historical records | No |

## What This Means

Three points matter at leadership level.

First, this session confirms that WAM's limiting factor right now is data quality and operational reliability, not feature velocity. The team itself framed the session as data-quality stabilization wrapped in sprint planning. That is the right instinct and worth reinforcing.

Second, the customer-trust exposure runs through perception, not actual loss. Customers and sales users experiencing "missing data" are seeing an activation defect. That distinction changes the communication: the data is intact, the fix is known, and the narrative should say so before users draw their own conclusions.

Third, problems 1 through 3 and the August 3 notification gate are now the same workstream. The cancelled-order cleanup was explicitly called a prerequisite for trusted notifications, and activation defects determine whether the data behind those notifications is believed. The gate review has to cover all three, not just the original gate items (supplier exclusions, sender and format changes, SharePoint/FAQ).

## Open Questions the Plan Does Not Yet Answer

1. Sequencing conflict: hard delete before audit visibility exists. The immediate fix is a one-time hard delete of cancelled records. The audit tab that preserves traceability (Track C) comes later. If the delete runs before any snapshot or archive is taken, those records are gone with no audit trail, which contradicts the plan's own stated intent. This needs an explicit answer before the delete runs.
2. Is any of this scoped into the August 3 timeline? The problems are named as gate-relevant but not yet confirmed on or off the critical path.
3. Removed-status design. Whether a new "removed" state is needed in the data model is still undecided; Tracks A and B depend on the answer.
4. Owners and dates. The work plan lists actions, but named owners and dates per track are not yet attached.

## Recommended Actions

1. Fold this into the one-page release gate view already requested. It should now cover cancelled cleanup (with the audit-before-delete answer), activation-failure fixes, and the scheduler investigation, each with owner, date, and on/off the Aug 3 path.
2. Require a snapshot or export before the one-time hard delete. One sentence to the team resolves the sequencing conflict cheaply.
3. Pre-position the "data is intact" narrative with Sales Operations. If sales stakeholders hear "data loss" before the fix lands, product credibility takes an avoidable hit. A short factual note (records intact, activation defect identified, fix in progress) is worth drafting once the root cause is confirmed.

## Evidence Note

Findings are drawn from an AI-generated transcript and Loop notes. Speaker attributions are treated as unconfirmed until validated. The "database still contains the records" finding is the team's current working conclusion, not yet a validated result; the UI-only vs. actual-loss investigation remains open.

---

**Executive takeaway:** the team has correctly shifted from building features to stabilizing the data foundation; the leadership priority is making sure the cleanup is sequenced safely, scoped against August 3, and communicated to Sales Operations before "data loss" hardens into the story.
