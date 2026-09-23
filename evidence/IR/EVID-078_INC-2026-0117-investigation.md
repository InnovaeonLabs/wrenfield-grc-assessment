# EVID-078: INC-2026-0117 Post-Termination Sign-In Investigation

| Field | Value |
|---|---|
| Opened | 2026-07-06 14:20 ET, raised by the lead assessor during access-review reconciliation (AR-EX-02) |
| Severity | Medium (potential unauthorized access by a former contractor) |
| Handler | Owen Castillo (Security Engineer) · Privacy: Rachel Stein (HIPAA Privacy Officer) |
| Subject | `vosei` (contractor, Northgate SOW 2025-044, engagement ended 2026-06-05) |
| Closed | 2026-07-09 |

## Timeline
| Time | Event |
|---|---|
| 2026-06-05 17:00 | Engagement ended (Northgate emailed the sponsor; no offboarding ticket raised) |
| 2026-06-09 07:42 | Okta sign-in success for `vosei`. Okta Verify push approved on the contractor's enrolled phone. Client: native mail app on the same phone; IP geolocates to the contractor's home metro (consistent with prior sessions) |
| 2026-07-06 14:05 | Assessor reconciliation flags terminated-but-active account with post-termination sign-in |
| 2026-07-06 14:20 | CISO notified; incident opened |
| 2026-07-06 14:31 | Okta account deactivated, sessions and refresh tokens revoked; GitHub membership removed; PATs and SSH keys revoked |
| 2026-07-07 | Log review (Okta, Google Workspace, GitHub, AWS staging) |
| 2026-07-08 | Interview with the contractor via Northgate; written attestation received |
| 2026-07-09 | Privacy Officer breach risk assessment complete; incident closed |

## Findings
- The 2026-06-09 sign-in was a **mail-client token refresh** after an app update prompted re-authentication. The user approved the push by habit.
- Google Workspace audit log: 14 emails synced to the device (mailbox of an engineer; DLP scan found **no PHI**). No Drive or Docs access.
- GitHub: no pushes, clones, or API calls after 2026-06-04. AWS staging (no PHI): no activity after 2026-06-04.
- The contractor attested to deleting the mail account from the device on 2026-07-08.

## HIPAA breach risk assessment (4 factors, 45 CFR 164.402)
1. Nature and extent of PHI: **none identified** in the synced messages (DLP plus manual review of subjects).
2. Unauthorized person: a former contractor bound by the Northgate MSA confidentiality terms.
3. Whether PHI was actually acquired or viewed: no PHI present.
4. Mitigation: access revoked, attestation of deletion obtained.

**Conclusion:** not a breach of unsecured PHI. No notification required. Documented and retained.

## Root cause and linkage
Contractor end dates were not enforced and offboarding depended on a manual ticket. See FIND-001 / FIND-006, POAM-001 / POAM-006. IR-4 handling was **effective** (contained within 26 minutes of discovery). *(Synthetic record.)*
