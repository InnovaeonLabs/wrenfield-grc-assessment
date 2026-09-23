# Evidence Request List (PBC) and Status

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

Tracker: [evidence-tracker.xlsx](evidence-tracker.xlsx) · [CSV](evidence-tracker.csv) · Quality rules: [evidence-quality-guide.md](evidence-quality-guide.md)

**How requests were written.** Each request names the **artifact**, the **period** or as-of date, the **population** ("ALL terminations", not "some examples"), and the **format** (system-generated export over screenshot). Vague requests produce vague evidence.

## Status as of 2026-09-18
| Status | Count |
|---|---|
| Requested | 2 |
| Received | 1 |
| Under Review | 2 |
| Accepted | 58 |
| Insufficient | 5 |
| Rework Required | 1 |
| Closed | 9 |
| **Total** | **78** |

**Evidence completion = (Accepted + Closed) / requested = 67 / 78 = 86%.** Insufficient items are not "complete". Each one became part of a finding.

| Highest evidence level | Items |
|---|---|
| Design | 19 |
| Implementation | 34 |
| Operating Effectiveness | 25 |

## Requests by control family
### AC: Access Control
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-001 | AC-1 | Current Access Control Policy with approval record and review history · *Current version* | Alicia Moreno | 2026-06-19 | Accepted | Design | — |
| EVID-002 | AC-2, AC-2(3), PS-4, PS-5 | Joiner/mover/leaver procedure · *Current version* | Nadia Rahman | 2026-06-19 | Accepted | Design | — |
| EVID-003 | AC-2(3), PS-4 | System-generated list of ALL terminations 2026-01-01 to 2026-06-30 (worker ID, type, date, effective time) · *2026-01-01 to 2026-06-30* | Denise Yamamoto | 2026-06-19 | Accepted | Operating Effectiveness | [file](../evidence/AC/EVID-003_peoplehub-terminations-2026H1.csv) |
| EVID-004 | AC-2(3) | Okta System Log export of user.lifecycle.deactivate events for the period · *2026-01-01 to 2026-06-30* | Nadia Rahman | 2026-06-19 | Accepted | Operating Effectiveness | [file](../evidence/AC/EVID-004_okta-deactivation-events-2026H1.csv) |
| EVID-005 | AC-2, AC-2(1), IA-2, AC-6(2) | Okta user export (all statuses) with MFA enrollment and group membership as of 2026-06-30 · *As of 2026-06-30* | Nadia Rahman | 2026-06-19 | Accepted | Implementation | [file](../access-review/source-exports/okta_users.csv) |
| EVID-006 | AC-2, AC-6, AC-6(5) | Entitlement exports from each in-scope system as of 2026-06-30 · *As of 2026-06-30* | System owners (9 systems) | 2026-07-01 | Accepted | Implementation | [file](../access-review/source-exports/entitlements.csv) |
| EVID-007 | AC-2, IA-2(1), IA-5 | AWS IAM credential report for wcp-prod · *As of 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Implementation | [file](../evidence/IA/EVID-007_aws-iam-credential-report_2026-06-30.csv) |
| EVID-008 | AC-6(7) | Q1 2026 access certification campaign export (reviewer, item, decision, timestamp) · *2026-03-02 to 2026-03-20* | Alicia Moreno | 2026-06-19 | Accepted | Operating Effectiveness | [file](../evidence/AC/EVID-008_q1-certification-summary.md) |
| EVID-009 | AC-6(7) | Evidence that quarterly access reviews are performed · *Undated* | Alicia Moreno | 2026-06-19 | Insufficient | Design | [file](../evidence/AC/EVID-009_insufficient-screenshot-example.md) |
| EVID-013 | AC-2, IA-5 | Service-account register with owner, purpose, credential type, and last rotation · *As of 2026-06-30* | Nadia Rahman | 2026-06-26 | Accepted | Implementation | [file](../access-review/source-exports/service_accounts.csv) |
| EVID-014 | AC-5 | Ledgerline role and permission matrix and SoD ruleset · *Current* | Laura Brenneman | 2026-06-19 | Accepted | Design | [file](../access-review/source-exports/sod_rules.csv) |
| EVID-015 | AC-5 | Monthly vendor-master change reports with reviewer sign-off (Jan–Jun) · *2026-01 to 2026-06* | Laura Brenneman | 2026-06-19 | Accepted | Operating Effectiveness | — |
| EVID-016 | AC-6, AC-6(2), AC-6(5) | AWS IAM Identity Center permission-set assignments for wcp-prod · *As of 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Implementation | [file](../access-review/source-exports/entitlements.csv) |
| EVID-017 | AC-6(5) | GitHub organization owners and repository admins · *As of 2026-06-30* | Grace Lindqvist | 2026-06-19 | Accepted | Implementation | [file](../access-review/source-exports/entitlements.csv) |
| EVID-018 | AC-17 | Remote administrative access architecture and session logging configuration · *As of 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Implementation | — |
| EVID-061 | AC-2, AC-2(3), PS-4, PS-5 | Revocation tickets for AR-EX-01/02/04/12/13/14 and all terminations 2026-07-01 to 2026-09-09 with de-provisioning timestamps · *2026-07-01 to 2026-09-09* | Nadia Rahman | 2026-09-10 | Closed | Operating Effectiveness | [file](../evidence/AC/EVID-061_terminations-and-deactivations_2026-07-01_to_09-09.csv) |
| EVID-062 | AC-2(1), AC-2(3) | HR-to-Okta reconciliation job design and last 5 run outputs · *2026-09-04 to 2026-09-10* | Nadia Rahman | 2026-09-10 | Closed | Operating Effectiveness | [file](../evidence/AC/EVID-062_hr-okta-reconciliation-job_2026-09-10.csv) |
| EVID-065 | AC-2, IA-5 | Updated service-account register showing owners, rotation, federation changes · *As of 2026-09-11* | Nadia Rahman | 2026-09-12 | Closed | Implementation | — |
| EVID-071 | AC-6, AC-6(5) | Just-in-time elevation workflow design and a live elevation record · *As of 2026-09-10* | Tomasz Wierzbicki | 2026-09-12 | Rework Required | Design | — |
| EVID-074 | AC-6(7) | Q3 2026 privileged access certification (new design) · *2026-Q3* | Alicia Moreno | 2026-09-30 | Requested | Operating Effectiveness | — |
| EVID-075 | AC-6, AC-6(2), AC-6(5) | Identity Center assignment export after privilege reduction · *As of 2026-09-03* | Tomasz Wierzbicki | 2026-09-05 | Accepted | Implementation | — |
| EVID-076 | AC-6(5) | GitHub org owners after reduction · *As of 2026-08-12* | Grace Lindqvist | 2026-08-14 | Accepted | Implementation | — |
| EVID-077 | AC-6(5), AC-6(2) | Okta administrator role assignment report after change · *As of 2026-07-21* | Nadia Rahman | 2026-07-24 | Accepted | Implementation | — |
### AT: Awareness and Training
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-019 | AT-2 | LMS completion report for annual security awareness (full workforce) and phishing simulation results · *FY2026 cycle as of 2026-06-30* | Denise Yamamoto | 2026-06-19 | Accepted | Operating Effectiveness | — |
| EVID-020 | AT-3 | Role-based training completion for engineers, admins, clinical/support staff · *2026-01-01 to 2026-06-30* | Denise Yamamoto | 2026-06-19 | Accepted | Operating Effectiveness | — |
| EVID-070 | AT-2 | LMS completion report after enforcement · *As of 2026-09-12* | Denise Yamamoto | 2026-09-15 | Under Review | Operating Effectiveness | — |
### AU: Audit and Accountability
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-021 | AU-2 | Logging standard, trail configurations, and sample events for required types · *As of 2026-06-30* | Owen Castillo | 2026-06-19 | Accepted | Implementation | — |
| EVID-022 | AU-6 | All weekly privileged-activity review tickets W01–W26 · *2026-W01 to 2026-W26* | Owen Castillo | 2026-06-19 | Accepted | Operating Effectiveness | [file](../evidence/AU/EVID-022_privileged-activity-reviews-2026H1.csv) |
| EVID-023 | AU-9 | Log archive bucket protections and SCPs · *As of 2026-06-30* | Owen Castillo | 2026-06-19 | Accepted | Implementation | — |
| EVID-024 | AU-11 | Retention settings for every audit source plus oldest available record per source · *As of 2026-06-30* | Owen Castillo | 2026-06-19 | Accepted | Implementation | [file](../evidence/AU/EVID-024_log-retention-config_2026-06-30.json) |
| EVID-067 | AU-11 | Retention configuration after change + oldest-record checks · *As of 2026-09-12* | Owen Castillo | 2026-09-15 | Closed | Implementation | [file](../evidence/AU/EVID-067_log-retention-config_2026-09-12.json) |
| EVID-072 | AU-6 | Weekly review tickets W27–W37 after the backup-reviewer change · *2026-W27 to 2026-W37* | Owen Castillo | 2026-09-15 | Received | Operating Effectiveness | — |
### CA: Assessment, Authorization, and Monitoring
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-025 | CA-2 | Most recent SOC 2 Type II report and external penetration test report · *FY2025* | Priya Raman | 2026-06-19 | Accepted | Operating Effectiveness | — |
| EVID-026 | CA-3, SA-9 | Quarrystone MSA/BAA and data sharing specification; 3 customer interface specs · *Current* | Liam Porter | 2026-06-19 | Accepted | Design | — |
| EVID-027 | CA-5, RA-7 | Existing security issue tracking (pre-assessment) · *2025-07-01 to 2026-06-30* | Priya Raman | 2026-06-19 | Accepted | Operating Effectiveness | — |
### CM: Configuration Management
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-028 | CM-6, CA-7, SC-7, AC-17 | Security Hub CIS benchmark results and finding history · *2026-01-01 to 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Implementation | — |
| EVID-029 | CM-2 | Terraform baseline and AMI build specification; drift check output · *As of 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Implementation | — |
| EVID-030 | CM-3 | Population of production changes (212) and full records for the 25 sampled (seed 20260618) · *2026-01-01 to 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Operating Effectiveness | [file](../evidence/CM/EVID-030_change-sample-2026H1.csv) |
| EVID-031 | CM-8, RA-5 | Asset inventory (AWS Config aggregator + MDM) with tag compliance · *As of 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Implementation | — |
### CP: Contingency Planning
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-032 | CP-2 | Current BC/DR plan · *Current version* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Design | — |
| EVID-033 | CP-4 | Contingency plan test records (last 24 months) · *2024-07-01 to 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Insufficient | Design | — |
| EVID-034 | CP-9 | Backup plans, job history (30 days), vault protections · *2026-06-01 to 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Operating Effectiveness | — |
| EVID-035 | CP-9(1) | Backup restore test records · *2025-07-01 to 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Insufficient | Implementation | — |
| EVID-069 | CP-9(1) | Restore test record with timings and integrity checks · *2026-08-27* | Tomasz Wierzbicki | 2026-09-01 | Closed | Operating Effectiveness | [file](../evidence/CP/EVID-069_restore-test-record_2026-08-27.md) |
### IA: Identification and Authentication
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-010 | IA-2(1), IA-2(2), IA-2(8) | Okta authentication and global session policy export · *As of 2026-06-30* | Nadia Rahman | 2026-06-19 | Accepted | Implementation | [file](../evidence/IA/EVID-010_okta-authentication-policies_2026-06-30.json) |
| EVID-011 | IA-2(1), IA-2(2) | Membership of all MFA exemption groups with reason and approval · *As of 2026-06-30* | Nadia Rahman | 2026-06-19 | Accepted | Implementation | [file](../evidence/IA/EVID-011_okta-mfa-exempt-group_2026-06-30.csv) |
| EVID-012 | IA-2(8) | Enabled authenticator configuration · *As of 2026-06-30* | Nadia Rahman | 2026-06-19 | Accepted | Implementation | — |
| EVID-063 | IA-2(1), IA-2(2) | Okta policy export after remediation + group deletion record · *As of 2026-09-04* | Nadia Rahman | 2026-09-05 | Closed | Implementation | [file](../evidence/IA/EVID-063_okta-authentication-policies_2026-09-04.json) |
| EVID-064 | IA-2(1), IA-5, AC-2(3) | AWS IAM credential report after remediation · *As of 2026-09-04* | Tomasz Wierzbicki | 2026-09-05 | Closed | Implementation | [file](../evidence/IA/EVID-064_aws-iam-credential-report_2026-09-04.csv) |
### IR: Incident Response
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-036 | IR-8 | Current incident response plan with review history · *Current version* | Owen Castillo | 2026-06-19 | Accepted | Design | — |
| EVID-037 | IR-3 | IR test/exercise records (last 24 months) · *2024-07-01 to 2026-06-30* | Owen Castillo | 2026-06-19 | Insufficient | Design | — |
| EVID-038 | IR-4, IR-6, SI-3 | All incident tickets for the period with timelines and notifications · *2026-01-01 to 2026-06-30* | Owen Castillo | 2026-06-19 | Accepted | Operating Effectiveness | [file](../evidence/IR/EVID-038_incident-tickets-2026H1.csv) |
| EVID-078 | IR-4, AC-2(3) | Investigation record for INC-2026-0117 (post-termination sign-in) · *2026-07-06 to 2026-07-09* | Owen Castillo | 2026-07-10 | Accepted | Operating Effectiveness | [file](../evidence/IR/EVID-078_INC-2026-0117-investigation.md) |
### MP: Media Protection
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-039 | MP-6 | Certificates of destruction for all devices retired in the period · *2026-01-01 to 2026-06-30* | Kevin Brandt | 2026-06-19 | Accepted | Operating Effectiveness | — |
### PE: Physical and Environmental Protection
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-040 | PE-3, MP-6, AC-18 | Inherited-control record and provider attestation review log; boundary definition · *Current* | Priya Raman | 2026-06-19 | Accepted | Design | [file](../docs/scope/system-profile.md) |
### PL: Planning
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-041 | PL-2 | Current system security plan · *Current version* | Priya Raman | 2026-06-19 | Accepted | Design | — |
### PM: Program Management
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-042 | PM-9 | Risk management strategy and Board-approved risk appetite · *Current* | Alicia Moreno | 2026-06-19 | Accepted | Design | — |
### PS: Personnel Security
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-043 | PS-3 | Background-check completion for 15 sampled H1 hires/contractors · *2026-01-01 to 2026-06-30* | Denise Yamamoto | 2026-06-19 | Accepted | Operating Effectiveness | — |
| EVID-044 | PS-5 | All transfers in period with before/after access · *2026-01-01 to 2026-06-30* | Denise Yamamoto | 2026-06-19 | Accepted | Operating Effectiveness | — |
| EVID-045 | PS-7 | Contractor roster with SOW start/end dates and scope · *2026-01-01 to 2026-06-30* | Sofia Ricci | 2026-06-19 | Accepted | Implementation | — |
| EVID-066 | PS-7 | Contractor end-date sync report and SOW amendment · *As of 2026-09-08* | Sofia Ricci | 2026-09-10 | Closed | Implementation | — |
### RA: Risk Assessment
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-046 | RA-2 | FIPS 199 categorization worksheet with approval · *Current* | Samir Haddad | 2026-06-19 | Accepted | Design | [file](../docs/scope/system-profile.md) |
| EVID-047 | RA-3 | Most recent risk assessment · *FY2025* | Priya Raman | 2026-06-19 | Accepted | Design | — |
| EVID-048 | RA-5, SI-2, SA-22 | All Critical/High vulnerability findings open at any point in H1, with detection and remediation dates · *2026-01-01 to 2026-06-30* | Owen Castillo | 2026-06-19 | Accepted | Operating Effectiveness | [file](../evidence/RA/EVID-048_vuln-remediation-aging-2026H1.csv) |
| EVID-060 | RA-7, AC-5, PM-9 | Signed risk acceptance for SoD conflict · *2026-08-12 to 2027-03-31* | Laura Brenneman | 2026-08-14 | Accepted | Design | [file](../risk/risk-acceptance/RACC-001.md) |
### SA: System and Services Acquisition
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-049 | SA-9, SR-6 | Vendor inventory with tiers and assessment dates · *As of 2026-06-30* | Beth Kowalski | 2026-06-19 | Accepted | Implementation | [file](../vendor-risk/vendor-assessment.xlsx) |
| EVID-052 | SA-22 | OS/database/runtime inventory with vendor support dates · *As of 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Implementation | — |
| EVID-073 | SA-9, SR-6 | Quarrystone contract amendment (redline) and interim US-only access confirmation · *As of 2026-09-15* | Beth Kowalski | 2026-09-30 | Under Review | Design | — |
### SC: System and Communications Protection
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-053 | SC-7, CM-6 | Security group rules for wf-sftp-01 and all groups with 0.0.0.0/0 ingress · *As of 2026-07-02* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Implementation | [file](../evidence/CM/EVID-053_wf-sftp-01-security-group_2026-07-02.json) |
| EVID-054 | SC-8 | TLS policies and database SSL enforcement; external TLS scan · *As of 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Implementation | — |
| EVID-055 | SC-12 | KMS key inventory, rotation, key policies · *As of 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Implementation | — |
| EVID-056 | SC-28 | Encryption status for all data stores; endpoint encryption compliance · *As of 2026-06-30* | Tomasz Wierzbicki | 2026-06-19 | Accepted | Implementation | — |
| EVID-068 | SC-7, CM-6 | Security group change record and Security Hub re-evaluation · *As of 2026-07-10* | Tomasz Wierzbicki | 2026-07-10 | Closed | Implementation | — |
### SI: System and Information Integrity
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-057 | SI-3 | EDR coverage reconciled to inventory · *As of 2026-06-30* | Owen Castillo | 2026-06-19 | Accepted | Implementation | — |
| EVID-058 | SI-4, CA-7 | Detection inventory and MDR triage metrics; 10 sample alerts · *2026-01-01 to 2026-06-30* | Owen Castillo | 2026-06-19 | Accepted | Operating Effectiveness | — |
### SR: Supply Chain Risk Management
| ID | Controls | Request (what, period, format) | Owner | Due | Status | Level | Sample in repo |
|---|---|---|---|---|---|---|---|
| EVID-050 | SR-6, SA-9 | Quarrystone SOC 2 Type II report and bridge letter · *2024-10-01 to 2026-03-31* | Beth Kowalski | 2026-06-19 | Accepted | Operating Effectiveness | [file](../evidence/SR/EVID-050_quarrystone-soc2-review-workpaper.md) |
| EVID-051 | SR-6 | Quarrystone most recent penetration test report and retest evidence · *2025-03* | Beth Kowalski (vendor-sourced) | 2026-08-07 | Requested | Design | — |
| EVID-059 | SR-2 | Approved C-SCRM plan · *Current* | Beth Kowalski | 2026-06-19 | Insufficient | Design | — |
