#!/usr/bin/env python3
"""Valida a estrutura mínima de um agente-produto."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from agent_product import validate_product


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida um agente-produto criado com agent-knowledge-ops.")
    parser.add_argument("project", help="Pasta do agente-produto a validar")
    args = parser.parse_args()

    errors, warnings = validate_product(Path(args.project))
    for warning in warnings:
        print(f"AVISO: {warning}")
    if errors:
        for error in errors:
            print(f"ERRO: {error}", file=sys.stderr)
        return 1

    print(f"Produto válido: {args.project}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
