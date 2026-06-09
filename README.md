# Agent Knowledge Ops

Kit operacional para transformar fontes brutas em conhecimento refinado, método reutilizável e capacidades operacionais para agentes.

Este diretório é o scaffold local do vault para o repositório `lucasbrisolla/agent-knowledge-ops`.

## Tese

Agentes melhores não precisam apenas de mais contexto. Eles precisam de conhecimento promovido com critério.

O fluxo central é:

```text
source intake
-> distillation
-> knowledge
-> method
-> operation
-> agent product
```

## Camadas

| Camada | Pergunta | Saída |
|---|---|---|
| `source intake` | Como a matéria-prima entra? | canal, playlist, livro, artigo, post, site |
| `distillation` | O que a fonte disse de útil? | nota rastreável por unidade |
| `knowledge` | O que o agente agora sabe? | conceito, princípio, warning, pergunta |
| `method` | Como o agente deve pensar? | heurística, checklist, pattern, processo |
| `operation` | O que o agente consegue fazer? | skill, workflow, playbook, template |
| `agent product` | Isso já merece produto próprio? | arquitetura mínima validada |

## Estrutura

- `FRAMEWORK.md`: visão geral do ciclo completo.
- `ARCHITECTURE.md`: separação entre captação, biblioteca, destilação, promoção, método, operação e produto.
- `ROADMAP.md`: ideias futuras sem misturar com o núcleo estável.
- `frameworks/`: frameworks irmãos de destilação, promoção e arquitetura mínima.
- `tools/`: scripts reutilizáveis para materializar bibliotecas e artefatos.
- `templates/`: formatos reutilizáveis para livros, fontes e decisões de promoção.
- `skills/`: futuros procedimentos executáveis.
- `examples/`: exemplos bons e ruins de destilação.
- `schemas/`: contratos textuais para notas e artefatos.

## Primeiro Caso Canônico

O caso `a-life-after-layoff` é o padrão inicial para intake de canal:

```text
YouTube channel
-> yt-dlp raw metadata/transcripts
-> Markdown video library
-> category index
-> selected video distillation
-> promoted method-wiki/skills
```

O script `tools/build-youtube-library.py` existe para recriar esse tipo de biblioteca em novos canais.

## Ideias Futuras Registradas

- `social-signal-research`: Reddit, HN, X, YouTube e comunidades como sinais de dor e tendência.
- `earnings-call-intelligence`: transcrições de resultados de companhias abertas para detectar tendências, práticas de gestão e movimentos setoriais.
- `agent-product-scaffold`: geração de repositório padrão para agentes-produto.

## Regra De Ouro

Fonte bruta não entra direto no agente.

Ela passa por uma destilação rastreável, depois por uma decisão de promoção, e só então vira conhecimento canônico, método ou operação.
