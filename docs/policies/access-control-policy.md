# ACP-002 Access Control Policy (excerpt)

| Field | Value |
|---|---|
| Version | 3.1 · approved 2025-01-15 by Alicia Moreno, CISO · **next review due 2026-01-15 (overdue; see OBS-01)** |
| Applies to | All workforce, contractors, and service identities accessing Wrenfield systems |
| Evidence ID | EVID-001 (fictional organization; excerpt written for this portfolio) |

> Why this excerpt exists: a policy is *design* evidence. This one is specific enough to test: "within 24 hours," "90 days," "separate account." That is why testing could show it was **not operating** (FIND-001, FIND-003). See the [evidence quality guide](../../audit/evidence-quality-guide.md).

## 4. Identification
- **4.1** Every person has exactly one workforce identity in Okta, linked to their PeopleHub worker ID.
- **4.2** Shared human accounts are prohibited. Vendor personnel receive named, federated accounts.
- **4.3** Service accounts are registered with a named owner, purpose, credential type, and rotation date.

## 5. Account lifecycle
- **5.1** Access is granted by ticket with manager and system-owner approval, based on the role access baseline.
- **5.2** Transfers: access from the prior role is re-baselined within 5 business days. *(Added in v3.2 draft after FIND-004.)*
- **5.3** Terminations: all access (SSO **and** non-SSO) is disabled **within 24 hours** of the termination effective time. Contractor accounts expire at the contract end date.
- **5.4** Administrative roles in AWS production (AdministratorAccess) and Okta (Super Administrator) must be used from a **separate privileged account** (`-adm`) protected by phishing-resistant MFA.
- **5.5** Temporary privileged grants have an expiry date not exceeding 30 days.
- **5.6** Accounts unused for **90 days** are disabled, except documented break-glass accounts that are tested quarterly.

## 6. Authentication
- **6.1** MFA is required for all access. Exceptions require CISO approval, a compensating control, and an expiry of **30 days or less**.
- **6.2** Replay-resistant authenticators only. SMS, voice, and email factors are disabled.

## 7. Review
- **7.1** Privileged and PHI access is recertified **quarterly**; all other access annually.
- **7.2** Reviewers may not certify their own access.
- **7.3** Reviewers must record a rationale when approving access flagged as inactive, outside the role baseline, or in SoD conflict. *(v3.2 draft)*

## 8. Separation of duties
- **8.1** Conflicting duties (see the Ledgerline SoD matrix) may not be held by one person without a documented risk acceptance and compensating control.
