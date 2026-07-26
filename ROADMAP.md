# Roadmap

Ideias e próximos módulos para o `agent-knowledge-ops`.

## Princípio

O roadmap guarda possibilidades sem confundir o núcleo do framework.

Uma ideia só deve virar framework, skill ou ferramenta quando tiver:

- fonte recorrente
- saída clara
- valor para um agente
- contrato reaproveitável

## Módulos Em Aberto

| Módulo | Status | Ideia |
|---|---|---|
| `source-project-setup` | iniciado | Criar estrutura padrão para organizar fontes grandes |
| `youtube-channel-intake` | iniciado | Criar bibliotecas locais de canais e playlists |
| `book-distillation` | iniciado | Destilar livros por capítulo para conhecimento de agente |
| `book-collection-setup` | iniciado | Criar README editorial e índice de livros no padrão `books/` |
| `book-to-method-wiki` | iniciado | Promover capítulos de livros para `_method-wiki` com baixo risco de erro |
| `knowledge-synthesis` | iniciado | Sintetizar evidências de múltiplas fontes antes da promoção |
| `company-web-research` | iniciado | Fazer pesquisa web rastreável sobre empresas, JVs e controladoras antes da destilação |
| `social-signal-research` | planejado | Transformar Reddit, HN, X, YouTube e comunidades em sinais |
| `web-article-intake` | planejado | Capturar sites e artigos como unidades rastreáveis |
| `earnings-call-intelligence` | ideia registrada | Analisar transcrições de resultados de companhias abertas |
| `agent-product-decision` | iniciado | Decidir que forma operacional criar antes de scaffoldar agente |
| `agent-product-scaffold` | iniciado | Gerar e validar a casa operacional de um agente-produto |
| `agent-product-creation` | iniciado | Orquestrar pedido de criação e delegar ao módulo interno `agent_creator` |

## Earnings Call Intelligence

Ideia registrada para explorar depois.

Objetivo:

Transformar transcrições de resultados, conference calls, releases e apresentações de companhias abertas em inteligência operacional para agentes.

Possíveis perguntas:

- Quais tendências aparecem em várias empresas do mesmo setor?
- O que empresas líderes estão fazendo sobre margem, eficiência, IA, capex, pricing ou caixa?
- Quais riscos estão ficando recorrentes?
- Como a linguagem da gestão mudou ao longo dos trimestres?
- Quais práticas parecem estar se espalhando entre pares?
- Que sinais antecipam mudança de estratégia, ciclo ou pressão competitiva?

Possíveis saídas:

- índice por empresa, trimestre e setor
- destilação por call
- matriz de tendências
- comparação entre pares
- warnings setoriais
- método de análise de resultado
- skill de leitura de earnings call

## Projeto De Fonte

Primeiro pacote operacional para organizar fontes grandes.

```text
project/
  README.md
  source-manifest.md
  raw/
  library/
  distillations/
  promotions/
  method-wiki/
  operations/
  agent-product/
```

Status:

- framework criado
- schema criado
- templates criados
- skill criada
- ferramenta `create-source-project.py` criada

## Knowledge Synthesis

Pacote para aumentar rigor entre destilação e promoção.

Status:

- `knowledge-synthesis-framework.md` criado
- `source-priority-framework.md` criado
- `evidence-bundle.schema.md` criado
- `evidence-bundle.md` criado
- exemplo multissource criado

## Company Web Research

Skill para pesquisa web empresarial com foco em rastreabilidade antes da destilação.

Status:

- skill criada
- integração leve ao fluxo principal documentada
- próximo passo possível: criar framework ou template de sessão se o padrão se repetir

## Decisão De Forma Operacional

Camada adicionada antes de qualquer scaffold de agente-produto.

Status:

- `frameworks/minimum-agent-product-architecture.md` atualizado para classificar forma operacional
- `schemas/agent-product-decision.schema.md` criado
- `templates/agent-product-decision.md` criado

Objetivo:

Evitar que toda fonte boa vire agente completo. A decisão deve escolher a menor forma suficiente: nota, method-wiki, skill, workflow, assistente leve, operador estruturado, sistema de domínio ou plataforma.

## Agente-Produto

O scaffold foi iniciado. A criação da estrutura pode acontecer a partir de uma especificação de agente, mas a ativação do produto continua condicionada a uso real.

Critério para avançar:

- pelo menos um projeto de fonte com destilações reais
- pelo menos uma promotion matrix preenchida
- pelo menos um método promovido
- caso de uso recorrente claro

Status do scaffold:

- schema de agente-produto criado
- templates de entrada, contrato, índice, domínio, estado e health check criados
- skill `agent-product-scaffold` criada
- `tools/create-agent-product.py` criado
- `tools/validate-agent-product.py` criado
- testes de criação e validação criados

## Módulo Interno `agent_creator`

Status:

- core extraído para `agent_creator/`;
- templates genéricos e schema movidos para o módulo;
- criação a partir de especificação Markdown adicionada;
- validação de enums e campos editoriais adicionada;
- adapters legados preservados.

Próximos passos:

- criar o primeiro produto real a partir de um caso de uso;
- promover padrões arquiteturais de fontes externas somente após síntese e avaliação;
- adicionar perfis arquiteturais quando houver mais de um caso real comparável.
