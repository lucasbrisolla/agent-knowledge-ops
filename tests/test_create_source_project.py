from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "create-source-project.py"


class CreateSourceProjectTemplateTest(unittest.TestCase):
    def test_templates_set_source_type_and_add_template_guidance(self) -> None:
        cases = [
            ("youtube", "youtube-channel", "Unidade principal: vídeo"),
            ("book", "book", "Unidade principal: capítulo"),
            ("earnings-calls", "earnings-calls", "Unidade principal: empresa + trimestre"),
        ]

        with tempfile.TemporaryDirectory() as tmp:
            for template, source_type, expected_guidance in cases:
                with self.subTest(template=template):
                    project = Path(tmp) / template
                    result = subprocess.run(
                        [
                            "python3",
                            str(SCRIPT),
                            str(project),
                            "--template",
                            template,
                            "--source-name",
                            f"Fonte {template}",
                            "--target-agent",
                            "accounting-ops",
                        ],
                        cwd=ROOT,
                        text=True,
                        capture_output=True,
                    )

                    self.assertEqual(result.returncode, 0, result.stderr)
                    manifest = (project / "source-manifest.md").read_text(encoding="utf-8")
                    readme = (project / "README.md").read_text(encoding="utf-8")

                    self.assertIn(f'source_type: "{source_type}"', manifest)
                    self.assertIn(expected_guidance, manifest)
                    self.assertIn(f"Tipo de fonte: {source_type}", readme)


if __name__ == "__main__":
    unittest.main()
