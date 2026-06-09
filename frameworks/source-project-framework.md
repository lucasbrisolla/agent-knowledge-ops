# Framework De Projeto De Fonte

Um projeto de fonte é a unidade operacional usada pelo `agent-knowledge-ops` para organizar uma fonte grande antes da destilação.

Ele existe para evitar que cada canal, livro, site, conjunto de posts ou coleção de calls vire uma estrutura artesanal diferente.

## Quando Criar Um Projeto De Fonte

Crie um projeto de fonte quando houver:

- mais de uma unidade de leitura
- necessidade de rastreabilidade
- possibilidade de destilação em lotes
- chance de promover conhecimento para mais de um agente
- valor em preservar fonte bruta, índice e decisões

Exemplos:

- um canal de YouTube
- um livro técnico
- uma coleção de artigos
- threads de Reddit sobre um domínio
- transcrições trimestrais de empresas abertas
- PDFs recorrentes de um regulador

## Estrutura Padrão

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

## Responsabilidade Das Pastas

| Caminho | Responsabilidade |
|---|---|
| `raw/` | Guardar matéria-prima original ou exportada |
| `library/` | Criar índice navegável e notas geradas |
| `distillations/` | Guardar destilações por unidade |
| `promotions/` | Guardar decisões editoriais |
| `method-wiki/` | Receber conhecimento promovido em método |
| `operations/` | Receber skills, workflows, playbooks e templates candidatos |
| `agent-product/` | Guardar material quando virar produto de agente |

## Arquivos De Controle

### `README.md`

Explica o projeto para humanos e agentes:

- qual é a fonte
- por que ela importa
- qual agente/produto ela pode melhorar
- qual é o estado atual
- quais são os próximos lotes

### `source-manifest.md`

É o contrato editorial da fonte:

- origem
- escopo
- pergunta central
- critérios de inclusão/exclusão
- status de cobertura
- agentes impactados

### `promotion-matrix.md`

É a mesa de decisão:

- o que foi encontrado
- tipo de conhecimento
- destino provável
- confiança
- evidência
- arquivo alvo
- próximo teste

## Fluxo

1. Criar o projeto de fonte.
2. Preencher `source-manifest.md`.
3. Capturar ou importar material em `raw/`.
4. Gerar ou escrever biblioteca em `library/`.
5. Selecionar unidades prioritárias.
6. Criar destilações em `distillations/`.
7. Registrar decisões em `promotion-matrix.md` e `promotions/`.
8. Promover apenas o que tiver destino claro.

## Estados Do Projeto

- `novo`
- `capturando`
- `indexado`
- `destilando`
- `parcialmente-promovido`
- `promovido`
- `arquivado`

## Guardrails

- Não colocar transcrição bruta direto em `method-wiki/`.
- Não criar skill sem método validado.
- Não preencher `agent-product/` antes de haver caso de uso recorrente.
- Não apagar `raw/` quando a fonte for difícil de recuperar.
- Não confundir volume processado com conhecimento promovido.

## Próxima Camada

Quando um projeto de fonte começa a gerar métodos recorrentes, ele pode alimentar:

- `method-wiki`
- `operations`
- `agent-product`

Essa decisão pertence ao `promotion-framework` e ao `minimum-agent-product-architecture`.
