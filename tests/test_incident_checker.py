import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".github/skills/incident-handoff/scripts/check_incident.py"
spec = importlib.util.spec_from_file_location("incident_checker", SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class IncidentCheckerTests(unittest.TestCase):
    def test_complete_fixture(self):
        data = json.loads((ROOT / "examples/infra-incident.json").read_text())
        self.assertEqual(checker.missing_fields(data), [])

    def test_incomplete_fixture_identifies_actionable_gaps(self):
        data = json.loads((ROOT / "examples/incomplete-incident.json").read_text())
        self.assertEqual(checker.missing_fields(data), ["severity", "started_at_utc", "next_owner"])

    def test_blank_values_are_missing(self):
        data = {key: "present" for key in checker.REQUIRED}
        data.update(severity="  ", actions=[], next_owner=None)
        self.assertEqual(checker.missing_fields(data), ["severity", "actions", "next_owner"])

    def test_non_object_rejected(self):
        with self.assertRaises(ValueError):
            checker.missing_fields([])

    def test_missing_file_fails_with_explanation(self):
        result = subprocess.run([sys.executable, str(SCRIPT), str(ROOT / "does-not-exist.json")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("Cannot check incident", result.stderr)


if __name__ == "__main__":
    unittest.main()
