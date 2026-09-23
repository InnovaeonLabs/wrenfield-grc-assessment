# Cybersecurity Risk-Scoring Methodology

| Field | Value |
|---|---|
| Document ID | RSK-MTH-001 · v1.0 · approved 2026-06-12 **(before any risk was scored)** |
| Owner | Alicia Moreno, CISO · approved by the Executive Risk Committee (CEO, CFO, CTO, CISO, General Counsel) |
| Basis | Adapted from NIST SP 800-30 Rev. 1 (qualitative likelihood and impact), aligned to Wrenfield's risk-management strategy (PM-9) |

## 1. Purpose

Every risk in the [risk register](risk-register.csv), and every finding in the [findings register](../findings/findings-register.csv), is scored with **this one method**. That keeps scores comparable and makes them easy to challenge. A score without a written rationale is not accepted.

## 2. Risk statement format

Each risk is written as **threat source → threat event → vulnerability/condition → asset → business impact** (per the SP 800-30 risk model):

> *An external actor (threat source) uses a stolen workforce credential (threat event) against an account exempted from MFA (vulnerability), gaining access to Okta-federated systems (asset), which leads to PHI exposure and contract breach (impact).*

## 3. Likelihood scale (1–5)

Likelihood is the chance that the threat event happens **and** succeeds against Wrenfield within the next 12 months, given the control state being scored.

| Score | Level | Anchor (any one is enough; the assessor records which applied) |
|---|---|---|
| 5 | Very High | Expected within 12 months (>90%); already occurring or observed at Wrenfield; trivially exploitable and actively targeted in healthcare |
| 4 | High | Likely (61–90%); common attack pattern against this asset type; a control gap is confirmed with no compensating control |
| 3 | Moderate | Possible (31–60%); a gap exists but partial or compensating controls raise attacker effort |
| 2 | Low | Unlikely (11–30%); effective controls in place, residual weakness needs uncommon skill or conditions |
| 1 | Very Low | Rare (≤10%); multiple layered controls tested effective |

## 4. Impact scale (1–5)

Impact is the **worst credible** business consequence, not the worst imaginable. Score each dimension and take the **highest** (the high-water mark, consistent with FIPS 199 thinking).

| Score | Level | PHI / privacy | Operations (WCP availability) | Financial | Legal / contractual | Patient safety |
|---|---|---|---|---|---|---|
| 5 | Severe | >50,000 records, or any SHCA Medicaid data; HHS breach report with media notice | Outage >24 h, or data loss beyond RPO | >$2M | Loss of the SHCA contract or a top-5 customer; regulator action | Credible contribution to patient harm |
| 4 | Major | 500–50,000 records | Outage 8–24 h | $500K–$2M | Material contract breach; formal cure notice | Care delays across several customers |
| 3 | Moderate | <500 records (still reportable) | Outage 2–8 h | $100K–$500K | Customer audit finding; remediation demanded | Workarounds needed; no harm expected |
| 2 | Minor | Internal-only exposure, no reportable breach | Degraded service <2 h | $10K–$100K | Contract observation; questionnaire exception | None |
| 1 | Negligible | None | No noticeable effect | <$10K | None | None |

## 5. Risk score and rating

**Risk Score = Likelihood × Impact** (range 1–25)

| Score | Rating | Color | Excel formula (score in column J) |
|---|---|---|---|
| 20–25 | **Critical** | Dark red | `=IF(J2>=20,"Critical",IF(J2>=10,"High",IF(J2>=5,"Moderate","Low")))` |
| 10–16 | **High** | Red/orange | (same formula) |
| 5–9 | **Moderate** | Amber | |
| 1–4 | **Low** | Green | |

Heat map (score shown in each cell):

| Likelihood ↓ / Impact → | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** | 5 M | 10 H | 15 H | 20 C | 25 C |
| **4** | 4 L | 8 M | 12 H | 16 H | 20 C |
| **3** | 3 L | 6 M | 9 M | 12 H | 15 H |
| **2** | 2 L | 4 L | 6 M | 8 M | 10 H |
| **1** | 1 L | 2 L | 3 L | 4 L | 5 M |

**Known limitation (stated openly):** the scales are ordinal, so multiplying them is a *prioritization convention, not a measurement*. A 12 is not "twice as risky" as a 6. **Ties are broken by Impact, then by Likelihood.** A risk with Impact 5 is never rated below Moderate, whatever its likelihood.

