# Stanford Commissioning App: ownership position for the 10-26 legal meeting

Prepared 2026-10-20 for Darryl Benson. Meeting: Monday 2026-10-26, 08:30 ET, Nikos Minas and Brandon Thompson. Internal working file; not for distribution outside Wesco.

## The question

Does Wesco own the entroCIM Commissioning toolset (test engine, Commissioning Test App, Commissioning Report App), or is it Stanford work product under the purchase order that funded its development for Stanford in 2022? Secondary: what Stanford is entitled to run if it drops entroCIM and keeps SkySpark-only licenses, and whether Stanford's terms restrict Wesco's reuse of the toolset elsewhere.

## Position

The Commissioning toolset is Wesco's pre-existing intellectual property. It was first commissioned and launched for CODA Tech Square in 2021 and applied at Stanford under the 2022 engagement. Under Stanford's PO terms (18.4), pre-existing or independently developed software is excluded from Stanford's work product. Stanford's work product is the test content written for it: the Gates examples (2022) and the LBRE scripts (2023).

## Facts in the record

| Date | Fact | Source |
|---|---|---|
| 2021-08-01 | Stanford Gates FTP documents dated; later named as the 2022 quote's example tests | 2022 quote |
| 2021-10-12 | Stanford "Functional Testing Programming" quote source file created | Word metadata on the 2022 quote PDF |
| 2021-10-20 | Hepta Systems proposal to Portman Holdings for the Commissioning FDD App at CODA Tech Square. Scope of Work, Interface and Deliverable sections are the same text as the later Stanford quote; the app's addition adjusts the entroCIM maintenance fee | CODA scope PDF (unsigned copy, price blank) |
| 2021-10-25 | Hepta Systems receives notice to proceed with the Commissioning App at CODA Tech Square | Jeremy Houck email, forwarded by Keith Bishop 2026-10-20 |
| 2022-01-13 | Warez LLC quote to Stanford, $57,500, engine, two apps, documentation, Gates examples; delivered as a compiled component | Quote (unsigned copy) |
| 2022-01-31 | Stanford PO 62783761 to Warez LLC; term to 2022-04-30; Stanford's PO terms incorporated, seller terms rejected | PO |
| 2023-10-17 | entroCIM quote to Stanford, $34,750, LBRE scripts on the existing toolset; excludes changes to the toolset itself | Quote (unsigned copy) |
| 2023-11-13 | Stanford PO 63305925 to entroCIM; same terms clause | PO |
| 2026-07-29 | Current Stanford PO terms page last updated; 18.2 ownership, 18.4 excluded materials and license-back, 18.5 reuse limit | fingate.stanford.edu |

## What Stanford's terms do with these facts

- 18.4 excludes IP "created, owned or licensed by Contractor" before the PO date, including software components. The CODA record puts the Commissioning App before the Stanford PO.
- 18.4 also gives Stanford a perpetual, irrevocable, royalty-free license to Excluded Materials to the extent necessary to use its Work Product. Stanford's Work Product is the Gates and LBRE tests. On this reading Stanford may keep running the app for those tests even though Wesco owns it.
- 18.5 restricts reuse of Work Product only. If the toolset is Excluded Materials, 18.5 does not reach it. The tests are Stanford's and should not be reused elsewhere without approval.
- The 2022 quote describes a design phase and prices the engine and views as new programming. The same scope, in the same words, was proposed to CODA three months earlier, so that language is the product's standard proposal text rather than a Stanford-specific design. Anything built new for Stanford beyond the CODA scope is the exposure; the Gates tests are the only Stanford-specific item in the quote.

## Gaps to close before Monday

1. CODA scope document: in hand. Remaining: the executed CODA order and price. Owner: Keith Bishop.
2. Evidence the app was delivered at CODA before 2022-01-31: deployment date, invoice, handover note. Owner: Keith Bishop.
3. CODA's purchase terms. If they carry a work-product clause, the question moves to CODA rather than ending. Owner: Mike Reed or Keith Bishop.
4. Entity chain: Hepta Systems (CODA, 2021), Warez LLC (Stanford, 2022), entroCIM (Stanford, 2023), Anixter/Wesco (now). Show Warez owned or licensed the app at the Stanford PO date and that the acquisition assignment carried it. Owner: Brandon Thompson.
5. What the 2022 build added beyond the CODA app: repo history or release notes. Owner: Keith Bishop or Ron Snyder.
6. Stanford PO terms as of January 2022 and November 2023. Owner: Nikos Minas.

## Questions for Nikos

- On these facts, is the toolset Excluded Materials under 18.4, and what evidence would make that conclusion safe?
- What is the scope of Stanford's license-back if they drop entroCIM: may they run the app on a SkySpark-only instance for their own tests?
- Does 18.5 create any exposure to Wesco's use of the toolset at other customers, given the Gates examples were built into the product?
- Going forward, what terms should accompany any customer-funded development on a university PO so this does not recur?

## What is said to Stanford meanwhile

Nothing on ownership. The line for Thursday 10-22 stands: the original agreements are under review and Wesco will respond in writing.
