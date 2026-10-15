"""CAT five-year financial model, v3.1 (2026-09-21).

v3.1: Sensolus Connect offered (API access to all data, vendor front end removed from the cost). That is Option 1's
scope. Price not yet given, so the Sensitivity sheet now carries a price-point table that reads the answer off
directly once it lands.

v3 changes (Darryl, 2026-09-21): POD team is all India at $22/hour and fractional for CAT, full effort during the
build and half retained afterwards; layer 1-3 engineering is split 70% India / 30% US operations at the AOP rates
rather than a flat US loaded cost.

v2 changes: Wesco product team (CDA-scale POD build, same team retained to maintain and enhance) added to every
option beyond Option 0; Year 0 build period with time-zero NPV; device and SIM refresh driven by life and term;
scenario engine for tornado and fleet sensitivities; input validation and sheet protection; break-evens rounded up
and stated on three bases. Regenerate after G1/G2/G4 inputs land.
"""
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, Protection
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter as CL

OUT = sys.argv[1] if len(sys.argv) > 1 else "CAT_Financial_Model.xlsx"
F = "Arial"
BLUE = Font(name=F, size=10, color="0000FF")
BLACK = Font(name=F, size=10)
GREEN = Font(name=F, size=10, color="008000")
GREENB = Font(name=F, size=10, color="008000", bold=True)
BOLD = Font(name=F, size=10, bold=True)
H1 = Font(name=F, size=14, bold=True, color="1F2A36")
H2 = Font(name=F, size=11, bold=True, color="1F2A36")
MUTED = Font(name=F, size=9, italic=True, color="595959")
HDR = Font(name=F, size=10, bold=True, color="FFFFFF")
HDRFILL = PatternFill("solid", fgColor="46596B")
YEL = PatternFill("solid", fgColor="FFFF00")
TOT = PatternFill("solid", fgColor="EEF1F4")
TOPB = Border(top=Side(style="thin", color="1F2A36"))
USD = '$#,##0;($#,##0);"-"'
USD2 = '$#,##0.00;($#,##0.00);"-"'
PCT = '0.0%;(0.0%);"-"'
NUM = '#,##0;(#,##0);"-"'
NUM2 = '#,##0.00;(#,##0.00);"-"'
MULT = '0.00"x"'
WRAP = Alignment(wrap_text=True, vertical="top")
WRAPC = Alignment(wrap_text=True, vertical="center")
UNLOCK = Protection(locked=False)
ENGINE_SHEET = "Engine"

wb = Workbook()
unlocked_cells = []  # (ws, coord)


def hdr(ws, row, labels, col=1):
    for i, l in enumerate(labels):
        c = ws.cell(row=row, column=col + i, value=l)
        c.font = HDR; c.fill = HDRFILL
        c.alignment = Alignment(horizontal="center" if i else "left", vertical="center", wrap_text=True)


def setw(ws, widths):
    for k, v in widths.items():
        ws.column_dimensions[k].width = v


def note(ws, cell, text, merge_to=None, height=None):
    ws[cell] = text; ws[cell].font = MUTED; ws[cell].alignment = WRAP
    if merge_to: ws.merge_cells(f"{cell}:{merge_to}")
    if height: ws.row_dimensions[ws[cell].row].height = height


def inp_cell(ws, coord, val, fmt, fill=None):
    c = ws[coord]; c.value = val; c.font = BLUE; c.number_format = fmt; c.protection = UNLOCK
    if fill: c.fill = fill
    return c


# =============================================================== Inputs
inp = wb.active; inp.title = "Inputs"
inp["A1"] = "CAT Financial Model: Inputs"; inp["A1"].font = H1
note(inp, "A2", "Blue = input. Yellow fill = the assumptions that move the answer most and are outstanding at a gate. "
     "Constant 2026 dollars, no escalation, so the discount rate should be a real rate. Only blue cells are editable "
     "(sheets are protected with no password; Review > Unprotect Sheet to change structure).", "G2", 40)
hdr(inp, 4, ["Parameter", "Value", "Unit", "Status", "Basis", "Source document", "Gate"])

