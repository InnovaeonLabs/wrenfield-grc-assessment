"""Executive metrics, charts, and the static dashboard, computed from data/ (never typed by hand).

    python tools/metrics.py

Writes dashboard/metrics.json, dashboard/dashboard.md, dashboard/index.html and four SVG charts.
tools/check_formulas.py then proves the Excel Dashboard formulas produce the same numbers.
"""
from __future__ import annotations

import datetime as dt
import html
import json
import statistics
from collections import Counter, defaultdict

from build import FAMILY, load_all
from common import ROOT, STATUS_DATE, band, d, md_table, write_json

OUT = ROOT / "dashboard"
SEV = ["Critical", "High", "Moderate", "Low"]
# validated categorical slots (dataviz reference palette; scripts/validate_palette.js PASS light+dark)
S1, S2, S3 = ("#2a78d6", "#3987e5"), ("#eb6834", "#d95926"), ("#1baf7a", "#199e70")
STATUS = {"Critical": "#d03b3b", "High": "#ec835a", "Moderate": "#fab219", "Low": "#0ca30c"}
SHORT = {"AC": "Access Control", "AT": "Awareness & Training", "AU": "Audit & Accountability", "CA": "Assessment & Monitoring",
         "CM": "Configuration Mgmt", "CP": "Contingency Planning", "IA": "Identification & Auth", "IR": "Incident Response",
         "MP": "Media Protection", "PE": "Physical & Environmental", "PL": "Planning", "PM": "Program Management",
         "PS": "Personnel Security", "RA": "Risk Assessment", "SA": "Services Acquisition", "SC": "System & Comms Protection",
         "SI": "System & Info Integrity", "SR": "Supply Chain Risk"}

SVG_STYLE = f"""<style>
  .surface {{ fill: #fcfcfb; }} .ink {{ fill: #0b0b0b; }} .ink2 {{ fill: #52514e; }} .muted {{ fill: #898781; }}
  .grid {{ stroke: #e1e0d9; }} .axis {{ stroke: #c3c2b7; }}
  .s1 {{ fill: {S1[0]}; }} .s2 {{ fill: {S2[0]}; }} .s3 {{ fill: {S3[0]}; }}
  .l1 {{ stroke: {S1[0]}; }} .l2 {{ stroke: {S2[0]}; }} .gap {{ stroke: #fcfcfb; }}
  text {{ font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }}
  @media (prefers-color-scheme: dark) {{
    .surface {{ fill: #1a1a19; }} .ink {{ fill: #ffffff; }} .ink2 {{ fill: #c3c2b7; }}
    .grid {{ stroke: #2c2c2a; }} .axis {{ stroke: #383835; }}
    .s1 {{ fill: {S1[1]}; }} .s2 {{ fill: {S2[1]}; }} .s3 {{ fill: {S3[1]}; }}
    .l1 {{ stroke: {S1[1]}; }} .l2 {{ stroke: {S2[1]}; }} .gap {{ stroke: #1a1a19; }}
  }}
</style>"""


def rbar(x, y, w, h, cls, tip, r=4):
    """Horizontal bar: square at the baseline (left), 4px rounded data-end (right)."""
    if w <= 0:
        return ""
    r = min(r, w, h / 2)
    p = (f"M{x:.1f},{y:.1f} H{x + w - r:.1f} Q{x + w:.1f},{y:.1f} {x + w:.1f},{y + r:.1f} "
         f"V{y + h - r:.1f} Q{x + w:.1f},{y + h:.1f} {x + w - r:.1f},{y + h:.1f} H{x:.1f} Z")
    return f'<path class="{cls}" d="{p}" data-tip="{html.escape(tip)}"><title>{html.escape(tip)}</title></path>'


