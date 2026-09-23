# Project Roadmap: Execution Phases 0–14

Every phase is **built**, not just planned. For each phase: objective · activities · artifact · key fields · populated sample · decision rationale · quality checks · output · GitHub location · interview talking point.

```
IDENTIFY REQUIREMENTS → IMPLEMENT CONTROLS → COLLECT EVIDENCE → TEST EFFECTIVENESS → IDENTIFY GAPS
→ ASSESS RISK → ASSIGN OWNERSHIP → REMEDIATE → TRACK PROGRESS → REPORT TO MANAGEMENT
   Ph 0–2          Ph 3              Ph 4             Ph 5–6             Ph 6, 9
     Ph 7–8          Ph 9–10           Ph 10–11     Ph 11              Ph 12
```

---

### Phase 0: Project charter and scope
| | |
|---|---|
| **Objective** | Define why the assessment exists, what is in scope, who decides what, and how success is measured |
| **Activities** | Business case (SHCA CSA, Lakemont finding, Board request); boundary; RACI separating assessor determinations from management remediation; timeline; engagement risks |
| **Artifacts** | [project-charter.md](scope/project-charter.md), [scope-statement.md](scope/scope-statement.md), [DISCLAIMER.md](../DISCLAIMER.md) |
| **Key fields** | Objectives O1–O7 with success measures; in/out-of-scope table with rationale; periods; scope change log |
| **Sample** | *"AC-18 Not Applicable: no wireless in boundary"*; scope v1.1 added the Quarrystone portal after walkthroughs |
| **Rationale** | One primary scenario (pre-contract readiness) with two supporting pressures makes the "why now" credible |
| **Quality checks** | Every out-of-scope item has a reason; periods are defined before testing |
| **Talking point** | "I wrote the RACI so the assessor owns *determinations* and management owns *remediation and risk acceptance*. That separation is SP 800-37's independence principle." |

### Phase 1: Organization and system profile
| | |
|---|---|
| **Objective** | Understand the business well enough to judge risk |
| **Activities** | Org profile, data types, systems, vendors, obligations, threats; FIPS 199 categorization with a challenged decision; data-flow diagram |
| **Artifacts** | [organization-profile.md](scope/organization-profile.md), [system-profile.md](scope/system-profile.md), [business-requirements.md](scope/business-requirements.md) (24 REQs) |
| **Sample** | Integrity categorized Moderate, not High, because RPM alerts are advisory. The recorded trigger to revisit that decision is RA-2 |
| **Quality checks** | Every threat maps to control families; every requirement maps to at least 1 control (rule CTL-03) |
| **Talking point** | "The data-flow diagram showed the full PHI extract leaving through an unsupported Windows host, a single path that tied five controls and two risks together." |

### Phase 2: Framework selection and control scoping
| | |
|---|---|
| **Objective** | Verify the current standard and select a defensible control subset |
| **Activities** | Verified SP 800-53 Rev. 5 **Release 5.2.0** (2025-08-27) on CSRC and OSCAL; mapped related publications; tailored from the 287-control Moderate baseline to 61 |
| **Artifacts** | [nist-800-53-strategy.md](assessment/nist-800-53-strategy.md), [assessment-plan.md](assessment/assessment-plan.md), [id-scheme.md](id-scheme.md), `data/moderate-baseline-5.2.0.txt` |
| **Rationale** | Contract drivers first, then threat weighting, then known problem areas, plus deliberately "expected-to-pass" controls to check for bias |
| **Quality checks** | Rule CTL-01: every control is in the official Moderate profile (PM excepted, since the PM family is not baseline-allocated) |
| **Talking point** | "I didn't test all 287. I showed why these 61, including ones I expected to pass, and noted that 5.2.0's new SI-2(7) isn't in Moderate but is worth tailoring in." |

### Phase 3: NIST 800-53 control matrix
| | |
|---|---|
| **Objective** | One row per control, from requirement to remediation |
| **Artifacts** | [nist-800-53-control-matrix.xlsx/csv](../controls/), [control-matrix.md](../controls/control-matrix.md) |
| **Key fields (33)** | ID, family, name, baseline, requirement summary, applicability plus rationale, origination, system, owner, REQs, **owner-stated vs assessor-validated status**, implementation, evidence required, available, and location, evidence level, method, expected vs actual, result, gap, risk rating, RISK/FIND/POAM IDs, observations, reviewed dates, CSF function |
| **Sample** | AC-2(3): owner said Implemented, validated as Partially; 16 of 19 within 24h; FIND-001 → POAM-001, closed 2026-09-10 |
| **Quality checks** | Rules CTL-04 to CTL-12 (evidence exists, OTS has a finding, bidirectional links, worksheet conclusions match) |
| **Talking point** | "27 of 61 owner-stated statuses didn't survive testing. That became the SSP rewrite finding." |

### Phase 4: Evidence request and collection
| | |
|---|---|
| **Objective** | Get reliable, complete evidence, and reject what isn't |
| **Artifacts** | [evidence-tracker.xlsx/csv](../audit/), [evidence-request-list.md](../audit/evidence-request-list.md), [evidence-quality-guide.md](../audit/evidence-quality-guide.md), [evidence/](../evidence/) |
| **Key fields** | EVID, controls, request, artifact, owner, request/due/received dates, status (8 controlled values), period, location, reviewer, result, **evidence level**, sufficiency, exception, follow-up, days late (formula) |
| **Sample** | EVID-009 screenshot **Insufficient**, replaced by EVID-008 (the export showed 412 of 412 approvals) |
| **Talking point** | "A policy is design evidence, a config export is implementation evidence, and only population testing shows operating effectiveness." |