I = {}
SRC917 = "Products/CAT/01_Technology_Research/CAT_Layers_1_3_Independent_Execution_2026-09-17.md"
SRCCDA = "AOP_FY27/Change_Logs/2026-08-18_CDA_FY27_AOP_Change_Log.md (sections 0 and 2)"
SRC916 = "Products/CAT/CAT.md; 2026-09-16 discussion transcript"
rows = [
    ("sec", "Fleet and vendor pricing"),
    ("N", "In-scope fleet size", 8300, "assets", "Inferred", "~$500,000/yr at ~$5/tracker/month (Tom Mitchell). Not counted.", SRC916, "G1", NUM, True, ("whole", 1, 1000000)),
    ("p0", "Vendor full-stack price (Option 0)", 5.00, "$/tracker/month", "Reported", "Sensolus and Alesea both ~$5; includes hardware, connectivity, services, support, replacement, and the vendor application.", SRC916, "G2", USD2, False, ("dec", 0, 100)),
    ("p1", "Sensolus Connect price (Option 1)", 3.50, "$/tracker/month", "Offered, price pending", "Sensolus offered Sensolus Connect on 2026-09-21: API access to all data, with their front-end application removed from the cost. That is Option 1's scope. No price yet, so $3.50 is still the 09-17 placeholder. Enter the quoted price here and the whole workbook follows.", "Sensolus call, 2026-09-21 (Darryl)", "G2", USD2, True, ("dec", 0, 100)),
    ("sec", "Wesco product team: POD build, then maintain and enhance (Options 1 and 3). All India, fractional to CAT"),
    ("ifte", "India development FTE", 7.00, "FTE", "Stated", "Darryl 2026-09-21: POD development is all India. Effort sized on the CDA FY27 development team (7.0 FTE, eight months).", "Darryl, 2026-09-21; effort from " + SRCCDA, "-", NUM2, False, ("dec", 0, 50)),
    ("nfte", "North America development FTE", 0.00, "FTE", "Stated", "Darryl 2026-09-21: none. CDA's own mix carried 0.25 North America FTE; CAT does not.", "Darryl, 2026-09-21", "-", NUM2, False, ("dec", 0, 50)),
    ("irate", "India rate", 22, "$/hour", "Benchmark", "CDA FY27 AOP rate.", SRCCDA, "-", USD2, False, ("dec", 0, 500)),
    ("nrate", "North America rate", 94, "$/hour", "Benchmark", "CDA FY27 AOP rate.", SRCCDA, "-", USD2, False, ("dec", 0, 500)),
    ("hours", "Annual hours per FTE", 1880, "hours", "Benchmark", "AOP calendar, matches Navigator and CDA.", SRCCDA, "-", NUM, False, ("whole", 0, 3000)),
    ("podm", "POD build duration", 8, "months", "Benchmark", "CDA: January to August. This is also Option 1 time to go-live.", SRCCDA, "-", NUM, False, ("whole", 0, 36)),
    ("podx", "POD build other IT expense", 45000, "$", "Benchmark", "CDA: licenses and field hardware.", SRCCDA, "-", USD, False, ("dec", 0, 10000000)),
    ("sus", "Team retained after build to maintain and enhance", 0.5, "% of build team", "Stated", "Darryl 2026-09-21: the team is fractional for CAT. Full effort through the build, then half retained to maintain and enhance. The same people carry other products.", "Darryl, 2026-09-21", "-", PCT, True, ("dec", 0, 3)),
    ("cap", "Share of build labor capitalized", 0.80, "%", "Convention", "CDA and entroCIM AOP convention. Memo only; does not change cash totals.", SRCCDA, "-", PCT, False, ("dec", 0, 1)),
    ("sec", "Option 3 devices and services (self-assembled layers 1-3)"),
    ("dev", "Device unit cost at volume", 90, "$/device", "Assumed", "Single-unit retail $175-$200; volume price not published.", SRC917 + " (sources 9, 22)", "G2 / OEM", USD, False, ("dec", 0, 10000)),
    ("life", "Device service life", 5, "years", "Assumed", "Drives refresh purchases inside the horizon when below 5. No residual value is credited at Year 5.", SRC917, "G3", NUM, False, ("whole", 1, 20)),
    ("loss", "Annual loss and damage rate", 0.08, "% of fleet/yr", "Assumed", "Pilot was 100 products, one tracker per vendor on each (200 trackers): good for comparing vendors, thin for a fleet loss rate.", SRC917, "G4", PCT, True, ("dec", 0, 1)),
    ("sim", "Connectivity, prepaid SIM", 14.00, "$/SIM", "Published", "1NCE $14 per SIM for 10 years.", SRC917 + " (source 14)", "-", USD2, False, ("dec", 0, 1000)),
    ("simterm", "SIM prepaid term", 10, "years", "Published", "Drives SIM renewal inside the horizon when below 5.", SRC917 + " (source 14)", "-", NUM, False, ("whole", 1, 20)),
    ("simrep", "New SIM for each replacement device (1 yes, 0 no)", 0, "switch", "Model choice", "0 matches 09-17. 1 corrects the R15 caveat.", SRC917, "-", "0", False, ("list", "0,1")),
    ("plat", "Device services platform", 6.00, "$/device/yr", "Assumed", "Golioth connect, location API ~1.5 req/day, AWS messaging and device management at published rates.", SRC917 + " (sources 15-17)", "G3", USD2, False, ("dec", 0, 1000)),
    ("sec", "Option 3 layer 1-3 engineering and fleet operations"),
    ("engshare", "India share of layer 1-3 engineering", 0.70, "%", "Stated", "Darryl 2026-09-21: split between the India development team and the US operations team. The balance is charged at the North America AOP rate. Replaces the flat $175,000 US loaded cost used on 09-17.", "Darryl, 2026-09-21", "-", PCT, True, ("dec", 0, 1)),
    ("bfte", "Layer 1-3 integration build team", 4, "FTE", "Assumed", "Ingest, device management and positioning integration, provisioning tooling. Separate from the PODs. Charged at the blended India/US rate below.", SRC917, "-", NUM2, False, ("dec", 0, 50)),
    ("bmo", "Layer 1-3 integration build duration", 12, "months", "Assumed", "Option 3 go-live is the later of this and the POD build.", SRC917, "-", NUM, False, ("whole", 0, 36)),
    ("sfte", "Layer 1-3 sustaining engineering", 1.5, "FTE", "Assumed", "Device services, firmware, carrier and integration upkeep. Separate from the product team.", SRC917, "-", NUM2, False, ("dec", 0, 50)),
    ("ofte", "Fleet operations", 2.0, "FTE", "Assumed", "Device health, exceptions, RMA. Excludes field labor absorbed elsewhere.", SRC917, "-", NUM2, False, ("dec", 0, 50)),
    ("opsc", "Loaded cost, fleet operations", 120000, "$/FTE/yr", "Assumed", "09-17 basis.", SRC917, "-", USD, False, ("dec", 0, 1000000)),
    ("ramp", "Fleet operations stand-up before go-live", 3, "months", "Assumed", "09-17: three to six months to recruit and stand up; low end used.", SRC917, "-", NUM, False, ("whole", 0, 24)),
    ("sec", "Timing and finance"),
    ("br", "Keep vendor service running during the build (1 yes, 0 no)", 0, "switch", "Model choice", "0 = no tracking until go-live. 1 = Option 0 cost carried for each option's build period.", "-", "Open", "0", False, ("list", "0,1")),
    ("disc", "Real discount rate", 0.10, "%/yr", "Placeholder", "Not a Wesco hurdle rate. Replace with Finance's real rate.", "-", "Finance", PCT, False, ("dec", 0, 0.5)),
]
dvs = {}
r = 5
for spec in rows:
    if spec[0] == "sec":
        inp.cell(row=r, column=1, value=spec[1]).font = H2
        r += 1; continue
    key, label, val, unit, status, basis, src, gate, fmt, yel, rule = spec
    inp.cell(row=r, column=1, value=label).font = BLACK
    inp.cell(row=r, column=1).alignment = WRAP
    inp_cell(inp, f"B{r}", val, fmt, YEL if yel else None)
    for j, v in enumerate([unit, status, basis, src, gate], start=3):
        c = inp.cell(row=r, column=j, value=v); c.font = BLACK if j != 6 else MUTED; c.alignment = WRAP
    inp.row_dimensions[r].height = 40
    I[key] = f"Inputs!$B${r}"
    kind = rule[0]
    if kind == "list":
        dv = DataValidation(type="list", formula1=f'"{rule[1]}"', allow_blank=False)
    else:
        dv = DataValidation(type="whole" if kind == "whole" else "decimal", operator="between",
                            formula1=str(rule[1]), formula2=str(rule[2]), allow_blank=False)
    dv.error = "Value outside the allowed range for this input."; dv.errorTitle = "Invalid input"; dv.showErrorMessage = True
    inp.add_data_validation(dv); dv.add(f"B{r}")
    r += 1

inp.cell(row=r, column=1, value="Derived (formulas, not inputs)").font = H2; r += 1
D = {}
derived = [
    ("team", "Product team annual cost", f"({I['ifte']}*{I['irate']}+{I['nfte']}*{I['nrate']})*{I['hours']}", USD, "CDA check: 8 months = $215,573"),
    ("tfte", "Product team size", f"{I['ifte']}+{I['nfte']}", NUM2, ""),
    ("t3", "Option 3 build period (months)", f"MAX({I['podm']},{I['bmo']})", NUM, "Later of POD build and layer 1-3 integration"),
    ("engc", "Layer 1-3 engineering, blended cost per FTE", f"({I['engshare']}*{I['irate']}+(1-{I['engshare']})*{I['nrate']})*{I['hours']}", USD, "India at $22/hour, US operations at $94/hour, at the split above"),
    ("af", "Five-year annuity factor", f"IF({I['disc']}=0,5,(1-(1+{I['disc']})^-5)/{I['disc']})", '0.0000', "End-of-year convention for Years 1-5; Year 0 at time zero"),
]
for key, label, f, fmt, nt in derived:
    inp.cell(row=r, column=1, value=label).font = BLACK
    c = inp.cell(row=r, column=2, value="=" + f); c.number_format = fmt; c.font = BLACK
    inp.cell(row=r, column=5, value=nt).font = MUTED
    D[key] = f"Inputs!$B${r}"
    r += 1
setw(inp, {"A": 42, "B": 12, "C": 15, "D": 12, "E": 58, "F": 40, "G": 10})
inp.freeze_panes = "A5"

N, p0, p1 = I["N"], I["p0"], I["p1"]


# =============================================================== Engine (scenario calculator)
# Columns: B base, C 09-17 basis, then tornado low/high pairs, then fleet table. Each column holds its own full
# parameter set so any one parameter can be overridden per column.
eng = wb.create_sheet(ENGINE_SHEET)
eng["A1"] = "Scenario engine"; eng["A1"].font = H1
note(eng, "A2", "Closed-form five-year calculation, one column per scenario. Column B must equal the Model sheet "
     "(checked on Reconciliation). Other columns change one parameter each; their override values are set on the "
     "Sensitivity sheet. No inputs live here.", "L2", 30)
