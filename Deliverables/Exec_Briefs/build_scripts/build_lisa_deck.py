#!/usr/bin/env python3
"""Wesco and Strev - brief for Lisa Orton.

Built ON the Wesco corporate template (master + 33 named layouts), taken from
Products/CDA/CDA_Exec_Brief_SHARE_2026-08-28.pptx. The master supplies the
Wesco logo at bottom left (0.57 / 6.50, 1.11 x 0.93) and the confidentiality
line, so neither is placed by hand and all content must clear T6.45.

Cover   -> layout "Title Slide_Dark"
Content -> layout "Blank-with-Title"

Sources: Revnue v2.5 (May 2026, superseded); Sunny Sharma call 2026-09-16;
Amy Aguirre / Lisa Orton thread 2026-09-15.
"""
from pptx import Presentation
from pptx.util import Inches as I, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

TEMPLATE = ("/mnt/user-data/uploads/Executive Operating System/Products/CDA/"
            "CDA_Exec_Brief_SHARE_2026-08-28.pptx")
OUT = "/mnt/user-data/outputs/2026-09-17_Lisa_Orton_Strev_Brief.pptx"
ASSETS = "/mnt/user-data/outputs/icons/"

GREEN     = RGBColor(0x00, 0xB1, 0x40)
GREEN_DK  = RGBColor(0x00, 0x95, 0x3A)
GREEN_TNT = RGBColor(0xE9, 0xF4, 0xEA)
GREEN_LT  = RGBColor(0xD8, 0xF0, 0xDE)
GREEN_PL  = RGBColor(0x8F, 0xE3, 0xA8)
DARK      = RGBColor(0x20, 0x26, 0x2C)
SLATE     = RGBColor(0x5B, 0x7A, 0x8E)
SLATE_DK  = RGBColor(0x46, 0x60, 0x6F)
GREY_LT   = RGBColor(0xEF, 0xF2, 0xF4)
GREY_MD   = RGBColor(0xC9, 0xD1, 0xD6)
GREY_TX   = RGBColor(0xE6, 0xEC, 0xEF)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
TEXT      = RGBColor(0x2B, 0x2B, 0x2B)
F_HEAD = "Titillium Web"    # theme major font
F_BODY = "Source Sans Pro"  # theme minor font
F = F_BODY                  # default

L0, CW = 0.73, 11.86          # template title-placeholder grid
FLOOR = 6.46                  # master logo zone starts at 6.50
COL4 = [0.73, 3.767, 6.804, 9.841]; CW4 = 2.75
COL3 = [0.73, 4.783, 8.836];        CW3 = 3.75
COL2 = [0.73, 6.825];               CW2 = 5.765

prs = Presentation(TEMPLATE)

sld_id_lst = prs.slides._sldIdLst
for sld in list(sld_id_lst):
    prs.part.drop_rel(sld.rId)
    sld_id_lst.remove(sld)

LAYOUT = {l.name: l for l in prs.slide_masters[0].slide_layouts}
LY_COVER = LAYOUT["Title Slide_Dark"]
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


def slide(title):
    """Content slide on Blank-with-Title. Logo, confidentiality line and slide
    number are inherited from the master. No subtitles."""
    s = prs.slides.add_slide(LY_BODY)
    ph = s.shapes.title
    ph.left, ph.top, ph.width, ph.height = I(L0), I(0.70), I(CW), I(0.50)
    tf = ph.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    r = p.add_run(); r.text = title
    r.font.name = F_HEAD; r.font.size = Pt(22); r.font.bold = True
    r.font.color.rgb = DARK
    return s


def band(s, t, txt, h=0.66, fill=GREEN_TNT, color=DARK, size=9.5):
    assert t + h <= FLOOR, "band %.2f+%.2f runs into the logo zone" % (t, h)
    rect(s, L0, t, CW, h, fill=fill)
    tb(s, L0 + 0.28, t + 0.09, CW - 0.56, h - 0.18, txt, size=size, color=color,
       anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.14, space_after=0)