### Phase 5: Access-control review
| | |
|---|---|
| **Objective** | Certify every privileged, PHI, and non-human entitlement |
| **Artifacts** | [access-review.xlsx/csv](../access-review/), [findings.md](../access-review/findings.md), [source-exports/](../access-review/source-exports/), [`review_engine.py`](../tools/review_engine.py) |
| **Sample** | 106 rows → 29 flagged → 20 exceptions + 1 false positive → 7 findings |
| **Quality checks** | Undispositioned flag fails the run; no self-review (ACR-04); every exception has closure evidence |
| **Talking point** | "The engine called `rgupta2` terminated. I reclassified it as a duplicate. Same fix, different root cause, different finding." |

### Phase 6: Control testing
| | |
|---|---|
| **Objective** | Examine/Interview/Test with expected vs actual |
| **Artifacts** | [worksheets/](assessment/worksheets/) (15 controls, 54 steps), [assessment-procedures.csv](../controls/assessment-procedures.csv), [test-results/](assessment/test-results/) (5 scripted tests) |
| **Sample** | TP-SI-2-02: 47 of 61 within SLA; Engineering's "not exploitable" claim recorded and challenged |
| **Talking point** | "Interview never satisfied a control on its own. It pointed me to what to test." |

### Phase 7: Risk assessment and risk register
| | |
|---|---|
| **Objective** | Translate weaknesses into business risk with a repeatable method |
| **Artifacts** | [risk-methodology.md](../risk/risk-methodology.md) (approved **before** scoring), [risk-register.xlsx/csv/md](../risk/), [RACC-001](../risk/risk-acceptance/RACC-001.md) |
| **Key fields** | Inherent, current (as tested), and residual L×I with formula ratings, plus a written rationale for each |
| **Sample** | RISK-007 treated by **Avoid** (decommission), residual L1×I4 |
| **Quality checks** | Scores never increase down the chain; residual never 0; no High+ residual accepted (RSK-01 to 03) |
| **Talking point** | "A control that failed testing gets no credit in the current score. Otherwise the register lies." |

### Phase 8: Vendor-risk assessment
| | |
|---|---|
| **Objective** | Program-level vendor oversight plus a deep assessment of the riskiest vendor |
| **Artifacts** | [vendor-assessment.xlsx/md](../vendor-risk/), [vendor-questionnaire.xlsx](../vendor-risk/vendor-questionnaire.xlsx), [vendor-summary.md](../vendor-risk/vendor-summary.md), SOC 2 workpaper [EVID-050](../evidence/SR/EVID-050_quarrystone-soc2-review-workpaper.md) |
| **Sample** | VR-001 Critical offshore access, found by interview. VR-003 was *our* over-sharing |
| **Talking point** | "Three of twelve vendor findings were Wrenfield's own, from reading the CUECs." |

### Phase 9: Findings and gap analysis
| | |
|---|---|
| **Objective** | Consolidate into control-level findings with root causes |
| **Artifacts** | [findings-register.xlsx/csv/md](../findings/) (19 findings + 6 observations) |
| **Format** | 5 Cs (condition, criteria, cause, effect, recommendation), management response, **executive version** |
| **Talking point** | "Findings roll up by root cause. Twenty account exceptions are really seven control failures." |

### Phase 10: POA&M development
| | |
|---|---|
| **Objective** | Every finding tracked to closure with owner, milestones, SLA |
| **Artifacts** | [poam.xlsx/csv/md](../poam/), `poam-milestones.csv` |
| **Key fields** | All prompt fields plus SLA date, original vs current target, change reason, formula-driven % complete, days open, overdue, slipped |
| **Talking point** | "Accepted risks stay on the POA&M so they are re-decided at expiry, not forgotten." |

### Phase 11: Remediation validation
| | |
|---|---|
| **Objective** | Close only on independent evidence |
| **Artifacts** | [lifecycle-traces.md](../poam/lifecycle-traces.md) (7 full lifecycles), [termination-deprovisioning-validation.md](assessment/test-results/termination-deprovisioning-validation.md), before/after evidence pairs |
| **Sample** | POAM-013: observed a live restore (3h41m vs 4h RTO). POAM-003: design evidence **rejected** |
| **Talking point** | "Remediated is not the same as validated. I re-ran the same test on new data." |

### Phase 12: Executive reporting
| | |
|---|---|
| **Objective** | Decisions, not data dumps |
| **Artifacts** | [security-assessment-report.md](executive-reporting/security-assessment-report.md), [executive-briefing.md](executive-reporting/executive-briefing.md), [dashboard](../dashboard/dashboard.md) ([HTML](../dashboard/index.html)), [metric-definitions.md](../dashboard/metric-definitions.md), Excel Dashboard sheet with live formulas |
| **Quality checks** | Every metric has a denominator and definition; Excel and Python agree (1,232 formulas, 0 errors) |
| **Talking point** | "The briefing asks the Board for three decisions. It doesn't ask them to read 61 controls." |

### Phase 13: GitHub / portfolio packaging
| | |
|---|---|
| **Artifacts** | [README](../README.md) (30-second, 5-minute, deep dive), [templates/](../templates/), [screenshots/](../screenshots/), CI workflow `.github/workflows/grc-ci.yml`, [lessons-learned.md](lessons-learned.md), [quality-review.md](quality-review.md) |
| **Quality checks** | `python tools/run_all.py` regenerates everything; `pytest` (7 regression tests); 43 integrity rules in CI |

### Phase 14: Resume and interview preparation
| | |
|---|---|
| **Artifacts** | [career/resume-bullets.md](../career/resume-bullets.md), [career/interview-prep.md](../career/interview-prep.md), [career/skill-to-evidence-matrix.md](../career/skill-to-evidence-matrix.md) |
| **Rule** | Every bullet and answer points to an artifact in this repo; nothing claims employment or a real audit |
