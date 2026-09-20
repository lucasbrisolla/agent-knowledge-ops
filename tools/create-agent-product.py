#!/usr/bin/env python3
"""Cria a estrutura mínima de um agente-produto."""

from __future__ import annotations

import argparse
from pathlib import Path

from agent_product import (
    DEFAULT_TARGET_USER,
    PRODUCT_STATUSES,
    RECOMMENDED_FORMS,
    STATE_VALUES,
    VERIFICATION_VALUES,
    ProductSpec,
    create_product,
    slugify,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Cria um scaffold de agente-produto para agent-knowledge-ops.")
    parser.add_argument("project", help="Pasta do agente-produto a criar")
    parser.add_argument("--product-name", default="", help="Nome humano do agente-produto")
    parser.add_argument("--description", required=True, help="Papel e fronteira do produto")
    parser.add_argument("--domain", required=True, help="Domínio principal atendido")
    parser.add_argument("--target-user", default=DEFAULT_TARGET_USER, help="Usuário ou perfil principal")
    parser.add_argument(
        "--recurring-use",
        default="Uso recorrente ainda não definido na especificação inicial",
        help="Uso recorrente que justifica o produto",
    )
    parser.add_argument(
        "--repeated-output",
        default="Output repetido ainda não definido na especificação inicial",
        help="Output que tende a se repetir",
    )
    parser.add_argument(
        "--source-basis",
        default="especificação inicial do produto",
        help="Fonte, método ou especificação que originou o produto",
    )
    parser.add_argument("--state-needed", choices=STATE_VALUES, default="unknown")
    parser.add_argument(
        "--verification-needed",
        choices=VERIFICATION_VALUES,
        default="multiple",
    )
    parser.add_argument(
        "--recommended-form",
        choices=RECOMMENDED_FORMS,
        default="structured-operator",
    )
    parser.add_argument("--status", choices=PRODUCT_STATUSES, default="candidate")
    parser.add_argument("--force", action="store_true", help="Completa pasta existente sem sobrescrever arquivos")
    args = parser.parse_args()

    project = Path(args.project)
    name = args.product_name or project.name.replace("-", " ").title()
    spec = ProductSpec(
        slug=slugify(project.name),
        name=name,
        description=args.description,
        domain=args.domain,
        target_user=args.target_user,
        recurring_use=args.recurring_use,
        repeated_output=args.repeated_output,
        source_basis=args.source_basis,
        state_needed=args.state_needed,
        verification_needed=args.verification_needed,
        recommended_form=args.recommended_form,
        status=args.status,
    )
    create_product(project, spec, force=args.force)
    print(f"Agente-produto criado: {project}")
    print("Próximo passo: revisar agent-product-spec.md, preencher o método e executar validate-agent-product.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
