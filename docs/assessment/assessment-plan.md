# Security Assessment Plan (SAP)

| Field | Value |
|---|---|
| Document ID | ASMT-SAP-001 · v1.0 · 2026-06-12 |
| Basis | NIST SP 800-37 Rev. 2 (Assess step, Tasks A-1 to A-6); SP 800-53A Rev. 5 (methods, objects, determination statements) |

## 1. Assessment methods (SP 800-53A)

| Method | What the assessor does | Typical objects | Strength of evidence |
|---|---|---|---|
| **Examine** | Review, inspect, observe, or analyze specifications, mechanisms, and activities | Policies, procedures, SSP, configurations, exports, tickets, logs | Shows *design*, and *implementation* when the object is a live configuration |
| **Interview** | Discuss with individuals to clarify, corroborate, or find evidence | Control owners, administrators, HR, vendor staff | Weakest on its own. Always corroborated by Examine or Test |
| **Test** | Exercise mechanisms or activities under specified conditions and compare actual to expected behavior | Reconciliations, re-performance, sample testing, configuration queries, restore tests | Strongest: shows *operating effectiveness* |

**Rule:** a **Satisfied** determination needs at least one *Examine* **and** either a *Test* or an *Examine* of system-generated evidence covering the period. **Interview alone never satisfies a control.**

## 2. Determination logic

Each control's determination statements (from SP 800-53A) are evaluated individually:

- **Satisfied (S):** evidence shows every determination statement is met.
- **Other Than Satisfied (O):** one or more statements are not met, or evidence is insufficient to conclude. *Insufficient evidence is a finding in itself*, recorded against the control, not a pass by default.
- **Not Assessed:** used only for controls determined *Not Applicable*.

## 3. Sampling approach

| Control frequency | Population | Sample size | Notes |
|---|---|---|---|
| Annual | 1 | 1 | e.g., policy review, CP test |
| Quarterly | 2 in period | 2 (all) | e.g., access certifications |
| Monthly | 6 | 2–6 (all in this assessment) | e.g., vendor-master change reviews |
| Weekly | 26 | 5–15; **all 26 tested** because the population is small and the review is a key control | Privileged-activity log reviews |
| Event-driven (terminations, transfers, changes, incidents) | Varies | **Full population if ≤25**; otherwise 25 selected randomly with seed recorded | Terminations: 19 of 19 · Transfers: 6 of 6 · Changes: 25 of 212 · Incidents: 6 of 6 |
| Configuration (point-in-time) | Full export | 100% via query | MFA policy, security groups, retention settings |

*Random selection for CM-3 used Python `random.Random(20260618).sample()` on the change-ticket export. The seed is recorded so another assessor can reproduce the sample.*

## 4. Reliability of information produced by the entity (IPE)

Before relying on any system-generated report, the assessor checks:
1. **Source:** how was it generated (report name, query, filters)? Was the assessor present, or was the query shared?
2. **Completeness:** does the population reconcile to an independent total? (Example: 19 H1 terminations in PeopleHub reconciled to 19 final-pay records in Ledgerline.)
3. **Accuracy:** do 3 records trace back to the source system?
4. **Period:** does the report cover the whole evidence period?

## 5. Reproducible tests

Several **Test** procedures are implemented as scripts that run against the (synthetic) evidence, so any reviewer can re-perform them:

| Test | Script | Evidence consumed | Output |
|---|---|---|---|
| Termination de-provisioning timeliness (AC-2(3), PS-4) | `tools/assessment_tests.py termination` | EVID-003, EVID-004, EVID-007 | [test-results/termination-deprovisioning.md](test-results/termination-deprovisioning.md) |
| Access certification exception engine (AC-2, AC-5, AC-6, IA-2) | `tools/review_engine.py` | EVID-005, EVID-006, role matrix | [access-review.csv](../../access-review/access-review.csv) |
| Privileged-activity review completeness (AU-6) | `tools/assessment_tests.py logreview` | EVID-022 | [test-results/au6-log-review.md](test-results/au6-log-review.md) |
| Vulnerability remediation SLA (RA-5, SI-2) | `tools/assessment_tests.py vulnsla` | EVID-048 | [test-results/si2-vuln-sla.md](test-results/si2-vuln-sla.md) |
| Change approval sample (CM-3) | `tools/assessment_tests.py changes` | EVID-030 | [test-results/cm3-change-sample.md](test-results/cm3-change-sample.md) |
| Post-remediation reconciliation (POAM-001 validation) | `tools/assessment_tests.py termination --asof 2026-09-10` | EVID-061, EVID-062 | [test-results/termination-deprovisioning-validation.md](test-results/termination-deprovisioning-validation.md) |

## 6. Assessment schedule by family

| Week of | Families | Key interviews |
|---|---|---|
| 2026-06-15 | AC, IA, PS (walkthroughs) | Nadia Rahman (IAM), Denise Yamamoto (HR), Kevin Brandt (IT) |
| 2026-06-22 | AU, SI, RA, CM | Owen Castillo (Security Eng), Tomasz Wierzbicki (SRE) |
| 2026-06-29 | CP, IR, SC, access-review snapshot | Tomasz Wierzbicki, Owen Castillo |
| 2026-07-06 | SA, SR, CA-3, vendor assessment | Beth Kowalski (Vendor Mgmt), Dr. Miriam Castell, Quarrystone CISO |
| 2026-07-13 | AT, PL, PM, CA, MP, PE | Priya Raman (GRC), Denise Yamamoto |
| 2026-07-20 | Follow-ups, insufficient-evidence rework, exit meetings | All control owners |

## 7. Rules of engagement

- Assessor accounts: AWS `SecurityAudit` (read-only), Okta Read-Only Admin, GitHub org auditor, SIEM read-only. All created for the engagement and **removed on 2026-07-31** (verified in the access review follow-up).
- No vulnerability scanning or exploitation by the assessor (the penetration test is a separate engagement).
- Findings that suggest an **active incident** go to the CISO the same day, outside the report cycle. This happened once: the post-termination login found during the access review (INC-2026-0117).
