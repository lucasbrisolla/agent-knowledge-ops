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
| `repeated_output` | não | Artefato ou saída que tende a se repetir |
| `state_needed` | sim | `yes`, `no` ou `unknown` |
| `verification_needed` | sim | `none`, `doctor`, `verify`, `sync-check`, `liveness` ou `multiple` |
| `recommended_form` | sim | `structured-operator`, `domain-operating-system` ou outra forma aprovada |
| `status` | sim | `candidate`, `pilot`, `active`, `paused` ou `archived` |

## Estrutura Mínima Gerada

```text
agent-product/
  AGENTS.md
  CLAUDE.md
  README.md
  DATA_CONTRACT.md
  PRODUCT_INDEX.md
  HEALTH_CHECK.md
  agent-product-spec.md
  domain.md
  states.yml
  _method-wiki/
  workflows/
  skills/
  templates/
  context/
  examples/
  evals/
  scripts/
  archive/
```

## Regras

- O scaffold cria estrutura e contratos; não inventa conhecimento de domínio.
- Conteúdo específico de empresa, pessoa ou caso começa em `context/`.
- Método reutilizável pertence a `_method-wiki/`.
- Rotinas recorrentes pertencem a `workflows/` ou `skills/`.
- O status inicial é `candidate` até existir uso real e avaliação.
- `agent-product-spec.md` é a fonte da decisão de criação; o scaffold não substitui a revisão humana.
