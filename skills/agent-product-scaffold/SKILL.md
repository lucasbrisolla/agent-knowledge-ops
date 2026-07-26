---
name: agent-product-scaffold
description: Use quando houver uma especificação de agente-produto e for necessário criar sua casa operacional sem inventar conhecimento de domínio.
---

# Agent Product Scaffold

Use esta skill para transformar uma especificação aprovada em uma estrutura inicial de agente-produto.

## Quando Usar

- O domínio, usuário e output recorrente já foram descritos.
- Existe uma decisão de forma operacional ou um desenho inicial do agente.
- O produto precisa de uma casa própria, mas ainda não deve ser marcado como ativo.

## Não Usar Como

- gerador de conhecimento de domínio
- substituto de `agent-product-decision`
- criação automática de workflows sem método validado
- autorização para copiar contexto empresarial ou pessoal para a camada do sistema

## Entrada Mínima

- nome e slug do produto
- descrição do papel e da fronteira
- domínio-alvo
- usuário principal, se conhecido
- uso recorrente
- output repetido, se conhecido
- fonte ou especificação de origem

## Fluxo

1. Ler `README.md`, `ARCHITECTURE.md`, `FRAMEWORK.md` e o schema de agente-produto.
2. Confirmar que a especificação não pede produto maior que a evidência disponível.
3. Executar `tools/create-agent-product.py` com os campos conhecidos.
4. Revisar `agent-product-spec.md`, `CLAUDE.md` e `DATA_CONTRACT.md`.
5. Preencher somente o método, workflow, skill, template e evals necessários ao primeiro caso real.
6. Executar `tools/validate-agent-product.py`.
7. Manter o status como `candidate` ou `pilot` até haver uso real.

## Saída Esperada

- scaffold completo e navegável
- contrato de dados explícito
- especificação preservada
- routing e guardrails iniciais
- pastas de método, operação, contexto, exemplos e avaliação
- validação estrutural sem placeholders pendentes

## Guardrails

- O scaffold não cria conteúdo específico do domínio.
- `context/` é separado de `_method-wiki/`.
- Um agente-produto candidato não deve ser tratado como fonte canônica ativa.
- Não adicionar runtime multiagente, banco ou dashboard sem dor operacional demonstrada.
