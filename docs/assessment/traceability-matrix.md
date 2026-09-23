# Traceability Matrix

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

Each row answers one auditor question: *how does this control get from contract language to measurable evidence, and what happened when it was tested?*

```
CONTROL → BUSINESS REQUIREMENT → IMPLEMENTATION → EVIDENCE → TEST PROCEDURE → RESULT → RISK → FINDING → REMEDIATION
```

| Control | Business requirement | Implementation | Evidence | Test procedure | Result | Risk | Finding | Remediation |
|---|---|---|---|---|---|---|---|---|
| AC-1 | REQ-001, REQ-014, REQ-024 | Access Control Policy ACP-002 v3.1 (approved 2025-01-15 by the CISO) covers account types, approvals, least privilege, separate admin accounts (§5.4), 24h de-provisioning (§5.3), inactivity (§5.6), and quarterly privileged recertification. | EVID-001, EVID-002 | Examine, Interview | ✅ Satisfied | — | — | Monitor |
| AC-2 | REQ-001, REQ-004, REQ-013, REQ-014, REQ-023 | Okta is the identity source for SSO apps. | EVID-002, EVID-005, EVID-006, EVID-007, EVID-013, EVID-061, EVID-065 | Examine, Interview, Test (TP-AC-2-01…TP-AC-2-04) | ❌ Other Than Satisfied | RISK-002, RISK-004, RISK-017 | FIND-001, FIND-004, FIND-005, FIND-006 | POAM-001 (Closed); POAM-004 (In Progress); POAM-005 (Closed); POAM-006 (Closed) |
| AC-2(1) | REQ-004, REQ-013 | Okta provisions users to GitHub and AWS IAM Identity Center with SCIM and group push. | EVID-004, EVID-005, EVID-062 | Examine, Interview | ❌ Other Than Satisfied | RISK-002 | FIND-001 | POAM-001 (Closed) |
| AC-2(3) | REQ-004, REQ-013 | ACP-002 §5.3 requires disabling within 24 hours of termination, and §5.6 requires disabling after 90 days of inactivity. | EVID-003, EVID-004, EVID-007, EVID-061, EVID-062, EVID-064 | Examine, Test (TP-AC-2(3)-01…TP-AC-2(3)-05) | ❌ Other Than Satisfied | RISK-002 | FIND-001 | POAM-001 (Closed) |
| AC-5 | REQ-023, REQ-024 | Ledgerline has an SoD ruleset (SOD-01 vendor master vs payment approval; SOD-02 AP entry vs approval). | EVID-014, EVID-015, EVID-060 | Examine, Interview, Test (TP-AC-5-01…TP-AC-5-04) | ❌ Other Than Satisfied | RISK-013 | FIND-007 | POAM-007 (Risk Accepted) |
| AC-6 | REQ-001, REQ-014, REQ-023 | A role-based access baseline exists (role_access_matrix). | EVID-006, EVID-016, EVID-017, EVID-075, EVID-076 | Examine, Test | ❌ Other Than Satisfied | RISK-001, RISK-004 | FIND-003 | POAM-003 (In Progress) |
| AC-6(2) | REQ-003, REQ-014 | ACP-002 §5.4 (since 2025-07) requires separate -adm accounts for AWS prod AdministratorAccess and Okta Super Administrator. | EVID-005, EVID-016, EVID-075 | Examine, Test | ❌ Other Than Satisfied | RISK-001 | FIND-003 | POAM-003 (In Progress) |
| AC-6(5) | REQ-003, REQ-014, REQ-023 | Defined privileged roles are SRE (AWS admin), IAM Engineer (Okta Super Admin), and CTO plus platform (up to 3 GitHub owners). | EVID-016, EVID-017, EVID-075, EVID-076, EVID-077 | Examine, Test (TP-AC-6(5)-01…TP-AC-6(5)-04) | ❌ Other Than Satisfied | RISK-001 | FIND-003 | POAM-003 (In Progress) |
| AC-6(7) | REQ-004, REQ-014, REQ-023 | Quarterly Okta manager certification campaigns cover app-assignment level access only. | EVID-008, EVID-009, EVID-074 | Examine, Interview, Test (TP-AC-6(7)-01…TP-AC-6(7)-04) | ❌ Other Than Satisfied | RISK-004 | FIND-004 | POAM-004 (In Progress) |
| AC-17 | REQ-003 | There is no network VPN into production. | EVID-018, EVID-028 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| AC-18 | REQ-001 | n/a (see applicability rationale). | EVID-040 | Examine | — Not Assessed | — | — | — |
| AT-2 | REQ-015 | Annual HIPAA and security awareness module in the LMS, plus quarterly phishing simulations. | EVID-019 | Examine, Test | ❌ Other Than Satisfied | RISK-015 | FIND-019 | POAM-019 (Completed – Pending Validation) |
| AT-3 | REQ-015 | Secure-coding training (annual) for engineers; privileged-user training for admins; HIPAA minimum-necessary training for clinical and support staff. | EVID-020 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| AU-2 | REQ-019, REQ-005 | Logging & Monitoring Standard LMS-004 defines required events. | EVID-021 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| AU-6 | REQ-019, REQ-005 | MDR monitors alerts 24x7 (SI-4). | EVID-022, EVID-072 | Examine, Test (TP-AU-6-01…TP-AU-6-03) | ❌ Other Than Satisfied | RISK-005 | FIND-009 | POAM-009 (In Progress) |
| AU-9 | REQ-019 | CloudTrail and audit logs are delivered to a dedicated log-archive account. | EVID-023 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| AU-11 | REQ-005, REQ-019 | At assessment: SIEM hot retention 90 days; the log-archive S3 lifecycle expired CloudTrail at 180 days; CloudWatch application-audit (PHI access) logs were kept 90 days with no archive. | EVID-024, EVID-067 | Examine, Test (TP-AU-11-01…TP-AU-11-04) | ❌ Other Than Satisfied | RISK-005 | FIND-008 | POAM-008 (Closed) |
| CA-2 | REQ-002, REQ-012 | Annual SOC 2 Type II examination by an independent CPA firm, an annual external penetration test (Lanternworks Security, fictional), and this SP 800-53 assessment (SAP ASMT-SAP-001). | EVID-025 | Examine, Interview | ✅ Satisfied | — | — | Monitor |
| CA-3 | REQ-018, REQ-021 | Each interconnection has an agreement (BAA plus interface or data-sharing specification). | EVID-026 | Examine | ✅ Satisfied | — | — | Monitor |
| CA-5 | REQ-002 | Before 2026-08, weaknesses were tracked in a Jira "SECISSUE" project with owners and due dates (SOC 2 remediation). | EVID-027 | Examine | ✅ Satisfied | — | — | Monitor |
| CA-7 | REQ-002, REQ-012 | Operational monitoring is in place (Security Hub CIS checks, weekly vulnerability scans, GuardDuty and MDR, a monthly security metrics deck to the CTO). | EVID-028, EVID-058 | Examine, Interview | ✅ Satisfied | RISK-016 | — | Monitor |
| CM-2 | REQ-001, REQ-023 | Infrastructure is defined in Terraform (baseline repo, PR-reviewed). | EVID-029 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| CM-3 | REQ-023 | Code and IaC changes go through GitHub PRs with required reviews and CI, then deploy through a protected environment with approvers. | EVID-030 | Examine, Test (TP-CM-3-01…TP-CM-3-03) | ❌ Other Than Satisfied | RISK-014 | FIND-018 | POAM-018 (In Progress) |
| CM-6 | REQ-001 | AWS Security Hub runs the CIS AWS Foundations benchmark across accounts (97% of controls passing at 2026-06-30). | EVID-028, EVID-053, EVID-068 | Examine, Test | ❌ Other Than Satisfied | RISK-012, RISK-007 | FIND-012 | POAM-012 (Closed) |
| CM-8 | REQ-001 | AWS Config aggregator (all accounts) plus the MDM inventory for endpoints. | EVID-031 | Examine, Test | ✅ Satisfied | RISK-006 | — | Monitor |
| CP-2 | REQ-011, REQ-017 | BC/DR Plan BCP-003 v2.1 (2025-11). | EVID-032 | Examine, Interview | ✅ Satisfied | — | — | Monitor |
| CP-4 | REQ-011, REQ-017 | The owner cited a 2024 AZ-failover exercise. | EVID-033 | Examine, Interview | ❌ Other Than Satisfied | RISK-008 | FIND-014 | POAM-014 (In Progress) |
| CP-9 | REQ-011, REQ-017 | Aurora continuous backup (PITR, 35 days), plus daily AWS Backup copies to the wcp-dr account in us-west-2 in a vault with Vault Lock (compliance mode) and KMS encryption. | EVID-034 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| CP-9(1) | REQ-011, REQ-017 | The owner treated backup-job success notifications as testing. | EVID-035, EVID-069 | Examine, Test (TP-CP-9(1)-01…TP-CP-9(1)-03) | ❌ Other Than Satisfied | RISK-008 | FIND-013 | POAM-013 (Closed) |
| IA-2 | REQ-020 | Every workforce user has a unique Okta identity tied to an HR worker ID. | EVID-005 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| IA-2(1) | REQ-003, REQ-020 | The Okta global session policy requires MFA except for members of MFA-Exempt-Legacy (a 2023 policy). | EVID-007, EVID-010, EVID-011, EVID-063, EVID-064 | Examine, Test (TP-IA-2(1)-01…TP-IA-2(1)-04) | ❌ Other Than Satisfied | RISK-003, RISK-001 | FIND-002 | POAM-002 (Closed) |
| IA-2(2) | REQ-003, REQ-020 | As for IA-2(1). | EVID-010, EVID-011, EVID-063 | Examine, Test | ❌ Other Than Satisfied | RISK-003 | FIND-002 | POAM-002 (Closed) |
| IA-2(8) | REQ-020 | All enabled authenticators are replay-resistant (Okta Verify push with number challenge, FastPass, FIDO2/WebAuthn, TOTP). | EVID-012, EVID-010 | Examine | ✅ Satisfied | — | — | Monitor |
| IA-5 | REQ-020 | Human authenticators are strong (Okta password policy plus MFA; help-desk identity verification SOP). | EVID-007, EVID-013, EVID-064, EVID-065 | Examine, Test | ❌ Other Than Satisfied | RISK-017 | FIND-005 | POAM-005 (Closed) |
| IR-3 | REQ-006, REQ-016 | IRP-005 requires an annual tabletop exercise that includes the MDR, Legal/Privacy, and Customer Ops. | EVID-037 | Examine, Interview (TP-IR-3-01…TP-IR-3-03) | ❌ Other Than Satisfied | RISK-009 | FIND-014 | POAM-014 (In Progress) |
| IR-4 | REQ-016 | 24x7 MDR triage with escalation to the on-call security engineer. | EVID-038, EVID-078 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| IR-6 | REQ-006, REQ-016, REQ-022 | Workforce reporting through the #security-report Slack channel, the phone line, or MDR. | EVID-038 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| IR-8 | REQ-006, REQ-016 | IRP-005 v4.0 was reviewed 2025-11 and approved by the CISO. | EVID-036 | Examine | ✅ Satisfied | RISK-009 | — | Monitor |
| MP-6 | REQ-021 | Laptops are FDE-encrypted. | EVID-039, EVID-040 | Examine, Test | ✅ Satisfied | RISK-018 | — | Monitor |
| PE-3 | REQ-001 | Inherited. | EVID-040 | Examine | ✅ Satisfied | — | — | Monitor |
| PL-2 | REQ-001, REQ-002 | SSP v1.3 dated 2025-02. | EVID-041 | Examine | ❌ Other Than Satisfied | RISK-016 | FIND-017 | POAM-017 (In Progress) |
| PM-9 | REQ-024, REQ-012 | Risk Management Strategy RMS-001 and a Board-approved Risk Appetite Statement (2025-10-21) define appetite by rating, acceptance authority, and escalation. | EVID-042, EVID-060 | Examine, Interview | ✅ Satisfied | — | — | Monitor |
| PS-3 | REQ-014 | Background checks are required before system access for all employees. | EVID-043 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| PS-4 | REQ-004, REQ-013 | HR processes terminations in PeopleHub and emails IT. | EVID-003, EVID-004, EVID-061 | Examine, Test | ❌ Other Than Satisfied | RISK-002 | FIND-001 | POAM-001 (Closed) |
| PS-5 | REQ-014 | Transfers are updated in PeopleHub. | EVID-044 | Examine, Test | ❌ Other Than Satisfied | RISK-004 | FIND-004 | POAM-004 (In Progress) |
| PS-7 | REQ-004, REQ-008, REQ-013 | The Northgate MSA requires screening and 2-business-day notice of contractor departures. | EVID-045, EVID-066 | Examine, Test | ❌ Other Than Satisfied | RISK-002, RISK-004 | FIND-006, FIND-001 | POAM-006 (Closed); POAM-001 (Closed) |
| RA-2 | REQ-001, REQ-012 | FIPS 199 categorization worksheet (2025-06) rates WCP-PROD Moderate. | EVID-046 | Examine, Interview | ✅ Satisfied | — | — | Monitor |
| RA-3 | REQ-012 | Annual HIPAA risk analysis (2025-09 report) using an SP 800-30-style method. | EVID-047 | Examine | ✅ Satisfied | — | — | Monitor |
| RA-5 | REQ-009 | Weekly authenticated scanning of EC2 and EKS nodes (agent-based), container image scanning in CI and in the registry, and a weekly external scan of internet-facing endpoints. | EVID-048, EVID-031 | Examine, Test | ✅ Satisfied | RISK-006 | — | Monitor |
| RA-7 | REQ-012, REQ-024 | Findings receive a treatment decision (mitigate, accept, transfer, or avoid) per RSK-MTH-001, with acceptance authority by rating. | EVID-027, EVID-060 | Examine | ✅ Satisfied | — | — | Monitor |
| SA-9 | REQ-007, REQ-008, REQ-018 | The Third-Party Risk Management Standard TPRM-007 requires tiering, due diligence before contract, security terms (BAA, notification, data return), and reassessment (Tier 1 annually, Tier 2 every 2 years). | EVID-049, EVID-026, EVID-050, EVID-051, EVID-073 | Examine, Interview, Test | ❌ Other Than Satisfied | RISK-010, RISK-011 | FIND-015, FIND-016 | POAM-015 (In Progress); POAM-016 (In Progress) |
| SA-22 | REQ-010 | Most components are current. | EVID-052, EVID-048 | Examine, Test (TP-SA-22-01…TP-SA-22-03) | ❌ Other Than Satisfied | RISK-007 | FIND-011 | POAM-011 (Delayed) |
| SC-7 | REQ-001, REQ-021 | Public traffic enters through CloudFront and WAF to internal ALBs. | EVID-053, EVID-028, EVID-068 | Examine, Test | ❌ Other Than Satisfied | RISK-012, RISK-007 | FIND-012 | POAM-012 (Closed) |
| SC-8 | REQ-021 | TLS 1.2+ only (the CloudFront and ALB security policies disable TLS 1.0/1.1). | EVID-054 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| SC-12 | REQ-021 | Customer-managed KMS keys for Aurora, S3 PHI buckets, EBS, and backups, with annual automatic rotation enabled. | EVID-055 | Examine | ✅ Satisfied | — | — | Monitor |
| SC-28 | REQ-021 | Aurora storage encryption (KMS CMK), S3 default encryption with bucket keys, EBS encryption-by-default at the account level, and backup vault encryption. | EVID-056 | Examine, Test (TP-SC-28-01…TP-SC-28-03) | ✅ Satisfied | RISK-018 | — | Monitor |
| SI-2 | REQ-009 | VM-003 sets SLAs of Critical 15 days, High 30, and Moderate 90. | EVID-048 | Examine, Test (TP-SI-2-01…TP-SI-2-03) | ❌ Other Than Satisfied | RISK-006 | FIND-010 | POAM-010 (In Progress) |
| SI-3 | REQ-016 | EDR on endpoints and EC2 hosts (including wf-sftp-01), runtime protection on EKS nodes (DaemonSet), and email security filtering. | EVID-057, EVID-038 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| SI-4 | REQ-019, REQ-016 | GuardDuty (all accounts), SIEM correlation rules (Okta anomalies, impossible travel, privilege escalation), and 24x7 MDR triage with a 30-minute SLA for High alerts. | EVID-058 | Examine, Test | ✅ Satisfied | — | — | Monitor |
| SR-2 | REQ-008, REQ-001 | No C-SCRM plan exists. | EVID-059 | Examine, Interview | ❌ Other Than Satisfied | RISK-011 | FIND-015 | POAM-015 (In Progress) |
| SR-6 | REQ-008, REQ-018 | Tier-based reassessment (Tier 1 annually) using a questionnaire plus attestation review (SOC 2 and pentest summaries). | EVID-049, EVID-050, EVID-051 | Examine, Test (TP-SR-6-01…TP-SR-6-04) | ❌ Other Than Satisfied | RISK-010, RISK-011 | FIND-015, FIND-016 | POAM-015 (In Progress); POAM-016 (In Progress) |

