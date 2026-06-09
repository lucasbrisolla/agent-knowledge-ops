#!/usr/bin/env python3
"""Cria README e índice editorial para uma coleção de livros."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Cria uma pasta editorial de livro em padrão books/<tema>.")
    parser.add_argument("project", help="Pasta da coleção, como books/budgeting")
    parser.add_argument("--book-title", required=True, help="Título do livro")
    parser.add_argument("--target-agent", required=True, help="Agente ou produto alvo")
    parser.add_argument("--source", default="", help="Caminho ou URL da fonte")
    parser.add_argument("--slug", default="", help="Slug usado no arquivo de índice")
    parser.add_argument("--chapters", nargs="*", default=[], help="Lista opcional de capítulos")
    parser.add_argument("--force", action="store_true", help="Permite completar uma pasta existente")
    args = parser.parse_args()

    project_path = Path(args.project)
    if project_path.exists() and not args.force and any(project_path.iterdir()):
        raise SystemExit(f"Pasta já existe e não está vazia: {project_path}. Use --force para completar.")

    project_path.mkdir(parents=True, exist_ok=True)
    slug = args.slug or slugify(project_path.name)
    readme_path = project_path / "README.md"
    index_path = project_path / f"{slug}-index.md"

    write_if_missing(
        readme_path,
        render_readme(
            book_title=args.book_title,
            target_agent=args.target_agent,
            source=args.source,
            index_filename=index_path.name,
        ),
    )
    write_if_missing(
        index_path,
        render_index(
            book_title=args.book_title,
            target_agent=args.target_agent,
            chapters=args.chapters,
        ),
    )

    print(f"Coleção de livro criada: {project_path}")
    print(f"README: {readme_path}")
    print(f"Índice: {index_path}")
    return 0


def write_if_missing(path: Path, content: str) -> None:
    if path.exists():
        return
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def render_readme(book_title: str, target_agent: str, source: str, index_filename: str) -> str:
    source_line = f"`{source}`" if source else "`[caminho ou URL da fonte]`"
    return f"""# {book_title}

Piloto de destilação editorial de *{book_title}* para aprofundar o `{target_agent}`.

## Fonte

{source_line}

Leitura atual: apenas índice/sumário.

## Papel Desta Pasta

Esta pasta não é destino final de conhecimento.

Ela existe para transformar o livro em insumo útil para a base viva do produto, de forma seletiva e incremental.

## Estratégia

1. **Índice** (`{index_filename}`) — mapa de destilação editorial do livro.
2. **Sessões por capítulo** — abrir apenas o capítulo priorizado e o artefato de destino mais provável.
3. **Promoção seletiva** — levar conteúdo apenas para a camada operacional do produto quando houver valor claro.

## Fluxo Editorial

O fluxo desejado é:

- lacuna real no `{target_agent}`
- capítulo priorizado
- destino definido antes da escrita
- leitura seletiva
- promoção para a base viva
- atualização do índice com status editorial

## Destinos Possíveis

Antes de destilar um capítulo, decidir o destino mais provável:

- `_method-wiki/concepts/`
- `_method-wiki/heuristics/`
- `_method-wiki/checklists/`
- `_method-wiki/patterns/`
- `_method-wiki/processes/`
- `tracks/*/workflows/`
- `tracks/*/playbooks/`
- `tracks/*/modes/`
- `skills/`
- `templates/`
- descarte por enquanto

## Filtro De Promoção

O teste para promover conteúdo deste livro é:

> "Uma pessoa no domínio alvo usaria isso para decidir, revisar, diagnosticar ou executar sem reescrever do zero?"

Se a resposta for não:

- descartar por enquanto
- ou manter apenas como referência de baixa prioridade

## Regra De Uso Do Índice

O índice não serve apenas para dizer o que cada capítulo parece conter.

Ele funciona como painel de status para responder:

- o que deste livro serve ao produto
- onde isso deve entrar
- o que já está coberto
- o que ainda precisa ser destilado
- o que deve ser descartado por baixa aderência

## Status

- [x] Estrutura da pasta criada.
- [x] Índice inicial baseado no sumário criado.
- [ ] Leitura de capítulos priorizados.
- [ ] Promoção dos primeiros capítulos úteis para a camada operacional.

## Observação

Registre aqui a tendência principal do livro: se ele tende a alimentar concepts, heuristics, checklists, workflows, playbooks, modes, skills ou templates.
"""


def render_index(book_title: str, target_agent: str, chapters: list[str]) -> str:
    rows = render_chapter_rows(chapters)
    return f"""# {book_title} Index

Mapa de destilação editorial de *{book_title}* para o `{target_agent}`.

Critério desta nota:

- leitura atual limitada ao sumário
- sem destilação de capítulos ainda
- classificação editorial preliminar por capítulo
- foco em apontar destino provável, status e aderência ao produto

## Legenda De Status

- `já coberto`: o capítulo parece bem representado por artefatos já existentes
- `parcialmente coberto`: já existe cobertura parcial, mas ainda pode haver ganho de destilação
- `spec definida`: leitura e desenho editorial já foram feitos; pendente executar a spec na base viva
- `destilar`: lacuna real ou provável; candidato de trabalho futuro
- `descartar por enquanto`: baixa aderência ao foco atual do produto

## Mapa Por Capítulo

| Capítulo | Tema principal | MD relacionado ou destino mais provável | Status | Observação |
|---|---|---|---|---|
{rows}

## Prioridade Futura De Destilação

### Prioridade Alta

- 

### Prioridade Média

- 

### Prioridade Baixa Por Enquanto

- 

## Leituras Que Este Índice Sugere Ao Produto

- 

## Regra Para Sessões Futuras

Ao abrir um capítulo:

1. confirmar se a lacuna no agente continua real
2. apontar o MD relacionado ou o destino mais provável antes de escrever
3. ler apenas o capítulo priorizado
4. decidir entre promover, aprofundar cobertura parcial ou descartar por enquanto
5. atualizar o status editorial no índice para evitar releitura e retrabalho
"""


def render_chapter_rows(chapters: list[str]) -> str:
    if not chapters:
        return "| 1 |  |  | `destilar` |  |"
    return "\n".join(
        f"| {index} | {escape_table(chapter)} |  | `destilar` |  |"
        for index, chapter in enumerate(chapters, start=1)
    )


def slugify(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower())
    return value.strip("-") or "book"


def escape_table(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


if __name__ == "__main__":
    raise SystemExit(main())
