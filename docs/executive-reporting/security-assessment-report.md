# Security Assessment Report (SAR): WCP-PROD

| Field | Value |
|---|---|
| Document ID | ASMT-SAR-001 · v1.0 · status date **2026-09-18** · for delivery 2026-09-30 |
| System | Wrenfield Care Platform, production (WCP-PROD) · FIPS 199 Moderate |
| Framework | NIST SP 800-53 Rev. 5 (Release 5.2.0) · procedures per SP 800-53A Rev. 5 · risk per SP 800-30 Rev. 1 |
| Prepared by | Lead assessor (simulated independent assessor: Markese Raley, portfolio author) |
| Prepared for | Samir Haddad (CTO, system owner), Alicia Moreno (CISO), Board Audit & Risk Committee; SHCA submission by 2026-10-13 |

> **Simulated.** Fictional organization and synthetic data. This report is a portfolio artifact. It is **not** an authorization decision, audit opinion, or regulatory determination. See [DISCLAIMER.md](../../DISCLAIMER.md).

---

## 1. Executive summary

Wrenfield engaged an independent-style assessment of 61 NIST SP 800-53 Rev. 5 controls for its production platform ahead of the SHCA Medicaid contract, which requires Moderate-baseline alignment, a SAR, and a POA&M.

**Overall conclusion: Wrenfield's foundations are sound. Encryption, logging design, backups, incident handling, and monitoring all tested effective. The weaknesses were concentrated in identity lifecycle, privileged access, and third-party oversight, which are the areas SHCA and Lakemont care about most.** Remediation has been fast: 7 of 19 findings are closed with independent validation, including every identity finding that Lakemont's review raised (MFA exemptions, terminated users). **Four High findings remain open.** Two of them, the unsupported legacy SFTP host (FIND-011) and the Quarrystone vendor conditions (FIND-016), **are conditions for SHCA go-live** and are tracked at CEO level.

<!-- GEN:keymetrics:START -->
| Measure | Result (status date 2026-09-18) |
|---|---|
| Controls assessed (SP 800-53 Rev. 5) | 60 assessed + 1 N/A, across 18 families |
| Satisfied / Other Than Satisfied | 31 / 29 (52% satisfied) |
| Owner-stated statuses corrected by testing | 27 of 61 |
| Findings (High / Moderate / Low) | 19 (7 / 10 / 2), 0 Critical |
| Findings closed with validation | 7 of 19 (median 66 days) |
| Open High findings | 4 (FIND-003, FIND-010, FIND-011, FIND-016) |
| POA&M overdue / slipped / risk-accepted | 2 / 1 / 1 |
| Access review | 106 entitlements, 20 exceptions (18 closed, 1 accepted, 1 open) |
| Vendor risk (Quarrystone) | 12 findings (1 Critical, contained) · decision: Mitigate (conditional continuation) + partial Transfer |
| Tier 1–2 vendors with current assessment | 9 of 14 |
| Evidence completion | 86% (67 of 78); 5 items insufficient, each became part of a finding |
| Enterprise risks rated High+ | 14 at fieldwork → 11 now → 0 at target (18 risks) |
<!-- GEN:keymetrics:END -->

### What management should do now
1. **Decide SRE priorities (CTO, by 2026-09-25).** One SRE team owns the legacy-host migration (POAM-011, High, slipped), change-control automation (POAM-018, overdue), and JIT admin elevation (POAM-003). Sequence High items first and accept a revised date for POAM-018.
2. **Execute the Quarrystone amendment (General Counsel, by 2026-09-30).** US-only access and 24-hour breach notice are conditions precedent. **No SHCA data may flow to Quarrystone until they are met.**
3. **Sign the MDR SOW change (CFO).** It is the only blocker on overdue POAM-009 (backup reviewer for privileged-log review).
4. **Hold the 2026-10-14 ransomware tabletop at executive level.** The SHCA 24-hour reporting path has never been rehearsed.

## 2. Scope and approach
- **Boundary:** AWS `wcp-prod`/`wcp-dr`/`log-archive`/`security-tooling`, Okta, GitHub + Actions, `wcp-core-db`, `wf-sftp-01`, PeopleHub, Ledgerline, security tooling, Quarrystone portal. See [scope-statement.md](../scope/scope-statement.md) and [system-profile.md](../scope/system-profile.md).
- **Controls:** 61 controls and enhancements, 18 families, tailored from the Moderate baseline. Selection rationale in [nist-800-53-strategy.md](../assessment/nist-800-53-strategy.md). *Selection was risk-weighted toward known problem areas, so the satisfied rate is not a whole-program score.*
- **Methods:** Examine, Interview, Test (SP 800-53A). Interview never satisfied a control alone. Populations of 25 or fewer were tested in full; larger ones by seeded random sample ([assessment-plan.md](../assessment/assessment-plan.md)).
- **Reproducible tests:** termination de-provisioning, log-review completeness, vulnerability SLA, change sample, and the 106-row access-review engine are scripts that re-perform against the evidence ([test-results/](../assessment/test-results/)).
- **Periods:** operating effectiveness 2026-01-01 to 2026-06-30; configuration as of 2026-06-30; remediation validation 2026-08-15 to 2026-09-16.

## 3. Results by CSF 2.0 Function (informal grouping)

