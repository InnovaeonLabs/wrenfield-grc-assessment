# Enterprise Cybersecurity Risk Register

> Generated from `data/*.yaml` by `tools/build.py`. Edit the data, not this file.

Workbook with live formulas: [risk-register.xlsx](risk-register.xlsx) · CSV: [risk-register.csv](risk-register.csv) · Method: [risk-methodology.md](risk-methodology.md) (approved **before** scoring)

Status date 2026-09-18. 18 risks.

## Rating distribution: inherent → current → residual
| State | Critical | High | Moderate | Low |
|---|---|---|---|---|
| Inherent | 6 | 11 | 1 | 0 |
| Current | 0 | 14 | 3 | 1 |
| Residual | 0 | 0 | 15 | 3 |

No risk reaches zero. Residual ratings reflect the target after treatment. Risks stay open until the POA&M item is validated.

## Heat map: current risk (as tested)
| Likelihood ↓ / Impact → | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** |  |  |  |  |  |
| **4** |  |  | H: R004 | H: R002 |  |
| **3** |  |  | M: R015 | H: R005, R006, R007, R009, R011, R016, R017 | H: R001, R003, R010 |
| **2** |  | L: R018 | M: R013 | M: R014 | H: R008, R012 |
| **1** |  |  |  |  |  |

## Heat map: residual risk (target)
| Likelihood ↓ / Impact → | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** |  |  |  |  |  |
| **4** |  |  |  |  |  |
| **3** |  |  | M: R015 |  |  |
| **2** |  | L: R018 | M: R004, R005, R009, R013, R014, R016 | M: R001, R002, R003, R006, R008, R010, R011, R012 |  |
| **1** |  |  |  | L: R007, R017 |  |

## Register
| ID | Risk | Inherent | Current | Treatment | Residual | Owner | Status | POA&M |
|---|---|---|---|---|---|---|---|---|
| RISK-001 | Privileged cloud or identity admin account misused or compromised | 20 Critical | 15 High | Mitigate | 8 Moderate | Samir Haddad | Treatment in progress | POAM-003 |
| RISK-002 | Unauthorized access by former employees or contractors | 16 High | 16 High | Mitigate | 8 Moderate | Alicia Moreno | Treated (residual achieved; monitoring) | POAM-001, POAM-006 |
| RISK-003 | Account takeover through MFA gaps | 20 Critical | 15 High | Mitigate | 8 Moderate | Alicia Moreno | Treated (residual achieved; monitoring) | POAM-002 |
| RISK-004 | Access creep from ineffective recertification | 12 High | 12 High | Mitigate | 6 Moderate | Alicia Moreno | Treatment in progress | POAM-004 |
| RISK-005 | Inability to detect or investigate PHI access | 12 High | 12 High | Mitigate | 6 Moderate | Alicia Moreno | Treatment in progress | POAM-008, POAM-009 |
| RISK-006 | Exploitation of unremediated vulnerabilities | 20 Critical | 12 High | Mitigate | 8 Moderate | Grace Lindqvist | Treatment in progress | POAM-010 |
| RISK-007 | Compromise of unsupported legacy components in the PHI path | 16 High | 12 High | Avoid | 4 Low | Samir Haddad | Treatment in progress (delayed) | POAM-011, POAM-012 |
| RISK-008 | Failed or slow recovery from ransomware or data corruption | 15 High | 10 High | Mitigate | 8 Moderate | Samir Haddad | Treatment in progress | POAM-013, POAM-014 |
| RISK-009 | Delayed or ineffective response to a major incident | 12 High | 12 High | Mitigate | 6 Moderate | Alicia Moreno | Treatment in progress | POAM-014 |
| RISK-010 | PHI exposure through the analytics vendor (Quarrystone) | 20 Critical | 15 High | Mitigate | 8 Moderate | Dr. Miriam Castell | Treatment in progress | POAM-016, POAM-015 |
| RISK-011 | Software or vendor supply-chain compromise | 15 High | 12 High | Mitigate | 8 Moderate | Beth Kowalski | Treatment in progress | POAM-015 |
| RISK-012 | Cloud misconfiguration exposing PHI or admin services | 20 Critical | 10 High | Mitigate | 8 Moderate | Tomasz Wierzbicki | Treatment in progress | POAM-012 |
| RISK-013 | Fraudulent vendor payment through an SoD conflict | 9 Moderate | 6 Moderate | Accept | 6 Moderate | Raymond Okafor | Accepted (RACC-001, expires 2027-03-31) | POAM-007 |
| RISK-014 | Unauthorized or untested changes cause an outage or security regression | 12 High | 8 Moderate | Mitigate | 6 Moderate | Tomasz Wierzbicki | Treatment in progress (overdue) | POAM-018 |
| RISK-015 | Phishing and social engineering of the workforce | 20 Critical | 9 Moderate | Accept | 9 Moderate | Denise Yamamoto | Accepted within tolerance (monitor) | POAM-019 |
| RISK-016 | Loss of SHCA contract or customer trust from unresolved compliance gaps | 15 High | 12 High | Mitigate | 6 Moderate | Elena Marsh | Treatment in progress | POAM-017 |
| RISK-017 | Service-account credential theft | 12 High | 12 High | Mitigate | 4 Low | Alicia Moreno | Treated (residual achieved; monitoring) | POAM-005 |
| RISK-018 | Loss or theft of an endpoint containing PHI | 12 High | 4 Low | Accept | 4 Low | Kevin Brandt | Accepted within appetite (Low) | — |

