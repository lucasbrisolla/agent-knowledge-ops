# Evidence Bundle Schema

Contrato mínimo para agrupar evidências antes de uma síntese ou decisão de promoção.

Um evidence bundle é o artefato intermediário entre destilação e promoção quando uma conclusão depende de mais de uma fonte ou precisa explicitar confiança.

## Campos

| Campo | Obrigatório | Descrição |
|---|---|---|
| `bundle_id` | sim | Identificador estável do pacote de evidências |
| `question` | sim | Pergunta editorial que orienta a busca |
| `target_agent` | não | Agente, produto ou método que pode usar a conclusão |
| `claim` | sim | Conclusão candidata em linguagem curta |
| `sources` | sim | Lista de fontes usadas |
| `deduplicated_findings` | sim | Achados consolidados sem repetição |
| `conflicts` | sim | Divergências, versões antigas ou sinais incompatíveis |
| `freshness` | sim | Avaliação de atualidade das fontes |
| `authority` | sim | Avaliação de autoridade das fontes |
| `confidence` | sim | `low`, `medium`, `high` ou `conflicting` |
| `recommended_destination` | sim | `promotion`, `archive`, `wait-for-more-evidence` ou `discard` |
| `target_path` | não | Arquivo provável se houver promoção |
| `next_test` | não | Como validar no uso real |

## Fonte

Cada item em `sources` deve registrar:

| Campo | Obrigatório | Descrição |
|---|---|---|
| `source_id` | sim | Identificador curto da fonte |
| `source_type` | sim | `book`, `video`, `pdf`, `web`, `chat`, `email`, `ticket`, `call`, `doc`, `code`, `other` |
| `path_or_url` | sim | Caminho local, URL ou referência rastreável |
| `date` | não | Data de publicação, captura ou atualização |
| `authority` | sim | `low`, `medium`, `high` |
| `freshness` | sim | `stale`, `acceptable`, `fresh`, `unknown` |
| `supports_claim` | sim | `yes`, `partial`, `no`, `conflicts` |
| `note` | não | Observação curta sobre a fonte |

## Regras

- Todo `claim` deve apontar para pelo menos uma fonte.
- Se houver fonte com `supports_claim: conflicts`, o `confidence` não pode ser `high` sem justificativa explícita.
- Se todas as fontes forem `stale` ou `unknown`, registre limitação em `conflicts` ou `freshness`.
- `recommended_destination: promotion` exige `target_path` ou justificativa de destino ainda aberto.
- Evidence bundle não promove nada sozinho; ele alimenta `promotion-matrix.md` ou uma nota em `promotions/`.

