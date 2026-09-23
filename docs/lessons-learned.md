# Lessons Learned

| Field | Value |
|---|---|
| Document ID | ASMT-LL-001 · 2026-09-18 |
| Format | Blameless. Each item: what happened → impact → change adopted → owner |
| Template | [templates/lessons-learned-template.md](../templates/lessons-learned-template.md) |

## Part A: Engagement lessons (simulated engagement)

### What worked
| ID | Lesson | Evidence |
|---|---|---|
| LL-01 | **Reconciling independent sources beats asking owners.** HR vs Okta vs system exports found the local AWS admin account, the vendor-portal leaver, and the duplicate identity. No owner had reported any of them | AR-EX-03, 04, 12 |
| LL-02 | **Scripted tests made findings undisputable.** Owners accepted the termination and SLA results quickly because anyone could re-run them | test-results/ |
| LL-03 | **Validation before closure caught a premature "done."** A JIT design screenshot was offered as closure evidence and returned; the item stayed open | EVID-071, POAM-003 |
| LL-04 | **Escalating by appetite, not instinct.** VR-001 was Critical, so it went to the CEO within 5 business days. That produced a decision (conditional continuation) in 5 days instead of a debate | FIND-016 |
| LL-05 | **Two versions of each finding.** Executives acted on the plain-language version; engineers acted on the 5-Cs version. Neither version would have worked for both audiences | findings-register.md |

### What did not work (and the change adopted)
| ID | What happened | Impact | Change adopted | Owner |
|---|---|---|---|---|
| LL-06 | Evidence requests like "show access reviews" returned a **screenshot** (EVID-009) | About 1 week lost on rework | Every PBC request names **artifact + population ("ALL") + period + format**. Screenshots are accepted only with URL, time, and user context | GRC Manager |
| LL-07 | **The questionnaire missed the Critical vendor issue**; the offshore access surfaced in an interview | A self-attested "US staff only" answer was false | Tier 1 assessments require a live technical interview plus a subcontractor list cross-checked against the SOC 2 report | Vendor Mgmt |
| LL-08 | Scope initially missed the **vendor portal** (local accounts) | Added in scope v1.1 after walkthroughs | Scoping checklist now asks: *"Where else do our users have accounts that SSO doesn't govern?"* | Lead assessor |
| LL-09 | One SRE team owns three POA&M items; two slipped or went overdue | POAM-011 slipped; POAM-018 overdue | POA&M planning now checks **owner capacity** across items, not just per item | CISO / CTO |
| LL-10 | Detection worked but response didn't (CSPM flagged RDP; nobody looked for 43 days) | FIND-012 | Every alert source must have a named queue and SLA before it counts as a control | Security Eng |
| LL-11 | Post-fix operating samples are small (7 terminations) | Closure confidence is limited | Closures are labeled "validated (limited sample)" and re-tested at the next annual assessment | Lead assessor |

## Part B: What I would do differently in a real company
1. **Negotiate access to the systems of record early.** Here, exports arrived as files. In a real engagement I would want read-only API access, or to watch every IPE pull (as I did for EVID-003), to reduce reliance on client-produced reports.
2. **Agree on the severity model with management before fieldwork.** Owners disputed severity once (FIND-010). A pre-agreed rubric turns that into a data discussion, not a negotiation.
3. **Assess inherited controls properly.** I marked PE-3 inherited on the strength of an inheritance record. A real assessment should review the provider's attestation scope and the customer-responsibility matrix line by line.
4. **Sample sizes by statute or framework guidance.** I used a frequency-based table. A regulated engagement (for example, FedRAMP or a financial audit) prescribes sampling and would change several sample sizes.
5. **Account for independence.** The same assessor recommended fixes and validated them. That is acceptable for readiness work, but an attestation would need separation.
6. **Budget time for politics.** Several delays (procurement, customer key exchange) were organizational, not technical. A real POA&M needs a dependency-escalation path from the first day.

## Part C: Portfolio-build lessons (real, not simulated)
These happened while building this repository. They are recorded because they are the same failure modes GRC work has.

| ID | What happened | How it was caught | Lesson |
|---|---|---|---|
| LL-B1 | A self-review slipped into the access-review data: the CISO was assigned to certify her own SIEM access | The integrity rule **ACR-04** (added as a placeholder, then implemented properly) failed | A rule you can't fail is not a control. Test the test |
| LL-B2 | Three findings listed controls that did not list them back (for example, FIND-010 → RA-5) | Integrity rule **CTL-10** (bidirectional links) | Traceability has to be checked in both directions, or it silently drifts |
| LL-B3 | The SSP-overstatement figure in the narrative (11) contradicted the computed owner-vs-validated delta (27) | The dashboard metric MET-05 surfaced the true count | Narrative numbers must come from the data, or be checked against it |
| LL-B4 | Early data files parsed "successfully" but silently mis-read 12 evidence records (unquoted commas) | A schema check for unexpected keys | "No error" ≠ "correct". Validate structure, not just parse success |
| LL-B5 | The dashboard's percentage formulas referenced hard-coded row numbers that were off by one | Cross-check of the Excel formulas (pycel) against the Python metrics | Two independent computations of the same metric catch what one alone cannot |
