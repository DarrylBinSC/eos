# Mermaid Sync Test

Test of a Mermaid diagram kept in sync between this file and a Miro diagram widget. Version 1 is the code as written by Claude, before any edits in Miro.

<!-- miro: board "Mermaid Sync Test 2026-10-15", widget "EOS diagram pipeline" (3458764687338519290). Source of truth: Mermaid code, synced. -->
```mermaid
flowchart LR
    classDef author fill:#E3E7EA,stroke:#8E9296,color:#1D252D
    classDef tool fill:#004986,stroke:#00305A,color:#FFFFFF
    classDef output fill:#CDEBD6,stroke:#00953A,color:#1D252D

    subgraph cloud [Claude session]
        A[Draft .md with Mermaid block]:::author
    end
    subgraph mac [Darryl's Mac]
        B[Pandoc inbox]:::tool
        C[Watcher and mermaid-filter]:::tool
        D[Word document]:::output
    end
    subgraph miro [Miro board]
        E[Editable diagram]:::output
    end

    A -->|copy to inbox| B
    B -->|convert| C
    C -->|render| D
    A -->|build from code| E
    E -->|read code back| A
```

::: {custom-style="Image Caption"}
EOS diagram pipeline, version 1 (before Miro edits).
:::

## Version 2: code read back from Miro after Darryl's visual edits

<!-- miro: same widget, read back 2026-10-15 after visual edits. -->
```mermaid
---
config:
  flowchart:
    nodeSpacing: 20
    rankSpacing: 25
---
flowchart BT
    classDef author fill:#E3E7EA,stroke:#8E9296,color:#1D252D
    classDef tool fill:#004986,stroke:#00305A,color:#FFFFFF
    classDef output fill:#CDEBD6,stroke:#00953A,color:#1D252D

    subgraph cloud [Claude session]
        A[Draft .md with Mermaid block]:::author
    end
    subgraph mac [Darryl's Mac]
        B[Pandoc inbox]:::tool
        C[Watcher and mermaid-filter]:::tool
        D[Word document]:::output
    end
    subgraph miro [Miro board]
        E[Editable diagram]:::output
      n1[PowerPoint build]:::output
      E --> n1
    end

    A -->|copy to inbox| B
    B -->|convert| C
    C -->|render| D
    A -->|build from code| E
    E -->|read code back| A
  style cloud fill:#c6dcff
  style mac fill:#adf0c7
```

::: {custom-style="Image Caption"}
EOS diagram pipeline, version 2 (after Miro edits: direction, spacing, new node, group colors).
:::
