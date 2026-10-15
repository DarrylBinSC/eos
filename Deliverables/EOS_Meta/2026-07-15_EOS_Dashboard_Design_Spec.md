# EOS Dashboard — Design Brief

**For:** Claude Design session. Attached: `EOS_Dashboard_Prototype.html` (working prototype with real data).
**Owner:** Darryl Benson, Senior Director. This is a private, single-user executive readout — not a team or customer-facing product.

## What this is

A one-page readout of an Executive Operating System: five leadership-effectiveness indicators (decision velocity, commitment balance, watch-list heat, impact capture, time at role), each rated Red/Amber/Green with a 3-day trend, plus supporting tables (decision radar, commitment aging, watch-list highs, recurring themes). It is regenerated automatically after each daily briefing.

## Usage pattern (design for this)

- Read in ~30 seconds, typically once a day, desktop browser.
- The question it answers: *where does my leadership attention go today?*
- Occasional deeper read: click an indicator card for the "why" and a recommended action.
- May occasionally be printed or saved to PDF.

## Goals for this session

Produce 2–3 distinct visual directions. Interested in seeing:

1. A denser, executive-terminal treatment (more information per screen, less air).
2. A refined version of the current card-based layout (better typography and hierarchy).
3. A dark mode variant of whichever direction is strongest.

The learning goal: which hierarchy decisions survive across treatments — what is structural vs. decoration.

## Must preserve (information design, non-negotiable)

- **Five indicators, no composite score.** A single "EOS score" is explicitly rejected — it hides more than it reveals.
- **RAG discipline:** Red/Amber/Green status is the primary signal; the metric number is secondary.
- **Why one click away:** every indicator exposes its reasoning and one recommended action on demand — never on the main surface.
- **Trends over snapshots:** each indicator shows direction over time (currently 3 data points; will grow).
- **Executive-read headline:** one or two sentences of judgment at the top, not a data summary.
- **Tables over charts** for the detail sections. No decorative visualization.
- **Tone:** professional, neutral, restrained. No enthusiasm, no gamification, no dashboard-product styling (no gauges, no donut charts, no KPI confetti).

## Open for design

Typography, spacing, density, color system (beyond keeping R/A/G semantics), card vs. row layout for indicators, treatment of trend sparklines, table styling, header/footer, dark mode palette, print layout.

## Technical constraints (matter for the final direction)

- Final output must be portable to a **single self-contained HTML file**: no external assets, no web fonts requiring network, no JS frameworks. System font stack preferred.
- Renders from a template that regenerates with fresh data each day — design decisions must be data-independent (e.g., tables grow/shrink, indicator count is fixed at five, RAG values change daily).
- Works offline from a local file; degrades sanely when printed.

## Out of scope

Changing the metrics, the scoring logic, or the content. Mobile-first layout (desktop is the primary surface; graceful narrow-screen fallback is enough).
