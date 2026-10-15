# Miro Export Test

This document tests the full path for a Miro diagram in a Word document: a frame exported from Miro, saved into the EOS, placed in Markdown, and converted by the Pandoc watcher. A synced Mermaid flowchart sits beside it for comparison.

## Figure from a Miro frame export

The image below is option 1A from the Launch Studio layout sketches, framed tightly in Miro and exported as an image.

<!-- miro: board "Launch Studio Sean Deck 2026-10", frame "Slide 1 options: What Launch Studio is" (3458764687098664603). Exported by Darryl. -->
![](Deliverables/EOS_Meta/2026-10-15_Miro_Export_Test_diagrams/launch_studio_slide1_options_2026-10-15.jpg)

::: {custom-style="Image Caption"}
Launch Studio, option 1A: from business prototype to supported product. Exported from Miro.
:::

## Figure from synced Mermaid code

<!-- miro: board "Mermaid Sync Test 2026-10-15", widget "EOS diagram pipeline" (3458764687338519290). Synced Mermaid; version 1 layout. -->
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
EOS diagram pipeline, rendered from Mermaid code by the watcher.
:::