def block(s, l, t, w, h, fill, lbl, lbl_color, body, body_color, size=11):
    rect(s, l, t, w, h, fill=fill)
    label(s, l + 0.26, t + 0.18, w - 0.52, lbl, color=lbl_color)
    tb(s, l + 0.26, t + 0.46, w - 0.52, h - 0.64, body, size=size,
       color=body_color, line_spacing=1.22, space_after=5)


def card(s, l, t, w, h, fill, head, head_color, body, body_color,
         head_size=10.5, body_size=8.8, line=None, chip=None, icon=None):
    rect(s, l, t, w, h, fill=fill, line=line, lw=1.0)
    y = t + 0.18
    if chip:
        rect(s, l + 0.22, y, 0.42, 0.42, fill=chip, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        if icon:
            s.shapes.add_picture(ASSETS + icon, I(l + 0.31), I(y + 0.09),
                                 I(0.24), I(0.24))
        y += 0.58
    tb(s, l + 0.22, y, w - 0.44, 0.48, head, size=head_size, color=head_color,
       bold=True, line_spacing=1.06, space_after=0, font=F_HEAD)
    y2 = y + 0.34
    tb(s, l + 0.22, y2, w - 0.44, h - (y2 - t) - 0.16, body, size=body_size,
       color=body_color, line_spacing=1.18, space_after=4)



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


fill_ph(12, "Status", 40, True, WHITE, font=F_HEAD)
fill_ph(16, "AI capabilities, site assessment, and what we recommend",
        14, False, GREY_TX)
fill_ph(1, "Darryl Benson  ·  Senior Director, CSS Platforms", 10.5, True, WHITE)
tb(s, 0.73, 5.58, 6.50, 0.22, "Prepared for Lisa Orton  ·  September 17, 2026",
   size=10.5, color=GREY_MD, line_spacing=1.0, space_after=0)

# =====================================================================
# 2 - WHERE THIS STANDS
# =====================================================================
s = slide("Where This Stands")

rect(s, L0, 1.34, CW, 1.30, fill=GREEN)
label(s, L0 + 0.28, 1.52, 4.0, "Product recommendation", color=GREEN_LT)
tb(s, L0 + 0.28, 1.80, CW - 0.56, 0.74,
   "**Enable the AI Feature Pack in Strev now.** Both capabilities the business needs are "
   "already inside it, and Strev's new model-key option removes the variable consumption "
   "cost. Potential overlap with IDP is a roadmap question, but should not stop the business "
   "from moving forward.",
   size=12, color=WHITE, line_spacing=1.24, space_after=0)

pairs = [
    ("AI capabilities",
     "The business requested **Smart Import** and **Data Enrichment**. Strev confirms both "
     "sit inside the AI Feature Pack at no incremental cost.\n"
     "The pack itself is not in the current agreement, and enabling AI in the Wesco instance "
     "needs to go through intake.\n"
     "This is what raised the build-versus-buy question against IDP."),
    ("Site assessment",
     "A separate capability the TS team has specified for remote site surveys, with asset "
     "records landing in Strev.\n"
     "**Not in production.** It has not been through intake, and the Strev integration has "
     "not been scoped.\n"
     "Whether the Strev side falls under the white-label agreement or is a separate "
     "arrangement with TS is not established."),
]
for i, (h, b) in enumerate(pairs):
    rect(s, COL2[i], 2.86, CW2, 2.24, fill=DARK)
    rect(s, COL2[i], 2.86, CW2, 0.05, fill=GREEN)
    tb(s, COL2[i] + 0.26, 3.06, CW2 - 0.52, 0.28, h, size=12.5, color=WHITE, bold=True,
       line_spacing=1.0, space_after=0, font=F_HEAD)
    tb(s, COL2[i] + 0.26, 3.38, CW2 - 0.52, 1.60, b, size=9.2, color=GREY_MD,
       line_spacing=1.18, space_after=5)

band(s, 5.62, h=0.78,
     txt="Both threads need the same two things from us: a revised agreement with Strev "
         "covering the AI features and pricing, and a clear path through Wesco intake.")

# =====================================================================
# 3 - AI IN STREV
# =====================================================================
s = slide("AI in Strev")

rect(s, COL2[0], 1.34, CW2, 1.72, fill=DARK)
label(s, COL2[0] + 0.26, 1.52, 4.0, "The request", color=GREY_MD)
tb(s, COL2[0] + 0.26, 1.80, CW2 - 0.52, 1.12,
   "**Smart Import** and **Data Enrichment**, for the workflow the business is building on "
   "the Strev platform.\n"
   "Strev's position is that both are enhancements inside the AI Feature Pack, carrying no "
   "incremental cost and no separate SKU.",
   size=10.5, color=WHITE, line_spacing=1.20, space_after=5)

rect(s, COL2[1], 1.34, CW2, 1.72, fill=GREEN)
label(s, COL2[1] + 0.26, 1.52, 4.0, "Why enable now", color=GREEN_LT)
tb(s, COL2[1] + 0.26, 1.80, CW2 - 0.52, 1.12,
   "The workflow is already built on Strev and the capability exists there today.\n"
   "IDP is not yet ready to support this work and will take development cycles that are not "
   "currently available.",
   size=10.5, color=WHITE, line_spacing=1.20, space_after=5)

rect(s, L0, 3.26, CW, 1.56, fill=GREY_LT)
label(s, L0 + 0.28, 3.44, 4.0, "Strev annual cost")
costs = [
    ("AI Feature Pack base license", "$84,000",
     "per environment, per year. Unchanged, and confirmed by Strev."),
    ("Per-tenant credits", "Removed",
     "if Wesco connects its own model subscription by API key. No credit pool, no overage."),
    ("Model consumption", "Wesco's own",
     "billed on agreements Wesco already holds, visible in Wesco's own reporting."),
]
for i, (lbl, val, note) in enumerate(costs):
    x = L0 + 0.28 + i * 3.86
    tb(s, x, 3.74, 3.58, 0.20, lbl, size=8.5, color=SLATE, line_spacing=1.0, space_after=0)
    tb(s, x, 3.96, 3.58, 0.30, val, size=17, color=DARK, bold=True,
       line_spacing=1.0, space_after=0, font=F_HEAD)
    tb(s, x, 4.32, 3.58, 0.42, note, size=8.5, color=TEXT, line_spacing=1.16, space_after=0)

band(s, 5.14, h=1.00,
     txt="The platform layer is already licensed: bulk import and update, OCR and ICR "
         "extraction, and the REST APIs all sit in the current agreement. The AI layer is "
         "what is missing, and the base license is the cost of adding it. Site assessment "
         "pricing is separate and has not been established.")

# =====================================================================
# 4 - SITE ASSESSMENT
# =====================================================================
s = slide("Site Assessment")

rect(s, COL2[0], 1.34, CW2, 2.06, fill=DARK)
label(s, COL2[0] + 0.26, 1.52, 4.0, "What TS specified", color=GREY_MD)
tb(s, COL2[0] + 0.26, 1.80, CW2 - 0.52, 1.46,
   "**Avatour with the PanoX V2 camera**, for live remote 360 site surveys of telecom rooms, "
   "IDFs, MDFs, data centres and equipment rooms on EaaS projects.\n"
   "Remote stakeholders join from a browser, look around independently, and capture "
   "snapshots of assets, serial numbers, rack layouts and labels.\n"
   "The intent is fewer site visits and better asset record accuracy.",
   size=9.8, color=GREY_TX, line_spacing=1.20, space_after=5)

rect(s, COL2[1], 1.34, CW2, 2.06, fill=GREEN)
label(s, COL2[1] + 0.26, 1.52, 4.0, "Where Strev fits", color=GREEN_LT)
tb(s, COL2[1] + 0.26, 1.80, CW2 - 0.52, 1.46,
   "**Strev is the asset management system of record.** Survey output creates or updates "
   "asset records: asset name and tag, serial number, manufacturer and model, "
   "building, floor, room and rack, notes and snapshot links.\n"
   "TS proposes Zapier first as a low-code proof of concept, then the Strev API if scale or "
   "security require it.",
   size=9.8, color=WHITE, line_spacing=1.20, space_after=5)

rect(s, L0, 3.60, CW, 1.54, fill=GREY_LT)
label(s, L0 + 0.28, 3.78, 4.0, "To close")
opens = [
    ("Intake", "Has not been through intake, so nothing is in production yet."),
    ("Strev integration", "TS records it as needing further research and development, and it "
                          "has not been scoped with Strev."),
    ("Pricing", "TS estimates $2,000 to $4,000 a year for one camera kit, but the Avatour "
                "rate it cites is $4,152 a year on its own. Zapier and the Strev integration "
                "are unpriced."),
]
for i, (lbl, note) in enumerate(opens):
    x = L0 + 0.28 + i * 3.86
    tb(s, x, 4.08, 3.58, 0.20, lbl, size=9.5, color=DARK, bold=True, line_spacing=1.0,
       space_after=0, font=F_HEAD)
    tb(s, x, 4.32, 3.58, 0.66, note, size=8.6, color=TEXT, line_spacing=1.16, space_after=0)

band(s, 5.46, h=0.94,
     txt="The capability is well specified on the Avatour side and the business case is "
         "clear. The cost is not. The estimate covers a single kit, three of its five line "
         "items carry no number, and the Strev commercial question is still open. A scale "
         "number is needed before this goes past a pilot.")

# =====================================================================
# 5 - NEXT STEPS
# =====================================================================
s = slide("Next Steps")

steps = [
    (DARK, "AI enablement", "UiPath",
     "Covers turning the AI Feature Pack on inside the Wesco-branded instance, including "
     "Smart Import and Data Enrichment."),
    (DARK, "Site assessment", "UiPath",
     "Covers the Avatour solution and the Strev integration the TS team needs to support "
     "it."),
    (GREEN, "With Strev", "Agreement and entitlements",
     "A current entitlement document, and a marked-up white-label agreement adding the AI "
     "features and pricing. Both agreed with Strev on September 16."),
]
for i, (fill, h, route, b) in enumerate(steps):
    rect(s, COL3[i], 1.34, CW3, 2.54, fill=fill)
    if fill == DARK:
        rect(s, COL3[i], 1.34, CW3, 0.05, fill=GREEN)
    tb(s, COL3[i] + 0.26, 1.58, CW3 - 0.52, 0.30, h, size=13, color=WHITE, bold=True,
       line_spacing=1.0, space_after=0, font=F_HEAD)
    tb(s, COL3[i] + 0.26, 1.96, CW3 - 0.52, 0.26, route, size=11,
       color=(WHITE if fill == GREEN else GREEN_PL), bold=True,
       line_spacing=1.0, space_after=0, font=F_HEAD)
    tb(s, COL3[i] + 0.26, 2.32, CW3 - 0.52, 1.40, b,
       size=10, color=(GREEN_LT if fill == GREEN else GREY_MD),
       line_spacing=1.22, space_after=7)

rect(s, L0, 4.28, CW, 1.20, fill=GREY_LT)
label(s, L0 + 0.28, 4.46, 4.0, "From Product")
tb(s, L0 + 0.28, 4.74, CW - 0.56, 0.58,
   "We will support both routes however Managed Services and the TS team need to run them. "
   "The one dependency worth noting is that the revised agreement and pricing updates need "
   "to happen alongside all of the other work.",
   size=10.5, color=TEXT, line_spacing=1.20, space_after=0)

prs.save(OUT)
print("saved:", OUT)