def compute(D):
    C, F, P, E, R = D["controls"], D["findings"], D["poam"], D["evidence"], D["risks"]
    V = D["vendor"]
    ar = json.loads((ROOT / "access-review" / "summary.json").read_text(encoding="utf-8"))
    res = Counter(c["result"] for c in C)
    val = Counter(c["status_validated"] for c in C)
    assessed = res["Satisfied"] + res["Other Than Satisfied"]
    fstat = Counter(f["status"] for f in F)
    open_f = [f for f in F if f["status"] not in ("Closed", "Risk Accepted")]
    high_open = [f for f in F if f["severity"] in ("Critical", "High") and f["status"] != "Closed"]
    closed = [p for p in P if p["status"] == "Closed"]
    ttc = [(d(p["closure_date"]) - d(D["fnd"][p["finding"]]["identified"])).days for p in closed]
    est = Counter(e["status"] for e in E)
    inv = []
    for v in V["inventory"]:
        s = sum(v["scores"])
        tier = 1 if s >= 9 else 2 if s >= 5 else 3
        last = d(v["last_assessed"]) if v["last_assessed"] else None
        months = {1: 12, 2: 24, 3: 36}[tier]
        nxt = dt.date(last.year + (last.month - 1 + months) // 12, (last.month - 1 + months) % 12 + 1, min(last.day, 28)) if last else None
        inv.append({"id": v["id"], "tier": tier, "current": bool(last and nxt >= STATUS_DATE)})
    t12 = [x for x in inv if x["tier"] <= 2]
    vr_sev = Counter(x["severity"] for x in V["vendor_findings"])
    # standing on the status date: residual once treatment is validated/accepted, otherwise the as-tested current score
    for r in R:
        done = r["status"].startswith(("Treated", "Accepted"))
        r["asof"], r["asof_score"] = (r["residual"], r["residual_score"]) if done else (r["current"], r["current_score"])
        r["asof_band"] = band(r["asof_score"])
    top = sorted(R, key=lambda r: (-r["asof_score"], -r["asof"][1], -r["asof"][0], r["id"]))[:5]
    m = {
        "status_date": str(STATUS_DATE),
        "controls": {"in_scope": len(C), "assessed": assessed, "satisfied": res["Satisfied"],
                     "other_than_satisfied": res["Other Than Satisfied"], "not_applicable": res["Not Assessed"],
                     "satisfied_pct": round(100 * res["Satisfied"] / assessed),
                     "validated_status": dict(val), "owner_status_changed": sum(c["status_owner"] != c["status_validated"] for c in C),
                     "evidence_level": dict(Counter(c["evidence_level"] for c in C))},
        "findings": {"total": len(F), "by_severity": {s: sum(f["severity"] == s for f in F) for s in SEV},
                     "by_status": dict(fstat), "open": len(open_f), "open_high_critical": len(high_open),
                     "open_high_ids": [f["id"] for f in high_open], "observations": len(D["obs"])},
        "poam": {"total": len(P), "closed_validated": len(closed), "overdue": [p["id"] for p in P if p["overdue"]],
                 "slipped": [p["id"] for p in P if p["slipped"]], "beyond_sla": [p["id"] for p in P if not p["within_sla"]],
                 "risk_accepted": [p["id"] for p in P if p["status"] == "Risk Accepted"],
                 "late_milestones": sum(len(p["late_milestones"]) for p in P),
                 "median_days_identified_to_validated_closure": statistics.median(ttc) if ttc else None,
                 "full_lifecycle_closures": [p["finding"] for p in closed]},
        "access_review": {k: ar[k] for k in ("entitlement_rows_reviewed", "privileged_rows", "phi_rows", "flagged_rows",
                                             "exceptions", "exception_rows", "false_positive_rows", "exceptions_closed",
                                             "exceptions_risk_accepted", "exceptions_open", "exception_rate_pct")},
        "vendor": {"tier12_total": len(t12), "tier12_current": sum(x["current"] for x in t12),
                   "vr_total": len(V["vendor_findings"]), "vr_by_severity": dict(vr_sev),
                   "vr_critical_high": vr_sev["Critical"] + vr_sev["High"],
                   "deep_assessment": "VEN-004 Quarrystone Analytics (fictional)", "treatment": V["decision"]["treatment"]},
        "evidence": {"total": len(E), "by_status": dict(est), "complete": est["Accepted"] + est["Closed"],
                     "completion_pct": round(100 * (est["Accepted"] + est["Closed"]) / len(E)),
                     "insufficient": est["Insufficient"], "overdue_outstanding": [e["id"] for e in E if not e.get("received") and d(e["due_date"]) < STATUS_DATE]},
        "risks": {"total": len(R), **{f"{s}_bands": {b: sum(r[f"{s}_band"] == b for r in R) for b in SEV} for s in ("inherent", "current", "residual")},
                  "asof_bands": {b: sum(r["asof_band"] == b for r in R) for b in SEV},
                  "top5_asof": [{"id": r["id"], "title": r["title"], "score": r["asof_score"], "band": r["asof_band"],
                                    "fieldwork": f"{r['current_score']} {r['current_band']}",
                                    "residual": f"{r['residual_score']} {r['residual_band']}", "owner": r["owner"], "status": r["status"]} for r in top]},
    }
    m["dashboard_crosscheck"] = {
        "MET-01": len(C), "MET-02": assessed, "MET-03": res["Satisfied"], "MET-03a": round(res["Satisfied"] / assessed, 2),
        "MET-04a": val["Implemented"], "MET-04b": val["Partially Implemented"], "MET-04c": val["Planned"] + val["Not Implemented"],
        "MET-05": m["controls"]["owner_status_changed"], "MET-06": len(F), "MET-06a": len(open_f),
        "MET-07": len(high_open), "MET-08": len(m["poam"]["overdue"]), "MET-08a": len(m["poam"]["slipped"]),
        "MET-09": len(closed), "MET-10": ar["exceptions"], "MET-10a": ar["exception_rows"],
        "MET-11": len(V["vendor_findings"]), "MET-11a": m["vendor"]["vr_critical_high"],
        "MET-11b": m["vendor"]["tier12_current"], "MET-11c": len(t12),
        "MET-12": round((est["Accepted"] + est["Closed"]) / len(E), 2),
        "MET-13a": sum(r["current_band"] in ("High", "Critical") for r in R),
        "MET-13b": sum(r["residual_band"] in ("High", "Critical") for r in R),
    }
    # weekly series of open findings (identified and not yet validated-closed; accepted counted separately)
    series, t = [], dt.date(2026, 6, 26)
    while t <= STATUS_DATE:
        def is_open(f, t=t):
            p = D["pm"][f["poam"]]
            if d(f["identified"]) > t:
                return False
            if p["status"] == "Closed" and d(p["closure_date"]) <= t:
                return False
            if p["status"] == "Risk Accepted" and dt.date(2026, 8, 12) <= t:
                return False
            return True
        series.append({"date": str(t), "open": sum(is_open(f) for f in F),
                       "open_high": sum(is_open(f) and f["severity"] in ("High", "Critical") for f in F)})
        t += dt.timedelta(days=7)
    if series[-1]["date"] != str(STATUS_DATE):
        series.append({"date": str(STATUS_DATE), "open": len(open_f),
                       "open_high": sum(f["severity"] in ("High", "Critical") for f in open_f)})
    m["open_findings_series"] = series
    fam = defaultdict(Counter)
    for c in C:
        fam[c["family"]][c["result"]] += 1
    m["controls"]["by_family"] = {k: dict(v) for k, v in sorted(fam.items())}
    return m


# ------------------------------------------------------------------ charts
def svg_family(m):
    fams = [(k, v) for k, v in m["controls"]["by_family"].items()]
    fams.sort(key=lambda kv: (-(kv[1].get("Satisfied", 0) + kv[1].get("Other Than Satisfied", 0)), kv[0]))
    W, rowh, bh, left, top = 660, 22, 14, 190, 58
    H = top + rowh * len(fams) + 40
    maxn = max(v.get("Satisfied", 0) + v.get("Other Than Satisfied", 0) for _, v in fams)
    scale = (W - left - 60) / maxn
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
           f'aria-label="Control assessment results by family">', SVG_STYLE,
           f'<rect class="surface" width="{W}" height="{H}" rx="8"/>',
           '<text class="ink" x="16" y="24" font-size="15" font-weight="600">Control results by family</text>',
           f'<text class="ink2" x="16" y="42" font-size="11">{m["controls"]["satisfied"]} of {m["controls"]["assessed"]} assessed controls Satisfied · AC-18 Not Applicable (excluded)</text>',
           f'<rect class="s1" x="{W - 250}" y="14" width="10" height="10" rx="2"/><text class="ink2" x="{W - 235}" y="23" font-size="11">Satisfied</text>',
           f'<rect class="s2" x="{W - 165}" y="14" width="10" height="10" rx="2"/><text class="ink2" x="{W - 150}" y="23" font-size="11">Other Than Satisfied</text>']
    for i in range(0, maxn + 1, 2):
        x = left + i * scale
        out.append(f'<line class="grid" x1="{x:.1f}" x2="{x:.1f}" y1="{top - 6}" y2="{top + rowh * len(fams)}" stroke-width="1"/>')
        out.append(f'<text class="muted" x="{x:.1f}" y="{top + rowh * len(fams) + 16}" font-size="10" text-anchor="middle">{i}</text>')
    for i, (k, v) in enumerate(fams):
        y = top + i * rowh + (rowh - bh) / 2
        s, o = v.get("Satisfied", 0), v.get("Other Than Satisfied", 0)
        out.append(f'<text class="ink2" x="{left - 8}" y="{y + bh - 3}" font-size="11" text-anchor="end">{k} · {html.escape(SHORT[k])}</text>')
        ws, wo = s * scale, o * scale
        if s:
            out.append(rbar(left, y, ws, bh, "s1", f"{k}: {s} Satisfied", r=0 if o else 4))
        if o:
            out.append(rbar(left + ws + (2 if s else 0), y, wo - (2 if s else 0), bh, "s2", f"{k}: {o} Other Than Satisfied"))
        out.append(f'<text class="ink2" x="{left + ws + wo + 6}" y="{y + bh - 3}" font-size="10">{s}/{s + o}</text>')
    out.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top - 6}" y2="{top + rowh * len(fams)}" stroke-width="1"/>')
    out.append("</svg>")
    return "\n".join(out)


