# FRB Cash Services RFP Response, Section 3.1 Smart Building Platform
## Review and Recommended Changes

Reviewer: Claude, for Darryl Benson
Date: 2026-08-19
Scope: Section 3.1 text and the two accompanying graphics. Sections 3.2 (IDL) and 3.3 (UUI) to follow.
Basis: the submitted draft text, plus the entroCIM project record in the Executive Operating System (`Products/entroCIM/entroCIM.md`, `entroCIM_Architecture_Slide_Prompt_2026-07-29.md`, `entroCIM_Roadmap.md`, `entroCIM_Dell_Support_Process_Diagrams.md`). The FRB source documents (Basis of Design, Spec Section 25 00 00 Rev. 7) were not available to me, so citation accuracy is not verified.

---

## Recommendation

Do not release 3.1 in its current form. The technical position is sound and the architecture is defensible, but the draft is a working document rather than a submission. Four issues will cost score or credibility regardless of how good the underlying solution is:

1. Internal drafting instructions are still in the body text.
2. The point-count sizing basis (25,000) is not reconciled to the asset table (1,647), so the number looks arbitrary or self-serving.
3. Three of the nine required use cases named in the opening paragraph are not addressed in the analytics table.
4. The section sells platform capability and is silent on who operates and tunes it after handover, which under-answers the RFP and leaves the services revenue unstated.

Items 1 through 3 are editorial and can be closed in one pass. Item 4 is a scope and commercial decision, not an editor's.

---

## Priority 1: Fix before this section goes anywhere

### 1.1 Internal instructions to the proposal team are in the submitted text

Four passages are written to the proposal writer, not to the Owner:

- "For this response, entroCIM is positioned as an Owner-hosted on-premises deployment..."
- "Although the proposed response should lead with an on-premises deployment, the architecture can support..."
- "The 25,000+ point capacity should be presented as a conservative, future-ready sizing basis that supports:"
- "The following high-level architecture illustration explains the connectivity architecture for discussion."

An evaluator reads these as evidence the response was assembled hastily and not reviewed. The last one is the worst, because it tells the Owner the diagram is for internal discussion rather than a commitment. All four need to be rewritten as direct statements of what is being proposed.

### 1.2 The asset table does not support the 25,000-point claim

The table totals correctly (1,647; I verified the arithmetic). The problem is that the section states a 25,000-point Day 1 capacity immediately above a table of 1,647 assets and never connects the two. An evaluator will reach one of two conclusions, both bad: the sizing is arbitrary, or the point count is inflated to justify licensing.

Fix by stating the conversion explicitly. Either add a points-per-asset column by system type, or add a basis sentence such as: the 1,647 assets identified from the current drawing set translate to approximately N integrated points at an average of X points per asset, and the platform is licensed for 25,000 points to absorb final vendor object exports and future scope.

Two related defects in the same block:

- "25,000" and "25,000+" are both used. Choose 25,000 and treat it as a licensed capacity commitment. The "+" is unbounded and unpriced, and it will be read as a commitment you did not intend to make.
- Two rows (IAQ Platform 100, Occupancy Analytics 200) carry weaker validation language than the other nine: "Architecture/HVAC references exist" rather than "Validated in architecture and detailed drawings." Those two rows are 300 assets, 18% of the total. If those systems are not confirmed scope, the asset basis moves materially. Either confirm them or footnote them as an assumption. Do not leave two grades of confidence in one column without saying so.
- The last bullet list repeats itself: "Future multi-site rollout" and "Multi-Site Management" are the same item.

### 1.3 Three required use cases are named but not answered

The opening paragraph commits to nine Owner-approved use cases. The analytics table covers six. Missing: Comfort Optimization, Smart Restroom Management, and Work Order Management integration. If the evaluation scores against the schedule of use cases line by line, you lose three items you can actually deliver. Add three rows.

