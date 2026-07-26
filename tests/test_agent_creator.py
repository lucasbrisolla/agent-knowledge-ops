from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import subprocess

from agent_creator.core import create_from_spec, load_spec, validate_product


VALID_SPEC = """---
product_id: "value-ops"
product_name: "Value Ops"
description: "Agente para transformar iniciativas em planos de valor verificáveis."
target_domain: "Value Management"
target_user: "Líderes de transformação"
source_basis: "escopo inicial do produto"
recurring_use: "Revisar iniciativas e capturar benefícios."
repeated_output: "Value Plan e Benefits Realization Review"
state_needed: "yes"
verification_needed: "multiple"
recommended_form: "structured-operator"
status: "candidate"
---

# Especificação De Agente-Produto — Value Ops

## Papel

Agente para estruturar e revisar iniciativas de valor.
"""


class AgentCreatorTest(unittest.TestCase):
    def test_cli_creates_product_from_specification(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec_path = root / "agent-product-spec.md"
            project = root / "value-ops"
            spec_path.write_text(VALID_SPEC, encoding="utf-8")

            result = subprocess.run(
                [
                    "python3",
                    "tools/create-agent-product-from-spec.py",
                    str(spec_path),
                    str(project),
                ],
                cwd=Path(__file__).resolve().parents[1],
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Value Ops", (project / "README.md").read_text(encoding="utf-8"))

    def test_creates_initial_architecture_from_markdown_spec(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec_path = root / "agent-product-spec.md"
            project = root / "value-ops"
            spec_path.write_text(VALID_SPEC, encoding="utf-8")

            create_from_spec(spec_path, project)

            for filename in (
                "README.md",
                "AGENTS.md",
                "CLAUDE.md",
                "DATA_CONTRACT.md",
                "PRODUCT_INDEX.md",
                "HEALTH_CHECK.md",
                "agent-product-spec.md",
                "domain.md",
                "states.yml",
            ):
                self.assertTrue((project / filename).is_file(), filename)
            for directory in (
                "_method-wiki",
                "workflows",
                "skills",
                "templates",
                "context",
                "examples",
                "evals",
                "scripts",
                "archive",
            ):
                self.assertTrue((project / directory).is_dir(), directory)

            domain = (project / "domain.md").read_text(encoding="utf-8")
            self.assertIn("Value Management", domain)
            self.assertIn("Líderes de transformação", domain)
            self.assertIn("Value Plan e Benefits Realization Review", domain)

    def test_rejects_invalid_enum_and_editorial_placeholder(self) -> None:
        invalid_spec = VALID_SPEC.replace(
            'recommended_form: "structured-operator"',
            'recommended_form: "forma-inexistente"',
        ).replace(
            'recurring_use: "Revisar iniciativas e capturar benefícios."',
            'recurring_use: "[definir]"',
        )
        with tempfile.TemporaryDirectory() as tmp:
            spec_path = Path(tmp) / "agent-product-spec.md"
            spec_path.write_text(invalid_spec, encoding="utf-8")

            with self.assertRaises(ValueError) as raised:
                load_spec(spec_path)

            message = str(raised.exception)
            self.assertIn("recommended_form", message)
            self.assertIn("recurring_use", message)

    def test_force_preserves_existing_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec_path = root / "agent-product-spec.md"
            project = root / "value-ops"
            spec_path.write_text(VALID_SPEC, encoding="utf-8")
            project.mkdir()
            (project / "README.md").write_text("# Conteúdo preservado\n", encoding="utf-8")

            create_from_spec(spec_path, project, force=True)

            self.assertEqual(
                (project / "README.md").read_text(encoding="utf-8"),
                "# Conteúdo preservado\n",
            )
            errors, warnings = validate_product(project)
            self.assertEqual(errors, [])
            self.assertEqual(warnings, [])


if __name__ == "__main__":
    unittest.main()
