# Promotion Schema

Contrato minimo para decidir o destino de uma destilação.

## Campos

| Campo | Obrigatorio | Descricao |
|---|---|---|
| `candidate_id` | sim | Ideia ou bloco candidato |
| `origin` | sim | Nota de destilação de origem |
| `decision` | sim | Resultado da avaliação |
| `destination_layer` | sim | `knowledge-base`, `method-wiki`, `operations`, `agent-product`, `archive`, `discard` |
| `target_path` | não | Arquivo ou pasta alvo |
| `confidence` | sim | `low`, `medium`, `high` |
| `reason` | sim | Por que promover ou descartar |
| `next_test` | não | Como validar no uso real |

## Decisoes Validas

- `promote`
- `merge-into-existing`
- `create-new`
- `archive`
- `discard-for-now`
- `wait-for-real-use`

## Regra

Toda promoção para `operations` deve dizer se e `skill`, `workflow`, `playbook` ou `template`.
