# WAM - Product Backlog Refinement: Problems Identified and Work Plan

**Meeting:** WAM - Product Backlog Refinement  
**Date:** 2026-07-20  
**Purpose:** Verbose dump of problems identified and the work plan discussed to fix them.  
**Primary sources:** Meeting transcript, Loop notes, and related Teams meeting artifacts from the WAM - Product Backlog Refinement meeting.

---

## Executive Summary

The dominant theme of the meeting was not new feature development. It was operational hardening of WAM/ADM, specifically:

1. Eliminating cancelled-order contamination in ADM.
2. Resolving perceived data loss and missing record issues.
3. Fixing license activation failures.
4. Improving filter and UI scalability for large datasets.
5. Addressing duplicate-record creation.
6. Cleaning up historical data and database growth.
7. Standardizing data quality problems, especially end-user matching.
8. Adding visibility mechanisms so records that are removed are still auditable.

---

## Problem Area 1: Cancelled Orders Polluting ADM

### Problem

The team identified that cancelled line items remain in ADM and can drive incorrect behavior:

- Notifications can be sent for cancelled items.
- Cancelled records can appear in license summaries.
- Cancelled records can affect analytics.
- Cancelled records can appear in exports.
- Cancelled records complicate renewal calculations and reporting.

Akansh described this as a prerequisite cleanup item before notification functionality can be trusted. The team explicitly stated that sales reps should not receive notifications for cancelled items.

### Root Cause

The system currently does not fully separate:

- Active line items
- Cancelled line items
- Removed line items

The existing workflows do not consistently mark and isolate cancelled records.

### Work Plan

#### Immediate Fix

One-time hard delete of cancelled records throughout ADM.

Actions:

- Validate cleanup query.
- Run query across ADM.
- Remove all cancelled items.
- Complete prior to notification release activities.

#### Long-Term Solution

Split the solution into separate implementation tracks.

##### Track A: Data Layer

- Add removed/cancelled state.
- Update DDP ingestion logic.
- Mark records as cancelled or removed.
- Maintain status history.

##### Track B: UI Layer

Hide removed/cancelled items from:

- License Summary
- Analytics
- Filters
- Searches
- Exports

These records should effectively disappear from normal workflows.

##### Track C: Audit Visibility

Create a dedicated **Removed/Cancelled Orders** tab containing:

- Search
- Grid
- Analytics
- Export

Include metadata such as:

- removed date
- part number
- PO/SO
- license key
- status
- supplier
- custom fields

The intent is for data to be removed from regular operational workflows without losing traceability.

---

## Problem Area 2: Missing Data / Reported Data Loss

### Problem

Users are reporting data loss.

Several discussions focused on:

- Missing records
- Differences between files and UDM/EUDM
- Activation visibility issues
- Bug 7827
- Production vs MDB discrepancies

The team debated whether data is actually disappearing or simply not surfacing correctly.

### Key Finding

Akansh stated that recent investigation suggests the database still contains the records.

The issue appears to be:

> Data exists but is not surfacing as activated and therefore appears missing to users.

The meeting explicitly lists the open question:

> Investigate if data loss is UI-only or actual DB loss.

### Work Plan

#### Investigation Work

- Compare Amar's file against UDM.
- Compare DEV vs EUDM.
- Analyze missing records.
- Determine root cause of visibility gaps.
- Review Bug 7827 findings.

#### Assigned Actions

- Analyze discrepancies between Amar's file and UDM.
- Investigate EUDM vs DEV record differences.
- Determine whether scheduler is failing to pick up records.

---

## Problem Area 3: License Activation Failures

### Problem

A significant activation reliability issue was discussed.

Three failure modes were identified:

1. Query does not return expected records.
2. Row update/deletion issues.
3. Null license start dates.

The null start-date scenario was repeatedly identified as a major contributor.

Records remain in:

- Pending Activation

instead of transitioning to:

- Activated

This creates the appearance of missing data.

