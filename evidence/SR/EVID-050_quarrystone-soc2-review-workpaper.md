# EVID-050: SOC 2 Report Review Workpaper: Quarrystone Analytics (fictional)

| Field | Value |
|---|---|
| Report | SOC 2 Type II, Security and Confidentiality criteria, period 2024-10-01 to 2025-09-30 (fictional report) |
| Bridge letter | Covers 2025-10-01 to 2026-03-31 (management assertion, not auditor-opined) |
| Reviewed by | Lead assessor, 2026-07-01 |
| Used for | SR-6, SA-9, vendor questionnaire items VQ-03/04/06/09/19/33/34 |

## 1. Scope check: does the report cover what Wrenfield uses?
| Question | Answer | Impact |
|---|---|---|
| Services in scope | Analytics platform, ingestion, customer portal | ✅ Covers Wrenfield's use |
| Locations in scope | US offices; **offshore subcontractor not mentioned** | ⚠️ Gap: led to the interview question that surfaced VR-001 |
| Period | Ends 2025-09-30; the bridge letter extends to 2026-03-31 | ⚠️ About 6 months (Apr–Sep 2026) with no assurance; next report expected 2026-12 |

## 2. Opinion
Unqualified. The auditor found controls suitably designed and operating effectively, **except for the deviations noted in section 4**. Those deviations did not rise to a qualification.

## 3. Subservice organizations (carve-out method)
| Subservice org | Service | Wrenfield action |
|---|---|---|
| Glacierbase Data Cloud (fictional) | Data warehouse | Relies on that provider's own attestation. Added to the fourth-party map |
| AWS (vendor's hosting) | Infrastructure | Same |

Carve-out means the vendor's auditor **did not test** these providers' controls. Wrenfield's assurance chain has a gap unless their reports are reviewed as well.

## 4. Exceptions noted
| Criterion | Exception | Vendor management response | Assessor view |
|---|---|---|---|
| CC6.2/CC6.3 | Quarterly user access review not performed for 1 of 4 quarters | Automated reminders and escalation added 2025-10 | Adequate; confirm in next report (VR-006) |
| CC8.1 | 2 of 40 sampled changes lacked documented approval | Branch protection now enforced | Adequate; confirm in next report (VR-006) |

## 5. Complementary user-entity controls (CUECs), Wrenfield's responsibilities
| CUEC listed in report | Wrenfield performing it? | Result |
|---|---|---|
| User entities manage and periodically review their users' portal access | **No.** Never performed; 1 former employee still active | **VR-007 / AR-EX-04 / FIND-001** |
| User entities secure credentials used for data transfer (SFTP keys, API keys) | Partially. SFTP key 811 days old, no owner | AR-EX-18 / FIND-005 |
| User entities send only data necessary for the service | **No.** 27 of 58 fields unused | **VR-003** |
| User entities notify the vendor of terminated users within 5 days | No process | Covered by POAM-001 JML checklist |

**Key point:** a SOC 2 report is not a certificate. Its value depends on reading the scope, the exceptions, the carve-outs, and the CUECs. Here, the CUEC section produced three Wrenfield-side findings.

## 6. Conclusion
The report supports reliance on the vendor's core security controls (access, encryption, change, backup) for the period covered. It **does not** address data location or subcontractor access, and the assurance gap after 2026-03-31 must be closed by the next report. Rating inputs go to VQ-03 (Partially Satisfactory) and the vendor decision. *(Synthetic workpaper.)*
