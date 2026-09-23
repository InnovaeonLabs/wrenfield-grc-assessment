# Access-Control Review: Findings

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

Full certification: [access-review.csv](access-review.csv) · [access-review.xlsx](access-review.xlsx) · raw exports: [source-exports/](source-exports/) · engine: [tools/review_engine.py](../tools/review_engine.py) · process: [README.md](README.md)

## Results at a glance
| Measure | Value |
|---|---|
| Snapshot date | 2026-06-30 |
| Entitlements reviewed | **106** (37 privileged · 31 PHI-bearing) |
| Accounts reviewed | 53 across 10 system labels |
| Rows flagged by engine | 29 |
| **Confirmed exceptions** | **20** across 28 rows (26% of rows) |
| False positives dispositioned | 1 (IR-Responder role inactive by design) |
| Exceptions closed · risk-accepted · open | 18 · 1 · 1 |
| GitHub org owners (max 3) | 5 at snapshot |

Engine flags are **not** findings. A reviewer confirms or dismisses each one. Exceptions are then **rolled up by root cause** into control-level findings, because auditors report control failures, not individual accounts.

## Exceptions rolled up to findings
| Finding | Title | Exceptions |
|---|---|---|
| FIND-001 | Terminated workforce retained active access | 4 |
| FIND-002 | MFA not enforced for all workforce and privileged accounts | 1 |
| FIND-003 | Excessive privileged access and administration from daily-use accounts | 6 |
| FIND-004 | Access recertification incomplete and ineffective (access creep) | 3 |
| FIND-005 | Service and shared accounts lack ownership, credential rotation, and individual accountability | 3 |
| FIND-006 | Contractor access not bound to engagement term and scope | 2 |
| FIND-007 | Segregation-of-duties conflict in vendor payment process | 1 |

## Engine flags
| Flag | Meaning | Rows |
|---|---|---|
| F-BASELINE | Privileged or PHI access not in role baseline | 8 |
| F-CONTRACT | Contract end date passed but worker active | 2 |
| F-DAILYADMIN | Privileged role on daily-use account (separate admin account required) | 6 |
| F-DUP | Possible duplicate identity (same person, multiple accounts) | 2 |
| F-INACTIVE | No use in > 90 days | 6 |
| F-MFA | MFA not enforced (not enrolled / exemption group) | 3 |
| F-SHARED | Shared account (no individual accountability) | 1 |
| F-SOD | Segregation-of-duties conflict | 2 |
| F-SVC-OWNER | Service account has no documented owner | 2 |
| F-SVC-ROTATION | Credential older than 365 days | 3 |
| F-TERM | Worker terminated in HR but access active | 8 |
| F-TRANSFER | Access from prior role retained after transfer | 1 |