PKEYS = ["N", "p0", "p1", "ifte", "nfte", "irate", "nrate", "hours", "podm", "podx", "sus",
         "dev", "life", "loss", "sim", "simterm", "simrep", "plat", "engshare", "bfte", "bmo", "sfte", "ofte", "opsc",
         "ramp", "br", "disc"]
PROW = {}
eng.cell(row=4, column=1, value="Scenario").font = BOLD
eng.cell(row=5, column=1, value="Parameter override").font = BOLD
rr = 7
eng.cell(row=6, column=1, value="Parameters").font = H2
for k in PKEYS:
    eng.cell(row=rr, column=1, value=k).font = BLACK
    PROW[k] = rr; rr += 1
rr += 1
eng.cell(row=rr, column=1, value="Outputs").font = H2; rr += 1
OUTS = ["team", "engc", "t3", "af", "o0y0", "o0a", "o05", "o0npv",
        "o1y0", "o1a", "o15", "o1npv", "o1team5", "o1cash5",
        "o3y0", "o3a", "o3ref5", "o3refpv", "o35", "o3npv", "o3team5", "o3eng5", "o3ops5", "o3cash5",
        "d1", "d3", "d1npv", "d3npv"]
OROW = {}
for k in OUTS:
    eng.cell(row=rr, column=1, value=k).font = BLACK
    OROW[k] = rr; rr += 1

scen_cols = []  # (col letter, name, overrides {key: formula-or-ref})


def eng_column(ci, name, overrides, desc=""):
    col = CL(ci)
    eng.cell(row=4, column=ci, value=name).font = BOLD
    eng.cell(row=5, column=ci, value=desc).font = MUTED
    for k in PKEYS:
        c = eng[f"{col}{PROW[k]}"]
        if k in overrides:
            c.value = "=" + str(overrides[k]); c.font = GREEN
        else:
            c.value = "=" + I[k]; c.font = GREEN
    P = lambda k: f"{col}${PROW[k]}"
    O = lambda k: f"{col}${OROW[k]}"
    r_ = P("disc")
    ref_dev_n = "+".join(f"IF({kk}*{P('life')}<=4,1,0)" for kk in range(1, 5))
    ref_sim_n = "+".join(f"IF({kk}*{P('simterm')}<=4,1,0)" for kk in range(1, 5))
    ref_dev_pv = "+".join(f"IF({kk}*{P('life')}<=4,(1+{r_})^-({kk}*{P('life')}+1),0)" for kk in range(1, 5))
    ref_sim_pv = "+".join(f"IF({kk}*{P('simterm')}<=4,(1+{r_})^-({kk}*{P('simterm')}+1),0)" for kk in range(1, 5))
    f = {
        "team": f"({P('ifte')}*{P('irate')}+{P('nfte')}*{P('nrate')})*{P('hours')}",
        "engc": f"({P('engshare')}*{P('irate')}+(1-{P('engshare')})*{P('nrate')})*{P('hours')}",
        "t3": f"MAX({P('podm')},{P('bmo')})",
        "af": f"IF({r_}=0,5,(1-(1+{r_})^-5)/{r_})",
        "o0y0": "0",
        "o0a": f"{P('N')}*{P('p0')}*12",
        "o05": f"{O('o0y0')}+5*{O('o0a')}",
        "o0npv": f"{O('o0y0')}+{O('o0a')}*{O('af')}",
        "o1y0": f"{O('team')}*{P('podm')}/12+{P('podx')}+{P('br')}*{P('N')}*{P('p0')}*{P('podm')}",
        "o1a": f"{P('N')}*{P('p1')}*12+{O('team')}*{P('sus')}",
        "o15": f"{O('o1y0')}+5*{O('o1a')}",
        "o1npv": f"{O('o1y0')}+{O('o1a')}*{O('af')}",
        "o1team5": f"{O('team')}*{P('podm')}/12+5*{O('team')}*{P('sus')}",
        "o1cash5": f"{O('o15')}-{O('o1team5')}",
        "o3y0": (f"{O('team')}*{O('t3')}/12+{P('podx')}+{P('bfte')}*{O('engc')}*{P('bmo')}/12"
                 f"+{P('N')}*({P('dev')}+{P('sim')})+{P('ofte')}*{P('opsc')}*{P('ramp')}/12"
                 f"+{P('br')}*{P('N')}*{P('p0')}*{O('t3')}"),
        "o3a": (f"{P('N')}*{P('loss')}*({P('dev')}+{P('sim')}*{P('simrep')})+{P('N')}*{P('plat')}"
                f"+{P('ofte')}*{P('opsc')}+{P('sfte')}*{O('engc')}+{O('team')}*{P('sus')}"),
        "o3ref5": f"{P('N')}*{P('dev')}*({ref_dev_n})+{P('N')}*{P('sim')}*({ref_sim_n})",
        "o3refpv": f"{P('N')}*{P('dev')}*({ref_dev_pv})+{P('N')}*{P('sim')}*({ref_sim_pv})",
        "o35": f"{O('o3y0')}+5*{O('o3a')}+{O('o3ref5')}",
        "o3npv": f"{O('o3y0')}+{O('o3a')}*{O('af')}+{O('o3refpv')}",
        "o3team5": f"{O('team')}*{O('t3')}/12+5*{O('team')}*{P('sus')}",
        "o3eng5": f"{P('bfte')}*{O('engc')}*{P('bmo')}/12+5*{P('sfte')}*{O('engc')}",
        "o3ops5": f"{P('ofte')}*{P('opsc')}*({P('ramp')}/12+5)",
        "o3cash5": f"{O('o35')}-{O('o3team5')}-{O('o3eng5')}-{O('o3ops5')}",
        "d1": f"{O('o15')}-{O('o05')}",
        "d3": f"{O('o35')}-{O('o05')}",
        "d1npv": f"{O('o1npv')}-{O('o0npv')}",
        "d3npv": f"{O('o3npv')}-{O('o0npv')}",
    }
    for k in OUTS:
        c = eng[f"{col}{OROW[k]}"]; c.value = "=" + f[k]; c.font = BLACK
        c.number_format = '0.0000' if k == "af" else (NUM if k == "t3" else USD)
    eng.column_dimensions[col].width = 13
    return col


E = lambda col, k: f"{ENGINE_SHEET}!${col}${OROW[k]}"
BASE = eng_column(2, "Base", {}, "All inputs")
C917 = eng_column(3, "09-17 basis", {"ifte": 0, "nfte": 0, "podx": 0, "ramp": 0,
                                     "engshare": f"(175000/{I['hours']}-{I['nrate']})/({I['irate']}-{I['nrate']})"},
                  "No product team, no POD expense, no ops stand-up, engineering at the flat $175,000 US rate")
setw(eng, {"A": 14})

# =============================================================== Sensitivity (drivers live here, engine reads them)
s = wb.create_sheet("Sensitivity")
s["A1"] = "CAT Financial Model: Sensitivity"; s["A1"].font = H1
note(s, "A2", "Each row changes one input and holds every other input at its Inputs value. Blue cells are editable. "
     "Differences are five-year totals against Option 0; positive means the option costs more than the declined "
     "subscription.", "K2", 30)
s["A4"] = "1. Which inputs move the answer (five-year, undiscounted)"; s["A4"].font = H2
hdr(s, 5, ["Driver", "Base", "Low", "High", "Option 1 vs 0 at low", "Option 1 vs 0 at high", "Option 1 swing",
           "Option 3 vs 0 at low", "Option 3 vs 0 at high", "Option 3 swing", "Rank (Option 1)"])
