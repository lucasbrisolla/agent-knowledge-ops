# Knowledge Synthesis Framework

Framework para transformar achados de múltiplas fontes em uma resposta ou decisão confiável antes da promoção.

Ele existe para evitar que o agente promova uma ideia só porque ela apareceu em uma fonte isolada, antiga, fraca ou contraditória.

## Pergunta Central

O que estas fontes, quando lidas em conjunto, permitem afirmar com segurança suficiente para melhorar julgamento ou execução?

## Quando Usar

Use síntese de conhecimento quando houver:

- mais de uma fonte sobre o mesmo tema
- fontes com autoridade diferente
- risco de informação desatualizada
- conflito entre evidências
- decisão de promoção para `method-wiki`, `operations` ou `agent-product`
- necessidade de explicar confiança e limites da conclusão

## Fluxo

1. Definir a pergunta editorial.
2. Listar as fontes usadas.
3. Separar achados por tema.
4. Deduplicar achados repetidos.
5. Identificar conflitos e evolução temporal.
6. Avaliar autoridade e frescor das fontes.
7. Produzir síntese curta com confiança.
8. Decidir se o achado entra em promoção, arquivo ou espera.

## Deduplicação

Junte achados quando eles tiverem:

- mesma conclusão central
- mesma entidade, processo ou problema
- evidência semelhante em fontes diferentes
- uma fonte confirmando outra
- diferença apenas de redação ou granularidade

Não junte achados quando houver:

- conclusões diferentes
- períodos diferentes com mudança material
- fontes falando de casos distintos
- divergência que afeta a decisão do agente

## Critérios De Confiança

| Critério | Sinal De Confiança Alta | Sinal De Confiança Baixa |
|---|---|---|
| Autoridade | documento oficial, fonte primária, artefato mantido | comentário solto, rascunho, fonte sem dono |
| Frescor | atualizado recentemente para o tema em questão | antigo e possivelmente superado |
| Consistência | múltiplas fontes concordam | fontes entram em conflito |
| Rastreabilidade | caminho, autor, data e trecho localizáveis | evidência difícil de reencontrar |
| Ação | muda decisão, diagnóstico ou execução | apenas informa contexto |

## Níveis De Confiança

- `high`: fontes recentes e autoritativas concordam.
- `medium`: há boa evidência, mas falta confirmação, frescor ou cobertura.
- `low`: achado plausível, mas depende de fonte fraca, antiga ou única.
- `conflicting`: há evidência relevante em direções incompatíveis.

## Saída Esperada

Toda síntese deve produzir:

- pergunta editorial
- conclusão curta
- fontes usadas
- achados deduplicados
- conflitos ou lacunas
- nível de confiança
- destino recomendado
- próximo teste

## Relação Com Promoção

Síntese não substitui promoção.

Ela alimenta a decisão de promoção com mais rigor. Um achado sintetizado ainda precisa passar pelo `promotion-framework` antes de virar conhecimento canônico, método ou operação.

## Anti-Patterns

- tratar volume de fontes como prova
- esconder conflitos para simplificar a narrativa
- promover conclusão antiga sem checar frescor
- citar fonte sem caminho rastreável
- transformar síntese em resumo longo
- ignorar que fontes diferentes têm autoridade diferente

