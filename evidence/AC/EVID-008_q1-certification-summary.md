# EVID-008: Q1 2026 Access Certification Campaign (summary of export)

*Synthetic summary of an Okta Access Certification export (412 rows). The row-level export is summarized here; the analysis below is what the assessor re-performed.*

| Attribute | Value |
|---|---|
| Campaign | "Q1-2026 Manager Certification" |
| Launched / closed | 2026-03-02 / 2026-03-20 |
| Scope | Okta **application assignments** only (47 apps). *Not in scope:* AWS permission sets, GitHub org roles, database roles, local accounts, the vendor portal |
| Items / reviewers | 412 items / 23 managers |
| Decisions | **412 Approve, 0 Revoke** |

## Reviewer behavior (from decision timestamps)

| Reviewers | Items | Time from first to last decision | Revocations |
|---|---|---|---|
| 17 of 23 | 301 | under 5 minutes each (median 2m 40s) | 0 |
| 6 of 23 | 111 | 12 min to 2 days | 0 |

## Re-test of approved items (assessor)

| Item approved in Q1 | What the access review found in July | Exception |
|---|---|---|
| `rgupta2` → GitHub (SAML app) | Duplicate identity of a contractor converted to employee in 2025 | AR-EX-12 |
| `cfernandes` → "WCP Support Console" | Kept from her Support role after transferring to Data Engineering on 2026-02-16 | AR-EX-13 |

## Conclusion

The campaign ran on schedule, which was the claim in EVID-009. However, it neither covered privileged systems nor produced a single revocation among items later shown to be invalid. **AC-6(7): Other Than Satisfied → FIND-004.**
