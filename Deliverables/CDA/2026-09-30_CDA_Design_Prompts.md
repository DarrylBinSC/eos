# Claude Design prompts for the CDA deck

Two prompts. The first takes a screenshot of the Plan slide. The second takes the visuals-only PDF (`2026-09-30_CDA_Story_Test_Visuals_Only.pdf`, 19 pages). Paste each prompt with its attachment. Anything Design produces is a mockup to choose from; the chosen layout gets rebuilt natively from the pro forma so the numbers stay live.

---

## Prompt 1: the Plan slide

**Attach:** a screenshot of slide 9, "Plan, 2027 to 2031".

```
Context
This is one slide from an internal Wesco business case for a managed service called Connected Device Assurance. The slide's job is to show a VP, in one look, that we build in 2027, start earning in 2028, invest cash through 2029, and recover it inside the plan. The numbers are illustrative and will change, so I need layout ideas, not a finished graphic.

The data on the slide
Revenue by year, $M: 0, 1.2, 3.7, 6.6, 8.8 (2027 to 2031).
Gross margin by year, $M: 0, 0.4, 1.4, 2.5, 4.0.
Cumulative net cash, $M: -0.26, -1.9, -2.3, -1.1, +3.3. It bottoms in 2029 and crosses zero in 2031.
Development investment in 2027: $261K. Peak cash requirement: $2.3M. 684 sites and $9.4M run rate by 2031 at 46 percent gross margin.

The story the picture has to tell on its own
Build, invest, recover. The trough is the point, not a problem: it is small, it is bounded, and it turns.

Task
Give me three different layouts for this one slide, side by side, using the attached screenshot only as a reference for brand, colors and the template frame (dark navy, Wesco green, pale green band at the bottom, Arial, title top left, logo bottom left, confidentiality line bottom center).

1. One picture. A single J-curve of cumulative cash as the hero, with revenue as a quiet backdrop, the trough and the zero crossing called out.
2. A timeline. Five year markers left to right, the cash figure at each, a visual weight or depth showing the trough, with build / first sites / peak investment / break-even as labels on the years.
3. A waterfall. From the 2027 investment down through the trough and back up to the 2031 position, so the recovery reads as a sequence of steps.

Constraints
Short noun-phrase title only, no subtitle. No more than one sentence of text on the slide besides the title and the chart labels. Nothing decorative. Colorblind-safe: never rely on color alone to separate series. Keep the pale green band at the bottom for a one-line takeaway. The figures may be placeholders; what I am judging is which shape makes "build, invest, recover" obvious to someone who has never seen the model.

Output
Three slide mockups, and one sentence under each on what that layout makes easiest to see and what it hides.
```

---

## Prompt 2: the story test

**Attach:** `2026-09-30_CDA_Story_Test_Visuals_Only.pdf`. It is the full deck with body text, subtitles and takeaways removed. Only titles, cards with their labels, tables and charts remain.

```
Context
This is a 19-page internal Wesco business case for a managed service called Connected Device Assurance, with all the prose stripped out. What remains is each slide's title and whatever visual element it has: cards, tables, charts. I want to know whether the pictures alone carry the argument, and where they do not.

The argument the deck is supposed to make, in order
1. After a device sale, nobody owns the devices; that gap is where recurring revenue lives.
2. One service closes the gap: inventory, patch, secure, one annual fee per site.
3. Wesco already has the parts; this is assembly, not invention.
4. It strengthens three platforms we already fund.
5. Sellers quote by site size, not device counts.
6. A seller earns real money on it.
7. One site makes money.
8. The plan makes money, after a bounded investment.
9. Two teams have to be staffed for it.
10. Named accounts, not a market estimate, are what make it real.
11. The market is large and we need a small share of it.
12. Here is what is evidence and what is still an estimate.
13. Three things are needed, in order: a sponsor, anchor accounts, an AOP position.

Two audiences
A sales leader who has to decide whether to sponsor it and put it in front of his top accounts, and a VP who has to carry it into an annual operating plan and defend a small development investment.

Task
Read the deck as pictures only, in order, and tell me:
1. Which slides carry their point visually without the words, and which are just boxes with labels. Be blunt.
2. Where the visual sequence breaks: a step in the argument that has no picture, or a picture that says something different from its step.
3. For each slide that is only boxes, propose one visual that would carry the point: a diagram, a comparison, a before-and-after, a single number, a flow. Sketch it in a sentence, or mock it if it is quick.
4. Which three slides would benefit most from a redesigned visual, ranked, and why those three.

Constraints
Do not rewrite the argument. Do not add slides. Do not propose visuals that depend on data the deck does not show. Wesco style: dark navy, Wesco green for the thing Wesco gains, restrained, no decoration, Arial.

Output
A short written assessment organized by the four questions above, then mockups for the three slides you ranked highest.
```
