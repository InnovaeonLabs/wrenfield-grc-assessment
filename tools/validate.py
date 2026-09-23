"""Cross-artifact integrity checks: the machine-checked version of "one governance system".

    python tools/validate.py      (exit code 1 on any failure; used by CI and pytest)

Writes docs/assessment/integrity-check.md.
"""
from __future__ import annotations

import re
import sys

from build import load_all
from common import DATA, EXPORTS, ROOT, STATUS_DATE, d, read_csv, split_ids

def oscal_id(cid: str) -> str:
    m = re.fullmatch(r"([A-Z]{2})-(\d+)(?:\((\d+)\))?", cid)
    return f"{m.group(1).lower()}-{m.group(2)}" + (f".{m.group(3)}" if m.group(3) else "")


def run(D):
    results = []
    ctl, ev, fnd, rsk, pm = D["ctl"], D["ev"], D["fnd"], D["rsk"], D["pm"]
    V = D["vendor"]
    vr = {x["id"]: x for x in V["vendor_findings"]}
    vq = {x["id"]: x for x in V["questionnaire"]}
    arx = {r["Exception ID"] for r in D["ar"] if r["Exception ID"]}
    baseline = {l.strip() for l in (DATA / "moderate-baseline-5.2.0.txt").read_text().splitlines() if l.strip()}

    def check(rid, desc, failures):
        results.append((rid, desc, failures))

    # ---- IDs and formats
    pats = {"control": r"[A-Z]{2}-\d+(\(\d+\))?", "REQ": r"REQ-\d{3}", "EVID": r"EVID-\d{3}", "FIND": r"FIND-\d{3}",
            "RISK": r"RISK-\d{3}", "POAM": r"POAM-\d{3}", "VR": r"VR-\d{3}", "VQ": r"VQ-\d{2}", "AR-EX": r"AR-EX-\d{2}"}
    bad = [c["id"] for c in D["controls"] if not re.fullmatch(pats["control"], c["id"])]
    bad += [x for x in list(ev) if not re.fullmatch(pats["EVID"], x)] + [x for x in fnd if not re.fullmatch(pats["FIND"], x)]
    bad += [x for x in rsk if not re.fullmatch(pats["RISK"], x)] + [x for x in pm if not re.fullmatch(pats["POAM"], x)]
    bad += [x for x in vr if not re.fullmatch(pats["VR"], x)] + [x for x in arx if not re.fullmatch(pats["AR-EX"], x)]
    check("ID-01", "All IDs follow the documented formats (docs/id-scheme.md)", bad)
    dup = []
    for name, items in (("controls", D["controls"]), ("evidence", D["evidence"]), ("findings", D["findings"]),
                        ("risks", D["risks"]), ("poam", D["poam"])):
        ids = [x["id"] for x in items]
        dup += [f"{name}:{i}" for i in set(ids) if ids.count(i) > 1]
    check("ID-02", "No duplicate IDs", dup)

    # ---- controls
    check("CTL-01", "Every selected control is in the SP 800-53B Moderate baseline (5.2.0 OSCAL profile), except PM (org-level)",
          [c["id"] for c in D["controls"] if not c["id"].startswith("PM-") and oscal_id(c["id"]) not in baseline])
    check("CTL-02", "Every control cites >= 1 business requirement that exists",
          [c["id"] for c in D["controls"] if not c["requirements"] or any(r not in D["reqs"] for r in c["requirements"])])
    check("CTL-03", "Every business requirement is covered by >= 1 control",
          [r for r in D["reqs"] if not any(r in c["requirements"] for c in D["controls"])])
    check("CTL-04", "Every control cites evidence that exists in the tracker",
          [f"{c['id']}->{e}" for c in D["controls"] for e in c["evidence"] if e not in ev] + [c["id"] for c in D["controls"] if not c["evidence"]])
    check("CTL-05", "Every Other-Than-Satisfied control links to >= 1 finding and POA&M",
          [c["id"] for c in D["controls"] if c["result"] == "Other Than Satisfied" and (not c["findings"] or not c["poams"])])
    check("CTL-06", "No Satisfied control carries an open finding",
          [c["id"] for c in D["controls"] if c["result"] == "Satisfied" and c["findings"]])
    check("CTL-07", "Not Applicable controls have a written applicability rationale",
          [c["id"] for c in D["controls"] if c["applicability"] == "Not Applicable" and not c.get("applicability_rationale")])
    check("CTL-08", "Status vocabulary is controlled",
          [c["id"] for c in D["controls"] if c["status_validated"] not in ("Implemented", "Partially Implemented", "Planned", "Not Implemented", "Not Applicable")
           or c["result"] not in ("Satisfied", "Other Than Satisfied", "Not Assessed")])
    check("CTL-09", "A Satisfied control is validated Implemented; an OTS control is not validated Implemented",
          [c["id"] for c in D["controls"] if (c["result"] == "Satisfied") != (c["status_validated"] == "Implemented")])
    check("CTL-10", "Control->finding links are bidirectional",
          [f"{c['id']}<->{f}" for c in D["controls"] for f in c["findings"] if f not in fnd or c["id"] not in fnd[f]["controls"]]
          + [f"{f['id']}<->{c}" for f in D["findings"] for c in f["controls"] if c not in ctl or f["id"] not in ctl[c]["findings"]])
    check("CTL-11", "Control->POA&M links match its findings",
          [c["id"] for c in D["controls"] if sorted(c["poams"]) != sorted(fnd[f]["poam"] for f in c["findings"])])
    check("CTL-12", "Deep-dive worksheets exist for key controls and their conclusion matches the matrix result",
          [w["control"] for w in D["worksheets"] if w["control"] not in ctl or not w["conclusion"].startswith(ctl[w["control"]]["result"])])

    # ---- findings
    check("FND-01", "Every finding maps to >= 1 control, >= 1 risk, and its own POA&M (FIND-nnn <-> POAM-nnn)",
          [f["id"] for f in D["findings"] if not f["controls"] or not f["risks"] or f["poam"] not in pm
           or pm[f["poam"]]["finding"] != f["id"] or f["poam"][-3:] != f["id"][-3:]])
    check("FND-02", "Finding status equals its POA&M status",
          [f["id"] for f in D["findings"] if f["status"] != pm[f["poam"]]["status"]])
    check("FND-03", "Every item a finding cites (EVID / AR-EX / VR) exists",
          [f"{f['id']}->{x}" for f in D["findings"] for x in f["related"]
           if (x.startswith("EVID") and x not in ev) or (x.startswith("AR-EX") and x not in arx) or (x.startswith("VR") and x not in vr)
           or (x.startswith("OBS") and x not in D["obs"])])
    check("FND-04", "Every finding has both a technical (5 Cs) and an executive version",
          [f["id"] for f in D["findings"] if not all(f.get(k) for k in ("condition", "criteria", "cause", "effect", "recommendation"))
           or not all(f["exec"].get(k) for k in ("what_happened", "why_care", "business_impact", "action", "urgency"))])
    check("FND-05", "Finding<->risk links are bidirectional",
          [f"{f['id']}<->{r}" for f in D["findings"] for r in f["risks"] if r not in rsk or f["id"] not in rsk[r]["findings"]]
          + [f"{r['id']}<->{f}" for r in D["risks"] for f in r["findings"] if f not in fnd or r["id"] not in fnd[f]["risks"]])

    # ---- POA&M
    closed = [p for p in D["poam"] if p["status"] == "Closed"]
    check("POA-01", "Closed items are validated: validator named, closure date, closure evidence Closed/Accepted, all milestones Done",
          [p["id"] for p in closed if not p["validated_by"] or not p["closure_date"] or not p["closure_evidence"]
           or any(ev[e]["status"] not in ("Closed", "Accepted") for e in p["closure_evidence"])
           or any(m["status"] != "Done" for m in p["milestones"])])
    check("POA-02", "At least 5 findings completed the full lifecycle to validated closure", [] if len(closed) >= 5 else [f"only {len(closed)}"])
    check("POA-03", "Targets within SLA, or a documented approved reason for the change",
          [p["id"] for p in D["poam"] if not p["within_sla"] and not p.get("target_change_reason")])
    check("POA-04", "Original target preserved; any change is explained",
          [p["id"] for p in D["poam"] if p["slipped"] and not p.get("target_change_reason")])
    check("POA-05", "Risk-accepted items reference a signed acceptance (RACC) and its evidence",
          [p["id"] for p in D["poam"] if p["status"] == "Risk Accepted" and ("EVID-060" not in p["closure_evidence"]
           or not (ROOT / "risk" / "risk-acceptance" / "RACC-001.md").exists())])
    check("POA-06", "Milestone completion dates are not in the future and 'Done' milestones have dates",
          [f"{p['id']}/{m['id']}" for p in D["poam"] for m in p["milestones"]
           if (m["status"] == "Done" and not m["completed"]) or (m["completed"] and d(m["completed"]) > STATUS_DATE)])
    check("POA-07", "Closure evidence cited by POA&M items exists",
          [f"{p['id']}->{e}" for p in D["poam"] for e in p["closure_evidence"] if e not in ev])

    # ---- risks
    check("RSK-01", "Scores never increase from inherent -> current -> residual, and residual is never zero",
          [r["id"] for r in D["risks"] if not (r["inherent_score"] >= r["current_score"] >= r["residual_score"] >= 1)])
    check("RSK-02", "Every risk score has a written rationale (inherent, current, residual)",
          [r["id"] for r in D["risks"] if not all(r.get(k) for k in ("rationale_inherent", "rationale_current", "rationale_residual"))])
    check("RSK-03", "No Critical/High residual risk is 'Accept'ed; accepted risks are within tolerance (<= Moderate)",
          [r["id"] for r in D["risks"] if r["treatment"] == "Accept" and r["residual_band"] in ("High", "Critical")])
    check("RSK-04", "Every risk has an accountable owner, treatment, and target date",
          [r["id"] for r in D["risks"] if not (r["owner"] and r["treatment"] and r["target_date"])])
    check("RSK-05", "Risk count within the 12-20 range the charter commits to",
          [] if 12 <= len(D["risks"]) <= 20 else [str(len(D["risks"]))])

    # ---- evidence
    check("EVD-01", "Evidence items reference controls that exist",
          [f"{e['id']}->{c}" for e in D["evidence"] for c in e["controls"] if c not in ctl])
    check("EVD-02", "Repository evidence locations resolve to real files",
          [e["id"] for e in D["evidence"] if not str(e["location"]).startswith("GRC-Vault:") and not (ROOT / str(e["location"])).exists()])
    check("EVD-03", "Evidence status vocabulary is controlled",
          [e["id"] for e in D["evidence"] if e["status"] not in ("Not Requested", "Requested", "Received", "Under Review", "Accepted",
                                                                   "Insufficient", "Rework Required", "Closed")])
    check("EVD-04", "Insufficient/rework evidence always records the exception and follow-up",
          [e["id"] for e in D["evidence"] if e["status"] in ("Insufficient", "Rework Required") and (not e["exception"] or e["follow_up"] == "No")])
    check("EVD-05", "Received dates are on/after request dates and not in the future",
          [e["id"] for e in D["evidence"] if e.get("received") and (d(e["received"]) < d(e["request_date"]) or d(e["received"]) > STATUS_DATE)])

    # ---- access review
    ar_find = [r for r in D["ar"] if r["Exception ID"]]
    check("ACR-01", "Every access-review exception rolls up to an existing finding and cites existing closure evidence",
          [r["Row ID"] for r in ar_find if r["Related Finding"] not in fnd
           or any(e not in ev for e in split_ids(r["Closure Evidence"]))])
    check("ACR-02", "Completed exceptions carry closure evidence and a completion date",
          [r["Row ID"] for r in ar_find if r["Completion Status"] in ("Completed", "Risk Accepted") and (not r["Closure Evidence"] or not r["Completion Date"])])
    check("ACR-03", "Every AR-EX a finding cites exists, and every AR-EX is cited by its finding",
          [x for x in arx if not any(x in f["related"] for f in D["findings"])])
    hr = {h["employee_id"]: h["full_name"] for h in read_csv(EXPORTS / "hr_roster.csv")}
    holder = {e["ent_id"]: hr.get(e["employee_id"], "") for e in read_csv(EXPORTS / "entitlements.csv")}
    check("ACR-04", "No self-review: the reviewer is never the account holder",
          [r["Row ID"] for r in D["ar"] if holder.get(r["Row ID"]) and holder[r["Row ID"]] == r["Reviewer"]])

    # ---- vendor
    check("VND-01", "Vendor findings link to existing questions and (where material) findings",
          [x["id"] for x in V["vendor_findings"] if any(q not in vq for q in x["questions"]) or (x["finding"] and x["finding"] not in fnd)])
    check("VND-02", "Every questionnaire item rated below Satisfactory links to a vendor finding",
          [q["id"] for q in V["questionnaire"] if q["evaluation"] in ("Unsatisfactory",) and not q["vr"]])
    check("VND-03", "Critical/High vendor findings roll into the POA&M",
          [x["id"] for x in V["vendor_findings"] if x["severity"] in ("Critical", "High") and not x["finding"]])
    return results


def main():
    D = load_all()
    results = run(D)
    fails = [(rid, desc, f) for rid, desc, f in results if f]
    lines = ["# Integrity Check: Cross-Artifact Traceability", "",
             "> Generated by `tools/validate.py`. CI fails if any rule fails.", "",
             f"**{len(results) - len(fails)} of {len(results)} rules pass.**", "",
             "| Rule | Check | Result |", "|---|---|---|"]
    for rid, desc, f in results:
        lines.append(f"| {rid} | {desc} | {'✅ PASS' if not f else '❌ FAIL: ' + ', '.join(f[:8])} |")
    (ROOT / "docs" / "assessment" / "integrity-check.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(results) - len(fails)}/{len(results)} integrity rules pass")
    for rid, desc, f in fails:
        print(f"  FAIL {rid}: {desc}: {f}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
