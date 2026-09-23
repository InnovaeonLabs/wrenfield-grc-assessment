# Control Assessment Worksheet: IR-3 Incident Response Testing

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

| Field | Value |
|---|---|
| Control | **IR-3 Incident Response Testing** (Incident Response) · baseline: Moderate |
| Requirement (paraphrased) | Test the effectiveness of the incident response capability at a defined frequency using defined tests. |
| Business drivers | REQ-006 (SHCA CSA §5.2), REQ-016 (HIPAA 45 CFR 164.308(a)(6)(ii)) |
| System / process | WCP-PROD |
| Control owner | Owen Castillo (Security Engineer) |
| Origination | Common (organization-wide) |
| Owner-stated status → validated | Implemented → **Partially Implemented** |
| Assessment objective (SP 800-53A, paraphrased) | Incident response capability is tested at the defined frequency using defined tests. |
| Interviewees | Owen Castillo (Security Engineer), Rachel Stein (HIPAA Privacy Officer) |

## Implementation (as described and observed)
IRP-005 requires an annual tabletop exercise that includes the MDR, Legal/Privacy, and Customer Ops. The last tabletop was 2024-09-18 (phishing-to-BEC scenario). The 2025 exercise was deferred twice.

## Test steps
| TP | Method | Procedure | Expected | Actual | Result | Evidence |
|---|---|---|---|---|---|---|
| TP-IR-3-01 | Examine | Request exercise records for 24 months | Exercise within 12 months with after-action items | Last exercise 2024-09-18 (21 months) | ❌ Fail | EVID-037 |
| TP-IR-3-02 | Interview | Ask the Privacy Officer to walk the SHCA 24h notification path | Rehearsed, documented path | Path known conceptually; not documented in IRP-005; never rehearsed | ❌ Fail | Interview notes 2026-07-15 |
| TP-IR-3-03 | Test | Cross-check real incident handling (IR-4) as a mitigating factor | Info only | 7 of 7 incidents handled per plan; mitigating but not a substitute for testing major-incident paths | ℹ️ Info | EVID-038, EVID-078 |

## Determination
| | |
|---|---|
| **Expected vs actual (summary)** | Expected: an IR exercise within the last 12 months with tracked corrective actions. Actual: the most recent was 21 months before fieldwork (EVID-037, Insufficient for the period). The 24-hour SHCA reporting path has never been exercised. Mitigating factor: real incidents in H1 were handled well (IR-4), which lowers but does not remove the risk. |
| **Assessment result** | **Other Than Satisfied** |
| **Highest evidence level obtained** | Design |
| **Deficiency** | IR capability not tested in the period. |
| **Risk** | RISK-009 (Delayed or ineffective response to a major incident) |
| **Finding** | [FIND-014](../../../findings/findings-register.md#find-014) Incident response and contingency plans not tested within 12 months (Moderate) |
| **POA&M** | POAM-014 |
| **Control owner response** | Agree; tabletop scheduled 2026-10-14 |

## Quality review (4 perspectives)
- **Auditor:** every step cites evidence IDs that resolve in the [evidence tracker](../../../audit/evidence-tracker.csv); the conclusion follows from the failed or passed steps.
- **Control owner:** the deficiency names a specific, actionable gap (not "improve access management").
- **Risk manager:** the linked risk states the business consequence and carries a scored rationale.
- **Hiring manager:** shows test design (population, sample, criteria), not just a checklist tick.
