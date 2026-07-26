# Contrato De Dados — {{PRODUCT_NAME}}

Define a fronteira entre método reutilizável, contexto situado, fontes e estado do produto.

## Decisão Inicial

- Domínio: {{DOMAIN}}
- Fonte-base: {{SOURCE_BASIS}}
- Estado necessário: `{{STATE_NEEDED}}`
- Verificação necessária: `{{VERIFICATION_NEEDED}}`
- Forma recomendada: `{{RECOMMENDED_FORM}}`

## Camada Do Sistema

Pode ser atualizada como parte da evolução do agente:

- `CLAUDE.md`
- `README.md`
- `PRODUCT_INDEX.md`
- `domain.md`
- `DATA_CONTRACT.md`
- `HEALTH_CHECK.md`
- `states.yml`
- `_method-wiki/`
- `workflows/`
- `skills/`
- `templates/`
- `scripts/`

## Camada Do Usuário E Do Contexto

Não sobrescrever ou reorganizar sem autorização explícita:

- `context/`
- `examples/` quando contiverem casos reais
- outputs produzidos em sessões de trabalho
- decisões, dados de empresas e premissas situadas

## Camada De Ingestão

Fontes brutas e projetos de fonte devem preservar rastreabilidade. Eles podem viver em `books/`, em projetos de fonte externos ou em subpastas de `context/`, desde que a origem e a decisão de promoção estejam registradas.

## Regra De Promoção

Informação específica de empresa, pessoa ou caso começa em `context/`. Ela só sobe para `_method-wiki/`, `workflows/` ou `skills/` quando demonstrar padrão reutilizável ou rotina recorrente.

## Regra De Escrita

Antes de modificar qualquer arquivo vivo:

1. ler o arquivo atual;
2. identificar se ele pertence à camada do sistema ou do usuário;
3. preservar a origem e a decisão que justificam a alteração;
4. validar o output produzido.