Also change "including Fault Detection and Diagnostics, ..." to "the following Owner-approved use cases:". "Including" signals a partial list, which invites the question of what else is required and unaddressed.

### 1.4 Capability commitments are written as options

The section uses "can be deployed," "can support," "can be organized," and "may be used" for things that are being sold, mixed with "will support" for the same class of statement. In a compliance-scored response, "can" reads as capability in principle and "will" reads as committed scope. Reserve "can" for genuine Owner options (hybrid connectivity, future cloud services) and use "will" everywhere the item is in the proposed scope.

---

## Priority 2: Compliance and scoring gaps

### 2.1 Security and identity content asserts the requirement instead of the capability

The User Administration paragraph states what Division 25 requires, then says the approach "aligns with the specification requirement." It never states what entroCIM actually provides. For this buyer that is a wasted paragraph. State the capability directly:

- SAML 2.0 SSO federated to the Bank's identity provider (this is in active use today per the internal record, so it is a supportable claim, not a roadmap item)
- MFA enforced at the Bank's IdP
- Least-privilege role model with the role table you already have
- Audit logging with a stated retention period
- Encryption in transit and at rest, with named standards
- No default credentials on any networked or connected device, per the Division 25 clause you already cite

**Heading to use in the response.** "User Administration" is now too narrow for what the content covers. Retitle it **3.1.6 Security, Identity, and User Administration**, with the role table kept under it. That heading matches the Division 25 language (role-based access control, authentication, encryption, audit logging) and makes the compliance mapping obvious to an evaluator scoring line by line.

Two qualifiers. If the response already carries a dedicated security or cybersecurity section elsewhere, keep this one as **3.1.6 User Administration and Access Control**, cover only the platform-level role model and SSO here, and cross-reference the security section for encryption, logging, and credential policy rather than restating them; duplicated security claims that drift apart are worse than a single cross-reference. And if the response does not use numbered subheads, the same titles work without the number, but see the line-level corrections table on converting the colon-terminated pseudo-headings throughout the section.

### 2.2 Content the Owner needs and the section does not provide

You are asking the Bank to host the platform on their infrastructure. They cannot cost that from this section. Missing:

- Compute, memory, and storage requirements for the VMs the Owner must provide, at 25,000 points
- Data retention period and storage growth rate
- High availability, failover, and backup/restore responsibility split
- Patch and upgrade responsibility on Owner-managed infrastructure, and the release cadence the Owner should plan for
- Licensing model and what happens commercially if the point count grows past 25,000
- Performance expectations (dashboard response, trend query, alarm latency)

Some of this may live in another section. If so, cross-reference it. If it lives nowhere, it is a gap.

### 2.3 Specification citations are in filename form

"25-00-00-Integrated-Automation-General-Requirements_Rev_7.pdf lists these use cases" should read "Specification Section 25 00 00, Integrated Automation General Requirements, Rev. 7, paragraph [x.x]." Filenames in body text look like working notes. The same applies to the Basis of Design references, which should carry a section or page number so the evaluator can verify the claim without hunting.

### 2.4 Section boundaries

Section 3.1 currently carries the full five-layer architecture graphic, the asset and point-count table, and language about normalization and the data model. Layers 2 and 4 belong to 3.2 and 3.3. Recommend moving the layered architecture graphic and the point-count table into a short architecture overview that precedes 3.1, so each of 3.1, 3.2, and 3.3 describes one layer and the shared sizing basis is stated once. Otherwise 3.2 will repeat it and the two versions will drift.

### 2.5 The section is silent on who operates the platform after handover

This is the largest content gap in 3.1. The section commits to nine use cases, and every one of them requires ongoing work to stay useful. FDD rules need writing and tuning against this building. Predictive maintenance thresholds need calibration once runtime history exists. IAQ scoring, occupancy baselines, and energy benchmarks all drift. The response describes the capability and says nothing about who does that work, for how long, or under what arrangement.

