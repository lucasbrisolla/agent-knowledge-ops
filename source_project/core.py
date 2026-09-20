"""Contrato e validação compartilhados por todos os projetos de fonte."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


DIRECTORIES = (
    "raw",
    "library",
    "distillations",
    "promotions",
    "method-wiki",
    "operations",
    "agent-product",
)

REQUIRED_FILES = (
    "README.md",
    "source-manifest.md",
    "promotion-matrix.md",
)

SOURCE_TYPES = frozenset(
    {
        "book",
        "youtube-channel",
        "youtube-playlist",
        "reddit",
        "web-site",
        "web-articles",
        "pdf-collection",
        "earnings-calls",
        "notes",
        "mixed",
    }
)

STATUSES = frozenset(
    {
        "novo",
        "capturando",
        "indexado",
        "destilando",
        "parcialmente-promovido",
        "promovido",
        "arquivado",
    }
)

MANIFEST_FIELDS = (
    "project",
    "source_type",
    "source_name",
    "source_url",
    "owner",
    "created",
    "status",
    "target_agents",
    "probable_outputs",
)


@dataclass(frozen=True)
class SourceProjectReport:
    """Resultado observável da validação de um projeto de fonte."""

    errors: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()

    @property
    def valid(self) -> bool:
        return not self.errors


def ensure_layout(project: Path) -> Path:
    """Cria apenas a estrutura física canônica e devolve o caminho resolvido."""

    project = project.expanduser().resolve()
    project.mkdir(parents=True, exist_ok=True)
    for directory in DIRECTORIES:
        (project / directory).mkdir(parents=True, exist_ok=True)
    return project


def validate_project(project: Path) -> SourceProjectReport:
    """Valida a estrutura e os campos de controle de um projeto de fonte."""

    project = project.expanduser()
    errors: list[str] = []
    warnings: list[str] = []

    if not project.is_dir():
        return SourceProjectReport((f"projeto de fonte não encontrado: {project}",))

    for filename in REQUIRED_FILES:
        if not (project / filename).is_file():
            errors.append(f"arquivo obrigatório ausente: {filename}")

    for directory in DIRECTORIES:
        if not (project / directory).is_dir():
            errors.append(f"pasta obrigatória ausente: {directory}/")

    manifest = project / "source-manifest.md"
    if manifest.is_file():
        try:
            fields = parse_frontmatter(manifest)
        except ValueError as exc:
            errors.append(str(exc))
        else:
            for field in MANIFEST_FIELDS:
                if field not in fields:
                    errors.append(f"campo ausente em source-manifest.md: {field}")

            project_id = fields.get("project", "").strip()
            if not project_id:
                errors.append("campo vazio em source-manifest.md: project")

            for field in ("source_name", "created"):
                if not fields.get(field, "").strip():
                    errors.append(f"campo vazio em source-manifest.md: {field}")

            source_type = fields.get("source_type", "").strip()
            if source_type and source_type not in SOURCE_TYPES:
                errors.append(f"tipo de fonte inválido: {source_type}")

            status = fields.get("status", "").strip()
            if status not in STATUSES:
                errors.append(f"status de projeto inválido: {status or '[vazio]'}")

    matrix = project / "promotion-matrix.md"
    if matrix.is_file():
        content = matrix.read_text(encoding="utf-8")
        if "| ID |" not in content:
            errors.append("promotion-matrix.md não contém a tabela de decisões esperada")

    if (project / "raw").is_dir() and not any((project / "raw").iterdir()):
        warnings.append("raw/ está vazio")
    if (project / "library").is_dir() and not any((project / "library").iterdir()):
        warnings.append("library/ está vazio")

    return SourceProjectReport(tuple(errors), tuple(warnings))


def parse_frontmatter(path: Path) -> dict[str, str]:
    """Lê o frontmatter simples usado pelo manifest sem exigir YAML externo."""

    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"source-manifest.md sem frontmatter YAML: {path}")

    try:
        end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration as exc:
        raise ValueError(f"frontmatter não encerrado: {path}") from exc

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:end], start=2):
        if not line.strip():
            continue
        if ":" not in line:
            if line.lstrip().startswith(("-", "[")):
                continue
            raise ValueError(f"linha inválida no frontmatter ({line_number}): {line}")
        key, raw_value = line.split(":", 1)
        fields[key.strip()] = raw_value.strip().strip('"')
    return fields
