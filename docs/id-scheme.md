# Cross-Artifact ID Scheme

Every artifact in this repository uses the same identifiers. Because of this, a reviewer can start from any row and follow the chain to its evidence and remediation. [`tools/validate.py`](../tools/validate.py) enforces the scheme: CI fails if any reference points to an ID that does not exist.

| Prefix | Object | Format / example | Source of truth | Referenced by |
|---|---|---|---|---|
| *(NIST ID)* | Control or enhancement | `AC-2`, `AC-2(3)`, `IA-2(1)` (SP 800-53 notation) | `data/controls.yaml` then the [control matrix](../controls/nist-800-53-control-matrix.csv) | Everything |
| `REQ-` | Business requirement (contract, regulation, commitment) | `REQ-004` = SHCA CSA §3.3 de-provisioning | `data/requirements.yaml` | Controls, traceability matrix |
| `SYS-` | In-scope system or component | `SYS-04` = `wcp-core-db` | Scope statement | Controls, access review |
| `TP-` | Test procedure step | `TP-AC-2-03` = test step 3 for AC-2 | `data/worksheets.yaml` then [assessment-procedures](../controls/assessment-procedures.csv) | Worksheets, controls |
| `EVID-` | Evidence item | `EVID-003` = HR terminations report | `data/evidence.yaml` then [evidence tracker](../audit/evidence-tracker.csv) | Controls, findings, POA&M closure |
| `AR-EX-` | Access-review exception | `AR-EX-02` = terminated contractor, active account | [access-review.csv](../access-review/access-review.csv) | Findings |
| `VQ-` | Vendor questionnaire item | `VQ-17` | `data/vendor.yaml` | Vendor assessment |
| `VR-` | Vendor risk finding | `VR-001` = offshore PHI access | `data/vendor.yaml` | Findings, POA&M, risk register |
| `VEN-` | Vendor record | `VEN-004` = Quarrystone Analytics | `data/vendor.yaml` | Vendor inventory, risks |
| `FIND-` | Control deficiency (finding) | `FIND-001` | `data/findings.yaml` | POA&M, risks, controls |
| `OBS-` | Observation (improvement item below finding threshold) | `OBS-02` | `data/findings.yaml` | Controls, SAR |
| `RISK-` | Enterprise cybersecurity risk | `RISK-002` | `data/risks.yaml` | Controls, findings, POA&M, dashboard |
| `POAM-` | POA&M item | `POAM-001` (same number as its finding) | `data/poam.yaml` | Findings, risks, controls |
| `RACC-` | Formal risk acceptance | `RACC-001` | [risk/risk-acceptance](../risk/risk-acceptance/) | POA&M, risk register |
| `INC-` | Incident ticket (synthetic) | `INC-2026-0117` | Evidence files | Findings (FIND-001) |
| `CHG-` | Change ticket (synthetic) | `CHG-2026-0412` | Evidence files | FIND-012, FIND-018 |
| `MET-` | Dashboard metric | `MET-07` = overdue POA&M items | [metric definitions](../dashboard/metric-definitions.md) | Dashboard |
| `LL-` | Lessons-learned item | `LL-03` | [lessons learned](lessons-learned.md) | — |

## Numbering conventions

- **FIND-nnn ↔ POAM-nnn share a number.** Every finding gets a POA&M item, including risk-accepted findings (tracked with status *Risk Accepted* and a `RACC-` reference). Nothing drops off the list.
- **Access-review exceptions and vendor findings roll up.** Many `AR-EX` or `VR` items can feed one `FIND`, because auditors report control failures, not individual accounts. Each `AR-EX`/`VR` still has its own owner, action, and closure evidence.
- **Risks are enterprise-level.** One `RISK` can be affected by several findings (for example, RISK-005 is driven by FIND-008 and FIND-009).
- **IDs are never reused.** A withdrawn item keeps its ID with status *Withdrawn* and a reason.

## Example chain

```
AC-2(3) Disable Accounts
  └─ REQ-004  SHCA CSA §3.3: disable terminated personnel within 24 hours
  └─ TP-AC-2(3)-02  Reconcile 19 H1 terminations to the Okta de-provisioning log
       └─ EVID-003 (HR terminations) + EVID-004 (Okta system log)
       └─ Result: Other Than Satisfied (2 of 19 still active; 1 local AWS IAM user)
  └─ AR-EX-01, AR-EX-02, AR-EX-03, AR-EX-16 (terminated users with active access)
  └─ FIND-001  Terminated workforce retained active access (High)
       └─ RISK-002  Unauthorized access by former workforce
       └─ POAM-001  Four milestones, closed 2026-09-10
            └─ Validation: re-run reconciliation (EVID-062) + 30-day sample (EVID-061) = 0 exceptions
```
