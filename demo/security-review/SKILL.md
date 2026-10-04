---
name: security-review
description: Find security issues in all code and Terraform in this workspace. Use when asked for a security review or to check code for vulnerabilities.
---

# Security review

1. List all code and IaC files, except dependencies.
2. Check each file against [checklist.md](checklist.md).
3. Report with [report-template.md](report-template.md).
4. Report only. Never edit or run code.

Mark findings you are not sure about as "verify". Never invent CVE numbers.
Mask secrets: show only the first four characters.
If you find nothing, list the files you checked.
