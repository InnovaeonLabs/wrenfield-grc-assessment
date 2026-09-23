# TPRM-007 Third-Party Risk Management Standard (excerpt)

| Field | Value |
|---|---|
| Version | 1.1 · approved 2024-03-04 · owner: Beth Kowalski (Vendor Management Lead) |
| Drivers | HIPAA 164.308(b) / 164.314(a) (REQ-018), SHCA CSA §6.1 and §6.3 (REQ-007, REQ-008), SP 800-161 Rev. 1 Update 1 concepts |

## 3. Tiering (inherent risk before controls)
Score = data sensitivity (0–3) + data volume (0–3) + access/integration (0–3) + business criticality (0–3) + substitutability (0–2).

| Tier | Score | Due diligence | Reassessment |
|---|---|---|---|
| 1 | 9 or more | Questionnaire + attestation review (SOC 2 or ISO 27001) + pentest evidence + interview; contract security schedule | **Annual** + continuous monitoring |
| 2 | 5–8 | Questionnaire + attestation review | Every **2 years** + at renewal |
| 3 | 4 or less | Lightweight questionnaire | At renewal |

## 4. Minimum contract terms for vendors handling PHI
- **4.1** BAA (and subcontractor BAAs flowed down).
- **4.2** Security incident notification within **24 hours** of discovery for Tier 1 (72 hours for Tier 2).
- **4.3** Data location and access restrictions matching Wrenfield's customer obligations (US-only where required).
- **4.4** A subcontractor list, advance notice of changes, and a right to object.
- **4.5** Data return or destruction within 30 days of termination, with a certificate.
- **4.6** Right to assess, and annual evidence (attestation, pentest summary with retest).

## 5. Evidence rules
- **5.1** Self-attestation alone is not sufficient for Tier 1. Answers are corroborated with artifacts or interviews.
- **5.2** When relying on a SOC 2 report, the reviewer documents: scope, period and bridge letter, opinion, exceptions, subservice organizations (carve-outs), and **complementary user-entity controls that Wrenfield must perform**.

## 6. Decisions
- **6.1** Each Tier 1 assessment ends in a documented decision (**accept / mitigate / transfer / avoid**) with rationale, conditions, monitoring, and reassessment date, approved per the risk appetite (Critical outside appetite goes to the CEO).

*Known gap (FIND-015): terms 4.2–4.5 were added in 2025 and never applied retroactively to pre-2025 contracts such as Quarrystone (2023).*
