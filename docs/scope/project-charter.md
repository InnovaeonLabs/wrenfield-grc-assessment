# Project Charter: WCP-PROD Security Control Assessment (Simulated)

| Field | Value |
|---|---|
| Document ID | GOV-CHR-001 |
| Version | 1.0 (approved) |
| Charter date | 2026-06-05 |
| Engagement sponsor | Alicia Moreno, Chief Information Security Officer (CISO) |
| Executive sponsor | Samir Haddad, Chief Technology Officer (CTO) |
| Engagement coordinator | Priya Raman, Security Compliance Manager |
| Lead assessor | Markese Raley, simulated independent assessor (portfolio author) |
| Classification | Internal (fictional organization; synthetic data) |

> **Portfolio integrity notice:** Wrenfield Health, Inc. and every person, system, vendor, contract, and dataset in this repository are **fictional**. This charter describes a **simulated** assessment built as an independent portfolio exercise. It is not an official assessment, audit, authorization, certification, or regulatory determination. See [DISCLAIMER.md](../../DISCLAIMER.md).

---

## 1. Business problem

Wrenfield Health is a healthcare-technology SaaS company. It has been selected as the preferred vendor for the **State Health Coverage Authority (SHCA) Chronic Care Coordination Program (C3P)**. SHCA is a fictional state Medicaid agency. The contract is worth $23.4M over five years and would add about 140,000 Medicaid members to the platform, with production go-live scheduled for **2027-01-11**.

The SHCA **Contract Security Addendum (CSA)** requires Wrenfield to:

1. maintain security controls aligned to the **NIST SP 800-53 Rev. 5 Moderate baseline** for systems that store, process, or transmit agency data (CSA §2.1);
2. deliver a **Security Assessment Report (SAR)** and a **Plan of Action & Milestones (POA&M)** at least 90 days before go-live, then quarterly (CSA §2.4). The first submission is due **2026-10-13**.

Two other pressures make the assessment urgent:

- **Customer finding.** In April 2026, the annual vendor security review by Wrenfield's largest customer, Lakemont Regional Health (fictional, about 21% of ARR), found *"no evidence of privileged-access recertification"* and *"undocumented MFA exceptions."* Lakemont asked for a remediation plan by Q4 2026.
- **Board request.** The Board's Audit & Risk Committee asked for an independent-style view of control effectiveness before the company takes on its first public-sector contract.

Wrenfield holds a SOC 2 Type II report (period 2024-10-01 to 2025-09-30). However, SOC 2 is not designed to demonstrate NIST SP 800-53 Moderate alignment. It has no POA&M construct, no system security plan requirement, and no contractual log-retention or US-only data-access tests. This engagement closes that gap.

## 2. Objectives

| # | Objective | Success measure |
|---|---|---|
| O1 | Determine whether selected SP 800-53 Rev. 5 controls are implemented correctly, operating as intended, and producing the desired outcome for WCP-PROD | Every in-scope control has an evidence-backed determination (Satisfied / Other Than Satisfied) traceable to test results |
| O2 | Perform a complete access certification of privileged and PHI-bearing access | 100% of privileged entitlements and PHI data-store entitlements on 9 in-scope systems reviewed; every exception dispositioned |
| O3 | Assess third-party risk for the most critical PHI-processing vendor | Tier-1 vendor assessment with risk decision, contract conditions, and monitoring plan |
| O4 | Record cybersecurity risks in an enterprise-style register | 12–20 risks with a documented, repeatable scoring method, owners, and treatments |
| O5 | Convert every material deficiency into a tracked POA&M item | 100% of findings map to a POA&M item or a documented risk acceptance |
| O6 | Validate remediation before closure | No POA&M item closed without assessor-validated closure evidence |
| O7 | Report to management | SAR and executive dashboard delivered by 2026-09-30 (13 days before the CSA deadline) |

## 3. Scope summary

The formal statement is in [scope-statement.md](scope-statement.md).

- **System:** Wrenfield Care Platform, production (WCP-PROD), FIPS 199 **Moderate**.
- **Controls:** 61 SP 800-53 Rev. 5 controls and enhancements across 18 families, tailored from the Moderate baseline (see [nist-800-53-strategy.md](../assessment/nist-800-53-strategy.md)).
- **Evidence period:** 2026-01-01 to 2026-06-30 for operating effectiveness; point-in-time configuration as of 2026-06-30.
- **Access review snapshot:** 2026-06-30.

## 4. Approach

