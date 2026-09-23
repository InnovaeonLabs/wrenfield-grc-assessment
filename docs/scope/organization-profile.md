# Organization Profile: Wrenfield Health, Inc. (fictional)

| Field | Value |
|---|---|
| Document ID | GOV-ORG-001 · v1.0 · 2026-06-12 |
| Prepared by | Lead assessor, from walkthroughs with the CISO, CTO, and GRC Manager |

> Wrenfield Health is fictional. Any resemblance to a real company is coincidental. Real platforms (AWS, Okta, GitHub, Google Workspace) are named only to describe a plausible technology stack. Nothing here states or implies anything about those companies' security. Every *vendor that is assessed* in this project is fictional.

## 1. Company at a glance

| Attribute | Detail |
|---|---|
| Legal name | Wrenfield Health, Inc. |
| Industry | Healthcare technology: B2B SaaS for care coordination and remote patient monitoring (RPM) |
| Founded / HQ | 2016 · Columbus, Ohio (remote-first, about 60% remote workforce) |
| Workforce | **347 active workforce identities**: 318 employees and 29 contractors (as of 2026-06-30) |
| Funding / size | Series C (2024), about $64M ARR |
| Business model | Subscription priced per enrolled patient per month; implementation fees; annual contracts with 3-year terms typical |
| Regulatory role | **HIPAA Business Associate** to every provider and health-plan customer; signs a BAA with each |
| Attestations | SOC 2 Type II (Security, Availability, Confidentiality), period 2024-10-01 to 2025-09-30 |

## 2. Products and services

| Product | What it does | Data |
|---|---|---|
| **Wrenfield Care Platform (WCP)**, clinician web app | Care managers and nurses coordinate chronic-care programs (diabetes, CHF, COPD, hypertension): care plans, tasks, outreach queues | PHI: demographics, diagnoses, meds, care plans, notes |
| WCP patient mobile app (iOS/Android) | Patients see care plans, message care teams, get reminders | PHI; patient credentials (patient-side auth is out of scope) |
| RPM ingestion | Receives readings (BP, glucose, weight, SpO₂) from cellular hubs run by Pulsewire Connect (fictional) | PHI (device readings tied to patients) |
| Integration engine | HL7 v2 ADT feeds and FHIR R4 APIs with customer EHRs | PHI |
| Risk stratification | Ranks patients for outreach using scores from **Quarrystone Analytics** (fictional), with a rules-based fallback built into WCP | PHI (full extract sent nightly) |

## 3. Customers

| Segment | Count | Notes |
|---|---|---|
| Health systems and physician groups | 38 | Largest: Lakemont Regional Health (fictional), about 21% of ARR, whose April 2026 vendor review raised two access-control findings |
| Medicare Advantage health plans | 2 | Send claims data for risk stratification |
| **Pending: SHCA (state Medicaid agency, fictional)** | 1 | C3P contract, about 140,000 members, go-live 2027-01-11; brings **NIST SP 800-53 Rev. 5 Moderate** obligations |
| Enrolled patients (covered lives) | about **410,000** | Rises to about 550,000 after SHCA go-live |

## 4. Sensitive information processed

| Information | Examples | Sensitivity | Governing obligations |
|---|---|---|---|
| Protected Health Information (PHI) | Name, DOB, address, MRN, member ID, diagnoses (ICD-10), medications, vitals, care notes | **High** | HIPAA Privacy and Security Rules; BAAs; SHCA CSA |
| Medicaid member data (post go-live) | As PHI, plus Medicaid ID and eligibility | **High** | SHCA CSA: US-only data access, 24-hour incident reporting, 12-month log retention |
| Workforce PII | SSN, compensation, background-check results (PeopleHub) | High | State privacy and breach laws |
| Financial data | Vendor bank details, payments (Ledgerline) | Moderate | SOX-like internal controls (not a public company; board policy) |
| Source code and secrets | WCP code, IaC, CI/CD secrets | High (integrity) | Internal secure-development standard |
| Security telemetry | CloudTrail, SIEM, EDR data | Moderate | Retention required by CSA §4.1 |

## 5. Technology environment

| Layer | Implementation |
|---|---|
| Cloud | AWS Organizations: `wcp-prod` (us-east-2), `wcp-dr` (us-west-2, backup copies), `log-archive`, `security-tooling`, `wcp-staging`, `wcp-dev`. Service Control Policies enforce region restriction and org-wide S3 Block Public Access |
| Compute | Amazon EKS (18 microservices), managed node groups from a hardened AMI; one legacy Windows EC2 host (`wf-sftp-01`); one self-managed PostgreSQL 11 EC2 host (`legacy-reports`) |
| Data | Aurora PostgreSQL `wcp-core-db` (PHI, KMS-encrypted), S3 (documents, device payloads, extracts), ElastiCache |
| Identity | Okta Workforce Identity (SSO, MFA incl. FastPass/WebAuthn), AWS IAM Identity Center federated from Okta; **some legacy AWS IAM users remain** |
| Source and CI/CD | GitHub Enterprise Cloud, GitHub Actions deploying through OIDC-federated AWS roles (no static deploy keys) |
| Endpoints | About 362 managed macOS/Windows laptops (MDM, full-disk encryption, EDR) |
| Security tooling | Cloud SIEM (SaaS), EDR, authenticated vulnerability scanning (agent- and network-based), AWS Security Hub (CIS AWS Foundations benchmark), GuardDuty; MDR service from Ironpeak MDR (fictional) |
| Collaboration | Google Workspace (under a BAA), Slack (no PHI by policy) |

