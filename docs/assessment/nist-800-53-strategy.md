# NIST SP 800-53 Strategy: Framework Verification, Selection, and Tailoring

| Field | Value |
|---|---|
| Document ID | ASMT-STR-001 · v1.0 · 2026-06-12 (standards re-verified 2026-09-23 during the portfolio build) |
| Owner | Lead assessor |

## 1. Standards verification

The spec required the current official SP 800-53 revision to be verified from authoritative NIST sources rather than from memory. It was checked against NIST CSRC pages and NIST's official OSCAL content on **2026-09-23**.

| Item | Verified value | Authoritative source |
|---|---|---|
| **Control catalog** | **NIST SP 800-53 Revision 5, Release 5.2.0** | [SP 800-53 Rev. 5 publication page](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) |
| Original publication | September 2020 (includes updates as of Dec. 10, 2020) | same |
| Latest release | **5.2.0, issued August 27, 2025.** Adds SA-15(13), SA-24, and SI-02(07); revises SI-07(12); updates discussion sections for software update and patch integrity (responding to EO 14306) | [NIST news, Aug 27, 2025](https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls) |
| Newer release? | **None found.** NIST's 2026 news feed (through 2026-09-21) lists no SP 800-53 release after 5.2.0 | [CSRC news 2026](https://csrc.nist.gov/news/2026), [RMF news](https://csrc.nist.gov/projects/risk-management/news) |
| Control catalog source | CPRT browser (framework `SP_800_53_5_2_0`) and OSCAL JSON in `usnistgov/oscal-content`. The OSCAL catalog metadata reads *version 5.2.0, last-modified 2026-05-11* | [OSCAL content repository](https://github.com/usnistgov/oscal-content/tree/main/nist.gov/SP800-53/rev5) |
| **Assessment procedures** | **SP 800-53A Rev. 5** (Jan 2022), updated with Release 5.2.0 procedures on Aug 27, 2025 | [SP 800-53A Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) |
| **Baselines** | **SP 800-53B**. A 5.2.0 release was issued for consistency with no baseline changes. The Moderate baseline was verified from NIST's OSCAL profile *"…Revision 5.2.0 MODERATE IMPACT BASELINE"* (v5.2.0) | [OSCAL Moderate profile](https://github.com/usnistgov/oscal-content/blob/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_MODERATE-baseline_profile.json) |

**Verification results.** Baseline membership of all 61 selected controls was checked against the official OSCAL Moderate profile (integrity rule CTL-01). **Every control ID and title was then checked programmatically against NIST's official OSCAL catalog (version 5.2.0, last-modified 2026-05-11): 61 of 61 match exactly** ([catalog-verification.md](catalog-verification.md), produced by [`tools/verify_catalog.py`](../../tools/verify_catalog.py)). The catalog file is not committed; re-run the script against a fresh download to repeat the check.

### Related NIST publications used (and how)

| Publication | Version / date (verified) | Used for |
|---|---|---|
| **SP 800-37 Rev. 2**, Risk Management Framework | Final, Dec 20, 2018 | Assessment lifecycle (Assess step A-1 to A-6), POA&M role, and separating the assessor from management |
| **SP 800-30 Rev. 1**, Guide for Conducting Risk Assessments | Final, Sep 17, 2012 | Likelihood × impact structure, threat/vulnerability framing, qualitative scales |
| **SP 800-53A Rev. 5** | Jan 2022, with 5.2.0 procedures | Examine / Interview / Test methods, determination statements, "Satisfied / Other Than Satisfied" |
| **SP 800-53B** | 5.2.0 release | Moderate baseline membership |
| **SP 800-161 Rev. 1, Update 1**, C-SCRM | Final, Nov 1, 2024 | Vendor tiering, supplier assessment, and fourth-party considerations (SR-2, SR-6) |
| **SP 800-18 Rev. 2** | Final, Jun 30, 2026 | SSP remediation (FIND-017). The new revision covers system security, privacy, and C-SCRM plans together, so the SSP rewrite is scoped to it |
| **SP 800-63-4**, Digital Identity Guidelines | Final, 2025 | Authenticator strength language for IA-2(1)/(2)/(8) recommendations (phishing-resistant MFA for admins) |
| **SP 800-61 Rev. 3**, Incident Response Recommendations | Final, Apr 3, 2025 | IR-3/IR-8 recommendations framed around CSF 2.0 functions |
| **SP 800-66 Rev. 2**, Implementing the HIPAA Security Rule | Final, Feb 14, 2024 | Linking HIPAA requirements (REQ-012 to REQ-021) to controls |
| **NIST CSF 2.0** (CSWP 29) | Final, Feb 26, 2024 | Executive-level grouping of results by Function (GV/ID/PR/DE/RS/RC) |

## 2. How the frameworks relate (and are kept distinct)

| Framework | What it is | What it is **not** | Role in this project |
|---|---|---|---|
| **SP 800-53 Rev. 5** | A *catalog of controls*: what to implement | Not a process, maturity model, or assessment method | The requirements baseline: every control ID in the matrix |
| **SP 800-53A Rev. 5** | *Assessment procedures*: how to decide whether a control is effective | Not a list of controls | Test design in the [assessment worksheets](worksheets/) |
| **SP 800-53B** | *Baselines*: which controls apply at Low/Moderate/High | Not tailored to any single organization | Starting point for selection |
| **SP 800-37 Rev. 2 (RMF)** | The *lifecycle* (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) | Not a control catalog | Engagement structure. No **authorization** decision is made here (there is no Authorizing Official in this simulation) |
| **SP 800-30 Rev. 1** | *Risk assessment method* | Not a control set | The [risk methodology](../../risk/risk-methodology.md) |
| **CSF 2.0** | *Outcome taxonomy* for communicating cybersecurity posture | Not a control catalog. CSF Subcategories are outcomes, not controls | Executive dashboard grouping only. The CSF mapping is **informal and analyst-produced**. NIST's CPRT informative references are the authoritative mappings |
| **HIPAA Security Rule** | Law and regulation (45 CFR 164) | Not a NIST publication | Business requirements that controls satisfy |
| **SOC 2 (AICPA TSC)** | Attestation criteria | Not interchangeable with 800-53 | Existing evidence source (CA-2), with its limits noted |

## 3. Selection method

Selection followed the SP 800-53B tailoring process, applied transparently:

1. **Start from the Moderate baseline**, because WCP-PROD is categorized FIPS 199 Moderate.
2. **Filter by the scenario's business requirements.** Each SHCA CSA clause and HIPAA requirement (REQ-001 to REQ-024) was mapped to controls. Controls with a direct contractual or regulatory driver were selected first.
3. **Weight by threat profile** ([organization profile §10](../scope/organization-profile.md#10-threat-concerns-drives-control-selection)). Identity, supply-chain, recovery, and vulnerability controls got the most depth.
4. **Include known problem areas.** The Lakemont customer review (MFA exceptions, no privileged recertification) put AC-2, AC-6(7), and IA-2(1)/(2) in scope as mandatory.
5. **Include a few *expected-to-pass* controls deliberately** (SC-8, SC-12, SC-28, SI-3, PS-3, MP-6). They check the assessment for bias and show what effective evidence looks like.
6. **Make applicability decisions explicitly**: one *Not Applicable* (AC-18) and one *inherited* control (PE-3), each with written justification.
7. **Stop at a defensible subset.** Testing all 287 Moderate-baseline controls and enhancements would not have fit the engagement timeline, and it would have spread the testing effort across low-risk areas.

### Selection summary by family

| Family | Selected | Why these | Considered and deferred |
|---|---|---|---|
| **AC** | AC-1, AC-2, AC-2(1), AC-2(3), AC-5, AC-6, AC-6(2), AC-6(5), AC-6(7), AC-17, AC-18 | Identity is the primary attack path. CSA §3.3 requires 24-hour de-provisioning and recertification | AC-2(2), (4), (5), (13); AC-3; AC-6(1), (9), (10). Lower marginal value for this engagement; noted for the FY27 assessment |
| **AT** | AT-2, AT-3 | HIPAA 164.308(a)(5); phishing is the main initial-access vector | AT-2(2), (3), AT-4 |
| **AU** | AU-2, AU-6, AU-9, AU-11 | CSA §4.1 12-month retention; breach-scoping ability under HIPAA | AU-3, AU-12 (covered through AU-2 testing) |
| **CA** | CA-2, CA-3, CA-5, CA-7 | CSA §2.4 requires assessment and POA&M; CA-3 covers the Quarrystone data exchange | CA-6 (no authorization decision in scope), CA-9 |
| **CM** | CM-2, CM-3, CM-6, CM-8 | IaC-managed cloud with some manual drift; change approval matters to SOC 2 and the CSA | CM-7, CM-10, CM-11 |
| **CP** | CP-2, CP-4, CP-9, CP-9(1) | Healthcare ransomware threat; CSA §8.1 annual CP test | CP-6, CP-7, CP-10 (AWS multi-AZ reviewed informally) |
| **IA** | IA-2, IA-2(1), IA-2(2), IA-2(8), IA-5 | CSA §3.2 MFA; Lakemont finding | IA-4, IA-8, IA-12 |
| **IR** | IR-3, IR-4, IR-6, IR-8 | CSA §5.2 24-hour reporting; HIPAA 164.308(a)(6) | IR-2, IR-5, IR-7 |
| **MP** | MP-6 | Endpoint disposal (ITAD) as the one on-premises media risk | MP-2 to MP-5 (no removable media with PHI, enforced by MDM) |
| **PE** | PE-3 (inherited) | Shows the inheritance model | All other PE controls inherited from AWS; office out of scope |
| **PL** | PL-2 | CSA requires a current SSP | PL-4, PL-8, PL-10, PL-11 |
| **PM** | PM-9 | Risk strategy and appetite drive the register and the acceptances. *PM controls are organization-wide and not allocated to baselines in SP 800-53B* | Other PM controls |
| **PS** | PS-3, PS-4, PS-5, PS-7 | The joiner/mover/leaver lifecycle is the root of most access findings | PS-6, PS-8, PS-9 |
| **RA** | RA-2, RA-3, RA-5, RA-7 | Categorization, risk assessment, scanning, and risk response | RA-3(1), RA-5(2), (5), (11), RA-9 |
| **SA** | SA-9, SA-22 | External services (vendors) and unsupported components | SA-4, SA-8, SA-11 (AppSec program is out of scope) |
| **SC** | SC-7, SC-8, SC-12, SC-28 | PHI protection at the boundary, in transit, and at rest | SC-7(x) enhancements, SC-13 |
| **SI** | SI-2, SI-3, SI-4 | Patch timeliness, malware defense, monitoring | SI-2(2), SI-4(x), SI-7 |
| **SR** | SR-2, SR-6 | C-SCRM plan and supplier assessments (Quarrystone) | SR-3, SR-5, SR-8, SR-10, SR-11 |

### Currency note: Release 5.2.0 additions

Release 5.2.0 added **SI-02(07) Root Cause Analysis**, **SA-15(13)**, and **SA-24**. None is in the Moderate baseline profile verified above, so none is mandatory for SHCA. However, FIND-010 (vulnerability SLA misses) involves repeated patch-deployment failures for container base images. **SI-02(07) is therefore recommended as an optional tailoring addition for FY27** and listed as a POA&M-010 milestone recommendation. This does not change the current baseline.

## 4. Applicability and origination rules

| Decision | Rule applied | Examples |
|---|---|---|
| *Applicable, system-specific* | Wrenfield implements it only for WCP-PROD | SC-7, CP-9, AU-11 |
| *Applicable, hybrid* | Partly inherited from a provider, partly Wrenfield's responsibility | MP-6 (AWS media + Wrenfield laptops), SC-28 (AWS encryption service + Wrenfield's key and configuration choices) |
| *Applicable, common (inherited)* | Fully provided by a common-control provider; Wrenfield verifies the provider's attestation | PE-3 (AWS data centers) |
| *Not Applicable* | The capability does not exist within the boundary. The justification is recorded and re-examined at each assessment | AC-18: no wireless networking inside the boundary; office Wi-Fi is outside it and cannot reach production except through Okta SSO+MFA, like any internet path |

## 5. Status vocabularies (controlled values)

| Field | Allowed values | Notes |
|---|---|---|
| Implementation Status (owner-stated and assessor-validated) | Implemented · Partially Implemented · Planned · Not Implemented · Not Applicable | The matrix records **both**. The gap between owner-stated and assessor-validated status is the "challenge" record |
| Assessment Result | Satisfied · Other Than Satisfied · Not Assessed | SP 800-53A terminology. *Not Assessed* is used only for N/A controls |
| Evidence Level (highest level obtained) | Design · Implementation · Operating Effectiveness | See the [evidence quality guide](../../audit/evidence-quality-guide.md) |
| Control Origination | System-specific · Hybrid · Common (inherited) | |

## 6. Informal CSF 2.0 grouping (for executive reporting only)

| CSF 2.0 Function | Families grouped here |
|---|---|
| GOVERN (GV) | PM, PL, CA-2/CA-5/CA-7 (oversight), SR, SA-9, PS, AT |
| IDENTIFY (ID) | RA, CM-8 |
| PROTECT (PR) | AC, IA, SC, CM-2/3/6, MP, PE, SA-22, SI-2/SI-3, CP-9 |
| DETECT (DE) | AU, SI-4 |
| RESPOND (RS) | IR |
| RECOVER (RC) | CP-2, CP-4, CP-9(1) |

*Assumption: controls are grouped by primary intent. Many controls support more than one Function. This grouping is for communication only and is not an authoritative crosswalk.*