The assessment follows the RMF **Assess** step (SP 800-37 Rev. 2, Task A-1 to A-6) and uses **SP 800-53A Rev. 5** assessment methods: Examine, Interview, and Test. Risk is scored with a 5×5 method adapted from **SP 800-30 Rev. 1**. Vendor risk follows **SP 800-161 Rev. 1 (Update 1)** supply-chain concepts. Details are in [assessment-plan.md](../assessment/assessment-plan.md).

## 5. Timeline (simulated engagement calendar)

| Milestone | Date | Status |
|---|---|---|
| Charter approved | 2026-06-05 | Done |
| Evidence request list (PBC) issued | 2026-06-10 | Done |
| Kickoff and control-owner walkthroughs | 2026-06-15 to 06-19 | Done |
| Fieldwork: evidence review and testing | 2026-06-15 to 07-24 | Done |
| Access review snapshot and certification | 2026-06-30 to 07-17 | Done |
| Vendor assessment (Quarrystone Analytics) | 2026-06-22 to 07-24 | Done |
| Draft findings issued | 2026-07-31 | Done |
| Management responses and POA&M baseline | 2026-08-07 | Done |
| Remediation validation window | 2026-08-15 to 09-16 | Done |
| **Status date for all reporting** | **2026-09-18** | Current |
| SAR and dashboard delivered to CISO/CTO | 2026-09-30 | Planned |
| SAR and POA&M submitted to SHCA | by 2026-10-13 | Planned |

## 6. Roles and responsibilities (RACI)

| Activity | Assessor | CISO | GRC Mgr | Control owners | CTO | Risk owners (execs) |
|---|---|---|---|---|---|---|
| Scope and control selection | R | A | C | I | C | I |
| Evidence requests and collection | R | I | A | R | I | I |
| Control testing and determinations | A/R | I | C | C | I | I |
| Access certification decisions | C | A | C | R (reviewers) | I | I |
| Risk scoring | R | A | C | C | C | C |
| Risk acceptance | C | C | I | I | C | A (per authority matrix) |
| POA&M ownership and remediation | C | A | R | R | I | C |
| Remediation validation and closure | A/R | I | C | C | I | I |
| Executive reporting | R | A | C | I | C | I |

R = Responsible, A = Accountable, C = Consulted, I = Informed. The assessor is accountable for *determinations*. Management is accountable for *remediation* and *risk acceptance*. Keeping these separate preserves assessor independence (SP 800-37 Rev. 2, Task A-1).

## 7. Constraints and assumptions

- **Independence.** The assessor does not design or operate controls. Where the assessor recommends a fix, the control owner decides how to implement it.
- **No production changes by the assessor.** All testing is read-only: exports, configuration reads, and sampling.
- **Sampling.** Sample sizes follow the frequency-based table in the assessment plan. Populations of 25 or fewer are tested in full.
- **Evidence reliability.** System-generated reports (information produced by the entity, or IPE) are checked for completeness and accuracy before use. See [evidence-quality-guide.md](../../audit/evidence-quality-guide.md).
- **Inherited controls.** Physical and environmental controls for AWS data centers are inherited. The assessor reviews the customer-responsibility split but does not test the provider's controls.
- **Synthetic data.** All exports, names, and identifiers in this repository are synthetic. No real PHI, credentials, or proprietary data are present.

## 8. Risks to the engagement

| Engagement risk | Mitigation |
|---|---|
| Control owners unavailable during fieldwork (summer PTO) | Walkthroughs front-loaded in week 1; delegate owner named per control |
| Evidence arrives late or in the wrong form (screenshots without dates) | PBC list specifies format, period, and population for every item; the tracker flags *Insufficient* early |
| Scope creep into staging/dev | Scope statement defines the boundary; changes need sponsor approval |
| Findings disputed by owners | Every determination cites evidence IDs; disputes are logged in the findings register with the assessor's position |
| Vendor slow to respond | Vendor questionnaire issued week 2; escalation through the business owner (VP Clinical Analytics) |

## 9. Deliverables

The six primary artifacts, the full set of 16 professional artifacts, and their GitHub locations are listed in the [README](../../README.md#deliverables). Every artifact uses the shared ID scheme in [id-scheme.md](../id-scheme.md).

## 10. Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Executive sponsor | Samir Haddad, CTO | Approved | 2026-06-05 |
| Engagement sponsor | Alicia Moreno, CISO | Approved | 2026-06-05 |
| Lead assessor | Markese Raley | Accepted engagement | 2026-06-05 |

*(Fictional approvals recorded for realism.)*
