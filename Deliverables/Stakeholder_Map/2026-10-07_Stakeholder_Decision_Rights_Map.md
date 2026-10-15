# Stakeholder Decision-Rights Map

Private working file. Who sponsors, decides, builds, delivers and sells each product in Darryl's portfolio, colored by current alignment. Mermaid fallback for the Miro board. Source data: `2026-10-07_Core_Stakeholders_Alignment_Draft.md`.

**Source of truth (Darryl, 2026-10-07): the private Miro board "Stakeholder Map 2026-10" (https://miro.com/app/board/uXjVEdM5q1g=/), in Darryl's personal Miro account.** The alignment draft is its data source; the .mmd is the Mermaid fallback. The .pptx and .png are superseded (`SUPERSEDED_2026-10-07_*`) and are not maintained.

```mermaid
flowchart LR
  subgraph EXEC["Executive and decision rights"]
    DIRK["Dirk Naylor<br/>EVP & GM, CSS"]
    GREG["Greg O'Brien<br/>SVP & GM, TSS"]
    AKASH["Akash Khurana<br/>CIO"]
    SEAN["Sean McCloskey<br/>VP, all digital products"]
    LISA["Lisa Orton<br/>IT to CSS connection"]
  end
  subgraph PEER["Peer and platform organizations"]
    BRAD["Brad Stevens<br/>VP Sales"]
    CHRISG["Chris Gazdic<br/>Product Operations"]
    MERWAN["Merwan Mereby<br/>India development and AI"]
    TOM["Tom Boss<br/>Finance"]
    MADDY["Maddy Taylor<br/>Digital Products peer"]
  end
  subgraph TEAM["Darryl's team"]
    DARRYL["Darryl Benson<br/>Sr Dir, CSS Platforms"]
    DAVID["David Blondel<br/>Product Executive"]
    RON["Ron Snyder<br/>Development"]
    CHAD["Chad Steger<br/>Deployment"]
    AKANSH["Akansh Gangil<br/>WAM / ADM PO"]
  end
  subgraph PROD["Products"]
    ECIM(["entroCIM"])
    CDA(["CDA"])
    WAM(["WAM"])
    NAV(["Navigator"])
    VIBE(["Vibe coding productization"])
    ARIS(["Aris (paused)"])
  end
  subgraph SALES["Sales and commercial"]
    NATE["Nathan Kehr<br/>CSS Platforms sales"]
    BILL["Bill Muczko<br/>Global Enterprise, CDA sponsor"]
    BOB["Bob Caprise<br/>CSS Sales"]
    SRIDHAR["Sridhar Loke<br/>Commercialization"]
    AMY["Amy Aguirre<br/>WAM commercial"]
    WASSIL["Michael Wassil<br/>Competitive intel"]
  end
  subgraph DELIV["Delivery and vendors"]
    EMILY["Emily Munk<br/>Strategic Initiatives, TSS"]
    SENTHIL["Senthil Govindaswamy<br/>WAM delivery"]
    DJ["DJ Vaughn<br/>Navigator delivery"]
    SUNNY["Sunny Sharma<br/>Strev, WAM vendor"]
  end

  AKASH -->|manages| SEAN
  AKASH -->|manages| LISA
  AKASH -->|manages| MERWAN
  LISA -->|influences| NAV
  SEAN -->|manages| DARRYL
  SEAN -->|manages| MADDY
  DARRYL -->|leads| DAVID
  DARRYL -->|leads| RON
  DARRYL -->|leads| CHAD
  DAVID -->|leads| AKANSH
  DIRK -->|sponsors| ECIM
  DIRK -->|sponsors| NAV
  LISA -->|routes to| DIRK
  SEAN -->|funds, originated| VIBE
  SEAN -->|receiving| ARIS
  AKASH -->|WAM takeover decision| WAM
  GREG -.->|delivery home, not engaged| CDA
  BRAD -.->|integrated platform push| ECIM
  CHRISG -->|product executive| NAV
  MERWAN -->|builds today| WAM
  TOM -->|P&L| ECIM
  DARRYL -->|stands up| VIBE
  DAVID -->|product executive| ECIM
  RON -->|builds| ECIM
  RON -->|builds| CDA
  CHAD -->|deploys| ECIM
  AKANSH -->|product owner| WAM
  ECIM -->|sold by| NATE
  CDA -->|champion| NATE
  CDA -->|sponsor| BILL
  CDA -->|champion| BOB
  CDA -->|commercialization| SRIDHAR
  WAM -->|commercialized by| AMY
  ECIM -->|intel| WASSIL
  CDA -.->|route to Greg| EMILY
  WAM -->|delivered by| SENTHIL
  NAV -->|delivered by| DJ
  WAM -->|platform vendor| SUNNY

  classDef ally fill:#00953A,stroke:#006B29,color:#FFFFFF
  classDef supportive fill:#CDEBD6,stroke:#00953A,color:#1D252D
  classDef neutral fill:#E3E7EA,stroke:#8E9296,color:#1D252D
  classDef mixed fill:#F7D9A8,stroke:#C77A12,color:#1D252D
  classDef unknown fill:#FFFFFF,stroke:#5B7A8E,color:#1D252D,stroke-dasharray:5 3
  classDef self fill:#1D252D,stroke:#1D252D,color:#FFFFFF
  classDef product fill:#004986,stroke:#004986,color:#FFFFFF
  class SEAN,LISA,CHRISG,NATE,BILL,BOB,DAVID,RON,CHAD,AKANSH ally
  class SRIDHAR,SENTHIL,DJ,WASSIL,MADDY,SUNNY supportive
  class AKASH,MERWAN,TOM,AMY neutral
  class BRAD mixed
  class DIRK,GREG,EMILY unknown
  class DARRYL self
  class ECIM,CDA,WAM,NAV,VIBE,ARIS product
  style EXEC fill:#F4F6F7,stroke:#B7C9D3
  style PEER fill:#F4F6F7,stroke:#B7C9D3
  style TEAM fill:#F4F6F7,stroke:#B7C9D3
  style PROD fill:#EAF0F6,stroke:#004986
  style SALES fill:#F4F6F7,stroke:#B7C9D3
  style DELIV fill:#F4F6F7,stroke:#B7C9D3
```

::: {custom-style="Image Caption"}
Decision rights across Darryl's products, 2026-10-07. Fill shows alignment: solid green ally, light green supportive, grey neutral, amber mixed, dashed outline unknown; navy is Darryl, blue ovals are products. Dotted lines are routes not yet established.
:::

## Assumptions

- Alignment corrected by Darryl 2026-10-07 for Sean McCloskey, Lisa Orton and Chris Gazdic (allies), Amy Aguirre (neutral) and Maddy Taylor (supportive); stated earlier for Nathan Kehr, Bill Muczko, Bob Caprise and the route through Emily Munk. The rest is Claude's reading of `06_Stakeholder_Map.md`.
- Reporting lines shown only at the top (Darryl, 2026-10-07): Akash Khurana is CIO, at Dirk Naylor's level; Sean McCloskey, Lisa Orton and Merwan Mereby report to him; the India development and AI groups report to Merwan; Lisa is the direct connection from IT to CSS and has influence and some responsibility on Navigator; Maddy Taylor reports to Sean; Sean is responsible for all digital products.
- Other reporting lines (Greg O'Brien to Brad Stevens and Emily Munk, Darryl to his team) are omitted to keep the map readable.
- Navigator's sales owner is not specific in the record; shown on the slide as CSS Sales.
- Update this file and the alignment draft together when a relationship changes.
