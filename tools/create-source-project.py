#!/usr/bin/env python3
"""Cria a estrutura padrão de um projeto de fonte."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


DIRECTORIES = [
    "raw",
    "library",
    "distillations",
    "promotions",
    "method-wiki",
    "operations",
    "agent-product",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Cria um projeto de fonte para agent-knowledge-ops.")
    parser.add_argument("project", help="Nome ou caminho do projeto a criar")
    parser.add_argument("--source-type", default="", help="Tipo de fonte, como youtube-channel, book ou earnings-calls")
    parser.add_argument("--source-name", default="", help="Nome da fonte")
    parser.add_argument("--source-url", default="", help="URL ou caminho da fonte")
    parser.add_argument("--target-agent", action="append", default=[], help="Agente alvo. Pode repetir.")
    parser.add_argument("--force", action="store_true", help="Permite criar dentro de pasta existente")
    args = parser.parse_args()

    project_path = Path(args.project)
    if project_path.exists() and not args.force:
        raise SystemExit(f"Projeto já existe: {project_path}. Use --force para completar a estrutura.")

    project_path.mkdir(parents=True, exist_ok=True)
    for directory in DIRECTORIES:
        (project_path / directory).mkdir(parents=True, exist_ok=True)

    source_name = args.source_name or project_path.name
    write_if_missing(project_path / "README.md", render_readme(source_name, args.source_type, args.target_agent))
    write_if_missing(
        project_path / "source-manifest.md",
        render_manifest(source_name, args.source_type, args.source_url, args.target_agent),
    )
    write_if_missing(project_path / "promotion-matrix.md", render_promotion_matrix())

    print(f"Projeto de fonte criado: {project_path}")
    print("Próximo passo: preencher source-manifest.md e capturar matéria-prima em raw/.")
    return 0


def write_if_missing(path: Path, content: str) -> None:
    if path.exists():
        return
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def render_readme(source_name: str, source_type: str, target_agents: list[str]) -> str:
    target = ", ".join(target_agents)
    return f"""# {source_name}

Projeto de fonte criado com `agent-knowledge-ops`.

## Objetivo

- Fonte: {source_name}
- Tipo de fonte: {source_type}
- Agente/produto alvo: {target}
- Pergunta central:
- Resultado esperado:

## Estrutura

- `raw/`: matéria-prima original ou exportada.
- `library/`: índice navegável e notas geradas.
- `distillations/`: destilações por unidade.
- `promotions/`: decisões editoriais detalhadas.
- `method-wiki/`: conhecimento promovido como método.
- `operations/`: skills, workflows, playbooks e templates candidatos.
- `agent-product/`: material para produto de agente, se amadurecer.

## Estado Atual

- Status: `novo`
- Unidades capturadas:
- Unidades indexadas:
- Unidades destiladas:
- Itens promovidos:

## Próximos Lotes

| Lote | Unidade/Filtro | Motivo | Status |
|---|---|---|---|
| 1 |  |  | `novo` |
"""


def render_manifest(source_name: str, source_type: str, source_url: str, target_agents: list[str]) -> str:
    agents = "\n".join(f'  - "{agent}"' for agent in target_agents)
    if not agents:
        agents = "  []"

    return f"""---
project: "{slugify(source_name)}"
source_type: "{source_type}"
source_name: "{source_name}"
source_url: "{source_url}"
owner: ""
created: "{date.today().isoformat()}"
status: "novo"
target_agents:
{agents}
probable_outputs: []
---

# Source Manifest — {source_name}

## Fonte

- Tipo: {source_type}
- Nome: {source_name}
- URL/caminho: {source_url}
- Autor/criador:
- Período coberto:
- Idioma:
- Direitos/observações:

## Objetivo Editorial

- Agente/produto alvo:
- Pergunta central:
- Decisão que esta fonte deve melhorar:
- Erro que esta fonte deve ajudar a evitar:

## Escopo

### Incluir

- 

### Excluir

- 

## Unidade De Trabalho

- Unidade principal:
- Granularidade:
- Critério para considerar uma unidade coberta:

## Cobertura

| Métrica | Valor |
|---|---:|
| Unidades estimadas |  |
| Unidades capturadas |  |
| Unidades indexadas |  |
| Unidades destiladas |  |
| Itens promovidos |  |
"""


def render_promotion_matrix() -> str:
    return """# Promotion Matrix

Matriz para decidir o destino de conhecimento extraído de uma fonte.

## Matriz

| ID | Fonte/Unidade | Achado | Tipo | Destino | Confiança | Evidência | Arquivo Alvo | Próximo Teste |
|---|---|---|---|---|---:|---|---|---|
| P-001 |  |  |  |  |  |  |  |  |

## Decisões

### Promover Agora

- 

### Aguardar Evidência

- 

### Arquivar

- 

### Descartar

- 
"""


def slugify(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower())
    return value.strip("-") or "source-project"


if __name__ == "__main__":
    raise SystemExit(main())
