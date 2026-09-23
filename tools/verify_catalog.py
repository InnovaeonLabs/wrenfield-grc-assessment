"""Optional: verify every control ID and title in the matrix against NIST's official OSCAL catalog.

The build does not download anything. Obtain the catalog yourself from NIST's official repository:
  https://github.com/usnistgov/oscal-content  ->  nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json

    python tools/verify_catalog.py path/to/NIST_SP-800-53_rev5_catalog.json
"""
from __future__ import annotations

import json
import re
import sys

from build import load_all


def walk(controls, out):
    for c in controls:
        out[c["id"]] = c["title"]
        walk(c.get("controls", []), out)


def main(path):
    cat = json.load(open(path, encoding="utf-8"))["catalog"]
    titles = {}
    for g in cat["groups"]:
        walk(g.get("controls", []), titles)
    version = cat["metadata"].get("version")
    bad = 0
    for c in load_all()["controls"]:
        m = re.fullmatch(r"([A-Z]{2})-(\d+)(?:\((\d+)\))?", c["id"])
        oid = f"{m.group(1).lower()}-{m.group(2)}" + (f".{m.group(3)}" if m.group(3) else "")
        official = titles.get(oid)
        ok = official is not None and official.lower() == c["name"].lower()
        if not ok:
            bad += 1
            print(f"MISMATCH {c['id']}: matrix='{c['name']}' official='{official}'")
    print(f"catalog version {version}: {len(load_all()['controls']) - bad} matched, {bad} mismatched")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1])
