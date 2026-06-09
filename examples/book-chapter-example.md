# Example — Book Chapter Distillation

Exemplo curto de como uma unidade de livro passaria pelo kit.

## Source

- Tipo: `book`
- Livro: `Toyota Kata`
- Unidade: capítulo sobre improvement kata
- Agente alvo: `agent-products`
- Lente: como transformar incerteza em rotina de melhoria para agentes

## Distillation

Tese da unidade:

O progresso em ambiente incerto melhora quando a pessoa separa condição atual, condição-alvo, obstáculo e próximo experimento.

Ideias reutilizáveis:

| Tipo | Ideia | Aplicação |
|---|---|---|
| `principle` | Melhorar é uma rotina treinável, não um insight ocasional. | Agentes devem guiar melhoria por loop recorrente. |
| `heuristic` | Não atacar todos os problemas; escolher o obstáculo atual. | Reduzir outputs grandes e difusos. |
| `question` | Qual é o próximo experimento pequeno que gera aprendizado? | Usar antes de criar workflow novo. |
| `workflow-candidate` | Current state -> target condition -> obstacle -> experiment -> learning. | Pode virar workflow de melhoria de agente. |

## Promotion Decision

- Resultado: `promote`
- Destino: `method-wiki`
- Arquivo alvo: `heuristics/improvement-kata.md`
- Confiança: `medium`
- Próximo teste: aplicar em uma revisao real de `accounting-ops` ou `agro-ops`

## Do Not Promote

- Historias especificas da Toyota sem adaptacao.
- Jargoes de manufatura que não melhoram agente.
