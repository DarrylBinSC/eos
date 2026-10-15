# AI Part Taxonomy Analysis: Process Brief and Required Data Model

Prepared for the team member writing the internal use case
Date: 2026-08-13
Source basis: Wesco Part Classification program (governing spec, ADM global-attribute mapping per DDPTRK-6346)

## How to use this document

Section 1 describes the classification process we already built and ran, so you do not re-invent it. Section 2 states where your use case is genuinely different and what that changes. Section 3 is the data model your output must conform to. Section 4 is the set of questions your use case needs to answer. Section 5 lists what is not yet locked, so you do not build on a moving target.

The short version of the ask: do not start from "what can AI extract from a part number." Start from the target data model, then work backward to what the taxonomy can actually support.

---

## 1. The process we used, and why each part exists

We ran a source-verified classification program across five supplier sheets, roughly 20,364 unique parts. Over 5,400 parts were classified, three sheets delivered, with a QA record for each. The design principle throughout: accuracy and traceability over completeness. A blank verified answer beats a confident guess.

### 1.1 The seven-phase loop

| Phase | What happens | Owner |
|---|---|---|
| 0 | Set the standard. Category definitions, the software-versus-service rule, sourcing requirements. Written once into a governing spec. | Human |
| 1 | Build a seeded scaffold. De-duplicate the sheet to unique parts, pre-fill any SKU already researched on a prior sheet. | AI |
| 2 | Research. Cluster by brand, one focused lookup per unique SKU, apply the rules. | AI |
| 3 | Merge and verify-save. Results merged into the master, formatted, save proven on disk before the run reports done. | AI |
| 4 | QA review. Independent pass on sourcing discipline, flag consistency, data integrity. Written QA summary. | AI + Human |
| 5 | Decide edge cases. Ambiguous or custom SKUs escalate to the team. AI never guesses. | Human |
| 6 | Close out. Map unique-part results onto every customer row, regenerate the summary, produce the QA deliverable. | AI |

### 1.2 Initial search method

The unit of work is the unique part, not the customer row. We de-duplicate first, research each unique `catalog_no` once in a master lookup, then map results back onto every source row by part number. This is why the second sheet is cheaper than the first: prior answers seed the next sheet. On the Convergint (Chris F.) sheet, 667 of 4,966 parts were pre-answered before any new work started.

Before searching, vendor names are normalized. The raw data gives two fields only, a part number and a vendor string, and the vendor strings are inconsistent: "AXIS COMMUNICATIONS INC..", "AXIS COMM" and "SHANGHAI AXIS COMMUNICATION" are all Axis. Normalization happens up front so brand clustering is clean.

Work is then ordered by brand cluster, reference-backed brands first, the long tail last. This matters more than it sounds: it front-loads the high-yield work and isolates the judgment-heavy remainder, which is where quality actually degrades.

For each part, one focused search, with a strict source hierarchy:

1. Manufacturer product, spec, datasheet or warranty page. Strongly preferred.
2. Official manufacturer datasheet or warranty-policy PDF.
3. Authorized distributor listing (Anixter, Graybar, ADI, CDW). Usable to confirm category and description, not for warranty or term unless it cites the manufacturer's own terms.

Forums, marketplace resellers, AI summaries and generic blogs are excluded.

The hardened sourcing rule is the single most important control: a row may be marked `needs_review = No` only if its `source_url` names the specific SKU. A brand homepage, a search-results URL, or a product-family page is not sufficient. We added this after roughly 119 homepage-only citations accumulated on one sheet and had to be re-sourced. It is cheaper to enforce at intake than to remediate.

Two knowledge assets compound and reduce lookups over time. A brand reference library, now 69 brands, holds canonical name, domain, default category and standard warranty policy. SKU decoders hold per-brand naming patterns (Milestone, Hanwha, Rhombus) that resolve a SKU without a lookup. Your use case is, in substance, a generalization of the SKU decoder concept, so start from what is already there rather than from a blank page.

### 1.3 How categorization worked

Category is a controlled vocabulary, exactly one value per part:

- Hardware. Physical products, including mounts, brackets, enclosures, cables and accessories.
- Software. Anything delivering software functionality or access to a software platform. This includes SaaS, cloud platforms, cloud storage and recording subscriptions, software licenses including those labeled "Service License," and software support or update plans such as Milestone Care Plus.
- Service. Genuine non-software labor or fees only: installation, configuration or programming fees, training, on-site visits, advance replacement and RMA handling.
- Extended Warranty. A SKU whose sole purpose is to extend or upgrade hardware warranty coverage.

Tie-breakers, applied in order:

1. If the deliverable is access to software, a platform or the cloud, it is Software, even when the vendor brands it a service and sells it with a term. This is the most common error, and the team confirmed the rule explicitly.
2. Service only when no software is delivered. A one-time card-format programming fee is Service. Ongoing cloud video storage is Software.
3. A hardware-plus-service bundle is classified by primary purpose, with the bundle described in the description field.
4. Genuine ambiguity is noted and flagged for review, not resolved by preference.

