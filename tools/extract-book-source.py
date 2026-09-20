#!/usr/bin/env python3
"""Extrai livros para os artefatos de intake de um projeto de fonte."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source_project import validate_project as validate_source_project  # noqa: E402


class IntakeError(RuntimeError):
    """Erro de configuração ou contrato do intake."""


class ExtractorError(RuntimeError):
    """Erro retornado pelo extrator externo."""

    def __init__(self, returncode: int) -> None:
        super().__init__(f"o extrator terminou com código {returncode}")
        self.returncode = returncode


@dataclass(frozen=True)
class ExtractorOutput:
    """Resultado normalizado que atravessa o seam do extrator externo."""

    text_path: Path
    metadata: dict[str, object]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Extrai um livro para raw/ e cria um índice em library/ "
            "sem promover o conteúdo para uma skill."
        )
    )
    parser.add_argument("project", help="Projeto de fonte já criado")
    parser.add_argument(
        "sources",
        nargs="+",
        help="Arquivo, pasta ou glob aceito pelo book-to-skill",
    )
    parser.add_argument(
        "--extractor-root",
        default="",
        help="Pasta do book-to-skill; alternativa: BOOK_TO_SKILL_ROOT",
    )
    parser.add_argument(
        "--mode",
        choices=("technical", "text"),
        default="text",
        help="Modo de extração encaminhado ao book-to-skill",
    )
    parser.add_argument(
        "--install-missing",
        choices=("ask", "yes", "no"),
        default="no",
        help="Política de instalação de dependências do extrator",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Permite substituir os artefatos gerados anteriormente",
    )
    return parser


def resolve_extractor_script(explicit_root: str) -> Path:
    root_value = explicit_root or os.environ.get("BOOK_TO_SKILL_ROOT", "")
    if not root_value:
        raise IntakeError(
            "extrator não configurado; use --extractor-root ou "
            "defina BOOK_TO_SKILL_ROOT"
        )

    root = Path(root_value).expanduser()
    script = root / "scripts" / "extract.py"
    if not script.is_file():
        raise IntakeError(f"extrator não encontrado em: {script}")
    return script.resolve()


def validate_project(project: Path) -> None:
    report = validate_source_project(project)
    if report.errors:
        raise IntakeError("projeto de fonte inválido: " + "; ".join(report.errors))


def artifact_paths(project: Path) -> tuple[Path, Path, Path]:
    return (
        project / "raw" / "full_text.txt",
        project / "raw" / "metadata.json",
        project / "library" / "book-index.md",
    )


def validate_output_state(project: Path, overwrite: bool) -> None:
    existing = [path for path in artifact_paths(project) if path.exists()]
    if existing and not overwrite:
        names = ", ".join(str(path.relative_to(project)) for path in existing)
        raise IntakeError(
            f"artefatos já existem: {names}. Use --overwrite para substituir"
        )


def run_extractor(
    extractor_script: Path,
    sources: list[str],
    mode: str,
    install_missing: str,
    workdir: Path,
) -> None:
    command = [
        sys.executable,
        str(extractor_script),
        *sources,
        "--mode",
        mode,
        "--install-missing",
        install_missing,
    ]
    environment = os.environ.copy()
    environment["BOOK_SKILL_WORKDIR"] = str(workdir)

    result = subprocess.run(
        command,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode:
        raise ExtractorError(result.returncode)


def load_extractor_output(workdir: Path) -> ExtractorOutput:
    text_path = workdir / "full_text.txt"
    metadata_path = workdir / "metadata.json"
    missing = [path.name for path in (text_path, metadata_path) if not path.is_file()]
    if missing:
        raise IntakeError(
            "o extrator terminou sem produzir: " + ", ".join(missing)
        )

    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise IntakeError(f"metadata.json inválido: {exc}") from exc
    if not isinstance(metadata, dict):
        raise IntakeError("metadata.json deve conter um objeto JSON")
    return ExtractorOutput(text_path=text_path, metadata=metadata)


def as_text(value: object, fallback: str = "não informado") -> str:
    if value is None or value == "":
        return fallback
    return str(value)


def escape_table_cell(value: object) -> str:
    return as_text(value).replace("|", "\\|").replace("\n", " ")


def render_book_index(metadata: dict[str, object], sources: list[str]) -> str:
    source_entries = metadata.get("sources")
    if not isinstance(source_entries, list):
        source_entries = []

    headings = metadata.get("chapter_headings_sample")
    if not isinstance(headings, list):
        headings = []

    lines = [
        "# Índice De Livro",
        "",
        "Índice de intake gerado a partir do `book-to-skill`.",
        "",
        "## Regra Editorial",
        "",
        "Esta pasta contém matéria-prima e navegação inicial. O conteúdo ainda",
        "não foi destilado nem promovido para `method-wiki/`, `operations/` ou",
        "`agent-product/`.",
        "",
        "## Intake",
        "",
        f"- Data: `{date.today().isoformat()}`",
        f"- Fonte(s) solicitada(s): {', '.join(f'`{source}`' for source in sources)}",
        f"- Formato detectado: `{escape_table_cell(metadata.get('format'))}`",
        f"- Método de extração: `{escape_table_cell(metadata.get('extraction_method'))}`",
        f"- Modo: `{escape_table_cell(metadata.get('extraction_mode'))}`",
        f"- Total de fontes: `{escape_table_cell(metadata.get('total_sources', len(source_entries)))}`",
        f"- Páginas: `{escape_table_cell(metadata.get('pages', 0))}`",
        f"- Palavras: `{escape_table_cell(metadata.get('words', 0))}`",
        f"- Tokens estimados: `{escape_table_cell(metadata.get('estimated_tokens', 0))}`",
        f"- Capítulos detectados: `{escape_table_cell(metadata.get('chapters_detected', 0))}`",
        f"- Sumário detectado: `{escape_table_cell('sim' if metadata.get('has_toc') else 'não')}`",
        "",
        "Artefatos: [texto extraído](../raw/full_text.txt) · [metadados](../raw/metadata.json)",
        "",
        "## Fontes Processadas",
        "",
        "| Arquivo | Formato | Método | Páginas | Capítulos | Sumário |",
        "|---|---|---|---:|---:|---|",
    ]

    if source_entries:
        for entry in source_entries:
            if not isinstance(entry, dict):
                continue
            lines.append(
                "| "
                + " | ".join(
                    (
                        escape_table_cell(entry.get("filename")),
                        escape_table_cell(entry.get("format")),
                        escape_table_cell(entry.get("extraction_method")),
                        escape_table_cell(entry.get("pages", 0)),
                        escape_table_cell(entry.get("chapters_detected", 0)),
                        escape_table_cell("sim" if entry.get("has_toc") else "não"),
                    )
                )
                + " |"
            )
    else:
        lines.append("| não informado | não informado | não informado | 0 | 0 | não |")

    lines.extend(["", "## Capítulos Detectados", ""])
    if headings:
        lines.extend(f"- {heading}" for heading in headings)
    else:
        lines.append("- Nenhum título de capítulo foi incluído nos metadados.")

    lines.extend(
        [
            "",
            "## Próxima Etapa",
            "",
            "Escolher uma unidade e aplicar `book-distillation` antes de qualquer",
            "promoção. Se o destino já for um `_method-wiki` existente, usar",
            "`book-to-method-wiki`.",
            "",
        ]
    )
    return "\n".join(lines)


def materialize(
    project: Path,
    sources: list[str],
    extractor_root: str,
    mode: str,
    install_missing: str,
    overwrite: bool,
) -> tuple[Path, Path, Path]:
    project = project.expanduser().resolve()
    validate_project(project)
    validate_output_state(project, overwrite)
    extractor_script = resolve_extractor_script(extractor_root)

    with tempfile.TemporaryDirectory(prefix="ako-book-intake-") as temporary:
        workdir = Path(temporary)
        run_extractor(extractor_script, sources, mode, install_missing, workdir)
        output = load_extractor_output(workdir)
        text_path, metadata_path, index_path = artifact_paths(project)

        with tempfile.TemporaryDirectory(prefix=".ako-book-intake-", dir=project) as staging:
            staging_path = Path(staging)
            staged_text = staging_path / "full_text.txt"
            staged_metadata = staging_path / "metadata.json"
            staged_index = staging_path / "book-index.md"

            shutil.copyfile(output.text_path, staged_text)
            metadata = dict(output.metadata)
            metadata["output_text"] = str(text_path)
            metadata["intake_tool"] = "book-to-skill"
            metadata["intake_date"] = date.today().isoformat()
            staged_metadata.write_text(
                json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            staged_index.write_text(
                render_book_index(metadata, sources), encoding="utf-8"
            )
            commit_artifacts(
                {
                    text_path: staged_text,
                    metadata_path: staged_metadata,
                    index_path: staged_index,
                },
                staging_path,
                overwrite,
            )

    return text_path, metadata_path, index_path


def commit_artifacts(
    staged: dict[Path, Path],
    staging_path: Path,
    overwrite: bool,
) -> None:
    """Instala o conjunto de artefatos e restaura o estado em caso de falha."""

    backups: dict[Path, Path] = {}
    installed: list[Path] = []
    try:
        for destination in staged:
            if destination.exists():
                if not overwrite:
                    raise IntakeError(
                        f"artefatos já existem: {destination.name}. Use --overwrite para substituir"
                    )
                backup = staging_path / f"backup-{len(backups)}-{destination.name}"
                shutil.copy2(destination, backup)
                backups[destination] = backup

        for destination, source in staged.items():
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            installed.append(destination)
    except OSError as exc:
        for destination in installed:
            backup = backups.get(destination)
            if backup and backup.is_file():
                shutil.copyfile(backup, destination)
            else:
                destination.unlink(missing_ok=True)
        raise IntakeError(f"não foi possível materializar o intake: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        text_path, metadata_path, index_path = materialize(
            project=Path(args.project),
            sources=args.sources,
            extractor_root=args.extractor_root,
            mode=args.mode,
            install_missing=args.install_missing,
            overwrite=args.overwrite,
        )
    except ExtractorError as exc:
        return exc.returncode
    except IntakeError as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 1

    print("Intake de livro concluído.")
    print(f"Texto: {text_path}")
    print(f"Metadados: {metadata_path}")
    print(f"Índice: {index_path}")
    print("Próxima etapa: escolher uma unidade e aplicar book-distillation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
