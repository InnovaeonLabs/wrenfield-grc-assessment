# EVID-009: Evidence Rejected as Insufficient (teaching example)

| Field | Value |
|---|---|
| Requested | "Evidence that quarterly access reviews are performed" (AC-6(7)) |
| Provided | A screenshot of an access-governance dashboard tile reading **"Q1 Access Review: 100% complete ✓"** |
| Received | 2026-06-15 |
| Status | **Insufficient** |
| Replaced by | EVID-008 (full campaign export: 412 decisions with reviewer, item, decision, and timestamp) |

## Why it was rejected

| Test of evidence | Result | Why |
|---|---|---|
| **Relevant**: does it address the control requirement? | Partly | It shows a campaign ended, not that privileges were *validated* |
| **Reliable**: can it be traced to the system of record? | No | No URL, no date or time, no user context, and it is cropped. It could be from any quarter or any tenant |
| **Sufficient**: does it cover the population? | No | No population size, no list of systems in scope, no reviewers |
| **Timely**: does it cover the evidence period? | Unknown | Undated |
| **Shows operation?** | No | "100% complete" is equally consistent with a thorough review and with a rubber stamp |

## What the replacement showed

The export (EVID-008) revealed the problem the screenshot hid:
- 412 of 412 items approved (0 revocations).
- 17 of 23 reviewers completed their whole list in under 5 minutes.
- The campaign approved a duplicate account (`rgupta2`) and a transferred user's prior-role PHI access.
- AWS, GitHub, database, and local accounts were **not in scope at all**.

**Lesson:** completion status is *implementation* evidence at best. Operating effectiveness needs the decisions themselves. See [evidence-quality-guide.md](../../audit/evidence-quality-guide.md).

*(Synthetic example; no real screenshot is reproduced.)*
