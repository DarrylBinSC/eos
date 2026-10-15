#!/usr/bin/env python3
"""CAT: Owning Layers 1 to 3. Companion deck to the Five Layer Model review.

Revised 2026-09-21: rebuilt on financial model v3. The operations interface (new PODs plus a
retained India product team) is now costed in every option beyond the vendor full stack, and
layer 1 to 3 engineering is charged at the 70/30 India/US split rather than a flat US rate.

Built ON the Wesco corporate template taken from the 2026-09-16 CAT deck, so
master, layouts, logo and confidentiality line are inherited. Helpers and grid
are carried over from Deliverables/Exec_Briefs/build_scripts/build_lisa_deck.py.

Audience: executive sponsor and Tom Mitchell. Cost model shown, labelled
illustrative. No subtitles, no dates assigned to Darryl.
"""
from pptx import Presentation
from pptx.util import Inches as I, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

TEMPLATE = ("/mnt/user-data/uploads/Executive Operating System/Deliverables/CAT/"
            "2026-09-16_CAT_Five_Layer_Model_Review.pptx")
OUT = "/mnt/user-data/outputs/2026-09-21_CAT_Layers_1_3_Independent_Execution.pptx"

GREEN     = RGBColor(0x00, 0xB1, 0x40)
GREEN_TNT = RGBColor(0xE9, 0xF4, 0xEA)
GREEN_LT  = RGBColor(0xD8, 0xF0, 0xDE)
GREEN_PL  = RGBColor(0x8F, 0xE3, 0xA8)
DARK      = RGBColor(0x20, 0x26, 0x2C)
SLATE     = RGBColor(0x5B, 0x7A, 0x8E)
GREY_LT   = RGBColor(0xEF, 0xF2, 0xF4)
GREY_MD   = RGBColor(0xC9, 0xD1, 0xD6)
GREY_TX   = RGBColor(0xE6, 0xEC, 0xEF)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
TEXT      = RGBColor(0x2B, 0x2B, 0x2B)
AMBER     = RGBColor(0xE8, 0x84, 0x2A)
F_HEAD = "Titillium Web"
F_BODY = "Source Sans Pro"

L0, CW = 0.73, 11.86
FLOOR = 6.46
COL4 = [0.73, 3.767, 6.804, 9.841]; CW4 = 2.75
COL3 = [0.73, 4.783, 8.836];        CW3 = 3.75
COL2 = [0.73, 6.825];               CW2 = 5.765

prs = Presentation(TEMPLATE)
sld_id_lst = prs.slides._sldIdLst
for sld in list(sld_id_lst):
    prs.part.drop_rel(sld.rId)
    sld_id_lst.remove(sld)

LAYOUT = {l.name: l for l in prs.slide_masters[0].slide_layouts}
LY_COVER = LAYOUT["Title Slide"]
LY_BODY = LAYOUT["Blank-with-Title"]


def rect(s, l, t, w, h, fill=None, line=None, lw=1.0, shape=MSO_SHAPE.RECTANGLE):
    sh = s.shapes.add_shape(shape, I(l), I(t), I(w), I(h))
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid(); sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line; sh.line.width = Pt(lw)
    sh.shadow.inherit = False
    return sh


def tb(s, l, t, w, h, txt, size=9.5, color=TEXT, bold=False, align=PP_ALIGN.LEFT,
       anchor=MSO_ANCHOR.TOP, space_after=3, line_spacing=1.14, font=None):
    box = s.shapes.add_textbox(I(l), I(t), I(w), I(h))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    for i, line in enumerate(txt.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space_after)
        p.line_spacing = line_spacing
        for j, seg in enumerate(line.split("**")):
            if seg == "":
                continue
            r = p.add_run(); r.text = seg
            r.font.name = font or F_BODY
            r.font.size = Pt(size)
            r.font.bold = (j % 2 == 1) or bold
            r.font.color.rgb = color
    return box


def label(s, l, t, w, txt, color=SLATE, size=8.5):
    return tb(s, l, t, w, 0.24, txt.upper(), size=size, color=color, bold=True,
              line_spacing=1.0, space_after=0)


def slide(title, notes=None):
    s = prs.slides.add_slide(LY_BODY)
    ph = s.shapes.title
    ph.left, ph.top, ph.width, ph.height = I(L0), I(0.70), I(CW), I(0.50)
    tf = ph.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run(); r.text = title
    r.font.name = F_HEAD; r.font.size = Pt(22); r.font.bold = True
    r.font.color.rgb = DARK
    if notes:
        s.notes_slide.notes_text_frame.text = notes
    return s