### Root Cause

Krishnanunni explained:

- Records with null license start dates never activate.
- Missing SO dates prevent activation.
- Pending activation records accumulate because activation logic cannot complete.

### Work Plan

#### Immediate

Analyze all three activation-failure categories:

- Query failures
- Upgrade/deletion failures
- Missing start dates

#### Code Changes

- Update SO start date handling.
- Modify DDP code.
- Update activation logic.
- Fix record transition behavior.

#### Tracking

Document pending activation defects in dedicated bug stories rather than mixing them with API enhancement work.

---

## Problem Area 4: Duplicate Record Creation

### Problem

Duplicate records are being created in lower environments.

Examples discussed:

- Duplicate end-customer records.
- Duplicate master integrator/vendor combinations.
- Duplicate records generated within a single DDP execution.

### Root Cause

Krishnanunni stated that investigation identified:

- Duplicate master integrator name/vendor combinations creating duplicates.
- Existing job logic allowing duplicate creation.

### Work Plan

- Create bug report.
- Analyze duplicate-generation path.
- Confirm whether issue still exists.
- Implement code fix.
- Validate in lower environments.

---

## Problem Area 5: Filter Performance and Scalability

### Problem

Current filter architecture does not scale.

Discussion referenced datasets:

- Tens of thousands of records
- Up to approximately 50,000 records

Issues include:

- Long load times
- Dropdown latency
- API bottlenecks
- Page blocking
- Potential production failures

### Root Cause

Current approach attempts to load excessive data into filter controls.

This creates:

- slow APIs
- slow dropdown rendering
- user experience degradation

### Work Plan

#### Backend

Implement:

- server-side pagination
- incremental retrieval
- smaller batches, such as 100 to 1,000 records

#### Frontend

Support:

- infinite scrolling
- type-ahead search
- partial loading

#### Reliability Enhancement

Load filters independently so:

- failure of one filter
- does not break the entire page load

#### Architecture Review

Team will evaluate:

- parallel loading strategy
- API optimization approach
- architectural changes before implementation

---

## Problem Area 6: ADM Database Growth

### Problem

Large volumes of inactive data may be degrading performance.

The notes identify concern about:

- obsolete records
- inactive records
- database clogging
- filter degradation

### Work Plan

Create an archival strategy:

- identify inactive data
- move or archive old records
- reduce operational dataset size
- improve filter performance and overall system responsiveness

---

## Problem Area 7: End User Data Quality

### Problem

End-user matching is inconsistent because values differ by case and formatting.

Example:

- User A
- USER A
- user a

may be treated differently.

### Work Plan

- Make matching case-insensitive.
- Normalize data.
- Convert historical records to uppercase.
- Update DEV and UI logic.
- Run corrective script against existing records.

---

## Leadership Takeaways

From a leadership perspective, the meeting exposed four systemic concerns:

| Priority | Concern |
|---|---|
| Critical | License activation defects causing apparent data loss |
| Critical | Cancelled-item contamination affecting notifications, analytics, and reporting |
| High | Data integrity issues, including duplicates, missing records, and scheduler pickup failures |
| High | Scalability limitations in filters and APIs as data volume grows |

The team's overall remediation strategy is:

1. Clean the existing data.
2. Fix activation and visibility defects.
3. Improve data integrity controls.
4. Separate operational records from cancelled records.
5. Redesign filter architecture for scale.
6. Archive inactive data.
7. Standardize user-entered data.

These themes align closely with the broader WAM/DDP/EUDM discussions around foundational data quality and operational reliability. The backlog refinement session was effectively a data-quality stabilization review wrapped in sprint planning.

---

## Source References

- `turn1search28`: WAM - Product Backlog Refinement meeting event and transcript excerpt.
- `turn1search30`: WAM - Product Backlog Refinement 2026-07-20 Loop notes.
- `turn1search32`: WAM - Product Backlog Refinement meeting recording/transcript artifact.
