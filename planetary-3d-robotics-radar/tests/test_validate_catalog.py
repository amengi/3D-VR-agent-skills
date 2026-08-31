from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).parents[1]
SCRIPT = SKILL_ROOT / "scripts" / "validate_catalog.py"
CATALOG = SKILL_ROOT / "references" / "paper-catalog.json"


class CatalogValidatorTests(unittest.TestCase):
    def run_validator(self, path: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(path)],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_bundled_catalog_is_valid(self) -> None:
        result = self.run_validator(CATALOG)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("papers validated", result.stdout)

    def test_score_arithmetic_failure_is_reported(self) -> None:
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
        data["papers"][0]["total"] += 1
        with tempfile.TemporaryDirectory() as directory:
            bad_catalog = Path(directory) / "bad.json"
            bad_catalog.write_text(json.dumps(data), encoding="utf-8")
            result = self.run_validator(bad_catalog)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("score sum", result.stderr)


if __name__ == "__main__":
    unittest.main()