Two consequences. An evaluator reads a platform proposal where they expected a platform and service proposal, and scores the use cases as capability rather than outcome. And the commercial opportunity goes unstated in the document that sets the Owner's expectations.

Recommend adding a short subsection covering: configuration and rule development during implementation, the tuning period after occupancy, the boundary between Owner-performed and Wesco-performed administration, and how ongoing optimization is arranged if the Owner wants it. Keep it factual and do not oversell a managed service whose operating ownership is still an open internal decision.

### 2.6 The analytics table describes inputs, not outputs

Every row in the analytics table describes what the platform collects or aggregates. Almost none states what the Owner receives or what decision it drives. "Aggregates EPMS, submeters, equipment status, schedules, occupancy, setpoints, and operating trends to identify consumption patterns and optimization opportunities" tells the evaluator what goes in, not what comes out.

Add a column, or a second sentence per row, stating the delivered artifact (dashboard, alarm, prioritized fault list, report, work order trigger) and the operational outcome. This is a low-effort, high-return change: the same six use cases score better because the Owner can see what they get on day one.

### 2.7 "Predictive Maintenance" is the most challengeable claim in the section

What the row actually describes is condition and rule-based prioritization using runtime, alarm history, fault recurrence, and performance trends. That is legitimate, valuable, and deliverable. It is not predictive maintenance in the failure-model sense, and a technical evaluator may say so.

If the specification uses the term "predictive maintenance," use the specification's term in the heading so the compliance mapping holds, and describe the mechanism honestly in the body. That protects the response at evaluation and protects delivery from an expectation you did not intend to set.

### 2.8 No commissioning or acceptance approach

The section claims support for nine use cases and proposes no means of proving any of them. Division 25 responses are normally expected to address point-to-point verification, functional demonstration of each use case, acceptance criteria, and the warranty or correction period. Stating an acceptance approach converts nine capability claims into nine verifiable deliverables, which is what an evaluator is trying to assess. If this lives in another section of the response, cross-reference it here.

---

## Priority 3: Consistency with the internal record

These are items I can see from the entroCIM project record that a proposal reviewer without that context would miss. Each is a judgment call for you, not an edit.

### 3.1 The underlying platform, and what "independent" actually has to answer

**Corrected 2026-08-19 by Darryl.** An earlier version of this review treated the SkySpark dependency as being in tension with the "Independent Data Layer" label. That was wrong. IDL is an industry term of art, not a proprietary claim: a data layer that is independent of any single source system, extensible, accessible to the Owner, and serving as the central point of data integration. IDLs are routinely built on SQL, graph, or time-series platforms. A commercially licensed data-and-analytics platform underneath one is normal, not a contradiction, and disclosure of every OEM component is not expected in this section.

What survives is narrower and more useful. Of the three tests in the industry definition, the third one, accessible to the Owner, is where an evaluator can press. The questions worth pre-answering in 3.2 are:

- Can the Owner query the normalized data store directly, and against a documented schema?
- Does direct Owner access require a separate third-party license?
- Can the Owner export the full normalized model, tag structure, and history in a usable, documented format?
- What happens to the Owner's data and model if the platform is replaced at end of term?

These are data-ownership and exit questions, not disclosure questions. Answering them affirmatively in 3.2 is what makes the word "independent" defensible. Silence on them is what makes it challengeable.

Section 3.1 needs no change on this point beyond not contradicting whatever 3.2 says.

### 3.2 The support connectivity in the second graphic contradicts the on-premises narrative

The text states that cloud services are not required for core on-premises operation. The second graphic shows an entroCIM Support Services cloud with a link into all three sites. A security reviewer will see a vendor remote-access path that the text does not explain.

Per the internal record, on-premises deployments are supported through Arcbeam, with a customer-supplied VPN as an alternative support path. Airwall applies only to Wesco-hosted cloud instances, so the diagram must not imply Airwall on-premises.