Durations are recorded as a number plus a unit so they sort, and they are placed by meaning rather than by convenience: subscription term for any subscription SKU regardless of category, supplier warranty for the manufacturer default warranty on hardware, and warranty coverage fields reserved exclusively for Extended Warranty SKUs. Confidence is High for an exact SKU on the manufacturer site, Medium for a distributor or family page that clearly covers the SKU, Low for a partial or ambiguous match. Unverifiable fields stay blank, never "N/A" or zero.

### 1.4 QA process

QA is layered, and each layer catches a different failure class.

Automated validation runs after every merge. It checks enum legality on every row (review flag in Yes, No or blank; confidence in High, Medium, Low or blank) and exits non-zero on any anomaly. This is what surfaced ten rows corrupted by commas inside URLs splitting columns during a merge. The merge was hardened to use a real CSV parser with full quoting, and the validator now runs as a standing guard.

Save integrity is treated as a control, not a formality. The working folder is cloud-synced and silently reverted saves twice early in the program, costing real work. Every save is now fingerprinted, snapshotted, re-read after a sync delay and compared, with automatic restore from snapshot on a detected revert. No step is reported complete until the save is proven on disk.

An independent QA pass follows each step and produces a one-page QA summary with an explicit verdict of PASS, PASS WITH FOLLOW-UPS, or FAIL. It carries a check-and-result table, counts by category, confidence and review status, mapping and join integrity, sourcing and vocabulary conformance, issues requiring human confirmation, reference-library updates, and overall program progress. Follow-ups are tracked, not merely noted. The ESSCOE sheet passed with follow-ups, and those follow-ups became real work.

Human review is bundled and tracked rather than ad hoc. Rows flagged for review are packaged into review packets with an assignee, sent date, due date and per-item decision of accept, fix, quarantine or leave. Every change is audited old to new. Returned decisions flow back into the master and, where the decision is general rather than SKU-specific, into the reference library, so the same question is not asked twice.

Two structural points worth carrying into your use case. First, every row carries the version of the spec it was classified under, plus a classification date, so when a rule tightens we can find and re-validate everything classified under the old rule. Second, a fixed regression set of known parts with known answers is re-run after any rule or code change.

---

## 2. Where your use case is different, and what that changes

The program above resolves attributes by researching an external authoritative source. Your use case proposes resolving attributes by parsing the internal part naming taxonomy. That is a different evidence class, and the difference is the most important thing to get right in the write-up.

A SKU-naming manufacturer page is evidence. A pattern inferred from a naming convention is a rule-based inference. It may be highly reliable, and for structured vendors it often is, but it is not the same fact type, and if the two are merged into one undifferentiated dataset the traceability that makes the current output safe to put in front of customers is lost.

The practical consequence: your output schema needs an evidence-type field alongside the existing source and confidence fields, with at least these values.

| evidence_type | Meaning | Typical confidence ceiling |
|---|---|---|
| `sku_source` | A source page naming the exact SKU | High |
| `decoder_rule` | A validated brand SKU-decoder pattern | Medium to High, if the decoder is validated |
| `taxonomy_inference` | Derived from internal taxonomy or description text | Medium at best, review by default until sampled and proven |
| `vendor_policy_default` | A brand-level default, such as the Axis five-year warranty | Medium, and only where the brand policy is documented |

Do not let a taxonomy inference set `needs_review = No` until the pattern has a measured accuracy rate against a validation sample. That is the direct analogue of the hardened sourcing rule, and skipping it would reintroduce the exact problem we already paid to fix.

Second point to make explicit. Taxonomy parsing is a coverage accelerator, not a replacement for research. It should reduce the number of parts needing a lookup and pre-fill fields for the researcher to confirm. Framing it as a replacement will overstate what it can do and will not survive review.

---

## 3. The data model your output must conform to

The end purpose is to sync findings into Asset Data Manager, consuming new global attributes on Anixter P360 and DDP P360 per Jira DDPTRK-6346. The key design shift in that ticket: warranty and software or licensing attributes are global rather than taxonomy-specific, so any part can carry them. Hardware with preloaded software carries both warranty and software attributes. Your model must therefore decouple these fields from category. Do not nest license fields under a Software branch.

### 3.1 ADM global attributes, and how our current fields map

| ADM global attribute | Controlled values | Our current field | Gap to close |
|---|---|---|---|
| Warranty Duration | 1, 2, 3, 5, 10 Years; 18 Months; Lifetime | `supplier_warranty_value` / `_unit`, `warranty_or_service_coverage_value` / `_unit` | Normalize free number-plus-unit to a fixed enum. Off-enum values such as 4 years or 90 days get flagged, not coerced |
| Supplier Warranty Effective | Date of Manufacture, Installation, Factory Shipment, Sale or Invoice, End-Customer Delivery | Not captured | New field. Blank plus review by default, researched where determinable |
| License Duration | 1 Month, 6 Months, 1, 2, 3, 5, 7, 10 Years, Perpetual | `subscription_term_value` / `_unit`, plus Perpetual derived from `purchasing_type` | Normalize to enum, add the Perpetual case, flag off-enum |
| Delivery Format | Physical Media, Electronic Download, License Key, Cloud or SaaS Access, Embedded or Preloaded, Email Delivery, Supplier Portal, Certificate or Entitlement. List pending final sign-off | Not captured | New field, enum not final |
| Software Type | Application, System, Firmware, Embedded, SaaS or Cloud, License or Entitlement, SW Maintenance or Support, SW Subscription, Security, Configuration or Programming. Pending final sign-off | `category = Software` only, which is coarse | New software subtype, enum not final |
| License Model | Perpetual, Subscription, Term License, Usage-Based, Seat-Based, Device-Based, Site License, Enterprise License, Concurrent User. TBD | `purchasing_type`, only Perpetual, Subscription or N/A | Expand purchasing type into License Model, remap existing values, flag what does not map |

