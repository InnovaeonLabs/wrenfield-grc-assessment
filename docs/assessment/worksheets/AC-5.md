# Control Assessment Worksheet: AC-5 Separation of Duties

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

| Field | Value |
|---|---|
| Control | **AC-5 Separation of Duties** (Access Control) · baseline: Moderate |
| Requirement (paraphrased) | Identify and document duties that require separation, and define system access authorizations that support that separation. |
| Business drivers | REQ-023 (SOC 2 system description commitments (CC6.1–CC6.3, CC8.1)), REQ-024 (Wrenfield Information Security Policy ISP-001 v4.0 and Risk Appetite Statement (Board-approved 2025-10-21)) |
| System / process | SYS-07 |
| Control owner | Laura Brenneman (Controller) |
| Origination | System-specific (Ledgerline) |
| Owner-stated status → validated | Implemented → **Partially Implemented** |
| Assessment objective (SP 800-53A, paraphrased) | Duties requiring separation are identified and documented; access authorizations support separation of duties. |
| Interviewees | Laura Brenneman (Controller), Raymond Okafor (CFO) |

## Implementation (as described and observed)
Ledgerline has an SoD ruleset (SOD-01 vendor master vs payment approval; SOD-02 AP entry vs approval). After the AP Specialist left in 2026-05, the Senior Accountant held both Vendor Master Maintain and Payment Approver (<= $25k). The compensating control is a monthly vendor-master change report that the Controller reviews and signs.

## Test steps
| TP | Method | Procedure | Expected | Actual | Result | Evidence |
|---|---|---|---|---|---|---|
| TP-AC-5-01 | Examine | Review Ledgerline SoD ruleset | Conflicting duties defined for vendor, AP, and payment functions | SOD-01 and SOD-02 defined and appropriate | ✅ Pass | EVID-014 |
| TP-AC-5-02 | Test | Apply SoD rules to all Ledgerline role assignments | No user holds conflicting roles | 1 conflict: jmercer holds Vendor Master Maintain and Payment Approver (<= $25k) | ❌ Fail | EVID-006; review engine F-SOD |
| TP-AC-5-03 | Test | Inspect all 6 monthly compensating reviews (Jan–Jun): signed, dated, independent reviewer, exceptions followed up | 6 of 6 operating | 6 of 6 signed by Controller within 10 days; 2 bank changes independently verified by callback | ✅ Pass | EVID-015 |
| TP-AC-5-04 | Examine | Check for a documented risk decision on the conflict | Approved acceptance at the correct authority | None at fieldwork; RACC-001 signed 2026-08-12 | ❌ Fail | EVID-060 |

## Determination
| | |
|---|---|
| **Expected vs actual (summary)** | Tested role assignments against the SoD rules (review engine) and inspected 6 of 6 monthly compensating reviews (Jan–Jun). Expected: no user holds conflicting roles, or a documented and operating compensating control exists. Actual: 1 conflict (jmercer, SOD-01). The compensating review operated 6 of 6 months (signed, dated, 2 bank-detail changes independently verified by callback). The conflict was not formally risk-accepted until RACC-001 (2026-08-12). |
| **Assessment result** | **Other Than Satisfied** |
| **Highest evidence level obtained** | Operating Effectiveness |
| **Deficiency** | Conflict existed without a documented risk decision; compensating control operates. |
| **Risk** | RISK-013 (Fraudulent vendor payment through an SoD conflict) |
| **Finding** | [FIND-007](../../../findings/findings-register.md#find-007) Segregation-of-duties conflict in vendor payment process (Moderate) |
| **POA&M** | POAM-007 |
| **Control owner response** | Agree; accepted via RACC-001 |

## Quality review (4 perspectives)
- **Auditor:** every step cites evidence IDs that resolve in the [evidence tracker](../../../audit/evidence-tracker.csv); the conclusion follows from the failed or passed steps.
- **Control owner:** the deficiency names a specific, actionable gap (not "improve access management").
- **Risk manager:** the linked risk states the business consequence and carries a scored rationale.
- **Hiring manager:** shows test design (population, sample, criteria), not just a checklist tick.
