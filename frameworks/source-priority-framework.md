# Source Priority Framework

Framework para escolher quais fontes consultar primeiro conforme a pergunta editorial.

Ele ajuda o agente a procurar evidência com intenção, em vez de tratar todas as fontes como equivalentes.

## Pergunta Central

Que tipo de fonte tem maior chance de responder esta pergunta com autoridade, frescor e rastreabilidade?

## Princípio

Prioridade não é exclusão.

Uma fonte prioritária deve ser consultada primeiro ou receber mais peso, mas fontes secundárias ainda podem confirmar, contextualizar ou contradizer a conclusão.

## Tipos De Pergunta

| Tipo De Pergunta | Fontes Prioritárias | Fontes De Apoio |
|---|---|---|
| Decisão tomada | decisão registrada, reunião, email, issue, PR | chat, notas pessoais, roadmap |
| Estado atual | tracker, dashboard, documento mantido | chat recente, email, changelog |
| Política ou regra | norma oficial, contrato, policy, manual | anúncio, FAQ, conversa |
| Método ou processo | runbook, SOP, checklist validado | exemplos, comentários, retro |
| Dor ou sinal de mercado | Reddit, HN, reviews, tickets, calls | artigos, posts, entrevistas |
| Conteúdo técnico | documentação oficial, código, testes | blog, tutorial, chat |
| Livro ou fonte longa | sumário, capítulo, notas de leitura | resenhas, entrevistas, palestras |
| PDF regulatório | PDF original, índice, seção normativa | resumo interno, apresentação |
| Earnings call | transcrição, release, apresentação | notícia, relatório, call anterior |

## Prioridade Por Camada Da Refinaria

### Intake

Priorize fontes primárias e preserváveis:

- PDF original
- HTML original
- transcrição exportada
- arquivo bruto
- metadados de origem

### Biblioteca

Priorize fontes que ajudam navegação:

- índice
- sumário
- capítulos
- timestamps
- seções
- tags
- metadados

### Destilação

Priorize a unidade selecionada:

- capítulo específico
- vídeo específico
- seção do PDF
- thread específica
- call de empresa + trimestre

### Promoção

Priorize evidência que prova reutilização:

- padrões recorrentes
- confirmação em mais de uma unidade
- lacuna real em `method-wiki`
- uso operacional provável
- risco de erro que o achado reduz

## Heurísticas

- Para fatos atuais, frescor pesa mais.
- Para regras oficiais, autoridade pesa mais.
- Para comportamento de usuários, linguagem real pesa mais.
- Para método, recorrência pesa mais.
- Para operação, repetibilidade pesa mais.
- Para agente-produto, caso de uso recorrente pesa mais que entusiasmo.

## Registro Mínimo

Ao priorizar fontes, registre:

- pergunta editorial
- fontes consultadas
- fontes ignoradas ou adiadas
- motivo da prioridade
- lacunas remanescentes
- impacto na confiança

## Anti-Patterns

- começar pela fonte mais fácil, não pela mais confiável
- tratar chat como política oficial
- tratar resumo como fonte primária
- usar material antigo para responder estado atual
- buscar tudo antes de definir pergunta
- ignorar fonte contraditória porque complica a promoção

