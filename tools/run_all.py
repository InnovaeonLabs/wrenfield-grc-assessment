"""One command to regenerate and verify everything.

    python tools/run_all.py

Order matters: raw evidence -> access-review engine -> assessment tests -> build artifacts ->
metrics/dashboard -> formula verification (pycel) -> cross-artifact integrity -> line-ending normalization.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STEPS = [
    ["tools/review_engine.py"],
    ["tools/assessment_tests.py", "all"],
    ["tools/build.py"],
    ["tools/metrics.py"],
    ["tools/check_formulas.py"],
    ["tools/validate.py"],
]
TEXT_EXT = {".md", ".csv", ".json", ".yaml", ".yml", ".py", ".svg", ".html", ".txt", ".toml", ".cfg"}


def normalize_line_endings():
    """Generated text uses LF regardless of OS (Windows write_text would emit CRLF)."""
    n = 0
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix in TEXT_EXT and ".venv" not in p.parts and ".git" not in p.parts:
            b = p.read_bytes()
            if b"\r\n" in b:
                p.write_bytes(b.replace(b"\r\n", b"\n"))
                n += 1
    return n


def main():
    for step in STEPS:
        print(f"==> {' '.join(step)}", flush=True)
        r = subprocess.run([sys.executable, *step], cwd=ROOT)
        if r.returncode != 0:
            print(f"FAILED: {' '.join(step)}")
            sys.exit(r.returncode)
    print(f"==> normalized line endings in {normalize_line_endings()} files")
    print("ALL STEPS PASSED")


if __name__ == "__main__":
    main()
