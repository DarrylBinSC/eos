# FRB Cash Services RFP Response, Section 4.1 High-Level Architecture
## Review and Recommended Changes

Reviewer: Claude, for Darryl Benson
Date: 2026-08-19
Scope: Section 4.1 text, the two tables, and the referenced network architecture illustration.
Basis: the submitted draft, the Section 3.1 draft reviewed earlier today, and the entroCIM project record in the Executive Operating System.

---

## Recommendation

The technical content here is stronger than 3.1. The network segmentation table is a genuinely good artifact, the direction-of-communication column is the kind of detail a security reviewer wants and rarely gets, and "no inbound internet exposure is required" is the single strongest security sentence in either section.

Three things must change before this leaves the building.

1. **The illustration contradicts the text on the same page.** The narrative states that no inbound internet exposure is required and that remote access is FRB-controlled. The diagram shows a Wesco-operated service delivery platform reaching across the internet, through the local firewall, into the entroCIM host. A security reviewer will see this immediately, and the contradiction is more damaging than either position would be on its own.
2. **Remove the subnet CIDRs from the network segmentation table.**
3. **Resolve the layer model.** The response currently describes three, four, and five layers in three different places.

---

## Priority 1

### 1.1 The illustration and the narrative describe two different architectures

This is the most serious finding in the section, and it is on a single page.

**The narrative says:** "Secure remote access for administration and support is provided and controlled by the FRB, using its existing enterprise remote-access solution (e.g., VPN + bastion). No inbound internet exposure is required for entroCIM." It also says user access to the web UI comes from the FRB's enterprise network, and that external connectivity is restricted to Owner-managed channels only.

**The illustration shows:** a region titled "Wesco's entroCIM On-Premise Service Delivery Platform" containing an entroCIM Deployment Support host and a service delivery server, connected across the internet cloud, through the customer's local firewall and switch, to the Local entroCIM host inside the customer network. That is a vendor-operated remote access path traversing the internet into the protected environment. It is the opposite of what the paragraph asserts.

Two further problems in the same diagram:

- **The enterprise applications and user access are drawn outside the customer network.** The entroCIM web/remote client, the browser user, and the enterprise applications block including IBM TRIRIGA all sit on the internet side of the cloud. As drawn, this says FRB operators and TRIRIGA reach entroCIM from outside the Bank's boundary over the internet, which contradicts the narrative and is almost certainly not what is intended.
- **No bastion, jump host, or DMZ appears anywhere in the diagram**, although the narrative makes bastion access central to the security position.

**What is actually going on here.** Per the project record, the normal support path for on-premises entroCIM is Arcbeam, providing services and support enablement, with customer-supplied VPN as the alternative. The diagram is the standard Wesco on-premises service delivery architecture, drawn as entroCIM genuinely supports on-premises customers today. The paragraph is the FRB-friendly security position. Both are honest; they are just not the same architecture, and only one of them can be proposed.

**This is your decision, not an editing fix.** Three options:

1. **Commit to the narrative.** FRB-controlled VPN and bastion only, no Wesco-operated path. Redraw the diagram with the Wesco service delivery platform removed and the FRB remote access path shown instead. This is the strongest security position and the easiest to get through review. The cost is on delivery, covered below.
2. **Commit to the diagram.** Describe the Wesco support path explicitly, state that it is outbound-initiated from the customer side with no inbound listener, brokered through the FRB secure edge device, and subject to FRB approval and monitoring. This is defensible if drawn and described accurately, and it matches how the product is actually supported. It will draw scrutiny, so it has to be precise.
3. **Offer both and let FRB choose.** Present the FRB-controlled path as the proposed baseline and the Wesco-managed path as an option the Owner may approve. This is honest, it matches the two paths that genuinely exist, and it lets the Bank's security team own the decision, which they will want to.

I would recommend option 3, with option 1 as the drawn baseline. It matches reality, it avoids over-committing on either side, and it hands the security decision to the people who will insist on making it anyway.

**Whichever you choose, the delivery consequence is real.** If the FRB-controlled path is what ships, support staff will need FRB-issued credentials or devices, and access requests will run on FRB timelines and approvals. The project record shows this exact pattern producing a hard block elsewhere, with a dev environment access request rejected outright and the approval chain unclear. Any SLA elsewhere in the response must be achievable under that constraint. Settle this with Ron Snyder before submission rather than after award.

