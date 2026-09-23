"""Access-certification exception engine (AC-2, AC-2(3), AC-5, AC-6, AC-6(2), IA-2, IA-5, PS-5, PS-7).

Reconciles independent sources the way an IGA tool (or a careful analyst with
a spreadsheet) would:

    HR roster (PeopleHub)  -- authoritative worker status, role, transfers
    Okta user export       -- identity status and MFA posture
    Entitlement exports    -- per-system access levels (8 systems)
    Service-account register, role-access baseline, SoD rule set

Each check produces a machine flag. Flags are NOT findings: a human reviewer
dispositions every flagged row (see reviewer_decisions.csv), either confirming
an exception (AR-EX-##) or recording why the flag is a false positive.
The run fails if any flag is left undispositioned.

Usage:  python tools/review_engine.py
Output: access-review/access-review.csv, access-review/summary.json
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict

from common import EXPORTS, META, ROOT, SNAPSHOT, d, read_csv, write_csv, write_json

HUMAN_TYPES = {"Employee", "Contractor", "External", "Admin (separate)", "IAM user (local)"}
NON_ROTATABLE = {"OIDC federation (no stored credential)"}

FLAG_TEXT = {
    "F-TERM": "Worker terminated in HR but access active",
    "F-CONTRACT": "Contract end date passed but worker active",
    "F-INACTIVE": f"No use in > {META['thresholds']['inactivity_days']} days",
    "F-MFA": "MFA not enforced (not enrolled / exemption group)",
    "F-BASELINE": "Privileged or PHI access not in role baseline",
    "F-TRANSFER": "Access from prior role retained after transfer",
    "F-DAILYADMIN": "Privileged role on daily-use account (separate admin account required)",
    "F-SOD": "Segregation-of-duties conflict",
    "F-DUP": "Possible duplicate identity (same person, multiple accounts)",
    "F-SVC-OWNER": "Service account has no documented owner",
    "F-SVC-ROTATION": f"Credential older than {META['thresholds']['credential_max_age_days']} days",
    "F-SHARED": "Shared account (no individual accountability)",
    "F-SVC-UNREG": "Non-human account missing from service-account register",
}


def load():
    hr = {r["employee_id"]: r for r in read_csv(EXPORTS / "hr_roster.csv")}
    okta = {r["login"]: r for r in read_csv(EXPORTS / "okta_users.csv")}
    ents = read_csv(EXPORTS / "entitlements.csv")
    svc = {r["account"]: r for r in read_csv(EXPORTS / "service_accounts.csv")}
    matrix = read_csv(EXPORTS / "role_access_matrix.csv")
    sod = read_csv(EXPORTS / "sod_rules.csv")
    decisions = {r["ent_id"]: r for r in read_csv(EXPORTS / "reviewer_decisions.csv")}
    return hr, okta, ents, svc, matrix, sod, decisions


def allowed(matrix, role_code, system, level) -> bool:
    return any(m["role_code"] in (role_code, "*") and m["system"] == system and m["access_level"] == level
               for m in matrix)


def run():
    hr, okta, ents, svc, matrix, sod, decisions = load()
    th = META["thresholds"]
    sep_admin = {tuple(x) for x in META["separate_admin_required"]}
    flags: dict[str, list[str]] = defaultdict(list)

    # Index what each person holds (for SoD) and names -> ids (for duplicates)
    holdings = defaultdict(set)
    for e in ents:
        if e["employee_id"]:
            holdings[e["employee_id"]].add(f"{e['system']}:{e['access_level']}")
    ids_by_name = defaultdict(set)
    for emp in hr.values():
        ids_by_name[emp["full_name"]].add(emp["employee_id"])

    for e in ents:
        eid, acct, atype = e["employee_id"], e["account"], e["account_type"]
        worker = hr.get(eid)
        last = d(e["last_used"])

        if worker:
            if worker["hr_status"] == "Terminated":
                flags[e["ent_id"]].append("F-TERM")
            end = d(worker["contract_end_date"])
            if worker["hr_status"] == "Active" and end and end < SNAPSHOT:
                flags[e["ent_id"]].append("F-CONTRACT")
            # duplicates: this record is terminated but the same person is active under another id
            twins = [i for i in ids_by_name[worker["full_name"]] if i != eid]
            if twins and worker["hr_status"] == "Terminated" and any(hr[i]["hr_status"] == "Active" for i in twins):
                flags[e["ent_id"]].append("F-DUP")

        if atype != "Break-glass" and last and (SNAPSHOT - last).days > th["inactivity_days"]:
            flags[e["ent_id"]].append("F-INACTIVE")

        if e["system"] == "Okta" and e["access_level"].startswith("SSO account"):
            o = okta.get(acct)
            if o and (o["mfa_enrolled"] == "N" or o["in_mfa_exempt_group"] == "Y"):
                flags[e["ent_id"]].append("F-MFA")

        if atype in HUMAN_TYPES and worker and (e["privileged"] == "Y" or e["phi"] == "Y"):
            if not allowed(matrix, worker["role_code"], e["system"], e["access_level"]):
                flags[e["ent_id"]].append("F-BASELINE")
                t_date, prior = d(worker["transfer_date"]), worker["prior_role_code"]
                if t_date and d(e["date_granted"]) < t_date and prior and allowed(matrix, prior, e["system"], e["access_level"]):
                    flags[e["ent_id"]].append("F-TRANSFER")

        if (e["system"], e["access_level"]) in sep_admin and atype not in ("Admin (separate)", "Break-glass"):
            flags[e["ent_id"]].append("F-DAILYADMIN")

        if eid:
            held = holdings[eid]
            for rule in sod:
                a = rule["access_a"] if ":" in rule["access_a"] else f"{rule['system']}:{rule['access_a']}"
                b = rule["access_b"] if ":" in rule["access_b"] else f"{rule['system']}:{rule['access_b']}"
                if a in held and b in held and f"{e['system']}:{e['access_level']}" in (a, b):
                    flags[e["ent_id"]].append("F-SOD")

        if atype in ("Service", "Shared", "Break-glass"):
            reg = svc.get(acct)
            if not reg:
                flags[e["ent_id"]].append("F-SVC-UNREG")
            else:
                if not reg["owner_employee_id"]:
                    flags[e["ent_id"]].append("F-SVC-OWNER")
                rot = d(reg["credential_last_rotated"])
                if reg["credential_type"] not in NON_ROTATABLE and rot and (SNAPSHOT - rot).days > th["credential_max_age_days"]:
                    flags[e["ent_id"]].append("F-SVC-ROTATION")
        if atype == "Shared":
            flags[e["ent_id"]].append("F-SHARED")

    # ---- merge with reviewer decisions ----
    rows, errors = [], []
    for e in ents:
        eid, f = e["ent_id"], sorted(set(flags.get(e["ent_id"], [])))
        dec = decisions.get(eid)
        if f and not dec:
            errors.append(f"{eid} ({e['account']} / {e['system']}) has flags {f} but no reviewer decision")
        worker = hr.get(e["employee_id"])
        reg = svc.get(e["account"])
        owner = hr.get(reg["owner_employee_id"]) if reg and reg["owner_employee_id"] else None
        rows.append({
            "Row ID": eid,
            "User / Account": e["account"],
            "Account Type": e["account_type"],
            "Department": worker["department"] if worker else (owner["department"] + " (owner)" if owner else ""),
            "Role": worker["job_title"] if worker else (reg["purpose"] if reg else "Vendor / non-human"),
            "Manager": worker["manager"] if worker else (owner["full_name"] + " (owner)" if owner else "UNDOCUMENTED" if reg else ""),
            "HR Status": worker["hr_status"] if worker else "n/a (non-human)",
            "System": e["system"],
            "Access Level": e["access_level"],
            "Privileged?": e["privileged"],
            "PHI Access?": e["phi"],
            "Date Granted": e["date_granted"],
            "Last Login": e["last_used"],
            "Business Justification": e["justification_on_file"],
            "Reviewer": e["reviewer"],
            "Review Date": dec["review_date"] if dec else "2026-07-10",
            "Engine Flags": "; ".join(f),
            "Review Decision": dec["decision"] if dec else "Retain",
            "Exception ID": dec["exception_id"] if dec else "",
            "Issue Identified": (dec["issue_identified"] if dec and dec["exception_id"] else
                                 ("None (flag dispositioned: see comment)" if f else "None")),
            "Required Action": dec["required_action"] if dec else "",
            "Action Owner": dec["action_owner"] if dec else "",
            "Due Date": dec["due_date"] if dec else "",
            "Completion Status": dec["completion_status"] if dec else "Completed",
            "Completion Date": dec["completion_date"] if dec else "2026-07-10",
            "Closure Evidence": dec["closure_evidence"] if dec else "",
            "Related Finding": dec["related_finding"] if dec else "",
            "Affected Control": dec["affected_control"] if dec else "",
            "Reviewer Comment": dec["reviewer_comment"] if dec else "",
        })
    for eid, dec in decisions.items():
        if dec["exception_id"] and not flags.get(eid) and not dec["reviewer_comment"]:
            errors.append(f"{eid}: exception {dec['exception_id']} has no engine flag and no reviewer rationale")
    if errors:
        print("ACCESS REVIEW INTEGRITY ERRORS:\n  " + "\n  ".join(errors))
        sys.exit(1)

    fields = list(rows[0].keys())
    write_csv(ROOT / "access-review" / "access-review.csv", rows, fields)

    exc_rows = [r for r in rows if r["Exception ID"]]
    exc_ids = sorted({r["Exception ID"] for r in exc_rows})
    flagged = [r for r in rows if r["Engine Flags"]]
    fp_rows = [r for r in flagged if not r["Exception ID"]]
    flag_counts = Counter(fl for r in rows for fl in r["Engine Flags"].split("; ") if fl)
    by_ex = {}
    for x in exc_ids:
        xs = [r for r in exc_rows if r["Exception ID"] == x]
        statuses = {r["Completion Status"] for r in xs}
        status = ("Risk Accepted" if statuses == {"Risk Accepted"} else
                  "Completed" if statuses == {"Completed"} else "In Progress")
        by_ex[x] = {"rows": len(xs), "accounts": sorted({r["User / Account"] for r in xs}),
                    "finding": xs[0]["Related Finding"], "status": status,
                    "issue": xs[0]["Issue Identified"]}
    summary = {
        "snapshot_date": str(SNAPSHOT),
        "entitlement_rows_reviewed": len(rows),
        "identities_reviewed": len({r["User / Account"] for r in rows}),
        "human_identities": len({e["employee_id"] for e in ents if e["employee_id"]}),
        "systems": sorted({r["System"] for r in rows}),
        "privileged_rows": sum(r["Privileged?"] == "Y" for r in rows),
        "phi_rows": sum(r["PHI Access?"] == "Y" for r in rows),
        "flagged_rows": len(flagged),
        "flags_by_type": {k: {"count": v, "meaning": FLAG_TEXT[k]} for k, v in sorted(flag_counts.items())},
        "exception_rows": len(exc_rows),
        "exceptions": len(exc_ids),
        "false_positive_rows": len(fp_rows),
        "exceptions_detail": by_ex,
        "exceptions_by_finding": dict(Counter(v["finding"] for v in by_ex.values())),
        "exceptions_closed": sum(v["status"] == "Completed" for v in by_ex.values()),
        "exceptions_risk_accepted": sum(v["status"] == "Risk Accepted" for v in by_ex.values()),
        "exceptions_open": sum(v["status"] == "In Progress" for v in by_ex.values()),
        "decisions": dict(Counter(r["Review Decision"] for r in rows)),
        "github_owner_count": sum(r["System"] == "GitHub" and r["Access Level"] == "Organization Owner" for r in rows),
        "github_owner_max": META["thresholds"]["github_max_owners"],
        "exception_rate_pct": round(100 * len(exc_rows) / len(rows)),
    }
    write_json(ROOT / "access-review" / "summary.json", summary)
    return summary


if __name__ == "__main__":
    s = run()
    print(f"rows={s['entitlement_rows_reviewed']} privileged={s['privileged_rows']} phi={s['phi_rows']} "
          f"flagged={s['flagged_rows']} exceptions={s['exceptions']} ({s['exception_rows']} rows) "
          f"false_positives={s['false_positive_rows']} closed={s['exceptions_closed']} "
          f"accepted={s['exceptions_risk_accepted']} open={s['exceptions_open']}")
    for k, v in s["flags_by_type"].items():
        print(f"  {k:15} {v['count']:3}  {v['meaning']}")
