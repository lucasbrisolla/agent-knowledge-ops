---
name: reviewing-agent-architecture
description: Use when the user says they want to improve an agent, an Agent Product, or agent-knowledge-ops and provides multiple Markdown files, frameworks, posts, diagrams, or architectural proposals to evaluate.
---

# Revisão E Aperfeiçoamento De Arquitetura De Agentes

Use esta skill para transformar um lote de fontes arquiteturais em uma decisão de melhoria rastreável. A revisão deve analisar primeiro e alterar arquivos somente depois de aprovação explícita.

## Gatilhos

Acione quando o usuário disser, por exemplo:

- “quero melhorar o agente”;
- “quero melhorar o `agent-knowledge-ops`”;
- “veja estes frameworks e diga o que vale incorporar”;
- “tenho vários MDs/posts sobre arquitetura de agentes”;
- “compare estas ideias com a arquitetura atual”.

O alvo pode ser qualquer Agent Product. Se o alvo não estiver claro, identifique-o antes de carregar as fontes.

## Fluxo

1. Ler a entrada do alvo: `README.md`, `AGENTS.md`/`CLAUDE.md`, `ARCHITECTURE.md`, `FRAMEWORK.md`, `ROADMAP.md` e backlog canônico.
2. Inventariar as fontes recebidas. Para lote grande, criar ou usar um projeto de fonte com `raw/`, `library/`, `distillations/` e `promotions/`.
3. Classificar cada fonte como evidência, padrão, funcionalidade, hipótese, warning ou opinião.
4. Destilar unidades pequenas e preservar origem, autoridade, frescor e contexto.
5. Sintetizar duplicatas, conflitos, lacunas e confiança. Não tratar volume de fontes como evidência de qualidade.
6. Comparar as sugestões com a arquitetura atual nas dimensões:
   - missão e fronteira;
   - interface, routing e carregamento de contexto;
   - fonte viva, persistência e estado;
   - verificabilidade, health check e drift;
   - método, workflows, skills e outputs;
   - escala, integrações, UI e multiagente.
7. Avaliar cada proposta com esta decisão: `incorporar`, `adaptar`, `rejeitar`, `adiar` ou `aguardar uso real`.
8. Produzir um relatório usando `templates/agent-improvement-review.md` ou uma estrutura equivalente.
9. Parar antes de editar o alvo e pedir aprovação das mudanças propostas.

## Critério De Decisão

Uma sugestão só deve ser promovida quando:

- resolve uma dor observável do alvo;
- melhora julgamento, execução, confiabilidade ou manutenção;
- tem evidência suficiente e origem rastreável;
- cabe na menor seam/module suficiente;
- não cria estado paralelo ou drift desnecessário;
- pode ser verificada por exemplo, teste, checklist ou uso real.

Rejeite ou adie sugestões que apenas adicionem sofisticação, duplicação, buzzwords, runtime multiagente, UI, banco ou plugin sem dor operacional demonstrada.

## Modo `review`

É o modo padrão. Não alterar arquivos do agente. Entregar:

- resumo executivo;
- fontes e qualidade da evidência;
- comparação com a arquitetura atual;
- matriz de propostas e decisões;
- mudanças recomendadas por prioridade;
- itens explicitamente não recomendados;
- perguntas ou experimentos necessários;
- próximo passo mínimo.

## Modo `apply`

Só usar depois de aprovação explícita. Para cada mudança aprovada:

1. definir arquivos, seam e critério de pronto;
2. atualizar primeiro contratos, documentação ou testes aplicáveis;
3. implementar a menor mudança composável;
4. validar links, templates, scripts e testes;
5. registrar o que foi incorporado e o que permaneceu pendente.

Se uma descoberta for reutilizável entre agentes, promovê-la no `agent-knowledge-ops` como método, padrão, checklist ou framework. Não copiar fontes brutas para `agent_creator` nem alterar seus templates sem decisão e avaliação.

## Saída Mínima

O relatório deve responder:

1. O que a arquitetura atual faz bem?
2. O que as fontes sugerem de novo?
3. O que é realmente aplicável ao alvo?
4. O que deve ser incorporado agora, depois ou nunca?
5. Qual é a menor mudança verificável?
