# Control Matrix Summary: NIST SP 800-53 Rev. 5 (Release 5.2.0)

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

Full matrix (33 fields): [nist-800-53-control-matrix.xlsx](nist-800-53-control-matrix.xlsx) · [CSV](nist-800-53-control-matrix.csv) · Procedures: [assessment-procedures.csv](assessment-procedures.csv)

## Results by family

| Family | Controls | Satisfied | Other Than Satisfied | N/A |
|---|---|---|---|---|
| AC Access Control | 11 | 2 | 8 | 1 |
| AT Awareness and Training | 2 | 1 | 1 | 0 |
| AU Audit and Accountability | 4 | 2 | 2 | 0 |
| CA Assessment, Authorization, and Monitoring | 4 | 4 | 0 | 0 |
| CM Configuration Management | 4 | 2 | 2 | 0 |
| CP Contingency Planning | 4 | 2 | 2 | 0 |
| IA Identification and Authentication | 5 | 2 | 3 | 0 |
| IR Incident Response | 4 | 3 | 1 | 0 |
| MP Media Protection | 1 | 1 | 0 | 0 |
| PE Physical and Environmental Protection | 1 | 1 | 0 | 0 |
| PL Planning | 1 | 0 | 1 | 0 |
| PM Program Management | 1 | 1 | 0 | 0 |
| PS Personnel Security | 4 | 1 | 3 | 0 |
| RA Risk Assessment | 4 | 4 | 0 | 0 |
| SA System and Services Acquisition | 2 | 0 | 2 | 0 |
| SC System and Communications Protection | 4 | 3 | 1 | 0 |
| SI System and Information Integrity | 3 | 2 | 1 | 0 |
| SR Supply Chain Risk Management | 2 | 0 | 2 | 0 |

## All controls

