"""Shared helpers: paths, data loading, dates, and risk-band math.

Every generator and check imports from here so thresholds and dates
live in exactly one place (data/meta.yaml).
"""
from __future__ import annotations

import csv
import datetime as dt
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
EXPORTS = ROOT / "access-review" / "source-exports"


def load_yaml(name: str):
    with open(DATA / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


META = load_yaml("meta.yaml")


def d(value) -> dt.date | None:
    """Parse YYYY-MM-DD (or pass through a date); blank -> None."""
    if value in (None, ""):
        return None
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    return dt.date.fromisoformat(str(value)[:10])


STATUS_DATE = d(META["status_date"])
SNAPSHOT = d(META["access_snapshot_date"])


def band(score: int | None) -> str:
    if not score:
        return ""
    for b in META["risk_bands"]:
        if score >= b["min"]:
            return b["band"]
    return "Low"


def read_csv(path: Path) -> list[dict]:
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:  # BOM so Excel renders UTF-8
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if r.get(k) is None else r.get(k)) for k in fields})


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, default=str) + "\n", encoding="utf-8")


def split_ids(value) -> list[str]:
    """'A; B, C' -> ['A','B','C'] (also accepts lists)."""
    if not value:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    return [p.strip() for p in str(value).replace(",", ";").split(";") if p.strip()]


def md_table(rows: list[dict], cols: list[str], headers: list[str] | None = None) -> str:
    headers = headers or cols
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    for r in rows:
        cells = [str(r.get(c, "") if r.get(c) is not None else "").replace("|", "\\|").replace("\n", " ") for c in cols]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def replace_between_markers(path: Path, key: str, content: str) -> None:
    """Replace text between <!-- GEN:key:START --> and <!-- GEN:key:END --> markers."""
    start, end = f"<!-- GEN:{key}:START -->", f"<!-- GEN:{key}:END -->"
    text = path.read_text(encoding="utf-8")
    if start not in text or end not in text:
        raise ValueError(f"markers for {key} not found in {path}")
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    path.write_text(f"{before}{start}\n{content.strip()}\n{end}{after}", encoding="utf-8")
