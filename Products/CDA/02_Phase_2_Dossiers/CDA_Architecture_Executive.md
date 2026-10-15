# Connected Device Assurance — Solution Structure (Executive View)
Overhauled 2026-07-27 to the product decomposition (partner sensor + Base/Advanced Wesco tools) and rulings of that date.

## What this diagram shows — and what it deliberately does not

**This is a solution structure / deployment responsibility view.** It answers: what are the pieces, who provides them (partner vs. Wesco), where do they run, and how do they reach the customer's devices. It is the view for an endorsement audience.

It is **not** a workflow or a dataflow. Companions:
- The **data-fidelity ladder** (discovered → validated → managed) is a three-chip slide graphic on the offer slide, not an architecture diagram.
- The **controlled-action workflow** (approve → execute → validate → evidence) is the sequence diagram in `Phase_2_Review_Timeline_and_Architecture.md` §3.2 — engineering/appendix material for security and legal audiences.

## Intent

Show the two Wesco tools and the partner sensor, their placement at the customer site (or remote), the Airwall path, and the WAM and Navigator integrations. Readable in under a minute.

```mermaid
flowchart LR
    subgraph customerSite["Customer Site"]
        devices["Covered Devices<br/>Cameras, Access Control, Network"]:::site
        serviceNode["Containerized Service Node<br/>Small PC or Customer Server"]:::network
        sensor["Partner Sensor<br/>Endpoint and OT Discovery"]:::external
        baseTool["Wesco Device Assurance, Base<br/>entroCIM: Health, Alerting, Evidence"]:::app
        advTool["Wesco Configuration Assurance, Advanced<br/>entroCIM: Firmware and Lifecycle"]:::app
        navFuture["Navigator Components<br/>Future: Field Service Integration"]:::future
        airwallEdge["Airwall"]:::secure
    end

    subgraph wesco["Wesco"]
        control["Service Delivery and Control<br/>Operators, Approvals, Evidence"]:::cloud
        wam["WAM<br/>Lifecycle and Refresh Signals"]:::data
        navigator["Navigator<br/>Field Work Orders, 2027 Integrations"]:::external
    end

    serviceNode --- sensor
    serviceNode --- baseTool
    serviceNode --- advTool
    serviceNode -.- navFuture

    devices -->|Endpoint and network activity| sensor
    sensor -->|Discovered assets and versions<br/>API| baseTool
    baseTool -.->|Device integration<br/>where completed| devices
    advTool -->|Validated versions and<br/>controlled updates| devices
    control -->|Manage remote devices over<br/>secure Airwall link| airwallEdge
    airwallEdge -->|Scoped access| baseTool
    control -->|Arcbeam clustering:<br/>run entroCIM devices from Wesco cloud| serviceNode
    baseTool -->|Alerts, evidence, escalation| control
    control -->|Refresh and failure signals| wam
    control -->|Field work packages| navigator

    classDef site fill:#eef6ff,stroke:#4b83c4,stroke-width:1px;
    classDef network fill:#f2f2f2,stroke:#777,stroke-width:1px;
    classDef secure fill:#fff4e5,stroke:#c47f00,stroke-width:1px;
    classDef cloud fill:#f1f5ff,stroke:#5b6ee1,stroke-width:1px;
    classDef app fill:#f4f7f2,stroke:#6a8f4e,stroke-width:1px;
    classDef data fill:#f7f1fb,stroke:#8a63a8,stroke-width:1px;
    classDef external fill:#f7f7f7,stroke:#777,stroke-width:1px;
    classDef future fill:#ffffff,stroke:#999,stroke-dasharray: 5 5;
```

## Assumptions

- The service node grouping (small PC or customer server) hosts all three components; in the fully remote mode the two Wesco tools run in Wesco Azure and reach the site over the same Airwall link. One diagram covers both by construction; the remote variant is stated in slide text, not drawn separately.
- The dashed base-tool-to-devices arrow is deliberate: base-tier device integration exists only where completed; otherwise the base tool carries partner-sourced data.
- Advanced tool reaches devices through direct device integration (verified models, validated versions).

## Validation Items

- Arcbeam shown per Darryl 07-27 as the second secure connection (semantics: Airwall link = manage the remote devices; Arcbeam = run entroCIM devices from the Wesco cloud). Clustering readiness still to validate with Ron Snyder.
- Partner sensor unnamed per 07-27 ruling.
- Navigator node components marked future (supports Navigator's 2027 integrations).

## Exclusions

- Credential handling, multi-tenancy, fleet management, container packaging: engineering detail, dossier §7 and §9.
