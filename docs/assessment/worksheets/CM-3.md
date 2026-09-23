# Control Assessment Worksheet: CM-3 Configuration Change Control

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

| Field | Value |
|---|---|
| Control | **CM-3 Configuration Change Control** (Configuration Management) · baseline: Moderate |
| Requirement (paraphrased) | Determine and document types of changes that are configuration-controlled; review, approve or disapprove, document, and implement changes; retain records; monitor and review activities. |
| Business drivers | REQ-023 (SOC 2 system description commitments (CC6.1–CC6.3, CC8.1)) |
| System / process | SYS-01, SYS-03, SYS-05 |
| Control owner | Tomasz Wierzbicki (Director, Platform Engineering) |
| Origination | System-specific |
| Owner-stated status → validated | Implemented → **Partially Implemented** |
| Assessment objective (SP 800-53A, paraphrased) | Configuration-controlled changes are reviewed, approved or disapproved, documented, implemented, and retained; activities are monitored. |
| Interviewees | Tomasz Wierzbicki (Director, Platform Engineering), Sofia Ricci (Engineering Manager) |

## Implementation (as described and observed)
Code and IaC changes go through GitHub PRs with required reviews and CI, then deploy through a protected environment with approvers. The change management procedure CMP-006 requires emergency changes to be retro-approved within 2 business days. Console changes have no preventive gate.

## Test steps
| TP | Method | Procedure | Expected | Actual | Result | Evidence |
|---|---|---|---|---|---|---|
| TP-CM-3-01 | Examine | Review CMP-006 change types and emergency rules | Defined | Standard, Normal, Emergency defined; emergency retro-approval within 2 business days | ✅ Pass | CMP-006 |
| TP-CM-3-02 | Test | Random sample 25 of 212 production changes (seed 20260618); verify approval before deploy, peer review, test evidence | 25 of 25 compliant | 22 of 25; exceptions CHG-2026-0412, -0288, -0356 | ❌ Fail | EVID-030; test-results/cm3-change-sample.md |
| TP-CM-3-03 | Interview | Ask how console changes are captured | Console changes detected and routed to change process | No detection; relies on engineers raising tickets | ❌ Fail | Interview notes 2026-06-24 |

## Determination
| | |
|---|---|
| **Expected vs actual (summary)** | Random sample of 25 of 212 changes (test-results/cm3-change-sample.md). Expected: 25 of 25 approved before deployment, or retro-approved within 2 business days for emergencies. Actual: 3 exceptions. CHG-2026-0412 (emergency RDP change, never approved or reverted), CHG-2026-0288 (retro approval after 9 days), and CHG-2026-0356 (deployed 5h38m before approval). |
| **Assessment result** | **Other Than Satisfied** |
| **Highest evidence level obtained** | Operating Effectiveness |
| **Deficiency** | Emergency and console change paths bypass approval. |
| **Risk** | RISK-014 (Unauthorized or untested changes cause an outage or security regression) |
| **Finding** | [FIND-018](../../../findings/findings-register.md#find-018) Emergency and console changes bypass approval (Moderate) |
| **POA&M** | POAM-018 |
| **Control owner response** | Agree |

## Quality review (4 perspectives)
- **Auditor:** every step cites evidence IDs that resolve in the [evidence tracker](../../../audit/evidence-tracker.csv); the conclusion follows from the failed or passed steps.
- **Control owner:** the deficiency names a specific, actionable gap (not "improve access management").
- **Risk manager:** the linked risk states the business consequence and carries a scored rationale.
- **Hiring manager:** shows test design (population, sample, criteria), not just a checklist tick.
