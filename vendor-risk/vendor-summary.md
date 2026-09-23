# Vendor Risk Executive Summary: Quarrystone Analytics, LLC (fictional)

| Field | Value |
|---|---|
| Vendor | VEN-004 Quarrystone Analytics, LLC: population-health analytics |
| Tier | **1** (inherent score 12 of 14: PHI, over 50k records, file-transfer integration, high criticality, hard to replace) |
| Assessment | 2026-06-22 to 2026-07-24 · questionnaire (36 items), SOC 2 Type II review, 2 interviews, contract review |
| Business owner | Dr. Miriam Castell, VP Clinical Analytics |
| **Decision** | **Mitigate: conditional continuation, plus partial Transfer.** Approved by the CEO 2026-07-22. **No SHCA (Medicaid) data until the conditions precedent are met** |
| Detail | [vendor-assessment.md](vendor-assessment.md) · [vendor-assessment.xlsx](vendor-assessment.xlsx) · [vendor-questionnaire.xlsx](vendor-questionnaire.xlsx) · SOC 2 workpaper [EVID-050](../evidence/SR/EVID-050_quarrystone-soc2-review-workpaper.md) |

## 1. Why this vendor
Quarrystone receives a **full PHI extract of about 410,000 patients every night** (58 fields, including contact details and free-text care notes) and returns risk scores that decide which patients care managers call first. It is the largest flow of PHI outside Wrenfield's boundary, and it would carry Medicaid data after the SHCA go-live.

## 2. Inherent vendor risk: **Critical**
Full identifiers, high volume, external processing, the vendor's own subcontractors (four; see the fourth-party map), and a data flow that leaves through an unsupported Wrenfield host.

## 3. Material findings
| ID | Finding | Severity | Party |
|---|---|---|---|
| **VR-001** | Undisclosed offshore subcontractor (Pune) with **production access to Wrenfield PHI**. It surfaced only in the interview; the questionnaire answer was "US staff only" | **Critical** | Vendor |
| **VR-002** | BAA allows **30 days** to notify of a breach. Wrenfield must notify SHCA in 24h and customers in 5 business days | High | Vendor (contract) |
| **VR-003** | Wrenfield sends **27 of 58 fields the model does not use** (address, phone, email, free text): a minimum-necessary failure | High | **Wrenfield** |

Nine further findings are rated Moderate or Low. They include stale pentest evidence, undefined data return, a SOC 2 CUEC Wrenfield was not performing, incomplete subcontractor disclosure, short log retention, and secondary-use ambiguity. **Three of the twelve are Wrenfield's own fault**, which is the point of reading the CUECs.

## 4. Mitigating controls already in place
Unqualified SOC 2 Type II (2 minor exceptions with adequate responses) · AES-256 at rest and TLS/SFTP in transit · SSO+MFA (FIDO2 for admins) · immutable backups · US data storage · $5M cyber insurance · WCP's rules-based fallback if scores are unavailable · **offshore access suspended 2026-07-24 (interim containment, vendor letter EVID-073).**

## 5. Residual risk
**High today → Moderate once the conditions are met** (RISK-010: current L3×I5 = 15; residual target L2×I4 = 8). Contractual US-only access with technical enforcement cuts likelihood. Data minimization cuts impact, since contact details and free text are no longer exposed.

## 6. Treatment decision and rationale
| Option | Considered? | Why / why not |
|---|---|---|
| **Accept** | Rejected | VR-001 is Critical and VR-002/003 are High: outside appetite (Critical cannot be accepted) |
| **Avoid** (replace vendor) | Rejected, for now | Replacement takes 9 to 12 months and the fallback is less accurate. The vendor's *core* security is mature; the problems are contractual and in data design, and fixable |
| **Transfer** | Partial | Raise cyber insurance to at least $10M naming Wrenfield, and add breach-cost indemnity. *Transfers money, not accountability* |
| **Mitigate** | **Chosen** | The fixes are specific and enforceable, and the 2027-01-31 renewal gives leverage |

## 7. Conditions precedent (before any SHCA data)
1. Executed amendment: **US-only storage and access** with technical enforcement, a subcontractor schedule, and approval rights (VR-001, VR-008).
2. **24-hour breach notification** (VR-002).
3. **Minimized, tokenized extract** in production (VR-003).

## 8. Contract and security requirements (amendment redline v3)
24h incident notice · US-only data and access, including subcontractors, with a quarterly access-log attestation · subcontractor schedule with 30-day notice and right to object (plus SHCA approval for agency data) · return and destroy data within 30 days with a certificate · 12-month access logs, provided within 5 business days on request · annual independent pentest with retest · no secondary use without consent (pending a legal opinion on VR-010) · cyber insurance of at least $10M · SAML SSO for the portal at renewal.

## 9. Monitoring requirements
| Frequency | Activity |
|---|---|
| Quarterly | US-only access attestation with an access-log sample; subcontractor-change check |
| Semi-annual | SOC 2 report or bridge letter review; open-issue review with the vendor CISO |
| Continuous | External attack-surface and breach-news monitoring; renewal trigger |
| Event-driven | Reassess on incident, subcontractor change, or material service change |

## 10. Reassessment frequency
**Focused reassessment January 2027** (before SHCA data flows; validates the conditions), then an **annual full Tier 1 assessment**.

## Lessons for the vendor program (feeds FIND-015)
- **Self-attestation missed the Critical issue. An interview found it.** Tier 1 reviews now require a live session with the vendor's technical lead.
- **Read the CUECs.** The SOC 2 listed three responsibilities Wrenfield was not performing.
- **Contracts drift.** A 2023 contract on the vendor's paper never received the 2025 minimum terms. Renewal dates now trigger a terms review.
