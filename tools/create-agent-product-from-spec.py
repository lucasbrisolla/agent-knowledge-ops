#!/usr/bin/env python3
"""Cria um Agent Product a partir de uma especificação Markdown validada."""

from __future__ import annotations

import argparse
from pathlib import Path

from agent_product import create_from_spec


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cria a arquitetura inicial de um Agent Product a partir de uma especificação."
    )
    parser.add_argument("specification", help="Arquivo Markdown com frontmatter de agent-product")
    parser.add_argument("project", help="Pasta do Agent Product a criar")
    parser.add_argument("--force", action="store_true", help="Completa a pasta sem sobrescrever arquivos")
    args = parser.parse_args()

    create_from_spec(Path(args.specification), Path(args.project), force=args.force)
    print(f"Agente-produto criado a partir da especificação: {args.project}")
    print("Próximo passo: revisar domain.md, preencher o primeiro caso real e executar validate-agent-product.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
