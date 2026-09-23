# Scope Statement: WCP-PROD Security Control Assessment

| Field | Value |
|---|---|
| Document ID | GOV-SCP-001 |
| Version | 1.1 (v1.0 2026-06-05; v1.1 2026-06-19 added the Quarrystone portal after walkthroughs) |
| Owner | Priya Raman, Security Compliance Manager |
| Approved by | Alicia Moreno, CISO |

## 1. System under assessment

| Attribute | Value |
|---|---|
| System name | Wrenfield Care Platform, production |
| System identifier | **WCP-PROD** |
| System type | Multi-tenant SaaS (clinician web app, patient mobile app back end, device-data ingestion, integration engine) |
| Security categorization (FIPS 199) | **Moderate**, as {Confidentiality: Moderate, Integrity: Moderate, Availability: Moderate}. Rationale in [system-profile.md](system-profile.md#4-security-categorization-fips-199) |
| Control baseline | SP 800-53B Moderate, tailored (61 controls selected by risk; see [strategy](../assessment/nist-800-53-strategy.md)) |
| System owner | Samir Haddad, CTO |
| Information owner (PHI) | Rachel Stein, HIPAA Privacy Officer |

## 2. Assessment boundary

**In scope**

| # | Component | Why it is in scope |
|---|---|---|
| SYS-01 | AWS accounts `wcp-prod` (us-east-2), `wcp-dr` (us-west-2), `log-archive`, `security-tooling` | Stores, processes, and logs PHI; DR copies |
| SYS-02 | Okta Workforce Identity (tenant `wrenfield`) | Common-control provider for identification, authentication, and SSO to every in-scope system |
| SYS-03 | GitHub Enterprise Cloud (org `wrenfield-health`), including GitHub Actions | Source code and CI/CD pipeline that deploys to WCP-PROD |
| SYS-04 | `wcp-core-db`: Aurora PostgreSQL cluster (the "customer database") | Primary PHI data store (about 410,000 patients) |
| SYS-05 | `wf-sftp-01`: legacy SFTP/reporting host (in the `legacy-integration` subnet of `wcp-prod`) | Sends PHI extracts to Quarrystone and 4 customers |
| SYS-06 | PeopleHub HRIS (SaaS, fictional) | Authoritative source for joiner/mover/leaver events that drive access |
| SYS-07 | Ledgerline ERP (SaaS, fictional) | Finance system; tests segregation of duties for vendor payments |
| SYS-08 | Security tooling: SIEM, EDR console, vulnerability scanner, AWS Security Hub (CSPM) | Monitoring controls; privileged access to security data |
| SYS-09 | Quarrystone Analytics customer portal (external, fictional vendor) | Wrenfield-managed user accounts on a vendor platform that holds PHI (added in v1.1) |
| SYS-10 | Corporate endpoints used for administrative access (macOS/Windows, MDM-managed) | Admin access path to production |

**Out of scope** (and why)

| Excluded | Rationale |
|---|---|
| `wcp-staging` and `wcp-dev` AWS accounts | No production PHI (synthetic data only, per the data-handling standard). Exception: the CI/CD path from GitHub to prod *is* in scope |
| Application security testing of WCP code (DAST/SAST/pentest) | Covered by the annual third-party penetration test (evidence reviewed under CA-2, not re-performed) |
| Corporate office network and Wi-Fi | Outside the authorization boundary; no production access from office networks without SSO+MFA (AC-18 determined *Not Applicable*) |
| AWS data-center physical controls | Inherited from the cloud provider (PE-3 marked *Implemented – inherited*) |
| Marketing and sales SaaS | No PHI or agency data |
| Vendors other than Quarrystone (deep assessment) | The vendor *program* (inventory, tiering, monitoring) is tested under SA-9/SR-6. Only the highest-risk vendor gets a deep assessment |

## 3. Time periods

| Period | Dates | Used for |
|---|---|---|
| Operating-effectiveness period | 2026-01-01 to 2026-06-30 | Samples of recurring controls (terminations, changes, log reviews, incidents) |
| Point-in-time configuration | as of 2026-06-30 | Settings: MFA policies, retention, security groups, encryption |
| Access review snapshot | 2026-06-30 | Entitlement exports |
| Fieldwork | 2026-06-15 to 2026-07-24 | Testing |
| Remediation validation | 2026-08-15 to 2026-09-16 | Closure testing of POA&M items |
| Status date | **2026-09-18** | All metrics, aging, and overdue calculations |

## 4. Controls in scope

**61 controls and enhancements across 18 families.** The list, applicability decisions, and selection rationale are in [nist-800-53-strategy.md](../assessment/nist-800-53-strategy.md) and the [control matrix](../../controls/nist-800-53-control-matrix.csv).

| Family | Count | Family | Count |
|---|---|---|---|
| AC Access Control | 11 | PE Physical and Environmental Protection | 1 |
| AT Awareness and Training | 2 | PL Planning | 1 |
| AU Audit and Accountability | 4 | PM Program Management | 1 |
| CA Assessment, Authorization, and Monitoring | 4 | PS Personnel Security | 4 |
| CM Configuration Management | 4 | RA Risk Assessment | 4 |
| CP Contingency Planning | 4 | SA System and Services Acquisition | 2 |
| IA Identification and Authentication | 5 | SC System and Communications Protection | 4 |
| IR Incident Response | 4 | SI System and Information Integrity | 3 |
| MP Media Protection | 1 | SR Supply Chain Risk Management | 2 |

*MA (Maintenance) was considered and excluded: Wrenfield does not maintain hardware inside the boundary, and remote administration is assessed under AC-17.*

## 5. Access review scope

- **Systems:** Okta, AWS (IAM Identity Center and IAM), GitHub, `wcp-core-db`, PeopleHub, Ledgerline, security tooling, plus the Quarrystone portal.
- **Population rule:** *all* privileged entitlements, *all* entitlements to PHI data stores, and all service/shared accounts on those systems. Standard (non-privileged, non-PHI) entitlements are covered by the Okta manager certification and are not re-reviewed here.
- **Identity sources:** PeopleHub HR roster (employees and contractors), Okta user export, per-system entitlement exports, and the service-account register.

## 6. Vendor assessment scope

- **Program level:** vendor inventory, tiering, and monitoring for all Tier 1–2 vendors (SA-9, SR-6).
- **Deep assessment:** **Quarrystone Analytics, LLC** (fictional). It is a population-health analytics vendor that receives a full PHI extract every night. Chosen as the highest inherent-risk vendor (see [vendor-summary.md](../../vendor-risk/vendor-summary.md)).

## 7. Assumptions and constraints

1. Evidence is provided by Wrenfield (IPE) and validated for completeness and accuracy before reliance.
2. Assessor access is read-only (AWS `SecurityAudit` role, Okta read-only admin, GitHub org auditor).
3. The assessment is point-in-time plus a 6-month look-back. It cannot show that controls will keep operating in the future. Continuous monitoring (CA-7) covers that.
4. A determination of *Satisfied* means the tested determination statements were met based on the evidence obtained. It is not a guarantee that no weakness exists.

## 8. Scope change log

| Date | Change | Approved by |
|---|---|---|
| 2026-06-19 | Added SYS-09 (Quarrystone portal). Walkthroughs showed Wrenfield manages local portal accounts, a complementary user-entity control (CUEC) listed in the vendor's SOC 2 report | CISO |
| 2026-07-02 | Added the security-group review for `wf-sftp-01` after CSPM showed an internet-exposed RDP rule (already inside the SYS-05 boundary; recorded for transparency) | GRC Manager |