def svg_heatmaps(D):
    W, H, cell = 640, 330, 40
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
           f'aria-label="Risk heat maps: current versus residual">', SVG_STYLE,
           f'<rect class="surface" width="{W}" height="{H}" rx="8"/>',
           '<text class="ink" x="16" y="24" font-size="15" font-weight="600">Enterprise risk: current (as tested) vs residual (target)</text>',
           '<text class="ink2" x="16" y="42" font-size="11">Cell = likelihood × impact; number = count of the 18 risks; color = rating band (label in cell)</text>']
    for gi, (state, title) in enumerate((("current", "Current"), ("residual", "Residual target"))):
        ox, oy = 60 + gi * 300, 70
        grid = defaultdict(list)
        for r in D["risks"]:
            grid[tuple(r[state])].append(r["id"])
        out.append(f'<text class="ink" x="{ox + 2.5 * cell}" y="{oy - 8}" font-size="12" font-weight="600" text-anchor="middle">{title}</text>')
        for L in range(5, 0, -1):
            for I in range(1, 6):
                x, y = ox + (I - 1) * cell, oy + (5 - L) * cell
                b = band(L * I)
                ids = grid.get((L, I), [])
                op = "0.85" if ids else "0.16"
                tip = f"{title}: L{L} × I{I} = {L * I} ({b}); " + (", ".join(ids) if ids else "no risks")
                out.append(f'<rect x="{x + 1}" y="{y + 1}" width="{cell - 2}" height="{cell - 2}" rx="3" fill="{STATUS[b]}" '
                           f'fill-opacity="{op}" data-tip="{html.escape(tip)}"><title>{html.escape(tip)}</title></rect>')
                if ids:
                    ink = "#ffffff" if b in ("Critical",) else "#0b0b0b"
                    out.append(f'<text x="{x + cell / 2}" y="{y + cell / 2 + 5}" font-size="14" font-weight="600" '
                               f'text-anchor="middle" fill="{ink}">{len(ids)}</text>')
            out.append(f'<text class="muted" x="{ox - 8}" y="{oy + (5 - L) * cell + cell / 2 + 4}" font-size="10" text-anchor="end">{L}</text>')
        for I in range(1, 6):
            out.append(f'<text class="muted" x="{ox + (I - 1) * cell + cell / 2}" y="{oy + 5 * cell + 14}" font-size="10" text-anchor="middle">{I}</text>')
        out.append(f'<text class="muted" x="{ox + 2.5 * cell}" y="{oy + 5 * cell + 30}" font-size="10" text-anchor="middle">Impact →</text>')
        out.append(f'<text class="muted" x="{ox - 30}" y="{oy + 2.5 * cell}" font-size="10" text-anchor="middle" transform="rotate(-90 {ox - 30} {oy + 2.5 * cell})">Likelihood →</text>')
    lx = 16
    for b in SEV:
        out.append(f'<rect x="{lx}" y="{H - 20}" width="10" height="10" rx="2" fill="{STATUS[b]}"/><text class="ink2" x="{lx + 14}" y="{H - 11}" font-size="11">{b}</text>')
        lx += 90
    out.append("</svg>")
    return "\n".join(out)


