# Vendor Risk Assessment: Quarrystone Analytics (fictional)

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

Workbooks: [vendor-assessment.xlsx](vendor-assessment.xlsx) (inventory with tiering formulas, profile, fourth parties, assessment, findings, decision) · [vendor-questionnaire.xlsx](vendor-questionnaire.xlsx) (blank template + responses) · Executive summary: [vendor-summary.md](vendor-summary.md)

## 1. Program view: vendor inventory and tiering
Tier 1–2 vendors with a current assessment: **9 of 14** (status date 2026-09-18). This is the SR-6 test behind FIND-015.

| ID | Vendor | Service | Score | Tier | Last assessed | Current? | Breach notice |
|---|---|---|---|---|---|---|---|
| VEN-001 | AWS | IaaS/PaaS hosting for WCP-PROD (BAA) | 14 | 1 | 2026-03-12 | Yes | Per provider BAA |
| VEN-002 | Okta | Workforce identity (SSO/MFA) | 12 | 1 | 2026-02-20 | Yes | Per provider terms |
| VEN-003 | GitHub | Source code, CI/CD (Actions) | 9 | 1 | 2026-01-28 | Yes | Per provider terms |
| VEN-004 | Quarrystone Analytics, LLC (fictional) | Population-health analytics; nightly full-PHI extract (about 410k patients) | 12 | 1 | 2026-07-24 | Yes | 30 days (BAA 2023) |
| VEN-005 | Pulsewire Connect (fictional) | RPM cellular hubs and device-data API | 13 | 1 | 2024-08-14 | No (overdue) | 10 days |
| VEN-006 | Ironpeak MDR (fictional) | 24x7 managed detection and response (SIEM/EDR access) | 10 | 1 | 2024-12-09 | No (overdue) | 48 hours |
| VEN-007 | Google Workspace | Email and documents (BAA) | 10 | 1 | 2026-04-09 | Yes | Per provider BAA |
| VEN-008 | Brightdesk (fictional) | Customer-support ticketing (limited PHI) | 7 | 2 | 2025-05-20 | Yes | 5 business days |
| VEN-009 | Clearpath Messaging (fictional) | Patient SMS/voice reminders (name + phone + appointment time) | 8 | 2 | 2024-05-06 | No (overdue) | Without unreasonable delay (no fixed period) |
| VEN-010 | PeopleHub (fictional) | HRIS (authoritative source for JML) | 7 | 2 | 2025-03-18 | Yes | 72 hours |
| VEN-011 | Ledgerline (fictional) | ERP / finance | 7 | 2 | 2025-09-02 | Yes | 72 hours |
| VEN-012 | Northgate Talent Partners (fictional) | Contract engineering staff (contractors receive privileged access) | 5 | 2 | never | No (never) | None in MSA |
| VEN-013 | Beaconline SIEM (fictional) | Cloud SIEM | 8 | 2 | 2025-02-11 | Yes | 72 hours |
| VEN-014 | Coldwater Secure Destruction (fictional) | IT asset disposition | 2 | 3 | 2025-10-01 | Yes | 5 business days |
| VEN-015 | Lanternworks Security (fictional) | Annual penetration testing | 4 | 3 | 2025-11-15 | Yes | 24 hours |
| VEN-016 | Tallis Print & Mail (fictional) | Patient letters (names, addresses, program info) | 8 | 2 | never | No (never) | BAA executed 2023; no timeline |

## 2. Vendor profile (VEN-004)
| Attribute | Detail |
|---|---|
| Name | Quarrystone Analytics, LLC (fictional) |
| Service | Population-health risk stratification and care-gap analytics. Nightly scores rank patients for care-manager outreach. |
| Business Owner | Dr. Miriam Castell, VP Clinical Analytics |
| Technical Owner | Liam Porter, Data Engineering Manager |
| Contract | MSA + BAA signed 2023-02-15 on vendor paper; renewal 2027-01-31 (negotiation leverage); annual fee $410k |
| Data Accessed | Full PHI extract of about 410,000 patients: name, DOB, address, phone, email, MRN, member ID, ICD-10 diagnoses, medications, vitals and RPM readings, care-plan events, free-text care notes (58 fields) |
| Data Sensitivity | PHI (regulated). Adds Medicaid member data after SHCA go-live. |
| Integration | Outbound: nightly SFTP push from wf-sftp-01 (Windows 2012 R2, unsupported) to the vendor landing zone. Inbound: risk scores pulled over HTTPS by API key (svc-qs-api). Portal: 6 Wrenfield user accounts plus 1 API key, local authentication (no SSO). |
| Criticality | High. Scores drive outreach prioritization. WCP has a rules-based fallback, so an outage degrades quality but does not stop care. Integrity matters: bad scores could mis-rank patients. |
| Geography | Vendor HQ Denver, CO. Storage in US (cloud region us-east-1). Access includes an offshore subcontractor in Pune, India. |
| Inherent Score | 12 |
| Inherent Rating | Tier 1, Critical inherent risk |
| Assessment Window | 2026-06-22 to 2026-07-24 |
| Assessor Contacts | Quarrystone CISO (interview 2026-07-14), Head of Data Engineering |