## Requirement coverage (reverse view)
Every business requirement maps to at least one tested control ([tools/validate.py](../../tools/validate.py) enforces this).

| REQ | Source | Requirement | Controls |
|---|---|---|---|
| REQ-001 | SHCA Contract Security Addendum §2.1 | Maintain security controls aligned to the NIST SP 800-53 Rev. 5 Moderate baseline for systems that store, process, or transmit agency data. | AC-1, AC-2, AC-6, AC-18, CM-2, CM-6, CM-8, PE-3, PL-2, RA-2, SC-7, SR-2 |
| REQ-002 | SHCA CSA §2.4 | Deliver a security assessment report and POA&M at least 90 days before go-live, then quarterly. No High POA&M item may be older than 90 days at go-live. | CA-2, CA-5, CA-7, PL-2 |
| REQ-003 | SHCA CSA §3.2 | Enforce multi-factor authentication for all privileged access and all remote access to systems handling agency data. | AC-6(2), AC-6(5), AC-17, IA-2(1), IA-2(2) |
| REQ-004 | SHCA CSA §3.3 | Disable access for terminated personnel within 24 hours. Recertify privileged access quarterly and all access at least annually. | AC-2, AC-2(1), AC-2(3), AC-6(7), PS-4, PS-7 |
| REQ-005 | SHCA CSA §4.1 | Retain audit logs for systems handling agency data for at least 12 months, with at least 90 days immediately searchable. | AU-2, AU-6, AU-11 |
| REQ-006 | SHCA CSA §5.2 | Report security incidents involving agency data to SHCA within 24 hours of discovery. Test incident response capability annually. | IR-3, IR-6, IR-8 |
| REQ-007 | SHCA CSA §6.1 | Store, process, and access agency data only within the United States. No offshore access, including by subcontractors. | SA-9 |
| REQ-008 | SHCA CSA §6.3 | Flow security requirements down to subcontractors handling agency data. Keep a subcontractor inventory, and obtain SHCA approval before a subcontractor accesses agency data. | PS-7, SA-9, SR-2, SR-6 |
| REQ-009 | SHCA CSA §7.1 | Remediate vulnerabilities within: Critical 15 days, High 30 days, Moderate 90 days. | RA-5, SI-2 |
| REQ-010 | SHCA CSA §7.4 | Use only vendor-supported software (OS, databases, runtimes) for components that process agency data, or document compensating controls approved by SHCA. | SA-22 |
| REQ-011 | SHCA CSA §8.1 | Maintain backups of agency data. Test restoration and the contingency plan at least annually. | CP-2, CP-4, CP-9, CP-9(1) |
| REQ-012 | HIPAA 45 CFR 164.308(a)(1)(ii)(A)-(B) | Conduct an accurate and thorough risk analysis, and implement security measures that reduce risks to a reasonable and appropriate level. | CA-2, CA-7, PM-9, RA-2, RA-3, RA-7 |
| REQ-013 | HIPAA 45 CFR 164.308(a)(3)(ii)(C) | Implement procedures for terminating access to ePHI when workforce employment or engagement ends. | AC-2, AC-2(1), AC-2(3), PS-4, PS-7 |
| REQ-014 | HIPAA 45 CFR 164.308(a)(4)(ii)(B)-(C) | Implement policies for authorizing, establishing, documenting, reviewing, and modifying access to ePHI. | AC-1, AC-2, AC-6, AC-6(2), AC-6(5), AC-6(7), PS-3, PS-5 |
| REQ-015 | HIPAA 45 CFR 164.308(a)(5)(i) | Implement a security awareness and training program for all workforce members. | AT-2, AT-3 |
| REQ-016 | HIPAA 45 CFR 164.308(a)(6)(ii) | Identify and respond to suspected or known security incidents, mitigate harmful effects, and document incidents and outcomes. | IR-3, IR-4, IR-6, IR-8, SI-3, SI-4 |
| REQ-017 | HIPAA 45 CFR 164.308(a)(7)(ii)(A),(B),(D) | Maintain a data backup plan and a disaster recovery plan, with testing and revision procedures. | CP-2, CP-4, CP-9, CP-9(1) |
| REQ-018 | HIPAA 45 CFR 164.308(b)(1); 164.314(a) | Obtain satisfactory assurances (business associate agreements) from subcontractors that create, receive, maintain, or transmit ePHI. | CA-3, SA-9, SR-6 |
| REQ-019 | HIPAA 45 CFR 164.312(b) | Implement mechanisms that record and examine activity in information systems containing ePHI (audit controls). | AU-2, AU-6, AU-9, AU-11, SI-4 |
| REQ-020 | HIPAA 45 CFR 164.312(d) | Verify that a person or entity seeking access to ePHI is the one claimed (person or entity authentication). | IA-2, IA-2(1), IA-2(2), IA-2(8), IA-5 |
| REQ-021 | HIPAA 45 CFR 164.312(a)(2)(iv), (e)(1) | Protect ePHI with encryption at rest where reasonable and appropriate, and guard against unauthorized access during transmission. | CA-3, MP-6, SC-7, SC-8, SC-12, SC-28 |
| REQ-022 | Customer BAAs/MSAs (standard Wrenfield paper) | Notify customers of breaches of unsecured PHI within 5 business days of discovery. Answer annual security questionnaires. Allow customer audits. | IR-6 |
| REQ-023 | SOC 2 system description commitments (CC6.1–CC6.3, CC8.1) | Restrict logical access by role, approve and remove access in a timely way, review access periodically, and authorize changes before deployment. | AC-2, AC-5, AC-6, AC-6(5), AC-6(7), CM-2, CM-3 |
| REQ-024 | Wrenfield Information Security Policy ISP-001 v4.0 and Risk Appetite Statement (Board-approved 2025-10-21) | Manage cybersecurity risk within Board-approved appetite. No Critical risk may be accepted, and High risks need CEO acceptance. | AC-1, AC-5, PM-9, RA-7 |
