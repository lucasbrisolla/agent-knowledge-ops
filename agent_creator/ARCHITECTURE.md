# Arquitetura Do `agent_creator`

## Seam

A seam do módulo é a especificação de Agent Product:

```text
ProductSpec Markdown
        ↓
agent_creator.core
        ↓
scaffold candidate + validação
```

O caller precisa conhecer apenas o contrato de frontmatter, o caminho de destino e o resultado da validação.

## Responsabilidades

| Parte | Responsabilidade |
|---|---|
| `core.py` | Parsear especificação, renderizar templates, criar estrutura e validar contrato |
| `templates/` | Arquivos genéricos de entrada, dados, routing, estado e diagnóstico |
| `schemas/` | Contrato dos campos aceitos pela especificação |
| `tools/create-agent-product-from-spec.py` | Adapter CLI para a interface `create` |
| `tools/create-agent-product.py` | Adapter legado para criação por argumentos |
| `tools/validate-agent-product.py` | Adapter CLI para a interface `validate` |

## Fluxo De Dados

```text
escopo do usuário
  ↓
agent-knowledge-ops: decisão e especificação
  ↓
agent_creator: scaffold
  ↓
produto `candidate`
  ↓
caso real, método e avaliação
```

## Profundidade E Limites

O módulo concentra filesystem, templating e validação atrás de uma interface pequena. Ele não conhece as fontes, o método ou o contexto do domínio. Essa separação permite trocar templates e regras de validação sem alterar o fluxo editorial da refinaria.

Padrões arquiteturais futuros devem entrar por meio de perfis, frameworks e evals promovidos pelo `agent-knowledge-ops`, nunca por cópia silenciosa de conteúdo dentro do scaffold.
