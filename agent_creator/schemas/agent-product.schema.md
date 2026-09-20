# Schema De Agente-Produto

Contrato mínimo para uma casa operacional de agente criada a partir de uma especificação validada.

## Campos Da Especificação

| Campo | Obrigatório | Descrição |
|---|---|---|
| `product_id` | sim | Identificador estável e curto do produto |
| `product_name` | sim | Nome humano do agente-produto |
| `description` | sim | Papel e fronteira do produto |
| `target_domain` | sim | Domínio principal atendido |
| `target_user` | não | Usuário ou perfil principal |
| `source_basis` | sim | Especificação, método ou fonte que originou o produto |
| `recurring_use` | sim | Uso recorrente que justifica a casa própria |
| `repeated_output` | sim | Artefato ou saída que tende a se repetir |
| `state_needed` | sim | `yes`, `no` ou `unknown` |
| `verification_needed` | sim | `none`, `doctor`, `verify`, `sync-check`, `liveness` ou `multiple` |
| `recommended_form` | sim | Forma operacional recomendada: `do-not-promote`, `knowledge-base`, `method-wiki`, `skill`, `workflow`, `light-assistant`, `structured-operator`, `domain-operating-system`, `local-first-platform` ou `wait-for-real-use` |
| `status` | sim | `candidate`, `pilot`, `active`, `paused` ou `archived` |

## Regras

- O scaffold cria estrutura e contratos; não inventa conhecimento de domínio.
- Conteúdo específico de empresa, pessoa ou caso começa em `context/`.
- Método reutilizável pertence a `_method-wiki/`.
- Rotinas recorrentes pertencem a `workflows/` ou `skills/`.
- O status inicial seguro é `candidate`.
- A especificação deve registrar uso recorrente e output antes de justificar um operador estruturado.