Recommendation: name the support path in the text, state that it is outbound-initiated and brokered through the FRB secure edge device with no inbound path, and present the customer-supplied VPN alternative so the Bank can choose. Getting ahead of this converts a security objection into a design decision the Bank owns.

Separately: the support intake and handoff process (how a Bank user reports an issue, who triages, when it reaches Wesco support, who owns it while the source is undetermined) is the exact set of items that is still unresolved on the Dell engagement. If the RFP asks for a support model, do not describe it as settled.

### 3.3 Containerization direction versus the hypervisor commitment

The response commits to installing on the Owner's hypervisor per Division 25. The internal record (2026-08-12) states containerization is the mandatory future deployment model and the exclusive direction, with automated build and deployment testing underway.

These are not necessarily in conflict, since containers can run on Owner-managed hosts. But the response should not lock a VM-image deployment model that the product is moving away from during a multi-year project. Recommendation: commit to running on Owner-managed infrastructure under Owner governance and Owner-controlled patching, without freezing the packaging method, and confirm with Ron Snyder that a containerized deployment satisfies the Division 25 hypervisor clause as written.

### 3.4 The FRB New York reference and the multi-district claim

Two problems with "FRB, NJ Cash Services facility later connect with the FRB NY site which has the entroCIM instance already":

- Customer reference. Naming another Federal Reserve district's installation in a competitive response usually needs consent. Confirm with Nathan Kehr before it goes out.
- The claim itself. Districts are separate entities with separate IT and security governance. A future connection between them is a governance decision, not a platform feature, and asserting it may read as presumptuous. The defensible claim is the one you actually want to make: the same data model, naming convention, dashboard structure, analytics logic, and user administration model can be applied consistently across districts. Say that instead.

### 3.5 Work order integration boundary

Graphic 1 shows Work Order Integration in Layer 3 (Wesco provided) and IBM TRIRIGA / CMMS in Layer 5 (customer provided). The text does not state the boundary. Make it explicit: entroCIM provides the integration and API; the Owner provides and licenses TRIRIGA. Also confirm with David Blondel or Ron Snyder whether the TRIRIGA work-order path is a productized connector or project-configured integration, and word it accordingly. Do not imply a shipping connector if the work is configuration.

---

## Line-level corrections

| Current | Issue | Recommended |
|---|---|---|
| "The proposed SBP Conceptual architecture follows a layered on-premises model that fits and facilitates the data from the Operational Technology systems to drive the actions and close the loop at Enterprise Business Systems." | Ungrammatical and unclear | "The proposed SBP architecture follows a layered on-premises model. Data from the operational technology systems is normalized in the data layer, analyzed and acted on in the platform layer, and returned to the Owner's enterprise business systems to close the loop." |
| "This allows FRB, NJ Cash Services facility later connect with the FRB NY site which has the entroCIM instance already and expand the same data model, dashboard structure, analytics logic, naming convention, and user administration model to additional sites." | Ungrammatical; makes a governance claim as a technical one | "This allows the same data model, dashboard structure, analytics logic, naming convention, and user administration model to be extended to additional Federal Reserve sites as the Owner directs." |
| "all cloud communication shall be brokered within the Bank's local client broker or a local broker with controlled vendor access" | Redundant and unclear as written | Quote the Basis of Design language exactly, or paraphrase once. |
| "Calculate the IAQ score across the room and the building compared against the Office Space Benchmark." | Imperative fragment; "Office Space Benchmark" is capitalized as a defined standard with no source | Name the standard being used (for example ASHRAE 62.1, RESET, or WELL) or remove the sentence. As written it will draw a question you cannot answer. |
| "ICUGN" | Not defined on first use | Spell out on first use. |
| "Total Assets 1647" | Formatting | 1,647. Also label the column consistently ("Estimated Assets"). |
| "Platform Architecture:", "On-Premises Deployment Approach:", etc. | Colon-terminated pseudo-headings | Use numbered subheads (3.1.1, 3.1.2) matching the rest of the response. |
| "BIM / Digital Twin ... 0" | A zero in an asset table invites a question | Footnote it: BIM is the source of the asset model, not a point source. |