drivers = [
    ("N", "Fleet size (assets)", 5000, 15000, NUM),
    ("p1", "Data-only price ($/tracker/month)", 2.00, 5.00, USD2),
    ("sus", "Product team retained after build", 0.5, 1.25, PCT),
    ("podm", "POD build duration (months)", 6, 12, NUM),
    ("engshare", "India share of layer 1-3 engineering", 1.0, 0.3, PCT),
    ("ofte", "Fleet operations FTE", 1, 3, NUM2),
    ("loss", "Loss and damage rate", 0.04, 0.15, PCT),
    ("dev", "Device unit cost", 60, 150, USD),
    ("plat", "Device services platform ($/device/yr)", 3, 10, USD2),
    ("life", "Device service life (years)", 3, 7, NUM),
    ("br", "Vendor service kept during build", 0, 1, "0"),
    ("disc", "Discount rate (affects NPV only)", 0.06, 0.14, PCT),
]
t0 = 6
ci = 4
for i, (k, label, lo, hi, fmt) in enumerate(drivers):
    rw = t0 + i
    s.cell(row=rw, column=1, value=label).font = BLACK
    b = s.cell(row=rw, column=2, value="=" + I[k]); b.font = GREEN; b.number_format = fmt
    inp_cell(s, f"C{rw}", lo, fmt); inp_cell(s, f"D{rw}", hi, fmt)
    lo_col = eng_column(ci, f"{k} low", {k: f"Sensitivity!$C${rw}"}, label); ci += 1
    hi_col = eng_column(ci, f"{k} high", {k: f"Sensitivity!$D${rw}"}, label); ci += 1
    for j, ref in enumerate([E(lo_col, "d1"), E(hi_col, "d1")]):
        c = s.cell(row=rw, column=5 + j, value="=" + ref); c.font = GREEN; c.number_format = USD
    c = s.cell(row=rw, column=7, value=f"=ABS(F{rw}-E{rw})"); c.number_format = USD; c.font = BOLD
    for j, ref in enumerate([E(lo_col, "d3"), E(hi_col, "d3")]):
        c = s.cell(row=rw, column=8 + j, value="=" + ref); c.font = GREEN; c.number_format = USD
    c = s.cell(row=rw, column=10, value=f"=ABS(I{rw}-H{rw})"); c.number_format = USD; c.font = BOLD
    t1 = t0 + len(drivers) - 1
    s.cell(row=rw, column=11, value=f"=RANK(G{rw},$G${t0}:$G${t1})").font = BLACK
t1 = t0 + len(drivers) - 1
note(s, f"A{t1 + 1}", "Discount rate shows no swing here because this table is undiscounted; it moves NPV only. "
     "The engineering row tests the India/US split: all-India at one end, 30% India at the other.", f"K{t1 + 1}", 28)

fr = t1 + 4
s.cell(row=fr - 1, column=1, value="2. Fleet size, the dominant variable (five-year, fully costed)").font = H2
hdr(s, fr, ["Fleet (assets)", "Option 0", "Option 1", "Option 3", "Option 3 cash only", "Lowest cost"])
fleets = [4000, 6000, 8300, 10000, 15000, 20000, 25000, 30000, 40000, 50000]
f0 = fr + 1
for i, fl in enumerate(fleets):
    rw = f0 + i
    inp_cell(s, f"A{rw}", fl, NUM)
    col = eng_column(ci, f"Fleet {i + 1}", {"N": f"Sensitivity!$A${rw}"}, "Fleet table"); ci += 1
    for j, k in enumerate(["o05", "o15", "o35", "o3cash5"]):
        c = s.cell(row=rw, column=2 + j, value="=" + E(col, k)); c.font = GREEN; c.number_format = USD
    s.cell(row=rw, column=6, value=f'=INDEX($B${fr}:$D${fr},MATCH(MIN(B{rw}:D{rw}),B{rw}:D{rw},0))').font = BLACK
f1 = f0 + len(fleets) - 1
ch = LineChart()
ch.title = "Five-year cost by fleet size"; ch.y_axis.title = "Five-year total ($)"; ch.x_axis.title = "Fleet (assets)"
ch.y_axis.numFmt = '$#,##0'; ch.height = 9; ch.width = 20
for cidx in (2, 3, 4):
    ch.add_data(Reference(s, min_col=cidx, max_col=cidx, min_row=fr, max_row=f1), titles_from_data=True)
ch.set_categories(Reference(s, min_col=1, min_row=f0, max_row=f1))
for ser, colr, dash in zip(ch.series, ["46596B", "3B76D9", "E8842A"], [None, "dash", None]):
    ser.graphicalProperties.line.solidFill = colr; ser.graphicalProperties.line.width = 28000; ser.smooth = False
    if dash: ser.graphicalProperties.line.dashStyle = dash
ch.legend.position = "b"; ch.y_axis.delete = False; ch.x_axis.delete = False
s.add_chart(ch, f"H{fr - 1}")
pr = f1 + 3
s.cell(row=pr - 1, column=1, value="3. Sensolus Connect price points: the G2 decision, read off directly").font = H2
hdr(s, pr, ["Connect price ($/tracker/month)", "Option 1 five-year", "vs Option 0", "Cheaper than Option 0?",
            "Break-even fleet vs Option 0", "Cheaper than Option 3?"])
O1FIX = f"({D['team']}*{I['podm']}/12+{I['podx']}+5*{D['team']}*{I['sus']})"
p0r, brr, podmr = I["p0"], I["br"], I["podm"]
prices = [1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00]
p_0 = pr + 1
for i, pv in enumerate(prices):
    rw = p_0 + i
    inp_cell(s, f"A{rw}", pv, USD2)
    c = s.cell(row=rw, column=2, value=f"={N}*$A{rw}*60+{O1FIX}"); c.number_format = USD; c.font = BLACK
    c = s.cell(row=rw, column=3, value=f"=B{rw}-{E(BASE, 'o05')}"); c.number_format = USD; c.font = BLACK
    s.cell(row=rw, column=4, value=f'=IF(B{rw}<{E(BASE, "o05")},"Yes","No")').font = BOLD
    m = f"(({p0r}-$A{rw})*60-{brr}*{p0r}*{podmr})"
    s.cell(row=rw, column=5, value=f'=IF({m}<=0,"Never",ROUNDUP({O1FIX}/{m},0))').number_format = NUM
    s.cell(row=rw, column=6, value=f'=IF(B{rw}<{E(BASE, "o35")},"Yes","No")').font = BLACK
p_1 = p_0 + len(prices) - 1
s.cell(row=p_1 + 2, column=1, value="Ceiling: highest price that still beats Option 0").font = BOLD
c = s.cell(row=p_1 + 2, column=2,
           value=f"=IF({N}=0,0,({E(BASE, 'o05')}-({E(BASE, 'o15')}-{N}*{I['p1']}*60))/({N}*60))")
c.number_format = USD2; c.font = GREENB
note(s, f"A{p_1 + 3}", "Option 1 totals here carry the POD build, the retained product team and any bridge months, so they are "
     "comparable with the Option 0 subscription on the same five-year basis. The break-even column answers the other "
     "half of the question: at a price above the ceiling, Option 1 still wins if the counted fleet (G1) is at least "
     "this large.", f"F{p_1 + 3}", 30)

setw(s, {"A": 38, "B": 13, "C": 13, "D": 13, "E": 15, "F": 15, "G": 14, "H": 15, "I": 15, "J": 14, "K": 10})

# =============================================================== Model (annual display, base inputs)
m = wb.create_sheet("Model", 0)
m["A1"] = "CAT Financial Model: Five-Year Cash View"; m["A1"].font = H1
note(m, "A2", "Constant 2026 dollars. Year 0 is the build period before go-live, at time zero for NPV; Years 1 to 5 are "
     "five full operating years, end-of-year convention, so every option is compared on the same 60 months of service. "
     "The entroCIM Sensolus connector (data in) is already built and excluded. The operations interface is not: any "
     "option beyond Option 0 needs new PODs and a team to maintain them.", "I2", 52)
