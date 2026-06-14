# Evidence Bundle — checklist de rollback para mudanças operacionais

## Pergunta Editorial

O agente deve promover um checklist de rollback para mudanças operacionais?

## Conclusão Candidata

- Claim: mudanças operacionais recorrentes devem ter rollback definido antes da execução.
- Agente/produto alvo: `operations-agent`
- Destino recomendado: `promotion`
- Arquivo alvo provável: `method-wiki/checklists/rollback-before-change.md`
- Confiança: `medium`

## Fontes

| ID | Tipo | Caminho/URL | Data | Autoridade | Frescor | Relação com o claim | Nota |
|---|---|---|---|---|---|---|---|
| S-001 | doc | `raw/meeting-notes/change-review-2026-06-01.md` | 2026-06-01 | high | fresh | yes | decisão registrada em reunião |
| S-002 | doc | `raw/runbooks/legacy-change-process.md` | 2025-10-15 | medium | acceptable | partial | processo antigo fala de aprovação, mas não exige rollback |
| S-003 | chat | `raw/chat/ops-incidents-june.md` | 2026-06-04 | medium | fresh | yes | incidentes recentes citam falta de plano de reversão |

## Achados Deduplicados

| ID | Achado | Fontes | Observação |
|---|---|---|---|
| F-001 | O time já decidiu exigir rollback antes de mudanças relevantes. | S-001 | Fonte mais autoritativa. |
| F-002 | O processo antigo tinha lacuna explícita sobre reversão. | S-002 | Ajuda a explicar por que o método precisa mudar. |
| F-003 | A falta de rollback apareceu em incidentes recentes. | S-003 | Sinal operacional recorrente. |

## Conflitos E Lacunas

- O runbook antigo não contradiz o claim, mas está incompleto.
- Falta ainda medir se o checklist reduz incidentes depois da promoção.

## Avaliação De Confiança

- Autoridade: reunião formal e runbook dão base suficiente.
- Frescor: duas fontes são recentes.
- Consistência: fontes apontam na mesma direção.
- Rastreabilidade: todos os caminhos locais estão registrados.
- Ação que melhora: reduz risco de mudança sem reversão clara.

## Decisão Recomendada

- Resultado: promover para `method-wiki`.
- Motivo: o achado muda execução recorrente e reduz erro operacional.
- Próximo teste: usar o checklist em duas mudanças reais e registrar fricções.

## Não Promover

- Não criar skill ainda; o método precisa ser testado como checklist primeiro.

