# Roadmap

Ideias e próximos módulos para o `agent-knowledge-ops`.

## Princípio

O roadmap guarda possibilidades sem confundir o núcleo do framework.

Uma ideia só deve virar framework, skill ou ferramenta quando tiver:

- fonte recorrente
- saída clara
- valor para um agente
- contrato reaproveitável

## Módulos Em Aberto

| Módulo | Status | Ideia |
|---|---|---|
| `youtube-channel-intake` | iniciado | Criar bibliotecas locais de canais e playlists |
| `book-distillation` | iniciado | Destilar livros por capítulo para conhecimento de agente |
| `social-signal-research` | planejado | Transformar Reddit, HN, X, YouTube e comunidades em sinais |
| `web-article-intake` | planejado | Capturar sites e artigos como unidades rastreáveis |
| `earnings-call-intelligence` | ideia registrada | Analisar transcrições de resultados de companhias abertas |
| `agent-product-scaffold` | planejado | Gerar repositório padrão de um agente-produto |

## Earnings Call Intelligence

Ideia registrada para explorar depois.

Objetivo:

Transformar transcrições de resultados, conference calls, releases e apresentações de companhias abertas em inteligência operacional para agentes.

Possíveis perguntas:

- Quais tendências aparecem em várias empresas do mesmo setor?
- O que empresas líderes estão fazendo sobre margem, eficiência, IA, capex, pricing ou caixa?
- Quais riscos estão ficando recorrentes?
- Como a linguagem da gestão mudou ao longo dos trimestres?
- Quais práticas parecem estar se espalhando entre pares?
- Que sinais antecipam mudança de estratégia, ciclo ou pressão competitiva?

Possíveis saídas:

- índice por empresa, trimestre e setor
- destilação por call
- matriz de tendências
- comparação entre pares
- warnings setoriais
- método de análise de resultado
- skill de leitura de earnings call

## Próxima Prioridade Arquitetural

Definir o scaffold padrão de um projeto criado pelo kit:

```text
project/
  README.md
  source-manifest.md
  raw/
  library/
  distillations/
  promotions/
  method-wiki/
  operations/
  agent-product/
```