## 6. Three risk states

| State | Definition | When scored |
|---|---|---|
| **Inherent** | Risk with **no controls** considered: likelihood and impact of the threat against the asset's exposure alone | Once, at identification |
| **Current (assessed)** | Risk with **existing controls as tested** during fieldwork, including tested deficiencies. A control that failed testing earns no credit | At fieldwork (July 2026); updated at each review |
| **Residual (target)** | Risk expected **after the planned treatment** is complete and validated | At treatment planning; confirmed when the POA&M item closes |

Rules:
- Residual risk is **never zero**. A likelihood of 1 still means "rare", not "impossible".
- A control reduces **likelihood** (it prevents or detects) or **impact** (it contains or recovers). Each change needs a written reason naming the control.
- If residual Impact equals inherent Impact, the rationale must say why impact cannot be reduced (for example, "an admin credential compromise still reaches all PHI; the control only makes it less likely").

## 7. Risk appetite and escalation (PM-9)

| Rating | Appetite | Required response | Who may accept | Maximum acceptance period |
|---|---|---|---|---|
| Critical | **Outside appetite** | Escalate to the CEO within 5 business days; treatment plan within 15 days; Board Audit & Risk Committee informed | Not acceptable. The only options are treat or avoid | — |
| High | Outside appetite | Treatment plan within 30 days; tracked in the POA&M | CEO (on CISO recommendation), time-bound, with compensating controls | 6 months |
| Moderate | Within tolerance | Treat or accept with rationale | Risk owner (VP level) with CISO concurrence | 12 months |
| Low | Within appetite | Accept and monitor | Risk owner | 12 months (reviewed annually) |

## 8. Treatment options

| Strategy | Meaning | Example in this project |
|---|---|---|
| **Mitigate** | Implement or strengthen controls | Enforce MFA for all accounts (RISK-003) |
| **Accept** | Formally accept with rationale, owner, expiry, and compensating controls | Finance SoD conflict with a monthly compensating review (RISK-013, RACC-001) |
| **Transfer** | Shift financial impact through contract or insurance. *Liability transfers; accountability does not* | Cyber insurance plus vendor indemnity for Quarrystone (RISK-010, partial) |
| **Avoid** | Stop the activity that creates the risk | Decommission `wf-sftp-01` rather than keep patching around it (RISK-007) |

## 9. Remediation timelines for findings (POA&M SLA)

| Finding severity | Target from POA&M open date | Rationale |
|---|---|---|
| Critical | 30 days | Outside appetite; immediate executive visibility |
| High | 90 days | Matches SHCA CSA §2.4: no High item older than 90 days at go-live |
| Moderate | 180 days | Within tolerance; batched into quarterly delivery |
| Low | 365 days | Annual cycle |

*Vulnerability (scanner) findings follow a separate, shorter SLA in the [Vulnerability Management Standard](../docs/policies/vulnerability-management-standard.md): Critical 15, High 30, Moderate 90 days, per SHCA CSA §7.1.*

## 10. Finding severity

Findings are scored with the **same matrix**, at the level of the individual weakness: *what is the likelihood and impact of this specific deficiency being exploited?* Severity is the band of that score. A finding's severity can differ from the rating of the enterprise risk it feeds, because enterprise risks combine several weaknesses and controls.

## 11. Review cadence

- The risk register is reviewed **monthly** by the GRC Manager and **quarterly** by the Executive Risk Committee.
- Any risk whose *current* score changes band is re-presented to its owner within 10 business days.
- Risk acceptances are reviewed at expiry or on a trigger event (incident, major change, new contract).

## 12. Worked example

**RISK-003: Account takeover through MFA gaps**
- *Inherent* L4 × I5 = **20 Critical**. Credential phishing is the leading intrusion path (L4). Okta federates into AWS prod and the PHI database (I5: >50k records).
- *Current* L3 × I5 = **15 High**. MFA covers 97% of human accounts (a partial control, so L drops to 3), but 9 humans (incl. an Okta Super Admin) were exempt. Impact is unchanged because the exempt admin could reach everything.
- *Residual* L2 × I4 = **8 Moderate**. Exemptions removed and phishing-resistant MFA (FastPass/WebAuthn) required for admins: L2, since session-token theft is still possible. Least-privilege work (POAM-003) limits what a single compromised non-admin account can reach: I4.
