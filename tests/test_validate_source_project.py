from __future__ import annotations

import subprocess
from pathlib import Path

from source_project import validate_project


ROOT = Path(__file__).resolve().parents[1]
CREATE = ROOT / "tools" / "create-source-project.py"
VALIDATE = ROOT / "tools" / "validate-source-project.py"


def test_created_book_project_satisfies_the_source_contract(tmp_path: Path) -> None:
    project = tmp_path / "book-project"
    created = subprocess.run(
        [
            "python3",
            str(CREATE),
            str(project),
            "--template",
            "book",
            "--source-name",
            "Livro de teste",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert created.returncode == 0, created.stderr
    report = validate_project(project)

    assert report.errors == ()
    assert "raw/ está vazio" in report.warnings
    assert "library/ está vazio" in report.warnings

    validated = subprocess.run(
        ["python3", str(VALIDATE), str(project)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert validated.returncode == 0, validated.stderr
    assert "Projeto de fonte válido" in validated.stdout


def test_validator_reports_missing_control_files_and_invalid_status(tmp_path: Path) -> None:
    project = tmp_path / "broken-project"
    project.mkdir()
    (project / "source-manifest.md").write_text(
        """---
project: "broken"
source_type: "book"
source_name: "Livro"
source_url: ""
owner: ""
created: "2026-09-20"
status: "inventado"
target_agents: []
probable_outputs: []
---
""",
        encoding="utf-8",
    )

    report = validate_project(project)

    assert any("README.md" in error for error in report.errors)
    assert any("promotion-matrix.md" in error for error in report.errors)
    assert any("status de projeto inválido" in error for error in report.errors)
