#!/usr/bin/env python3
"""Validate the simple frontmatter and relative Markdown links used in this workshop.

This is not a complete YAML parser or a replacement for the Agent Skills specification.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def validate(path):
    text = path.read_text(encoding="utf-8")
    errors = []
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        return ["missing YAML frontmatter delimiters"]
    fields = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line or line.startswith(" "):
            errors.append("this checker supports only single-line top-level YAML fields")
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith(("'", '"')):
            errors.append("this checker expects unquoted single-line fields")
        if ": " in value or " #" in value:
            errors.append("quote complex YAML values and validate them with a full YAML parser")
        if key in fields:
            errors.append(f"duplicate field: {key}")
        fields[key] = value
    name = fields.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append("invalid name")
    if name != path.parent.name:
        errors.append("name must match directory")
    description = fields.get("description", "")
    if not 1 <= len(description) <= 1024:
        errors.append("description must contain 1–1024 characters")
    if not text[match.end():].strip():
        errors.append("missing instructions")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text[match.end():]):
        if not re.match(r"[a-z]+://", target) and not target.startswith("#"):
            if not (path.parent / target.split("#")[0]).exists():
                errors.append(f"missing resource: {target}")
    return errors


def main():
    skills = sorted((ROOT / ".github/skills").glob("*/SKILL.md"))
    if not skills:
        print("No skills found", file=sys.stderr)
        return 1
    failures = 0
    for path in skills:
        errors = validate(path)
        print(f"{path.relative_to(ROOT)}: {'; '.join(errors) if errors else 'OK'}")
        failures += bool(errors)
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
