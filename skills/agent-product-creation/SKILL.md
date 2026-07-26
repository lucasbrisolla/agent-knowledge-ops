---
name: agent-product-creation
description: Use quando o usuário pedir a criação de um novo Agent Product a partir de um escopo, domínio ou método aprovado.
---

# Criação De Agent Product

Use esta skill como fluxo de orquestração para pedidos como “crie o `value-ops`”.

## Fronteira

Esta skill pertence ao `agent-knowledge-ops` e coordena a criação. A materialização filesystem é delegada ao módulo interno `agent_creator`.

## Fluxo

1. Ler `README.md`, `ARCHITECTURE.md`, `FRAMEWORK.md` e o framework de arquitetura mínima.
2. Identificar papel, fronteira, usuário, uso recorrente, output, fontes vivas, estado e verificações.
3. Escolher a menor forma operacional suficiente.
4. Registrar a decisão em uma especificação Markdown com frontmatter compatível com `agent_creator/schemas/agent-product.schema.md`.
5. Recusar ou reduzir o escopo quando não houver uso recorrente, output ou fronteira suficiente.
6. Executar:

```bash
python3 tools/create-agent-product-from-spec.py \
  caminho/agent-product-spec.md \
  caminho/do/novo-produto
```

7. Revisar `README.md`, `domain.md`, `DATA_CONTRACT.md`, `PRODUCT_INDEX.md` e `HEALTH_CHECK.md` do produto criado.
8. Executar `tools/validate-agent-product.py`.
9. Manter o produto como `candidate` até existir método suficiente, uso real e avaliação mínima.

## O Que Preencher Na Primeira Execução

- arquitetura inicial;
- routing mínimo;
- contrato de dados;
- estado e health check;
- perguntas e decisões pendentes;
- esqueleto dos módulos necessários.

Não preencher método, workflow complexo ou contexto específico sem evidência e caso real. Não tratar a criação do scaffold como ativação do produto.

## Integração Com Conhecimento Arquitetural

Frameworks, posts e grafos sobre arquitetura de agentes devem ser incorporados primeiro ao fluxo de fontes do `agent-knowledge-ops`. Somente padrões promovidos e avaliados podem alterar templates, perfis ou critérios do `agent_creator`.
