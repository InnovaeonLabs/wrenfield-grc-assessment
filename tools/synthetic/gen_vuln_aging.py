"""Generate the synthetic vulnerability-aging export used as EVID-048.

Transparency note: the evidence in this portfolio is synthetic. This generator
is committed so anyone can see exactly how the dataset was built. The counts
are fixed on purpose (see ALLOCATION), so the SI-2 test result is deterministic.

    python tools/synthetic/gen_vuln_aging.py
"""
import csv
import datetime as dt
import random
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "evidence" / "RA" / "EVID-048_vuln-remediation-aging-2026H1.csv"
SNAP = dt.date(2026, 6, 30)
SLA = {"Critical": 15, "High": 30}
rng = random.Random(20260630)

CONTAINER = ["wcp-api", "care-plan-svc", "fhir-gateway", "rpm-ingest", "auth-proxy", "integration-engine"]
NODES = ["eks-node-ami-2026.01", "eks-node-ami-2026.03", "eks-node-ami-2026.05"]
TITLES = {
    "container": ["Outdated OpenSSL in base image", "Vulnerable JSON parser dependency", "Prototype pollution in npm package",
                  "HTTP/2 rapid-reset DoS in web framework", "Path traversal in static-file middleware", "XML external entity in parser library"],
    "node": ["Kernel privilege-escalation patch missing", "Container runtime escape patch missing", "glibc buffer overflow patch missing"],
}

# (severity, outcome, count): the allocation IS the test's expected result
ALLOCATION = [
    ("Critical", "met", 7), ("Critical", "open_breach", 2),
    ("High", "met", 40), ("High", "late", 8), ("High", "open_breach", 4),
]
FIXED_OPEN = {  # named open breaches that tie to other findings
    ("Critical", 0): ("notify-worker", "container", "Y", "OpenSSL 1.1.1 (end-of-life) in node:16 base image - multiple critical CVEs", "N (engineering: no network-reachable path)"),
    ("Critical", 1): ("notify-worker", "container", "Y", "Node.js 16 runtime end-of-life - unpatched HTTP parser flaw", "N (engineering: no network-reachable path)"),
    ("High", 0): ("wf-sftp-01", "ec2-windows", "Y", "Windows Server 2012 R2 cumulative security update unavailable (OS out of support)", "Y"),
    ("High", 1): ("wf-sftp-01", "ec2-windows", "Y", "SMB signing not required / legacy protocol enabled", "Y"),
    ("High", 2): ("wf-sftp-01", "ec2-windows", "Y", "Third-party SFTP server version with known auth bypass (vendor patch requires OS upgrade)", "Y"),
    ("High", 3): ("legacy-reports", "ec2-linux", "N", "PostgreSQL 11 out of community support - unpatched privilege escalation", "Y"),
}


def main():
    rows, n = [], 0
    open_idx = {"Critical": 0, "High": 0}
    for sev, outcome, count in ALLOCATION:
        for _ in range(count):
            n += 1
            sla = SLA[sev]
            if outcome == "open_breach":
                asset, atype, inet, title, reach = FIXED_OPEN[(sev, open_idx[sev])]
                open_idx[sev] += 1
                age = rng.randint(sla + 12, sla + 60)
                first = SNAP - dt.timedelta(days=age)
                rows.append(dict(vuln_id=f"VULN-{26000 + n}", asset=asset, asset_type=atype, internet_facing=inet,
                                 severity=sev, title=title, first_detected=first.isoformat(), remediated="",
                                 status="Open", sla_days=sla, exploitable_path_claimed=reach, exception_ref=""))
                continue
            if rng.random() < 0.7:
                asset, atype, title = rng.choice(CONTAINER), "container", rng.choice(TITLES["container"])
            else:
                asset, atype, title = rng.choice(NODES), "eks-node", rng.choice(TITLES["node"])
            days = rng.randint(2, sla) if outcome == "met" else rng.randint(sla + 3, sla + 44)
            first = dt.date(2026, 1, 1) + dt.timedelta(days=rng.randint(0, 175 - days))
            rows.append(dict(vuln_id=f"VULN-{26000 + n}", asset=asset, asset_type=atype,
                             internet_facing="Y" if asset in ("wcp-api", "fhir-gateway", "auth-proxy") else "N",
                             severity=sev, title=title, first_detected=first.isoformat(),
                             remediated=(first + dt.timedelta(days=days)).isoformat(), status="Remediated",
                             sla_days=sla, exploitable_path_claimed="", exception_ref=""))
    rows.sort(key=lambda r: r["first_detected"])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} rows -> {OUT}")


if __name__ == "__main__":
    main()
