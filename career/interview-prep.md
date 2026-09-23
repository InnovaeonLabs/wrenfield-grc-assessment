# Interview Preparation

Answer frameworks built **only** from work in this repository. Open with "In my portfolio project, a simulated assessment of a fictional healthcare SaaS…" and never imply it was a real employer or audit.

**Structure for every answer:** *Context (1 sentence) → What I did → What I found (a number) → Why it matters → What I'd do differently at a real company.*

---

### 1. How did you select controls?
- Started from the **SP 800-53B Moderate baseline** (287 controls and enhancements), verified against NIST's official OSCAL profile for Release 5.2.0, because the system is FIPS 199 Moderate.
- Filtered by **contract and regulatory drivers first** (24 REQs: SHCA CSA clauses, HIPAA), then **threat weighting** (identity, vendor, ransomware), then **known problem areas** (Lakemont's findings).
- Deliberately included **expected-to-pass controls** (SC-8, SC-12, SC-28, SI-3) to check the assessment for bias. All passed.
- Result: 61 controls in 18 families. *Differently:* in a real FedRAMP-style engagement the baseline is prescribed, not tailored this aggressively.

### 2. How did you determine applicability?
- Three outcomes: **applicable (system-specific or hybrid)**, **inherited** (PE-3 from the cloud provider, with an inheritance record and annual attestation review), or **Not Applicable** (AC-18: no wireless in the boundary). Every N/A has a written rationale, and a rule fails the build without one.
- Talking point: *N/A is a claim like any other, so it needs evidence (here, the boundary diagram).*

### 3. What makes evidence sufficient?
- Five tests: **relevant, reliable, complete (population), accurate, timely**. Then a level: **design → implementation → operating effectiveness**.
- Example: an access-review "100% complete" screenshot (EVID-009) failed reliability and completeness. The export (EVID-008) showed 412 of 412 approvals, with 17 of 23 reviewers finishing in under 5 minutes.
- IPE: I reconciled 19 terminations to 19 final-pay records before trusting the HR report.

### 4. Design versus operating effectiveness?
- Design: *is the control defined right?* (ACP-002 says "disable within 24h").
- Operating effectiveness: *did it work every time over the period?* 16 of 19 terminations were within 24h; 2 never happened; and a local AWS admin account stayed active 95 days.
- The policy was fine. The control failed in operation. That distinction was the whole of FIND-001.

### 5. How did you score risk?
- Wrote the method **before** scoring: 1–5 likelihood (with frequency anchors) × 1–5 impact (worst credible across PHI, operations, financial, legal, and patient safety; take the highest). Bands 1–4 / 5–9 / 10–16 / 20–25.
- Stated the limitation: ordinal scales, so the multiplication is a prioritization convention, not a measurement.
- Every L and I value has a written rationale. For example, RISK-003 inherent L4×I5 = 20: phishing is the top vector, and Okta federates to all PHI.

### 6. How did you handle residual risk?
- Three states: inherent (no controls) → **current (as tested; a failed control earns no credit)** → residual target. Residual is never zero.
- Risk-by-risk rationale for what each control changes (likelihood versus impact). Example: RISK-007 treated by **Avoid** (decommission), so residual L1×I4. Impact stays at 4 because the replacement still moves the same data.
- Acceptance only within appetite. The finance SoD conflict was accepted at Moderate with a compensating control that tested 6 of 6 months (RACC-001).

### 7. What did you find during the access review?
- 106 privileged, PHI, and non-human entitlements on 9 systems. 29 flagged, 20 confirmed exceptions, 1 false positive (an approval-gated incident role that is *supposed* to be idle).
- Highlights: a terminated contractor's **post-termination sign-in** (escalated the same day, HIPAA 4-factor assessment, no breach); a **local AWS admin** belonging to a leaver; **5 GitHub owners** against a cap of 3; a **shared vendor EDR login**; a **duplicate identity** from a contractor-to-employee conversion.
- Rolled up to 7 findings; 18 of 20 exceptions closed and verified.

### 8. How would you challenge a control owner?
- Real example (FIND-010): Engineering said two Critical findings were "not exploitable." My position: *that is a conclusion, so show me the reachability analysis and use the exception process the standard already requires.* The determination stood; they filed the exception with evidence.
- My standard questions: *Show me the population, not an example. Show me a time it caught something. What happens when that person is on PTO? Where does this identity exist outside SSO?*
- Also rejected a design screenshot offered as proof that JIT elevation operates (EVID-071).

### 9. What is a POA&M?
- A **Plan of Action & Milestones** (CA-5): every weakness with owner, corrective action, milestones, resources, dates, status, and closure evidence. It is the contract deliverable SHCA requires (CSA §2.4).
- Mine tracks SLA date, **original versus current target** (slips need an approved reason), formula-driven % complete, overdue flags, and validation method. Accepted risks stay on it until expiry.

### 10. How did you prioritize remediation?
- By severity (same 5×5 method at weakness level) → SLA (High 90 days, per the contract's rule) → **go-live dependency** (FIND-011 and FIND-016 block SHCA) → **owner capacity** (one SRE team owned three items, so I asked the CTO to sequence them).
- Quick wins with high risk reduction came first: MFA exemptions and terminated access closed in weeks.

### 11. How did you assess vendor risk?
- Tiered all 16 vendors on a 14-point inherent-risk score. Deep-assessed the highest (full PHI extract of about 410k patients).
- Questionnaire (36 items) + **SOC 2 review** (scope, exceptions, carve-outs, **CUECs**) + interviews. The interview found what the questionnaire hid: an **undisclosed offshore subcontractor** (Critical).
- Decision: Mitigate (conditional continuation) + partial Transfer. Avoid and Accept were rejected with reasons, and there are conditions precedent before Medicaid data flows.

### 12. What would you escalate to management?
- Anything **outside appetite**: VR-001 (Critical) went to the CEO within 5 business days, as the risk strategy requires.
- **Decisions only management can make:** SRE sequencing (CTO), MDR contract signature (CFO), vendor amendment (General Counsel).
- **Incidents found during fieldwork** go immediately, outside the report cycle (INC-2026-0117 was raised the same day).

### 13. What would you do differently in a real company?
- Read-only API access to systems of record rather than client-produced exports; a pre-agreed severity rubric; line-by-line review of inherited controls; framework-prescribed sampling; and keeping the recommending assessor separate from the validating one for attestation work. See [lessons-learned.md](../docs/lessons-learned.md) Part B.

### Bonus: "Tell me about a mistake."
- Building the project, an automated rule caught that I had assigned the CISO to certify **her own** access, which is a self-review. Another rule caught three one-directional control-to-finding links. *Lesson: build checks that can fail, and trust them over your own confidence.* ([lessons-learned.md](../docs/lessons-learned.md) Part C)