hdr(m, 4, ["Line item", "Year 0 (build)", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "5-yr total", "NPV"])
YC = ["B", "C", "D", "E", "F", "G"]  # Year 0..5
M = {}
row = 5


def section(title):
    global row
    m.cell(row=row, column=1, value=title).font = H2; row += 1


def line(key, label, y0, yop, bold=False, fill=None, border=False):
    """y0: formula for Year 0 (or None). yop: function j(1..5)->formula, or formula string for all years."""
    global row
    m.cell(row=row, column=1, value=label).font = BOLD if bold else BLACK
    for j, col in enumerate(YC):
        if j == 0:
            val = y0 if y0 is not None else "0"
        else:
            val = yop(j) if callable(yop) else (yop if yop is not None else "0")
        c = m[f"{col}{row}"]; c.value = "=" + val; c.number_format = USD; c.font = BOLD if bold else BLACK
    g = m[f"H{row}"]; g.value = f"=SUM(B{row}:G{row})"; g.number_format = USD; g.font = BOLD
    h = m[f"I{row}"]; h.value = f"=B{row}+NPV({I['disc']},C{row}:G{row})"; h.number_format = USD
    h.font = BOLD if bold else BLACK
    for col in "ABCDEFGHI":
        if fill: m[f"{col}{row}"].fill = fill
        if border: m[f"{col}{row}"].border = TOPB
    M[key] = row; row += 1


def ssum(a, b):
    return lambda j: f"SUM({YC[j]}{M[a]}:{YC[j]}{M[b]})"


TEAM, T3, ENGC = D["team"], D["t3"], D["engc"]
section("Option 0: vendor full stack, vendor application (the declined baseline)")
line("o0", "Vendor subscription, all layers", None, f"{N}*{p0}*12", bold=True, fill=TOT)
row += 1
section("Option 1: vendor keeps layers 1-3; Wesco PODs on the existing connector")
line("o1_data", "Vendor data access at G2 price (placeholder)", None, f"{N}*{p1}*12")
line("o1_br", "Bridge: vendor full stack during build", f"{I['br']}*{N}*{p0}*{I['podm']}", None)
line("o1_podx", "POD build other IT (licenses, field hardware)", I["podx"], None)
line("o1_cash", "External cash subtotal", None, None, bold=True, border=True)
for j, col in enumerate(YC):
    m[f"{col}{M['o1_cash']}"].value = f"=SUM({col}{M['o1_data']}:{col}{M['o1_podx']})"
line("o1_tb", "Product team: POD build", f"{TEAM}*{I['podm']}/12", None)
line("o1_tm", "Product team: maintain and enhance (retained share)", None, f"{TEAM}*{I['sus']}")
line("o1", "Option 1 total, fully costed", None, None, bold=True, fill=TOT, border=True)
for j, col in enumerate(YC):
    m[f"{col}{M['o1']}"].value = f"={col}{M['o1_cash']}+{col}{M['o1_tb']}+{col}{M['o1_tm']}"
row += 1
section("Option 3: Wesco self-assembles layers 1-3 and builds the PODs")
line("d_init", "Devices, initial fleet", f"{N}*{I['dev']}", None)
line("s_init", "SIMs, initial fleet (prepaid)", f"{N}*{I['sim']}", None)
line("d_rep", "Device replacements (loss and damage)", None, f"{N}*{I['loss']}*{I['dev']}")
line("s_rep", "SIMs for replacement devices", None, f"{N}*{I['loss']}*{I['sim']}*{I['simrep']}")
line("d_ref", "Device refresh at end of service life", None, lambda j: f"IF(AND({j}>1,MOD({j}-1,{I['life']})=0),{N}*{I['dev']},0)")
line("s_ref", "SIM renewal at end of prepaid term", None, lambda j: f"IF(AND({j}>1,MOD({j}-1,{I['simterm']})=0),{N}*{I['sim']},0)")
line("plat", "Device services platform", None, f"{N}*{I['plat']}")
line("o3_br", "Bridge: vendor full stack during build", f"{I['br']}*{N}*{p0}*{T3}", None)
line("o3_podx", "POD build other IT (licenses, field hardware)", I["podx"], None)
line("o3_cash", "External cash subtotal (the build thesis number)", None, None, bold=True, border=True)
for j, col in enumerate(YC):
    m[f"{col}{M['o3_cash']}"].value = f"=SUM({col}{M['d_init']}:{col}{M['o3_podx']})"
line("o3_tb", "Product team: build period, full effort (PODs)", f"{TEAM}*{T3}/12", None)
line("o3_tm", "Product team: maintain and enhance (retained share)", None, f"{TEAM}*{I['sus']}")
line("o3_eb", "Layer 1-3 integration build (70% India / 30% US)", f"{I['bfte']}*{ENGC}*{I['bmo']}/12", None)
line("o3_es", "Layer 1-3 sustaining engineering", None, f"{I['sfte']}*{ENGC}")
line("o3_ob", "Fleet operations stand-up", f"{I['ofte']}*{I['opsc']}*{I['ramp']}/12", None)
line("o3_os", "Fleet operations", None, f"{I['ofte']}*{I['opsc']}")
line("o3", "Option 3 total, fully costed", None, None, bold=True, fill=TOT, border=True)
for j, col in enumerate(YC):
    m[f"{col}{M['o3']}"].value = f"={col}{M['o3_cash']}+SUM({col}{M['o3_tb']}:{col}{M['o3_os']})"
row += 1
section("Difference from Option 0 (positive = costs more than the declined subscription)")
for k, lab in [("o1", "Option 1 vs Option 0"), ("o3", "Option 3 vs Option 0")]:
    line("d_" + k, lab, None, None)
    for j, col in enumerate(YC):
        m[f"{col}{M['d_' + k]}"].value = f"={col}{M[k]}-{col}{M['o0']}"
row += 1
section("Cumulative cost, for payback reading")
for k, lab in [("o0", "Option 0"), ("o1", "Option 1"), ("o3", "Option 3")]:
    m.cell(row=row, column=1, value=lab + " cumulative").font = BLACK
    for j, col in enumerate(YC):
        c = m[f"{col}{row}"]; c.value = f"=SUM($B${M[k]}:{col}{M[k]})"; c.number_format = USD; c.font = BLACK
    M["cum_" + k] = row; row += 1
row += 1
section("Memo")
m.cell(row=row, column=1, value="Capitalizable build labor, Option 1").font = BLACK
c = m[f"B{row}"]; c.value = f"={I['cap']}*B{M['o1_tb']}"; c.number_format = USD; c.font = BLACK; row += 1
m.cell(row=row, column=1, value="Capitalizable build labor, Option 3").font = BLACK
c = m[f"B{row}"]; c.value = f"={I['cap']}*(B{M['o3_tb']}+B{M['o3_eb']})"; c.number_format = USD; c.font = BLACK; row += 1
note(m, f"A{row}", "Capitalization changes the P&L view, not cash. No residual value is credited for devices still in "
     "service after Year 5, which is modestly conservative against Option 3. Options 2 and 4 are not modelled; see "
     "Open Inputs.", f"I{row}", 28)
setw(m, {"A": 48, "B": 14, "C": 12, "D": 12, "E": 12, "F": 12, "G": 12, "H": 14, "I": 14})
m.freeze_panes = "B5"

# =============================================================== Break-even
be = wb.create_sheet("Break-even", 1)
be["A1"] = "CAT Financial Model: Break-even and G2 Price Ceilings"; be["A1"].font = H1
note(be, "A2", "Three bases. Run-rate is one steady operating year after the build. Five-year cash is undiscounted and "
     "includes the build. NPV includes the build at time zero. Asset counts are rounded up. A funding case will be "
     "read on the five-year or NPV basis.", "C2", 42)
