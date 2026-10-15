# entroCIM Support Process: Dell to Wesco

Two companion diagrams. Diagram 1 shows the end-to-end issue path across both organizations, including the unvalidated Dell-side process and the handoff. Diagram 2 shows the established Wesco Freshdesk lifecycle in detail.

---

## Diagram 1: End-to-End Issue Flow and Organizational Handoff

### Intent

Show how an issue travels from an affected user through Dell IT to Wesco support, where the handoff occurs, and which parts of the process are assumed rather than confirmed. Intended for the process agreement discussion with Dell.

```mermaid
flowchart LR
    subgraph dellOrg["Dell - Process Assumed, Requires Validation"]
        affectedUser["Affected User"]:::user
        dellIntake["Dell IT Intake"]:::risk
        dellTriage{"Dell IT issue or<br/>entroCIM issue?"}:::risk
        dellSnow["Dell ServiceNow<br/>Ticket"]:::external
    end

    subgraph wescoOrg["Wesco Support - Established Process"]
        supportEmail["support@entrocim.com<br/>support.ec@wesco.com"]:::app
        freshdesk["Freshdesk Ticket<br/>+ Support Group Notification"]:::app
        wescoLifecycle["Triage, Assignment,<br/>Resolution, Closure"]:::app
    end

    affectedUser -.->|Reports issue<br/>method unconfirmed| dellIntake
    dellIntake -.->|Initial triage<br/>criteria unconfirmed| dellTriage
    dellTriage -.->|Dell-managed infrastructure,<br/>access, servers, networking| dellSnow
    dellTriage -.->|Application or deployment<br/>handoff trigger unconfirmed| supportEmail
    supportEmail -->|Email creates ticket| freshdesk
    freshdesk --> wescoLifecycle
    wescoLifecycle -.->|Cross-referenced records<br/>when joint investigation needed| dellSnow
    wescoLifecycle -.->|Status and closure<br/>owner unconfirmed| affectedUser

    classDef user fill:#eefaf6,stroke:#3b8f73,stroke-width:1px,color:#222222;
    classDef risk fill:#fff0f0,stroke:#c43b3b,stroke-width:2px,color:#222222;
    classDef external fill:#f7f7f7,stroke:#777777,stroke-width:1px,color:#222222;
    classDef app fill:#f4f7f2,stroke:#6a8f4e,stroke-width:1px,color:#222222;
    style dellOrg fill:#ffffff,stroke:#b8b8b8,color:#222222
    style wescoOrg fill:#ffffff,stroke:#b8b8b8,color:#222222
    linkStyle default stroke:#555555
```

Dashed arrows and red-bordered nodes mark assumed behavior. Solid arrows mark the confirmed Wesco process. The record cross-referencing between Freshdesk and ServiceNow is mutual; shown as a single arrow for renderer compatibility.

> Renderer note (2026-07-24): Miro's Mermaid plugin rejects both YAML frontmatter and the `%%{init}%%` directive. These blocks are plain Mermaid (classDefs only) so they paste cleanly into Miro.

### Assumptions

- Dell IT receives issues first and performs initial routing. This is Wesco's current understanding, not a confirmed process.
- The two Wesco support addresses are the only intended intake path into Freshdesk.

### Validation Items (to be confirmed in the process agreement)

- How users report issues to Dell
- Who performs the initial triage
- Criteria distinguishing a Dell IT issue from an entroCIM issue
- When and how an issue is submitted to Wesco support
- Who owns the issue while its source is still being determined
- When a Dell ServiceNow ticket is required
- How Freshdesk and ServiceNow records are coordinated
- Who communicates status and closure to affected users

### Exclusions

- Wesco internal lifecycle detail (see Diagram 2)
- Technical infrastructure and connectivity detail

---

## Diagram 2: Wesco Freshdesk Lifecycle

### Intent

Show the established Wesco support process from ticket creation through closure, including the triage determination and the ServiceNow coordination path.

```mermaid
flowchart TB
    intake["1. Intake<br/>Email creates Freshdesk ticket,<br/>notifies support group"]:::app
    assign["2. Review and Assignment<br/>One accountable owner<br/>per ticket"]:::app
    triage{"3. Triage<br/>Determine issue category"}:::app
    appIssue["Application, configuration,<br/>or deployment issue"]:::app
    education["User knowledge,<br/>training, or process"]:::user
    dellDep["Dell-managed<br/>IT dependency"]:::external
    snow["Dell ServiceNow ticket<br/>Records cross-referenced"]:::external
    resolve["5. Resolution and Closure<br/>Root cause, corrective action,<br/>confirmation documented"]:::app
    review["6. Weekly Support Meeting<br/>Open tickets, priorities,<br/>ownership, blockers"]:::monitoring

    intake --> assign
    assign --> triage
    triage -->|Owned in Freshdesk| appIssue
    triage -->|Guidance provided| education
    triage -->|Coordinate via<br/>Dell ServiceNow| dellDep
    dellDep --> snow
    appIssue --> resolve
    education --> resolve
    snow -->|Resolution reflected<br/>in both systems| resolve
    resolve -.->|Ongoing review| review

    classDef app fill:#f4f7f2,stroke:#6a8f4e,stroke-width:1px,color:#222222;
    classDef user fill:#eefaf6,stroke:#3b8f73,stroke-width:1px,color:#222222;
    classDef external fill:#f7f7f7,stroke:#777777,stroke-width:1px,color:#222222;
    classDef monitoring fill:#f0f7ff,stroke:#3b78a0,stroke-width:1px,color:#222222;
    linkStyle default stroke:#555555
```

### Assumptions

- Owner responsibilities (symptom review, impact confirmation, technical triage coordination, resource engagement, status communication, driving to closure) sit within step 2 and are documented in the process narrative rather than the diagram.
- Dell environment access is coordinated through a team member with a Dell-managed laptop; excluded from the diagram as operational detail.

### Validation Items

- Ownership and handoff responsibilities when an investigation identifies a Dell-managed dependency (to be defined in the process agreement)
- Accountable owner on each side for joint investigations

### Exclusions

- Prioritization criteria and SLA detail
- Combined-cause issues requiring joint investigation (follow the ServiceNow coordination path)