## Exception index
| Exception | Accounts | Decision | Finding | Status |
|---|---|---|---|---|
| AR-EX-01 | `dwhitlock` @ Ledgerline, `dwhitlock` @ Okta | Revoke | FIND-001 | Completed |
| AR-EX-02 | `vosei` @ GitHub, `vosei` @ Okta | Revoke | FIND-001 | Completed |
| AR-EX-03 | `mfeld-admin` @ AWS wcp-prod | Revoke | FIND-001 | Completed |
| AR-EX-04 | `pbrennan` @ Quarrystone portal | Revoke | FIND-001 | Completed |
| AR-EX-05 | `dokonkwo` @ AWS wcp-prod | Modify | FIND-003 | Completed |
| AR-EX-06 | `bnguyen` @ AWS wcp-prod | Modify | FIND-003 | Completed |
| AR-EX-07 | `bnguyen` @ wcp-core-db | Revoke | FIND-003 | Completed |
| AR-EX-08 | `glindqvist` @ GitHub, `hlarsen` @ GitHub | Modify | FIND-003 | Completed |
| AR-EX-09 | `kbrandt` @ Okta | Modify | FIND-003 | Completed |
| AR-EX-10 | `lbaptiste` @ AWS wcp-prod, `twierzbicki` @ AWS wcp-prod | Modify | FIND-003 | In Progress |
| AR-EX-11 | `kbrandt` @ Okta, `mcole` @ Okta, `svc-vulnscan` @ Okta | Modify | FIND-002 | Completed |
| AR-EX-12 | `rgupta2` @ GitHub, `rgupta2` @ Okta | Revoke | FIND-004 | Completed |
| AR-EX-13 | `cfernandes` @ wcp-core-db | Revoke | FIND-004 | Completed |
| AR-EX-14 | `sparks` @ AWS wcp-prod | Revoke | FIND-004 | Completed |
| AR-EX-15 | `awu` @ Okta | Retain with exception | FIND-006 | Completed |
| AR-EX-16 | `awu` @ wcp-core-db | Revoke | FIND-006 | Completed |
| AR-EX-17 | `jmercer` @ Ledgerline | Retain with exception | FIND-007 | Risk Accepted |
| AR-EX-18 | `svc-quarrystone-sftp` @ wf-sftp-01 | Modify | FIND-005 | Completed |
| AR-EX-19 | `svc-reporting-etl` @ AWS wcp-prod | Modify | FIND-005 | Completed |
| AR-EX-20 | `ironpeak-soc` @ Security tooling (EDR) | Modify | FIND-005 | Completed |

## Exception detail: FINDING → RISK → CONTROL → REMEDIATION → OWNER → DUE → EVIDENCE OF CLOSURE
### AR-EX-01: Terminated employee (2026-05-22) still enabled in Okta
| Chain | Detail |
|---|---|
| **Accounts / systems** | `dwhitlock` @ Ledgerline, `dwhitlock` @ Okta |
| **Engine flags** | F-TERM |
| **Finding** | FIND-001: Terminated workforce retained active access (High) |
| **Risk** | RISK-002 (Unauthorized access by former employees or contractors) |
| **Affected control** | AC-2(3); PS-4 |
| **Remediation** | Revoke: Disable Okta account; confirm no sign-in after termination |
| **Owner** | Nadia Rahman |
| **Due date** | 2026-07-07 |
| **Status / completed** | Completed / 2026-07-06 |
| **Evidence of closure** | EVID-061 |
| **Reviewer comment** | No Ledgerline transactions after 2026-05-21 (Controller verified) No sign-in after 2026-05-21 per Okta System Log |

### AR-EX-02: Terminated contractor (engagement ended 2026-06-05) still enabled; Okta sign-in on 2026-06-09 after end date
| Chain | Detail |
|---|---|
| **Accounts / systems** | `vosei` @ GitHub, `vosei` @ Okta |
| **Engine flags** | F-TERM |
| **Finding** | FIND-001: Terminated workforce retained active access (High) |
| **Risk** | RISK-002 (Unauthorized access by former employees or contractors) |
| **Affected control** | AC-2(3); PS-7; IR-4 |
| **Remediation** | Revoke: Disable Okta; revoke sessions; open incident to investigate post-termination sign-in |
| **Owner** | Nadia Rahman |
| **Due date** | 2026-07-06 |
| **Status / completed** | Completed / 2026-07-06 |
| **Evidence of closure** | EVID-061; EVID-078 |
| **Reviewer comment** | Escalated to CISO same day as INC-2026-0117 (see incident record) Last GitHub activity 2026-06-04 (before end date) |

### AR-EX-03: Local AWS IAM user of employee terminated 2026-03-27 still active (console password + access key); outside Okta de-provisioning
| Chain | Detail |
|---|---|
| **Accounts / systems** | `mfeld-admin` @ AWS wcp-prod |
| **Engine flags** | F-DAILYADMIN; F-INACTIVE; F-TERM |
| **Finding** | FIND-001: Terminated workforce retained active access (High) |
| **Risk** | RISK-002 (Unauthorized access by former employees or contractors) |
| **Affected control** | AC-2(3); AC-2 |
| **Remediation** | Revoke: Delete IAM user and keys; review CloudTrail for activity after 2026-03-27 |
| **Owner** | Tomasz Wierzbicki |
| **Due date** | 2026-07-07 |
| **Status / completed** | Completed / 2026-07-06 |
| **Evidence of closure** | EVID-064 |
| **Reviewer comment** | CloudTrail shows no use after 2026-03-20; root cause is local accounts outside SSO |

