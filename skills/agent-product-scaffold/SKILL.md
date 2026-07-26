---
name: agent-product-scaffold
description: Use como adapter legado quando uma especificação aprovada precisar virar um scaffold de Agent Product.
---

# Agent Product Scaffold

Esta skill preserva o nome histórico do scaffold, mas delega a implementação ao módulo interno `agent_creator`.

## Quando Usar

- O domínio, usuário, uso recorrente e output já foram descritos.
- Existe uma decisão de forma operacional ou uma especificação aprovada.
- O produto precisa de uma casa própria, mas ainda deve permanecer como `candidate`.

## Não Usar Como

- gerador de conhecimento de domínio;
- substituto da decisão de promoção;
- criação automática de workflows sem método validado;
- autorização para copiar contexto empresarial ou pessoal para a camada do sistema.

## Fluxo

1. Use `agent-product-creation` para interpretar o pedido e preparar a especificação.
2. Execute `tools/create-agent-product-from-spec.py` para materializar o scaffold.
3. Revise `domain.md`, `DATA_CONTRACT.md`, `PRODUCT_INDEX.md` e `HEALTH_CHECK.md`.
4. Execute `tools/validate-agent-product.py`.
5. Mantenha o status como `candidate` ou `pilot` até haver uso real e avaliação.

## Guardrails

- O módulo não cria conteúdo específico do domínio.
- `context/` é separado de `_method-wiki/`.
- O produto candidato não é fonte canônica ativa.
- Não adicionar runtime multiagente, banco ou dashboard sem dor operacional demonstrada.