B = {}
brow_ = [4]


def bsec(title):
    be.cell(row=brow_[0], column=1, value=title).font = H2; brow_[0] += 1


def bline(key, label, formula, fmt, bold=False, nt=None, font=None):
    r_ = brow_[0]
    be.cell(row=r_, column=1, value=label).font = BOLD if bold else BLACK
    c = be.cell(row=r_, column=2, value="=" + formula); c.number_format = fmt
    c.font = font or (BOLD if bold else BLACK)
    if nt:
        x = be.cell(row=r_, column=3, value=nt); x.font = MUTED; x.alignment = WRAP
    B[key] = f"$B${r_}"; B[key + "_x"] = f"'Break-even'!$B${r_}"
    brow_[0] += 1


def BEF(fixed, margin):
    return f'IF({margin}<=0,"Never",ROUNDUP({fixed}/{margin},0))'


L = lambda k: I[k]
ref_n = lambda term: "+".join(f"IF({kk}*{term}<=4,1,0)" for kk in range(1, 5))
ref_pv = lambda term: "+".join(f"IF({kk}*{term}<=4,(1+{L('disc')})^-({kk}*{term}+1),0)" for kk in range(1, 5))

bsec("Run-rate: one steady operating year, undiscounted")
bline("rr_v", "Option 0 per asset per year", f"{p0}*12", USD2)
bline("rr_var", "Option 3 variable cost per asset per year",
      f"{L('dev')}/{L('life')}+{L('loss')}*{L('dev')}+{L('sim')}/{L('simterm')}+{L('loss')}*{L('sim')}*{L('simrep')}+{L('plat')}", USD2)
bline("rr_m3", "Option 3 margin per asset per year", f"{B['rr_v']}-{B['rr_var']}", USD2)
bline("rr_f3", "Option 3 fixed cost per year (team, engineering, fleet ops)", f"{TEAM}*{L('sus')}+{L('sfte')}*{ENGC}+{L('ofte')}*{L('opsc')}", USD)
bline("rr_be3", "Break-even fleet, Option 3 vs Option 0", BEF(B['rr_f3'], B['rr_m3']), NUM, bold=True, nt="09-17 figure was ~18,000 before the product team was added")
bline("rr_m1", "Option 1 margin per asset per year", f"({p0}-{p1})*12", USD2)
bline("rr_f1", "Option 1 fixed cost per year (product team)", f"{TEAM}*{L('sus')}", USD)
bline("rr_be1", "Break-even fleet, Option 1 vs Option 0", BEF(B['rr_f1'], B['rr_m1']), NUM, bold=True)
brow_[0] += 1
bsec("Five-year cash: build plus five operating years, undiscounted")
bline("fy_v", "Option 0 per asset", f"{p0}*60", USD2)
bline("fy_var", "Option 3 variable per asset",
      f"{L('dev')}+{L('sim')}+5*({L('loss')}*({L('dev')}+{L('sim')}*{L('simrep')})+{L('plat')})"
      f"+{L('dev')}*({ref_n(L('life'))})+{L('sim')}*({ref_n(L('simterm'))})+{L('br')}*{p0}*{T3}", USD2)
bline("fy_m3", "Option 3 margin per asset", f"{B['fy_v']}-{B['fy_var']}", USD2)
bline("fy_f3", "Option 3 fixed cost",
      f"{TEAM}*{T3}/12+{L('podx')}+{L('bfte')}*{ENGC}*{L('bmo')}/12+{L('ofte')}*{L('opsc')}*{L('ramp')}/12"
      f"+5*({TEAM}*{L('sus')}+{L('sfte')}*{ENGC}+{L('ofte')}*{L('opsc')})", USD)
bline("fy_be3", "Break-even fleet, Option 3 vs Option 0", BEF(B['fy_f3'], B['fy_m3']), NUM, bold=True)
bline("fy_m1", "Option 1 margin per asset", f"({p0}-{p1})*60-{L('br')}*{p0}*{L('podm')}", USD2)
bline("fy_f1", "Option 1 fixed cost", f"{TEAM}*{L('podm')}/12+{L('podx')}+5*{TEAM}*{L('sus')}", USD)
bline("fy_be1", "Break-even fleet, Option 1 vs Option 0", BEF(B['fy_f1'], B['fy_m1']), NUM, bold=True)
brow_[0] += 1
bsec("NPV: build at time zero, operating years discounted")
AF = D["af"]
bline("pv_v", "Option 0 per asset", f"{p0}*12*{AF}", USD2)
bline("pv_var", "Option 3 variable per asset",
      f"{L('dev')}+{L('sim')}+({L('loss')}*({L('dev')}+{L('sim')}*{L('simrep')})+{L('plat')})*{AF}"
      f"+{L('dev')}*({ref_pv(L('life'))})+{L('sim')}*({ref_pv(L('simterm'))})+{L('br')}*{p0}*{T3}", USD2)
bline("pv_m3", "Option 3 margin per asset", f"{B['pv_v']}-{B['pv_var']}", USD2)
bline("pv_f3", "Option 3 fixed cost",
      f"{TEAM}*{T3}/12+{L('podx')}+{L('bfte')}*{ENGC}*{L('bmo')}/12+{L('ofte')}*{L('opsc')}*{L('ramp')}/12"
      f"+({TEAM}*{L('sus')}+{L('sfte')}*{ENGC}+{L('ofte')}*{L('opsc')})*{AF}", USD)
bline("pv_be3", "Break-even fleet, Option 3 vs Option 0", BEF(B['pv_f3'], B['pv_m3']), NUM, bold=True)
bline("pv_m1", "Option 1 margin per asset", f"({p0}-{p1})*12*{AF}-{L('br')}*{p0}*{L('podm')}", USD2)
bline("pv_f1", "Option 1 fixed cost", f"{TEAM}*{L('podm')}/12+{L('podx')}+{TEAM}*{L('sus')}*{AF}", USD)
bline("pv_be1", "Break-even fleet, Option 1 vs Option 0", BEF(B['pv_f1'], B['pv_m1']), NUM, bold=True)
brow_[0] += 1
bsec("G2 price ceilings: highest data-only price at which Option 1 still costs less (five-year)")
o1fixed = f"({E(BASE, 'o15')}-{N}*{p1}*60)"
bline("c0", "Than Option 0, fully costed", f"IF({N}=0,0,({E(BASE, 'o05')}-{o1fixed})/({N}*60))", USD2, bold=True,
      nt="A negative value means no data-only price makes Option 1 cheaper at this fleet size", font=GREENB)
bline("c3", "Than Option 3, fully costed", f"IF({N}=0,0,({E(BASE, 'o35')}-{o1fixed})/({N}*60))", USD2, bold=True, font=GREENB)
bline("c0x", "Than Option 0, product team excluded (the build thesis view)",
      f"IF({N}=0,0,({E(BASE, 'o05')}-({E(BASE, 'o1cash5')}-{N}*{p1}*60))/({N}*60))", USD2, font=GREEN)
bline("cp", "Current placeholder price", p1, USD2, font=GREEN)
setw(be, {"A": 60, "B": 16, "C": 62})

# =============================================================== Reconciliation
rc = wb.create_sheet("Reconciliation")
rc["A1"] = "Reconciliation"; rc["A1"].font = H1
note(rc, "A2", "Part 1 proves the engine reproduces the 2026-09-17 figures when the product team is switched off and layer 1-3 "
     "engineering is set back to the flat $175,000 US rate. "
     "Part 2 walks the Option 3 figure from 09-17 to today. Part 3 checks the Model sheet against the engine.", "F2", 30)
