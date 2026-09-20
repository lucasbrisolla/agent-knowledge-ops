# Issue tracker

Este repositório usa um tracker local em Markdown.

## Convenções

- Uma iniciativa ocupa um diretório em `.scratch/<feature-slug>/`.
- A especificação fica em `.scratch/<feature-slug>/spec.md`.
- Cada ticket fica em `.scratch/<feature-slug>/issues/<NN>-<slug>.md`.
- Os tickets são numerados em ordem de dependência, começando por `01`.
- O estado de triagem aparece na linha `Status:` perto do início do arquivo.
- Comentários e histórico podem ser acrescentados sob `## Comentários`.

## Publicação

Quando uma skill disser para publicar uma spec ou ticket, criar os arquivos
Markdown dentro de `.scratch/` sem criar issues externas.

## Bloqueios

Cada ticket deve declarar uma linha `Blocked by:` com os números e títulos dos
tickets que precisam estar concluídos antes dele. Um ticket sem dependências
usa `None (can start immediately)`.