def band(s, t, txt, h=0.66, fill=GREEN_TNT, color=DARK, size=9.5):
    assert t + h <= FLOOR, "band %.2f+%.2f runs into the logo zone" % (t, h)
    rect(s, L0, t, CW, h, fill=fill)
    tb(s, L0 + 0.28, t + 0.09, CW - 0.56, h - 0.18, txt, size=size, color=color,
       anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.16, space_after=0)


def darkcard(s, l, t, w, h, head, body, accent=GREEN, head_size=12.5,
             body_size=9.2, body_color=GREY_MD, head_h=0.56):
    rect(s, l, t, w, h, fill=DARK)
    rect(s, l, t, w, 0.05, fill=accent)
    tb(s, l + 0.26, t + 0.22, w - 0.52, head_h, head, size=head_size, color=WHITE,
       bold=True, line_spacing=1.02, space_after=0, font=F_HEAD)
    body_t = t + 0.22 + head_h + 0.10
    tb(s, l + 0.26, body_t, w - 0.52, h - (body_t - t) - 0.18, body, size=body_size,
       color=body_color, line_spacing=1.20, space_after=5)


# =====================================================================
# 1 - COVER
# =====================================================================
s = prs.slides.add_slide(LY_COVER)
by_idx = {p.placeholder_format.idx: p for p in s.placeholders}


def fill_ph(idx, text, size, bold, color, font=None):
    if idx not in by_idx:
        return
    tf = by_idx[idx].text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run(); r.text = text
    r.font.name = font or F_BODY; r.font.size = Pt(size); r.font.bold = bold
    r.font.color.rgb = color


fill_ph(12, "Owning Layers 1 to 3", 40, True, DARK, font=F_HEAD)
fill_ph(16, "Connected Asset Tracking: what independent execution would take",
        14, False, SLATE)
fill_ph(1, "Darryl Benson  ·  Senior Director, CSS Platforms", 10.5, True, DARK)
tb(s, 0.73, 5.58, 7.20, 0.22,
   "Companion to the Five Layer Model review  ·  September 21, 2026",
   size=10.5, color=SLATE, line_spacing=1.0, space_after=0)
s.notes_slide.notes_text_frame.text = (
    "Companion deck to the 16 September five layer review, revised on 21 September. That deck "
    "established the frame: layer 4 is built, layer 5 needs new PODs, and layers 1 to 3 are "
    "entirely vendor supplied. This one answers "
    "the next question, which is what it would actually take for Wesco to own layers 1 to 3 "
    "without a partner. It still does not recommend an option. It does put a number on the "
    "one that has been assumed to be cheaper.")

# =====================================================================
# 2 - WHERE THIS LANDS
# =====================================================================
s = slide("Where This Lands", notes=(
    "Three findings, and the third is the one to act on. Independent execution is real but it "
    "is an assembly plus an operation, not a build. The cost comparison turns almost entirely "
    "on whether internal labor is counted, which is why two credible people can look at the "
    "same stack and reach opposite conclusions. The labor is no longer only the layer 1 to 3 "
    "engineering: every option except staying on the vendor's own application needs new PODs "
    "for the operations team and a team retained to maintain them. And the fastest route to a "
    "defensible answer is a price, not a design. Say plainly that none of this argues with "
    "the build direction."))

rect(s, L0, 1.34, CW, 1.12, fill=GREEN)
label(s, L0 + 0.28, 1.50, 5.0, "The finding", color=GREEN_LT)
tb(s, L0 + 0.28, 1.76, CW - 0.56, 0.60,
   "**Independent execution is an assembly plus an operation, not a build.** Nothing at layers "
   "1 to 3 has to be engineered from first principles. The open question is not whether Wesco "
   "can build it, it is whether Wesco should own the operation that comes with it.",
   size=11.5, color=WHITE, line_spacing=1.22, space_after=0)