### 1.2 The subnet CIDRs must come out

The table publishes specific internal addressing: 10.21.63.0/24, 10.21.64.0/24, 10.21.12.0/24, 10.10.40.0/24, 10.21.18.0/24, 10.21.65.0/24, 10.21.15.0/24.

There are only two possibilities and both are bad.

If these are real FRB addresses, the response is publishing a Federal Reserve Bank's internal network topology in a document that will be emailed, printed, stored on shared drives, and read by people outside the evaluation team. For this client, that is a serious finding, and it is the kind of thing that damages credibility precisely with the security reviewers you most need to impress.

If they are illustrative and invented, they are fabricated specifics presented with the authority of fact, sitting in a column where every other entry says "Customer-defined." An evaluator who knows their own addressing will see numbers that are not theirs and conclude the table was lifted from somewhere else.

Replace every subnet entry with "Owner-defined" and keep the rest of the row intact. The table loses nothing: its value is in the protocol, port, and direction columns, not the addressing.

**Question for you before this is closed:** where did those numbers come from? If they were carried in from another customer's deployment or a reference architecture, that needs checking across the whole response, not just this table.

### 1.3 The response describes three different layer models

- The opening paragraph of 4.1 says three layers: OT Systems, IDL, and "Smart Building Platform Unified User Interface (SBP/UUI)".
- The table immediately below it lists four: Field and OT Systems, Integration and Data, Smart Building Platform, Enterprise and Operational Workflow.
- The Section 3 architecture graphic shows five: OT, IDL, SBP, UUI, Enterprise.
- Sections 3.1, 3.2, and 3.3 treat SBP, IDL, and UUI as three separate things, which the 4.1 opening paragraph merges into two.

An evaluator reading 3.x and 4.1 together sees an architecture section that cannot count its own architecture. This is more damaging than it looks, because the layered model is the central claim of the response.

Recommendation: adopt the five-layer model from the graphic everywhere, since that is the version that is drawn, and the one 3.1 through 3.3 imply. Rewrite the 4.1 opening paragraph and expand the table to five rows to match. If there is a reason the narrative wants three layers, then state the five-layer model and note that it is commonly summarized as three, but do not leave the reader to reconcile it.

---

## The illustration, as a drawing

Separate from the architectural contradiction in 1.1, the diagram is not submission-ready. The same criticisms apply as to the multi-site graphic in Section 3.1.

- **It is a generic Wesco diagram, not an FRB one.** "Customer Network," "Local entroCIM," and unlabeled generic device groups. A proposal diagram should be titled and labeled for FRB NJ Cash Services, with the Bank's named systems on it.
- **Legibility.** Text is small, several labels are truncated or ambiguous, and the connectivity key in the lower left is too small to read at page scale. It will be printed.
- **The subnets from the segmentation table appear nowhere on it.** That reinforces the concern in 1.2 that those addresses came from another source.
- **No security zones or boundaries are drawn.** For this audience, the diagram should show the security boundary explicitly, along with the OT VLAN segmentation the narrative relies on. The narrative claims VLAN isolation, minimized lateral movement, and restricted external connectivity; the diagram shows a single flat local switch.
- **"nginx (Optional)" appears on the diagram as well as in the text.** Decide whether it is in the proposed deployment and draw it that way. Optional components on an architecture diagram read as an unfinished design.
- **Arrow direction and initiation are not distinguishable.** For every link crossing a boundary, the diagram should make clear which side initiates. That single piece of information is what a security reviewer is looking for, and it is what would make the support path in 1.1 defensible if you choose that option.

Recommendation: redraw for this project. If schedule does not permit a proper redraw, the safer choice is to remove the diagram and describe the architecture in text, because as drawn it actively undercuts the narrative beside it.

---

## Priority 2

### 2.1 The IDL is named as a primary layer and then never described

The opening paragraph names the Independent Data Layer as one of the three primary layers. The corresponding table row, "Integration and Data Layer," describes only transport: BACnet/IP, Modbus TCP/IP, MQTT, REST APIs, and the open-protocol requirement. Those are integration methods, not a data layer.

Nothing in 4.1 describes normalization, metadata, the asset and equipment model, tagging, historization, or data quality, which is the entire content of Section 3.2. The SBP row then refers to "normalized IDL data" without anything having explained where normalization occurs.