### AR-EX-04: Former employee (terminated 2025-11-14) retains Quarrystone portal account (local auth; not federated to Okta)
| Chain | Detail |
|---|---|
| **Accounts / systems** | `pbrennan` @ Quarrystone portal |
| **Engine flags** | F-INACTIVE; F-TERM |
| **Finding** | FIND-001: Terminated workforce retained active access (High) |
| **Risk** | RISK-002 (Unauthorized access by former employees or contractors) |
| **Affected control** | AC-2(3); SA-9 |
| **Remediation** | Revoke: Deactivate portal account; add portal to JML checklist; request SAML SSO from vendor |
| **Owner** | Liam Porter |
| **Due date** | 2026-07-10 |
| **Status / completed** | Completed / 2026-07-09 |
| **Evidence of closure** | EVID-061 |
| **Reviewer comment** | This is the vendor SOC 2 CUEC Wrenfield was not performing (VR-007) |

### AR-EX-05: AdministratorAccess in production not required for Software Engineer role; 2024 migration grant never removed
| Chain | Detail |
|---|---|
| **Accounts / systems** | `dokonkwo` @ AWS wcp-prod |
| **Engine flags** | F-BASELINE; F-DAILYADMIN |
| **Finding** | FIND-003: Excessive privileged access and administration from daily-use accounts (High) |
| **Risk** | RISK-001 (Privileged cloud or identity admin account misused or compromised) |
| **Affected control** | AC-6(5); AC-6 |
| **Remediation** | Modify: Replace with Developer-ReadOnly-Prod; use approval-gated elevation for incidents |
| **Owner** | Tomasz Wierzbicki |
| **Due date** | 2026-08-21 |
| **Status / completed** | Completed / 2026-08-20 |
| **Evidence of closure** | EVID-075 |
| **Reviewer comment** | Owner agreed; no ongoing need |

### AR-EX-06: AdministratorAccess in production not required for Data Engineer role
| Chain | Detail |
|---|---|
| **Accounts / systems** | `bnguyen` @ AWS wcp-prod |
| **Engine flags** | F-BASELINE; F-DAILYADMIN |
| **Finding** | FIND-003: Excessive privileged access and administration from daily-use accounts (High) |
| **Risk** | RISK-001 (Privileged cloud or identity admin account misused or compromised) |
| **Affected control** | AC-6(5); AC-6 |
| **Remediation** | Modify: Replace with Developer-ReadOnly-Prod; use approval-gated elevation for incidents |
| **Owner** | Tomasz Wierzbicki |
| **Due date** | 2026-08-21 |
| **Status / completed** | Completed / 2026-08-20 |
| **Evidence of closure** | EVID-075 |
| **Reviewer comment** | Owner initially disputed (pipeline troubleshooting); resolved with time-boxed elevation |

### AR-EX-07: Write access to the PHI primary database is not required for Data Engineer role (backfill finished 2025-07)
| Chain | Detail |
|---|---|
| **Accounts / systems** | `bnguyen` @ wcp-core-db |
| **Engine flags** | F-BASELINE |
| **Finding** | FIND-003: Excessive privileged access and administration from daily-use accounts (High) |
| **Risk** | RISK-001 (Privileged cloud or identity admin account misused or compromised) |
| **Affected control** | AC-6; AC-6(5) |
| **Remediation** | Revoke: Revoke app_rw; run future backfills as reviewed migration jobs |
| **Owner** | Tomasz Wierzbicki |
| **Due date** | 2026-07-31 |
| **Status / completed** | Completed / 2026-08-14 |
| **Evidence of closure** | EVID-075 |
| **Reviewer comment** | Completed 14 days after due date (migration-job pattern had to be built first) |