| Function | Controls | Satisfied | Other Than Satisfied | Reading |
|---|---|---|---|---|
| GOVERN | 16 | 8 | 8 | Risk strategy and assessments exist; vendor oversight, SSP currency, and personnel lifecycle lag |
| IDENTIFY | 4 | 4 | 0 | Categorization, risk assessment, scanning, inventory work |
| PROTECT | 29 (+1 N/A) | 12 | 16 | Crypto and boundary design strong; identity and access is the weak cluster |
| DETECT | 5 | 3 | 2 | Monitoring strong; retention and human review gaps |
| RESPOND | 4 | 3 | 1 | Incidents handled well; the capability was never exercised |
| RECOVER | 3 | 1 | 2 | Plan exists; restore now proven; CP test pending |

![Control results by family](../../dashboard/control-results-by-family.svg)

## 4. Significant (High) findings

| ID | Finding | Status | Why it matters |
|---|---|---|---|
| FIND-001 | Terminated workforce retained active access (incl. a post-termination sign-in and a local AWS admin account) | ✅ Closed, validated 2026-09-10 | Former-worker access to PHI and payments; SHCA 24h rule |
| FIND-002 | MFA exemption group (9 humans incl. an Okta Super Admin); IAM user without MFA | ✅ Closed, validated 2026-09-05 | One phished password could reach everything |
| FIND-003 | Excess privileged access; admin performed from daily accounts | 🔶 In progress (1 of 4 milestones), target 2026-11-05 | Highest-impact identity risk (RISK-001) |
| FIND-010 | 23% of Critical/High vulnerabilities past SLA; exception process unused | 🔶 In progress, target 2026-11-05 | Contract SLA gap, visible to SHCA quarterly |
| FIND-011 | Unsupported OS, DB, and runtime in the PHI path | ⏳ **Delayed**, revised target 2026-12-15 (approved) | **Go-live blocker** (CSA §7.4) |
| FIND-012 | Internet-exposed RDP on the legacy host for 43 days; CSPM alert ignored | ✅ Closed, validated 2026-07-10 | Common ransomware entry point; no evidence of compromise |
| FIND-016 | Quarrystone: undisclosed offshore PHI access, 30-day breach notice, excess data | 🔶 In progress; offshore access suspended 2026-07-24 | **Go-live blocker**; possible breach of 2 current customer BAAs |

The full register (technical and executive versions of every finding) is in [findings-register.md](../../findings/findings-register.md). Remediation plans are in [poam.md](../../poam/poam.md), and the 7 closures with full lifecycle traces are in [lifecycle-traces.md](../../poam/lifecycle-traces.md).

## 5. Access-control review
106 privileged, PHI, and non-human entitlements on 9 systems were certified; 20 exceptions rolled up to 7 findings; 18 exceptions are closed, 1 is risk-accepted (the finance SoD conflict, RACC-001), and 1 is open (a remaining daily-account admin). The review found what a manager-only certification could not: a **local AWS admin account** of a leaver, a **vendor portal account** outside SSO, a **shared vendor login**, and a **duplicate identity** from a contractor-to-employee conversion. Details: [access-review/findings.md](../../access-review/findings.md).

## 6. Third-party risk
Deep assessment of Quarrystone Analytics (Tier 1; nightly full-PHI extract of about 410k patients): 36 questions and 12 vendor findings, including **1 Critical**, found by interview, not by questionnaire: an offshore subcontractor with production access. It was escalated to the CEO within 5 business days, as the risk appetite requires. Decision: **Mitigate (conditional continuation) + partial Transfer**, with conditions precedent before SHCA data flows. Program-level: 9 of 14 Tier 1–2 vendors have a current assessment. Summary: [vendor-summary.md](../../vendor-risk/vendor-summary.md).

## 7. Risk posture
18 enterprise risks were scored with a documented method ([risk-methodology.md](../../risk/risk-methodology.md)). At fieldwork, 14 were High and none Critical. After validated treatments, **11 are High today**, and every residual target is Moderate or Low. Residual is never zero. Risks stay at their current score until the POA&M item is *validated*, not when the owner reports it done. See the [risk register](../../risk/risk-register.md).

![Risk heat maps](../../dashboard/risk-heatmap.svg)

## 8. Remediation status
![Open findings over time](../../dashboard/open-findings-trend.svg)

- **Validated closures:** FIND-001, 002, 005, 006, 008, 012, 013. Each was closed only after re-performance or observation (for example, the termination test re-run on 7 of 7 new leavers; a live restore in 3h41m against a 4h RTO).
- **Evidence rejected on the way:** EVID-071 (a JIT-elevation *design screenshot* offered as proof of an *operating* control) was returned as Rework Required.
- **Overdue:** POAM-009 (procurement dependency) and POAM-018 (SRE capacity). **Slipped:** POAM-011 (+40 days, approved, with compensating controls).

## 9. Assessor's conclusion and limitations
Based on the evidence examined, 31 of 60 applicable controls are Satisfied. The 29 Other-Than-Satisfied controls are tracked to closure in the POA&M, and the SHCA High-item rule (no High older than 90 days at go-live) **is achievable if the CTO's sequencing decision (§1) is made this month.**

Limitations: point-in-time testing with a 6-month look-back; small post-remediation operating samples (re-tested at the FY27 assessment); inherited AWS physical controls not tested; application security testing out of scope (covered by the annual penetration test).

## 10. Appendices
[Control matrix](../../controls/nist-800-53-control-matrix.csv) · [Worksheets](../assessment/worksheets/) · [Traceability](../assessment/traceability-matrix.md) · [Evidence tracker](../../audit/evidence-tracker.csv) · [Integrity check](../assessment/integrity-check.md) · [Dashboard](../../dashboard/dashboard.md) · [Lessons learned](../lessons-learned.md)
