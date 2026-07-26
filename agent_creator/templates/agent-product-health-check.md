# Health Check — {{PRODUCT_NAME}}

Use esta nota para avaliar se o produto está pronto para sair de `candidate` e suportar uso recorrente.

## Escopo Inicial

- Domínio: {{DOMAIN}}
- Uso recorrente: {{RECURRING_USE}}
- Output esperado: {{REPEATED_OUTPUT}}
- Verificação indicada na especificação: `{{VERIFICATION_NEEDED}}`

## Escala

- `0`: ausente ou apenas implícito.
- `1`: frágil ou ambíguo.
- `2`: utilizável com disciplina manual.
- `3`: modular, revisável e confiável.

## Check Estrutural

| Área | Pergunta | Nota | Evidência |
|---|---|---:|---|
| Entrada | `CLAUDE.md` roteia sem carregar a base inteira? |  |  |
| Método | O método está separado de contexto específico? |  |  |
| Routing | O problema chega ao workflow ou skill correto? |  |  |
| Dados | `DATA_CONTRACT.md` protege fontes vivas e contexto do usuário? |  |  |
| Outputs | Os artefatos têm formato e consumidor definidos? |  |  |
| Verificação | Cada output relevante possui `verify`, revisão ou evidência adequada? |  |  |
| Avaliação | Existem exemplos e casos antes/depois? |  |  |
| Estado | O ciclo de vida do produto está explícito em `states.yml`? |  |  |

## Gate De Ativação

Só mudar `status` para `active` quando houver:

- uso recorrente observado;
- pelo menos um workflow utilizado em caso real;
- outputs canônicos definidos;
- método suficiente para o escopo;
- avaliação mínima registrada;
- fronteira de dados revisada.