### AR-EX-08: GitHub org owners (5) exceed the approved maximum of 3; owner role not required for VP Engineering
| Chain | Detail |
|---|---|
| **Accounts / systems** | `glindqvist` @ GitHub, `hlarsen` @ GitHub |
| **Engine flags** | F-BASELINE |
| **Finding** | FIND-003: Excessive privileged access and administration from daily-use accounts (High) |
| **Risk** | RISK-001 (Privileged cloud or identity admin account misused or compromised) |
| **Affected control** | AC-6(5) |
| **Remediation** | Modify: Reduce to Maintainer; document owner roster in the access policy |
| **Owner** | Samir Haddad |
| **Due date** | 2026-08-14 |
| **Status / completed** | Completed / 2026-08-11 |
| **Evidence of closure** | EVID-076 |
| **Reviewer comment** | — |

### AR-EX-09: Okta Super Administrator is not part of the IT Manager role and is held on a daily-use account
| Chain | Detail |
|---|---|
| **Accounts / systems** | `kbrandt` @ Okta |
| **Engine flags** | F-BASELINE; F-DAILYADMIN |
| **Finding** | FIND-003: Excessive privileged access and administration from daily-use accounts (High) |
| **Risk** | RISK-001 (Privileged cloud or identity admin account misused or compromised) |
| **Affected control** | AC-6(5); AC-6(2) |
| **Remediation** | Modify: Downgrade to Organization Administrator |
| **Owner** | Alicia Moreno |
| **Due date** | 2026-07-24 |
| **Status / completed** | Completed / 2026-07-20 |
| **Evidence of closure** | EVID-077 |
| **Reviewer comment** | — |

### AR-EX-10: Production AdministratorAccess used from a daily-use account (ACP-002 §5.4 requires a separate admin account)
| Chain | Detail |
|---|---|
| **Accounts / systems** | `lbaptiste` @ AWS wcp-prod, `twierzbicki` @ AWS wcp-prod |
| **Engine flags** | F-DAILYADMIN |
| **Finding** | FIND-003: Excessive privileged access and administration from daily-use accounts (High) |
| **Risk** | RISK-001 (Privileged cloud or identity admin account misused or compromised) |
| **Affected control** | AC-6(2) |
| **Remediation** | Modify: Issue a -adm account with phishing-resistant MFA; remove admin from the daily account |
| **Owner** | Nadia Rahman |
| **Due date** | 2026-09-30 |
| **Status / completed** | In Progress / 2026-09-02 |
| **Evidence of closure** | EVID-075 |
| **Reviewer comment** | -adm account issued 2026-09-15; daily-account removal scheduled after on-call rotation ends |

### AR-EX-11: Member of MFA-Exempt-Legacy group; MFA not enforced (user also held Okta Super Administrator)
| Chain | Detail |
|---|---|
| **Accounts / systems** | `kbrandt` @ Okta, `mcole` @ Okta, `svc-vulnscan` @ Okta |
| **Engine flags** | F-MFA; F-SVC-ROTATION |
| **Finding** | FIND-002: MFA not enforced for all workforce and privileged accounts (High) |
| **Risk** | RISK-003 (Account takeover through MFA gaps) |
| **Affected control** | IA-2(1); IA-2(2) |
| **Remediation** | Modify: Remove from exemption group; enroll phishing-resistant MFA |
| **Owner** | Nadia Rahman |
| **Due date** | 2026-09-05 |
| **Status / completed** | Completed / 2026-08-28 |
| **Evidence of closure** | EVID-063 |
| **Reviewer comment** | "Temporary" exemption for a lost phone in 2025 never removed Exemption dated 2023 (MFA outage troubleshooting) and never removed |

