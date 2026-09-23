# Remediation Lifecycle Traces

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

The spec requires at least 5 findings to travel the **full** lifecycle. **7 did**, each closed only after independent validation:

```
CONTROL FAILURE → AUDIT FINDING → RISK → POA&M → CORRECTIVE ACTION → VALIDATION → CLOSURE
```

Closure means the assessor **re-performed** the test (or observed the control operating) and inspected closure evidence. The owner saying "done" is not enough. Compare POAM-003, where a design-only screenshot (EVID-071) was **returned as Rework Required**.

## FIND-001 → POAM-001: Terminated workforce retained active access

| Stage | What happened | Date | Evidence |
|---|---|---|---|
| **1. Control failure** | AC-2(3) Disable Accounts: Re-performed the 24h test on all 19 H1 terminations (docs/assessment/test-results/termination-deprovisioning.md). Expected: 19 of 19 within 24h, including non-SSO accounts. Actual: 16 of 19 within SLA, 1 late (209h), 2 never deactivated (one with a post-termination sign-in, which became INC-2026-0117), plus 1 active local AWS IAM user and 1 Quarrystone portal account belonging to leavers. | fieldwork | EVID-003, EVID-004, EVID-007, EVID-061 |
| **2. Audit finding** | FIND-001 (High): 2 of 19 workers terminated in H1 2026 were still enabled in Okta at the 2026-06-30 snapshot, and 1 more was disabled 9 days late. A terminated contractor signed in 4 days after the contract ended (INC-2026-0117). A local AWS IAM user with AdministratorAccess belonging to an employee terminated 2026-03-27 was still active 95 days later. A former employee still had a Quarrystone portal account (local authentication). | 2026-07-06 | AR-EX-01, AR-EX-02, AR-EX-03, AR-EX-04, VR-007, EVID-003, EVID-004, EVID-007, EVID-078 |
| **3. Risk** | RISK-002 Unauthorized access by former employees or contractors: current 16 High (L4×I4) | 2026-09-18 | [risk register](../risk/risk-register.md) |
| **4. POA&M** | POAM-001 opened; owner Nadia Rahman (IAM Engineer); target 2026-09-11 (SLA 2026-11-05) | 2026-08-07 | [poam.md](poam.md#poam-001) |
| **5. Corrective action** | Disable identified accounts; implement daily HR-to-Okta/AWS/portal reconciliation with auto-ticketing; update SOP-IAM-02 with a local-account checklist and 24h SLA (4 milestones, first due 2026-07-10) | 2026-07-09, 2026-08-03, 2026-08-26 | — |
| **6. Validation** | Re-performance: tools/assessment_tests.py termination-validation (7 of 7 within 24h, 0 job exceptions); inspection of IAM credential report (break-glass only) | 2026-09-10 | EVID-061, EVID-062, EVID-064, EVID-078 |
| **7. Closure** | Closed by Lead assessor; residual Moderate (RISK-002 residual L2 x I4 = 8) | 2026-09-10 | — |

## FIND-002 → POAM-002: MFA not enforced for all workforce and privileged accounts

| Stage | What happened | Date | Evidence |
|---|---|---|---|
| **1. Control failure** | IA-2(1) Multi-factor Authentication to Privileged Accounts: Expected: 100% of privileged access requires MFA. Actual: 1 Okta Super Administrator (kbrandt) was in the exemption group, and the IAM user mfeld-admin (AdministratorAccess) had a console password without MFA. | fieldwork | EVID-007, EVID-010, EVID-011, EVID-063 |
| **2. Audit finding** | FIND-002 (High): An Okta policy created in 2023 as a "temporary" workaround exempted the MFA-Exempt-Legacy group (11 accounts, 9 human) from MFA. One member was an Okta Super Administrator. None of the exemptions had approval or an expiry date. In AWS, the IAM user mfeld-admin (AdministratorAccess) had a console password and no MFA. | 2026-06-30 | AR-EX-11, EVID-010, EVID-011, EVID-007, EVID-063, EVID-064 |
| **3. Risk** | RISK-003 Account takeover through MFA gaps: current 15 High (L3×I5) | 2026-09-18 | [risk register](../risk/risk-register.md) |
| **4. POA&M** | POAM-002 opened; owner Nadia Rahman (IAM Engineer); target 2026-09-05 (SLA 2026-11-05) | 2026-08-07 | [poam.md](poam.md#poam-002) |
| **5. Corrective action** | Delete exemption policy and group; enroll all members (hardware key accommodation); convert service users to integrations; require phishing-resistant MFA for admin apps; delete non-break-glass IAM users; add time-bound exception workflow (4 milestones, first due 2026-08-28) | 2026-08-27, 2026-08-27, 2026-08-28 | — |
| **6. Validation** | Inspection of Okta policy export and IAM credential report; re-performance of password-only sign-in with a test account (denied) | 2026-09-05 | EVID-063, EVID-064 |
| **7. Closure** | Closed by Lead assessor; residual Moderate (RISK-003 residual L2 x I4 = 8) | 2026-09-05 | — |

## FIND-005 → POAM-005: Service and shared accounts lack ownership, credential rotation, and individual accountability

| Stage | What happened | Date | Evidence |
|---|---|---|---|
| **1. Control failure** | IA-5 Authenticator Management: Tested credential age for all 13 registered non-human accounts. Expected: none older than 365 days unless federated. Actual: 3 stale (svc-quarrystone-sftp SSH key 811 days; svc-reporting-etl access key 539 days; svc-vulnscan password since 2023), and 1 shared vendor password (ironpeak-soc). Sampled 5 help-desk MFA resets: 5 of 5 had identity verification recorded. | fieldwork | EVID-007, EVID-013, EVID-064, EVID-065 |
| **2. Audit finding** | FIND-005 (Moderate): Of 13 non-human accounts: 2 had no documented owner (svc-quarrystone-sftp, whose SSH key was 811 days old and which pushes the nightly PHI extract; svc-reporting-etl, an IAM user with a 539-day static access key created by a now-terminated employee). The MDR vendor used a single shared login to the EDR console, so containment actions could not be attributed to individual analysts. | 2026-07-09 | AR-EX-18, AR-EX-19, AR-EX-20, EVID-013, EVID-065 |
| **3. Risk** | RISK-017 Service-account credential theft: current 12 High (L3×I4) | 2026-09-18 | [risk register](../risk/risk-register.md) |
| **4. POA&M** | POAM-005 opened; owner Nadia Rahman (IAM Engineer); target 2026-09-12 (SLA 2027-02-03) | 2026-08-07 | [poam.md](poam.md#poam-005) |
| **5. Corrective action** | Assign owners; rotate or federate stale credentials; named federated accounts for MDR analysts; add owner/rotation fields and quarterly attestation to the register (5 milestones, first due 2026-08-21) | 2026-08-18, 2026-08-25, 2026-08-31, 2026-09-03 | — |
| **6. Validation** | Re-performance of the review engine's service-account checks on the updated register; inspection of EDR console user list (no shared logins) | 2026-09-12 | EVID-065, EVID-064 |
| **7. Closure** | Closed by Lead assessor; residual Low (RISK-017 residual L1 x I4 = 4) | 2026-09-12 | — |

## FIND-006 → POAM-006: Contractor access not bound to engagement term and scope

| Stage | What happened | Date | Evidence |
|---|---|---|---|
| **1. Control failure** | PS-7 External Personnel Security: Tested all 5 contractors active in H1 against SOW dates and scope. Expected: access ends at the contract end date and matches SOW scope. Actual: 1 contractor ended without de-provisioning (reported under FIND-001). 1 was active past the recorded end date with the extension undocumented (AR-EX-15). 1 had PHI production access outside the QA SOW scope (AR-EX-16). | fieldwork | EVID-045, EVID-066 |
| **2. Audit finding** | FIND-006 (Moderate): One contractor remained active 22 days past the recorded contract end date while working under an extension that had not been documented. The same contractor had PHI production database access that the QA SOW did not require (QA uses staging with synthetic data). | 2026-07-08 | AR-EX-15, AR-EX-16, EVID-045, EVID-066 |
| **3. Risk** | RISK-002 Unauthorized access by former employees or contractors: current 16 High (L4×I4) | 2026-09-18 | [risk register](../risk/risk-register.md) |
| **4. POA&M** | POAM-006 opened; owner Sofia Ricci (Engineering Manager); target 2026-09-10 (SLA 2027-02-03) | 2026-08-07 | [poam.md](poam.md#poam-006) |
| **5. Corrective action** | Okta account expiry = SOW end date for all contractors; SOW scope required on contractor access requests; monthly contractor roster to sponsors (3 milestones, first due 2026-07-24) | 2026-07-22, 2026-08-24 | — |
| **6. Validation** | Inspection: Okta expiry dates reconciled to SOW register for all active contractors (29 of 29) | 2026-09-08 | EVID-066 |
| **7. Closure** | Closed by Lead assessor; residual Moderate (RISK-002 residual) | 2026-09-10 | — |

## FIND-008 → POAM-008: Audit log retention below the 12-month contractual requirement

| Stage | What happened | Date | Evidence |
|---|---|---|---|
| **1. Control failure** | AU-11 Audit Record Retention: Examined the retention configuration for 5 sources and queried the oldest available record in each. Expected: 12 months or more for all. Actual: CloudTrail 180 days, app audit 90 days, SIEM 90 days (the oldest records matched the settings, so there was no hidden longer retention). | fieldwork | EVID-024, EVID-067 |
| **2. Audit finding** | FIND-008 (Moderate): CloudTrail logs expired after 180 days. Application audit logs recording PHI access (who viewed which patient) were kept 90 days. SIEM hot retention was 90 days. | 2026-06-25 | EVID-024, EVID-067 |
| **3. Risk** | RISK-005 Inability to detect or investigate PHI access: current 12 High (L3×I4) | 2026-09-18 | [risk register](../risk/risk-register.md) |
| **4. POA&M** | POAM-008 opened; owner Owen Castillo (Security Engineer); target 2026-09-15 (SLA 2027-02-03) | 2026-08-07 | [poam.md](poam.md#poam-008) |
| **5. Corrective action** | 400-day lifecycle with tiering (hot 90d searchable); archive application audit logs to log-archive; quarterly oldest-record check (3 milestones, first due 2026-08-21) | 2026-08-19, 2026-08-27 | — |
| **6. Validation** | Inspection of lifecycle/subscription config; test: oldest CloudTrail object (2026-03-20, 182 days) still present after old 180-day rule would have expired it | 2026-09-12 | EVID-067 |
| **7. Closure** | Closed by Lead assessor; residual Moderate (RISK-005 residual after POAM-009) | 2026-09-15 | — |

## FIND-012 → POAM-012: Internet-exposed RDP on legacy host; CSPM alert not triaged

| Stage | What happened | Date | Evidence |
|---|---|---|---|
| **1. Control failure** | SC-7 Boundary Protection: Enumerated all security groups with 0.0.0.0/0 ingress. Expected: only CloudFront/ALB listeners on 443. Actual: wf-sftp-01 allowed TCP 3389 (RDP) from 0.0.0.0/0, added under emergency change CHG-2026-0412 on 2026-05-19 and never reverted (43 days exposed at discovery). No evidence of successful RDP logons from external addresses (reviewed Windows Security log 4624 type 10 for the period). Fixed within 24h of discovery; validated 2026-07-10. | fieldwork | EVID-053, EVID-028, EVID-068 |
| **2. Audit finding** | FIND-012 (High): The security group for wf-sftp-01 allowed RDP (TCP 3389) from 0.0.0.0/0 for 43 days. It was added under emergency change CHG-2026-0412 for a vendor support session, never approved, and never reverted. AWS Security Hub flagged it as High the next day, but no one triaged it. No successful external RDP logons were found (Windows event 4624 logon type 10 reviewed). | 2026-07-02 | EVID-053, EVID-028, EVID-068, EVID-030 |
| **3. Risk** | RISK-012 Cloud misconfiguration exposing PHI or admin services: current 10 High (L2×I5) | 2026-09-18 | [risk register](../risk/risk-register.md) |
| **4. POA&M** | POAM-012 opened; owner Tomasz Wierzbicki (Director, Platform Engineering); target 2026-07-10 (SLA 2026-09-30) | 2026-07-02 | [poam.md](poam.md#poam-012) |
| **5. Corrective action** | Remove rule; route Security Hub High findings to on-call with 7-day SLA; SCP guardrail blocking 0.0.0.0/0 on admin ports (4 milestones, first due 2026-07-03) | 2026-07-03, 2026-07-07, 2026-07-09 | — |
| **6. Validation** | Inspection of SG and Security Hub status; re-performance: attempted to add 0.0.0.0/0:3389 rule in a sandbox OU account (denied by SCP) | 2026-07-10 | EVID-068, EVID-053 |
| **7. Closure** | Closed by Lead assessor; residual Moderate (RISK-012 residual L2 x I4 = 8) | 2026-07-10 | — |

## FIND-013 → POAM-013: Backup restoration never tested

| Stage | What happened | Date | Evidence |
|---|---|---|---|
| **1. Control failure** | CP-9(1) Testing for Reliability and Integrity: Expected: an annual documented restore test with integrity validation. Actual: none; job-success logs only (EVID-035, Insufficient). | fieldwork | EVID-035, EVID-069 |
| **2. Audit finding** | FIND-013 (Moderate): Backups are taken, protected, and copied cross-region (CP-9 satisfied), but no restore of the PHI database had ever been performed or documented. Backup job success was treated as proof of recoverability. | 2026-06-26 | EVID-035, EVID-069 |
| **3. Risk** | RISK-008 Failed or slow recovery from ransomware or data corruption: current 10 High (L2×I5) | 2026-09-18 | [risk register](../risk/risk-register.md) |
| **4. POA&M** | POAM-013 opened; owner Tomasz Wierzbicki (Director, Platform Engineering); target 2026-09-01 (SLA 2027-02-03) | 2026-08-07 | [poam.md](poam.md#poam-013) |
| **5. Corrective action** | Documented restore from DR vault into isolated account with timing and integrity checks; semi-annual schedule in BCP-003 (3 milestones, first due 2026-08-21) | 2026-08-19, 2026-08-27 | — |
| **6. Validation** | Observation of restore test; inspection of timings vs RTO/RPO and integrity check output | 2026-09-01 | EVID-069 |
| **7. Closure** | Closed by Lead assessor; residual Moderate (RISK-008 residual L2 x I4 = 8, pending POAM-014) | 2026-09-01 | — |
