# Framework Book To Method-Wiki

Este framework controla a passagem de conhecimento de um livro para um `_method-wiki` existente.

Ele é inspirado no padrão de destilação usado em `internal-audit-ops/books`, especialmente Graham e COSO ERM: capítulo ou seção só é trabalhado quando há lacuna real, destino provável e arquivo alvo.

## Objetivo

Reduzir erro ao transformar livro em método operacional.

O objetivo não é resumir capítulos. É melhorar uma base viva de agente com conceitos, heurísticas, checklists, patterns e processos que o agente realmente usará.

## Quando Usar

Use este framework quando:

- o agente já tem ou terá um `_method-wiki`
- um livro deve aprofundar método, julgamento ou execução
- existem capítulos com destinos prováveis
- a leitura deve editar arquivos existentes sempre que possível
- o risco de criar conteúdo teórico demais é alto

## Fluxo

```text
book chapter
-> target method-wiki file
-> gap check
-> selective reading
-> patch existing method
-> promotion record
-> index status update
```

## Regra Central

Destino antes da leitura.

Antes de abrir um capítulo, defina:

- lacuna real no agente
- arquivo alvo em `_method-wiki`
- tipo de contribuição esperada
- critério de promoção
- critério de descarte

## Tipos De Contribuição

- `concept`: melhora vocabulário, definição ou distinção
- `heuristic`: melhora julgamento
- `checklist`: melhora execução ou revisão
- `pattern`: reconhece situação recorrente
- `process`: ordena etapas de trabalho
- `warning`: evita erro recorrente
- `question`: melhora diagnóstico

## Matriz De Decisão

| Resultado | Ação |
|---|---|
| Já coberto com qualidade | Marcar `já coberto` e não mexer |
| Coberto, mas raso | Enriquecer MD existente |
| Lacuna clara e recorrente | Criar novo MD apenas se nenhum destino existente servir |
| Conteúdo interessante, mas sem uso | Marcar `descartar por enquanto` |
| Conteúdo fora do domínio | Marcar fora de escopo |
| Conteúdo depende de uso real | Marcar `aguardar piloto` |

## Ordem De Preferência

1. Enriquecer MD existente.
2. Criar seção em MD existente.
3. Criar novo MD somente se houver lacuna estrutural.
4. Criar skill/workflow apenas se houver método operacional recorrente.
5. Descartar ou arquivar quando não houver destino.

## Status Recomendados No Índice

- `já coberto`
- `parcialmente coberto`
- `destilar`
- `spec definida`
- `promovido`
- `aguardar piloto`
- `fora de escopo`
- `descartar por enquanto`

## Guardrails

- Não carregar livro inteiro se a unidade é capítulo.
- Não criar novo arquivo por padrão.
- Não transformar citação ou resumo em método.
- Não promover conteúdo que não muda decisão, diagnóstico ou execução.
- Não misturar conteúdo de outro domínio no method-wiki central.
- Não deixar capítulo destilado sem atualizar o índice.

## Checklist Antes De Destilar

- [ ] O capítulo tem lacuna real no agente?
- [ ] Existe arquivo alvo?
- [ ] O arquivo alvo foi lido antes da alteração?
- [ ] O destino provável foi registrado no índice?
- [ ] O critério de promoção está claro?
- [ ] O critério de descarte está claro?

## Checklist Depois De Destilar

- [ ] O MD alvo ficou mais útil para execução?
- [ ] A mudança é rastreável até capítulo/seção?
- [ ] O índice foi atualizado?
- [ ] A decisão de promoção foi registrada?
- [ ] O que não foi promovido ficou explícito?
- [ ] Próxima unidade prioritária foi definida?
