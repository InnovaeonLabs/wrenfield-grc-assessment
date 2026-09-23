# Control Assessment Worksheet: AC-2 Account Management

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

| Field | Value |
|---|---|
| Control | **AC-2 Account Management** (Access Control) · baseline: Moderate |
| Requirement (paraphrased) | Define allowed account types; assign account managers; require approvals for account creation; create, modify, disable, and remove accounts per defined conditions; monitor account use; notify account managers when accounts are no longer needed; review accounts for compliance at a defined frequency. |
| Business drivers | REQ-001 (SHCA Contract Security Addendum §2.1), REQ-004 (SHCA CSA §3.3), REQ-013 (HIPAA 45 CFR 164.308(a)(3)(ii)(C)), REQ-014 (HIPAA 45 CFR 164.308(a)(4)(ii)(B)-(C)), REQ-023 (SOC 2 system description commitments (CC6.1–CC6.3, CC8.1)) |
| System / process | SYS-01, SYS-02, SYS-03, SYS-04, SYS-05, SYS-06, SYS-07, SYS-08, SYS-09 |
| Control owner | Nadia Rahman (IAM Engineer) |
| Origination | Hybrid (Okta common control + system-specific accounts) |
| Owner-stated status → validated | Implemented → **Partially Implemented** |
| Assessment objective (SP 800-53A, paraphrased) | Account types are defined; account managers assigned; creation, modification, disabling, and removal follow approved conditions; accounts are monitored and reviewed; managers are notified when access is no longer needed. |
| Interviewees | Nadia Rahman (IAM Engineer), Denise Yamamoto (Director of People), Tomasz Wierzbicki (system owner) |

## Implementation (as described and observed)
Okta is the identity source for SSO apps. Access requests go through Jira service desk tickets approved by the manager and the system owner. Termination tickets are raised manually by IT from HR emails. Local accounts exist outside Okta on AWS (legacy IAM users), wf-sftp-01, and the Quarrystone portal, and are managed ad hoc. There is a service-account register, but it lacked owner and rotation fields until 2026-07.

## Test steps
| TP | Method | Procedure | Expected | Actual | Result | Evidence |
|---|---|---|---|---|---|---|
| TP-AC-2-01 | Examine | Review ACP-002 v3.1 and SOP-IAM-02 v2.0 for account types, approvals, conditions, and review frequency | All AC-2 elements defined, including non-SSO and service accounts | Elements defined for Okta SSO accounts; local accounts and service accounts not addressed in the procedure | ❌ Fail | EVID-001, EVID-002 |
| TP-AC-2-02 | Interview | Walk through the joiner/mover/leaver process with IAM and HR; ask how HR events reach IT and how local accounts are found | Automated or reliably triggered handoff covering all account stores | HR emails IT; IT raises a ticket manually; no one owns local-account discovery; transfers do not trigger review | ❌ Fail | Interview notes 2026-06-16 |
| TP-AC-2-03 | Test | Reconcile 106 entitlements on 9 systems against HR status, role baseline, SoD rules, and service register (tools/review_engine.py) | 0 unauthorized, orphaned, or unowned accounts | 20 confirmed exceptions across 28 rows (4 terminated, 1 duplicate, 1 transfer, 1 inactive, 2 contractor, 3 service or shared, plus privilege exceptions under AC-6) | ❌ Fail | EVID-005, EVID-006, EVID-013; access-review/access-review.csv |
| TP-AC-2-04 | Test | Verify every non-human account has an owner and a credential within rotation policy | 13 of 13 owned and current | 11 of 13 owned; 3 stale credentials; 1 shared vendor login | ❌ Fail | EVID-013 |

## Determination
| | |
|---|---|
| **Expected vs actual (summary)** | Full reconciliation of 106 entitlements on 9 systems against HR, the role baseline, the SoD rules, and the service register (tools/review_engine.py). Expected: every account is authorized, owned, and current. Actual: 20 exceptions across 28 entitlement rows. They include terminated users (4), a duplicate identity, inactive access, contractor term drift, service accounts without owners or rotation, and a shared vendor login. |
| **Assessment result** | **Other Than Satisfied** |
| **Highest evidence level obtained** | Operating Effectiveness |
| **Deficiency** | Account lifecycle not enforced for local, contractor, transferred, and service accounts. |
| **Risk** | RISK-002 (Unauthorized access by former employees or contractors), RISK-004 (Access creep from ineffective recertification), RISK-017 (Service-account credential theft) |
| **Finding** | [FIND-001](../../../findings/findings-register.md#find-001) Terminated workforce retained active access (High), [FIND-004](../../../findings/findings-register.md#find-004) Access recertification incomplete and ineffective (access creep) (Moderate), [FIND-005](../../../findings/findings-register.md#find-005) Service and shared accounts lack ownership, credential rotation, and individual accountability (Moderate), [FIND-006](../../../findings/findings-register.md#find-006) Contractor access not bound to engagement term and scope (Moderate) |
| **POA&M** | POAM-001, POAM-004, POAM-005, POAM-006 |
| **Control owner response** | Agree (Nadia Rahman, 2026-08-07) |

## Quality review (4 perspectives)
- **Auditor:** every step cites evidence IDs that resolve in the [evidence tracker](../../../audit/evidence-tracker.csv); the conclusion follows from the failed or passed steps.
- **Control owner:** the deficiency names a specific, actionable gap (not "improve access management").
- **Risk manager:** the linked risk states the business consequence and carries a scored rationale.
- **Hiring manager:** shows test design (population, sample, criteria), not just a checklist tick.
