# CHECKPOINT: Wrenfield GRC Assessment (portfolio project)

**Status (2026-09-23): v1 COMPLETE.** All 15 phases (0–14) built, generated, and verified. Local git only (not yet pushed).

## What this is
A simulated NIST SP 800-53 Rev. 5 (Release 5.2.0) security control assessment of the fictional healthcare SaaS **Wrenfield Health** (system WCP-PROD), framed as pre-contract readiness for a fictional state Medicaid agency (SHCA). Status date for all metrics: **2026-09-18**.

## How to regenerate / verify
```bash
python -m venv .venv && .venv/Scripts/pip install -r requirements.txt
python tools/run_all.py   # review_engine → assessment_tests → build → metrics → check_formulas (pycel) → validate → LF normalize
pytest -q                 # 7 regression tests
```
- **Source of truth:** `data/*.yaml` plus `access-review/source-exports/*.csv` plus `evidence/**`. Everything in controls/, risk/, audit/, findings/, poam/, vendor-risk/*.xlsx|md, workbook/, templates/*.csv|xlsx, dashboard/, docs/assessment/{worksheets,test-results,traceability-matrix,integrity-check}.md, and docs/scope/business-requirements.md is **generated**.
- `README.md`, `docs/executive-reporting/*.md` have `<!-- GEN:keymetrics -->` blocks filled by `tools/metrics.py`.
- No LibreOffice on this host: formulas are verified with **pycel** (1,232 formulas, 0 errors, dashboard cross-check 0 mismatches). pycel lacks COUNTA/ROWS/array COUNTIF; use wildcard COUNTIF and helper columns.

## Key numbers (all computed)
61 controls / 18 families (31 Satisfied, 29 OTS, 1 N/A) · 27 owner-stated statuses corrected · 19 findings (7 High / 10 Mod / 2 Low) · 7 closed with validation · 4 open High · 2 overdue POA&M, 1 slipped, 1 risk-accepted (RACC-001) · access review 106 rows / 20 exceptions / 1 FP · vendor 12 VR (1 Critical) · 78 evidence, 86% complete · 18 risks (14 High at fieldwork → 11 now → 0 target) · 43/43 integrity rules.

## Decisions made
- Fictional vendors for everything assessed; real platforms (AWS/Okta/GitHub/Google Workspace) named only as stack, with no claims about them.
- Standards verified 2026-09-23 via NIST CSRC/OSCAL (see docs/assessment/nist-800-53-strategy.md §1). Control titles were not machine-verified against the full OSCAL catalog (download not performed); `tools/verify_catalog.py` does it when given the JSON.
- CSVs are written with UTF-8 BOM (Excel-friendly). `.gitattributes` enforces LF.

## Possible next steps
- Push to GitHub as `InnovaeonLabs/wrenfield-grc-assessment` (README badge and resume bullets already use this name).
- Run `tools/verify_catalog.py` against the official OSCAL catalog JSON.
- Optional v2: OSCAL-format SSP/POA&M export; a second vendor deep-dive; a Q4 "continuous monitoring" status update.