## Scoring rationale (inherent → control → residual)
### RISK-001: Privileged cloud or identity admin account misused or compromised
*An attacker phishes or steals the session of a user holding production AdministratorAccess, Okta Super Admin, or GitHub owner, then exfiltrates PHI or destroys infrastructure.*

| Field | Value |
|---|---|
| Asset / process | AWS wcp-prod admin plane, Okta tenant, GitHub org |
| Threat → vulnerability | External actor (phishing, session-token theft) or malicious/negligent insider → Excess admin grants; admin performed from daily-use accounts; no JIT elevation |
| Existing controls | Okta SSO+MFA for most users; CloudTrail and GuardDuty; MDR 24x7; Vault Lock on backups |
| **Inherent** | L4 × I5 = **20 Critical**: L4: identity-based intrusion is the dominant cloud attack path. I5: admin reaches all PHI (>50k records) and can cause an outage over 24h. |
| **Current** (as tested) | L3 × I5 = **15 High**: L3: MFA and monitoring raise attacker effort, but 6 unjustified or daily-account admin assignments existed. I5 unchanged: any admin can still reach everything. |
| **Treatment** | Mitigate: Remove excess grants; -adm accounts; JIT elevation; GitHub owner cap (POAM-003) |
| **Residual** (target) | L2 × I4 = **8 Moderate**: L2: -adm accounts with phishing-resistant MFA plus approval-gated JIT elevation. I4: time-boxed sessions and Vault Lock limit destructive impact and dwell time, but exfiltration during a session is still possible. |
| Owner · target · status | Samir Haddad (CTO) · 2026-11-05 · Treatment in progress |
| Links | Controls AC-6, AC-6(2), AC-6(5), IA-2(1) · Findings FIND-003 · POA&M POAM-003 |

### RISK-002: Unauthorized access by former employees or contractors
*A departed worker's still-active account is used, by them or by an attacker, to access PHI or financial systems.*

