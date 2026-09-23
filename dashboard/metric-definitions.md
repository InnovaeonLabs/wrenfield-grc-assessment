# Metric Definitions

Every dashboard number is computed from `data/` by [`tools/metrics.py`](../tools/metrics.py) **and** by live formulas in [workbook/wrenfield-grc-workbook.xlsx](../workbook/wrenfield-grc-workbook.xlsx) (sheet *Dashboard*). [`tools/check_formulas.py`](../tools/check_formulas.py) fails the build if the two disagree.

**Anti-fake-precision rules:** whole-number percentages only, **always with the denominator** ("31 of 60"); no averaging of ordinal risk scores; risk posture is reported as *counts per band*, never a summed "risk score"; the status date is fixed (2026-09-18) so figures reproduce.

| ID | Metric | Calculation | Excel formula (Dashboard sheet) | Why it matters / caveat |
|---|---|---|---|---|
| MET-01 | Controls in scope | Rows in the control matrix | `COUNTIF(Controls!A:A,"?*")` | Scope size; tailored subset of the Moderate baseline, not the full baseline |
| MET-02 | Controls assessed | Result ∈ {Satisfied, Other Than Satisfied} | `COUNTIF(result,"Satisfied")+COUNTIF(result,"Other Than Satisfied")` | Excludes Not Applicable (AC-18) |
| MET-03 / 03a | Controls Satisfied / % | Result = Satisfied; ÷ MET-02 | `COUNTIF(...)`; `ROUND(MET-03/MET-02,2)` | **Selection was risk-weighted toward known problem areas**, so this is not a whole-program pass rate |
| MET-04a–c | Validated implementation status | Count by assessor-validated status | `COUNTIF(validated,...)` | Owner-stated vs validated is shown separately |
| MET-05 | Owner-stated statuses corrected | Owner-stated ≠ validated | `COUNTIF(changed,"Yes")` | Indicates self-assessment optimism; the key input to the SSP rewrite (FIND-017) |
| MET-06 / 06a | Findings total / open | Open = not Closed and not Risk Accepted | `COUNTIF(Findings!A:A,"FIND-*")`, minus closed and accepted | Accepted risks are tracked but not "open work" |
| MET-07 | Open High/Critical findings | Severity High/Critical and status ≠ Closed | `COUNTIFS(sev,"High",status,"<>Closed")+…` | Measured against SHCA's 90-day High rule |
| MET-08 / 08a | Overdue / slipped POA&M | Overdue = not Closed/Accepted and current target < status date; slipped = current ≠ original target | `COUNTIF(POAM!Overdue,"Yes")` | Slips must carry an approved reason (integrity rule POA-04) |
| MET-09 | POA&M closed and validated | Status = Closed (validation required by rule POA-01) | `COUNTIF(status,"Closed")` | "Done" by the owner is not "Closed" |
| MET-09b | Median days, identification → validated closure | Median over closed items | (Python only) | Median, not mean: robust to the fast FIND-012 fix |
| MET-10 / 10a | Access-review exceptions / rows | Distinct AR-EX IDs; rows carrying one | `SUM(helper)`; `COUNTIF(ex,"AR-EX-*")` | Exceptions roll up to 7 findings |
| MET-11 / 11a | Vendor findings / Critical+High | Count of VR items | `COUNTIF(VendorFindings!A:A,"VR-*")` | From the Quarrystone deep assessment |
| MET-11b / 11c | Tier 1–2 vendors current / total | Tier from inherent-score formula; current = next due ≥ status date | `COUNTIFS(tier,"<=2",current,"Yes")` | Program health (FIND-015) |
| MET-12 | Evidence completion % | (Accepted + Closed) ÷ all requested items | `ROUND((COUNTIF(..,"Accepted")+COUNTIF(..,"Closed"))/COUNTIF(ids,"EVID-*"),2)` | **Insufficient ≠ complete**: an Insufficient item is a finding, not progress |
| MET-13a / 13b | Risks rated High+ (current → residual target) | Count by band | `COUNTIF(band,"High")+COUNTIF(band,"Critical")` | Target, not achieved, until POA&M validation |
