#!/usr/bin/env python3
"""Read a fictional incident JSON file and report fields requiring clarification."""
import argparse
import json
from pathlib import Path

REQUIRED = ("severity", "impact", "started_at_utc", "actions", "current_status", "next_owner")


def missing_fields(record):
    if not isinstance(record, dict):
        raise ValueError("The incident must be a JSON object.")
    return [key for key in REQUIRED if key not in record or record[key] is None
            or (isinstance(record[key], str) and not record[key].strip())
            or record[key] == [] or record[key] == {}]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        missing = missing_fields(data)
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Cannot check incident: {exc}\n")
    print(json.dumps({"missing_fields": missing, "complete": not missing}, indent=2))


if __name__ == "__main__":
    main()
