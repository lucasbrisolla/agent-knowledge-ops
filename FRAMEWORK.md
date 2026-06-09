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
8. Checagem de arquitetura mínima
```

## Princípio Central

Nem toda fonte merece promoção.

Nem toda boa ideia merece virar skill.

Nem todo conjunto de conhecimento merece virar agent product.

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
- `discard`

## Teste De Promoção

Promova apenas se a saída:

- melhora julgamento do agente
- reduz erro recorrente
- melhora execução prática
- evita releitura da fonte
- serve em mais de um caso
- tem destino claro

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
