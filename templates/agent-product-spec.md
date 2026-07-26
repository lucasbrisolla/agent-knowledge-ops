---
product_id: "{{PRODUCT_SLUG}}"
product_name: "{{PRODUCT_NAME}}"
target_domain: "{{DOMAIN}}"
target_user: "{{TARGET_USER}}"
source_basis: "{{SOURCE_BASIS}}"
state_needed: "{{STATE_NEEDED}}"
verification_needed: "{{VERIFICATION_NEEDED}}"
recommended_form: "{{RECOMMENDED_FORM}}"
status: "{{STATUS}}"
---

# Especificação De Agente-Produto — {{PRODUCT_NAME}}

## Papel

{{DESCRIPTION}}

## Uso Recorrente

{{RECURRING_USE}}

## Output Repetido

{{REPEATED_OUTPUT}}

## Decisões Ainda Necessárias

- Qual é a fronteira exata do domínio?
- Quais fontes vivas o agente pode ler ou atualizar?
- Quais outputs são canônicos?
- O que exige `doctor`, `verify`, `sync-check` ou `liveness`?
- Qual uso real transforma este candidato em produto ativo?

## Regra De Maturidade

Este produto permanece `candidate` até haver método promovido, uso recorrente observado e avaliação mínima dos outputs.
