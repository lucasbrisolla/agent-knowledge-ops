from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "create-agent-product.py"
VALIDATOR = ROOT / "tools" / "validate-agent-product.py"


class CreateAgentProductTest(unittest.TestCase):
    def test_creates_minimum_agent_product_contract(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "value-ops"
            result = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    str(project),
                    "--product-name",
                    "Value Ops",
                    "--description",
                    "Agente de transformação empresarial e geração de valor.",
                    "--domain",
                    "Value Management e execução estratégica",
                    "--target-user",
                    "Líderes de transformação",
                    "--recurring-use",
                    "Revisar iniciativas e capturar benefícios.",
                    "--repeated-output",
                    "Value Plan e Benefits Realization Review",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((project / "CLAUDE.md").exists())
            self.assertTrue((project / "AGENTS.md").exists())
            self.assertTrue((project / "DATA_CONTRACT.md").exists())
            self.assertTrue((project / "agent-product-spec.md").exists())
            self.assertTrue((project / "_method-wiki").is_dir())
            self.assertTrue((project / "workflows").is_dir())
            self.assertTrue((project / "evals").is_dir())

            readme = (project / "README.md").read_text(encoding="utf-8")
            spec = (project / "agent-product-spec.md").read_text(encoding="utf-8")
            domain = (project / "domain.md").read_text(encoding="utf-8")
            self.assertIn("# Value Ops", readme)
            self.assertIn("Value Management e execução estratégica", spec)
            self.assertIn("Value Plan e Benefits Realization Review", domain)
            self.assertNotIn("{{", readme)
            self.assertNotIn("{{", spec)

    def test_generated_product_passes_structural_validation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "value-ops"
            create = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    str(project),
                    "--product-name",
                    "Value Ops",
                    "--description",
                    "Agente de transformação empresarial.",
                    "--domain",
                    "Value Management",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
            self.assertEqual(create.returncode, 0, create.stderr)

            result = subprocess.run(
                ["python3", str(VALIDATOR), str(project)],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Produto válido", result.stdout)

    def test_preserves_operational_decision_fields_from_cli(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "value-ops"
            result = subprocess.run(
                [
                    "python3",
                    str(SCRIPT),
                    str(project),
                    "--product-name",
                    "Value Ops",
                    "--description",
                    "Agente de transformação empresarial.",
                    "--domain",
                    "Value Management",
                    "--state-needed",
                    "yes",
                    "--verification-needed",
                    "multiple",
                    "--recommended-form",
                    "domain-operating-system",
                    "--status",
                    "pilot",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            spec = (project / "agent-product-spec.md").read_text(encoding="utf-8")
            self.assertIn('state_needed: "yes"', spec)
            self.assertIn('recommended_form: "domain-operating-system"', spec)
            self.assertIn('status: "pilot"', spec)

    def test_validator_rejects_missing_contract_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "value-ops"
            project.mkdir()
            (project / "README.md").write_text("# Value Ops\n", encoding="utf-8")

            result = subprocess.run(
                ["python3", str(VALIDATOR), str(project)],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("CLAUDE.md", result.stderr)


if __name__ == "__main__":
    unittest.main()
