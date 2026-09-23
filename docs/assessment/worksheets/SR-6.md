# Control Assessment Worksheet: SR-6 Supplier Assessments and Reviews

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

| Field | Value |
|---|---|
| Control | **SR-6 Supplier Assessments and Reviews** (Supply Chain Risk Management) · baseline: Moderate |
| Requirement (paraphrased) | Assess and review the supply chain-related risks associated with suppliers or contractors and the systems, components, or services they provide, at a defined frequency. |
| Business drivers | REQ-008 (SHCA CSA §6.3), REQ-018 (HIPAA 45 CFR 164.308(b)(1); 164.314(a)) |
| System / process | Vendors (14 Tier 1–2) |
| Control owner | Beth Kowalski (Vendor Management Lead) |
| Origination | Common (vendor-management program) |
| Owner-stated status → validated | Implemented → **Partially Implemented** |
| Assessment objective (SP 800-53A, paraphrased) | Supply chain-related risks of suppliers and the services they provide are assessed and reviewed at the defined frequency. |
| Interviewees | Beth Kowalski (Vendor Management Lead), Dr. Miriam Castell (VP Clinical Analytics), Quarrystone CISO |

## Implementation (as described and observed)
Tier-based reassessment (Tier 1 annually) using a questionnaire plus attestation review (SOC 2 and pentest summaries). There is no fourth-party inventory. Assessments are tracked in a spreadsheet.

## Test steps
| TP | Method | Procedure | Expected | Actual | Result | Evidence |
|---|---|---|---|---|---|---|
| TP-SR-6-01 | Test | Compare last-assessed dates for all 14 Tier 1–2 vendors to their tier frequency | 14 of 14 current | 9 of 14 current; 5 overdue or never assessed | ❌ Fail | EVID-049 |
| TP-SR-6-02 | Examine | Review Quarrystone SOC 2: opinion, exceptions, carve-outs, CUECs | Info | Unqualified; 2 exceptions; 2 carve-outs; CUEC for portal user review not performed by Wrenfield | ℹ️ Info | EVID-050 |
| TP-SR-6-03 | Interview | Interview Quarrystone CISO on subcontractors and data location | Answers consistent with questionnaire | Revealed undisclosed offshore subcontractor with production access (contradicts questionnaire) | ❌ Fail | Interview notes 2026-07-14 |
| TP-SR-6-04 | Examine | Request the pentest report and retest | Current test with retest | Summary letter only; still outstanding | ❌ Fail | EVID-051 |

## Determination
| | |
|---|---|
| **Expected vs actual (summary)** | Expected: all Tier 1–2 vendors assessed within frequency. Actual: 5 of 14 overdue or never assessed (including Tier 1 Pulsewire and Ironpeak). The Quarrystone deep assessment found 12 vendor-risk issues (1 Critical, contained 2026-07-24). The vendor's pentest report and retest evidence are still outstanding (EVID-051). |
| **Assessment result** | **Other Than Satisfied** |
| **Highest evidence level obtained** | Operating Effectiveness |
| **Deficiency** | Supplier reviews overdue; self-attestation missed a Critical issue. |
| **Risk** | RISK-010 (PHI exposure through the analytics vendor (Quarrystone)), RISK-011 (Software or vendor supply-chain compromise) |
| **Finding** | [FIND-015](../../../findings/findings-register.md#find-015) Third-party risk monitoring incomplete; no C-SCRM plan (Moderate), [FIND-016](../../../findings/findings-register.md#find-016) Quarrystone Analytics: offshore PHI access, inadequate breach-notification terms, and excessive data sharing (High) |
| **POA&M** | POAM-015, POAM-016 |
| **Control owner response** | Agree |

## Quality review (4 perspectives)
- **Auditor:** every step cites evidence IDs that resolve in the [evidence tracker](../../../audit/evidence-tracker.csv); the conclusion follows from the failed or passed steps.
- **Control owner:** the deficiency names a specific, actionable gap (not "improve access management").
- **Risk manager:** the linked risk states the business consequence and carries a scored rationale.
- **Hiring manager:** shows test design (population, sample, criteria), not just a checklist tick.
