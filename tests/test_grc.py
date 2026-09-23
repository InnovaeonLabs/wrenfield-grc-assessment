"""Regression tests: the numbers quoted in the reports must stay true to the evidence.

    pytest -q
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import assessment_tests  # noqa: E402
import review_engine  # noqa: E402
import validate  # noqa: E402
from build import load_all  # noqa: E402


def test_termination_test_reproduces_finding_001():
    r = assessment_tests.termination()
    assert (r["population"], r["within_sla"], r["late"], r["not_deactivated"]) == (19, 16, 1, 2)
    assert r["local_accounts_active_for_terminated"] == ["mfeld-admin"]
    assert r["final_pay_refs_present"] == 19  # IPE completeness check


def test_remediation_validation_supports_closure_of_poam_001():
    r = assessment_tests.termination_validation()
    assert r["within_sla"] == r["population"] == 7
    assert r["job_exceptions_total"] == 0
    assert r["iam_users_remaining"] == ["aws-breakglass"]


def test_log_review_vuln_and_change_tests():
    assert (lambda r: (r["performed"], r["effective"]))(assessment_tests.logreview()) == (19, 17)
    v = assessment_tests.vulnsla()
    assert (v["population"], v["breached"], v["open_past_sla"], v["open_past_sla_critical"]) == (61, 14, 6, 2)
    c = assessment_tests.changes()
    assert (c["sample"], c["exceptions"]) == (25, 3)


def test_access_review_engine():
    s = review_engine.run()
    assert s["entitlement_rows_reviewed"] == 106
    assert s["exceptions"] == 20 and s["exception_rows"] == 28
    assert s["false_positive_rows"] == 1  # the IR-Responder role, dispositioned by the reviewer
    assert (s["exceptions_closed"], s["exceptions_risk_accepted"], s["exceptions_open"]) == (18, 1, 1)


def test_all_integrity_rules_pass():
    results = validate.run(load_all())
    failures = {rid: f for rid, _, f in results if f}
    assert not failures, failures


def test_scope_counts_match_documents():
    D = load_all()
    assert len(D["controls"]) == 61
    assert len({c["family"] for c in D["controls"]}) == 18
    assert 12 <= len(D["risks"]) <= 20
    assert sum(p["status"] == "Closed" for p in D["poam"]) >= 5
    scope = (ROOT / "docs/scope/scope-statement.md").read_text(encoding="utf-8")
    assert "**61 controls and enhancements across 18 families.**" in scope


def test_dashboard_formulas_match_python_metrics():
    fc = json.loads((ROOT / "dashboard/formula-check.json").read_text(encoding="utf-8"))
    assert fc["errors"] == 0 and fc["dashboard_mismatches"] == 0 and fc["formulas_evaluated"] > 1000