### AR-EX-12: Duplicate identity: legacy contractor account from before conversion to employee (2025-04-01); unused since 2025-03-28
| Chain | Detail |
|---|---|
| **Accounts / systems** | `rgupta2` @ GitHub, `rgupta2` @ Okta |
| **Engine flags** | F-DUP; F-INACTIVE; F-TERM |
| **Finding** | FIND-004: Access recertification incomplete and ineffective (access creep) (Moderate) |
| **Risk** | RISK-004 (Access creep from ineffective recertification) |
| **Affected control** | AC-2 |
| **Remediation** | Revoke: Deactivate rgupta2; confirm no tokens remain |
| **Owner** | Nadia Rahman |
| **Due date** | 2026-07-17 |
| **Status / completed** | Completed / 2026-07-14 |
| **Evidence of closure** | EVID-061 |
| **Reviewer comment** | Engine flagged this as a terminated worker record; reviewer re-classified it as a duplicate (same person active as rgupta) |

### AR-EX-13: Transferred from Support to Data Engineering on 2026-02-16 but kept PHI support access from prior role; used on 2026-05-14 (after transfer)
| Chain | Detail |
|---|---|
| **Accounts / systems** | `cfernandes` @ wcp-core-db |
| **Engine flags** | F-BASELINE; F-TRANSFER |
| **Finding** | FIND-004: Access recertification incomplete and ineffective (access creep) (Moderate) |
| **Risk** | RISK-004 (Access creep from ineffective recertification) |
| **Affected control** | PS-5; AC-2 |
| **Remediation** | Revoke: Revoke; update the transfer checklist to re-baseline access |
| **Owner** | Tomasz Wierzbicki |
| **Due date** | 2026-07-17 |
| **Status / completed** | Completed / 2026-07-13 |
| **Evidence of closure** | EVID-061 |
| **Reviewer comment** | Interview: used to help former team on an escalation; should have gone through a ticket |

### AR-EX-14: No use in 240 days (inactive > 90-day threshold)
| Chain | Detail |
|---|---|
| **Accounts / systems** | `sparks` @ AWS wcp-prod |
| **Engine flags** | F-INACTIVE |
| **Finding** | FIND-004: Access recertification incomplete and ineffective (access creep) (Moderate) |
| **Risk** | RISK-004 (Access creep from ineffective recertification) |
| **Affected control** | AC-2 |
| **Remediation** | Revoke: Revoke; re-request through ticket if needed |
| **Owner** | Tomasz Wierzbicki |
| **Due date** | 2026-07-17 |
| **Status / completed** | Completed / 2026-07-13 |
| **Evidence of closure** | EVID-061 |
| **Reviewer comment** | — |

### AR-EX-15: Contract end date (2026-05-31) passed in PeopleHub while the contractor was still engaged; manager confirmed extension and SOW amendment pending
| Chain | Detail |
|---|---|
| **Accounts / systems** | `awu` @ Okta |
| **Engine flags** | F-CONTRACT |
| **Finding** | FIND-006: Contractor access not bound to engagement term and scope (Moderate) |
| **Risk** | RISK-002 (Unauthorized access by former employees or contractors), RISK-004 (Access creep from ineffective recertification) |
| **Affected control** | PS-7 |
| **Remediation** | Retain with exception: Execute SOW amendment; update end date in PeopleHub; set Okta account expiry |
| **Owner** | Sofia Ricci |
| **Due date** | 2026-07-24 |
| **Status / completed** | Completed / 2026-07-22 |
| **Evidence of closure** | EVID-066 |
| **Reviewer comment** | Ambiguous case: access was legitimate in fact but unsupported on paper for 22 days |

### AR-EX-16: PHI production access not required for the QA role (QA uses staging with synthetic data)
| Chain | Detail |
|---|---|
| **Accounts / systems** | `awu` @ wcp-core-db |
| **Engine flags** | F-BASELINE; F-CONTRACT |
| **Finding** | FIND-006: Contractor access not bound to engagement term and scope (Moderate) |
| **Risk** | RISK-002 (Unauthorized access by former employees or contractors), RISK-004 (Access creep from ineffective recertification) |
| **Affected control** | AC-6; PS-7 |
| **Remediation** | Revoke: Revoke |
| **Owner** | Tomasz Wierzbicki |
| **Due date** | 2026-07-17 |
| **Status / completed** | Completed / 2026-07-13 |
| **Evidence of closure** | EVID-066 |
| **Reviewer comment** | — |

