# Framework Principal

Este kit organiza a refinaria de conhecimento: a passagem de fonte bruta para julgamento operacional de agente.

## Objetivo

Permitir que livros, canais de YouTube, posts de Reddit, artigos, sites, PDFs e notas antigas sejam transformados em conhecimento que melhora respostas, decisões e execução de agentes.

Fontes recorrentes de inteligência, como transcrições de resultados de companhias abertas, também entram no mesmo ciclo: primeiro viram biblioteca rastreável, depois destilação, depois método ou operação.

## Ciclo

```text
1. Intake de fonte
2. Biblioteca ou índice de unidades
3. Destilação por unidade
4. Extração de conhecimento
5. Decisão de promoção
6. Atualização de method-wiki
7. Candidato operacional
8. Decisão de forma operacional
9. Checagem de arquitetura mínima
10. Scaffold de agente-produto candidato, se houver especificação suficiente
11. Arquitetura inicial do produto candidato, se o pedido for de criação
```

## Princípio Central

Nem toda fonte merece promoção.

Nem toda boa ideia merece virar skill.

Nem todo conjunto de conhecimento merece virar agent product.

Antes de criar um agente, decida a menor forma operacional suficiente:

```text
nota
-> method-wiki
-> skill/workflow
-> assistente leve
-> operador estruturado
-> sistema de domínio
-> plataforma multi-superfície
```

A pergunta de promoção para agente não é "isso é interessante?". É "qual uso recorrente, output e estado justificam subir de nível?".

Quando a decisão for criar um agente-produto, use `agent-product-scaffold` para gerar a casa operacional mínima. O scaffold não substitui a decisão de promoção e não torna o produto ativo automaticamente.

Quando o pedido vier diretamente como escopo de criação, use `agent-product-creation`: ela interpreta o escopo, registra a especificação e chama o módulo interno `agent_creator`.

## Unidade De Trabalho

Escolha uma unidade pequena antes de ler:

- livro: capítulo
- YouTube: vídeo
- Reddit: thread ou post
- artigo: artigo
- site: página ou seção
- PDF técnico: seção
- earnings call: empresa + trimestre
- release de resultado: seção ou métrica material

## Bibliotecas Geradas

Quando a fonte for grande, crie primeiro uma biblioteca navegável antes da destilação.

Exemplos:

- canal do YouTube: `raw/`, `videos/`, `index.md`
- livro: índice de capítulos, notas por capítulo, matriz de promoção
- Reddit: threads brutas, posts selecionados, clusters de dor
- site: mapa de páginas, notas por página, índice de conceitos
- earnings calls: índice por empresa, trimestre, setor e tema recorrente

O objetivo da biblioteca é dar rastreabilidade e seleção. Ela não substitui a destilação.

## Destinos Possíveis

- `concept`
- `principle`
- `heuristic`
- `pattern`
- `warning`
- `question`
- `checklist`
- `process`
- `template`
- `playbook-candidate`
- `workflow-candidate`
- `skill-candidate`
- `agent-product-decision`
- `agent-product-candidate`
- `discard`

## Teste De Promoção

Promova apenas se a saída:

- melhora julgamento do agente
- reduz erro recorrente
- melhora execução prática
- evita releitura da fonte
- serve em mais de um caso
- tem destino claro
- tem a menor forma operacional suficiente

## Estados Editoriais

- `novo`
- `indexado`
- `destilar`
- `parcialmente coberto`
- `já coberto`
- `promovido`
- `descartar por enquanto`
- `aguardar uso real`

## Guardrail

O kit deve aumentar critério, não volume.

Se uma destilação vira resumo bonito mas não muda decisão, resposta ou execução, ela ainda não virou conhecimento de agente.


## Decisão De Forma Operacional

Use `frameworks/minimum-agent-product-architecture.md` quando uma destilação, evidence bundle ou método começar a pedir produto próprio.

Use `templates/agent-product-decision.md` para registrar a decisão antes de criar agente, skill ou workflow maior.

O resultado esperado não precisa ser sempre agente-produto. Resultados válidos incluem:

- manter como knowledge base
- promover para method-wiki
- criar skill
- criar workflow em produto existente
- criar assistente leve
- criar operador estruturado
- criar sistema operacional de domínio
- aguardar uso real

Regra:

> Criar a menor forma operacional que resolva a dor atual.

## Incorporação De Conhecimento Arquitetural

Frameworks, posts, grafos e outras fontes sobre arquitetura de agentes devem seguir o mesmo ciclo de intake, biblioteca, destilação, síntese e promoção. Só padrões promovidos e avaliados devem alterar templates, perfis ou critérios usados pelo `agent_creator`.
