#!/usr/bin/env python3
"""Valida o contrato executável de um projeto de fonte."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from source_project import validate_project  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Valida a estrutura e os contratos de um projeto de fonte."
    )
    parser.add_argument("project", help="Pasta do projeto de fonte")
    args = parser.parse_args(argv)

    report = validate_project(Path(args.project))
    for warning in report.warnings:
        print(f"AVISO: {warning}")
    if report.errors:
        for error in report.errors:
            print(f"ERRO: {error}", file=sys.stderr)
        return 1

    print(f"Projeto de fonte válido: {args.project}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