### Fourth-party (subcontractor) map
| Subcontractor | Role | Location | In SOC 2? | Disclosed initially? |
|---|---|---|---|---|
| Glacierbase Data Cloud (fictional) | Cloud data warehouse (stores all Wrenfield data) | US region | Carved out (subservice organization) | Yes |
| AWS (vendor's own hosting) | Ingestion and model hosting | US region | Carved out | Yes |
| Meridian Offshore Data Services Pvt. Ltd. (fictional) | Data-engineering support: pipeline troubleshooting with production access | Pune, India | Not listed | No (found at interview 2026-07-14) |
| Hollis Helpdesk (fictional) | Support ticketing (tickets may contain PHI snippets) | US | Not listed | No |

## 3. Assessment (36 questions)
Evaluation mix: 15 Satisfactory, 12 Partially Satisfactory, 9 Unsatisfactory.

| ID | Domain | Requirement | Vendor response | Evaluation | VR |
|---|---|---|---|---|---|
| VQ-01 | Security governance | Named security leader, approved policy set reviewed annually, executive oversight | CISO in place since 2022; ISO 27001-aligned policy set reviewed 2026-01; quarterly board security update | Satisfactory | — |
| VQ-02 | Risk management | Annual risk assessment with tracked treatments | Annual risk assessment (2026-02); risk register maintained | Satisfactory | — |
| VQ-03 | Certifications and attestations | Current SOC 2 Type II (or ISO 27001) covering services used | SOC 2 Type II 2024-10-01 to 2025-09-30; bridge letter to 2026-03-31; next report expected 2026-12 | Partially Satisfactory | VR-006 |
| VQ-04 | Access control | Timely provisioning/deprovisioning and periodic reviews of staff with customer-data access | Quarterly reviews; SOC 2 notes 1 of 4 quarters missed (management response: automation added) | Partially Satisfactory | VR-006 |
| VQ-05 | Access control | Least privilege for production customer data | Role-based; 14 US staff plus the subcontractor team have production read access | Partially Satisfactory | VR-001 |
| VQ-06 | MFA | MFA for all workforce and privileged access | SSO with MFA for all staff; FIDO2 required for admins | Satisfactory | — |
| VQ-07 | MFA | Customer portal supports SSO/MFA | Portal uses local accounts with optional TOTP; SAML SSO available on Enterprise tier only | Unsatisfactory | VR-007 |
| VQ-08 | Encryption | Encryption in transit (TLS 1.2+ / SFTP) | SFTP (SSH) inbound; TLS 1.2+ API | Satisfactory | — |
| VQ-09 | Encryption | Encryption at rest with managed keys | AES-256 at rest in warehouse and object storage; cloud KMS; annual rotation | Satisfactory | — |
| VQ-10 | Encryption | Customer data segregation | Schema-per-client logical separation; shared keys | Partially Satisfactory | — |
| VQ-11 | Vulnerability management | Scanning with defined remediation SLAs | Monthly authenticated scans; Critical 30 days, High 60 | Satisfactory | — |
| VQ-12 | Penetration testing | Annual independent penetration test with retest evidence | Last external test 2025-03; 1 High finding 'remediated'; summary letter only | Unsatisfactory | VR-004 |
| VQ-13 | Secure development | SAST, code review, dependency scanning | SAST and dependency scanning in CI; 2-person review | Satisfactory | — |
| VQ-14 | Supply-chain risk | SBOM and third-party component governance | No SBOM produced; dependency scanning only | Partially Satisfactory | VR-011 |
| VQ-15 | Incident response | Documented IR plan tested annually | IR plan; tabletop 2026-02 | Satisfactory | — |
| VQ-16 | Breach notification | Notify Wrenfield of security incidents affecting its data within 24 hours of discovery | BAA: 'without unreasonable delay and no later than 30 days' | Unsatisfactory | VR-002 |
| VQ-17 | Incident response | Cooperate with customer investigations, including log provision | 'Reasonable cooperation'; no commitment to provide logs | Partially Satisfactory | VR-009 |
| VQ-18 | Business continuity | BC/DR plan with RTO/RPO appropriate to the service | RTO 72h / RPO 24h; tested 2026-01 | Satisfactory | — |
| VQ-19 | Backups | Backups with immutability and restore testing | Daily backups, 30-day retention, immutable; restore tested 2026-01 | Satisfactory | — |
| VQ-20 | Logging | Log access to customer data; retain at least 12 months | Access logs retained 90 days | Partially Satisfactory | VR-009 |
| VQ-21 | Privacy | Receive only data needed for the service (minimum necessary) | Model uses 31 of 58 fields; address, phone, email, free-text notes unused but received | Unsatisfactory | VR-003 |
| VQ-22 | Privacy | No secondary use of Wrenfield data without written permission | De-identified (Safe Harbor) pooled data used to improve cross-client models, per vendor MSA §12 | Partially Satisfactory | VR-010 |
| VQ-23 | Data location | US-only storage AND access (SHCA CSA §6.1; 2 customer BAAs) | Storage in US region. Initially answered 'US staff only'; interview revealed offshore subcontractor production access | Unsatisfactory | VR-001 |
| VQ-24 | Privacy | Documented de-identification method | HIPAA Safe Harbor procedure, annual review | Satisfactory | — |
| VQ-25 | Data retention | Defined retention for raw and derived data | Raw extracts 90 days; derived features and models retained indefinitely | Partially Satisfactory | VR-005 |
| VQ-26 | Termination and data return | Return and destroy data within 30 days of termination with certificate | 'Upon request'; no timeframe or certificate | Unsatisfactory | VR-005 |
| VQ-27 | Subcontractors | Complete list of subcontractors with access to Wrenfield data | Initially listed 2 (cloud warehouse, cloud host); 4 identified after SOC 2 review and interview | Unsatisfactory | VR-008 |
| VQ-28 | Subcontractors | BAA and security flow-down to every subcontractor | BAAs with warehouse and offshore firm; offshore agreement lacks data-location restriction | Partially Satisfactory | VR-001 |
| VQ-29 | Subcontractors | Advance notice and right to object to new subcontractors | No notice provision | Unsatisfactory | VR-008 |
| VQ-30 | Personnel security | Background checks for staff with data access | US staff screened; subcontractor staff screened by subcontractor under local law | Partially Satisfactory | VR-001 |
| VQ-31 | Personnel security | Annual security and HIPAA training | Annual training; 98% completion | Satisfactory | — |
| VQ-32 | Risk transfer | Cyber liability insurance adequate to data volume | $5M cyber policy | Satisfactory | — |
| VQ-33 | Change management | Changes approved and tested before production | SOC 2 notes 2 of 40 changes lacked approval (remediated) | Partially Satisfactory | VR-006 |
| VQ-34 | Physical security | Physical security of facilities hosting data | Inherited from cloud providers (SOC 2 carve-out) | Satisfactory | — |
| VQ-35 | Data transfer | Secure, supported transfer mechanism from Wrenfield | Vendor receives via SFTP from Wrenfield's wf-sftp-01 (Wrenfield-side, unsupported OS) | Unsatisfactory | VR-012 |
| VQ-36 | Assurance cooperation | Right to assess; annual questionnaire; evidence on request | Annual questionnaire; on-site with 30 days notice | Satisfactory | — |

## 4. Vendor findings (VR-###)
1 Critical, 2 High, 7 Moderate, 2 Low.

| ID | Title | Severity | Party | Status | Finding |
|---|---|---|---|---|---|
| VR-001 | Undisclosed offshore subcontractor with production access to Wrenfield PHI | Critical | Vendor | Interim contained (offshore access suspended 2026-07-24); contractual fix open | FIND-016 |
| VR-002 | Breach notification term of 30 days | High | Vendor | In negotiation (redline v3) | FIND-016 |
| VR-003 | Extract exceeds minimum necessary (27 of 58 fields unused) | High | Wrenfield | In progress (target 2026-10-16) | FIND-016 |
| VR-004 | Penetration test evidence stale and incomplete | Moderate | Vendor | Evidence requested (EVID-051, overdue) | FIND-016 |
| VR-005 | Data retention and return/destruction undefined | Moderate | Vendor | In negotiation | FIND-016 |
| VR-006 | SOC 2 exceptions (access reviews, change approvals) | Low | Vendor | Monitor | monitor |
| VR-007 | Wrenfield not performing SOC 2 CUEC for portal user management; no SSO | Moderate | Wrenfield | Partially remediated (review + JML done; SSO at 2027 renewal) | FIND-001 |
| VR-008 | Incomplete subcontractor disclosure; no notice of new subcontractors | Moderate | Vendor | In negotiation | FIND-016 |
| VR-009 | Access logs kept 90 days; no commitment to support investigations | Moderate | Vendor | In negotiation | FIND-016 |
| VR-010 | Secondary use of pooled de-identified data | Moderate | Both (legal review) | Legal review in progress | FIND-016 |
| VR-011 | No SBOM for vendor software | Low | Vendor | Monitor | monitor |
| VR-012 | Extract transferred from an unsupported Wrenfield host | Moderate | Wrenfield | In progress (delayed; POAM-011) | FIND-011 |
