# Access-Control Review: Process

**Deliverable:** [access-review.xlsx](access-review.xlsx) / [access-review.csv](access-review.csv) (106 certified entitlements) · **Findings:** [findings.md](findings.md) · **Engine:** [`tools/review_engine.py`](../tools/review_engine.py)

## 1. Scope
- **Systems (9):** Okta, AWS `wcp-prod` (IAM Identity Center and local IAM), GitHub, `wcp-core-db`, `wf-sftp-01`, PeopleHub, Ledgerline, security tooling (SIEM and EDR), Quarrystone portal.
- **Population rule:** 100% of privileged entitlements, 100% of PHI-bearing entitlements, 100% of service, shared, and break-glass accounts, **plus every entitlement held by any identity flagged as terminated, duplicate, or contract-lapsed** (the termination check follows the person, not the entitlement class).
- **Snapshot:** 2026-06-30. Certification 2026-07-06 to 2026-07-17.

## 2. Independent sources ([source-exports/](source-exports/))
| File | Source | Why it matters |
|---|---|---|
| `hr_roster.csv` | PeopleHub (HR, authoritative) | Worker status, role, transfers, contract end dates |
| `okta_users.csv` | Okta | Account status, MFA posture, exemption group |
| `entitlements.csv` | 9 system exports | What each account can actually do |
| `service_accounts.csv` | Service-account register | Owner and credential age for non-human accounts |
| `role_access_matrix.csv` | Approved role baseline | What each role *should* have |
| `sod_rules.csv` | SoD rule set | Conflicting combinations |
| `reviewer_decisions.csv` | Reviewer dispositions | Human judgment on every flag |

## 3. Method
1. **Reconcile** (engine): 13 automated checks (terminated, contract-lapsed, inactive > 90 days, MFA not enforced, outside role baseline, retained after transfer, admin on daily account, SoD conflict, duplicate identity, unowned service account, stale credential, shared account, unregistered non-human account).
2. **Certify** (humans): each row goes to the right reviewer (system owner or manager). **No self-review:** for example, the Director of Platform Engineering's admin rows went to the CTO, and the CISO's own SIEM access went to the CTO (enforced by integrity rule ACR-04).
3. **Disposition every flag.** Confirm it as an exception (`AR-EX-##`) or record why it is a false positive. The run **fails** if any flag is undispositioned.
4. **Roll up by root cause.** 20 exceptions become 7 control-level findings (FIND-001 to FIND-007).
5. **Remediate and verify.** Each exception has an owner, a due date, and closure evidence (EVID-###) verified in a post-change export.

## 4. Decision vocabulary
| Decision | Meaning |
|---|---|
| Retain | Access appropriate; no change |
| Retain (time-bound) | Appropriate until a fixed date (the assessor's own accounts, removed 2026-07-31) |
| Retain with exception | Keep, with documented exception/compensating control (SoD → RACC-001; contractor extension → SOW amendment) |
| Modify | Reduce or re-scope (for example, AdministratorAccess → read-only + JIT) |
| Revoke | Remove |

## 5. Judgment calls worth discussing in an interview
- **`rgupta2`**: the engine said "terminated worker". The reviewer determined it was a **duplicate identity** of an active employee (a contractor-to-employee conversion). Same action, different root cause, so it went to FIND-004, not FIND-001.
- **`awu`**: contract end date passed but the contractor was legitimately still working. The access was valid in fact but unsupported on paper. Resolved by fixing the paper (SOW amendment) *and* the control (Okta expiry dates).
- **`ocastillo` IR-Responder**: flagged inactive (118 days), dispositioned as a **false positive**, because an approval-gated incident role is *supposed* to be idle.
- **`jmercer` SoD**: a real conflict with a real compensating control that operated 6 of 6 months. The right answer was a **formal risk acceptance**, not revocation.