cards = [
    ("The cost turns on labor",
     "Five year total is **$1.5M** if internal labor is treated as free and **$4.7M** once the "
     "product team, the engineering and the operation are costed.\nThe declined subscription is "
     "below both, at **$2.5M**."),
    ("Break-even is near 25,000 assets",
     "Below that, owning layers 1 to 3 costs more than renting them, because the fixed cost of "
     "the build and the operation is spread over too few assets.\nThe inferred fleet is "
     "**8,300**."),
    ("The fastest answer is a price",
     "An unbundled price for data access with layers 1 to 3 retained settles this faster than "
     "any technical work.\nBelow roughly **$3.00** per tracker per month it beats the "
     "subscription, with our product team counted."),
]
for i, (h, b) in enumerate(cards):
    darkcard(s, COL3[i], 2.66, CW3, 2.20, h, b)

band(s, 5.06, h=0.92,
     txt="None of this argues with the build direction. It argues with testing that direction "
         "against an application estimate instead of against the five year cost of owning "
         "three layers and the operation that keeps them running.")

# =====================================================================
# 3 - PARTNER OR SUPPLIER
# =====================================================================
s = slide("Partner Or Supplier", notes=(
    "This distinction is doing a lot of work and it is worth slowing down on. The instruction "
    "was to stop renting someone else's software. That is satisfiable without pretending Wesco "
    "will make its own trackers. A partner owns a layer of the capability. A supplier sells a "
    "component into a capability we own. Every option on the table buys hardware from someone. "
    "The difference is whether that someone also owns the product."))

rect(s, COL2[0], 1.34, CW2, 1.96, fill=DARK)
rect(s, COL2[0], 1.34, CW2, 0.05, fill=AMBER)
label(s, COL2[0] + 0.26, 1.56, 4.0, "Partner", color=GREY_MD)
tb(s, COL2[0] + 0.26, 1.86, CW2 - 0.52, 1.30,
   "Owns a layer of the capability and the customer relationship that goes with it.\n"
   "Replacing the partner means replacing the product. The data model, the roadmap and the "
   "exit terms are theirs.\n"
   "**This is the declined Sensolus model.**",
   size=10.2, color=GREY_TX, line_spacing=1.20, space_after=5)

rect(s, COL2[1], 1.34, CW2, 1.96, fill=GREEN)
label(s, COL2[1] + 0.26, 1.56, 4.0, "Supplier", color=GREEN_LT)
tb(s, COL2[1] + 0.26, 1.86, CW2 - 0.52, 1.30,
   "Sells a component into a capability Wesco owns.\n"
   "Replaceable without replacing the product. Certified devices, a SIM contract, a metered "
   "positioning service.\n"
   "**This is what independent execution actually looks like.**",
   size=10.2, color=WHITE, line_spacing=1.20, space_after=5)

rect(s, L0, 3.52, CW, 1.36, fill=GREY_LT)
label(s, L0 + 0.28, 3.70, 6.0, "Bought from someone in every option")
buys = [
    ("The tracker itself", "A certified device. Wesco has no reason to make one."),
    ("The network", "A carrier or an IoT MVNO carries the message."),
    ("Position and device services", "Metered infrastructure, not a build."),
]
for i, (h, b) in enumerate(buys):
    x = L0 + 0.28 + i * 3.86
    tb(s, x, 3.98, 3.58, 0.22, h, size=10.5, color=DARK, bold=True, line_spacing=1.0,
       space_after=0, font=F_HEAD)
    tb(s, x, 4.24, 3.58, 0.50, b, size=9.0, color=TEXT, line_spacing=1.16, space_after=0)

band(s, 5.10, h=0.90,
     txt="Wesco can execute this without a partner. It cannot execute it without suppliers, "
         "and an estimate built on the assumption that it can will not survive contact with a "
         "certification lab or a carrier.")

# =====================================================================
# 4 - WHAT THE THREE LAYERS CONTAIN
# =====================================================================
s = slide("What The Three Layers Contain", notes=(
    "The five layer model named the layers. This page inventories them, because the estimate "
    "lives in the inventory rather than in the names. Read the risk line at the bottom of each "
    "column. Layer 1 risk is loss rate, layer 2 risk is administrative, layer 3 risk is the "
    "physics of battery life and an operating obligation we do not have today."))

