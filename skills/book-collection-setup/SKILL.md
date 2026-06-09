---
name: book-collection-setup
description: Use quando precisar criar uma pasta editorial de livro em `books/` com README e índice no padrão usado por agentes como accounting-ops.
---

# Book Collection Setup

Use esta skill para criar ou revisar uma pasta `books/<tema>/` que servirá como camada editorial de livros para um agente.

## Quando Usar

- Um livro deve alimentar method-wiki, workflows, playbooks ou skills.
- O usuário quer replicar o padrão `books/<tema>/README.md` + `<tema>-index.md`.
- A leitura atual está no nível de índice/sumário.
- Ainda não está claro quais capítulos merecem destilação.

## Fluxo

1. Criar pasta `books/<tema>/`.
2. Criar `README.md` com papel editorial, fonte, estratégia e filtro de promoção.
3. Criar `<tema>-index.md` com mapa por capítulo.
4. Classificar cada capítulo por status.
5. Definir destino provável antes da leitura detalhada.
6. Priorizar capítulos de alta aderência.
7. Promover apenas conteúdo com lacuna real no agente.

## Comando Base

```bash
python3 tools/create-book-collection.py books/budgeting \
  --book-title "Budgeting" \
  --target-agent accounting-ops \
  --source "/caminho/do/livro.epub"
```

## Status Permitidos

- `já coberto`
- `parcialmente coberto`
- `spec definida`
- `destilar`
- `descartar por enquanto`

## Guardrails

- Não resumir o livro inteiro.
- Não transformar a pasta `books/` em destino final.
- Não criar chapter notes sem destino provável.
- Não promover conteúdo que apenas "parece interessante".
- Atualizar o índice depois de cada sessão para evitar releitura.

## Saídas Esperadas

- `README.md` editorial.
- `<tema>-index.md` com mapa por capítulo.
- Lista de prioridades de destilação.
- Destinos prováveis para capítulos relevantes.
