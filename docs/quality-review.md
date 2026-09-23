# Quality Review: Four Perspectives

Before an artifact was marked final it was reviewed from four perspectives. This log records the questions asked and **what was corrected** as a result. Automated checks that enforce some of these reviews are in [integrity-check.md](assessment/integrity-check.md) (43 rules) and [`tools/check_formulas.py`](../tools/check_formulas.py).

| Perspective | Question | Standard applied |
|---|---|---|
| **Auditor** | Can I trace the conclusion to evidence? | Every determination cites EVID IDs that resolve; every closed POA&M item cites Closed/Accepted evidence and a validator |
| **Control owner** | Is the requirement understandable and actionable? | Findings name a specific gap, cause, and action. No "improve access management" |
| **Risk manager** | Can I understand the business consequence? | Every finding maps to a scored enterprise risk with written L and I rationale |
| **Hiring manager** | Does this prove real GRC work? | Judgment is visible: disputes, false positives, rejected evidence, accepted risk, slipped dates |

## Review log

| Artifact | Perspective | Issue found | Correction |
|---|---|---|---|
| Control matrix | Auditor | Single "implementation status" hid where owners overstated | Split into **Owner-Stated** vs **Assessor-Validated**, plus a formula flag (27 corrected) |
| Control matrix | Risk manager | RA-5 was OTS only because of SI-2's SLA failure, which double-counted one weakness | RA-5 Satisfied (scanning works) with OBS-02; the SLA failure sits on SI-2 alone |
| Control matrix | Auditor | CA-3 failed for Quarrystone contract *content*, which is SA-9's job | CA-3 Satisfied (agreements exist); content gaps under SA-9 (FIND-016) |
| Access review | Auditor | CISO certifying her own SIEM access (ENT-095) | Reviewer changed to CTO; rule ACR-04 now enforces "no self-review" |
| Access review | Control owner | `rgupta2` labeled "terminated" confused the IAM team (the person still works here) | Re-classified as **duplicate identity** (FIND-004), with the engine-versus-reviewer difference explained |
| Findings | Hiring manager | Findings read as a list of problems with no pushback | Added the challenge record for FIND-010 (owner dispute, assessor position, resolution) |
| Findings | Risk manager | The Quarrystone Critical (VR-001) vs the finding's High severity looked inconsistent | Documented: Critical at discovery, contained 2026-07-24; High pending the contract fix |
| Risk register | Risk manager | Top-risk list ranked risks already remediated | "Now" score = residual once validated; fieldwork score kept alongside |
| Risk register | Auditor | Residual equal to current for RISK-015 looked like no treatment | Rationale states why: training is hygiene; the risk is accepted within tolerance |
| POA&M | Auditor | Risk-accepted item flagged "beyond SLA" | Accepted items use the acceptance expiry as their target; SLA shows "n/a (acceptance expiry)" |
| POA&M | Control owner | "% complete" was subjective | Now a formula: milestones Done ÷ total |
| Evidence tracker | Auditor | "Insufficient" was counted as progress in an early completion metric | Completion = (Accepted + Closed) ÷ requested. Insufficient items are findings, not progress |
| SAR | Hiring manager | Early draft said "52% satisfied" with no context | Adds that selection was risk-weighted, so this is not a whole-program score |
| Dashboard | Auditor | Excel and Python metrics could diverge | pycel cross-check: 1,232 formulas, 0 errors, 0 mismatches |
| Worksheets | Control owner | Objectives quoted as if they were NIST text | Labeled "paraphrased"; NIST publication cited as authoritative |
| All | Portfolio integrity | Risk of implying real employment or audit | DISCLAIMER plus a banner on every executive document; "simulated" in every title block |