| Field | Value |
|---|---|
| Asset / process | All in-scope systems, including Ledgerline and the vendor portal |
| Threat → vulnerability | Former workforce member (disgruntled or careless), or an attacker using an orphaned account → Manual de-provisioning; local accounts outside SSO; contractor end dates not enforced |
| Existing controls | Okta deactivation by IT ticket; asset recovery at exit |
| **Inherent** | L4 × I4 = **16 High**: L4: turnover of about 38/year plus contractors, and orphaned accounts are a well-known misuse path. I4: AWS admin or PHI DB access affects 500–50,000+ records; limited by role mix. |
| **Current** (as tested) | L4 × I4 = **16 High**: L4 unchanged: the control failed testing (2 of 19 not disabled, 1 post-termination sign-in, local admin account active 95 days) and earns no credit. I4. |
| **Treatment** | Mitigate: HR-to-Okta reconciliation with auto-ticketing; contractor expiry; local-account cleanup (POAM-001, POAM-006) |
| **Residual** (target) | L2 × I4 = **8 Moderate**: L2: daily reconciliation job, contractor account expiry, and a local-account inventory, validated 7 of 7. I4 unchanged: a missed account could still reach sensitive data. |
| Owner · target · status | Alicia Moreno (CISO) · 2026-09-10 · Treated (residual achieved; monitoring) |
| Links | Controls AC-2, AC-2(1), AC-2(3), PS-4, PS-7 · Findings FIND-001, FIND-006 · POA&M POAM-001, POAM-006 |

### RISK-003: Account takeover through MFA gaps
*An attacker obtains the password of an MFA-exempt account and signs in directly, inheriting that user's access, including identity administration.*

| Field | Value |
|---|---|
| Asset / process | Okta and all federated systems |
| Threat → vulnerability | Credential phishing, password spraying, reuse of breached credentials → MFA exemption group (9 humans incl. an Okta Super Admin); IAM user without MFA |
| Existing controls | Global MFA policy for 97% of users; replay-resistant authenticators; Okta ThreatInsight |
| **Inherent** | L4 × I5 = **20 Critical**: L4: phishing is the leading initial-access vector. I5: federation reaches AWS prod and PHI. |
| **Current** (as tested) | L3 × I5 = **15 High**: L3: MFA covers 97%, a partial control. I5: an exempt Okta Super Admin could reach everything. |
| **Treatment** | Mitigate: Delete the exemption policy; enroll all users; phishing-resistant admin MFA; exception workflow (POAM-002) |
| **Residual** (target) | L2 × I4 = **8 Moderate**: L2: no exemptions; phishing-resistant MFA for admins; token theft still possible. I4: least-privilege work narrows what one account reaches. |
| Owner · target · status | Alicia Moreno (CISO) · 2026-09-05 · Treated (residual achieved; monitoring) |
| Links | Controls IA-2(1), IA-2(2), IA-2(8) · Findings FIND-002 · POA&M POAM-002 |

### RISK-004: Access creep from ineffective recertification
*Users accumulate access beyond need over time, increasing the blast radius of any compromise or misuse.*

| Field | Value |
|---|---|
| Asset / process | Privileged and PHI entitlements across 9 systems |
| Threat → vulnerability | Insider misuse; attacker leveraging over-privileged accounts → Rubber-stamp reviews; privileged systems out of review scope; no re-baseline on transfer |
| Existing controls | Quarterly Okta app certification (limited scope) |
| **Inherent** | L4 × I3 = **12 High**: L4: fast growth, transfers, and contractors make creep near-certain without review. I3: creep usually adds read access; worst credible case is fewer than 500 records. |
| **Current** (as tested) | L4 × I3 = **12 High**: L4: the review operated but was ineffective (100% approval, key systems excluded), so no credit. I3. |
| **Treatment** | Mitigate: Redesign certifications; transfer-triggered review (POAM-004) |
| **Residual** (target) | L2 × I3 = **6 Moderate**: L2: full-scope campaigns with usage data and flagged items needing rationale. I3. |
| Owner · target · status | Alicia Moreno (CISO) · 2026-10-31 · Treatment in progress |
| Links | Controls AC-6(7), AC-2, PS-5 · Findings FIND-004, FIND-006 · POA&M POAM-004 |

