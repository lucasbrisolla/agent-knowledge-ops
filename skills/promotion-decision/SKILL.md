---
name: promotion-decision
description: Use when deciding whether distilled knowledge should become knowledge-base, method-wiki, operations, agent-product material, archive, or discard.
---

# Promotion Decision

Use esta skill depois de uma destilação.

## Fluxo

1. Identificar a ideia candidata.
2. Verificar se ela e reutilizável sem a fonte.
3. Verificar se já existe algo parecido.
4. Escolher camada de destino.
5. Decidir entre enriquecer existente, criar novo, arquivar ou descartar.
6. Registrar confiança e próximo teste.

## Camadas

- `knowledge-base`: saber estável
- `method-wiki`: critério de pensamento
- `operations`: capacidade executavel
- `agent-product`: produto com fronteira própria
- `archive`: interessante, sem uso agora
- `discard`: não melhora agente

## Guardrails

- Se não muda julgamento nem execução, não promover.
- Se só serve para uma situação, considerar `archive`.
- Se vira ação recorrente, considerar `workflow`.
- Se vira transformação atômica, considerar `skill`.
- Se exige domínio persistente, considerar arquitetura mínima.
