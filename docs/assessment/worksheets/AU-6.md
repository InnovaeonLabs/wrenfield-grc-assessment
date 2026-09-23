# Control Assessment Worksheet: AU-6 Audit Record Review, Analysis, and Reporting

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

| Field | Value |
|---|---|
| Control | **AU-6 Audit Record Review, Analysis, and Reporting** (Audit and Accountability) · baseline: Moderate |
| Requirement (paraphrased) | Review and analyze audit records at a defined frequency for signs of inappropriate or unusual activity; report findings to defined personnel; adjust review when risk changes. |
| Business drivers | REQ-019 (HIPAA 45 CFR 164.312(b)), REQ-005 (SHCA CSA §4.1) |
| System / process | SYS-01, SYS-02, SYS-08 |
| Control owner | Owen Castillo (Security Engineer) |
| Origination | System-specific |
| Owner-stated status → validated | Implemented → **Partially Implemented** |
| Assessment objective (SP 800-53A, paraphrased) | Audit records are reviewed and analyzed at the defined frequency for inappropriate or unusual activity; findings reported to defined personnel. |
| Interviewees | Owen Castillo (Security Engineer) |

## Implementation (as described and observed)
MDR monitors alerts 24x7 (SI-4). Separately, LMS-004 §6 requires a weekly human review of privileged activity (AWS admin actions, Okta admin changes, GitHub owner actions), documented in a SEC ticket. One primary reviewer, no designated backup.

## Test steps
| TP | Method | Procedure | Expected | Actual | Result | Evidence |
|---|---|---|---|---|---|---|
| TP-AU-6-01 | Examine | Review LMS-004 §6 review requirements and the SIEM report definition | Weekly review of all privileged principals | Weekly defined; report scope excluded local AWS IAM users | ❌ Fail | EVID-021 |
| TP-AU-6-02 | Test | Test all 26 weeks for existence, timeliness (5 days), and disposition of flagged items | 26 of 26 effective | 19 performed; 17 effective (65%); 7 missed; 2 incomplete | ❌ Fail | EVID-022; test-results/au6-log-review.md |
| TP-AU-6-03 | Interview | Ask about backup coverage and escalation | Backup reviewer and escalation defined | No backup; missed weeks not escalated | ❌ Fail | Interview notes 2026-06-23 |

## Determination
| | |
|---|---|
| **Expected vs actual (summary)** | Tested all 26 weeks (test-results/au6-log-review.md). Expected: 26 of 26 performed within 5 days with every flag dispositioned. Actual: 19 performed and 17 fully effective (65%). 7 weeks were missed (migration, PTO) and 2 reviews were marked 'reviewed' with undispositioned flags. The review scope also excluded local IAM users. |
| **Assessment result** | **Other Than Satisfied** |
| **Highest evidence level obtained** | Operating Effectiveness |
| **Deficiency** | Single point of failure in a key detective control. |
| **Risk** | RISK-005 (Inability to detect or investigate PHI access) |
| **Finding** | [FIND-009](../../../findings/findings-register.md#find-009) Privileged-activity log reviews not consistently performed or documented (Moderate) |
| **POA&M** | POAM-009 |
| **Control owner response** | Agree; MDR backup pending SOW change |

## Quality review (4 perspectives)
- **Auditor:** every step cites evidence IDs that resolve in the [evidence tracker](../../../audit/evidence-tracker.csv); the conclusion follows from the failed or passed steps.
- **Control owner:** the deficiency names a specific, actionable gap (not "improve access management").
- **Risk manager:** the linked risk states the business consequence and carries a scored rationale.
- **Hiring manager:** shows test design (population, sample, criteria), not just a checklist tick.