rc["A3"] = "Tolerance"; rc["A3"].font = BLACK
inp_cell(rc, "B3", 0.005, PCT)
note(rc, "C3", "Published figures were rounded to the nearest $10,000.")
hdr(rc, 5, ["Figure", "Published / expected", "This workbook", "Difference", "Check", "Note"])
r_ = 6


def rline(label, pub, formula, fmt=USD, nt="", pub_is_formula=False):
    global r_
    rc.cell(row=r_, column=1, value=label).font = BLACK
    p = rc.cell(row=r_, column=2, value=pub); p.number_format = fmt; p.font = GREEN if pub_is_formula else BLUE
    c = rc.cell(row=r_, column=3, value="=" + formula); c.number_format = fmt; c.font = GREEN
    d = rc.cell(row=r_, column=4, value=f"=IF(B{r_}=0,C{r_},C{r_}/B{r_}-1)"); d.number_format = PCT; d.font = BLACK
    rc.cell(row=r_, column=5, value=f'=IF(ABS(D{r_})<=$B$3,"Ties","Differs")').font = BOLD
    rc.cell(row=r_, column=6, value=nt).font = MUTED
    r_ += 1


rc.cell(row=r_, column=1, value="Part 1. 09-17 figures, with the 09-18 additions switched off").font = H2; r_ += 1
rline("Option 0 five-year", 2490000, E(C917, "o05"))
rline("Option 3, internal labor free", 1410000, E(C917, "o3cash5"))
rline("Option 3, labor costed", 4620000, E(C917, "o35"), nt="Published $4.62M; exact $4,623,500")
r_ += 1
rc.cell(row=r_, column=1, value="Part 2. Option 3 walk, 09-17 to today").font = H2; r_ += 1
walk = [
    ("09-17 Option 3, labor costed", E(C917, "o35")),
    ("+/- Layer 1-3 engineering at the India/US split rather than $175,000", f"({I['bfte']}*{I['bmo']}/12+5*{I['sfte']})*({ENGC}-175000)"),
    ("+ Product team, build period", f"{E(BASE, 'o3team5')}-5*{TEAM}*{I['sus']}"),
    ("+ Product team, maintain and enhance (5 years)", f"5*{TEAM}*{I['sus']}"),
    ("+ POD build other IT", I["podx"]),
    ("+ Fleet operations stand-up before go-live", f"{I['ofte']}*{I['opsc']}*{I['ramp']}/12"),
]
w0 = r_
for lab, f in walk:
    rc.cell(row=r_, column=1, value=lab).font = BLACK
    c = rc.cell(row=r_, column=3, value="=" + f); c.number_format = USD; c.font = GREEN; r_ += 1
rc.cell(row=r_, column=1, value="Walk total").font = BOLD
c = rc.cell(row=r_, column=3, value=f"=SUM(C{w0}:C{r_ - 1})"); c.number_format = USD; c.font = BOLD
wt = r_; r_ += 1
rline("Walk total equals current Option 3", f"=C{wt}", E(BASE, "o35"), pub_is_formula=True,
      nt="Any difference is from other inputs changed since 09-17")
r_ += 1
rc.cell(row=r_, column=1, value="Part 3. Model sheet equals engine").font = H2; r_ += 1
for k, lab in [("o0", "Option 0"), ("o1", "Option 1"), ("o3", "Option 3")]:
    rline(f"{lab} five-year", f"=Model!$H${M[k]}", E(BASE, {"o0": "o05", "o1": "o15", "o3": "o35"}[k]), pub_is_formula=True)
    rline(f"{lab} NPV", f"=Model!$I${M[k]}", E(BASE, {"o0": "o0npv", "o1": "o1npv", "o3": "o3npv"}[k]), pub_is_formula=True)
rline("POD build labor, CDA effort at all-India rates", 193013, f"{TEAM}*{I['podm']}/12", nt="CDA's own mix (6.75 India + 0.25 NA) cost $215,573 for the same eight months")
setw(rc, {"A": 50, "B": 18, "C": 16, "D": 12, "E": 10, "F": 55})

# =============================================================== Open Inputs
g = wb.create_sheet("Open Inputs")
g["A1"] = "What replaces each assumption"; g["A1"].font = H1
note(g, "A2", "The model becomes a business case only when these land. Owners are from the CAT risk and dependency log.", "E2")
hdr(g, 4, ["Input", "Gate", "What replaces the assumption", "Owner", "Effect on the answer"])
gates = [
    ("Product team: dedicated or shared", "Open", "Decision on whether the CAT PODs team is dedicated, or shared with CDA and entroCIM so only a share is charged to CAT", "Darryl Benson", "Largest single lever on Option 1. At 100% retained the team costs about two-thirds of the subscription it replaces"),
    ("Fleet size (8,300, inferred)", "G1", "Counted asset baseline: classes, sites, loss and replacement spend", "Supply chain operations, via Tom Mitchell", "Largest lever on Option 3. Everything internal is fixed cost spread over assets"),
    ("Data-only price ($3.50, placeholder)", "G2", "Written unbundled Sensolus pricing, scope-matched to Option 1", "Sensolus, via Tom Mitchell", "Settles Option 1. Compare to the ceilings on Break-even"),
    ("POD scope and effort (CDA benchmark)", "Open", "POD scope for the operations interface, sized by the dev team rather than borrowed from CDA", "Darryl Benson's development team", "Moves the build period and the team size"),
    ("Layer 1-3 engineering rate", "Open", "Whether the product team absorbs layer 1-3 work at its blended rate or US engineering is required", "Darryl Benson", "Low case in Sensitivity; large effect on Option 3 only"),
    ("Loss and damage rate (8%)", "G4", "Measured loss, damage, battery and read rates from the pilot", "Tom Mitchell and supply chain", "Moderate. 100 assets per vendor is thin evidence for a fleet rate"),
    ("Device unit cost ($90)", "G2 / OEM", "Volume quote from Sensolus hardware-only or a merchant OEM", "Sensolus or OEM, via Tom Mitchell", "Small"),
    ("Device endpoint and payload", "G3", "Sensolus technical session: endpoint configurability, payload spec", "Sensolus, via Tom Mitchell", "Can remove Option 3 entirely if the endpoint is fixed"),
    ("Discount rate (10%, placeholder)", "Finance", "Wesco real hurdle rate", "Finance", "NPV only"),
    ("Options 2 and 4", "G1 / OEM", "Asset class split and merchant OEM device-management pricing", "Supply chain; OEM", "Option 4 may be the cost winner and is unpriced; both would also carry the product team"),
]
for i, rowv in enumerate(gates):
    for j, v in enumerate(rowv):
        c = g.cell(row=5 + i, column=1 + j, value=v); c.font = BLACK; c.alignment = WRAP
    g.row_dimensions[5 + i].height = 44
setw(g, {"A": 32, "B": 10, "C": 50, "D": 28, "E": 52})

# =============================================================== Summary (first)
sm = wb.create_sheet("Summary", 0)
sm["A1"] = "Connected Asset Tracking (CAT): Five-Year Financial Analysis"; sm["A1"].font = Font(name=F, size=16, bold=True, color="1F2A36")
note(sm, "A2", "Version 3, 2026-09-21. Illustrative model for discussion; not a business case and not a recommendation. "
     "Every option beyond Option 0 carries new PODs for the operations interface, built by the India team at CDA-scale "
     "effort and half retained afterwards to maintain and enhance. Rebuild on G1, G2 and G4 before it informs funding.", "I2", 42)