### RISK-005: Inability to detect or investigate PHI access
*Misuse goes unnoticed, or a breach found months later cannot be scoped, forcing presumptive notification of large patient populations.*

| Field | Value |
|---|---|
| Asset / process | Audit logs (CloudTrail, application PHI-access audit, SIEM) |
| Threat → vulnerability | Undetected insider or attacker activity; late-discovered breach → 90–180-day retention; inconsistent privileged-activity review |
| Existing controls | Comprehensive event logging (AU-2); immutable log archive (AU-9); MDR alerting (SI-4) |
| **Inherent** | L3 × I4 = **12 High**: L3: breaches are often discovered after 90+ days. I4: inability to scope means broad notification plus contract breach. |
| **Current** (as tested) | L3 × I4 = **12 High**: L3: logging is strong, but retention is short and 35% of weekly reviews were missed or incomplete. I4. |
| **Treatment** | Mitigate: Extend retention (POAM-008, done); backup reviewer and escalation (POAM-009) |
| **Residual** (target) | L2 × I3 = **6 Moderate**: L2: 400-day retention plus a backup reviewer. I3: records now exist to scope and limit notification. |
| Owner · target · status | Alicia Moreno (CISO) · 2026-10-31 · Treatment in progress |
| Links | Controls AU-6, AU-11, AU-2, AU-9 · Findings FIND-008, FIND-009 · POA&M POAM-008, POAM-009 |

### RISK-006: Exploitation of unremediated vulnerabilities
*An attacker exploits a known, unpatched flaw in a production service or host to gain a foothold.*

| Field | Value |
|---|---|
| Asset / process | Internet-facing services and container workloads |
| Threat → vulnerability | Opportunistic exploitation of known CVEs; ransomware affiliates → 23% SLA misses; end-of-life runtimes; exception process unused |
| Existing controls | WAF; weekly authenticated scanning; container image scanning; EDR; MDR |
| **Inherent** | L4 × I5 = **20 Critical**: L4: exploitation of known vulnerabilities is a top initial-access vector. I5: PHI platform compromise. |
| **Current** (as tested) | L3 × I4 = **12 High**: L3: scanning, WAF, and EDR are effective layers, but 6 items are open past SLA. I4: segmentation (private subnets) limits the blast radius from most workloads. |
| **Treatment** | Mitigate: Upgrade EOL runtimes; exception process; SLA reporting; tag enforcement (POAM-010) |
| **Residual** (target) | L2 × I4 = **8 Moderate**: L2: SLA adherence with governed exceptions. I4: same architecture. |
| Owner · target · status | Grace Lindqvist (VP Engineering) · 2026-11-05 · Treatment in progress |
| Links | Controls RA-5, SI-2, CM-8 · Findings FIND-010 · POA&M POAM-010 |

### RISK-007: Compromise of unsupported legacy components in the PHI path
*An attacker exploits an unpatchable flaw on the legacy SFTP host, which holds the nightly full-PHI extract, and pivots or exfiltrates.*

