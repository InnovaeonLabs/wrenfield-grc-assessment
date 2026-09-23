# Findings Register

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

Workbook: [findings-register.xlsx](findings-register.xlsx) · CSV: [findings-register.csv](findings-register.csv) · POA&M: [poam.md](../poam/poam.md)

**19 findings**: 7 High, 10 Moderate, 2 Low · Status as of 2026-09-18: 7 Closed, 9 In Progress, 1 Risk Accepted, 1 Delayed, 1 Completed – Pending Validation. Plus 6 observations (below the finding threshold).

Each finding is written twice. The **Technical / GRC version** uses the audit "5 Cs" for control owners and auditors. The **Executive version** is plain language for leadership: what happened, why it matters, business impact, action, and urgency.

| ID | Title | Severity | Control | Risk | POA&M | Status |
|---|---|---|---|---|---|---|
| [FIND-001](#find-001) | Terminated workforce retained active access | High | AC-2(3) | RISK-002 | POAM-001 | Closed |
| [FIND-002](#find-002) | MFA not enforced for all workforce and privileged accounts | High | IA-2(1) | RISK-003 | POAM-002 | Closed |
| [FIND-003](#find-003) | Excessive privileged access and administration from daily-use accounts | High | AC-6(5) | RISK-001 | POAM-003 | In Progress |
| [FIND-004](#find-004) | Access recertification incomplete and ineffective (access creep) | Moderate | AC-6(7) | RISK-004 | POAM-004 | In Progress |
| [FIND-005](#find-005) | Service and shared accounts lack ownership, credential rotation, and individual accountability | Moderate | IA-5 | RISK-017 | POAM-005 | Closed |
| [FIND-006](#find-006) | Contractor access not bound to engagement term and scope | Moderate | PS-7 | RISK-002, RISK-004 | POAM-006 | Closed |
| [FIND-007](#find-007) | Segregation-of-duties conflict in vendor payment process | Moderate | AC-5 | RISK-013 | POAM-007 | Risk Accepted |
| [FIND-008](#find-008) | Audit log retention below the 12-month contractual requirement | Moderate | AU-11 | RISK-005 | POAM-008 | Closed |
| [FIND-009](#find-009) | Privileged-activity log reviews not consistently performed or documented | Moderate | AU-6 | RISK-005 | POAM-009 | In Progress |
| [FIND-010](#find-010) | Vulnerability remediation exceeds contractual SLAs | High | SI-2 | RISK-006 | POAM-010 | In Progress |
| [FIND-011](#find-011) | Unsupported software components in the PHI data path | High | SA-22 | RISK-007 | POAM-011 | Delayed |
| [FIND-012](#find-012) | Internet-exposed RDP on legacy host; CSPM alert not triaged | High | SC-7 | RISK-012, RISK-007 | POAM-012 | Closed |
| [FIND-013](#find-013) | Backup restoration never tested | Moderate | CP-9(1) | RISK-008 | POAM-013 | Closed |
| [FIND-014](#find-014) | Incident response and contingency plans not tested within 12 months | Moderate | IR-3 | RISK-009, RISK-008 | POAM-014 | In Progress |
| [FIND-015](#find-015) | Third-party risk monitoring incomplete; no C-SCRM plan | Moderate | SR-6 | RISK-011, RISK-010 | POAM-015 | In Progress |
| [FIND-016](#find-016) | Quarrystone Analytics: offshore PHI access, inadequate breach-notification terms, and excessive data sharing | High | SA-9 | RISK-010 | POAM-016 | In Progress |
| [FIND-017](#find-017) | System security plan outdated and overstates control implementation | Low | PL-2 | RISK-016 | POAM-017 | In Progress |
| [FIND-018](#find-018) | Emergency and console changes bypass approval | Moderate | CM-3 | RISK-014 | POAM-018 | In Progress |
| [FIND-019](#find-019) | Security awareness training completion below 100% | Low | AT-2 | RISK-015 | POAM-019 | Completed – Pending Validation |

<a id="find-001"></a>
## FIND-001: Terminated workforce retained active access
**Severity:** High (L4 × I4 = 16) · **Status:** Closed · **Owner:** Nadia Rahman (IAM Engineer) · **Identified:** 2026-07-06 · **Source:** Control test + access review
**Controls:** AC-2(3), AC-2, AC-2(1), PS-4, PS-7 · **Risk:** RISK-002 · **POA&M:** [POAM-001](../poam/poam.md#poam-001) · **Related:** AR-EX-01, AR-EX-02, AR-EX-03, AR-EX-04, VR-007, EVID-003, EVID-004, EVID-007, EVID-078

### Technical / GRC version
| | |
|---|---|
| **Condition** | 2 of 19 workers terminated in H1 2026 were still enabled in Okta at the 2026-06-30 snapshot, and 1 more was disabled 9 days late. A terminated contractor signed in 4 days after the contract ended (INC-2026-0117). A local AWS IAM user with AdministratorAccess belonging to an employee terminated 2026-03-27 was still active 95 days later. A former employee still had a Quarrystone portal account (local authentication). |
| **Criteria** | SHCA CSA §3.3 and ACP-002 §5.3 require disabling within 24 hours. HIPAA 164.308(a)(3)(ii)(C) requires termination procedures. The vendor SOC 2 CUEC requires Wrenfield to manage its portal users. |
| **Cause** | De-provisioning depended on IT manually creating a ticket from an HR email, with no automated HR trigger (AC-2(1)). The offboarding checklist covered only Okta, not local accounts (AWS IAM users, wf-sftp-01, the vendor portal). Contract end dates were not enforced. |
| **Effect** | Former workers could reach PHI systems (AWS admin) or financial systems (Ledgerline AP) after separation. One post-termination sign-in required a HIPAA breach risk assessment (outcome, low probability of compromise). |
| **Recommendation** | Automate HR-driven de-provisioning or daily reconciliation with auto-ticketing. Eliminate or register all local accounts. Set expiry dates on contractor accounts. Add vendor portals to the JML checklist and pursue SSO for them. |
| **Management response** | Agree. The CISO committed to automated reconciliation by 2026-08-21 and local-account cleanup by 2026-07-10. |

### Executive version
- **What happened:** Some people who had left the company still had working logins, including one former contractor who signed in after leaving and one former engineer who kept administrator access to our production cloud.
- **Why it matters:** Former workers keeping access is one of the most common causes of healthcare data breaches and insider incidents, and the state contract requires access removal within 24 hours.
- **Business impact:** A misuse could expose patient data (reportable breach), breach the SHCA contract, and repeat the exact concern Lakemont raised in its review.
- **Recommended action / status:** Fixed. Accounts were disabled the day they were found, a daily automated check was added, and the fix was verified with 7 of 7 later departures removed on time.
- **Urgency:** Closed. Keep monitoring through the daily job and re-test annually.

<a id="find-002"></a>
## FIND-002: MFA not enforced for all workforce and privileged accounts
**Severity:** High (L4 × I4 = 16) · **Status:** Closed · **Owner:** Nadia Rahman (IAM Engineer) · **Identified:** 2026-06-30 · **Source:** Control test + access review
**Controls:** IA-2(1), IA-2(2) · **Risk:** RISK-003 · **POA&M:** [POAM-002](../poam/poam.md#poam-002) · **Related:** AR-EX-11, EVID-010, EVID-011, EVID-007, EVID-063, EVID-064

### Technical / GRC version
| | |
|---|---|
| **Condition** | An Okta policy created in 2023 as a "temporary" workaround exempted the MFA-Exempt-Legacy group (11 accounts, 9 human) from MFA. One member was an Okta Super Administrator. None of the exemptions had approval or an expiry date. In AWS, the IAM user mfeld-admin (AdministratorAccess) had a console password and no MFA. |
| **Criteria** | SHCA CSA §3.2 requires MFA for all privileged and remote access. HIPAA 164.312(d) requires person or entity authentication. ACP-002 §6.1 limits exceptions to 30 days with CISO approval. |
| **Cause** | Exceptions were granted by help desk and IT without a workflow, an expiry, or review. Legacy IAM users bypass the Okta policy entirely. |
| **Effect** | Password-only access to an identity administrator account put every downstream system at risk from a single phished password. This is the exact MFA concern raised in the Lakemont review. |
| **Recommendation** | Remove the exemption policy and group. Enroll all members, with accommodation alternatives such as hardware keys. Convert service users to non-interactive integrations. Require phishing-resistant MFA for admin apps. Remove IAM users other than break-glass. Implement a time-bound exception workflow. |
| **Management response** | Agree. Target 2026-09-05. |

### Executive version
- **What happened:** Nine employees, including one administrator who controls everyone's logins, could sign in with just a password because of a "temporary" 2023 exception that was never removed.
- **Why it matters:** Stolen passwords are the most common way attackers get in. Multi-factor authentication stops most of those attacks, and both the state contract and our largest customer require it.
- **Business impact:** One phished administrator password could have given an attacker access to every system, including patient data.
- **Recommended action / status:** Fixed. The exception was deleted, all nine users now use MFA, administrators must use phishing-resistant sign-in, and the fix was verified by testing a password-only sign-in (blocked).
- **Urgency:** Closed. A formal exception process now prevents recurrence.

<a id="find-003"></a>
## FIND-003: Excessive privileged access and administration from daily-use accounts
**Severity:** High (L3 × I5 = 15) · **Status:** In Progress · **Owner:** Tomasz Wierzbicki (Director, Platform Engineering) · **Identified:** 2026-07-10 · **Source:** Access review
**Controls:** AC-6(5), AC-6, AC-6(2) · **Risk:** RISK-001 · **POA&M:** [POAM-003](../poam/poam.md#poam-003) · **Related:** AR-EX-05, AR-EX-06, AR-EX-07, AR-EX-08, AR-EX-09, AR-EX-10, EVID-016, EVID-017, EVID-071, EVID-075, EVID-076, EVID-077

### Technical / GRC version
| | |
|---|---|
| **Condition** | Production AWS AdministratorAccess was held by 2 engineers outside the SRE role, including a 2024 'temporary' migration grant. GitHub had 5 organization owners against an approved maximum of 3. An IT Manager held Okta Super Administrator. A Data Engineer had write access to the PHI primary database. 2 of 3 authorized SRE admins used their email and browsing accounts for production administration, contrary to ACP-002 §5.4. |
| **Criteria** | AC-6 and AC-6(5) least privilege. ACP-002 §5.4 separate admin accounts. SOC 2 CC6.3 commitment. |
| **Cause** | Privileged grants have no expiry, and no privileged-access review existed before this assessment. The separate-admin-account policy (2025-07) was never rolled out. |
| **Effect** | A compromised daily account, which is exposed to phishing and browsing, could immediately act as a production administrator over all PHI. |
| **Recommendation** | Remove excess grants. Issue -adm accounts with phishing-resistant MFA. Introduce just-in-time (JIT), approval-gated elevation with automatic expiry for AWS admin. Enforce the GitHub owner cap. |
| **Management response** | Agree. Engineering initially disputed the Data Engineer's need; resolved with time-boxed elevation. Target 2026-11-05. |

### Executive version
- **What happened:** More people had "keys to everything" in our production systems than their jobs require, and some administrators used the same account for email and for managing production.
- **Why it matters:** If any of those accounts were phished, an attacker would instantly have full control of patient data and infrastructure.
- **Business impact:** This is the highest-impact identity risk in the assessment (maximum patient-data exposure and outage potential).
- **Recommended action / status:** 7 of 8 excess grants removed. Separate admin accounts and time-limited, approved elevation are being finished.
- **Urgency:** High. Complete by 2026-11-05, before SHCA go-live.

<a id="find-004"></a>
## FIND-004: Access recertification incomplete and ineffective (access creep)
**Severity:** Moderate (L3 × I3 = 9) · **Status:** In Progress · **Owner:** Alicia Moreno (CISO) · **Identified:** 2026-07-10 · **Source:** Control test + access review
**Controls:** AC-6(7), AC-2, PS-5 · **Risk:** RISK-004 · **POA&M:** [POAM-004](../poam/poam.md#poam-004) · **Related:** AR-EX-12, AR-EX-13, AR-EX-14, EVID-008, EVID-009, EVID-044, EVID-074

### Technical / GRC version
| | |
|---|---|
| **Condition** | Quarterly Okta certifications cover app assignments only. AWS, GitHub, database, and local accounts were never reviewed. In the Q1 campaign, 412 of 412 items were approved and 17 of 23 reviewers finished in under 5 minutes. The campaign approved a duplicate account (rgupta2) and a transferred user's prior-role PHI access, which that user used after the transfer. One user kept production access unused for 240 days. |
| **Criteria** | SHCA CSA §3.3 requires quarterly privileged recertification. HIPAA 164.308(a)(4)(ii)(C). AC-6(7). PS-5. |
| **Cause** | Campaign scope is limited to what the Okta certification feature can see. Reviewers get no usage data or risk flags. Transfers do not trigger an access re-baseline. |
| **Effect** | Access accumulates beyond need, which undermines least privilege and raises insider and compromise impact. |
| **Recommendation** | Expand campaigns to all privileged and PHI entitlements across the 9 systems. Give reviewers last-used dates and role-baseline deviations (the review engine output). Require a rationale for approving flagged items. Add a transfer-triggered re-certification. |
| **Management response** | Agree. The Q3 campaign is being run on the new design; its results are due 2026-09-30. |

### Executive version
- **What happened:** Our quarterly access reviews were a checkbox. Managers approved everything within minutes, and the most sensitive systems were never included.
- **Why it matters:** Reviews are how we catch access that people no longer need. A review that approves everything does not protect us.
- **Business impact:** People keep sensitive access they no longer need, which is exactly what our largest customer flagged ("no evidence of privileged-access recertification").
- **Recommended action / status:** The first full privileged review has been completed (this assessment). Reviews are being redesigned to cover all sensitive systems and show reviewers which items need attention.
- **Urgency:** Moderate. First redesigned review due 2026-09-30.

<a id="find-005"></a>
## FIND-005: Service and shared accounts lack ownership, credential rotation, and individual accountability
**Severity:** Moderate (L3 × I3 = 9) · **Status:** Closed · **Owner:** Nadia Rahman (IAM Engineer) · **Identified:** 2026-07-09 · **Source:** Access review
**Controls:** IA-5, AC-2 · **Risk:** RISK-017 · **POA&M:** [POAM-005](../poam/poam.md#poam-005) · **Related:** AR-EX-18, AR-EX-19, AR-EX-20, EVID-013, EVID-065

### Technical / GRC version
| | |
|---|---|
| **Condition** | Of 13 non-human accounts: 2 had no documented owner (svc-quarrystone-sftp, whose SSH key was 811 days old and which pushes the nightly PHI extract; svc-reporting-etl, an IAM user with a 539-day static access key created by a now-terminated employee). The MDR vendor used a single shared login to the EDR console, so containment actions could not be attributed to individual analysts. |
| **Criteria** | IA-5 (refresh authenticators; the Wrenfield standard is 365 days). AC-2 (account managers for every account). ACP-002 §4.2 (no shared accounts). |
| **Cause** | The service-account register had no owner or rotation fields. Vendor access was set up for convenience during MDR onboarding. |
| **Effect** | Long-lived secrets increase the chance of undetected credential theft, and orphaned accounts are not monitored by anyone. |
| **Recommendation** | Assign owners. Rotate or federate credentials (IAM roles, OIDC). Replace the shared vendor login with named federated accounts. Add owner and rotation fields and quarterly attestation to the register. |
| **Management response** | Agree. Target 2026-09-12. |

### Executive version
- **What happened:** A few automated system accounts had no owner and passwords or keys that had not changed in 1.5 to 2+ years. One vendor team shared a single login to a security tool.
- **Why it matters:** Old, unowned credentials are easy to steal and hard to notice. Shared logins mean we cannot tell who did what.
- **Business impact:** One of the affected accounts moves our nightly patient-data extract, so it deserves careful control.
- **Recommended action / status:** Fixed and verified. Every account has an owner, credentials were rotated or replaced with keyless access, and the vendor now uses individual logins.
- **Urgency:** Closed.

<a id="find-006"></a>
## FIND-006: Contractor access not bound to engagement term and scope
**Severity:** Moderate (L2 × I4 = 8) · **Status:** Closed · **Owner:** Sofia Ricci (Engineering Manager) · **Identified:** 2026-07-08 · **Source:** Access review
**Controls:** PS-7, AC-2 · **Risk:** RISK-002, RISK-004 · **POA&M:** [POAM-006](../poam/poam.md#poam-006) · **Related:** AR-EX-15, AR-EX-16, EVID-045, EVID-066

### Technical / GRC version
| | |
|---|---|
| **Condition** | One contractor remained active 22 days past the recorded contract end date while working under an extension that had not been documented. The same contractor had PHI production database access that the QA SOW did not require (QA uses staging with synthetic data). |
| **Criteria** | PS-7 (external personnel requirements and monitoring). ACP-002 §5.3 (contractor end dates enforced). Minimum necessary (HIPAA 164.502(b)). |
| **Cause** | Contractor end dates were not enforced in Okta, and access requests were not checked against SOW scope. |
| **Effect** | Contractor access can outlive or exceed the engagement, which increases PHI exposure through third-party personnel. |
| **Recommendation** | Set Okta account expiry equal to the SOW end date. Require SOW scope on contractor access requests. Send a monthly contractor roster to sponsors. |
| **Management response** | Agree. Target 2026-09-10. |

### Executive version
- **What happened:** A contractor's paperwork said their engagement had ended, even though they were still working, and they had access to patient data their job did not require.
- **Why it matters:** Contractors are a common source of excess access, and paperwork that does not match reality weakens every control built on it.
- **Business impact:** Low likelihood but meaningful patient-data exposure. Fixed without disruption to the contractor's work.
- **Recommended action / status:** Fixed and verified. Contractor accounts now expire automatically at the contract end date.
- **Urgency:** Closed.

<a id="find-007"></a>
## FIND-007: Segregation-of-duties conflict in vendor payment process
**Severity:** Moderate (L2 × I3 = 6) · **Status:** Risk Accepted · **Owner:** Laura Brenneman (Controller) · **Identified:** 2026-07-10 · **Source:** Access review
**Controls:** AC-5 · **Risk:** RISK-013 · **POA&M:** [POAM-007](../poam/poam.md#poam-007) · **Related:** AR-EX-17, EVID-014, EVID-015, EVID-060

### Technical / GRC version
| | |
|---|---|
| **Condition** | The Senior Accountant can both maintain vendor master data (including bank details) and approve payments up to $25,000 (SOD-01). A compensating control, a monthly vendor-master change report reviewed by the Controller, operated 6 of 6 months, but it was never formally documented as a risk decision. |
| **Criteria** | AC-5. Wrenfield internal-control policy (Board-approved) on payment SoD. |
| **Cause** | The finance team shrank to three people after the AP Specialist left in 2026-05. Duties were consolidated temporarily. |
| **Effect** | A single person could create or alter a vendor and approve payment to it, up to $25,000 per transaction. |
| **Recommendation** | Formally accept the risk with the compensating control and an expiry date, and redesign roles when the AP role is backfilled. Keep the callback verification of bank-detail changes. |
| **Management response** | Agree. RACC-001 signed by the CFO (risk owner) with CISO concurrence on 2026-08-12, expiring 2027-03-31. |

### Executive version
- **What happened:** In a small finance team, one person can both set up a vendor's bank details and approve payments to that vendor.
- **Why it matters:** This combination is the classic setup for payment fraud. It is common in small teams, which is why a compensating review exists.
- **Business impact:** Up to $25,000 per fraudulent payment before detection. The monthly independent review limits how long fraud could go undetected.
- **Recommended action / status:** Risk formally accepted by the CFO until 2027-03-31 with the independent monthly review in place. Roles will be split when the team is re-staffed.
- **Urgency:** Moderate. Tracked. Revisit at expiry or when the AP role is filled.

<a id="find-008"></a>
## FIND-008: Audit log retention below the 12-month contractual requirement
**Severity:** Moderate (L3 × I3 = 9) · **Status:** Closed · **Owner:** Owen Castillo (Security Engineer) · **Identified:** 2026-06-25 · **Source:** Control test
**Controls:** AU-11 · **Risk:** RISK-005 · **POA&M:** [POAM-008](../poam/poam.md#poam-008) · **Related:** EVID-024, EVID-067

### Technical / GRC version
| | |
|---|---|
| **Condition** | CloudTrail logs expired after 180 days. Application audit logs recording PHI access (who viewed which patient) were kept 90 days. SIEM hot retention was 90 days. |
| **Criteria** | SHCA CSA §4.1 requires 12 months (90 days searchable). HIPAA 164.312(b) audit controls. Customers' breach investigations need historical PHI-access records. |
| **Cause** | Retention was set in 2022 for cost reasons, before contractual requirements existed, and was never revisited. |
| **Effect** | If a breach were discovered late, which is common, Wrenfield could not show which patients' records were accessed. That could force broader breach notifications than necessary and would breach the SHCA contract. |
| **Recommendation** | Extend retention to 400 days via lifecycle tiering. Archive application audit logs to the log-archive account. Keep 90 days searchable in the SIEM. Add a quarterly oldest-record check. |
| **Management response** | Agree. Target 2026-09-15. |

### Executive version
- **What happened:** We kept records of who looked at patient data for only 3 to 6 months. The state contract requires 12.
- **Why it matters:** Breaches are often discovered months later. Without the records, we cannot prove which patients were or were not affected.
- **Business impact:** Over-notification of patients, regulatory exposure, and a direct contract violation.
- **Recommended action / status:** Fixed. Retention is extended to 13 months, and we confirmed older logs are no longer being deleted. Full proof comes with time, so this is re-checked next year.
- **Urgency:** Closed.

<a id="find-009"></a>
## FIND-009: Privileged-activity log reviews not consistently performed or documented
**Severity:** Moderate (L3 × I3 = 9) · **Status:** In Progress · **Owner:** Owen Castillo (Security Engineer) · **Identified:** 2026-06-26 · **Source:** Control test
**Controls:** AU-6 · **Risk:** RISK-005 · **POA&M:** [POAM-009](../poam/poam.md#poam-009) · **Related:** EVID-022, EVID-072

### Technical / GRC version
| | |
|---|---|
| **Condition** | The weekly privileged-activity review was performed in 19 of 26 weeks and fully effective in 17 of 26 (65%). Missed weeks coincided with a SIEM migration and reviewer PTO. Two reviews were marked "Reviewed" with flagged items left undispositioned. The review scope excluded local AWS IAM users. |
| **Criteria** | AU-6. LMS-004 §6 weekly review. HIPAA 164.308(a)(1)(ii)(D) information system activity review. |
| **Cause** | The review depends on one person with no backup reviewer, no escalation when a week is missed, and a report scope defined before local IAM users were known. |
| **Effect** | Misuse of privileged access, such as an admin creating a backdoor account, could go unnoticed for weeks. |
| **Recommendation** | Name a backup reviewer (the MDR under an SOW change). Auto-create the weekly ticket with escalation after 5 business days. Expand scope to all privileged principals. Require a disposition per flagged item. |
| **Management response** | Agree. Committed 2026-09-15; the MDR SOW change was delayed in procurement. |

### Executive version
- **What happened:** A weekly check of what our administrators did in production was skipped about 1 week in 4, usually when the one person responsible was away.
- **Why it matters:** This check is how we would notice an administrator account being misused.
- **Business impact:** Slower detection of insider misuse or a compromised admin account.
- **Recommended action / status:** Adding a backup reviewer (our 24/7 monitoring vendor) and automatic escalation. This is late because of a contract change.
- **Urgency:** Moderate. Now overdue. Escalated to the CISO for procurement follow-through.

<a id="find-010"></a>
## FIND-010: Vulnerability remediation exceeds contractual SLAs
**Severity:** High (L3 × I4 = 12) · **Status:** In Progress · **Owner:** Grace Lindqvist (VP Engineering) · **Identified:** 2026-06-29 · **Source:** Control test
**Controls:** SI-2 · **Risk:** RISK-006 · **POA&M:** [POAM-010](../poam/poam.md#poam-010) · **Related:** EVID-048, OBS-02, OBS-04

### Technical / GRC version
| | |
|---|---|
| **Condition** | 14 of 61 (23%) Critical and High vulnerabilities in H1 exceeded SLA. 6 remained open past SLA at 2026-06-30, including 2 Critical in the notify-worker container (end-of-life Node.js 16 and OpenSSL 1.1.1). 4 of the 6 are on unsupported hosts where no patch exists. No risk exceptions were filed. Engineering asserts the 2 Critical items are unreachable. |
| **Criteria** | SHCA CSA §7.1 (Critical 15 days, High 30 days). VM-003 §5 SLAs and §7 exception process. |
| **Cause** | End-of-life runtimes block patching, and the exception process is not used. Remediation work competes with feature work without SLA visibility. 7% of resources are untagged, which delays scan scoping. |
| **Effect** | Known exploitable weaknesses stay open longer than allowed, which increases the chance of compromise and breaches the contract. |
| **Recommendation** | Upgrade the notify-worker runtime. File documented exceptions with reachability analysis where they are justified. Add SLA dashboards to engineering planning. Enforce tag policy. Consider SI-2(7) root-cause analysis (new in Release 5.2.0) for repeat SLA misses. |
| **Management response** | Partially agree. Engineering disputes the 2 Critical ratings (no network-reachable path) but agrees the exception process must be used. Target 2026-11-05. |

**Challenge record (owner disputed):** Assessor position: exploitability may justify an exception, but only through the documented VM-003 §7 process with evidence (reachability analysis, compensating controls, CISO approval, and an expiry). An assertion in a meeting is not evidence. The determination stands. Management accepted this approach, and an exception request with reachability analysis is milestone M1.

### Executive version
- **What happened:** About 1 in 4 serious security flaws were fixed later than our contract allows. A few are still open, mostly on old systems that can no longer be patched.
- **Why it matters:** Attackers routinely exploit known, unpatched flaws. The state contract sets hard deadlines for fixing them.
- **Business impact:** Higher chance of compromise, plus a measurable contract-compliance gap that SHCA will see in our quarterly reports.
- **Recommended action / status:** Upgrade the outdated component, use the formal exception process where a flaw truly cannot be reached, and put fix deadlines in front of engineering leads every sprint.
- **Urgency:** High. Target 2026-11-05.

<a id="find-011"></a>
## FIND-011: Unsupported software components in the PHI data path
**Severity:** High (L3 × I4 = 12) · **Status:** Delayed · **Owner:** Tomasz Wierzbicki (Director, Platform Engineering) · **Identified:** 2026-06-26 · **Source:** Control test
**Controls:** SA-22 · **Risk:** RISK-007 · **POA&M:** [POAM-011](../poam/poam.md#poam-011) · **Related:** EVID-052, EVID-048, VR-012

### Technical / GRC version
| | |
|---|---|
| **Condition** | Three components are past vendor or community support: wf-sftp-01 (Windows Server 2012 R2, which pushes the nightly full-PHI extract to Quarrystone and receives 4 customer file drops), legacy-reports (PostgreSQL 11, which holds a PHI extract for monthly outcome reports), and notify-worker (Node.js 16). No SHCA-approved exception exists. |
| **Criteria** | SHCA CSA §7.4 (supported software only). SA-22. |
| **Cause** | Legacy integration components were never included in the platform modernization, and there is no lifecycle review of non-IaC assets. |
| **Effect** | Security flaws in these components will never be patched. They account for 4 of the 6 open past-SLA vulnerabilities. |
| **Recommendation** | Avoid the risk: replace wf-sftp-01 with a managed transfer service (encrypted, IaC-managed), migrate legacy-reports to the supported Aurora replica, and upgrade notify-worker. Keep compensating controls until then (EDR, allowlist, weekly scans, SSM-only admin). |
| **Management response** | Agree. Target 2026-11-05. Milestone 2 (SFTP migration) slipped from 2026-09-15 because 2 of 4 customers had not completed partner-side key exchange. Revised target 2026-12-15, approved by the CTO on 2026-09-12. |

### Executive version
- **What happened:** Three pieces of old software that the manufacturers no longer fix are still in use, including the server that sends our full patient dataset to an analytics vendor every night.
- **Why it matters:** Unpatchable software is a standing invitation to attackers, and the state contract prohibits it for their data.
- **Business impact:** This is the single biggest technical obstacle to SHCA go-live.
- **Recommended action / status:** Replace, do not patch. The migration is under way but has slipped about 3 months because some customers are slow to switch. Temporary protections are in place.
- **Urgency:** High. The migration must finish before SHCA data flows (target 2026-12-15, ahead of the 2027-01-11 go-live).

<a id="find-012"></a>
## FIND-012: Internet-exposed RDP on legacy host; CSPM alert not triaged
**Severity:** High (L4 × I4 = 16) · **Status:** Closed · **Owner:** Tomasz Wierzbicki (Director, Platform Engineering) · **Identified:** 2026-07-02 · **Source:** Control test
**Controls:** SC-7, CM-6 · **Risk:** RISK-012, RISK-007 · **POA&M:** [POAM-012](../poam/poam.md#poam-012) · **Related:** EVID-053, EVID-028, EVID-068, EVID-030

### Technical / GRC version
| | |
|---|---|
| **Condition** | The security group for wf-sftp-01 allowed RDP (TCP 3389) from 0.0.0.0/0 for 43 days. It was added under emergency change CHG-2026-0412 for a vendor support session, never approved, and never reverted. AWS Security Hub flagged it as High the next day, but no one triaged it. No successful external RDP logons were found (Windows event 4624 logon type 10 reviewed). |
| **Criteria** | SC-7 boundary protection. CM-6 deviation approval. CMP-006 emergency change rules. The Security Hub triage standard (High within 7 days). |
| **Cause** | The console change path bypasses IaC and approvals. Security Hub findings were not routed to the SRE on-call queue. |
| **Effect** | An unsupported Windows server holding PHI extracts was exposed to internet-wide RDP brute-force and exploitation. |
| **Recommendation** | Remove the rule (done within 24h). Route Security Hub High findings to on-call with an SLA. Add an SCP or guardrail that blocks 0.0.0.0/0 on admin ports. Tie emergency changes to automatic revert. |
| **Management response** | Agree. Remediated 2026-07-03 and validated 2026-07-10. |

### Executive version
- **What happened:** For six weeks, an old server holding patient data had a remote-login door open to the entire internet. It was opened for a support session and forgotten. An automated alert fired, but no one acted on it.
- **Why it matters:** Open remote-login ports on old Windows servers are one of the most common ransomware entry points.
- **Business impact:** Potential patient-data breach and ransomware entry. We found no evidence anyone got in.
- **Recommended action / status:** Closed within 24 hours of discovery. Alerts now go to the on-call engineer, and a guardrail blocks this type of rule.
- **Urgency:** Closed.

<a id="find-013"></a>
## FIND-013: Backup restoration never tested
**Severity:** Moderate (L2 × I4 = 8) · **Status:** Closed · **Owner:** Tomasz Wierzbicki (Director, Platform Engineering) · **Identified:** 2026-06-26 · **Source:** Control test
**Controls:** CP-9(1) · **Risk:** RISK-008 · **POA&M:** [POAM-013](../poam/poam.md#poam-013) · **Related:** EVID-035, EVID-069

### Technical / GRC version
| | |
|---|---|
| **Condition** | Backups are taken, protected, and copied cross-region (CP-9 satisfied), but no restore of the PHI database had ever been performed or documented. Backup job success was treated as proof of recoverability. |
| **Criteria** | CP-9(1). SHCA CSA §8.1 (tested restoration annually). HIPAA 164.308(a)(7)(ii)(D). |
| **Cause** | Recovery was assumed rather than tested. There was no scheduled restore exercise in the BC/DR plan. |
| **Effect** | In a ransomware or corruption event, recovery time and completeness were unknown. RTO and RPO were promises, not demonstrated capabilities. |
| **Recommendation** | Perform and document a restore from the DR vault into an isolated account, with timings and integrity checks. Schedule it semi-annually. |
| **Management response** | Agree. Target 2026-09-01. |

### Executive version
- **What happened:** We had backups, but we had never proven we could restore from them.
- **Why it matters:** Ransomware attacks often succeed because backups turn out to be unusable. A backup is only as good as its last successful restore.
- **Business impact:** Unknown recovery time for the platform clinicians depend on.
- **Recommended action / status:** Proven. On 2026-08-27 we restored the full patient database in 3 hours 41 minutes (target 4 hours) and lost only 11 minutes of data (target 1 hour). The test is now scheduled twice a year.
- **Urgency:** Closed.

<a id="find-014"></a>
## FIND-014: Incident response and contingency plans not tested within 12 months
**Severity:** Moderate (L3 × I3 = 9) · **Status:** In Progress · **Owner:** Owen Castillo (Security Engineer) · **Identified:** 2026-06-26 · **Source:** Control test
**Controls:** IR-3, CP-4 · **Risk:** RISK-009, RISK-008 · **POA&M:** [POAM-014](../poam/poam.md#poam-014) · **Related:** EVID-033, EVID-037, OBS-03

### Technical / GRC version
| | |
|---|---|
| **Condition** | The last IR tabletop was 2024-09-18, 21 months before fieldwork. There has been no plan-level contingency test (only 2024 engineering failover notes). The SHCA 24-hour incident-reporting path and the IR contact roster (2 departed staff) have never been exercised or validated. |
| **Criteria** | IR-3, CP-4, IRP-005 and BCP-003 (annual testing), SHCA CSA §5.2 and §8.1. |
| **Cause** | Exercises were deferred twice for delivery priorities, with no escalation. |
| **Effect** | Roles, decision rights, and notification timelines are untested. Real incidents were handled well (IR-4), but a major ransomware event would test untested paths. |
| **Recommendation** | Run a combined ransomware tabletop (IR + CP) including MDR, Legal/Privacy, Customer Ops, and executives. Update IRP-005 with the SHCA 24h step and the current roster. Track after-action items in the POA&M. |
| **Management response** | Agree. Tabletop scheduled 2026-10-14. Target 2026-11-15. |

### Executive version
- **What happened:** We have not practiced our incident response or disaster plans in almost two years, and the new state-contract requirement to report incidents within 24 hours has never been rehearsed.
- **Why it matters:** Teams that have not practiced lose critical hours in a real crisis, and the 24-hour clock does not wait.
- **Business impact:** Slower, more costly recovery and a risk of missing a contractual reporting deadline.
- **Recommended action / status:** An executive-level ransomware exercise is scheduled for 2026-10-14, followed by plan updates.
- **Urgency:** Moderate. Must be done before SHCA go-live.

<a id="find-015"></a>
## FIND-015: Third-party risk monitoring incomplete; no C-SCRM plan
**Severity:** Moderate (L3 × I3 = 9) · **Status:** In Progress · **Owner:** Beth Kowalski (Vendor Management Lead) · **Identified:** 2026-07-17 · **Source:** Control test (vendor program)
**Controls:** SR-6, SA-9, SR-2 · **Risk:** RISK-011, RISK-010 · **POA&M:** [POAM-015](../poam/poam.md#poam-015) · **Related:** EVID-049, EVID-059

### Technical / GRC version
| | |
|---|---|
| **Condition** | 5 of 14 Tier 1–2 vendors (36%) lack a current assessment, including Tier 1 Pulsewire Connect (last 2024-08) and Ironpeak MDR (never assessed after onboarding). No fourth-party (subcontractor) inventory exists. There is no supply chain risk management plan (outline only). 3 older contracts lack breach-notification timelines. |
| **Criteria** | SA-9, SR-6 (reassess at tier frequency), SR-2, TPRM-007, SHCA CSA §6.3 subcontractor inventory. |
| **Cause** | Vendor management is one person, part time. Reassessment is spreadsheet-tracked with no reminders, and the program was not resourced as the vendor count grew. |
| **Effect** | Vendor risks can drift unnoticed, as the Quarrystone offshore access (FIND-016) shows. |
| **Recommendation** | Clear the overdue assessments (Tier 1 first). Build a fourth-party inventory from vendor questionnaires. Approve a C-SCRM plan aligned to SP 800-161r1-upd1 and SP 800-18r2. Add contract-renewal triggers. |
| **Management response** | Agree. Target 2027-02-03 (Moderate SLA), with Tier 1 vendors by 2026-11-30. |

### Executive version
- **What happened:** About a third of our important vendors have not had a security check-up on schedule, and we do not track the companies our vendors themselves rely on.
- **Why it matters:** Many healthcare breaches start at a vendor. The state contract requires us to know and approve anyone who touches their data.
- **Business impact:** Unmanaged vendor risk, plus a contract obligation (subcontractor inventory) we cannot yet meet.
- **Recommended action / status:** Clear the backlog (critical vendors first), build the subcontractor inventory, and adopt a formal supply chain risk plan.
- **Urgency:** Moderate. Critical vendors by 2026-11-30.

<a id="find-016"></a>
## FIND-016: Quarrystone Analytics: offshore PHI access, inadequate breach-notification terms, and excessive data sharing
**Severity:** High (L3 × I5 = 15) · **Status:** In Progress · **Owner:** Dr. Miriam Castell (VP Clinical Analytics, business owner) · **Identified:** 2026-07-17 · **Source:** Vendor assessment
**Controls:** SA-9, SR-6 · **Risk:** RISK-010 · **POA&M:** [POAM-016](../poam/poam.md#poam-016) · **Related:** VR-001, VR-002, VR-003, VR-004, VR-005, VR-008, VR-010, EVID-050, EVID-051, EVID-073

### Technical / GRC version
| | |
|---|---|
| **Condition** | Quarrystone receives a nightly full-PHI extract (about 410k patients). (1) An undisclosed offshore subcontractor (Pune, India) had production access to Wrenfield PHI (VR-001, rated Critical, escalated to the CEO 2026-07-17; interim suspension confirmed 2026-07-24). (2) The BAA allows 30-day breach notice, against Wrenfield's 24h SHCA and 5-business-day customer obligations (VR-002). (3) The extract includes fields not needed for scoring: full address, phone, email, free-text notes (VR-003). Supporting issues: pentest evidence stale, data return undefined, secondary-use ambiguity. |
| **Criteria** | SHCA CSA §6.1 (US-only) and §6.3 (flow-down). HIPAA 164.502(b) minimum necessary and 164.314(a). 2 customer BAAs prohibit offshore access. SA-9. |
| **Cause** | The contract was signed in 2023 on the vendor's paper before TPRM-007 existed. The questionnaire relied on self-attestation. Data minimization was never designed into the extract. |
| **Effect** | Potential breach of 2 current customer BAAs and a blocking condition for SHCA. A breach at the vendor could go unreported to Wrenfield for up to 30 days. |
| **Recommendation** | Conditional continuation (Mitigate + Transfer): execute the amendment (US-only access with technical enforcement, 24h notification, subcontractor approval, data return and destruction within 30 days with a certificate, log cooperation). Minimize the extract to scoring-required fields with tokenized identifiers. Obtain a current pentest and retest. Do not send SHCA data until the conditions are met. |
| **Management response** | Agree. The CEO approved conditional continuation on 2026-07-22. The amendment is in redline v3. Target 2026-11-05. |

### Executive version
- **What happened:** The analytics vendor that receives our full patient dataset every night was letting an overseas subcontractor access it, which we did not know about. Their contract also allows them to wait 30 days before telling us about a breach.
- **Why it matters:** Two current customer contracts forbid offshore access, the state contract requires US-only handling, and we must report incidents to the state within 24 hours. A 30-day vendor delay makes that impossible.
- **Business impact:** Possible breach of current customer contracts today, and a hard stop for the SHCA contract ($23.4M) if not fixed.
- **Recommended action / status:** Offshore access was suspended within a week of discovery. Contract changes (US-only, 24-hour notice) are in negotiation. We will stop sending data the vendor does not need. No state data will be shared until all conditions are met.
- **Urgency:** High. Conditions must be met before SHCA go-live. CEO-level visibility.

<a id="find-017"></a>
## FIND-017: System security plan outdated and overstates control implementation
**Severity:** Low (L2 × I2 = 4) · **Status:** In Progress · **Owner:** Priya Raman (Security Compliance Manager) · **Identified:** 2026-07-14 · **Source:** Control test
**Controls:** PL-2 · **Risk:** RISK-016 · **POA&M:** [POAM-017](../poam/poam.md#poam-017) · **Related:** EVID-041, OBS-01

### Technical / GRC version
| | |
|---|---|
| **Condition** | SSP v1.3 (2025-02) predates the EKS migration, the log-archive account, and the Quarrystone SFTP flow, and it states a higher implementation status than testing supports for 27 of the 61 in-scope controls. |
| **Criteria** | PL-2. SHCA CSA §2.1 (current SSP expected with the assessment package). |
| **Cause** | The SSP was maintained as a SOC 2 narrative, with no update trigger tied to architecture changes. |
| **Effect** | SHCA and customers would receive an inaccurate description of the system, a credibility and contractual risk rather than a direct technical one. |
| **Recommendation** | Rewrite the SSP in control-by-control form using this matrix as the source. Adopt the SP 800-18 Rev. 2 structure. Add architecture-change triggers to the change process. |
| **Management response** | Agree. Target 2026-12-15. |

### Executive version
- **What happened:** Our main security document describing the system is out of date and, in places, describes protections as working when they were not.
- **Why it matters:** The state and our customers rely on this document, so it has to be accurate.
- **Business impact:** Credibility and contract risk, not a direct security exposure.
- **Recommended action / status:** Rewrite it from this assessment's verified results, and update it whenever the architecture changes.
- **Urgency:** Low. Needed for the SHCA package by 2026-12-15.

<a id="find-018"></a>
## FIND-018: Emergency and console changes bypass approval
**Severity:** Moderate (L3 × I3 = 9) · **Status:** In Progress · **Owner:** Tomasz Wierzbicki (Director, Platform Engineering) · **Identified:** 2026-06-29 · **Source:** Control test
**Controls:** CM-3 · **Risk:** RISK-014 · **POA&M:** [POAM-018](../poam/poam.md#poam-018) · **Related:** EVID-030

### Technical / GRC version
| | |
|---|---|
| **Condition** | 3 of 25 sampled changes failed. CHG-2026-0412 (emergency, no approval, never reverted, which caused FIND-012). CHG-2026-0288 (retro approval after 9 business days against a standard of 2). CHG-2026-0356 (deployed 5h38m before approval was recorded). 2 of the 3 emergency changes in the sample failed. |
| **Criteria** | CM-3. CMP-006 §4.3. SOC 2 CC8.1 commitment. |
| **Cause** | The code pipeline enforces review, but the console and emergency paths rely on people remembering. No report flags emergency changes awaiting retro approval. |
| **Effect** | Unreviewed changes can introduce outages or security regressions, as FIND-012 shows. |
| **Recommendation** | Auto-open a retro-approval task on every emergency change with a 2-day escalation. Alert on console changes to security groups and IAM (CloudTrail + EventBridge). Require approval before the deploy job runs. |
| **Management response** | Agree. Committed 2026-09-11. Milestone 1 is done; milestones 2 and 3 are waiting on an SRE backlog slot. |

### Executive version
- **What happened:** Most production changes go through a strict approval process, but urgent fixes and manual console changes sometimes skip it. One of those created the exposure in FIND-012.
- **Why it matters:** Unapproved changes are a common cause of both outages and security holes.
- **Business impact:** Moderate. The main risk is repeats of FIND-012.
- **Recommended action / status:** Automatic follow-up on every emergency change, and alerts on risky manual changes.
- **Urgency:** Moderate. Now overdue, so it needs a scheduling decision from the CTO.

<a id="find-019"></a>
## FIND-019: Security awareness training completion below 100%
**Severity:** Low (L2 × I2 = 4) · **Status:** Completed – Pending Validation · **Owner:** Denise Yamamoto (Director of People) · **Identified:** 2026-06-26 · **Source:** Control test
**Controls:** AT-2 · **Risk:** RISK-015 · **POA&M:** [POAM-019](../poam/poam.md#poam-019) · **Related:** EVID-019, EVID-070

### Technical / GRC version
| | |
|---|---|
| **Condition** | 316 of 347 workforce members (91%) completed annual training. 31 were overdue, 4 of them with PHI data-store access. The policy's access-suspension step for users more than 30 days overdue was not enforced. |
| **Criteria** | AT-2. HIPAA 164.308(a)(5)(i). Training policy HR-011. |
| **Cause** | Overdue reminders went to users only, with no manager escalation or enforcement. |
| **Effect** | A small increase in phishing and data-handling risk. Mainly a compliance gap. |
| **Recommendation** | Enforce the suspension step via an Okta group rule. Escalate to managers at 14 days. Report completion monthly. |
| **Management response** | Agree. Enforcement live 2026-08-20; 344 of 347 complete as of 2026-09-12, with 3 on leave. |

### Executive version
- **What happened:** About 1 in 11 staff had not completed required annual security training.
- **Why it matters:** Training is a regulatory requirement and our first defense against phishing.
- **Business impact:** Low. A compliance gap more than a direct risk.
- **Recommended action / status:** Overdue users now lose access until they complete it. Completion is at 99%, with the rest on leave.
- **Urgency:** Low. Final verification in progress.

## Observations
| ID | Control | Observation |
|---|---|---|
| OBS-01 | AC-1 | Access Control Policy annual review overdue by about 5 months; draft v3.2 in approval. Recommend: approve by 2026-10-31 and add a policy-review calendar to the GRC tracker. |
| OBS-02 | CM-8 | 7% of EC2/EKS resources lack owner tags, delaying host-scan coverage by 1-3 weeks. Recommend: enforce tag policy with an SCP deny on untagged launches (tracked as POAM-010 milestone M4). |
| OBS-03 | IR-8 | IR plan contact roster lists 2 departed staff and lacks the SHCA 24h notification step. Addressed in POAM-014 milestone M1. |
| OBS-04 | SI-2 | SI-02(07) Root Cause Analysis (new in SP 800-53 Release 5.2.0; not in the Moderate baseline) recommended as optional FY27 tailoring given repeated patch-SLA misses on container base images. |
| OBS-05 | CA-7 | No written ISCM strategy, although monitoring operates. Recommend: document the strategy using the metric definitions in dashboard/metric-definitions.md as the starting point. |
| OBS-06 | PM-9 | Risk appetite statement lacks explicit third-party risk tolerance (for example, maximum Tier 1 vendors overdue for reassessment). Recommend adding it at the next Board review. |
