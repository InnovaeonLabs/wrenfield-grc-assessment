# Plan of Action & Milestones (POA&M)

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

Workbook with live formulas (SLA date, % complete, days open, overdue, slipped): [poam.xlsx](poam.xlsx) · CSV: [poam.csv](poam.csv), [poam-milestones.csv](poam-milestones.csv) · Full lifecycle traces: [lifecycle-traces.md](lifecycle-traces.md)

**Status as of 2026-09-18:** 7 Closed, 9 In Progress, 1 Risk Accepted, 1 Delayed, 1 Completed – Pending Validation · **Overdue:** 2 (POAM-009, POAM-018) · **Slipped:** 1 (POAM-011) · **Late milestones:** 5

| ID | Finding | Severity | Owner | Open | Target | Status | % done | Flags |
|---|---|---|---|---|---|---|---|---|
| [POAM-001](#poam-001) | FIND-001 | High | Nadia Rahman | 2026-08-07 | 2026-09-11 | Closed | 100% | — |
| [POAM-002](#poam-002) | FIND-002 | High | Nadia Rahman | 2026-08-07 | 2026-09-05 | Closed | 100% | — |
| [POAM-003](#poam-003) | FIND-003 | High | Tomasz Wierzbicki | 2026-08-07 | 2026-11-05 | In Progress | 25% | — |
| [POAM-004](#poam-004) | FIND-004 | Moderate | Alicia Moreno | 2026-08-07 | 2026-10-31 | In Progress | 50% | — |
| [POAM-005](#poam-005) | FIND-005 | Moderate | Nadia Rahman | 2026-08-07 | 2026-09-12 | Closed | 100% | — |
| [POAM-006](#poam-006) | FIND-006 | Moderate | Sofia Ricci | 2026-08-07 | 2026-09-10 | Closed | 100% | — |
| [POAM-007](#poam-007) | FIND-007 | Moderate | Laura Brenneman | 2026-08-07 | 2027-03-31 | Risk Accepted | 33% | — |
| [POAM-008](#poam-008) | FIND-008 | Moderate | Owen Castillo | 2026-08-07 | 2026-09-15 | Closed | 100% | — |
| [POAM-009](#poam-009) | FIND-009 | Moderate | Owen Castillo | 2026-08-07 | 2026-09-15 | In Progress | 50% | ⏰ OVERDUE |
| [POAM-010](#poam-010) | FIND-010 | High | Grace Lindqvist | 2026-08-07 | 2026-11-05 | In Progress | 40% | — |
| [POAM-011](#poam-011) | FIND-011 | High | Tomasz Wierzbicki | 2026-08-07 | 2026-12-15 | Delayed | 25% | ↪ SLIPPED ⚠ beyond SLA |
| [POAM-012](#poam-012) | FIND-012 | High | Tomasz Wierzbicki | 2026-07-02 | 2026-07-10 | Closed | 100% | — |
| [POAM-013](#poam-013) | FIND-013 | Moderate | Tomasz Wierzbicki | 2026-08-07 | 2026-09-01 | Closed | 100% | — |
| [POAM-014](#poam-014) | FIND-014 | Moderate | Owen Castillo | 2026-08-07 | 2026-11-15 | In Progress | 25% | — |
| [POAM-015](#poam-015) | FIND-015 | Moderate | Beth Kowalski | 2026-08-07 | 2027-02-03 | In Progress | 0% | — |
| [POAM-016](#poam-016) | FIND-016 | High | Dr. Miriam Castell | 2026-08-07 | 2026-11-05 | In Progress | 20% | — |
| [POAM-017](#poam-017) | FIND-017 | Low | Priya Raman | 2026-08-07 | 2026-12-15 | In Progress | 0% | — |
| [POAM-018](#poam-018) | FIND-018 | Moderate | Tomasz Wierzbicki | 2026-08-07 | 2026-09-11 | In Progress | 33% | ⏰ OVERDUE |
| [POAM-019](#poam-019) | FIND-019 | Low | Denise Yamamoto | 2026-08-07 | 2026-09-30 | Completed – Pending Validation | 67% | — |

## Items
<a id="poam-001"></a>
### POAM-001: Terminated workforce retained active access (SSO, local AWS IAM, vendor portal)
**Finding** FIND-001 · **Severity** High · **Controls** AC-2(3), AC-2, AC-2(1), PS-4, PS-7 · **Risks** RISK-002 · **Owner** Nadia Rahman (IAM Engineer)
**Open** 2026-08-07 · **SLA** 2026-11-05 · **Original target** 2026-09-11 · **Current target** 2026-09-11 · **Status** Closed (100% of milestones)

- **Root cause:** Manual HR-email-to-IT ticketing with no automated trigger; local accounts not in offboarding checklist; contractor end dates not enforced
- **Corrective action:** Disable identified accounts; implement daily HR-to-Okta/AWS/portal reconciliation with auto-ticketing; update SOP-IAM-02 with a local-account checklist and 24h SLA
- **Resources:** IAM Engineer (about 60h); Okta Workflows (existing license); HR ops (4h)
- **Dependencies:** Okta Workflows connector to PeopleHub
- **Validation method:** Re-performance: tools/assessment_tests.py termination-validation (7 of 7 within 24h, 0 job exceptions); inspection of IAM credential report (break-glass only)
- **Closure evidence:** EVID-061, EVID-062, EVID-064, EVID-078 · **Validated by:** Lead assessor · **Closed:** 2026-09-10
- **Residual risk:** Moderate (RISK-002 residual L2 x I4 = 8)

- **Notes:** Operating sample is small (7); full re-test scheduled for FY27.

| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Disable 4 identified accounts (AR-EX-01..04); investigate post-termination sign-in (INC-2026-0117) | 2026-07-10 | Done | 2026-07-09 |
| M2 | Deploy daily HR-to-Okta/AWS IAM/portal reconciliation job with auto-ticketing | 2026-08-21 | Done | 2026-08-03 |
| M3 | Update SOP-IAM-02 (24h SLA, local-account checklist, vendor portals); train IT | 2026-08-28 | Done | 2026-08-26 |
| M4 | Assessor validation: re-perform termination test on all terminations since 2026-07-01 + 5 job runs | 2026-09-11 | Done | 2026-09-10 |

<a id="poam-002"></a>
### POAM-002: MFA exemption group and AWS IAM user without MFA
**Finding** FIND-002 · **Severity** High · **Controls** IA-2(1), IA-2(2) · **Risks** RISK-003 · **Owner** Nadia Rahman (IAM Engineer)
**Open** 2026-08-07 · **SLA** 2026-11-05 · **Original target** 2026-09-05 · **Current target** 2026-09-05 · **Status** Closed (100% of milestones)

- **Root cause:** Exceptions granted without workflow, expiry, or review; legacy IAM users bypass Okta policy
- **Corrective action:** Delete exemption policy and group; enroll all members (hardware key accommodation); convert service users to integrations; require phishing-resistant MFA for admin apps; delete non-break-glass IAM users; add time-bound exception workflow
- **Resources:** IAM Engineer (about 30h); 12 FIDO2 keys (about $600)
- **Dependencies:** Hardware key delivery for accessibility accommodation
- **Validation method:** Inspection of Okta policy export and IAM credential report; re-performance of password-only sign-in with a test account (denied)
- **Closure evidence:** EVID-063, EVID-064 · **Validated by:** Lead assessor · **Closed:** 2026-09-05
- **Residual risk:** Moderate (RISK-003 residual L2 x I4 = 8)



| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Enroll 9 human members in MFA (accommodation for 1) | 2026-08-28 | Done | 2026-08-27 |
| M2 | Convert svc-vulnscan and svc-confroom to non-interactive integrations | 2026-08-28 | Done | 2026-08-27 |
| M3 | Delete Legacy Exemption Policy and group; phishing-resistant policy on admin apps (CHG-2026-0731) | 2026-09-01 | Done | 2026-08-28 |
| M4 | Assessor validation: policy export, group lookup, password-only sign-in attempt, IAM credential report | 2026-09-05 | Done | 2026-09-05 |

<a id="poam-003"></a>
### POAM-003: Excessive privileged access; administration from daily-use accounts
**Finding** FIND-003 · **Severity** High · **Controls** AC-6(5), AC-6, AC-6(2) · **Risks** RISK-001 · **Owner** Tomasz Wierzbicki (Director, Platform Engineering)
**Open** 2026-08-07 · **SLA** 2026-11-05 · **Original target** 2026-11-05 · **Current target** 2026-11-05 · **Status** In Progress (25% of milestones)

- **Root cause:** Privileged grants without expiry; no privileged-access review before 2026; separate-admin policy never rolled out
- **Corrective action:** Remove excess grants; issue -adm accounts with phishing-resistant MFA; implement approval-gated JIT elevation for AWS admin; enforce GitHub owner cap
- **Resources:** SRE (about 80h); IAM Engineer (about 20h)
- **Dependencies:** IAM Identity Center permission-set redesign; EVID-071 returned as Rework Required (design-only evidence)
- **Validation method:** Inspection of Identity Center/GitHub/Okta admin exports; re-performance: request and observe a JIT elevation, confirm auto-expiry in CloudTrail
- **Closure evidence:** EVID-075, EVID-076, EVID-077, EVID-071 · **Validated by:** — · **Closed:** —
- **Residual risk:** Moderate target (RISK-001 residual L2 x I4 = 8); currently High

- **Notes:** Evidence EVID-071 rejected: a screenshot of an approval screen shows the design, not that elevation operates.

| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Remove excess grants: AR-EX-05/06/07/08/09 | 2026-08-21 | Done | 2026-08-20 |
| M2 | Issue -adm accounts for remaining admins; remove admin from daily accounts (AR-EX-10) | 2026-09-30 | In Progress | — |
| M3 | Implement JIT elevation (approval + 4h auto-expiry) for AWS AdministratorAccess | 2026-10-23 | In Progress | — |
| M4 | Assessor validation: assignment export + live elevation record with CloudTrail evidence | 2026-11-05 | Not Started | — |

<a id="poam-004"></a>
### POAM-004: Access recertification incomplete in scope and ineffective in operation
**Finding** FIND-004 · **Severity** Moderate · **Controls** AC-6(7), AC-2, PS-5 · **Risks** RISK-004 · **Owner** Alicia Moreno (CISO)
**Open** 2026-08-07 · **SLA** 2027-02-03 · **Original target** 2026-10-31 · **Current target** 2026-10-31 · **Status** In Progress (50% of milestones)

- **Root cause:** Campaign scope limited to Okta app assignments; no usage data or risk flags for reviewers; no transfer trigger
- **Corrective action:** Redesign certification to cover all privileged and PHI entitlements on 9 systems with usage and baseline flags; require rationale for approving flagged items; transfer-triggered re-certification
- **Resources:** GRC Manager (about 40h); IAM Engineer (about 30h); review_engine.py reused as the flagging logic
- **Dependencies:** Q3 campaign completion by reviewers
- **Validation method:** Inspection of campaign export (population completeness vs entitlement exports; % flagged items with rationale; removals actioned)
- **Closure evidence:** EVID-061, EVID-074 · **Validated by:** — · **Closed:** —
- **Residual risk:** Moderate (RISK-004 residual L2 x I3 = 6)



| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Revoke duplicate, transferred, and inactive access (AR-EX-12/13/14) | 2026-07-17 | Done | 2026-07-14 |
| M2 | Add transfer trigger to SOP-IAM-02 (re-baseline access within 5 business days) | 2026-08-28 | Done | 2026-08-25 |
| M3 | Run Q3 privileged certification on new design (EVID-074) | 2026-09-30 | In Progress | — |
| M4 | Assessor validation: review Q3 campaign decisions for flagged items and rationale quality | 2026-10-31 | Not Started | — |

<a id="poam-005"></a>
### POAM-005: Service/shared accounts without owners, stale credentials, shared vendor login
**Finding** FIND-005 · **Severity** Moderate · **Controls** IA-5, AC-2 · **Risks** RISK-017 · **Owner** Nadia Rahman (IAM Engineer)
**Open** 2026-08-07 · **SLA** 2027-02-03 · **Original target** 2026-09-12 · **Current target** 2026-09-12 · **Status** Closed (100% of milestones)

- **Root cause:** Service register lacked owner/rotation fields; vendor access set up for convenience
- **Corrective action:** Assign owners; rotate or federate stale credentials; named federated accounts for MDR analysts; add owner/rotation fields and quarterly attestation to the register
- **Resources:** IAM Engineer (about 20h); SRE (about 16h)
- **Dependencies:** Ironpeak MDR SSO onboarding
- **Validation method:** Re-performance of the review engine's service-account checks on the updated register; inspection of EDR console user list (no shared logins)
- **Closure evidence:** EVID-065, EVID-064 · **Validated by:** Lead assessor · **Closed:** 2026-09-12
- **Residual risk:** Low (RISK-017 residual L1 x I4 = 4)



| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Assign owners to all 13 non-human accounts; add fields to register | 2026-08-21 | Done | 2026-08-18 |
| M2 | Rotate svc-quarrystone-sftp key (AR-EX-18) | 2026-08-28 | Done | 2026-08-25 |
| M3 | Replace ironpeak-soc shared login with 6 named federated accounts (AR-EX-20) | 2026-09-04 | Done | 2026-08-31 |
| M4 | Migrate svc-reporting-etl to IAM role; delete IAM user (AR-EX-19) | 2026-09-11 | Done | 2026-09-03 |
| M5 | Assessor validation: register re-test (owner + credential age) and IAM credential report | 2026-09-12 | Done | 2026-09-12 |

<a id="poam-006"></a>
### POAM-006: Contractor access not bound to engagement term and scope
**Finding** FIND-006 · **Severity** Moderate · **Controls** PS-7, AC-2 · **Risks** RISK-002, RISK-004 · **Owner** Sofia Ricci (Engineering Manager)
**Open** 2026-08-07 · **SLA** 2027-02-03 · **Original target** 2026-09-10 · **Current target** 2026-09-10 · **Status** Closed (100% of milestones)

- **Root cause:** Contract end dates not enforced in Okta; access requests not checked against SOW scope
- **Corrective action:** Okta account expiry = SOW end date for all contractors; SOW scope required on contractor access requests; monthly contractor roster to sponsors
- **Resources:** IAM Engineer (about 8h); Vendor Mgmt (about 4h)
- **Dependencies:** —
- **Validation method:** Inspection: Okta expiry dates reconciled to SOW register for all active contractors (29 of 29)
- **Closure evidence:** EVID-066 · **Validated by:** Lead assessor · **Closed:** 2026-09-10
- **Residual risk:** Moderate (RISK-002 residual)



| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Execute SOW amendment for awu; revoke out-of-scope PHI access (AR-EX-15/16) | 2026-07-24 | Done | 2026-07-22 |
| M2 | Set Okta expiry for all contractor accounts; add SOW-scope field to access request form | 2026-08-28 | Done | 2026-08-24 |
| M3 | Assessor validation: expiry report vs SOW register | 2026-09-10 | Done | 2026-09-08 |

<a id="poam-007"></a>
### POAM-007: SoD conflict (vendor master + payment approval)
**Finding** FIND-007 · **Severity** Moderate · **Controls** AC-5 · **Risks** RISK-013 · **Owner** Laura Brenneman (Controller)
**Open** 2026-08-07 · **SLA** 2027-02-03 · **Original target** 2027-03-31 · **Current target** 2027-03-31 · **Status** Risk Accepted (33% of milestones)

- **Root cause:** Finance team reduced to 3 after AP departure
- **Corrective action:** Formal risk acceptance (RACC-001) with compensating monthly independent review; split roles when AP role is backfilled
- **Resources:** Controller (2h/month for compensating review)
- **Dependencies:** AP Specialist hire
- **Validation method:** Monthly: GRC inspects signed vendor-master change report; at expiry: re-test role assignments
- **Closure evidence:** EVID-060, EVID-015 · **Validated by:** — · **Closed:** —
- **Residual risk:** Moderate, accepted (RISK-013 residual L2 x I3 = 6)

- **Notes:** Accepted risks stay on the POA&M until expiry so they are re-decided, not forgotten.

| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Sign RACC-001 (CFO as risk owner; CISO concurrence) | 2026-08-14 | Done | 2026-08-12 |
| M2 | Continue monthly compensating review (evidence each month to GRC) | 2027-03-31 | In Progress | — |
| M3 | Split roles at AP backfill (requisition open) | 2027-03-31 | Not Started | — |

<a id="poam-008"></a>
### POAM-008: Audit log retention below 12-month requirement
**Finding** FIND-008 · **Severity** Moderate · **Controls** AU-11 · **Risks** RISK-005 · **Owner** Owen Castillo (Security Engineer)
**Open** 2026-08-07 · **SLA** 2027-02-03 · **Original target** 2026-09-15 · **Current target** 2026-09-15 · **Status** Closed (100% of milestones)

- **Root cause:** 2022 cost-driven retention settings never revisited after contractual requirements emerged
- **Corrective action:** 400-day lifecycle with tiering (hot 90d searchable); archive application audit logs to log-archive; quarterly oldest-record check
- **Resources:** Security Engineer (about 16h); storage cost about $180/month
- **Dependencies:** —
- **Validation method:** Inspection of lifecycle/subscription config; test: oldest CloudTrail object (2026-03-20, 182 days) still present after old 180-day rule would have expired it
- **Closure evidence:** EVID-067 · **Validated by:** Lead assessor · **Closed:** 2026-09-15
- **Residual risk:** Moderate (RISK-005 residual after POAM-009)

- **Notes:** Full 12-month retention can only be demonstrated over time; FY27 assessment re-tests.

| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Change S3 lifecycle to 400-day expiry with Glacier IR after 90d (CHG-2026-0702) | 2026-08-21 | Done | 2026-08-19 |
| M2 | Subscribe app-audit CloudWatch logs to log-archive (Firehose) | 2026-08-28 | Done | 2026-08-27 |
| M3 | Assessor validation: config inspection + oldest-object query | 2026-09-15 | Done | 2026-09-12 |

<a id="poam-009"></a>
### POAM-009: Weekly privileged-activity review missed 7 of 26 weeks; 2 incomplete
**Finding** FIND-009 · **Severity** Moderate · **Controls** AU-6 · **Risks** RISK-005 · **Owner** Owen Castillo (Security Engineer)
**Open** 2026-08-07 · **SLA** 2027-02-03 · **Original target** 2026-09-15 · **Current target** 2026-09-15 · **Status** In Progress (50% of milestones)

- **Root cause:** Single reviewer; no escalation; scope excluded local IAM users
- **Corrective action:** Backup reviewer (MDR under SOW change); auto-created weekly ticket with 5-day escalation; expand scope to all privileged principals; disposition required per flag
- **Resources:** MDR SOW change (about $1,500/month); Security Engineer (about 12h)
- **Dependencies:** Procurement approval of MDR SOW change (pending CFO signature)
- **Validation method:** Test: all weeks since change performed within 5 days with dispositions; inspect escalation config
- **Closure evidence:** EVID-072 · **Validated by:** — · **Closed:** —
- **Residual risk:** Moderate (RISK-005 residual L2 x I3 = 6)

- **Notes:** Overdue since 2026-09-15; escalated to CISO 2026-09-16.

| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Expand SIEM report scope to all privileged principals incl. IAM users | 2026-08-21 | Done | 2026-08-14 |
| M2 | Auto-create weekly review ticket with escalation to CISO at 5 business days | 2026-08-28 | Done | 2026-08-28 |
| M3 | Execute MDR SOW change for backup reviewer | 2026-09-11 | Delayed | — |
| M4 | Assessor validation: W27–W37 reviews (EVID-072) | 2026-09-15 | Not Started | — |

<a id="poam-010"></a>
### POAM-010: 23% of Critical/High vulnerabilities exceeded SLA; exception process unused
**Finding** FIND-010 · **Severity** High · **Controls** SI-2 · **Risks** RISK-006 · **Owner** Grace Lindqvist (VP Engineering)
**Open** 2026-08-07 · **SLA** 2026-11-05 · **Original target** 2026-11-05 · **Current target** 2026-11-05 · **Status** In Progress (40% of milestones)

- **Root cause:** End-of-life runtimes block patching; no exception discipline; SLA not visible in engineering planning; 7% untagged assets
- **Corrective action:** Upgrade notify-worker runtime; file exceptions with reachability analysis where justified; SLA dashboard in sprint planning; tag-policy SCP
- **Resources:** Engineering (about 3 sprint-weeks); Security Engineer (about 16h)
- **Dependencies:** FIND-011 (4 open breaches resolve only when legacy hosts are decommissioned)
- **Validation method:** Re-performance: tools/assessment_tests.py vulnsla on Q3 export (target: >= 95% within SLA, 0 open Critical past SLA without exception)
- **Closure evidence:** — · **Validated by:** — · **Closed:** —
- **Residual risk:** Moderate (RISK-006 residual L2 x I4 = 8)

- **Notes:** CISO approved a 30-day exception for the 2 criticals (expires 2026-09-30) contingent on M2; consider SI-2(7) root cause analysis (OBS-04).

| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Submit VM-003 §7 exception for 2 notify-worker criticals with reachability analysis (CISO decision) | 2026-08-21 | Done | 2026-08-20 |
| M2 | Upgrade notify-worker to supported Node.js LTS + current base image | 2026-09-30 | In Progress | — |
| M3 | SLA-breach dashboard reviewed in weekly engineering leads meeting | 2026-09-15 | Done | 2026-09-09 |
| M4 | Tag-policy SCP denying untagged EC2/EKS launches (OBS-02) | 2026-10-15 | Not Started | — |
| M5 | Assessor validation: re-run SLA test on Q3 population | 2026-11-05 | Not Started | — |

<a id="poam-011"></a>
### POAM-011: Unsupported components (Windows 2012 R2 SFTP host, PostgreSQL 11, Node.js 16) in PHI path
**Finding** FIND-011 · **Severity** High · **Controls** SA-22 · **Risks** RISK-007 · **Owner** Tomasz Wierzbicki (Director, Platform Engineering)
**Open** 2026-08-07 · **SLA** 2026-11-05 · **Original target** 2026-11-05 · **Current target** 2026-12-15 · **Status** Delayed (25% of milestones)

- **Root cause:** Legacy integrations excluded from modernization; no lifecycle review for non-IaC assets
- **Corrective action:** Avoid: replace wf-sftp-01 with managed transfer (IaC, PGP + SFTP, vendor/customer keys); migrate legacy-reports to supported Aurora replica; upgrade notify-worker (with POAM-010); maintain compensating controls until then
- **Resources:** SRE (about 120h); Customer Ops coordination with 4 customers + Quarrystone; managed transfer service about $400/month
- **Dependencies:** Customer partner-side key exchange (2 of 4 pending); POAM-010 M2 for notify-worker
- **Validation method:** Inspection of EOL inventory and AWS Config (instances terminated); re-run vulnsla to confirm legacy-host findings closed
- **Closure evidence:** — · **Validated by:** — · **Closed:** —
- **Residual risk:** Low target (RISK-007 residual L1 x I4 = 4); currently High
- **Target change:** M2 slipped: 2 of 4 customers have not completed partner key exchange. SLA extension approved by CTO and CISO 2026-09-12 with compensating controls (EDR, allowlist, SSM-only admin, weekly scans); still ahead of SHCA go-live 2027-01-11.
- **Notes:** Treatment is Avoid (decommission) rather than patching, which is not possible.

| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Stand up managed transfer service (IaC) and test with Quarrystone | 2026-08-28 | Done | 2026-08-26 |
| M2 | Cut over Quarrystone + 4 customers; decommission wf-sftp-01 | 2026-09-15 | Delayed | — |
| M3 | Migrate legacy-reports to Aurora read replica; decommission EC2 host | 2026-10-30 | In Progress | — |
| M4 | Assessor validation: inventory shows 0 unsupported components; hosts terminated | 2026-12-15 | Not Started | — |

<a id="poam-012"></a>
### POAM-012: RDP open to 0.0.0.0/0 on wf-sftp-01; CSPM High finding untriaged 43 days
**Finding** FIND-012 · **Severity** High · **Controls** SC-7, CM-6 · **Risks** RISK-012, RISK-007 · **Owner** Tomasz Wierzbicki (Director, Platform Engineering)
**Open** 2026-07-02 · **SLA** 2026-09-30 · **Original target** 2026-07-10 · **Current target** 2026-07-10 · **Status** Closed (100% of milestones)

- **Root cause:** Console change path bypasses IaC/approval; Security Hub findings not routed to on-call
- **Corrective action:** Remove rule; route Security Hub High findings to on-call with 7-day SLA; SCP guardrail blocking 0.0.0.0/0 on admin ports
- **Resources:** SRE (about 12h)
- **Dependencies:** —
- **Validation method:** Inspection of SG and Security Hub status; re-performance: attempted to add 0.0.0.0/0:3389 rule in a sandbox OU account (denied by SCP)
- **Closure evidence:** EVID-068, EVID-053 · **Validated by:** Lead assessor · **Closed:** 2026-07-10
- **Residual risk:** Moderate (RISK-012 residual L2 x I4 = 8)

- **Notes:** Remediated during fieldwork. Still reported as a finding because the control failed during the period.

| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Remove 3389 ingress rule; confirm SSM-only admin (CHG-2026-0521); review Windows 4624 type-10 logons | 2026-07-03 | Done | 2026-07-03 |
| M2 | Route Security Hub High findings to SRE on-call queue | 2026-07-08 | Done | 2026-07-07 |
| M3 | Deploy SCP guardrail for admin ports from 0.0.0.0/0 | 2026-07-10 | Done | 2026-07-09 |
| M4 | Assessor validation: SG export, Security Hub PASSED, guardrail test | 2026-07-10 | Done | 2026-07-10 |

<a id="poam-013"></a>
### POAM-013: Backup restoration never tested
**Finding** FIND-013 · **Severity** Moderate · **Controls** CP-9(1) · **Risks** RISK-008 · **Owner** Tomasz Wierzbicki (Director, Platform Engineering)
**Open** 2026-08-07 · **SLA** 2027-02-03 · **Original target** 2026-09-01 · **Current target** 2026-09-01 · **Status** Closed (100% of milestones)

- **Root cause:** Recoverability assumed from job success; no scheduled restore test
- **Corrective action:** Documented restore from DR vault into isolated account with timing and integrity checks; semi-annual schedule in BCP-003
- **Resources:** SRE (about 16h); isolated recovery account
- **Dependencies:** —
- **Validation method:** Observation of restore test; inspection of timings vs RTO/RPO and integrity check output
- **Closure evidence:** EVID-069 · **Validated by:** Lead assessor · **Closed:** 2026-09-01
- **Residual risk:** Moderate (RISK-008 residual L2 x I4 = 8, pending POAM-014)



| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Write restore runbook and integrity-check queries | 2026-08-21 | Done | 2026-08-19 |
| M2 | Perform restore test (assessor observes) | 2026-08-28 | Done | 2026-08-27 |
| M3 | Add semi-annual restore test to BCP-003 calendar; assessor validation | 2026-09-01 | Done | 2026-09-01 |

<a id="poam-014"></a>
### POAM-014: IR and contingency plans not tested in 12+ months; SHCA 24h path unrehearsed
**Finding** FIND-014 · **Severity** Moderate · **Controls** IR-3, CP-4 · **Risks** RISK-009, RISK-008 · **Owner** Owen Castillo (Security Engineer)
**Open** 2026-08-07 · **SLA** 2027-02-03 · **Original target** 2026-11-15 · **Current target** 2026-11-15 · **Status** In Progress (25% of milestones)

- **Root cause:** Exercises deferred twice without escalation
- **Corrective action:** Combined ransomware tabletop (IR + CP) with MDR, Legal/Privacy, Customer Ops, execs; update IRP-005 (SHCA 24h step, roster); track after-action items
- **Resources:** Facilitator (MDR-provided, in contract); 3h of 12 participants
- **Dependencies:** Executive calendar availability
- **Validation method:** Inspection of exercise materials, attendance, after-action report; verify corrective actions are tracked
- **Closure evidence:** — · **Validated by:** — · **Closed:** —
- **Residual risk:** Moderate (RISK-009 residual L2 x I3 = 6)



| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Update IRP-005: SHCA 24h notification step + current roster (OBS-03) | 2026-09-15 | Done | 2026-09-11 |
| M2 | Conduct ransomware tabletop (IR + CP) | 2026-10-14 | Not Started | — |
| M3 | Publish after-action report; add corrective actions to POA&M | 2026-10-30 | Not Started | — |
| M4 | Assessor validation | 2026-11-15 | Not Started | — |

<a id="poam-015"></a>
### POAM-015: 5 of 14 Tier 1–2 vendors overdue; no fourth-party inventory; no C-SCRM plan
**Finding** FIND-015 · **Severity** Moderate · **Controls** SR-6, SA-9, SR-2 · **Risks** RISK-011, RISK-010 · **Owner** Beth Kowalski (Vendor Management Lead)
**Open** 2026-08-07 · **SLA** 2027-02-03 · **Original target** 2027-02-03 · **Current target** 2027-02-03 · **Status** In Progress (0% of milestones)

- **Root cause:** Under-resourced vendor program; spreadsheet tracking without reminders
- **Corrective action:** Clear overdue assessments (Tier 1 first); build fourth-party inventory; approve C-SCRM plan aligned to SP 800-161r1-upd1 / SP 800-18r2; renewal triggers
- **Resources:** Vendor Mgmt (about 0.5 FTE for 4 months); GRC Manager support
- **Dependencies:** Vendor responsiveness
- **Validation method:** Inspection of vendor register (100% Tier 1–2 within frequency) and approved C-SCRM plan
- **Closure evidence:** — · **Validated by:** — · **Closed:** —
- **Residual risk:** Moderate (RISK-011 residual L2 x I4 = 8)



| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Assess Tier 1 overdue vendors (Pulsewire, Ironpeak) | 2026-11-30 | In Progress | — |
| M2 | Fourth-party inventory from updated questionnaires (all Tier 1) | 2026-12-15 | Not Started | — |
| M3 | Approve C-SCRM plan | 2027-01-15 | Not Started | — |
| M4 | Assess remaining Tier 2 overdue vendors; assessor validation | 2027-02-03 | Not Started | — |

<a id="poam-016"></a>
### POAM-016: Quarrystone: offshore PHI access, 30-day breach notice, excessive data fields, stale pentest
**Finding** FIND-016 · **Severity** High · **Controls** SA-9, SR-6 · **Risks** RISK-010 · **Owner** Dr. Miriam Castell (VP Clinical Analytics)
**Open** 2026-08-07 · **SLA** 2026-11-05 · **Original target** 2026-11-05 · **Current target** 2026-11-05 · **Status** In Progress (20% of milestones)

- **Root cause:** 2023 contract on vendor paper before TPRM-007; self-attestation relied on; extract not designed for minimum necessary
- **Corrective action:** Contract amendment (US-only + technical enforcement, 24h notice, subcontractor approval, data return/destruction 30 days with certificate, log cooperation); minimize extract to scoring-required fields with tokenized IDs; obtain current pentest + retest; SHCA data blocked until conditions met
- **Resources:** General Counsel (about 20h); Data Engineering (about 60h for extract redesign); Vendor Mgmt
- **Dependencies:** Vendor negotiation; Quarrystone model retraining on minimized fields
- **Validation method:** Inspection of executed amendment; test: sample extract file schema vs approved minimum field list; inspection of pentest/retest; vendor attestation of US-only access with access-log sample
- **Closure evidence:** EVID-073, EVID-051 · **Validated by:** — · **Closed:** —
- **Residual risk:** Moderate target (RISK-010 residual L2 x I4 = 8); currently High

- **Notes:** VR-001 (Critical) escalated to CEO 2026-07-17 per risk appetite; CEO approved conditional continuation 2026-07-22.

| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Interim: vendor suspends offshore access to Wrenfield data (letter) | 2026-07-24 | Done | 2026-07-24 |
| M2 | Execute contract amendment (redline v3 in negotiation) | 2026-09-30 | In Progress | — |
| M3 | Deploy minimized, tokenized extract (drop address, phone, email, free text) | 2026-10-16 | In Progress | — |
| M4 | Receive current pentest report + retest letter (EVID-051) | 2026-10-30 | Not Started | — |
| M5 | Assessor validation + vendor risk re-score | 2026-11-05 | Not Started | — |

<a id="poam-017"></a>
### POAM-017: SSP outdated; overstates implementation of 27 of 61 controls
**Finding** FIND-017 · **Severity** Low · **Controls** PL-2 · **Risks** RISK-016 · **Owner** Priya Raman (Security Compliance Manager)
**Open** 2026-08-07 · **SLA** 2027-08-07 · **Original target** 2026-12-15 · **Current target** 2026-12-15 · **Status** In Progress (0% of milestones)

- **Root cause:** SSP maintained as SOC 2 narrative; no update trigger on architecture change
- **Corrective action:** Rewrite SSP control-by-control from the validated matrix (SP 800-18 Rev. 2 structure); add architecture-change trigger in CMP-006
- **Resources:** GRC Manager (about 80h); control owner reviews
- **Dependencies:** Control owners' review time
- **Validation method:** Inspection: SSP statements traced to matrix determinations (sample 15 controls)
- **Closure evidence:** — · **Validated by:** — · **Closed:** —
- **Residual risk:** Low (RISK-016 residual)



| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | SSP outline on SP 800-18r2 structure; boundary + data flows updated | 2026-09-30 | In Progress | — |
| M2 | Control implementation statements (61 controls) reviewed by owners | 2026-11-30 | Not Started | — |
| M3 | Approval by CTO (system owner); assessor validation | 2026-12-15 | Not Started | — |

<a id="poam-018"></a>
### POAM-018: Emergency and console changes bypass approval (3 of 25 sampled)
**Finding** FIND-018 · **Severity** Moderate · **Controls** CM-3 · **Risks** RISK-014 · **Owner** Tomasz Wierzbicki (Director, Platform Engineering)
**Open** 2026-08-07 · **SLA** 2027-02-03 · **Original target** 2026-09-11 · **Current target** 2026-09-11 · **Status** In Progress (33% of milestones)

- **Root cause:** Console/emergency paths rely on memory; no retro-approval tracking
- **Corrective action:** Auto-open retro-approval task on every emergency change with 2-day escalation; CloudTrail/EventBridge alerts on console changes to security groups and IAM; approval gate before deploy job
- **Resources:** SRE (about 24h)
- **Dependencies:** SRE backlog capacity (competing with POAM-011)
- **Validation method:** Test: all emergency changes since 2026-08-28 retro-approved within 2 business days; trigger a test SG change and confirm alert
- **Closure evidence:** — · **Validated by:** — · **Closed:** —
- **Residual risk:** Moderate (RISK-014 residual L2 x I3 = 6)

- **Notes:** Overdue since 2026-09-11; needs CTO prioritization decision against POAM-011 (same SRE team).

| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Retro-approval task automation for emergency changes | 2026-08-28 | Done | 2026-08-28 |
| M2 | EventBridge alerts on console SG/IAM changes to on-call | 2026-09-04 | Not Started | — |
| M3 | Assessor validation: sample of emergency changes since M1 + alert test | 2026-09-11 | Not Started | — |

<a id="poam-019"></a>
### POAM-019: Security awareness training completion 91%; suspension not enforced
**Finding** FIND-019 · **Severity** Low · **Controls** AT-2 · **Risks** RISK-015 · **Owner** Denise Yamamoto (Director of People)
**Open** 2026-08-07 · **SLA** 2027-08-07 · **Original target** 2026-09-30 · **Current target** 2026-09-30 · **Status** Completed – Pending Validation (67% of milestones)

- **Root cause:** Reminders to users only; no manager escalation or enforcement
- **Corrective action:** Okta group rule enforcing suspension at 30 days overdue; manager escalation at 14 days; monthly completion reporting
- **Resources:** People Ops (about 8h); IAM Engineer (about 4h)
- **Dependencies:** —
- **Validation method:** Inspection: LMS roster reconciled to Okta active population; leave exceptions verified in PeopleHub
- **Closure evidence:** EVID-070 · **Validated by:** — · **Closed:** —
- **Residual risk:** Moderate, accepted (RISK-015 residual L3 x I3 = 9)



| # | Milestone | Due | Status | Completed |
|---|---|---|---|---|
| M1 | Manager escalation at 14 days; enforcement group rule live | 2026-08-21 | Done | 2026-08-20 |
| M2 | Reach >= 99% (documented leave exceptions) | 2026-09-15 | Done | 2026-09-12 |
| M3 | Assessor validation of EVID-070 (leave records for 3 exceptions) | 2026-09-30 | In Progress | — |

