---
name: source-project-setup
description: Use quando precisar criar a estrutura padrão de um projeto de fonte para organizar raw, biblioteca, destilações, promoções, method-wiki, operações e agente-produto.
---

# Source Project Setup

Use esta skill para iniciar um projeto de fonte antes de capturar, indexar ou destilar conteúdo.

## Quando Usar

- Uma fonte é grande demais para uma nota única.
- Há várias unidades de leitura ou análise.
- O usuário quer reaproveitar conhecimento em agentes.
- A fonte pode gerar método, skill ou agente-produto no futuro.

## Fluxo

1. Definir nome do projeto e tipo de fonte.
2. Criar estrutura padrão.
3. Preencher `source-manifest.md`.
4. Registrar critérios de priorização.
5. Criar `promotion-matrix.md`.
6. Deixar `agent-product/` vazio até existir evidência operacional.

## Estrutura

```text
project/
  README.md
  source-manifest.md
  promotion-matrix.md
  raw/
  library/
  distillations/
  promotions/
  method-wiki/
  operations/
  agent-product/
```

## Templates Disponíveis

Use `--template` para aplicar defaults editoriais:

- `youtube`: canal ou playlist de YouTube, unidade principal `vídeo`.
- `book`: livro, unidade principal `capítulo`.
- `earnings-calls`: resultados de empresas abertas, unidade principal `empresa + trimestre`.

Exemplo:

```bash
python3 tools/create-source-project.py ../canal-carreira --template youtube
```

## Guardrails

- Não começar pela skill; comece pela fonte e pelo manifest.
- Não misturar bruto, biblioteca e conhecimento promovido.
- Não promover item sem evidência.
- Não criar agente-produto por entusiasmo inicial.
- Manter o agente-produto no radar, mas como etapa posterior.

## Saída Esperada

- Projeto de fonte pronto para intake.
- Manifest preenchido ao menos parcialmente.
- Matriz de promoção criada.
- Próximo lote definido.