---

## Graphics

**Graphic 1 (five-layer architecture).** Strong, and it does most of the work of the section. Two corrections:

- The legend assigns Layers 1 and 5 to the customer. Layer 1 includes the Smart Building and IoT Devices band (occupancy analytics, IAQ, smart restroom, environmental, energy IoT). If Wesco is furnishing any of those sensors, the legend contradicts the scope. This is the same open question as the two weakly-validated rows in the asset table; resolve both together.
- "Future IoT Devices & Smart Systems" and "Additional OT / IoT Devices" read as placeholders. Either name representative device classes or remove the boxes.

**Graphic 2 (multi-site clustered on-premises).** Not usable as shown. It is illegible at page scale, the sites are labeled generically (Site 1, 2, 3) rather than for this project, there is no caption or legend, and it introduces the vendor support cloud without explanation. It currently raises more questions than it answers, and the one question it raises loudest is a security question.

Recommendation: redraw at one-page legible scale with FRB-specific labels, a legend, an explicit security boundary, and a callout for the support path per item 3.2 above. If a redraw is not feasible in the schedule, cut it from 3.1 and put the connectivity detail in the security section as text. A single-site diagram would also serve better here, since multi-site is a future condition and 3.1 is describing what is being delivered.

---

## Verification items and owners

| Item | Why it matters | Owner |
|---|---|---|
| 25,000-point sizing basis and licensing implication | Stated in the response, becomes a commercial commitment | Ron Snyder (technical), Tom Boss (commercial) |
| Points-per-asset conversion from the 1,647 asset table | Closes the credibility gap in 1.2 | Ron Snyder / MSI engineering lead |
| IAQ and occupancy sensor scope: furnish or integrate | Affects 18% of the asset basis and the graphic legend | Proposal lead / estimating |
| Owner data access, export, and end-of-term rights | Makes "independent" defensible in 3.2 | Ron Snyder |
| Whether the spec or Basis of Design requires FIPS 140-2/140-3 validated cryptographic modules | entroCIM is not FIPS validated. Existing FRB deployment is good evidence it is not binding, but a written spec requirement would override that and force a clarification or exception response | Proposal coordinator (document search), then Darryl |
| Who performs analytics configuration and ongoing tuning, and under what arrangement | Closes the largest content gap, item 2.5 | Darryl, with Nathan Kehr on the commercial side |
| Containerized deployment vs the Division 25 hypervisor clause | Avoids committing to a packaging model the product is leaving | Ron Snyder |
| TRIRIGA work order integration: productized or configured | Avoids implying a connector that does not ship | David Blondel / Ron Snyder |
| FRB New York reference consent and the multi-district claim | Customer reference permission and claim accuracy | Nathan Kehr |
| Support connectivity path acceptability to FRB security | Reconciles the text with graphic 2 | Ron Snyder with Bank IT |
| Specification paragraph citations | Verifiability of every compliance claim | Proposal coordinator |

---

## Carry into 3.2 and 3.3

- 3.2 should answer the Owner-access and end-of-term questions in item 3.1 directly. That is what makes "independent" hold up, and it is the part of the industry definition an evaluator can actually test.
- 3.2 should also state the semantic model and tagging convention, since every analytics claim in 3.1 depends on it.
- Move the point-count and asset table out of 3.1 into a shared architecture overview so 3.2 does not restate it differently.
- Watch for the same modal-verb problem ("can" versus "will") in 3.2 and 3.3.
- 3.3 should carry the identity and access detail (SSO, MFA, session management, role definitions) so 3.1 can reference it rather than duplicate it. Decide now which section owns it.