The ADM model separates concepts our current schema blurs, specifically warranty duration versus license duration, and a three-value purchasing type versus a nine-value License Model. It also adds three attributes we do not capture at all.

### 3.2 A correction on start dates

Warranty and license start dates are not part-master attributes. A part number does not have a warranty start date. An instance of that part, sold on an order and installed at a customer, does.

What the part master can carry is the rule: the Supplier Warranty Effective trigger, meaning whether the clock starts at manufacture, shipment, invoice, installation or customer delivery. The actual start date is computed downstream from the transaction or asset record, using that trigger plus the order, shipment or install date.

If your use case commits to extracting start dates from the taxonomy, it is wrong at the model level and will fail review. State the boundary explicitly: this pipeline delivers duration and the effective-date trigger. Entitlement and asset records deliver the dates. This is the same boundary that separates the part master from the entitlement model in the broader WAM data architecture, so it is worth getting right in writing.

### 3.3 Required provenance fields on every row

These are not optional, and they are the reason the current output is trustworthy.

| Field | Purpose |
|---|---|
| `evidence_type` | Which class of evidence produced the value, per section 2 |
| `source_url` or `rule_id` | The specific source page, or the identifier of the decoder or taxonomy rule applied |
| `confidence` | High, Medium, Low |
| `needs_review` | Yes or No, with the hardened rule enforced |
| `spec_version` | Which version of the rules produced this row, so a rule change can be re-validated |
| `classified_date` | When the value was last set or changed |
| `notes` | Ambiguity, conflict, or why a field is blank |

Blank means unknown. Do not write "N/A," "unknown" or zero in place of a real value.

---

## 4. Questions your use case needs to answer

Answer these in the document itself. They are the questions the work will be reviewed against.

1. What is the exact input? Which fields of the naming taxonomy are available, on how many parts, and how complete and consistent are they? Give real counts, not estimates.
2. Which target attributes do you claim taxonomy parsing can populate, and at what expected accuracy? Map each claim to the ADM attribute table in section 3.1. Any attribute not in that table needs a justification for why we would capture it.
3. How do you measure that accuracy? Define the validation sample, the sample size, and the pass threshold at which a pattern is allowed to set `needs_review = No`.
4. How does a taxonomy-derived value interact with a conflicting research-derived value? Which wins, and who decides?
5. What is your controlled vocabulary handling? Specifically, what happens to a value that does not map to an ADM enum. The required answer is flag for review, never coerce to the nearest enum.
6. How do you handle the global-attribute design? Show that hardware with preloaded software can carry both warranty and software attributes in your model.
7. What is the QA gate? Which automated checks run, what triggers a human review packet, and what does the QA verdict look like.
8. What is the reuse and compounding mechanism? How does a validated pattern get promoted into the shared decoder or reference library, and who approves that promotion.
9. What does it not do? Name the boundary explicitly, including the start-date boundary in section 3.2 and the parts the taxonomy cannot resolve.
10. What is the interface to the existing program? This is not a greenfield build. State what it reads from and writes to, and what happens to the roughly 5,600 parts already classified.

---

## 5. Dependencies and open items

These are not settled, and the use case should treat them as dependencies rather than assumptions.

- Final sign-off on the Delivery Format, Software Type and License Model value lists. Two are marked pending in the ADM ticket. Building against an unsigned enum means rework.
- The Wesco data-lake restructuring, which is in progress and creates room for these attributes.
- The ADM consumption and field-mapping spec.
- The sync mechanism itself, meaning how a delivered batch reaches ADM and P360, whether by API, export or staging table. This is not decided.
- Jira reference: DDPTRK-6346.

---

## Assumptions and what to verify

Stated so they are not read as fact:

- The ADM attribute list and controlled values above are taken from the DDPTRK-6346 mapping as captured on 2026-07-06. Confirm nothing has changed before the use case is finalized, particularly the three enums marked pending.
- The existing classified volume is stated as over 5,400 parts as of 2026-06-30 and the reference library at 69 brands as of the 2026-07-06 roadmap. Both grow. Pull current figures from the tool rather than quoting these.
- Whether the taxonomy his use case refers to is the internal Wesco product taxonomy, the manufacturer SKU naming conventions, or both, is not stated in the request. The distinction changes the approach materially and should be resolved in the first paragraph of his document.
