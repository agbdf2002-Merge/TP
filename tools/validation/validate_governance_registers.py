#!/usr/bin/env python3
"""
Validate Technology Policy governance registers.

This script is intentionally lightweight and dependency-free so it can run in
GitHub Actions without installing third-party packages.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FILES = {
    "requirements": ROOT / "registers/master/master_requirements_register_expanded.csv",
    "controls": ROOT / "registers/master/master_control_register_expanded.csv",
    "evidence": ROOT / "governance/evidence/evidence_library_register.csv",
    "rtm": ROOT / "registers/traceability/regulatory_traceability_matrix_expanded.csv",
}

PATTERNS = {
    "requirement": re.compile(r"^ETP-RQ-\d{4}$"),
    "control": re.compile(r"^CTRL-\d{3}$"),
    "evidence": re.compile(r"^EVD-\d{3}$"),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path}")
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def require_columns(name: str, rows: list[dict[str, str]], columns: list[str]) -> None:
    if not rows:
        raise AssertionError(f"{name} is empty")
    available = set(rows[0].keys())
    missing = [col for col in columns if col not in available]
    if missing:
        raise AssertionError(f"{name} missing columns: {missing}")


def unique_values(name: str, rows: list[dict[str, str]], column: str) -> set[str]:
    values: list[str] = []
    for row in rows:
        value = row.get(column, "").strip()
        if not value:
            raise AssertionError(f"{name} row missing {column}: {row}")
        values.append(value)
    duplicates = sorted({v for v in values if values.count(v) > 1})
    if duplicates:
        raise AssertionError(f"{name} has duplicate {column} values: {duplicates}")
    return set(values)


def validate_pattern(name: str, values: set[str], pattern: re.Pattern[str]) -> None:
    invalid = sorted(v for v in values if not pattern.match(v))
    if invalid:
        raise AssertionError(f"{name} has invalid IDs: {invalid}")


def main() -> int:
    errors: list[str] = []
    try:
        requirements = read_csv(FILES["requirements"])
        controls = read_csv(FILES["controls"])
        evidence = read_csv(FILES["evidence"])
        rtm = read_csv(FILES["rtm"])

        require_columns("requirements", requirements, ["Requirement_ID"])
        require_columns("controls", controls, ["Control_ID", "Requirement_ID"])
        require_columns("evidence", evidence, ["Evidence_ID", "Requirement_ID", "Control_ID"])
        require_columns("rtm", rtm, ["RTM_ID", "Requirement_ID", "Control_ID", "Evidence_Object"])

        req_ids = unique_values("requirements", requirements, "Requirement_ID")
        ctrl_ids = unique_values("controls", controls, "Control_ID")
        evd_ids = unique_values("evidence", evidence, "Evidence_ID")
        rtm_ids = unique_values("rtm", rtm, "RTM_ID")

        validate_pattern("requirements", req_ids, PATTERNS["requirement"])
        validate_pattern("controls", ctrl_ids, PATTERNS["control"])
        validate_pattern("evidence", evd_ids, PATTERNS["evidence"])

        missing_req_from_controls = sorted({r["Requirement_ID"].strip() for r in controls} - req_ids)
        if missing_req_from_controls:
            raise AssertionError(f"controls reference missing requirements: {missing_req_from_controls}")

        missing_req_from_evidence = sorted({r["Requirement_ID"].strip() for r in evidence} - req_ids)
        if missing_req_from_evidence:
            raise AssertionError(f"evidence references missing requirements: {missing_req_from_evidence}")

        missing_ctrl_from_evidence = sorted({r["Control_ID"].strip() for r in evidence} - ctrl_ids)
        if missing_ctrl_from_evidence:
            raise AssertionError(f"evidence references missing controls: {missing_ctrl_from_evidence}")

        missing_req_from_rtm = sorted({r["Requirement_ID"].strip() for r in rtm} - req_ids)
        if missing_req_from_rtm:
            raise AssertionError(f"rtm references missing requirements: {missing_req_from_rtm}")

        missing_ctrl_from_rtm = sorted({r["Control_ID"].strip() for r in rtm} - ctrl_ids)
        if missing_ctrl_from_rtm:
            raise AssertionError(f"rtm references missing controls: {missing_ctrl_from_rtm}")

        missing_evd_from_rtm = sorted({r["Evidence_Object"].strip() for r in rtm} - evd_ids)
        if missing_evd_from_rtm:
            raise AssertionError(f"rtm references missing evidence objects: {missing_evd_from_rtm}")

        print("Governance register validation passed")
        print(f"Requirements: {len(req_ids)}")
        print(f"Controls: {len(ctrl_ids)}")
        print(f"Evidence objects: {len(evd_ids)}")
        print(f"RTM rows: {len(rtm_ids)}")
        return 0

    except AssertionError as exc:
        errors.append(str(exc))

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
