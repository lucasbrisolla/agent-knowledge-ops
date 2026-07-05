# Agent Product Decision Schema

Contrato mínimo para decidir qual forma operacional um conhecimento refinado deve virar.

Use este schema quando uma destilação, evidence bundle, method-wiki ou conjunto de fontes começar a pedir algo mais operacional.

## Campos

| Campo | Obrigatório | Descrição |
|---|---|---|
| `decision_id` | sim | Identificador curto e estável da decisão |
| `source_basis` | sim | Fonte, destilação, evidence bundle ou method-wiki que motivou a decisão |
| `target_domain` | sim | Domínio ou produto afetado |
| `recurring_use` | sim | Uso recorrente observado ou esperado |
| `repeated_output` | não | Artifact/output que tende a se repetir |
| `living_source` | não | Fonte viva que precisaria ser mantida |
| `state_needed` | sim | `yes`, `no` ou `unknown` |
| `verification_needed` | sim | `none`, `doctor`, `verify`, `sync-check`, `liveness`, `multiple` |
| `recommended_form` | sim | Forma operacional recomendada |
| `minimum_package` | sim | Blocos mínimos para implementar sem overengineering |
| `do_not_build_yet` | sim | Complexidades proibidas agora |
| `next_action` | sim | Próxima ação concreta |
| `review_trigger` | não | Sinal que justifica reavaliar a decisão depois |

## `recommended_form`

Valores permitidos:

- `do-not-promote`
- `knowledge-base`
- `method-wiki`
- `skill`
- `workflow`
- `light-assistant`
- `structured-operator`
- `domain-operating-system`
- `local-first-platform`
- `wait-for-real-use`

## Regras

- `local-first-platform` exige fonte canônica estável e justificativa de múltiplas superfícies.
- `domain-operating-system` exige pelo menos uma fonte viva, output recorrente e risco de drift.
- `structured-operator` exige artifact/output repetido e regra de persistência.
- `skill` exige gatilho claro de uso e saída verificável.
- `method-wiki` exige método reutilizável, não apenas resumo.
- Se `state_needed: unknown`, não criar plataforma nem sistema de domínio.
- Se não houver `recurring_use`, preferir `knowledge-base`, `method-wiki` ou `wait-for-real-use`.
