# Arquitetura Do Projeto

O `agent-knowledge-ops` é uma refinaria operacional de conhecimento para agentes.

Ele não é apenas um conjunto de prompts. Ele organiza a passagem de fontes brutas para conhecimento promovido, método, operações e produtos de agente.

## Tese Arquitetural

O projeto separa quatro coisas que normalmente ficam misturadas:

1. **Captação**: trazer a matéria-prima para perto.
2. **Destilação**: transformar uma unidade em conhecimento rastreável.
3. **Promoção**: decidir o que merece virar memória operacional.
4. **Produto**: empacotar conhecimento, método e execução em um agente utilizável.

## Mapa De Camadas

```text
sources
  ↓
intake
  ↓
libraries
  ↓
distillations
  ↓
knowledge
  ↓
method-wiki
  ↓
operations
  ↓
agent-product scaffold
  ↓
agent-products
```

## Camadas

| Camada | Responsabilidade | Exemplos |
|---|---|---|
| `sources` | Identificar matéria-prima | livros, vídeos, Reddit, earnings calls, sites |
| `intake` | Capturar e normalizar | `yt-dlp`, scraping, PDFs, RSS |
| `libraries` | Criar navegação local | índice de vídeos, capítulos, threads, calls |
| `distillations` | Extrair valor por unidade | nota por vídeo, capítulo, call, artigo |
| `knowledge` | Consolidar conhecimento | princípios, warnings, padrões, conceitos, evidence bundles |
| `method-wiki` | Ensinar o agente a pensar | heurísticas, checklists, frameworks |
| `operations` | Ensinar o agente a agir | skills, playbooks, workflows, templates |
| `agent-products` | Empacotar produto | README, AGENTS, contratos, exemplos |

## Regra De Dependência

Cada camada pode depender da anterior, mas não deve pular etapas sem justificativa.

```text
raw source != knowledge
library != distillation
distillation != method
method != skill
skill != product
```

## Estrutura Do Repositório

```text
agent-knowledge-ops/
  README.md
  FRAMEWORK.md
  ARCHITECTURE.md
  ROADMAP.md
  frameworks/
  schemas/
  templates/
  skills/
  tools/
  examples/
  agent_creator/
```

## Responsabilidade Dos Diretórios

| Diretório | Função |
|---|---|
| `frameworks/` | Modelos conceituais e critérios de decisão |
| `schemas/` | Contratos de estrutura para notas e artefatos |
| `templates/` | Arquivos base para novos projetos e destilações |
| `skills/` | Procedimentos executáveis por agentes |
| `tools/` | Scripts utilitários locais |
| `examples/` | Casos ilustrativos bons e ruins |
| `agent_creator/` | Materialização e validação de Agent Products candidatos |

## Arquitetura De Um Projeto De Fonte

Um projeto de fonte é uma instância da refinaria aplicada a uma fonte grande.

Exemplo:

```text
source-project/
  README.md
  source-manifest.md
  promotion-matrix.md
  raw/
  library/
  distillations/
  promotions/
  method-wiki/
  operations/
  agent-product/
```

O diretório `agent-product/` fica vazio no início. Ele existe para manter o destino no radar, não para forçar produto antes de haver evidência operacional.

## Contratos Entre Camadas

### Intake Para Biblioteca

Entrada:

- URL, arquivo ou pasta de fonte.
- Metadados mínimos.
- Conteúdo bruto preservável.

Saída:

- Índice navegável.
- Unidades discretas.
- Status de cobertura.
- Links para fonte bruta.

Para livros, `tools/extract-book-source.py` delega a extração determinística ao
`book-to-skill`, persiste `raw/full_text.txt` e `raw/metadata.json` e gera
`library/book-index.md`. Essa integração termina na biblioteca; não cria skill
nem pula a destilação ou a decisão de promoção.

Projetos de fonte compartilham um contrato executável em `source_project/`.
`tools/validate-source-project.py` verifica a estrutura, o manifest, o status e
a promotion matrix antes de um pipeline escrever seus artefatos. Perfis de
livro e YouTube podem manter seus índices específicos, mas não criam uma
segunda estrutura de projeto.