Recommendation: split that row in two. An "Integration Layer" row covering protocols and interfaces, and an "Independent Data Layer" row covering normalization, the semantic model, metadata and asset relationships, historization, and Owner access. This also fixes the layer-count problem in 1.2, since it moves the table toward the five-layer model.

### 2.2 SBP and UUI are merged in a response that separates them

The Smart Building Platform row ends with "The same Local entroCIM platform also provide dashboards, heatmaps, trend charts, alarm consoles, and model-based views through the UUI." That is Section 3.3's content inside Section 3.1's row.

Give the UUI its own row. If the response has a dedicated 3.3, the architecture section should reflect that structure rather than collapse it.

### 2.3 The unencrypted OT protocols are visible and unaddressed

The table shows BACnet/IP on UDP 47808 and Modbus/TCP on 502. Both are cleartext and unauthenticated. Meanwhile Section 3.1 emphasizes encryption in transit and at rest.

This is not a flaw in the design. It is inherent to those protocols and every competitor will have the same exposure. But a Federal Reserve security reviewer will notice the gap between the encryption narrative and the OT rows, and it is far better to name it than to be asked about it.

Add a short note beneath the table: OT field protocols such as BACnet/IP and Modbus/TCP do not provide native encryption or authentication, which is why they are confined to dedicated, segmented VLANs with routing controlled at the local firewall, and why all traffic leaving the OT segments toward users, APIs, and enterprise systems is encrypted. Stating the compensating control converts a weakness into evidence of a considered design.

### 2.4 Named components create obligations that are not addressed

The text names nginx as an optional reverse proxy and Mosquitto as the MQTT broker. Three issues:

- **"Optional" is ambiguous in a proposal.** Either these are in the proposed deployment or they are not. Say which.
- **Patch and vulnerability responsibility.** Naming specific open-source components on Owner-hosted infrastructure invites the immediate question of who monitors CVEs and applies patches, and on what cadence. This is the same gap flagged in the 3.1 review under Owner-hosting content. Answer it once, somewhere, and cross-reference.
- **I cannot verify either component from the project record.** Confirm with Ron Snyder that this is how entroCIM actually deploys before it is written down as architecture.

### 2.5 The isolation claim needs one more check

The Core Services row lists DNS, NTP, syslog, AV, and configuration management as internal only, and the narrative says no inbound internet exposure is required. Good.

The question not answered: does entroCIM or any component beneath it require **outbound** connectivity for license validation, activation, or update retrieval? This is a common and embarrassing discovery after award, and it interacts with the licensed third-party analytics platform underneath. Confirm with Ron Snyder, and if outbound is required for licensing, say so plainly now with the proposed control, rather than having it surface in a security review.

### 2.6 Document citations are still in filename form

"App A_FRB CSC Systems Integrated Architecture Single Line.pdf", "the Drawing & Spec List dated 2026.07.15", and "20260623_BOD - FRBNY, NJ - WP#4_Smart Building (Final).pdf" should be formal document references with revision and, where a specific requirement is cited, a section or paragraph number. Same issue as 3.1. Fix both together with one pass across the response.

### 2.7 ICUGN

Section 4.1 expands it as "Isolated Corporate User Group Network." Section 3.1 called it "the Bank's IT VLAN network known as the ICUGN." Confirm the expansion against the Basis of Design, define it once at first use in the document as a whole, and use the acronym alone thereafter. Getting the client's own network name wrong is the kind of error evaluators remember.

### 2.8 SCADA and PLC scope

The table includes a SCADA/PLC VLAN with Modbus/TCP marked "(as used)". The Section 3.1 asset table has no SCADA or PLC category. Either this is real scope that 3.1 omits, or it is a generic row carried in from a template. Resolve it, and remove the "(as used)" hedge either way.

---

## Line-level corrections

