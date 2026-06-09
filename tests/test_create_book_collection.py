from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "create-book-collection.py"


class CreateBookCollectionTest(unittest.TestCase):
    def test_creates_readme_and_index_for_book_collection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "books" / "budgeting"
            result = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    str(project),
                    "--book-title",
                    "Budgeting",
                    "--target-agent",
                    "accounting-ops",
                    "--source",
                    "/livros/budgeting.epub",
                    "--chapters",
                    "Introduction to Budgeting",
                    "The System of Budgets",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            readme = (project / "README.md").read_text(encoding="utf-8")
            index = (project / "budgeting-index.md").read_text(encoding="utf-8")

            self.assertIn("Piloto de destilação editorial de *Budgeting* para aprofundar o `accounting-ops`.", readme)
            self.assertIn("`/livros/budgeting.epub`", readme)
            self.assertIn("| 1 | Introduction to Budgeting |", index)
            self.assertIn("| 2 | The System of Budgets |", index)
            self.assertIn("`destilar`", index)


if __name__ == "__main__":
    unittest.main()