### Biblioteca Para Destilação

Entrada:

- Unidade selecionada.
- Pergunta editorial.
- Agente/produto alvo.

Saída:

- Tese da unidade.
- Ideias reutilizáveis.
- Evidências.
- O que não promover.
- Decisão recomendada.

### Destilação Para Method-Wiki

Entrada:

- Conjunto de destilações.
- Padrões recorrentes.
- Lacuna operacional clara.

Saída:

- Princípio.
- Heurística.
- Checklist.
- Warning.
- Processo.

### Destilação Para Síntese

Entrada:

- Achados de uma ou mais destilações.
- Fontes com autoridade e frescor diferentes.
- Pergunta editorial clara.

Saída:

- Evidence bundle.
- Achados deduplicados.
- Conflitos e lacunas.
- Confiança explícita.
- Recomendação de destino.

### Method-Wiki Para Operação

Entrada:

- Método validado.
- Caso de uso recorrente.
- Forma clara de execução.

Saída:

- Skill.
- Workflow.
- Playbook.
- Template.
- Script de apoio.

### Especificação Para Agente-Produto

Entrada:

- Desenho ou especificação do agente.
- Domínio e fronteira claros.
- Usuário e uso recorrente conhecidos ou explicitamente pendentes.
- Output esperado.

Saída:

- Scaffold navegável de agente-produto.
- `CLAUDE.md` e `AGENTS.md` de entrada.
- `DATA_CONTRACT.md` para separar sistema, contexto e ingestão.
- `agent-product-spec.md` preservando a decisão de criação.
- Pastas de método, workflows, skills, templates, contexto, exemplos e evals.
- Status inicial `candidate`.

O scaffold cria estrutura e contratos. Ele não cria conhecimento de domínio nem transforma automaticamente um produto candidato em produto ativo.

### Módulo Interno `agent_creator`

O `agent-knowledge-ops` continua interpretando o escopo e registrando a decisão. O módulo interno `agent_creator` recebe a especificação aprovada e materializa a casa operacional:

```text
decisão de produto
  ↓
agent_creator.create
  ↓
scaffold + arquitetura inicial + validação
```

Padrões arquiteturais futuros entram por promoção de fontes e métodos. O creator não recebe conteúdo bruto diretamente.

## Tipos De Pipelines

| Pipeline | Exemplo | Saída Inicial |
|---|---|---|
| `youtube-channel-intake` | canal de carreira | biblioteca de vídeos |
| `source-project-setup` | qualquer fonte grande | scaffold de projeto |
| `book-distillation` | livro técnico | destilações por capítulo |
| `book-collection-setup` | pasta `books/<tema>/` | README editorial e índice por capítulo |
| `book-to-method-wiki` | livro com destino em `_method-wiki` | promoção segura para método existente |
| `knowledge-synthesis` | múltiplas fontes sobre o mesmo achado | evidence bundle com confiança |
| `company-web-research` | empresa, JV ou controladora sem contexto local consolidado | mapa de fontes e achados verificáveis |
| `social-signal-research` | Reddit, HN, X | clusters de dor e tendência |
| `web-article-intake` | artigos e sites | mapa de páginas e conceitos |
| `earnings-call-intelligence` | transcrições de resultados | padrões de gestão e setor |
| `agent-product-scaffold` | especificação de agente-produto | casa operacional validável |

## Guardrail Arquitetural

O projeto deve ser modular.

Cada novo tipo de fonte pode ter uma automação própria, mas todos devem convergir para os mesmos contratos:

- biblioteca rastreável
- destilação por unidade
- decisão de promoção
- method-wiki ou operação quando fizer sentido

Quando houver especificação suficiente para um agente-produto, o scaffold deve consumir os contratos existentes em vez de criar uma arquitetura paralela.

Sem esse contrato comum, cada pipeline vira um projeto artesanal isolado.
