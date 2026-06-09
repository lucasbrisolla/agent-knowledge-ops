# Framework De Coleção De Livros

Este framework padroniza a pasta `books/<tema>/` usada para transformar livros em insumo útil para um agente.

Ele foi inspirado no padrão editorial já usado em produtos como `accounting-ops`, onde cada livro ou grupo de livros tem:

- `README.md`
- `<tema>-index.md`
- leitura seletiva
- status por capítulo
- destino provável antes da destilação
- promoção apenas para a base viva do agente

## Objetivo

Evitar que livros virem resumos longos sem destino operacional.

A pasta de livro não é o destino final do conhecimento. Ela é uma área de trabalho editorial para decidir:

- o que o livro pode melhorar no agente
- quais capítulos merecem destilação
- quais partes já estão cobertas
- quais ideias devem ser descartadas por enquanto
- para onde cada achado deve ser promovido

## Estrutura

```text
books/
  tema-ou-livro/
    README.md
    tema-ou-livro-index.md
    raw/
    distillations/
    promotions/
```

Em produtos existentes, `raw/`, `distillations/` e `promotions/` podem ser omitidos no início se o fluxo ainda estiver só no índice editorial.

## README Editorial

O `README.md` responde:

- qual livro ou coleção está sendo usada
- qual agente/produto será alimentado
- qual é o papel da pasta
- qual é a estratégia de leitura
- quais destinos são possíveis
- qual filtro de promoção será usado
- qual é o status da pasta

## Índice Editorial

O `<tema>-index.md` funciona como painel de controle.

Ele deve conter:

- critério da nota
- legenda de status
- mapa por capítulo
- prioridade futura de destilação
- leituras que o índice sugere ao produto
- regra para sessões futuras

## Status Por Capítulo

Use status explícitos para evitar releitura:

- `já coberto`
- `parcialmente coberto`
- `spec definida`
- `destilar`
- `descartar por enquanto`

## Regra De Promoção

Antes de abrir um capítulo, defina o destino mais provável.

Exemplos:

- `_method-wiki/concepts/`
- `_method-wiki/heuristics/`
- `_method-wiki/checklists/`
- `_method-wiki/patterns/`
- `_method-wiki/processes/`
- `tracks/*/workflows/`
- `tracks/*/playbooks/`
- `tracks/*/modes/`
- `skills/`
- `templates/`
- `discard`

## Guardrails

- Não destilar livro inteiro por completismo.
- Não promover capítulo sem lacuna real no agente.
- Não criar arquivos novos se enriquecer um arquivo existente for melhor.
- Não confundir sumário comentado com destilação.
- Não transformar o livro em destino final.

## Fluxo

1. Criar pasta do livro ou tema.
2. Criar `README.md` editorial.
3. Criar `<tema>-index.md` a partir do sumário.
4. Marcar status preliminar por capítulo.
5. Priorizar capítulos com lacuna real.
6. Destilar apenas capítulos selecionados.
7. Promover para method-wiki, workflow, playbook, skill ou template.
8. Atualizar o índice para registrar status e evitar retrabalho.
