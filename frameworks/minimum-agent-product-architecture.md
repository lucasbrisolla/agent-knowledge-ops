# Minimum Agent Product Architecture

Usar quando uma base de conhecimento ou método comeca a pedir um produto/agente próprio.

## Pergunta Central

Isso já virou um agent product de verdade ou ainda é apenas conhecimento organizado?

## Camadas Minimas

1. Superficie de uso
2. Fonte viva e persistência
3. Verificabilidade
4. Operação recorrente
5. Controle de drift

## Blocos Possíveis

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `PRODUCT_INDEX.md`
- `DATA_CONTRACT.md`
- `HEALTH_CHECK.md`
- `domain.md`
- `_method-wiki/`
- `workflows/`
- `skills/`
- `templates/`
- `examples/`
- `scripts/`

## Regra

Nem todo conhecimento refinado merece virar produto.

Criar um agent product apenas quando houver:

- domínio persistente
- uso recorrente
- fronteira clara
- artefatos ou outputs repetidos
- necessidade de estado ou fonte viva
- risco de drift se ficar solto

## Resultado Da Avaliacao

- `não criar produto`
- `manter como knowledge base`
- `promover para method-wiki de produto existente`
- `criar workflow em produto existente`
- `criar novo agent product`