| Current | Issue | Recommended |
|---|---|---|
| "Based on the App A... and the Drawing & Spec List dated 2026.07.15, HVAC/BMS, EPMS/electrical, ... and BIM as the current system categories." | Sentence fragment, no verb | "Appendix A and the Drawing and Specification List dated 15 July 2026 identify the following current system categories: HVAC/BMS, EPMS and electrical, lighting controls, elevators, geothermal, plumbing, smart washroom, fire alarm, IAQ, occupancy, and BIM." |
| "The SBP that deployed as Local entroCIM consumes normalized IDL data" | Ungrammatical | "The Smart Building Platform, deployed as an on-premises entroCIM instance, consumes normalized data from the IDL" |
| "The same Local entroCIM platform also provide dashboards" | Subject/verb agreement, and see 2.2 | Move to a UUI row and correct to "provides" |
| "Local entroCIM" (throughout) | Capitalized as if a product name or SKU | "the on-premises entroCIM instance" |
| "The proposed on-prem or Owner-controlled deployment" | "or" implies two options or uncertainty; "on-prem" is informal | "The proposed on-premises, Owner-controlled deployment" |
| "Below is an example of how entroCIM handles the different Network segmentation the relates the above High Level Network architecture for clarity." | Ungrammatical | "The following table describes the network segmentation associated with the architecture above." |
| "in this case IBM TRIRIGA" | Missing punctuation | "the Owner's existing IWMS/CMMS, in this case IBM TRIRIGA," |
| "Below is the illustration of High Level Network Architecture proposed for FRB NJ" | Informal | "The following illustration shows the proposed high-level network architecture for the FRB NJ Cash Services facility." |
| "47808via", "47808and", "8883(preferred)", "443(vendor API)", "8883, HTTPS" | Missing spaces, repeated throughout the table | Correct spacing throughout |
| "BBMD/FDR" | Undefined acronyms | Spell out at first use: BACnet Broadcast Management Device and Foreign Device Registration |
| "Modbus TCP/IP where approved" | Ambiguous placement of the qualifier | "Modbus TCP/IP, where approved by the Owner" |
| "Modbus/TCP 502 (as used)" | Hedge | Remove, and see 2.8 |

---

## Content missing from 4.1

Each of these is the kind of thing a technical evaluator expects in a high-level architecture section:

- **Redundancy and availability.** Single application server is implied and never stated. What happens when it fails, and is HA offered?
- **Time synchronization.** NTP appears in the Core Services row without comment. Trend integrity, fault correlation, and alarm sequencing all depend on synchronized time across OT systems and the platform. One sentence establishes that you understand this.
- **Where the IDL physically runs.** Same host as the application, separate host, separate storage? The section names the application server and never locates the data layer.
- **Backup and recovery.** Not mentioned anywhere in 4.1, and the Owner is hosting.
- **Virtual infrastructure requirements.** Flagged in the 3.1 review and still absent. The Owner cannot size or cost what they are being asked to host.

---

## Verification items and owners

| Item | Why it matters | Owner |
|---|---|---|
| Which remote access architecture is being proposed, per item 1.1 | The text and the diagram currently propose two different ones | Darryl, with Ron Snyder |
| Origin of the subnet CIDRs | Security disclosure or fabricated specifics, and possible contamination elsewhere in the response | Proposal lead, then Darryl |
| Whether Wesco can meet its support commitments under FRB-controlled VPN and bastion only | The narrative forecloses the normal on-premises support path | Darryl, with Ron Snyder |
| nginx and Mosquitto as actual entroCIM deployment components | Named as architecture, unverifiable from the record | Ron Snyder |
| Outbound connectivity required for licensing, activation, or updates | Directly tests the isolation claim | Ron Snyder |
| Patch and CVE responsibility for named OSS components on Owner infrastructure | Follows immediately from naming them | Ron Snyder |
| ICUGN expansion, verified against the Basis of Design | Client's own network name | Proposal coordinator |
| SCADA and PLC scope | Present in 4.1, absent from the 3.1 asset table | Proposal lead |
| Final layer model, applied across 3.x and 4.1 | Central claim of the response | Darryl |

---

## Consistency actions across 3.x and 4.1

These cannot be fixed inside one section:

1. Settle the layer model and apply it to the graphic, the 4.1 opening paragraph, the 4.1 table, and the 3.1 through 3.3 structure.
2. Settle the remote access architecture once, then make the 4.1 narrative, the 4.1 illustration, and the Section 3.1 multi-site graphic all say the same thing. Three artifacts currently show three positions on vendor connectivity.
3. Convert all filename citations to formal document references in one pass.
4. Define ICUGN once, at first use in the document.
5. Reconcile the 3.1 asset categories with the 4.1 network segments, in both directions.
