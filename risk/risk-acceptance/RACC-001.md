# Risk Acceptance RACC-001: Finance Segregation-of-Duties Conflict

| Field | Value |
|---|---|
| Acceptance ID | **RACC-001** |
| Related | FIND-007 · RISK-013 · POAM-007 · AR-EX-17 · AC-5 |
| Risk owner | Raymond Okafor, CFO |
| Concurrence | Alicia Moreno, CISO |
| Date signed | 2026-08-12 |
| **Expires** | **2027-03-31** (or earlier on trigger) |

## 1. Risk being accepted
Jordan Mercer (Senior Accountant) holds both **Vendor Master Maintain** and **Payment Approver (≤ $25,000)** in Ledgerline (SoD rule SOD-01). One person could create or alter a vendor, including bank details, and approve payments to it.

## 2. Why accept rather than fix now
- The finance team is three people after the AP Specialist departed (2026-05-22). Splitting the roles today would leave no backup for payment approvals during month-end close.
- The AP Specialist requisition is open (target hire Q4 2026). Roles will be split at onboarding.

## 3. Rating (RSK-MTH-001)
| State | L × I | Rating | Rationale |
|---|---|---|---|
| Inherent | 3 × 3 = 9 | Moderate | Business-email-compromise bank-change fraud is common; impact is bounded by the $25k limit per payment and monthly detection |
| With compensating control | 2 × 3 = 6 | **Moderate** | Compensating review operated 6 of 6 months, plus callbacks |

Moderate is within tolerance, so it may be accepted by the risk owner (VP level or above) with CISO concurrence (RSK-MTH-001 §7). **This acceptance is within authority.**

## 4. Compensating controls (must keep operating)
1. **Monthly vendor-master change report** reviewed and signed by the Controller (independent of the user) within 10 business days of month end. Every bank-detail change is verified by **callback to a known number**.
2. Payments above $25,000 require CFO approval (outside the user's authority).
3. GRC collects the signed report monthly as evidence. A missed month voids this acceptance and escalates to the CFO.

## 5. Conditions and triggers for early review
- Any missed compensating review.
- Any fraud event or attempted bank-change fraud.
- AP role backfilled (roles split within 30 days of start).
- A change to the approval limit.

## 6. Signatures (fictional)
| Role | Name | Decision | Date |
|---|---|---|---|
| Risk owner | Raymond Okafor, CFO | **Accept** until 2027-03-31 | 2026-08-12 |
| Security concurrence | Alicia Moreno, CISO | Concur | 2026-08-12 |
| Recorded by | Priya Raman, GRC | Entered in risk register and POA&M | 2026-08-12 |

*Accepted risks stay on the POA&M (status "Risk Accepted") so they are re-decided at expiry rather than forgotten.*
