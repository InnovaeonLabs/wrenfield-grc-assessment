# LMS-004 Logging & Monitoring Standard and CMP-006 Change Management Procedure (excerpts)

## LMS-004 Logging & Monitoring Standard
| Field | Value |
|---|---|
| Version | 1.4 · approved 2025-06-02 · owner: Owen Castillo |

- **§3 Required events:** authentication (success and failure), privileged actions, IAM and policy changes, PHI record view, export, and print (application audit), configuration changes, security-tool alerts.
- **§4 Protection:** logs are delivered to the `log-archive` account with Object Lock. Operational admins cannot stop or delete trails (SCP).
- **§5 Retention:** *v1.4 said 180 days (CloudTrail) and 90 days (application).* **Superseded 2026-08 by v1.5: 400 days for all audit sources, 90 days searchable (FIND-008).**
- **§6 Weekly privileged-activity review:** a human review of AWS admin actions, Okta admin changes, and GitHub owner actions, documented in a SEC ticket within 5 business days of week end. **Each flagged item needs a disposition.** *v1.5 adds a named backup reviewer and escalation to the CISO when a week is missed (FIND-009).*

## CMP-006 Change Management Procedure
| Field | Value |
|---|---|
| Version | 3.0 · approved 2025-04-14 · owner: Tomasz Wierzbicki |

- **§3 Change types:** *Standard* (pre-approved, low risk, templated), *Normal* (PR review + approver before deploy), *Emergency* (restore service or close an active security risk).
- **§4.1** Normal changes are approved **before** deployment; the deploy job requires an approved environment reviewer.
- **§4.3** Emergency changes may deploy on verbal approval but must be **retro-approved within 2 business days**, and any temporary configuration must be **reverted or converted into a normal change**.
- **§5** Console changes to production are emergency changes by definition. *(Gap: no detection existed; FIND-018.)*
