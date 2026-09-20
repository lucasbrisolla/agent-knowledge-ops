from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "tools" / "extract-book-source.py"


def _create_project(tmp_path: Path) -> Path:
    project = tmp_path / "book-project"
    for directory in (
        "raw",
        "library",
        "distillations",
        "promotions",
        "method-wiki",
        "operations",
        "agent-product",
    ):
        (project / directory).mkdir(parents=True)
    (project / "README.md").write_text("# Livro\n", encoding="utf-8")
    (project / "source-manifest.md").write_text(
        """---
project: "book-project"
source_type: "book"
source_name: "Livro de teste"
source_url: ""
owner: ""
created: "2026-09-20"
status: "novo"
target_agents: []
probable_outputs: []
---

# Source Manifest
""",
        encoding="utf-8",
    )
    (project / "promotion-matrix.md").write_text(
        "| ID | Fonte/Unidade | Achado |\n|---|---|---|\n",
        encoding="utf-8",
    )
    return project


def _create_fake_extractor(tmp_path: Path) -> Path:
    extractor = tmp_path / "fake-book-to-skill"
    scripts = extractor / "scripts"
    scripts.mkdir(parents=True)
    (scripts / "extract.py").write_text(
        """
import json
import os
import sys
from pathlib import Path

workdir = Path(os.environ["BOOK_SKILL_WORKDIR"])
Path(os.environ["FAKE_ARGUMENT_LOG"]).write_text(
    json.dumps(sys.argv[1:]), encoding="utf-8"
)
if os.environ.get("FAKE_EXTRACTOR_FAIL") == "1":
    print("fake extraction failed", file=sys.stderr)
    raise SystemExit(17)

(workdir / "full_text.txt").write_text(
    "Table of Contents\\n\\nChapter 1: Intake\\n\\nChapter 2: Method",
    encoding="utf-8",
)
(workdir / "metadata.json").write_text(
    json.dumps(
        {
            "filename": "sample-book.md",
            "format": "md",
            "extraction_method": "text",
            "extraction_mode": "technical",
            "file_size_mb": 0.01,
            "pages": 12,
            "chars": 58,
            "words": 9,
            "estimated_tokens": 12,
            "total_sources": 1,
            "chapters_detected": 2,
            "chapter_headings_sample": [
                "Chapter 1: Intake",
                "Chapter 2: Method",
            ],
            "has_toc": True,
            "sources": [
                {
                    "source_file": "/tmp/sample-book.md",
                    "filename": "sample-book.md",
                    "format": "md",
                    "extraction_method": "text",
                    "file_size_mb": 0.01,
                    "pages": 12,
                    "pages_label": "12",
                    "chars": 58,
                    "words": 9,
                    "estimated_tokens": 12,
                    "chapters_detected": 2,
                    "has_toc": True,
                }
            ],
        },
        ensure_ascii=False,
    ),
    encoding="utf-8",
)
""".strip()
        + "\n",
        encoding="utf-8",
    )
    return extractor


def _run_cli(
    project: Path,
    source: Path,
    extractor: Path,
    tmp_path: Path,
    *extra_args: str,
    fail: bool = False,
) -> subprocess.CompletedProcess[str]:
    argument_log = tmp_path / "arguments.json"
    environment = os.environ.copy()
    environment["FAKE_ARGUMENT_LOG"] = str(argument_log)
    if fail:
        environment["FAKE_EXTRACTOR_FAIL"] = "1"
    return subprocess.run(
        [
            sys.executable,
            str(CLI),
            str(project),
            str(source),
            "--extractor-root",
            str(extractor),
            *extra_args,
        ],
        cwd=ROOT,
        env=environment,
        text=True,
        capture_output=True,
    )


def test_extract_book_source_materializes_raw_and_library_contract(tmp_path: Path) -> None:
    project = _create_project(tmp_path)
    extractor = _create_fake_extractor(tmp_path)
    source = tmp_path / "sample-book.md"
    source.write_text("# Sample book\n", encoding="utf-8")

    result = _run_cli(project, source, extractor, tmp_path, "--mode", "technical")

    assert result.returncode == 0, result.stderr
    assert (project / "raw" / "full_text.txt").read_text(encoding="utf-8").startswith(
        "Table of Contents"
    )
    metadata = json.loads((project / "raw" / "metadata.json").read_text(encoding="utf-8"))
    assert metadata["chapters_detected"] == 2
    assert metadata["output_text"] == str(project / "raw" / "full_text.txt")
    assert metadata["intake_tool"] == "book-to-skill"

    index = (project / "library" / "book-index.md").read_text(encoding="utf-8")
    assert "# Índice De Livro" in index
    assert "Chapter 1: Intake" in index
    assert "12" in index
    assert "../raw/full_text.txt" in index
    assert not (project / "SKILL.md").exists()

    forwarded = json.loads((tmp_path / "arguments.json").read_text(encoding="utf-8"))
    assert "--mode" in forwarded
    assert "technical" in forwarded
    assert "--install-missing" in forwarded
    assert "no" in forwarded


def test_extract_book_source_does_not_leave_partial_artifacts_on_failure(tmp_path: Path) -> None:
    project = _create_project(tmp_path)
    extractor = _create_fake_extractor(tmp_path)
    source = tmp_path / "sample-book.md"
    source.write_text("# Sample book\n", encoding="utf-8")

    result = _run_cli(project, source, extractor, tmp_path, fail=True)

    assert result.returncode == 17
    assert "fake extraction failed" in result.stderr
    assert not (project / "raw" / "full_text.txt").exists()
    assert not (project / "raw" / "metadata.json").exists()
    assert not (project / "library" / "book-index.md").exists()


def test_extract_book_source_requires_overwrite_for_existing_artifacts(tmp_path: Path) -> None:
    project = _create_project(tmp_path)
    extractor = _create_fake_extractor(tmp_path)
    source = tmp_path / "sample-book.md"
    source.write_text("# Sample book\n", encoding="utf-8")

    first = _run_cli(project, source, extractor, tmp_path)
    assert first.returncode == 0, first.stderr
    full_text = project / "raw" / "full_text.txt"
    full_text.write_text("conteúdo preservado\n", encoding="utf-8")

    second = _run_cli(project, source, extractor, tmp_path)

    assert second.returncode == 1
    assert "--overwrite" in second.stderr
    assert full_text.read_text(encoding="utf-8") == "conteúdo preservado\n"


def test_extract_book_source_rejects_incomplete_project(tmp_path: Path) -> None:
    project = tmp_path / "incomplete-project"
    project.mkdir()
    extractor = _create_fake_extractor(tmp_path)
    source = tmp_path / "sample-book.md"
    source.write_text("# Sample book\n", encoding="utf-8")

    result = _run_cli(project, source, extractor, tmp_path)

    assert result.returncode == 1
    assert "raw" in result.stderr
    assert "library" in result.stderr