kv = [("Fleet size used", f"={N}", NUM, "assets, inferred, not counted"),
      ("Product team, build", f"={D['tfte']}", NUM2, "FTE, all India, CDA-scale effort"),
      ("Product team, retained", f"={TEAM}*{I['sus']}", USD, "a year to maintain and enhance, from go-live"),
      ("Option 0 annual subscription", f"={N}*{p0}*12", USD, "the cost the build direction set out to avoid")]
for i, (lab, f, fmt, nt) in enumerate(kv):
    sm.cell(row=4 + i, column=1, value=lab).font = BOLD
    c = sm.cell(row=4 + i, column=3, value=f); c.number_format = fmt; c.font = GREEN
    sm.cell(row=4 + i, column=4, value=nt).font = MUTED
hdr(sm, 9, ["Option", "What it is", "Go-live (months)", "External cash", "Product team", "Layer 1-3 engineering",
            "Fleet operations", "5-yr total", "NPV", "vs Option 0"])
opts = [
    ("Option 0", "Vendor full stack and vendor application, as declined", "0", E(BASE, "o05"), "0", "0", "0", E(BASE, "o05"), E(BASE, "o0npv")),
    ("Option 1", "Vendor keeps layers 1-3; Wesco PODs on the existing connector. G2 price is a placeholder", I["podm"],
     E(BASE, "o1cash5"), E(BASE, "o1team5"), "0", "0", E(BASE, "o15"), E(BASE, "o1npv")),
    ("Option 3", "Wesco self-assembles layers 1-3 and builds the PODs", T3,
     E(BASE, "o3cash5"), E(BASE, "o3team5"), E(BASE, "o3eng5"), E(BASE, "o3ops5"), E(BASE, "o35"), E(BASE, "o3npv")),
]
for i, (name, desc, gl, cash, team, engc, ops, tot, npv) in enumerate(opts):
    r_ = 10 + i
    sm.cell(row=r_, column=1, value=name).font = BOLD
    d = sm.cell(row=r_, column=2, value=desc); d.font = BLACK
    for j, (f, fmt) in enumerate([(gl, NUM), (cash, USD), (team, USD), (engc, USD), (ops, USD), (tot, USD), (npv, USD)]):
        c = sm.cell(row=r_, column=3 + j, value="=" + f); c.number_format = fmt
        c.font = GREEN if "!" in f else BLACK
    c = sm.cell(row=r_, column=10, value=f"=H{r_}-$H$10"); c.number_format = USD; c.font = BOLD
    for col in range(1, 11):
        sm.cell(row=r_, column=col).alignment = WRAPC
    sm.row_dimensions[r_].height = 30
    if i == 0:
        sm.cell(row=r_, column=3).value = "Vendor-led"; sm.cell(row=r_, column=3).font = BLACK
note(sm, "A13", "Options 2 and 4 are not modelled (no OEM pricing or asset class split). Both would carry the product team. See Open Inputs.", "J13")

sm["A15"] = "Model outputs"; sm["A15"].font = H2
BE_ = lambda k: B[k + "_x"]
tx = lambda ref, f='"$#,##0"': f"TEXT({ref},{f})"
findings = [
    f'="1. At "&{tx(N, chr(34) + "#,##0" + chr(34))}&" assets the declined subscription is the lowest-cost option fully costed: "&{tx("H10")}&" over five years, against "&{tx("H11")}&" for Option 1 and "&{tx("H12")}&" for Option 3."',
    f'="2. Any option beyond Option 0 carries the product team: "&{tx("C6")}&" a year to maintain and enhance the PODs, "&TEXT(C6/C7,"0%")&" of the subscription it would replace, and "&{tx("E11")}&" of Option 1\'s "&{tx("H11")}&" over five years."',
    f'="3. G2: with the retained team counted, Option 1 beats Option 0 only if data-only access is priced below "&TEXT({BE_("c0")},"$0.00")&" per tracker per month. At the "&TEXT({p1},"$0.00")&" placeholder it needs a fleet of "&IF(ISNUMBER({BE_("fy_be1")}),TEXT({BE_("fy_be1")},"#,##0"),{BE_("fy_be1")})&" assets."',
    f'="4. Option 3 breaks even with Option 0 at "&IF(ISNUMBER({BE_("fy_be3")}),TEXT({BE_("fy_be3")},"#,##0"),{BE_("fy_be3")})&" assets on five-year cash and "&IF(ISNUMBER({BE_("pv_be3")}),TEXT({BE_("pv_be3")},"#,##0"),{BE_("pv_be3")})&" on NPV, against an inferred fleet of "&TEXT({N},"#,##0")&"."',
    f'="5. Leave out all internal labor, which is the view behind the build direction, and Option 3 costs "&{tx("D12")}&" and Option 1 "&{tx("D11")}&". The saving exists only in that view."',
]
for i, f in enumerate(findings):
    r_ = 16 + i
    c = sm.cell(row=r_, column=1, value=f); c.font = BLACK; c.alignment = WRAP
    sm.merge_cells(start_row=r_, start_column=1, end_row=r_, end_column=10); sm.row_dimensions[r_].height = 30
sm["A22"] = "Interpretation (judgment, not a model output)"; sm["A22"].font = H2
interp = [
    "The build direction treats the application as the cheap layer. It is cheap to write and not cheap to own: the recurring cost is the team that keeps it running, not the build.",
    "If Wesco builds, the case is strategic rather than cost avoidance at this fleet size: control of the data, a POD framework reused across CDA and CAT, and a possible sellable service with Wesco as customer zero. It should be argued that way.",
    "The decision that could change the numbers most is internal: whether the PODs team is dedicated to CAT or shared across the portfolio. That is Darryl's to set, and it matters as much as the Sensolus price.",
]
for i, t in enumerate(interp):
    r_ = 23 + i
    c = sm.cell(row=r_, column=1, value=t); c.font = BLACK; c.alignment = WRAP
    sm.merge_cells(start_row=r_, start_column=1, end_row=r_, end_column=10); sm.row_dimensions[r_].height = 30

bc = BarChart(); bc.type = "bar"; bc.grouping = "stacked"; bc.overlap = 100
bc.title = "Five-year cost by option and component"; bc.height = 8; bc.width = 22
bc.add_data(Reference(sm, min_col=4, max_col=7, min_row=9, max_row=12), titles_from_data=True)
bc.set_categories(Reference(sm, min_col=1, min_row=10, max_row=12))
for ser, colr in zip(bc.series, ["46596B", "3B76D9", "E8842A", "9AA5B1"]):
    ser.graphicalProperties.solidFill = colr; ser.graphicalProperties.line.solidFill = colr
bc.x_axis.scaling.orientation = "maxMin"; bc.y_axis.numFmt = '$#,##0'; bc.y_axis.majorGridlines = None
bc.y_axis.delete = False; bc.x_axis.delete = False; bc.legend.position = "b"; bc.gapWidth = 60
sm.add_chart(bc, "A27")
setw(sm, {"A": 11, "B": 44, "C": 11, "D": 14, "E": 14, "F": 14, "G": 13, "H": 14, "I": 14, "J": 14})

# =============================================================== finishing
order = ["Summary", "Inputs", "Model", "Break-even", "Sensitivity", "Reconciliation", "Open Inputs", ENGINE_SHEET]
wb._sheets = [wb[n] for n in order]
for ws in wb.worksheets:
    for rowc in ws.iter_rows():
        for c in rowc:
            if c.value is not None and c.font is not None and c.font.name != F:
                c.font = Font(name=F, size=10, bold=c.font.b, color=c.font.color)
    ws.sheet_view.showGridLines = False
    ws.page_setup.orientation = "landscape"; ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.protection.sheet = True  # no password; input cells are unlocked
    ws.protection.formatColumns = False; ws.protection.formatRows = False
wb.save(OUT)
print("saved", OUT)
