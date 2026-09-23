# Control Assessment Worksheet: SI-2 Flaw Remediation

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

| Field | Value |
|---|---|
| Control | **SI-2 Flaw Remediation** (System and Information Integrity) · baseline: Moderate |
| Requirement (paraphrased) | Identify, report, and correct system flaws; test updates before installation; install security-relevant updates within a defined time; incorporate flaw remediation into configuration management. |
| Business drivers | REQ-009 (SHCA CSA §7.1) |
| System / process | SYS-01, SYS-05 |
| Control owner | Grace Lindqvist (VP Engineering) |
| Origination | System-specific |
| Owner-stated status → validated | Implemented → **Partially Implemented** |
| Assessment objective (SP 800-53A, paraphrased) | Flaws are identified, reported, and corrected; security-relevant updates installed within the defined time; remediation is part of configuration management. |
| Interviewees | Grace Lindqvist (VP Engineering), Owen Castillo (Security Engineer) |

## Implementation (as described and observed)
VM-003 sets SLAs of Critical 15 days, High 30, and Moderate 90. Findings are auto-ticketed to the owning team. Container fixes ship through base-image rebuilds. Risk exceptions require a CISO-approved form (VM-003 §7).

## Test steps
| TP | Method | Procedure | Expected | Actual | Result | Evidence |
|---|---|---|---|---|---|---|
| TP-SI-2-01 | Examine | Review VM-003 SLAs and exception process | SLAs match CSA §7.1; exception process defined | Matches; exception process in §7 | ✅ Pass | VM-003 |
| TP-SI-2-02 | Test | Compute SLA adherence for all 61 Critical/High findings in H1 | 100% within SLA or with approved exception | 47 of 61 (77%) within SLA; 14 breached; 0 exceptions filed | ❌ Fail | EVID-048; test-results/si2-vuln-sla.md |
| TP-SI-2-03 | Interview | Discuss the 2 open Critical findings with Engineering | Remediation plan or approved exception | Engineering asserts no reachable path; no analysis documented; no exception filed | ❌ Fail | Interview notes 2026-06-29 |

## Determination
| | |
|---|---|
| **Expected vs actual (summary)** | Full population test (test-results/si2-vuln-sla.md). Expected: 100% remediated within SLA, or approved exception. Actual: 14 of 61 (23%) breached SLA; 6 remain open past SLA (2 Critical), and 0 exceptions were filed. Engineering disputes the 2 Critical findings as unreachable. Assessor position: the SLA applies until an exception with reachability analysis is approved. |
| **Assessment result** | **Other Than Satisfied** |
| **Highest evidence level obtained** | Operating Effectiveness |
| **Deficiency** | Remediation timeliness below SLA; exception process unused. |
| **Risk** | RISK-006 (Exploitation of unremediated vulnerabilities) |
| **Finding** | [FIND-010](../../../findings/findings-register.md#find-010) Vulnerability remediation exceeds contractual SLAs (High) |
| **POA&M** | POAM-010 |
| **Control owner response** | Partially agree: disputes severity of 2 Critical findings; agrees to use the exception process |

## Quality review (4 perspectives)
- **Auditor:** every step cites evidence IDs that resolve in the [evidence tracker](../../../audit/evidence-tracker.csv); the conclusion follows from the failed or passed steps.
- **Control owner:** the deficiency names a specific, actionable gap (not "improve access management").
- **Risk manager:** the linked risk states the business consequence and carries a scored rationale.
- **Hiring manager:** shows test design (population, sample, criteria), not just a checklist tick.
