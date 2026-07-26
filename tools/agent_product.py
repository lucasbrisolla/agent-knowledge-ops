"""Shared helpers for creating and validating agent-product scaffolds."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path


PRODUCT_DIRECTORIES = [
    "_method-wiki",
    "workflows",
    "skills",
    "templates",
    "context",
    "examples",
    "evals",
    "scripts",
    "archive",
]

ROOT_TEMPLATES = {
    "AGENTS.md": "agent-product-agents.md",
    "CLAUDE.md": "agent-product-claude.md",
    "README.md": "agent-product-readme.md",
    "DATA_CONTRACT.md": "agent-product-data-contract.md",
    "PRODUCT_INDEX.md": "agent-product-index.md",
    "HEALTH_CHECK.md": "agent-product-health-check.md",
    "agent-product-spec.md": "agent-product-spec.md",
    "domain.md": "agent-product-domain.md",
    "states.yml": "agent-product-states.yml",
}

DIRECTORY_PURPOSES = {
    "_method-wiki": "Método reutilizável para pensar, diagnosticar, decidir e revisar.",
    "workflows": "Sequências operacionais recorrentes com entradas, passos, outputs e verificações.",
    "skills": "Transformações atômicas que o agente pode reutilizar em mais de um workflow.",
    "templates": "Formatos mínimos para entradas, decisões e outputs canônicos.",
    "context": "Contexto específico, fontes vivas, empresas, casos e dados situados.",
    "examples": "Exemplos curtos para calibrar método, routing e qualidade de output.",
    "evals": "Casos de avaliação para comparar outputs e identificar regressões.",
    "scripts": "Verificações e utilitários locais, preferencialmente determinísticos.",
    "archive": "Material histórico que não pertence ao fluxo operacional ativo.",
}


@dataclass(frozen=True)
class ProductSpec:
    slug: str
    name: str
    description: str
    domain: str
    target_user: str
    recurring_use: str
    repeated_output: str
    source_basis: str
    state_needed: str
    verification_needed: str
    recommended_form: str
    status: str

    @property
    def values(self) -> dict[str, str]:
        return {
            "PRODUCT_SLUG": self.slug,
            "PRODUCT_NAME": self.name,
            "DESCRIPTION": self.description,
            "DOMAIN": self.domain,
            "TARGET_USER": self.target_user,
            "RECURRING_USE": self.recurring_use,
            "REPEATED_OUTPUT": self.repeated_output,
            "SOURCE_BASIS": self.source_basis,
            "STATE_NEEDED": self.state_needed,
            "VERIFICATION_NEEDED": self.verification_needed,
            "RECOMMENDED_FORM": self.recommended_form,
            "STATUS": self.status,
            "TODAY": date.today().isoformat(),
        }


def slugify(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower())
    return value.strip("-") or "agent-product"


def render_template(template: str, values: dict[str, str]) -> str:
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered.rstrip() + "\n"


def template_root() -> Path:
    return Path(__file__).resolve().parents[1] / "templates"


def write_if_missing(path: Path, content: str) -> None:
    if path.exists():
        return
    path.write_text(content, encoding="utf-8")


def create_product(project: Path, spec: ProductSpec, force: bool = False) -> None:
    if project.exists() and any(project.iterdir()) and not force:
        raise SystemExit(f"Pasta já existe e não está vazia: {project}. Use --force para completar.")

    project.mkdir(parents=True, exist_ok=True)
    for directory in PRODUCT_DIRECTORIES:
        (project / directory).mkdir(parents=True, exist_ok=True)

    values = spec.values
    templates = template_root()
    for destination, source in ROOT_TEMPLATES.items():
        content = (templates / source).read_text(encoding="utf-8")
        write_if_missing(project / destination, render_template(content, values))

    for directory, purpose in DIRECTORY_PURPOSES.items():
        content = (templates / "agent-product-directory-readme.md").read_text(encoding="utf-8")
        directory_values = {**values, "DIRECTORY_NAME": directory, "DIRECTORY_PURPOSE": purpose}
        write_if_missing(
            project / directory / "README.md",
            render_template(content, directory_values),
        )


def validate_product(project: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not project.is_dir():
        return [f"Pasta do produto não encontrada: {project}"], warnings

    for filename in ROOT_TEMPLATES:
        if not (project / filename).is_file():
            errors.append(f"Arquivo obrigatório ausente: {filename}")

    for directory in PRODUCT_DIRECTORIES:
        if not (project / directory).is_dir():
            errors.append(f"Pasta obrigatória ausente: {directory}")

    for path in project.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".yml", ".yaml"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"Arquivo não está em UTF-8: {path.relative_to(project)}")
            continue
        if "{{" in content or "}}" in content:
            errors.append(f"Placeholder não resolvido: {path.relative_to(project)}")

    agents_path = project / "AGENTS.md"
    if agents_path.is_file() and "CLAUDE.md" not in agents_path.read_text(encoding="utf-8"):
        errors.append("AGENTS.md deve apontar para CLAUDE.md")

    spec_path = project / "agent-product-spec.md"
    if spec_path.is_file():
        spec = spec_path.read_text(encoding="utf-8")
        for field in ("product_id:", "product_name:", "target_domain:", "status:"):
            if field not in spec:
                errors.append(f"agent-product-spec.md sem campo: {field}")
        if 'status: "candidate"' not in spec:
            warnings.append("O produto não está marcado como candidate")

    return errors, warnings
