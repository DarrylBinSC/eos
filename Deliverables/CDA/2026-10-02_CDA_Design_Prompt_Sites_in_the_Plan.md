# Claude Design prompt: Sites in the plan

**Attach:** a screenshot of slide 9, "Sites in the plan" (current native build).
Anything Design produces is a mockup to choose from. The chosen layout is rebuilt natively from the pro forma (v4.6, Deck Figures tab) so the numbers stay live.

```
Context
This is one slide from an internal Wesco business case for a managed service called Connected Device Assurance (CDA). Customers pay one annual fee per site. The slide sits between "One site" (what a single site earns: $15,700 a year for a Large site, $10,300 for a Medium site) and "Plan, 2027 to 2031" (five-year revenue and cumulative cash). Its job is to show the arithmetic between them: how many sites each anchor account brings, and when. The audience is a sales leader being asked to sponsor the product and a VP carrying it into an annual operating plan. The numbers are illustrative and will change, so I need layout ideas, not a finished graphic.

The attached slide works today. Each anchor account is a horizontal bar whose length is its sites in 2031. What it does not show is timing: accounts go live in different years and ramp over several years, and the Plan slide that follows is a timeline. I want the bars to take on a Gantt feel so the listener sees when sites come on, not only how many.

The data
Years run 2027 to 2031. 2027 is the build year: no sites, development only.
Installed sites by year (end of year):
- Kroger, retail, Large, named: 2028 143, 2029 286, 2030 429, 2031 429. 60,000 devices. $6.7M a year at full deployment.
- Cisco, corporate real estate, Medium, named: 2029 94, 2030 141, 2031 187. 14,960 devices. $1.9M a year.
- Pharma, Medium, still to name: 2029 50, 2030 85, 2031 120. 12,000 devices. $1.2M a year.
- Automotive, Medium, still to name: 2030 50, 2031 85. 8,500 devices. $0.9M a year.
- Third lane, Medium, still to name: 2031 50. 5,000 devices. $0.5M a year.
Total installed sites: 2028 143, 2029 430, 2030 705, 2031 871 (100,460 devices, shown rounded as 100,500 in the headline).
Total line that must stay on the slide: 429 Large sites x $15,700 + 442 Medium sites x $10,300 = $11.3M a year at full deployment.
Takeaway band: Kroger and Cisco are 77% of the run rate; the three anchors still to name are the rest.
Sites go live through the year, not on January 1.

The story the picture has to tell on its own
Two named accounts carry most of the plan and come on first; three accounts still to be named fill in later and are smaller. The total climbs year by year to 871 sites, which is why revenue on the next slide compounds.

Task
Give me three layouts for this one slide, side by side, using the attached screenshot as the reference for brand, colors and frame (dark navy, slate, Wesco green, pale green takeaway band at the bottom, Arial, title top left, logo bottom left, confidentiality line bottom center).

1. Gantt with ramp. Columns are the years 2027 to 2031. Each account is a bar that starts in its go-live year and runs to 2031, stepped or shaded so the sites installed each year are visible inside the bar (for example 143 / 286 / 429 for Kroger). Keep a way to compare account size: bar thickness proportional to 2031 sites, or a clear site count at the end of each bar.
2. Swimlanes by volume. Same year columns, but each account's lane grows in height as its sites ramp, so the slide reads as volume over time while keeping one lane per account.
3. Gantt plus totals. Concept 1, with a totals row under the year columns (143, 430, 705, 871 sites) that lines up with the year axis of the Plan slide that follows, so the two slides read as one sequence.

Constraints
- Named accounts must look visibly different from accounts still to name (today: solid navy versus dashed outline). Never imply the three placeholders are signed.
- Keep, for each account: name, vertical and size (Large or Medium), devices, and dollars a year at full deployment. They may move, but they must stay on the slide.
- Keep the total line and the takeaway band.
- 2027 is shown as the build year with no sites; do not leave it as an unexplained empty column.
- Color: green only for what Wesco gains, never for an ask or a placeholder. Colorblind-safe: never rely on color alone to separate named from to-name, or one year from the next.
- Short noun-phrase title only ("Sites in the plan"), one sentence of headline at most, nothing decorative.
- Readable from the back of a room: labels at least 10 pt equivalent.

Output
Three slide mockups, and one sentence under each on what that layout makes easiest to see and what it hides. Then say which one you would choose for a sales leader who has 30 seconds on this slide.
```

## Notes for Darryl (not for the designer)

- **The tradeoff to watch.** A Gantt bar's length means time, so it can no longer also mean size, which is what the current slide uses it for. Concepts 1 and 3 keep size through bar thickness or an end label; concept 2 makes size the height. Judge the mockups on whether Kroger still reads as the big account at a glance.
- **Why concept 3.** The totals row (143, 430, 705, 871) on the same year axis as the Plan chart makes slide 9 lead straight into slide 10: sites climb, so revenue climbs. That is the bridge you said the deck was missing.
- **Data source.** Sites by year are the Accounts tab, "Sites under contract" rows, v4.6. If the mockup is chosen, the native rebuild adds those rows to Deck Figures so the slide stays live.
