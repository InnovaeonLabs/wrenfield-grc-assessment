# EVID-069: Backup Restore Test Record (wcp-core-db), 2026-08-27

| Field | Value |
|---|---|
| Control | CP-9(1) Testing for Reliability and Integrity (POAM-013 closure evidence) |
| Performed by | Jae-won Kim (Senior SRE) using `jkim-adm` · **observed by the lead assessor** (screen share) |
| Change record | CHG-2026-0744 (standard change: restore into isolated recovery account) |
| Source | AWS Backup vault `wcp-dr-vault` (us-west-2, Vault Lock compliance mode), recovery point 2026-08-27T06:00Z |
| Target | Isolated account `wcp-recovery-test` (no network path to production; destroyed after test) |
| Objectives (BCP-003) | RTO 4h · RPO 1h |

## Timeline

| Time (ET) | Step |
|---|---|
| 09:02 | Test start. Simulated scenario: primary cluster unusable (ransomware encryption) |
| 09:10 | Recovery point selected (latest cross-region copy, 06:00Z = 02:00 ET) |
| 09:14 | Restore job started (Aurora cluster from snapshot copy) |
| 11:58 | Cluster available; parameter group and KMS key (DR CMK) applied |
| 12:21 | Application smoke tests passed against restored endpoint (read-only config) |
| 12:43 | Integrity validation completed; **test declared successful** |

**Measured RTO: 3h 41m** (target 4h: met with 19 minutes of margin, which is thin).
**Measured data loss: 11 minutes.** Continuous backup (PITR) replication plus the cross-region copy schedule were restored to the latest available point; compared with the last committed transaction in production at test start. Target RPO 1h: met.

## Integrity checks (12 tables)

| Check | Method | Result |
|---|---|---|
| Row counts | `SELECT count(*)` per table vs production at the recovery-point timestamp (from CloudWatch metrics) | 12 of 12 match within expected in-flight delta |
| Checksums | `md5(string_agg(...))` over primary keys + updated_at for 12 PHI tables, recovery point vs production read replica at same LSN | 12 of 12 match |
| Encryption | Restored cluster `StorageEncrypted=true`, KMS key = DR CMK | Pass |
| Access | Restored cluster not reachable from any production network; security group allows the test bastion only | Pass |

## Issues found (tracked)
1. The runbook step for re-pointing the application secret was missing and took 14 minutes to work out. The runbook is now updated (v1.1).
2. The RTO margin is thin. Recommendation: pre-provision a warm parameter group and a restore-role in `wcp-dr` (logged as a POAM-014 after-action candidate for the October exercise).

## Assessor conclusion
Restore capability **demonstrated**. CP-9(1) remediation validated on 2026-09-01, once the semi-annual schedule was added to BCP-003. *(Synthetic record.)*
