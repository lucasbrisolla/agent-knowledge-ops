# {{PRODUCT_NAME}}

Produto-agente candidato criado com `agent-knowledge-ops`.

## O Que É

{{DESCRIPTION}}

## Domínio

{{DOMAIN}}

## Usuário Principal

{{TARGET_USER}}

## Uso Recorrente

{{RECURRING_USE}}

## Estado Atual

- Status: `candidate`
- Fonte-base: `{{SOURCE_BASIS}}`
- Método promovido: ainda não validado
- Outputs verificados: ainda não definidos

## Como Começar

1. Ler `CLAUDE.md`.
2. Consultar `domain.md` para escolher o módulo mínimo.
3. Consultar `PRODUCT_INDEX.md` somente quando precisar localizar um artefato.
4. Registrar contexto específico em `context/`, não em `_method-wiki/`.
5. Validar qualquer output recorrente antes de promovê-lo para a fonte viva.

## Estrutura

- `agent-product-spec.md`: especificação e decisão inicial.
- `DATA_CONTRACT.md`: fronteira entre sistema, contexto e fontes.
- `domain.md`: mapa leve do domínio.
- `_method-wiki/`: método reutilizável.
- `workflows/`: sequências recorrentes.
- `skills/`: transformações atômicas.
- `templates/`: formatos de entrada e saída.
- `context/`: dados situados, empresas, casos e fontes vivas.
- `examples/`: calibradores curtos.
- `evals/`: casos para medir qualidade.
- `HEALTH_CHECK.md`: diagnóstico estrutural e operacional.