## 6. Critical systems and high-value assets

| Asset | Why it matters | Business impact if compromised |
|---|---|---|
| `wcp-core-db` | Single largest PHI store | HHS breach notification, customer and contract loss, regulatory penalties |
| AWS `wcp-prod` administrative plane | Full control of data and infrastructure | PHI exfiltration or destructive (ransomware-style) outage |
| Okta tenant | Key to every system | Identity compromise cascades to all apps |
| GitHub org and Actions | Code and deployment integrity | Supply-chain compromise of a clinical platform |
| Nightly Quarrystone extract (`wf-sftp-01`) | Full PHI copy leaves the boundary daily | Third-party breach exposure; SHCA US-only violation |
| Backups (`wcp-dr`) | Recovery from ransomware | Prolonged outage of clinical workflows |

## 7. Major vendors (summary)

Full inventory and tiering: [vendor-assessment.xlsx](../../vendor-risk/vendor-assessment.xlsx) (sheet *Vendor Inventory*).

| Vendor | Service | Tier |
|---|---|---|
| AWS | IaaS/PaaS hosting (under a BAA) | 1 |
| Okta | Workforce identity | 1 |
| GitHub | Source code, CI/CD | 1 |
| Google Workspace | Email and documents (under a BAA) | 1 |
| **Quarrystone Analytics, LLC** *(fictional)* | Population-health analytics; nightly PHI extract | **1: deep assessment** |
| Pulsewire Connect *(fictional)* | RPM cellular hubs and device-data API | 1 |
| Ironpeak MDR *(fictional)* | 24×7 managed detection and response (read access to security telemetry) | 1 |
| Brightdesk *(fictional)* | Customer-support ticketing (limited PHI) | 2 |
| Clearpath Messaging *(fictional)* | Patient SMS/voice reminders | 2 |
| PeopleHub *(fictional)* | HRIS | 2 |
| Ledgerline *(fictional)* | ERP / finance | 2 |
| Northgate Talent Partners *(fictional)* | Contract engineering staff | 2 |

## 8. Regulatory and contractual obligations

Tracked as business requirements `REQ-###` in [business-requirements.md](business-requirements.md) and linked to controls in the [traceability matrix](../assessment/traceability-matrix.md).

- **HIPAA Security Rule** (45 CFR Part 164, Subpart C) as a business associate, plus breach notification duties to covered entities (45 CFR 164.410).
- **SHCA Contract Security Addendum:** SP 800-53 Rev. 5 Moderate alignment, SAR and POA&M, MFA, 24-hour de-provisioning, 12-month log retention, US-only data access, 24-hour incident reporting, vulnerability SLAs, subcontractor flow-down.
- **Customer BAAs and MSAs:** breach notice within 5 business days (typical term), annual security questionnaire, right to audit.
- **SOC 2 commitments** made to customers (logical access, change management, availability).

## 9. Security organization

| Role | Name | Reports to |
|---|---|---|
| CEO | Elena Marsh | Board |
| CFO | Raymond Okafor | CEO |
| CTO (system owner, WCP-PROD) | Samir Haddad | CEO |
| CISO | Alicia Moreno | CTO (dotted line to Audit & Risk Committee) |
| Security Compliance Manager (GRC) | Priya Raman | CISO |
| IAM Engineer | Nadia Rahman | CISO |
| Security Engineer (detection and response) | Owen Castillo | CISO |
| VP Engineering | Grace Lindqvist | CTO |
| Director, Platform Engineering (SRE) | Tomasz Wierzbicki | CTO |
| IT Manager | Kevin Brandt | CTO |
| HIPAA Privacy Officer | Rachel Stein | General Counsel (Theo Anand) |
| VP Clinical Analytics (Quarrystone business owner) | Dr. Miriam Castell | CEO |
| Director of People (HR) | Denise Yamamoto | CEO |
| Controller | Laura Brenneman | CFO |
| Vendor Management Lead | Beth Kowalski | CFO |

The security team has 4 FTE plus the MDR service. That is lean for 347 workforce identities and a PHI platform, and it explains several findings about review cadence (AU-6, AC-6(7)).

## 10. Threat concerns (drives control selection)

| Threat | Relevance to Wrenfield | Controls emphasized |
|---|---|---|
| Identity-centric intrusion (phishing, MFA fatigue, help-desk social engineering, session-token theft) | Most common intrusion path into SaaS/cloud organizations; Okta and AWS admin are keys to everything | AC-2, AC-6, IA-2(1)/(2)/(8), IA-5, AU-6 |
| Ransomware and destructive attacks on healthcare | Healthcare is heavily targeted; clinical workflows depend on availability | CP-2/4/9, IR-3/4/8, SI-4 |
| Third-party / supply-chain compromise | Full PHI extract leaves the boundary daily; CI/CD dependencies | SA-9, SR-2, SR-6, CA-3 |
| Exploitation of unpatched or unsupported software | Legacy Windows 2012 R2 host faces vendors; container base images | RA-5, SI-2, SA-22, SC-7 |
| Insider misuse and access creep | Small teams, fast growth, contractor churn | AC-5, AC-6(7), PS-4/5/7 |
| Cloud misconfiguration | Large IaC estate; manual console changes still happen | CM-2, CM-6, SC-7, SC-28 |
