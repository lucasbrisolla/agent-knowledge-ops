# Agent Knowledge Ops

Kit operacional para transformar fontes brutas em conhecimento refinado, métodos reutilizáveis e capacidades operacionais para agentes.

![Diagrama do fluxo de refinaria de conhecimento](assets/knowledge-refinery.svg)

## O que este kit resolve

Fontes brutas não entram diretamente em um agente. O kit organiza um fluxo rastreável para capturar, estruturar, destilar e promover conhecimento antes de transformá-lo em método, operação ou agente-produto.

```text
source intake
-> library
-> distillation
-> promotion decision
-> knowledge / method / operation
-> agent product, se houver maturidade
```

A ideia central é simples: um agente não precisa apenas de mais contexto. Ele precisa de conhecimento selecionado com critério e ligado a uma forma de uso.

## O que este kit faz

- organiza fontes grandes em projetos rastreáveis;
- separa fonte bruta, biblioteca, destilação e promoção;
- sintetiza evidências de múltiplas fontes antes de promover conhecimento;
- transforma unidades de conhecimento em method-wikis, workflows, skills e templates;
- cria e valida o scaffold de um agente-produto quando já existe desenho e fronteira suficientes;
- mantém o agente-produto como `candidate` até existir uso real e avaliação.

## Para quem é

O kit atende a quem precisa:

- transformar livros, vídeos, artigos, posts, sites, PDFs ou transcrições em conhecimento reutilizável;
- manter rastreabilidade entre fonte, destilação e decisão editorial;
- promover conhecimento para um method-wiki, uma skill, um workflow ou um template;
- decidir se um caso recorrente realmente precisa de um agente-produto.

## Fluxo de trabalho

Use a menor forma operacional suficiente para o problema atual:

1. Escolha a fonte e uma unidade pequena de trabalho: capítulo, vídeo, artigo, thread, seção ou trimestre.
2. Crie uma biblioteca quando a fonte for grande ou recorrente.
3. Destile cada unidade com uma pergunta editorial clara.
4. Registre o que deve ser promovido, o que já está coberto e o que deve aguardar.
5. Promova apenas conhecimento com destino e uso definidos.
6. Crie uma operação ou um agente-produto somente quando houver método, fronteira e caso de uso recorrente.

O fluxo completo está descrito no [`FRAMEWORK.md`](FRAMEWORK.md). A separação entre camadas está em [`ARCHITECTURE.md`](ARCHITECTURE.md).

## Projeto de fonte

Antes de destilar uma fonte grande, crie um projeto de fonte:

```text
project/
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

Cada camada tem uma função:

- `raw/`: preserva a matéria-prima original ou exportada;
- `library/`: cria um índice navegável e unidades discretas;
- `distillations/`: registra a leitura refinada por unidade;
- `promotions/`: documenta decisões editoriais e justificativas;
- `method-wiki/`: recebe conhecimento promovido como método;
- `operations/`: recebe skills, workflows, playbooks e templates candidatos;
- `agent-product/`: fica reservado para um produto quando houver maturidade suficiente.

### Tipos de fonte

Os templates de projeto cobrem os seguintes casos:

- `youtube`: canal ou playlist, com `vídeo` como unidade principal;
- `book`: livro, com `capítulo` como unidade principal;
- `earnings-calls`: resultados de empresas abertas, com `empresa + trimestre` como unidade principal.

Para uma coleção de livros no padrão `books/<tema>/`, use [`book-collection-setup`](skills/book-collection-setup/SKILL.md). Ele cria o README editorial e o índice por capítulo usados para decidir o que deve ser destilado e promovido.

Quando um livro deve alimentar um `_method-wiki` existente, use [`book-to-method-wiki`](skills/book-to-method-wiki/SKILL.md). A skill define o destino antes da leitura, prioriza o enriquecimento de arquivos existentes e pede a atualização do índice ao final da sessão.

Para extrair um livro para `raw/` e criar `library/book-index.md` antes da destilação, use [`book-source-intake`](skills/book-source-intake/SKILL.md). O extrator é opcional e não cria `SKILL.md` nem promove conhecimento automaticamente.

## Comece pela tarefa

Escolha o ponto de entrada que corresponde ao trabalho:

| Tarefa | Ponto de entrada |
|---|---|
| Criar um projeto de fonte | [`source-project-setup`](skills/source-project-setup/SKILL.md) |
| Validar um projeto de fonte | `python3 tools/validate-source-project.py caminho/do/projeto` |
| Criar uma biblioteca de canal ou playlist | [`youtube-channel-intake`](skills/youtube-channel-intake/SKILL.md) |
| Destilar livros ou vídeos | [`book-distillation`](skills/book-distillation/SKILL.md) ou [`youtube-distillation`](skills/youtube-distillation/SKILL.md) |
| Sintetizar evidências de múltiplas fontes | [`knowledge-synthesis-framework`](frameworks/knowledge-synthesis-framework.md) e [`evidence-bundle`](templates/evidence-bundle.md) |
| Pesquisar uma empresa antes da destilação | [`company-web-research`](skills/company-web-research/SKILL.md) |
| Decidir se algo deve ser promovido | [`promotion-decision`](skills/promotion-decision/SKILL.md) |
| Criar um agente-produto candidato | [`agent-product-creation`](skills/agent-product-creation/SKILL.md) ou [`agent-product-scaffold`](skills/agent-product-scaffold/SKILL.md) |
| Revisar a arquitetura de um agente existente | [`reviewing-agent-architecture`](skills/reviewing-agent-architecture/SKILL.md) |

Para síntese, consulte também o contrato de [`evidence-bundle`](schemas/evidence-bundle.schema.md). Para priorizar fontes por tipo de pergunta, use o [`source-priority-framework`](frameworks/source-priority-framework.md).

## Criar e validar um agente-produto

Quando a especificação já estiver aprovada, crie o scaffold e valide a estrutura:

```bash
python3 tools/create-agent-product.py ../meu-agente \
  --product-name "Meu Agente" \
  --description "Papel e fronteira do agente." \
  --domain "Domínio do agente"

python3 tools/validate-agent-product.py ../meu-agente
```

Para criar a partir de uma especificação aprovada, use:

```bash
python3 tools/create-agent-product-from-spec.py \
  caminho/agent-product-spec.md ../meu-agente
```

O scaffold cria a casa operacional e os contratos iniciais. Ele não cria conhecimento de domínio nem ativa automaticamente o produto.

Para revisar melhorias arquiteturais, use [`reviewing-agent-architecture`](skills/reviewing-agent-architecture/SKILL.md). Separe a análise (`review`) da implementação (`apply`) e só aplique mudanças depois da aprovação correspondente.

## Escolha a menor forma operacional suficiente

Nem toda fonte merece promoção, nem toda boa ideia precisa virar uma skill, e nem todo conhecimento precisa virar um agente completo.

```text
nota
-> method-wiki
-> skill / workflow
-> assistente leve
-> operador estruturado
-> sistema de domínio
-> plataforma multi-superfície
```

A decisão deve considerar o uso recorrente, o output esperado, o estado que precisa ser mantido e a fronteira do produto.

## Estrutura do repositório

| Caminho | Papel |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Instruções canônicas para agentes que trabalham no repositório |
| [`CLAUDE.md`](CLAUDE.md) | Ponto de entrada compatível para instruções de agentes |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | Arquitetura e contratos entre camadas |
| [`FRAMEWORK.md`](FRAMEWORK.md) | Ciclo completo da refinaria |
| [`ROADMAP.md`](ROADMAP.md) | Módulos em aberto e direção de evolução |
| [`frameworks/`](frameworks/) | Modelos conceituais e critérios de decisão |
| [`schemas/`](schemas/) | Contratos de estrutura para notas e artefatos |
| [`templates/`](templates/) | Arquivos-base reutilizáveis |
| [`skills/`](skills/) | Procedimentos executáveis por agentes |
| [`tools/`](tools/) | Scripts utilitários locais |
| [`examples/`](examples/) | Exemplos de destilação e uso |
| [`agent_creator/`](agent_creator/) | Materialização e validação de Agent Products candidatos |

## Regra de ouro

Fonte bruta não entra diretamente no agente.

Ela passa por biblioteca, destilação e decisão de promoção antes de virar conhecimento canônico, método ou operação.