layers = [
    ("1", "Device",
     "The tracker, its radio, GNSS, battery, enclosure, mounting and certification.\n"
     "**Bought, not built.** The merchant market is mature and already certified for North "
     "American carriers.\n"
     "Custom hardware adds $20,000 to $30,000 per variant in certification alone, plus twelve "
     "to eighteen months."),
    ("2", "Connectivity",
     "The subscription that carries the message, plus SIM lifecycle, activation, suspension "
     "and billing reconciliation.\n"
     "**LTE-M is the North American answer.** AT&T has exited NB-IoT and migrated customers to "
     "LTE-M.\n"
     "Published benchmark is about $1.40 per device per year. This layer is cheap to own and "
     "easy to leave."),
    ("3", "Device services",
     "Position solving and assistance data, firmware, configuration, diagnostics, remote "
     "commands, and the support behind them.\n"
     "**Buyable as metered infrastructure** from four credible categories of supplier.\n"
     "Also where battery life is set: take devices off the cloud that solves their positions "
     "and the published battery figures do not travel with them."),
]
for i, (num, name, body) in enumerate(layers):
    rect(s, COL3[i], 1.34, CW3, 3.16, fill=GREY_LT)
    rect(s, COL3[i] + 0.26, 1.54, 0.40, 0.40, fill=DARK,
         shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    tb(s, COL3[i] + 0.26, 1.63, 0.40, 0.24, num, size=13, color=WHITE, bold=True,
       align=PP_ALIGN.CENTER, line_spacing=1.0, space_after=0, font=F_HEAD)
    tb(s, COL3[i] + 0.76, 1.61, CW3 - 1.02, 0.28, name, size=13.5, color=DARK, bold=True,
       line_spacing=1.0, space_after=0, font=F_HEAD)
    tb(s, COL3[i] + 0.26, 2.12, CW3 - 0.52, 2.24, body, size=9.0, color=TEXT,
       line_spacing=1.20, space_after=6)

rect(s, L0, 4.70, CW, 0.52, fill=DARK)
tb(s, L0 + 0.28, 4.79, CW - 0.56, 0.34,
   "**Wesco owns none of these three today.** Layer 4, the data plane, is built and running. "
   "Layer 5, the interface the operations team works in, is new PODs and a team to keep them.",
   size=10.5, color=WHITE, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.0, space_after=0)

band(s, 5.42, h=0.86,
     txt="Layer 3 is where the monthly fee goes and where the operating burden would transfer "
         "to us. It is the layer that does not appear anywhere in an application estimate.")

# =====================================================================
# 5 - WHO SELLS WHAT
# =====================================================================
s = slide("Who Sells What", notes=(
    "The market map, organised by layer, because most of these companies describe themselves "
    "as end to end and only two or three of them are. The practical reading is in the right "
    "hand column: the only place Wesco is genuinely absent is device services, and device "
    "services is purchasable in pieces. What no one in this table sells is the operating "
    "function."))

rows = [
    ("Full solution vendors", "Sensolus, Alesea, Samsara, Tive, Roambee",
     "Everything for one fee. What you give up is unbundled economics and control of the data model", DARK),
    ("Merchant device makers", "Digital Matter, Queclink, Teltonika, Abeeway, Lansitec",
     "Certified devices, optional device management and location engine, data routed to your platform", None),
    ("Connectivity", "1NCE, Soracom, KORE, Aeris, EMnify, Eseye; carriers direct; Skylo for satellite",
     "The bearer and the SIM estate. Nothing above it", None),
    ("Device services", "Nordic nRF Cloud, AWS IoT, Azure, AVSystem, IoTerop, Golioth, Memfault",
     "Positioning, firmware, diagnostics and observability, metered. The layer Wesco lacks", GREEN),
    ("Platform and application", "Wesco: entroCIM, SkySpark, ADM, DDP",
     "Built, running and integrated. Nothing missing that this decision depends on", None),
]
y = 1.34
for name, who, gives, accent in rows:
    h = 0.80
    fill = GREY_LT if accent is None else accent
    txt_main = WHITE if accent else DARK
    txt_sub = GREY_MD if accent else TEXT
    rect(s, L0, y, CW, h, fill=fill)
    tb(s, L0 + 0.28, y + 0.08, 2.70, h - 0.16, name, size=10.5, color=txt_main, bold=True,
       line_spacing=1.08, space_after=0, font=F_HEAD, anchor=MSO_ANCHOR.MIDDLE)
    tb(s, L0 + 3.10, y + 0.08, 3.90, h - 0.16, who, size=9.0, color=txt_sub,
       line_spacing=1.16, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
    tb(s, L0 + 7.20, y + 0.08, 4.38, h - 0.16, gives, size=9.0, color=txt_sub,
       line_spacing=1.16, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
    y += h + 0.10

band(s, 5.84, h=0.56,
     txt="No supplier in this table sells the operating function. That part is staffed, not "
         "purchased.")

# =====================================================================
# 6 - THE GAP
# =====================================================================
s = slide("The Gap", notes=(
    "Stated as capability rather than technology, because the technology is all purchasable. "
    "Two of the three concentrations can be engineered away: avoid custom hardware and the "
    "certification gap disappears, contract connectivity and that gap closes in weeks. The "
    "third one cannot be avoided, only staffed. It is also the line most likely to be cut in "
    "a funding conversation, and cutting it is how these programmes fail quietly."))

gaps = [
    ("Avoidable", "Device engineering and certification",
     "Embedded firmware, RF and antenna work, regulatory and carrier approval.\n"
     "**Avoid it by buying certified devices.** No requirement identified so far forces "
     "custom hardware.", GREEN),
    ("Closable", "Connectivity administration",
     "Contract, activation and suspension, billing reconciliation, usage alarms, SIM "
     "lifecycle.\n**Four to eight weeks** and an assigned administrator.", SLATE),
    ("Permanent", "Fleet operations",
     "Daily exception list, batteries, damaged and lost devices, spares, RMA, escalation when "
     "a customer site goes dark.\n**Three to six months to stand up, then ongoing. Unowned "
     "and unfunded today.**", AMBER),
]
for i, (tag, head, body, accent) in enumerate(gaps):
    rect(s, COL3[i], 1.34, CW3, 2.42, fill=DARK)
    rect(s, COL3[i], 1.34, CW3, 0.05, fill=accent)
    label(s, COL3[i] + 0.26, 1.56, 3.2, tag, color=accent)
    tb(s, COL3[i] + 0.26, 1.84, CW3 - 0.52, 0.56, head, size=13, color=WHITE, bold=True,
       line_spacing=1.04, space_after=0, font=F_HEAD)
    tb(s, COL3[i] + 0.26, 2.46, CW3 - 0.52, 1.18, body, size=9.2, color=GREY_MD,
       line_spacing=1.20, space_after=5)

rect(s, L0, 4.00, CW, 1.42, fill=GREY_LT)
label(s, L0 + 0.28, 4.18, 6.0, "Also to be closed, and none of it is exotic")
items = [
    "Positioning service contract and integration",
    "Device management and firmware platform",
    "Secure ingest, device identity and key custody",
    "Mobile asset modelling in SkySpark and Haystack",
    "Provisioning bench and a tested device pool",
    "Commissioning, unbinding and one system of record",
    "Spares, reverse logistics and replacement stock",
    "Governance: one owner, one funding route",
]
for i, it in enumerate(items):
    x = L0 + 0.28 + (i % 4) * 2.90
    yy = 4.48 + (i // 4) * 0.40
    tb(s, x, yy, 2.72, 0.34, it, size=8.8, color=TEXT, line_spacing=1.12, space_after=0)

band(s, 5.56, h=0.84,
     txt="Only one of these gaps is permanent, and it is the one with no owner and no budget "
         "line. Governance is the item that is blocking today and it is not a technical task.")

# =====================================================================
# 7 - WHAT IT COSTS
# =====================================================================
s = slide("What It Costs", notes=(
    "Say the caveat before the numbers, not after. This is an illustrative model on stated "
    "assumptions, built to be argued with. The point is not the precision, it is the shape: "
    "the vendor number sits between the two versions of the build number, and the difference "
    "between those two versions is people. Anyone who wants to defend the build case has to "
    "defend a fourth column that is not on this page: self-assembly with every internal "
    "person treated as free, which reads $1.5M. The India rate is what makes the middle "
    "column close; the operation is what makes the right hand one far away."))

totals = [
    ("Vendor full stack", "$2.5M", "The declined baseline. Hardware, connectivity, positioning, "
     "device management, support, replacement and their application in one fee.", GREEN, WHITE),
    ("Vendor data, our PODs", "$2.7M", "Their layers 1 to 3 at the placeholder data price, plus "
     "the PODs build and the team retained to maintain them.", SLATE, WHITE),
    ("Self-assembled", "$4.7M", "Labor costed. Adds the layer 1 to 3 build, sustaining "
     "engineering and a fleet operations team.", DARK, AMBER),
]
for i, (lbl, val, note, fill, valcolor) in enumerate(totals):
    rect(s, COL3[i], 1.34, CW3, 1.96, fill=fill)
    label(s, COL3[i] + 0.26, 1.54, 3.2, lbl,
          color=(GREEN_LT if fill == GREEN else GREY_MD))
    tb(s, COL3[i] + 0.26, 1.82, CW3 - 0.52, 0.62, val, size=40, color=valcolor, bold=True,
       line_spacing=1.0, space_after=0, font=F_HEAD)
    tb(s, COL3[i] + 0.26, 2.52, CW3 - 0.52, 0.66, note, size=9.0,
       color=(WHITE if fill == GREEN else GREY_MD), line_spacing=1.18, space_after=0)

tb(s, L0, 3.44, CW, 0.24,
   "Five year total cost of ownership at the inferred fleet of 8,300 assets. Exclude internal "
   "labor entirely, which is the build thesis view, and self-assembly reads $1.5M",
   size=9.5, color=SLATE, line_spacing=1.0, space_after=0)

rect(s, L0, 3.78, CW, 1.44, fill=GREY_LT)
label(s, L0 + 0.28, 3.96, 6.0, "What the model assumes")
params = [
    ("Fleet", "8,300 assets, inferred from $500,000 a year at $5 a month. Not counted."),
    ("Device", "$90 at volume, five year life, 8 percent lost or damaged a year."),
    ("Running cost", "$1.40 a year connectivity, $6 a year device services, per device."),
    ("People", "Seven India developers for the PODs, half retained after; four to build layers "
     "1 to 3, then 1.5 engineering and 2.0 operations."),
]
for i, (h, b) in enumerate(params):
    x = L0 + 0.28 + i * 2.90
    tb(s, x, 4.24, 2.72, 0.22, h, size=10, color=DARK, bold=True, line_spacing=1.0,
       space_after=0, font=F_HEAD)
    tb(s, x, 4.48, 2.72, 0.60, b, size=8.6, color=TEXT, line_spacing=1.14, space_after=0)

band(s, 5.38, h=0.92, fill=RGBColor(0xFD, 0xF1, 0xE5),
     txt="**Illustrative model on stated assumptions. No line in it is a Wesco quote.** It "
         "should be rebuilt on the counted asset baseline and written vendor pricing before "
         "it informs a decision.")

# =====================================================================
# 8 - WHERE BREAK-EVEN SITS
# =====================================================================
s = slide("Where Break-even Sits", notes=(
    "This is the page that turns the model into a decision rule. Per asset per year, the "
    "vendor charges sixty dollars for everything. Self-assembling the same thing costs about "
    "thirty-three in devices, connectivity and services, which leaves twenty-seven a year per "
    "asset to cover the people. Divide the fixed cost by that margin and you get the fleet "
    "size at which owning it starts to pay. Counting the build, it is about twenty-five "
    "thousand assets; once built, the run rate alone breaks even near eighteen and a half "
    "thousand. Even the most generous version, which assumes the layer 1 to 3 engineering is "
    "absorbed, lands near fourteen thousand, still well above the inferred fleet."))

steps = [
    ("$60", "Vendor cost", "Per asset per year, all in, replacement included", GREEN),
    ("$33", "Self-assembled variable cost", "Device amortisation and replacement, connectivity, device services", SLATE),
    ("$27", "Left to cover people", "The margin available per asset per year", DARK),
]
for i, (val, head, note, fill) in enumerate(steps):
    rect(s, COL3[i], 1.34, CW3, 1.52, fill=fill)
    tb(s, COL3[i] + 0.26, 1.52, 1.40, 0.52, val, size=32, color=WHITE, bold=True,
       line_spacing=1.0, space_after=0, font=F_HEAD)
    tb(s, COL3[i] + 0.26, 2.08, CW3 - 0.52, 0.24, head, size=10.5, color=WHITE, bold=True,
       line_spacing=1.0, space_after=0, font=F_HEAD)
    tb(s, COL3[i] + 0.26, 2.34, CW3 - 0.52, 0.40, note, size=8.6,
       color=(WHITE if fill == GREEN else GREY_MD), line_spacing=1.14, space_after=0)

rect(s, L0, 3.10, CW, 1.60, fill=GREY_LT)
label(s, L0 + 0.28, 3.28, 6.0, "Fixed cost divided by that margin")
tb(s, L0 + 0.28, 3.56, 5.60, 0.62, "25,000", size=42, color=DARK, bold=True,
   line_spacing=1.0, space_after=0, font=F_HEAD)
tb(s, L0 + 0.28, 4.22, 5.60, 0.34,
   "assets before owning layers 1 to 3 beats renting them, counting the build. Once built, "
   "the run rate alone breaks even near 18,500",
   size=9.2, color=TEXT, line_spacing=1.16, space_after=0)
tb(s, L0 + 6.30, 3.56, 5.28, 0.30,
   "**8,300 assets is the inferred fleet.**", size=11, color=DARK,
   line_spacing=1.0, space_after=0)
tb(s, L0 + 6.30, 3.88, 5.28, 0.70,
   "Treat the layer 1 to 3 engineering as absorbed and count only the operations staff and "
   "the retained product team, and break-even is still about 14,000.\n"
   "The fleet count is not a denominator for the model. It is the decision.",
   size=9.2, color=TEXT, line_spacing=1.18, space_after=5)

band(s, 5.00, h=0.90,
     txt="This is why the asset baseline is the gating item. Every other number in the model "
         "can be improved with a quote. This one can only be established by counting.")

# =====================================================================
# 9 - HOW LONG IT TAKES
# =====================================================================
s = slide("How Long It Takes", notes=(
    "Time is the argument that usually gets skipped. Option 1 is not a plan, it is a working "
    "integration whose interface is eight months of POD work, not a year of stack building. "
    "The independent path is a year before a production deployment, and "
    "the long pole is not engineering, it is recruiting and standing up the operations "
    "function. Adding engineers does not compress it."))

tl = [
    ("8 months", "Vendor data, our PODs",
     "The connector is built and syncing, so layer 4 is delivered. The operations interface is "
     "not: new PODs at CDA-scale effort, then the team stays to maintain them.", GREEN),
    ("4 to 7 months", "Device maker plus our platform",
     "Buy devices, keep their device management and location engine, own connectivity and the "
     "platform. Removes the layer 3 build and most of its risk. The PODs run in parallel and "
     "set the floor at eight months.", SLATE),
    ("9 to 15 months", "Wesco-owned stack",
     "Certified devices, bought device services, our ingest and tooling, plus three to six "
     "months to stand up fleet operations in parallel.", DARK),
    ("Add 12 to 18", "Custom hardware",
     "Design, certification and a first production run. Not recommended, and no requirement "
     "identified so far forces it.", AMBER),
]
y = 1.34
RH = 0.94
for dur, head, body, accent in tl:
    rect(s, L0, y, CW, RH, fill=GREY_LT)
    rect(s, L0, y, 0.06, RH, fill=accent)
    tb(s, L0 + 0.34, y + 0.08, 2.10, RH - 0.16, dur, size=14, color=accent, bold=True,
       line_spacing=1.0, space_after=0, font=F_HEAD, anchor=MSO_ANCHOR.MIDDLE)
    tb(s, L0 + 2.60, y + 0.08, 3.10, RH - 0.16, head, size=11, color=DARK, bold=True,
       line_spacing=1.08, space_after=0, font=F_HEAD, anchor=MSO_ANCHOR.MIDDLE)
    tb(s, L0 + 6.00, y + 0.08, 5.58, RH - 0.16, body, size=9.0, color=TEXT,
       line_spacing=1.16, space_after=0, anchor=MSO_ANCHOR.MIDDLE)
    y += RH + 0.12

band(s, 5.60, h=0.70, size=9.5,
     txt="The longest pole in the independent path is staffing the operation, not writing the "
         "software.")

# =====================================================================
# 10 - WHAT THE MARKET TIMING SAYS
# =====================================================================
s = slide("What The Market Timing Says", notes=(
    "Three things changed in the last eighteen months and they cut both ways. The components "
    "of an independent stack are cheaper, better standardised and more available than they "
    "were, which strengthens the case for owning the capability. The same maturity is the "
    "reason building those components yourself would be a poor use of capital."))

trends = [
    ("Radio settled", "AT&T exited NB-IoT",
     "AT&T stopped certifying NB-IoT devices and moved customers to LTE-M. Verizon and T-Mobile "
     "are holding NB-IoT for now.\n**LTE-M is the North American answer for assets that "
     "travel**, and the technology risk in that choice is gone."),
    ("Lock-in eased", "SGP.32 is commercially available",
     "The GSMA remote SIM standard built for IoT reached commercial availability in July 2026.\n"
     "**One hardware build can change carrier profile in the field.** Breadth still depends on "
     "which operators have integrated."),
    ("Services matured", "Device services became purchasable",
     "Positioning, firmware and observability are now metered infrastructure. Nordic acquired "
     "Memfault in June 2025 and folded observability and over-the-air update into its cloud.\n"
     "**The hard layer is now a contract, not a project.**"),
]
for i, (tag, head, body) in enumerate(trends):
    rect(s, COL3[i], 1.34, CW3, 2.76, fill=GREY_LT)
    label(s, COL3[i] + 0.26, 1.54, 3.2, tag, color=GREEN)
    tb(s, COL3[i] + 0.26, 1.82, CW3 - 0.52, 0.56, head, size=12.5, color=DARK, bold=True,
       line_spacing=1.04, space_after=0, font=F_HEAD)
    tb(s, COL3[i] + 0.26, 2.44, CW3 - 0.52, 1.52, body, size=9.4, color=TEXT,
       line_spacing=1.20, space_after=6)

band(s, 4.36, h=1.04,
     txt="The same maturity that makes owning the capability more plausible is what makes "
         "building the components a poor use of capital. Buy the parts, own the product, staff "
         "the operation.")

# =====================================================================
# 11 - WHAT DECIDES IT
# =====================================================================
s = slide("What Decides It", notes=(
    "Close on two asks and one warning. The two asks are the counted fleet and a written "
    "unbundled price, and neither of them sits with this team, which is why sponsorship is "
    "what we need from this conversation. The gating technical question belongs early in the "
    "vendor session rather than at the end of it, because a fixed endpoint removes every "
    "direct ingest option regardless of price. The last line is the honest one: on internal "
    "savings alone, at the fleet size currently assumed, this does not pay back."))

asks = [
    ("Ask one", "A written unbundled price",
     "What does Sensolus charge for data access with layers 1 to 3 retained? Below roughly "
     "$3.00 per tracker per month it beats the declined subscription even with our product "
     "team counted, and the remaining question is contractual rather than architectural."),
    ("Ask two", "A counted asset baseline",
     "How many returnable assets, of which classes, going where, and what do we lose and "
     "replace today? Break-even is a fleet size question and the fleet has never been "
     "counted."),
]
for i, (tag, head, body) in enumerate(asks):
    rect(s, COL2[i], 1.34, CW2, 1.86, fill=GREEN if i == 0 else DARK)
    label(s, COL2[i] + 0.26, 1.54, 3.2, tag, color=GREEN_LT if i == 0 else GREY_MD)
    tb(s, COL2[i] + 0.26, 1.82, CW2 - 0.52, 0.30, head, size=13, color=WHITE, bold=True,
       line_spacing=1.0, space_after=0, font=F_HEAD)
    tb(s, COL2[i] + 0.26, 2.20, CW2 - 0.52, 0.86, body, size=9.5,
       color=WHITE if i == 0 else GREY_MD, line_spacing=1.20, space_after=0)

rect(s, L0, 3.42, CW, 1.12, fill=GREY_LT)
label(s, L0 + 0.28, 3.60, 8.0, "Ask this early in the vendor session, not at the end")
tb(s, L0 + 0.28, 3.88, CW - 0.56, 0.54,
   "**Is the device endpoint configurable by the device owner, and is the payload "
   "specification available to customers?** If the endpoint is fixed to vendor "
   "infrastructure, every direct ingest option is unavailable regardless of price, and the "
   "decision reduces to taking their data or buying different hardware.",
   size=10, color=TEXT, line_spacing=1.20, space_after=0)

rect(s, L0, 4.74, CW, 1.10, fill=DARK)
tb(s, L0 + 0.28, 4.94, CW - 0.56, 0.74,
   "**On internal savings alone, at the fleet size currently assumed, this does not pay "
   "back.** If it is worth doing, it is more likely worth doing as a product decision with "
   "Wesco as customer zero, and it should be argued that way rather than defended on a saving "
   "the model does not support.",
   size=10.5, color=WHITE, line_spacing=1.22, space_after=0)

prs.save(OUT)
print("saved:", OUT, "slides:", len(prs.slides.__iter__.__self__._sldIdLst))