| Field | Value |
|---|---|
| Asset / process | wf-sftp-01 (Windows 2012 R2), legacy-reports (PostgreSQL 11), notify-worker (Node 16) |
| Threat → vulnerability | Exploitation of unpatchable flaws; ransomware → No vendor patches; host previously exposed via internet-facing RDP |
| Existing controls | EDR; SFTP source allowlist; weekly scanning; SSM-only admin (after FIND-012 fix) |
| **Inherent** | L4 × I4 = **16 High**: L4: unsupported, internet-reachable Windows host. I4: a full-PHI extract sits there transiently (worst credible case is one night's file, bounded). |
| **Current** (as tested) | L3 × I4 = **12 High**: L3: RDP closed, allowlist and EDR in place, but no patches. I4. |
| **Treatment** | Avoid: Decommission wf-sftp-01 and legacy-reports; upgrade notify-worker (POAM-011) |
| **Residual** (target) | L1 × I4 = **4 Low**: L1: components decommissioned (Avoid). I4 kept, because the managed-transfer replacement still moves the same data. |
| Owner · target · status | Samir Haddad (CTO) · 2026-12-15 · Treatment in progress (delayed) |
| Links | Controls SA-22, SC-7, CM-6, SI-2 · Findings FIND-011, FIND-012 · POA&M POAM-011, POAM-012 |

### RISK-008: Failed or slow recovery from ransomware or data corruption
*A destructive event forces recovery, and recovery takes longer than RTO or loses data because the process was never exercised.*

| Field | Value |
|---|---|
| Asset / process | wcp-core-db and WCP services |
| Threat → vulnerability | Ransomware; destructive insider; data corruption → Restore never tested (at fieldwork); contingency plan untested |
| Existing controls | PITR (35 days); cross-region, cross-account backups with Vault Lock; BC/DR plan |
| **Inherent** | L3 × I5 = **15 High**: L3: healthcare ransomware frequency. I5: outage over 24h for clinical workflows. |
| **Current** (as tested) | L2 × I5 = **10 High**: L2: strong, immutable backups reduce the chance of an unrecoverable event. I5: recovery time was unproven. |
| **Treatment** | Mitigate: Semi-annual restore tests (POAM-013, done); CP exercise (POAM-014) |
| **Residual** (target) | L2 × I4 = **8 Moderate**: L2. I4: restore proven at 3h41m (within the 4h RTO); a full contingency exercise is pending (POAM-014). |
| Owner · target · status | Samir Haddad (CTO) · 2026-11-15 · Treatment in progress |
| Links | Controls CP-2, CP-4, CP-9, CP-9(1) · Findings FIND-013, FIND-014 · POA&M POAM-013, POAM-014 |

### RISK-009: Delayed or ineffective response to a major incident
*During a major incident, unclear roles or notification steps delay containment or cause a missed contractual or regulatory notification deadline.*

| Field | Value |
|---|---|
| Asset / process | Incident response capability and notification obligations |
| Threat → vulnerability | Major incident (ransomware, large PHI breach) stressing untested processes → No IR exercise in 21 months; SHCA 24h path never rehearsed |
| Existing controls | IRP-005 (current); 24x7 MDR; incidents in H1 handled well (IR-4 satisfied) |
| **Inherent** | L3 × I4 = **12 High**: L3: at least one significant incident per year is plausible. I4: missed notification means a contract breach and regulatory scrutiny. |
| **Current** (as tested) | L3 × I4 = **12 High**: L3: good day-to-day handling, but major-incident paths are untested. I4. |
| **Treatment** | Mitigate: Ransomware tabletop and plan update (POAM-014) |
| **Residual** (target) | L2 × I3 = **6 Moderate**: L2: rehearsed plan with the SHCA step. I3: faster, coordinated response limits impact. |
| Owner · target · status | Alicia Moreno (CISO) · 2026-11-15 · Treatment in progress |
| Links | Controls IR-3, IR-4, IR-6, IR-8 · Findings FIND-014 · POA&M POAM-014 |

### RISK-010: PHI exposure through the analytics vendor (Quarrystone)
*A breach at Quarrystone or its offshore subcontractor exposes Wrenfield PHI, and notice arrives too late for Wrenfield to meet 24h or 5-day obligations.*

| Field | Value |
|---|---|
| Asset / process | Nightly full-PHI extract (about 410k patients) processed by Quarrystone and its subcontractors |
| Threat → vulnerability | Vendor or subcontractor breach; unauthorized offshore access; delayed breach notice → Offshore subcontractor access; 30-day notice term; excess data fields; stale pentest |
| Existing controls | BAA; SOC 2 Type II (unqualified); encryption in transit and at rest; interim suspension of offshore access (2026-07-24) |
| **Inherent** | L4 × I5 = **20 Critical**: L4: third-party breaches are frequent in healthcare, and an undisclosed offshore party was present. I5: >50k records plus SHCA contract loss. |
| **Current** (as tested) | L3 × I5 = **15 High**: L3: vendor controls are generally mature (SOC 2, encryption) and offshore access is suspended, but the contract terms are unchanged. I5. |
| **Treatment** | Mitigate: Contract amendment; data minimization; pentest and retest; monitoring plan (POAM-016). Transfer (partial) through cyber insurance and vendor indemnity. |
| **Residual** (target) | L2 × I4 = **8 Moderate**: L2: contractual US-only with technical enforcement, 24h notice, and current pentest. I4: minimized extract (no contact details or free text) reduces the records and sensitivity exposed. |
| Owner · target · status | Dr. Miriam Castell (VP Clinical Analytics) · 2026-11-05 · Treatment in progress |
| Links | Controls SA-9, SR-6, CA-3 · Findings FIND-016, FIND-015 · POA&M POAM-016, POAM-015 |

### RISK-011: Software or vendor supply-chain compromise
*A compromised dependency or vendor integration introduces malicious code or access into WCP.*

| Field | Value |
|---|---|
| Asset / process | CI/CD pipeline, open-source dependencies, vendor integrations |
| Threat → vulnerability | Malicious dependency or compromised vendor update or integration → No C-SCRM plan; no fourth-party inventory; 5 vendors overdue for review |
| Existing controls | Dependency scanning; branch protection and required review; OIDC deploy (no static keys); pinned base images |
| **Inherent** | L3 × I5 = **15 High**: L3: supply-chain attacks are increasing. I5: code execution in the PHI platform. |
| **Current** (as tested) | L3 × I4 = **12 High**: L3: good pipeline hygiene, but no program-level supply chain risk management. I4: OIDC and least-privilege deploy roles limit what a compromised pipeline can reach. |
| **Treatment** | Mitigate: C-SCRM plan; clear the vendor backlog; fourth-party inventory (POAM-015) |
| **Residual** (target) | L2 × I4 = **8 Moderate**: L2: C-SCRM plan, current vendor reviews, fourth-party visibility. I4. |
| Owner · target · status | Beth Kowalski (Vendor Management Lead) · 2027-02-03 · Treatment in progress |
| Links | Controls SR-2, SR-6, SA-9 · Findings FIND-015 · POA&M POAM-015 |

### RISK-012: Cloud misconfiguration exposing PHI or admin services
*A manual misconfiguration (an open port, a public resource) exposes PHI or an admin interface to the internet.*

| Field | Value |
|---|---|
| Asset / process | AWS wcp-prod network and storage configuration |
| Threat → vulnerability | Opportunistic internet scanning; misconfiguration exploited by attackers → Console changes bypass IaC; CSPM findings not routed to on-call |
| Existing controls | Org-wide S3 Block Public Access (SCP); encryption by default; Security Hub CIS checks; IaC for most resources |
| **Inherent** | L4 × I5 = **20 Critical**: L4: misconfiguration is a leading cloud breach cause. I5: public PHI exposure. |
| **Current** (as tested) | L2 × I5 = **10 High**: L2: strong preventive guardrails for data stores (block public access, encryption). The observed exposure was an admin port, not data. I5: remains the worst credible case. |
| **Treatment** | Mitigate: Route CSPM to on-call; admin-port guardrail; emergency change auto-revert (POAM-012, POAM-018) |
| **Residual** (target) | L2 × I4 = **8 Moderate**: L2: CSPM routed to on-call plus SCP guardrails on admin ports. I4: guardrails prevent the most severe (data-store) exposures. |
| Owner · target · status | Tomasz Wierzbicki (Director, Platform Engineering) · 2026-09-11 · Treatment in progress |
| Links | Controls CM-2, CM-6, SC-7, SC-28 · Findings FIND-012 · POA&M POAM-012 |

### RISK-013: Fraudulent vendor payment through an SoD conflict
*A user alters vendor bank details and approves payments to an attacker-controlled account.*

| Field | Value |
|---|---|
| Asset / process | Ledgerline vendor master and payments |
| Threat → vulnerability | Insider fraud or coerced insider (business email compromise) → One user holds vendor-master maintenance and payment approval (≤ $25k) |
| Existing controls | Compensating: monthly vendor-master change report reviewed by the Controller; callback verification of bank-detail changes; payments over $25k need CFO approval |
| **Inherent** | L3 × I3 = **9 Moderate**: L3: BEC-driven bank-change fraud is common. I3: bounded by the $25k approval limit and monthly detection (worst credible case $100k–500k over a month). |
| **Current** (as tested) | L2 × I3 = **6 Moderate**: L2: the compensating review operated 6 of 6 months, plus callbacks. I3. |
| **Treatment** | Accept: RACC-001 risk acceptance with compensating control; split roles at AP backfill (POAM-007) |
| **Residual** (target) | L2 × I3 = **6 Moderate**: L2. I3: accepted with the compensating control until the roles are split. |
| Owner · target · status | Raymond Okafor (CFO) · 2027-03-31 · Accepted (RACC-001, expires 2027-03-31) |
| Links | Controls AC-5 · Findings FIND-007 · POA&M POAM-007 |

### RISK-014: Unauthorized or untested changes cause an outage or security regression
*An emergency or console change is made without review and introduces an outage or exposure (FIND-012 is a realized example).*

| Field | Value |
|---|---|
| Asset / process | WCP production configuration |
| Threat → vulnerability | Human error under time pressure; unreviewed emergency changes → Emergency and console change paths lack enforced approval and revert |
| Existing controls | PR review and CI for code and IaC; protected deploy environments |
| **Inherent** | L3 × I4 = **12 High**: L3: frequent changes. I4: multi-hour outage or exposure. |
| **Current** (as tested) | L2 × I4 = **8 Moderate**: L2: 22 of 25 sampled changes were compliant; the pipeline is strong. I4: realized once (FIND-012). |
| **Treatment** | Mitigate: Retro-approval automation; console-change alerts (POAM-018) |
| **Residual** (target) | L2 × I3 = **6 Moderate**: L2. I3: console-change alerting and auto-revert shorten the exposure window. |
| Owner · target · status | Tomasz Wierzbicki (Director, Platform Engineering) · 2026-09-11 · Treatment in progress (overdue) |
| Links | Controls CM-3 · Findings FIND-018 · POA&M POAM-018 |

### RISK-015: Phishing and social engineering of the workforce
*A user is tricked into disclosing credentials, approving a push, or sending PHI or payments to an attacker.*

| Field | Value |
|---|---|
| Asset / process | Workforce identities and endpoints |
| Threat → vulnerability | Phishing, help-desk social engineering, BEC → 9% training non-completion (at fieldwork); human error |
| Existing controls | MFA with number challenge; email security; phishing simulations (4.3% click rate); help-desk identity verification; EDR |
| **Inherent** | L5 × I4 = **20 Critical**: L5: phishing attempts are constant. I4: credential compromise leading to PHI access. |
| **Current** (as tested) | L3 × I3 = **9 Moderate**: L3: layered controls (MFA, filtering, EDR) catch most attempts (INC-2026-0012 shows MFA blocked a successful phish). I3: least privilege and monitoring limit impact. |
| **Treatment** | Accept: Training enforcement (POAM-019); continue simulations and phishing-resistant MFA rollout |
| **Residual** (target) | L3 × I3 = **9 Moderate**: L3 and I3 unchanged: training completion is a hygiene fix and does not move the risk. Accepted as within tolerance (Moderate) with an ongoing awareness program. |
| Owner · target · status | Denise Yamamoto (Director of People) · 2026-09-30 · Accepted within tolerance (monitor) |
| Links | Controls AT-2, AT-3, IA-2(8) · Findings FIND-019 · POA&M POAM-019 |

### RISK-016: Loss of SHCA contract or customer trust from unresolved compliance gaps
*SHCA or Lakemont judges Wrenfield's remediation insufficient, delaying go-live or leading to termination or non-renewal.*

| Field | Value |
|---|---|
| Asset / process | SHCA C3P contract ($23.4M) and top customer relationships (Lakemont) |
| Threat → vulnerability | Contract cure notice or termination; customer non-renewal after security review → Outdated SSP; open High POA&M items near go-live; vendor conditions unmet |
| Existing controls | This assessment and the POA&M; executive sponsorship; customer communication plan |
| **Inherent** | L3 × I5 = **15 High**: L3: 7 High findings against a 90-day rule. I5: loss of a $23.4M contract or a customer worth 21% of ARR. |
| **Current** (as tested) | L3 × I4 = **12 High**: L3: strong remediation momentum (7 of 19 closed in 6 weeks), but 3 High items are open with dependencies. I4: SHCA would more likely require a cure plan than terminate. |
| **Treatment** | Mitigate: Close High POA&M items before go-live; SSP rewrite (POAM-017); proactive customer update |
| **Residual** (target) | L2 × I3 = **6 Moderate**: L2: High items closed before 2027-01-11, and the SSP is accurate. I3. |
| Owner · target · status | Elena Marsh (CEO) · 2026-12-15 · Treatment in progress |
| Links | Controls PL-2, CA-5, CA-7 · Findings FIND-017 · POA&M POAM-017 |

### RISK-017: Service-account credential theft
*A stolen long-lived service credential grants quiet, unmonitored access to PHI extracts.*

| Field | Value |
|---|---|
| Asset / process | Non-human accounts with static credentials (SFTP push, reporting ETL, vendor logins) |
| Threat → vulnerability | Credential theft from hosts or repositories; vendor-side compromise → Keys 1.5–3 years old; no owners; a shared vendor login |
| Existing controls | Secrets Manager rotation for DB credentials; OIDC for CI/CD |
| **Inherent** | L3 × I4 = **12 High**: L3: static keys leak through repositories, hosts, and backups. I4: PHI extract access. |
| **Current** (as tested) | L3 × I4 = **12 High**: L3: modern patterns exist, but the legacy exceptions carry the risk. I4. |
| **Treatment** | Mitigate: Owners, rotation or federation, and named vendor accounts (POAM-005) |
| **Residual** (target) | L1 × I4 = **4 Low**: L1: federation and rotation with owners and quarterly attestation. I4: a compromised service identity would still reach the same data. |
| Owner · target · status | Alicia Moreno (CISO) · 2026-09-12 · Treated (residual achieved; monitoring) |
| Links | Controls IA-5, AC-2 · Findings FIND-005 · POA&M POAM-005 |

### RISK-018: Loss or theft of an endpoint containing PHI
*A lost or stolen laptop exposes PHI stored locally.*

| Field | Value |
|---|---|
| Asset / process | About 362 workforce laptops |
| Threat → vulnerability | Theft, loss in transit → Mobile workforce (60% remote) |
| Existing controls | Full-disk encryption (100%); MDM remote wipe; policy against storing PHI locally, with DLP; EDR |
| **Inherent** | L4 × I3 = **12 High**: L4: several devices are lost each year. I3: a local PHI cache could hold under 500 records. |
| **Current** (as tested) | L2 × I2 = **4 Low**: L2: devices are still lost (INC-2026-0063), but FDE means a lost encrypted device is not a breach of unsecured PHI. I2: exposure is internal-only and non-reportable when encryption is verified. |
| **Treatment** | Accept: None beyond current controls; annual review |
| **Residual** (target) | L2 × I2 = **4 Low**: Unchanged; within appetite. |
| Owner · target · status | Kevin Brandt (IT Manager) · 2027-07-15 · Accepted within appetite (Low) |
| Links | Controls SC-28, MP-6 · Findings — · POA&M — |

