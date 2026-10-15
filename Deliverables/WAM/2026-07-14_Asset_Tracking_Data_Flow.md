> **SUPERSEDED 2026-08-19 by `2026-08-19_Complex_Build_Asset_Flow_v4.md`.** Retained for the decision trail. Corrected by Darryl on 2026-08-19: the path to ADM runs through DDP/EUDM rather than VAS direct, the capture mechanism is a WMX-triggered VAS workflow rather than a serial pull-back, and ACT is a dotted contingency into ADM rather than a live interim path. The VAS to CPQ template pull recorded here is confirmed and still holds. Diagram 1 below, the current-state gap view, is retired: current state is pre-DDP and not defined, and the work is the target state only.

# Asset Tracking Data Flow — v3.1 (Miro-compatible)
As of 2026-07-14. Source: VAS Roadmap transcript (Akansh Gangil framing, Govardhan Shetty mechanics). Audience: executive/internal alignment. Transcript 7:31–26:06 uncaptured — validate nothing contradicts.

Changes in v3.1: `%%{init}%%` directive replaces YAML frontmatter (Miro's renderer rejects frontmatter config); VAS→DDP sync edge removed from both diagrams for layout (recorded in Assumptions instead), which pulls DDP in tight behind WMX.

## The story in one sentence

Today serials are captured at shipment in WMX but never connected to the parent-child structure VAS already knows — so complex-build assets reach the customer with no serialized identity; the proposal closes that loop through VAS rather than building or scaling a separate capture tool.

**Memory hook:** *VAS knows the family, WMX knows the serials — today they never meet. The fix: introduce them, retire ACT.*

---

## Diagram 1 — Current State: Where the Gap Lives

### Intent
Show today's order-to-customer flow for asset attributes and make visible why complex-build serial/MAC data never reaches WAM at scale. (The disconnected bottom row is deliberate: nothing in the confirmed order chain feeds ADM today.)

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#f7f7f7","primaryBorderColor":"#9aa0a6","primaryTextColor":"#222222","lineColor":"#555555","clusterBkg":"#ffffff","clusterBorder":"#b8b8b8","tertiaryColor":"#ffffff"},"flowchart":{"diagramPadding":30,"nodeSpacing":60,"rankSpacing":70,"curve":"linear"}}}%%
flowchart LR
    vasTemplates["VAS<br/>Finished-goods templates<br/>parent-child BOM"]:::app
    cpq["CPQ"]:::app
    oms["OMS"]:::app
    wmx["WMX<br/>Serial capture at shipment"]:::app
    ddp["DDP / EUDM"]:::data
    act["ACT<br/>JPMC projects, few warehouses"]:::external
    adm["ADM"]:::app
    strev["Strev Platform<br/>WAM"]:::app
    customer["Customer / Integrator"]:::user
    gapComplexBuild["GAP: complex-build serial and MAC<br/>never linked to parent-child structure"]:::risk

    vasTemplates -->|"FG template pulled<br/>at sales order"| cpq
    cpq -->|"Order"| oms
    oms -->|"Fulfillment"| wmx
    wmx -->|"Serials propagate<br/>simple products only"| ddp
    wmx -.->|"No path for complex builds"| gapComplexBuild
    act -.->|"Limited complex-build capture"| adm
    adm -->|"Asset records"| strev
    strev -->|"Install-base visibility"| customer

    classDef app fill:#f4f7f2,stroke:#6a8f4e,stroke-width:1px;
    classDef data fill:#f7f1fb,stroke:#8a63a8,stroke-width:1px;
    classDef external fill:#f7f7f7,stroke:#777,stroke-width:1px;
    classDef user fill:#eefaf6,stroke:#3b8f73,stroke-width:1px;
    classDef risk fill:#fff0f0,stroke:#c43b3b,stroke-width:2px;
```

### Assumptions
- WMX serial capture is against the order at shipment (Govardhan, to be confirmed in detail).
- VAS part data is fully synced with DDP including price/cost (Govardhan) — edge omitted from the diagram for readability.

### Validation Items
- WMX MAC-address capture: unconfirmed (Steve Leslie / Sid).
- WMX complex-build limitation: no capability, no roadmap until 2028 (Akansh; confirm with GPO).
- ACT scope (JPMC + limited warehouses, not scaling): per Akansh and background sales discussions.

### Exclusions
Protocols, integration mechanics, DDP internals, and the VAS↔DDP sync edge — context, not the point of this view.

---

## Diagram 2 — Future State (Proposed): VAS Closes the Loop

### Intent
Show Govardhan's proposed mechanism: serials pulled back from WMX onto the VAS parent-child template, delivering serialized structures to ADM/WAM; ACT retired. The dashed PROPOSED links are the only new integrations.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#f7f7f7","primaryBorderColor":"#9aa0a6","primaryTextColor":"#222222","lineColor":"#555555","clusterBkg":"#ffffff","clusterBorder":"#b8b8b8","tertiaryColor":"#ffffff"},"flowchart":{"diagramPadding":30,"nodeSpacing":60,"rankSpacing":70,"curve":"linear"}}}%%
flowchart LR
    vas["VAS<br/>Parent-child template<br/>plus serial and MAC per transaction"]:::future
    cpq["CPQ"]:::app
    oms["OMS"]:::app
    wmx["WMX<br/>Serial capture at shipment<br/>unchanged"]:::app
    adm["ADM<br/>Normalization and enrichment"]:::app
    strev["Strev Platform<br/>WAM"]:::app
    customer["Customer / Integrator"]:::user
    act["ACT<br/>Retired from this flow"]:::external

    vas -->|"FG template at sales order"| cpq
    cpq -->|"Order"| oms
    oms -->|"Fulfillment"| wmx
    wmx -.->|"PROPOSED: serials pulled back<br/>under part number"| vas
    vas -.->|"PROPOSED: serialized<br/>parent-child structure"| adm
    adm -->|"Enriched asset records"| strev
    strev -->|"Install-base visibility<br/>incl. complex builds"| customer

    classDef app fill:#f4f7f2,stroke:#6a8f4e,stroke-width:1px;
    classDef external fill:#f7f7f7,stroke:#777,stroke-dasharray: 5 5;
    classDef user fill:#eefaf6,stroke:#3b8f73,stroke-width:1px;
    classDef future fill:#ffffff,stroke:#999,stroke-dasharray: 5 5;
```

### Assumptions
- The order chain (VAS→CPQ→OMS→WMX) is unchanged; the only new integrations are the serial pull-back and the VAS→ADM feed.
- VAS can extend to hold serial/MAC per transaction (Akansh's proposal; Govardhan agreed in principle).
- VAS↔DDP sync continues as today (omitted for readability).

### Validation Items
- WMX serial/MAC availability for complex-build orders — Steve Leslie (GPO) + Sid (WMX solution architect); Akansh engaging.
- Alan's detailed opinion once process is clear.
- GPO roadmap buy-in (Steve Leslie dictates the roadmap); then user validation (Troy Doyle).
- ACT lesson: validate WMX source-data fitness before funding the integration.

### Exclusions
Timing, sequencing, and ownership of the build — premature until validation items close. DDP node omitted (sync unchanged, not part of the proposal).
