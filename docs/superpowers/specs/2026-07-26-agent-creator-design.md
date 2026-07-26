# Módulo `agent-creator` — Especificação De Design

**Data:** 2026-07-26
**Status:** aprovado para implementação
**Escopo:** primeiro módulo interno de criação de Agent Products do `agent-knowledge-ops`

## Contexto

O `agent-knowledge-ops` já possui um scaffold de agente-produto, mas a capacidade está misturada com a refinaria de conhecimento. O scaffold atual cria arquivos, diretórios e contratos a partir de argumentos de CLI; ele não interpreta um escopo, não registra uma decisão de produto e não gera uma arquitetura inicial orientada ao caso de uso.

Ao mesmo tempo, o framework de arquitetura mínima evoluiu no backlog e a cópia mantida dentro do produto ficou menor e desatualizada. É necessário criar uma seam explícita entre:

```text
escopo, fontes e método promovido
-> decisão de produto
-> agent-creator
-> Agent Product candidate
```

## Objetivo

Criar um módulo interno chamado `agent-creator` que materialize uma especificação aprovada em um scaffold navegável e em uma arquitetura inicial mínima, mantendo o `agent-knowledge-ops` como porta de entrada e orquestrador.

## Não Objetivos

O módulo não deve, nesta versão:

- inventar conhecimento específico do domínio;
- transformar posts, frameworks ou fontes brutas diretamente em método canônico;
- criar workflows complexos sem caso de uso real;
- escolher automaticamente uma arquitetura multiagente, UI, banco ou integração externa;
- ativar o produto ou marcá-lo como `active`;
- sobrescrever arquivos existentes por padrão;
- substituir a decisão de promoção do `agent-knowledge-ops`.

## Fronteira Do Módulo

### `agent-knowledge-ops`

Responsável por:

- intake, biblioteca, destilação e síntese de fontes;
- promoção para conhecimento, método, operação ou produto;
- interpretação do escopo fornecido pelo usuário;
- registro da decisão de forma operacional;
- chamada do `agent-creator` com uma especificação estruturada.

### `agent-creator`

Responsável por:

- consumir a especificação estruturada;
- criar a casa operacional do produto;
- gerar a arquitetura inicial e seus contratos;
- preservar o status `candidate`;
- validar estrutura, campos mínimos, placeholders e referências essenciais.

## Interface

A interface de alto nível deve ter duas operações:

```text
create(specification, target)
validate(target)
```

O formato de entrada será uma especificação Markdown com frontmatter compatível com o schema de agente-produto. A CLI pode continuar aceitando argumentos por compatibilidade, mas deve produzir a mesma especificação estruturada e usar a mesma implementação interna.

### Campos Mínimos Da Especificação

- `product_id`;
- `product_name`;
- `description`;
- `target_domain`;
- `source_basis`;
- `recurring_use`;
- `repeated_output`;
- `state_needed`;
- `verification_needed`;
- `recommended_form`;
- `status`.

Campos ausentes ou valores fora do contrato devem gerar erro explícito. Defaults editoriais como `[definir]` não devem ser tratados como preenchimento válido para um produto pronto para pilotar.

## Saída Inicial

O módulo deve gerar, sem conteúdo de domínio inventado:

```text
produto/
  AGENTS.md
  CLAUDE.md
  README.md
  DATA_CONTRACT.md
  PRODUCT_INDEX.md
  HEALTH_CHECK.md
  agent-product-spec.md
  domain.md
  states.yml
  _method-wiki/README.md
  workflows/README.md
  skills/README.md
  templates/README.md
  context/README.md
  examples/README.md
  evals/README.md
  scripts/README.md
  archive/README.md
```

O `domain.md`, o routing, o `DATA_CONTRACT.md` e o `HEALTH_CHECK.md` devem explicar a arquitetura inicial e registrar decisões pendentes de forma explícita. As pastas de método e operação permanecem como esqueletos até haver caso real.

## Regras De Segurança

- Criar uma pasta vazia ou uma pasta inexistente sem exigir confirmação adicional.
- Recusar uma pasta existente e não vazia, salvo uso explícito de `--force`/modo equivalente.
- Com `--force`, escrever apenas arquivos ausentes e preservar arquivos existentes.
- Nunca copiar contexto empresarial, pessoal ou de caso para a camada do sistema.
- Manter `status: "candidate"` como default seguro.
- Não considerar a existência de diretórios vazios como evidência de método ou operação validada.

## Validação

O validador deve distinguir:

- erros estruturais: arquivos ou diretórios ausentes, UTF-8 inválido, placeholders não resolvidos e campos obrigatórios ausentes;
- erros de contrato: enums inválidos, status incompatível, especificação incompleta ou `AGENTS.md` sem referência a `CLAUDE.md`;
- avisos de maturidade: produto fora de `candidate`, campos editoriais pendentes ou ausência de outputs ainda esperada para um scaffold inicial.

A validação estrutural não deve afirmar que o domínio está correto. Ela apenas confirma que o produto candidato está em uma forma operável e revisável.

## Testes

Os testes devem provar, test-first:

1. uma especificação válida cria a arquitetura inicial;
2. a criação preserva todos os valores da especificação;
3. uma especificação inválida falha com mensagem acionável;
4. arquivos existentes não são sobrescritos;
5. o produto gerado passa na validação estrutural;
6. placeholders editoriais proibidos são rejeitados;
7. a CLI legada continua produzindo o mesmo contrato básico.

## Evolução Posterior

Depois de um primeiro caso real, o módulo poderá receber:

- perfis arquiteturais por tipo de produto;
- seleção de padrões promovidos pelo `agent-knowledge-ops`;
- geração assistida do primeiro workflow, template ou eval;
- integração com uma base de padrões de arquitetura de agentes;
- evals de arquitetura antes/depois.

Essas extensões não entram no v1 para evitar que o scaffold passe a inventar método ou arquitetura específica sem evidência.