### AR-EX-17: SoD conflict SOD-01: Vendor Master Maintain + Payment Approver (<= $25k)
| Chain | Detail |
|---|---|
| **Accounts / systems** | `jmercer` @ Ledgerline |
| **Engine flags** | F-SOD |
| **Finding** | FIND-007: Segregation-of-duties conflict in vendor payment process (Moderate) |
| **Risk** | RISK-013 (Fraudulent vendor payment through an SoD conflict) |
| **Affected control** | AC-5 |
| **Remediation** | Retain with exception: Formal risk acceptance with compensating monthly vendor-master change review by the Controller; redesign roles when the AP role is backfilled |
| **Owner** | Laura Brenneman |
| **Due date** | 2026-08-14 |
| **Status / completed** | Risk Accepted / 2026-08-12 |
| **Evidence of closure** | EVID-060; EVID-015 |
| **Reviewer comment** | Three-person finance team after AP departure; see RACC-001 |

### AR-EX-18: Service account has no documented owner; SSH key not rotated in over 365 days
| Chain | Detail |
|---|---|
| **Accounts / systems** | `svc-quarrystone-sftp` @ wf-sftp-01 |
| **Engine flags** | F-SVC-OWNER; F-SVC-ROTATION |
| **Finding** | FIND-005: Service and shared accounts lack ownership, credential rotation, and individual accountability (Moderate) |
| **Risk** | RISK-017 (Service-account credential theft) |
| **Affected control** | IA-5; AC-2 |
| **Remediation** | Modify: Assign owner (Liam Porter); rotate key; retire with SFTP migration (POAM-011) |
| **Owner** | Liam Porter |
| **Due date** | 2026-08-28 |
| **Status / completed** | Completed / 2026-08-25 |
| **Evidence of closure** | EVID-065 |
| **Reviewer comment** | — |

### AR-EX-19: IAM user with a static access key over 365 days old; creator terminated; no documented owner
| Chain | Detail |
|---|---|
| **Accounts / systems** | `svc-reporting-etl` @ AWS wcp-prod |
| **Engine flags** | F-SVC-OWNER; F-SVC-ROTATION |
| **Finding** | FIND-005: Service and shared accounts lack ownership, credential rotation, and individual accountability (Moderate) |
| **Risk** | RISK-017 (Service-account credential theft) |
| **Affected control** | IA-5; AC-2 |
| **Remediation** | Modify: Assign owner; migrate to an IAM role; delete the IAM user and key |
| **Owner** | Tomasz Wierzbicki |
| **Due date** | 2026-09-11 |
| **Status / completed** | Completed / 2026-09-03 |
| **Evidence of closure** | EVID-064; EVID-065 |
| **Reviewer comment** | — |

### AR-EX-20: Shared vendor login to EDR console; containment actions not attributable to an individual
| Chain | Detail |
|---|---|
| **Accounts / systems** | `ironpeak-soc` @ Security tooling (EDR) |
| **Engine flags** | F-SHARED |
| **Finding** | FIND-005: Service and shared accounts lack ownership, credential rotation, and individual accountability (Moderate) |
| **Risk** | RISK-017 (Service-account credential theft) |
| **Affected control** | AC-2; IA-2 |
| **Remediation** | Modify: Replace with named federated accounts for each MDR analyst; disable the shared login |
| **Owner** | Owen Castillo |
| **Due date** | 2026-09-04 |
| **Status / completed** | Completed / 2026-08-31 |
| **Evidence of closure** | EVID-065 |
| **Reviewer comment** | Contrast ENT-096: the same vendor already uses named SSO accounts in the SIEM |

