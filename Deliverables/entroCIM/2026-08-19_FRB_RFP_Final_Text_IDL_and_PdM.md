# FRB Cash Services RFP: Final Text
## Owner Data Access (Section 3.2) and Predictive Maintenance (Section 3.1)

Prepared for Darryl Benson, 2026-08-19. Paste-ready. Bulk export removed per your direction. Output formats confirmed by you: JSON, CSV, SQL, Zinc, Trio.

The only bracketed items remaining are specification paragraph numbers, which need the source document.

---

# 1. Owner Data Access and Ownership

**Placement:** Section 3.2, Independent Data Layer, as a subsection at the end of that section. Suggested heading number 3.2.x, matching whatever numbering 3.2 ends up using.

**Heading:** Owner Data Access and Ownership

---

All data collected, normalized, and stored in the Independent Data Layer is the property of the Owner. Wesco places no ownership claim and no commercial restriction on the Owner's operational data.

The Owner has direct programmatic access to that data through entroCIM's secure REST API. The API exposes the complete data model, tag structure, point and asset metadata, historical time-series data, and platform functions, and is available to Owner-developed applications, Owner analytics tools, and approved third-party systems. Access is authenticated, role-scoped, and encrypted in transit, consistent with the security model described in Section 3.1.

The Owner can enumerate and export the full contents of the data layer at any time, including the asset and equipment hierarchy, the tag and naming structure, point metadata, and historical trend data. Supported output formats are JSON, CSV, SQL, Zinc, and Trio.

At the end of the platform's service life, or at any time at the Owner's direction, the complete data set, model, and history will be provided to the Owner in a documented, non-proprietary format suitable for import into a successor system, together with the accompanying schema and model documentation.

---

**Optional sentence, to add only if Ron Snyder confirms it.** Placement is the end of the third paragraph.

> Owner access to the API and to data export requires no additional or separate licensing.

This is a strong claim and worth making if it is true. It is the one item in this text I could not verify from the project record.

---

# 2. Predictive Maintenance

The earlier draft was unclear on placement because the text I wrote was three paragraphs and the destination is a table cell. Splitting it resolves that, and the split is better than the original for a separate reason: the maturity point applies to five use cases, not just this one, so stating it once below the table is more accurate and shorter than repeating it per row.

Two changes, in two places.

## 2a. Replaces the Predictive Maintenance cell in the Analytics Capabilities table, Section 3.1

**Placement:** the Description cell of the existing Predictive Maintenance row. Keep the row heading exactly as the specification words it, so the compliance mapping is unambiguous.

---

Applies condition-based analytics to identify equipment requiring attention before failure. The platform evaluates runtime accumulation against service intervals, alarm and fault recurrence, and deviation in performance trends such as efficiency, capacity, cycling frequency, and response to control commands. Assets are ranked by condition, and equipment showing degradation is surfaced with a recommended intervention and the supporting operational evidence, so that maintenance can be planned rather than reactive. Specification Section 25 00 00, Rev. 7, paragraph [x.x] defines predictive maintenance in terms of asset condition, runtime, alarm history, and trends.

---

## 2b. New paragraph, immediately following the Analytics Capabilities table, Section 3.1

**Placement:** directly after the table, before the User Administration subsection. This is new content, not a replacement.

**Heading:** Analytics Maturity and Operating History

---

Several of the analytics above become more effective as the facility accumulates operating history. At handover, predictive maintenance, energy performance, comfort optimization, occupancy pattern analysis, and fault detection operate on manufacturer service intervals, design parameters, threshold-based rules, and published benchmarks. As the building establishes its own operating record through the first year of occupancy, asset-specific baselines, seasonal load profiles, and trend-based degradation detection progressively replace those initial references, and detection accuracy improves while nuisance alarms decline.

This is a normal and expected characteristic of building analytics rather than a limitation of the platform. The verification approach in [reference the commissioning subsection] accounts for it by scheduling the demonstration of history-dependent use cases during a defined post-occupancy period, and by providing for a tuning period in which rules, thresholds, and baselines are refined against actual building operation.

---

## Why this structure

Keeping the specification's term in the row heading preserves the line-by-line compliance mapping. Describing the mechanism in the cell using the specification's own four inputs, which the original draft already quoted, means the claim matches the definition being scored against. And moving the maturity statement below the table sets the first-year expectation once, in writing, for every use case it applies to.

The practical value is in delivery rather than evaluation. Without this paragraph, the Owner can reasonably expect failure prediction on a building with no operating history, and the team is asked at substantial completion to demonstrate analytics that need a year of data. With it, that expectation is set in the proposal and carried into the commissioning approach.

---

## Related open item

The commissioning cross-reference in 2b assumes the commissioning subsection from the previous draft is included. If commissioning is not going into this response, replace that sentence with a plain statement that history-dependent analytics are demonstrated during an agreed post-occupancy period. Do not simply delete it, since the maturity paragraph raises a question that the reader then expects answered.
