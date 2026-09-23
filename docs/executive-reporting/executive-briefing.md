# Board Briefing: Security Assessment of the Care Platform

**To:** Board Audit & Risk Committee · **From:** CISO, with the independent assessor · **Date:** 2026-09-18 · **Reading time:** 3 minutes
*(Fictional organization. Portfolio exercise.)*

## The one-paragraph version
We tested 61 security controls on the platform that holds patient data for about 410,000 people, against the federal standard our new state Medicaid contract requires. **The core protections work:** encryption, backups, monitoring, and day-to-day incident handling. **The gaps were in who has access and in one key vendor.** We found them, fixed the most urgent ones within weeks, and proved the fixes worked. Four serious items remain. Two of them must be resolved before the state contract goes live in January.

## Scorecard
<!-- GEN:keymetrics:START -->
| Measure | Result (status date 2026-09-18) |
|---|---|
| Controls assessed (SP 800-53 Rev. 5) | 60 assessed + 1 N/A, across 18 families |
| Satisfied / Other Than Satisfied | 31 / 29 (52% satisfied) |
| Owner-stated statuses corrected by testing | 27 of 61 |
| Findings (High / Moderate / Low) | 19 (7 / 10 / 2), 0 Critical |
| Findings closed with validation | 7 of 19 (median 66 days) |
| Open High findings | 4 (FIND-003, FIND-010, FIND-011, FIND-016) |
| POA&M overdue / slipped / risk-accepted | 2 / 1 / 1 |
| Access review | 106 entitlements, 20 exceptions (18 closed, 1 accepted, 1 open) |
| Vendor risk (Quarrystone) | 12 findings (1 Critical, contained) · decision: Mitigate (conditional continuation) + partial Transfer |
| Tier 1–2 vendors with current assessment | 9 of 14 |
| Evidence completion | 86% (67 of 78); 5 items insufficient, each became part of a finding |
| Enterprise risks rated High+ | 14 at fieldwork → 11 now → 0 at target (18 risks) |
<!-- GEN:keymetrics:END -->

## What we fixed (and proved)
- **Former employees and contractors with working logins.** Closed. An automatic daily check now removes access within 24 hours (tested on 7 of 7 recent departures).
- **Nine staff who could log in with only a password**, including one administrator. Closed. Everyone now uses multi-factor sign-in.
- **A remote-login port open to the internet** on an old server. Closed within 24 hours of discovery. No evidence of intrusion.
- **Backups we had never restored.** Proven. The full patient database was restored in 3h41m (target 4h).

## What still needs the Board's attention
| Issue | Why it matters | Owner | Deadline |
|---|---|---|---|
| **Analytics vendor** let an overseas subcontractor access our full patient dataset, and its contract allows 30 days before telling us about a breach | Violates 2 customer contracts today; blocks the $23.4M state contract | VP Clinical Analytics / General Counsel | Contract fix by 2026-09-30; **no state data shared until fixed** |
| **Old, unpatchable server** that sends that dataset nightly | State contract prohibits unsupported software; migration slipped about 3 months | CTO | 2026-12-15 (before 2027-01-11 go-live) |
| **Too many "keys to everything"** in production | Largest single identity risk | CTO | 2026-11-05 |
| **Security fixes applied late** (about 1 in 4 serious flaws past deadline) | Visible in our quarterly reports to the state | VP Engineering | 2026-11-05 |

## Decisions requested
1. **Endorse** the CEO's conditional continuation of the analytics vendor, with state data blocked until the conditions are met.
2. **Note** one formally accepted risk: a finance duty-overlap in a 3-person team, with an independent monthly review, until 2027-03-31.
3. **Support** the CTO in sequencing one engineering team's work so all serious items close before go-live.

## How to read our numbers
Every figure is calculated from the assessment records and cross-checked automatically. Percentages always show their denominator. An item counts as "fixed" only after independent re-testing. Full report: [security-assessment-report.md](security-assessment-report.md).
