# Resume Bullets (Project Section)

**How to list it:** put this under **Projects**, never under Experience.

> **Wrenfield Health GRC Assessment (independent portfolio project, simulated)** · NIST SP 800-53 Rev. 5 · github.com/InnovaeonLabs/wrenfield-grc-assessment

Formula: **Action + Scope + Method + Finding/Output + Business value.** Every number below is reproducible from the repo.

## GRC Analyst
- Scoped and executed a simulated **NIST SP 800-53 Rev. 5 (Release 5.2.0)** assessment of **61 controls across 18 families** for a fictional healthcare SaaS, using SP 800-53A Examine/Interview/Test methods; produced **19 findings** (7 High), **19 POA&M items**, and a Security Assessment Report aligned to a state Medicaid contract's Moderate-baseline requirement.
- Built a **traceability model** linking 24 business requirements → controls → 78 evidence items → test procedures → risks → POA&M, enforced by **43 automated integrity rules** in CI.
- Validated **7 remediations to closure** by re-performing tests (for example, 7 of 7 new leavers de-provisioned within 24h). Rejected design-only closure evidence, so no item closed on assertion.

## Information Security Analyst
- Tested identity, logging, vulnerability, backup, and change controls against synthetic evidence. Found **23% of Critical/High vulnerabilities past SLA**, **65% effective weekly privileged-log reviews**, and an **internet-exposed RDP port** on an unsupported host; drove each to a tracked fix.
- Wrote reproducible Python assessment tests (termination de-provisioning, log-review completeness, vulnerability SLA, change sampling) so any reviewer can re-perform results from the evidence.

## IT Risk Analyst
- Designed a **5×5 likelihood-impact methodology** (adapted from NIST SP 800-30 Rev. 1) with appetite, escalation, and acceptance authority. Scored **18 enterprise risks** inherent → current (as tested) → residual, with written rationale for every value.
- Documented a **formal risk acceptance** for a finance segregation-of-duties conflict, backed by a compensating control that tested effective 6 of 6 months. Recommended **Avoid** (decommission) over patching for unsupported legacy components.

## Security Compliance Analyst
- Mapped HIPAA Security Rule and contract clauses to SP 800-53 controls. Built a **78-item evidence tracker** with evidence-level grading (design / implementation / operating effectiveness), reaching **86% evidence completion** and rejecting insufficient artifacts such as undated screenshots.
- Produced audit-ready Excel workbooks with **controlled vocabularies, live formulas, and conditional formatting** (1,232 formulas verified error-free), plus CSV and Markdown views for version control.

## IAM Governance Analyst
- Certified **106 privileged, PHI, and non-human entitlements** across 9 systems by reconciling HR, IdP, entitlement, service-account, role-baseline, and SoD sources with a 13-check engine. Confirmed **20 exceptions** (terminated users still active, excess admins, a duplicate identity, a shared vendor login) and dispositioned 1 false positive.
- Rolled exceptions up to **7 root-cause findings** and tracked **18 of 20** to verified closure, including automated HR-to-IdP de-provisioning and removal of MFA exemptions for 9 users.

## Third-Party Risk Analyst
- Tiered **16 vendors** with a scored inherent-risk model (9 of 14 Tier 1–2 current). Performed a deep assessment of a PHI analytics vendor: **36-question questionnaire, SOC 2 report review including CUECs, and interviews**.
- Identified **12 vendor findings**, including a **Critical undisclosed offshore subcontractor**, and escalated it to the CEO per risk appetite. Recommended **conditional continuation** with contract conditions (24h breach notice, US-only access, data minimization, destruction certificates) and a monitoring and reassessment plan.

## One-line version (summary section)
Built a simulated NIST SP 800-53 Rev. 5 assessment for a fictional healthcare SaaS, covering control testing, access certification, vendor risk, risk register, POA&M, and executive reporting, with every artifact traceable and machine-validated.
