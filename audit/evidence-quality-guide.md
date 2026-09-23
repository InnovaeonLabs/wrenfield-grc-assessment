# Evidence Quality Guide: Documentation ≠ Implementation ≠ Operating Effectiveness

> **A policy that exists does not prove a control operates.** This guide is how every item in the [evidence tracker](evidence-tracker.csv) was judged, with real examples from this assessment.

## 1. The three levels

| Level | Question it answers | Typical artifacts | What it **cannot** prove |
|---|---|---|---|
| **Design** (documentation exists) | *Is the control defined correctly?* | Policy, standard, procedure, SSP narrative, RACI | That anyone follows it |
| **Implementation** | *Is the control actually configured or deployed right now?* | System configuration export, policy JSON, group membership, screenshot **with context** | That it worked across the period, or catches exceptions |
| **Operating effectiveness** | *Did it work, every time it should have, over the period?* | Complete population plus sample tests, tickets with timestamps, logs, re-performance | (Nothing by itself: it still needs a reliable population) |

A control is **Satisfied** only when evidence reaches the level the control's nature requires. Periodic and event-driven controls (terminations, reviews, patching) need **operating-effectiveness** evidence. Pure configuration controls (encryption at rest) can be satisfied at **implementation** level with a full-population configuration query.

## 2. Worked contrasts from this assessment

| Control | Design evidence (exists) | Implementation evidence | Operating-effectiveness evidence | Verdict |
|---|---|---|---|---|
| **AC-2(3)** Disable accounts | ACP-002 §5.3: "disable within 24 hours" (EVID-001) | Okta deactivation feature in use | **19 terminations vs Okta log (EVID-003/004): 16 on time, 1 late, 2 never; plus a local AWS admin active 95 days** | Policy was fine; **operation failed** (FIND-001) |
| **AC-6(7)** Access reviews | Quarterly review in ACP-002 §7.1 | Campaign configured in Okta; screenshot "100% complete" (EVID-009, **rejected**) | **Export of 412 decisions (EVID-008): 100% approved, 17 of 23 reviewers < 5 min, invalid items approved** | Ran on schedule; **not effective** (FIND-004) |
| **CP-9 / CP-9(1)** Backups | BCP-003 RTO 4h / RPO 1h | Backup plans + Vault Lock (EVID-034): **CP-9 Satisfied** | Restore test: **none until 2026-08-27** (EVID-035 Insufficient → EVID-069) | Backups existed; **recoverability unproven** (FIND-013) |
| **IR-8 / IR-3** Incident response | IRP-005 current (IR-8 Satisfied) | MDR contract, on-call rota | Exercise: last one 21 months ago (EVID-037 Insufficient) | Plan ≠ capability (FIND-014) |
| **AU-11** Retention | LMS-004 retention section | Retention settings (EVID-024) | Oldest-record query: matched settings exactly (no hidden longer retention) | Configuration itself was the failure (FIND-008) |
| **AT-2** Training | Policy HR-011 | LMS assignment rules | **Completion vs Okta population: 316 of 347** | 91%, enforcement not operating (FIND-019) |
| **SC-28** Encryption at rest | Data-handling standard | **Config query of 100% of data stores + MDM (EVID-056)** | (A full-population configuration query is sufficient for a continuous technical control) | **Satisfied** |

## 3. Sufficiency tests applied to every item

| Test | Question | Common failure seen |
|---|---|---|
| **Relevant** | Does it address *this* control's requirement? | A backup *job* log offered for a *restore* test (EVID-035) |
| **Reliable** | Is it system-generated, traceable, and unaltered? | Undated, cropped screenshot (EVID-009) |
| **Complete (population)** | Does it cover *all* items, not examples? | "Here are 5 terminations" rather than *all* 19; requests always say "ALL" |
| **Accurate** | Do records trace back to the source system? | 3 records traced from each export to the system of record |
| **Timely** | Does it cover the evidence period or as-of date? | 2024 failover notes offered for a 2026 CP test (EVID-033) |

### Information produced by the entity (IPE)
System reports are only as good as their query. Before relying on one, the assessor records how it was produced and checks **completeness** against an independent total.

*Example:* the PeopleHub termination report (EVID-003) reconciled to 19 final-pay or final-invoice records. A report filtered wrongly (for example, excluding contractors) would have hidden the `vosei` case, the one with a post-termination sign-in.

## 4. Status vocabulary (tracker)
`Not Requested → Requested → Received → Under Review → Accepted | Insufficient | Rework Required → Closed`
- **Insufficient** is terminal for the period: the evidence does not exist, so the control is Other Than Satisfied.
- **Rework Required** means the right thing exists but was provided wrongly, for example EVID-071: a design screenshot offered for an operating JIT elevation. The owner must resubmit.
- **Closed** is used for remediation-validation evidence tied to a closed POA&M item.

## 5. How to challenge a control owner (script used in fieldwork)
1. *"Show me the population, not an example."*
2. *"Show me an instance where the control caught something."* A control that never fires is either perfect or not operating.
3. *"What happens when the person who does this is on PTO?"* This found the AU-6 single point of failure.
4. *"Where else does this identity exist outside SSO?"* This found `mfeld-admin` and the vendor-portal account.
5. *"Is that a conclusion or evidence?"* See FIND-010: "not exploitable" was asserted, not shown.