def svg_burndown(m):
    s = m["open_findings_series"]
    W, H, left, right, top, bottom = 640, 280, 44, 90, 58, 44
    pw, ph = W - left - right, H - top - bottom
    maxy = max(x["open"] for x in s)
    maxy = (maxy // 5 + 1) * 5
    d0, d1 = dt.date.fromisoformat(s[0]["date"]), dt.date.fromisoformat(s[-1]["date"])
    span = (d1 - d0).days
    X = lambda ds: left + pw * (dt.date.fromisoformat(ds) - d0).days / span  # noqa: E731
    Y = lambda v: top + ph * (1 - v / maxy)  # noqa: E731
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
           f'aria-label="Open findings over time">', SVG_STYLE, f'<rect class="surface" width="{W}" height="{H}" rx="8"/>',
           '<text class="ink" x="16" y="24" font-size="15" font-weight="600">Open findings over time</text>',
           '<text class="ink2" x="16" y="42" font-size="11">Weekly. A finding leaves the count only at validated closure (or formal risk acceptance)</text>']
    for v in range(0, maxy + 1, 5):
        out.append(f'<line class="grid" x1="{left}" x2="{left + pw}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke-width="1"/>'
                   f'<text class="muted" x="{left - 6}" y="{Y(v) + 3:.1f}" font-size="10" text-anchor="end">{v}</text>')
    for i, (mk, lab) in enumerate((("2026-07-31", "Draft report"), ("2026-08-07", "POA&amp;M baseline"))):
        x = X(mk)
        out.append(f'<line class="axis" x1="{x:.1f}" x2="{x:.1f}" y1="{top}" y2="{top + ph}" stroke-width="1"/>'
                   f'<text class="muted" x="{x + 3:.1f}" y="{top + 10 + 12 * i}" font-size="9">{lab}</text>')
    for key, cls, name in (("open", "l1", "All open findings"), ("open_high", "l2", "Open High/Critical")):
        pts = " ".join(f"{X(p['date']):.1f},{Y(p[key]):.1f}" for p in s)
        out.append(f'<polyline class="{cls}" fill="none" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" points="{pts}"/>')
        for p in s:
            tip = f"{p['date']}: {p[key]} {name.lower()}"
            out.append(f'<circle class="{cls.replace("l", "s")} gap" cx="{X(p["date"]):.1f}" cy="{Y(p[key]):.1f}" r="4" stroke-width="2" '
                       f'data-tip="{html.escape(tip)}"><title>{html.escape(tip)}</title></circle>')
        last = s[-1]
        out.append(f'<text class="ink2" x="{X(last["date"]) + 8:.1f}" y="{Y(last[key]) + 4:.1f}" font-size="11">{last[key]} {name.split()[-1] if key == "open" else "High+"}</text>')
    for p in (s[0], s[len(s) // 2], s[-1]):
        out.append(f'<text class="muted" x="{X(p["date"]):.1f}" y="{top + ph + 16}" font-size="10" text-anchor="middle">{p["date"][5:]}</text>')
    out.append(f'<line class="axis" x1="{left}" x2="{left + pw}" y1="{top + ph}" y2="{top + ph}" stroke-width="1"/>')
    out.append(f'<rect class="s1" x="{left}" y="{H - 16}" width="10" height="3" rx="1"/><text class="ink2" x="{left + 14}" y="{H - 11}" font-size="11">All open findings</text>'
               f'<rect class="s2" x="{left + 140}" y="{H - 16}" width="10" height="3" rx="1"/><text class="ink2" x="{left + 154}" y="{H - 11}" font-size="11">Open High/Critical</text>')
    out.append("</svg>")
    return "\n".join(out)


def svg_findings(m, D):
    W, rowh, bh, left, top = 640, 34, 16, 90, 62
    rows = []
    for s in SEV[1:]:
        fs = [f for f in D["findings"] if f["severity"] == s]
        rows.append((s, sum(f["status"] == "Closed" for f in fs), sum(f["status"] == "Risk Accepted" for f in fs),
                     sum(f["status"] not in ("Closed", "Risk Accepted") for f in fs)))
    H = top + rowh * len(rows) + 30
    maxn = max(sum(r[1:]) for r in rows)
    scale = (W - left - 80) / maxn
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
           f'aria-label="Findings by severity and status">', SVG_STYLE, f'<rect class="surface" width="{W}" height="{H}" rx="8"/>',
           '<text class="ink" x="16" y="24" font-size="15" font-weight="600">Findings by severity and status</text>',
           f'<text class="ink2" x="16" y="42" font-size="11">{m["findings"]["total"]} findings · status as of {m["status_date"]}</text>']
    lx = W - 330
    for cls, name in (("s1", "Closed (validated)"), ("s2", "Open"), ("s3", "Risk accepted")):
        out.append(f'<rect class="{cls}" x="{lx}" y="14" width="10" height="10" rx="2"/><text class="ink2" x="{lx + 14}" y="23" font-size="11">{name}</text>')
        lx += 120 if name != "Open" else 60
    for i, (s, c, a, o) in enumerate(rows):
        y = top + i * rowh
        out.append(f'<text class="ink2" x="{left - 8}" y="{y + bh - 3}" font-size="12" text-anchor="end">{s}</text>')
        x = left
        segs = [(c, "s1", "closed (validated)"), (o, "s2", "open"), (a, "s3", "risk accepted")]
        segs = [sg for sg in segs if sg[0]]
        for j, (n, cls, name) in enumerate(segs):
            w = n * scale - (2 if j < len(segs) - 1 else 0)
            out.append(rbar(x, y, w, bh, cls, f"{s}: {n} {name}", r=4 if j == len(segs) - 1 else 0))
            x += n * scale
        out.append(f'<text class="ink2" x="{x + 6}" y="{y + bh - 3}" font-size="11">{c + a + o}</text>')
    out.append(f'<line class="axis" x1="{left}" x2="{left}" y1="{top - 6}" y2="{top + rowh * len(rows) - 12}" stroke-width="1"/>')
    out.append("</svg>")
    return "\n".join(out)


# ------------------------------------------------------------------ html + md
def tile(label, value, sub):
    return f'<div class="tile"><div class="tl">{html.escape(label)}</div><div class="tv">{html.escape(str(value))}</div><div class="ts">{sub}</div></div>'


def build_html(m, svgs, D):
    c, f, p, a, v, e = m["controls"], m["findings"], m["poam"], m["access_review"], m["vendor"], m["evidence"]
    tiles = "".join([
        tile("Controls satisfied", f"{c['satisfied']} / {c['assessed']}", f"{c['satisfied_pct']}% of assessed · {c['owner_status_changed']} owner-stated statuses corrected"),
        tile("Open findings", f["open"], f"{f['open_high_critical']} High/Critical open · {f['total']} total"),
        tile("POA&M validated closed", f"{p['closed_validated']} / {len(D['poam'])}", f"{len(p['overdue'])} overdue · {len(p['slipped'])} slipped · median {p['median_days_identified_to_validated_closure']:.0f} days to close"),
        tile("Evidence completion", f"{e['completion_pct']}%", f"{e['complete']} of {e['total']} accepted/closed · {e['insufficient']} insufficient"),
        tile("Access-review exceptions", a["exceptions"], f"{a['exceptions_closed']} closed · {a['exceptions_risk_accepted']} accepted · {a['exceptions_open']} open · {a['entitlement_rows_reviewed']} entitlements"),
        tile("Tier 1–2 vendors current", f"{v['tier12_current']} / {v['tier12_total']}", f"{v['vr_total']} VR findings · {v['vr_critical_high']} Critical/High"),
    ])
    top = "".join(f"<tr><td>{r['id']}</td><td>{html.escape(r['title'])}</td><td>{r['score']} {r['band']}</td><td>{r['residual']}</td>"
                  f"<td>{html.escape(r['owner'])}</td><td>{html.escape(r['status'])}</td></tr>" for r in m["risks"]["top5_asof"])
    open_rows = "".join(f"<tr><td>{x['id']}</td><td>{html.escape(x['title'])}</td><td>{x['severity']}</td><td>{x['poam']}</td>"
                        f"<td>{D['pm'][x['poam']]['current_target']}</td><td>{html.escape(x['status'])}</td></tr>"
                        for x in D["findings"] if x["status"] not in ("Closed", "Risk Accepted"))
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>WCP-PROD Assessment Dashboard</title>
<style>
:root {{ color-scheme: light; --page:#f9f9f7; --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --line:#e1e0d9; --accent:#1F4E5A; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ color-scheme: dark; --page:#0d0d0d; --surface:#1a1a19; --ink:#ffffff; --ink2:#c3c2b7; --line:#2c2c2a; --accent:#7fb7c4; }} }}
:root[data-theme="dark"] {{ color-scheme: dark; --page:#0d0d0d; --surface:#1a1a19; --ink:#ffffff; --ink2:#c3c2b7; --line:#2c2c2a; --accent:#7fb7c4; }}
body {{ margin:0; background:var(--page); color:var(--ink); font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }}
main {{ max-width: 1320px; margin: 0 auto; padding: 24px 16px 48px; }}
h1 {{ font-size: 22px; margin: 0 0 4px; }} h2 {{ font-size: 16px; margin: 28px 0 10px; color: var(--accent); }}
.sub {{ color: var(--ink2); font-size: 13px; margin-bottom: 18px; }}
.tiles {{ display:grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 12px; }}
.tile {{ background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 14px; }}
.tl {{ font-size: 12px; color: var(--ink2); }} .tv {{ font-size: 30px; font-weight: 600; margin: 4px 0; }} .ts {{ font-size: 11px; color: var(--muted); }}
.charts {{ display:grid; grid-template-columns: repeat(auto-fit, minmax(420px, 1fr)); gap: 12px; }}
.charts svg {{ width: 100%; height: auto; border: 1px solid var(--line); border-radius: 10px; }}
table {{ width:100%; border-collapse: collapse; background: var(--surface); font-size: 12.5px; }}
th, td {{ text-align:left; padding: 7px 8px; border-bottom: 1px solid var(--line); vertical-align: top; }}
th {{ color: var(--ink2); font-weight: 600; }} td:first-child {{ font-variant-numeric: tabular-nums; white-space: nowrap; }}
.note {{ font-size: 12px; color: var(--ink2); }}
#tip {{ position: fixed; pointer-events: none; background: var(--ink); color: var(--page); font-size: 12px; padding: 6px 8px; border-radius: 6px; display:none; max-width: 320px; }}
@media (max-width: 520px) {{ .charts {{ grid-template-columns: 1fr; }} .tv {{ font-size: 24px; }} }}
</style></head>
<body><main>
<h1>WCP-PROD Security Control Assessment: Executive Dashboard</h1>
<div class="sub">Wrenfield Health (fictional) · simulated NIST SP 800-53 Rev. 5 (Release 5.2.0) assessment · status date {m['status_date']} · every number computed from <code>data/</code> by <code>tools/metrics.py</code> (definitions: metric-definitions.md)</div>
<div class="tiles">{tiles}</div>
<h2>Where the program stands</h2>
<div class="charts">{svgs['family']}{svgs['findings']}{svgs['burndown']}{svgs['heatmap']}</div>
<h2>Top enterprise risks on the status date</h2>
<table><thead><tr><th>ID</th><th>Risk</th><th>Now</th><th>Residual target</th><th>Owner</th><th>Status</th></tr></thead><tbody>{top}</tbody></table>
<h2>Open findings requiring management attention</h2>
<table><thead><tr><th>ID</th><th>Finding</th><th>Severity</th><th>POA&amp;M</th><th>Target</th><th>Status</th></tr></thead><tbody>{open_rows}</tbody></table>
<p class="note">Portfolio exercise. Fictional organization and synthetic data; not an official assessment, audit, or authorization.</p>
</main><div id="tip" role="tooltip"></div>
<script>
const tip = document.getElementById('tip');
document.querySelectorAll('[data-tip]').forEach(el => {{
  el.addEventListener('mousemove', e => {{ tip.textContent = el.dataset.tip; tip.style.display = 'block';
    tip.style.left = Math.min(e.clientX + 12, window.innerWidth - 330) + 'px'; tip.style.top = (e.clientY + 12) + 'px'; }});
  el.addEventListener('mouseleave', () => tip.style.display = 'none');
}});
</script></body></html>"""


def build_md(m):
    c, f, p, a, v, e, r = m["controls"], m["findings"], m["poam"], m["access_review"], m["vendor"], m["evidence"], m["risks"]
    rows = [
        ("MET-02/03", "Controls assessed / Satisfied", f"{c['assessed']} / {c['satisfied']} ({c['satisfied_pct']}%)"),
        ("MET-04", "Validated implementation status", ", ".join(f"{k} {v}" for k, v in c["validated_status"].items())),
        ("MET-05", "Owner-stated statuses corrected by assessor", c["owner_status_changed"]),
        ("MET-06", "Findings total / open", f"{f['total']} / {f['open']}"),
        ("MET-07", "Open High/Critical findings", f"{f['open_high_critical']} ({', '.join(f['open_high_ids'])})"),
        ("MET-08", "Overdue POA&M items / slipped", f"{len(p['overdue'])} ({', '.join(p['overdue'])}) / {len(p['slipped'])} ({', '.join(p['slipped'])})"),
        ("MET-09", "POA&M closed and validated", f"{p['closed_validated']} of {p['total']}"),
        ("MET-09b", "Median days, identification → validated closure", p["median_days_identified_to_validated_closure"]),
        ("MET-10", "Access-review exceptions (closed / accepted / open)", f"{a['exceptions']} ({a['exceptions_closed']} / {a['exceptions_risk_accepted']} / {a['exceptions_open']})"),
        ("MET-11", "Vendor findings / Critical+High", f"{v['vr_total']} / {v['vr_critical_high']}"),
        ("MET-11b", "Tier 1–2 vendors with current assessment", f"{v['tier12_current']} of {v['tier12_total']}"),
        ("MET-12", "Evidence completion", f"{e['completion_pct']}% ({e['complete']} of {e['total']})"),
        ("MET-13", "Risks rated High+ at fieldwork → now → residual target", f"{sum(r['current_bands'][b] for b in ('Critical', 'High'))} → {sum(r['asof_bands'][b] for b in ('Critical', 'High'))} → {sum(r['residual_bands'][b] for b in ('Critical', 'High'))}"),
    ]
    top = md_table([{"Risk": x["id"], "Title": x["title"], "At fieldwork": x["fieldwork"], "Now": f"{x['score']} {x['band']}",
                     "Residual target": x["residual"], "Owner": x["owner"], "Status": x["status"]} for x in r["top5_asof"]],
                   ["Risk", "Title", "At fieldwork", "Now", "Residual target", "Owner", "Status"])
    return f"""# Executive Dashboard

> Generated by `tools/metrics.py` from `data/`. Interactive version: [index.html](index.html). Excel version with live formulas: [workbook/wrenfield-grc-workbook.xlsx](../workbook/wrenfield-grc-workbook.xlsx) (sheet *Dashboard*), cross-checked against these values by `tools/check_formulas.py`. Every metric is defined in [metric-definitions.md](metric-definitions.md).

**Status date {m['status_date']}**

| ID | Metric | Value |
|---|---|---|
{chr(10).join(f'| {a} | {b} | {c_} |' for a, b, c_ in rows)}

![Control results by family](control-results-by-family.svg)
![Findings by severity and status](findings-by-severity.svg)
![Open findings over time](open-findings-trend.svg)
![Risk heat maps](risk-heatmap.svg)

## Top enterprise risks on the status date
"Now" = residual once treatment is validated or accepted, otherwise the as-tested score.

{top}
"""


def key_metrics_table(m):
    c, f, p, a, v, e, r = m["controls"], m["findings"], m["poam"], m["access_review"], m["vendor"], m["evidence"], m["risks"]
    hi = lambda k: sum(r[k][b] for b in ("Critical", "High"))  # noqa: E731
    rows = [
        ("Controls assessed (SP 800-53 Rev. 5)", f"{c['assessed']} assessed + {c['not_applicable']} N/A, across 18 families"),
        ("Satisfied / Other Than Satisfied", f"{c['satisfied']} / {c['other_than_satisfied']} ({c['satisfied_pct']}% satisfied)"),
        ("Owner-stated statuses corrected by testing", f"{c['owner_status_changed']} of {c['in_scope']}"),
        ("Findings (High / Moderate / Low)", f"{f['total']} ({f['by_severity']['High']} / {f['by_severity']['Moderate']} / {f['by_severity']['Low']}), 0 Critical"),
        ("Findings closed with validation", f"{p['closed_validated']} of {p['total']} (median {p['median_days_identified_to_validated_closure']:.0f} days)"),
        ("Open High findings", f"{f['open_high_critical']} ({', '.join(f['open_high_ids'])})"),
        ("POA&M overdue / slipped / risk-accepted", f"{len(p['overdue'])} / {len(p['slipped'])} / {len(p['risk_accepted'])}"),
        ("Access review", f"{a['entitlement_rows_reviewed']} entitlements, {a['exceptions']} exceptions ({a['exceptions_closed']} closed, {a['exceptions_risk_accepted']} accepted, {a['exceptions_open']} open)"),
        ("Vendor risk (Quarrystone)", f"{v['vr_total']} findings ({v['vr_by_severity'].get('Critical', 0)} Critical, contained) · decision: {v['treatment']}"),
        ("Tier 1–2 vendors with current assessment", f"{v['tier12_current']} of {v['tier12_total']}"),
        ("Evidence completion", f"{e['completion_pct']}% ({e['complete']} of {e['total']}); {e['insufficient']} items insufficient, each became part of a finding"),
        ("Enterprise risks rated High+", f"{hi('current_bands')} at fieldwork → {hi('asof_bands')} now → {hi('residual_bands')} at target ({r['total']} risks)"),
    ]
    header = "| Measure | Result (status date " + m["status_date"] + ") |" + chr(10) + "|---|---|" + chr(10)
    return header + chr(10).join(f"| {k} | {v_} |" for k, v_ in rows)


def inject(m):
    from common import replace_between_markers
    table = key_metrics_table(m)
    for rel in ("README.md", "docs/executive-reporting/security-assessment-report.md", "docs/executive-reporting/executive-briefing.md"):
        path = ROOT / rel
        if path.exists() and "<!-- GEN:keymetrics:START -->" in path.read_text(encoding="utf-8"):
            replace_between_markers(path, "keymetrics", table)


def main():
    D = load_all()
    m = compute(D)
    write_json(OUT / "metrics.json", m)
    svgs = {"family": svg_family(m), "findings": svg_findings(m, D), "burndown": svg_burndown(m), "heatmap": svg_heatmaps(D)}
    for name, key in (("control-results-by-family", "family"), ("findings-by-severity", "findings"),
                      ("open-findings-trend", "burndown"), ("risk-heatmap", "heatmap")):
        (OUT / f"{name}.svg").write_text(svgs[key], encoding="utf-8")
    (OUT / "index.html").write_text(build_html(m, svgs, D), encoding="utf-8")
    (OUT / "dashboard.md").write_text(build_md(m), encoding="utf-8")
    inject(m)
    print(json.dumps(m["dashboard_crosscheck"]))


if __name__ == "__main__":
    main()
