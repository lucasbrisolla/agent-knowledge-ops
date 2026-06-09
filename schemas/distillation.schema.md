# Distillation Schema

Contrato minimo para uma nota de destilação.

## Campos

| Campo | Obrigatorio | Descricao |
|---|---|---|
| `source_id` | sim | Fonte original |
| `unit_id` | sim | Capítulo, vídeo, thread, artigo ou seção |
| `target_agent` | sim | Produto/agente alvo |
| `probable_destination` | sim | Destino provável antes da escrita |
| `thesis` | sim | Tese central da unidade |
| `reusable_ideas` | sim | Ideias que podem sobreviver fora da fonte |
| `do_not_promote` | sim | Conteudo interessante, mas sem destino |
| `gaps_or_contradictions` | não | Lacunas ou tensoes |
| `recommended_decision` | sim | Promover, arquivar, descartar ou aguardar uso |

## Tipos De Ideia

- `concept`
- `principle`
- `heuristic`
- `pattern`
- `warning`
- `question`
- `checklist-candidate`
- `workflow-candidate`
- `skill-candidate`

## Regra

Destilação boa deve ser rastreável até a fonte, mas utilizável sem reler a fonte inteira.