| ID | Name | Owner-stated | Validated | Result | Evidence level | Risk | Finding | POA&M | Worksheet |
|---|---|---|---|---|---|---|---|---|---|
| AC-1 | Policy and Procedures | Implemented | Implemented | Satisfied | Design | Low | — | — |  |
| AC-2 | Account Management | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | High | FIND-001, FIND-004, FIND-005, FIND-006 | POAM-001, POAM-004, POAM-005, POAM-006 | [AC-2](../docs/assessment/worksheets/AC-2.md) |
| AC-2(1) | Automated System Account Management | Implemented | Partially Implemented | Other Than Satisfied | Implementation | High | FIND-001 | POAM-001 |  |
| AC-2(3) | Disable Accounts | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | High | FIND-001 | POAM-001 | [AC-2(3)](../docs/assessment/worksheets/AC-2-3.md) |
| AC-5 | Separation of Duties | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | Moderate | FIND-007 | POAM-007 | [AC-5](../docs/assessment/worksheets/AC-5.md) |
| AC-6 | Least Privilege | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | High | FIND-003 | POAM-003 |  |
| AC-6(2) | Non-privileged Access for Nonsecurity Functions | Implemented | Partially Implemented | Other Than Satisfied | Implementation | High | FIND-003 | POAM-003 |  |
| AC-6(5) | Privileged Accounts | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | High | FIND-003 | POAM-003 | [AC-6(5)](../docs/assessment/worksheets/AC-6-5.md) |
| AC-6(7) | Review of User Privileges | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | Moderate | FIND-004 | POAM-004 | [AC-6(7)](../docs/assessment/worksheets/AC-6-7.md) |
| AC-17 | Remote Access | Implemented | Implemented | Satisfied | Implementation |  | — | — |  |
| AC-18 | Wireless Access | Not Applicable | Not Applicable | Not Assessed | Design |  | — | — |  |
| AT-2 | Literacy Training and Awareness | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | Low | FIND-019 | POAM-019 |  |
| AT-3 | Role-based Training | Implemented | Implemented | Satisfied | Operating Effectiveness |  | — | — |  |
| AU-2 | Event Logging | Implemented | Implemented | Satisfied | Implementation |  | — | — |  |
| AU-6 | Audit Record Review, Analysis, and Reporting | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | Moderate | FIND-009 | POAM-009 | [AU-6](../docs/assessment/worksheets/AU-6.md) |
| AU-9 | Protection of Audit Information | Implemented | Implemented | Satisfied | Implementation |  | — | — |  |
| AU-11 | Audit Record Retention | Implemented | Partially Implemented | Other Than Satisfied | Implementation | Moderate | FIND-008 | POAM-008 | [AU-11](../docs/assessment/worksheets/AU-11.md) |
| CA-2 | Control Assessments | Implemented | Implemented | Satisfied | Operating Effectiveness |  | — | — |  |
| CA-3 | Information Exchange | Implemented | Implemented | Satisfied | Design |  | — | — |  |
| CA-5 | Plan of Action and Milestones | Implemented | Implemented | Satisfied | Implementation |  | — | — |  |
| CA-7 | Continuous Monitoring | Implemented | Implemented | Satisfied | Operating Effectiveness | Low | — | — |  |
| CM-2 | Baseline Configuration | Implemented | Implemented | Satisfied | Implementation |  | — | — |  |
| CM-3 | Configuration Change Control | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | Moderate | FIND-018 | POAM-018 | [CM-3](../docs/assessment/worksheets/CM-3.md) |
| CM-6 | Configuration Settings | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | High | FIND-012 | POAM-012 |  |
| CM-8 | System Component Inventory | Implemented | Implemented | Satisfied | Implementation | Low | — | — |  |
| CP-2 | Contingency Plan | Implemented | Implemented | Satisfied | Design |  | — | — |  |
| CP-4 | Contingency Plan Testing | Implemented | Not Implemented | Other Than Satisfied | Design | Moderate | FIND-014 | POAM-014 |  |
| CP-9 | System Backup | Implemented | Implemented | Satisfied | Operating Effectiveness |  | — | — |  |
| CP-9(1) | Testing for Reliability and Integrity | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | Moderate | FIND-013 | POAM-013 | [CP-9(1)](../docs/assessment/worksheets/CP-9-1.md) |
| IA-2 | Identification and Authentication (Organizational Users) | Implemented | Implemented | Satisfied | Implementation |  | — | — |  |
| IA-2(1) | Multi-factor Authentication to Privileged Accounts | Implemented | Partially Implemented | Other Than Satisfied | Implementation | High | FIND-002 | POAM-002 | [IA-2(1)](../docs/assessment/worksheets/IA-2-1.md) |
| IA-2(2) | Multi-factor Authentication to Non-privileged Accounts | Implemented | Partially Implemented | Other Than Satisfied | Implementation | High | FIND-002 | POAM-002 |  |
| IA-2(8) | Access to Accounts — Replay Resistant | Implemented | Implemented | Satisfied | Implementation |  | — | — |  |
| IA-5 | Authenticator Management | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | Moderate | FIND-005 | POAM-005 |  |
| IR-3 | Incident Response Testing | Implemented | Partially Implemented | Other Than Satisfied | Design | Moderate | FIND-014 | POAM-014 | [IR-3](../docs/assessment/worksheets/IR-3.md) |
| IR-4 | Incident Handling | Implemented | Implemented | Satisfied | Operating Effectiveness |  | — | — |  |
| IR-6 | Incident Reporting | Implemented | Implemented | Satisfied | Operating Effectiveness |  | — | — |  |
| IR-8 | Incident Response Plan | Implemented | Implemented | Satisfied | Design | Low | — | — |  |
| MP-6 | Media Sanitization | Implemented | Implemented | Satisfied | Operating Effectiveness |  | — | — |  |
| PE-3 | Physical Access Control | Implemented | Implemented | Satisfied | Design |  | — | — |  |
| PL-2 | System Security and Privacy Plans | Implemented | Partially Implemented | Other Than Satisfied | Design | Low | FIND-017 | POAM-017 |  |
| PM-9 | Risk Management Strategy | Implemented | Implemented | Satisfied | Operating Effectiveness |  | — | — |  |
| PS-3 | Personnel Screening | Implemented | Implemented | Satisfied | Operating Effectiveness |  | — | — |  |
| PS-4 | Personnel Termination | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | High | FIND-001 | POAM-001 |  |
| PS-5 | Personnel Transfer | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | Moderate | FIND-004 | POAM-004 |  |
| PS-7 | External Personnel Security | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | Moderate | FIND-006, FIND-001 | POAM-006, POAM-001 |  |
| RA-2 | Security Categorization | Implemented | Implemented | Satisfied | Design |  | — | — |  |
| RA-3 | Risk Assessment | Implemented | Implemented | Satisfied | Design |  | — | — |  |
| RA-5 | Vulnerability Monitoring and Scanning | Implemented | Implemented | Satisfied | Operating Effectiveness | Low | — | — |  |
| RA-7 | Risk Response | Implemented | Implemented | Satisfied | Implementation |  | — | — |  |
| SA-9 | External System Services | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | High | FIND-015, FIND-016 | POAM-015, POAM-016 |  |
| SA-22 | Unsupported System Components | Partially Implemented | Partially Implemented | Other Than Satisfied | Implementation | High | FIND-011 | POAM-011 | [SA-22](../docs/assessment/worksheets/SA-22.md) |
| SC-7 | Boundary Protection | Implemented | Partially Implemented | Other Than Satisfied | Implementation | High | FIND-012 | POAM-012 |  |
| SC-8 | Transmission Confidentiality and Integrity | Implemented | Implemented | Satisfied | Implementation |  | — | — |  |
| SC-12 | Cryptographic Key Establishment and Management | Implemented | Implemented | Satisfied | Implementation |  | — | — |  |
| SC-28 | Protection of Information at Rest | Implemented | Implemented | Satisfied | Implementation |  | — | — | [SC-28](../docs/assessment/worksheets/SC-28.md) |
| SI-2 | Flaw Remediation | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | High | FIND-010 | POAM-010 | [SI-2](../docs/assessment/worksheets/SI-2.md) |
| SI-3 | Malicious Code Protection | Implemented | Implemented | Satisfied | Operating Effectiveness |  | — | — |  |
| SI-4 | System Monitoring | Implemented | Implemented | Satisfied | Operating Effectiveness |  | — | — |  |
| SR-2 | Supply Chain Risk Management Plan | Planned | Planned | Other Than Satisfied | Design | Moderate | FIND-015 | POAM-015 |  |
| SR-6 | Supplier Assessments and Reviews | Implemented | Partially Implemented | Other Than Satisfied | Operating Effectiveness | High | FIND-015, FIND-016 | POAM-015, POAM-016 | [SR-6](../docs/assessment/worksheets/SR-6.md) |
