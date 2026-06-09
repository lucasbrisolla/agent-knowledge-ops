# Promotion Framework

Decide o que acontece depois da destilação.

## Pergunta Central

Isso deve virar conhecimento, método, operação ou descarte?

## Destinos

| Destino | Quando usar |
|---|---|
| `knowledge-base` | quando a ideia é estável e reutilizável |
| `method-wiki` | quando muda como pensar, diagnosticar ou decidir |
| `operations` | quando gera ação recorrente |
| `agent-product` | quando há domínio, workflow e persistência suficientes |
| `archive` | quando é interessante, mas ainda sem uso |
| `discard` | quando não melhora julgamento ou execução |

## Regras

Promover para `knowledge-base` quando a ideia puder ser usada sem abrir a fonte original.

Promover para `method-wiki` quando a ideia virar critério, heurística, checklist, pattern ou processo.

Promover para `operations` quando houver sequência recorrente ou transformação atômica.

Promover para `agent-product` apenas quando o conjunto já tiver uso recorrente, fronteira de domínio e necessidade de superfície própria.

## Anti-Patterns

- transformar fonte em resumo permanente
- criar skill antes de validar uso recorrente
- duplicar conhecimento que já existe
- promover insight lateral por entusiasmo
- confundir exemplo com regra

## Decisão Mínima

Toda promoção deve registrar:

- destino
- motivo
- arquivo alvo
- confiança
- próximo teste de uso
