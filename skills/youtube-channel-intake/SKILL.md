---
name: youtube-channel-intake
description: Use quando precisar criar uma biblioteca local de canal ou playlist do YouTube a partir de metadados e legendas do yt-dlp.
---

# YouTube Channel Intake

Use esta skill para transformar um canal, playlist ou lote de vídeos em uma biblioteca Markdown rastreável.

## Quando Usar

- O usuário quer baixar ou organizar um canal inteiro.
- Já existem arquivos `*.info.json` e `*.srt` do `yt-dlp`.
- O objetivo é criar uma base antes da destilação.
- O canal será usado como fonte recorrente para um agente.

## Fluxo

1. Criar pasta do projeto com `raw/`, `videos/`, `distillations/` e `promotions/`.
2. Baixar metadados e legendas com `yt-dlp`, sem baixar os vídeos.
3. Rodar `tools/build-youtube-library.py`.
4. Revisar categorias geradas.
5. Marcar vídeos prioritários para destilação.
6. Usar `youtube-distillation` apenas nos vídeos selecionados.
7. Promover padrões recorrentes usando o `promotion-framework`.

## Comando Base

```bash
yt-dlp "URL_DO_CANAL_OU_PLAYLIST" \
  --skip-download --ignore-errors \
  --write-info-json --write-subs --write-auto-subs \
  --sub-langs "en.*,pt.*" --convert-subs srt \
  --sleep-requests 2 --sleep-interval 5 --max-sleep-interval 15 \
  -o "raw/%(upload_date>%Y-%m-%d)s-%(id)s-%(title).120s.%(ext)s"
```

## Guardrails

- Não baixar vídeos quando metadados e legendas forem suficientes.
- Não apagar `raw/`.
- Não tratar biblioteca gerada como conhecimento refinado.
- Não editar manualmente arquivos gerados se eles serão sobrescritos.
- Não destilar tudo com a mesma profundidade.

## Saídas Esperadas

- `README.md` do projeto.
- `index.md` com tabela navegável.
- `videos/**/*.md` com frontmatter, descrição, capítulos e transcrição.
- Lista de vídeos sem transcrição.
- Lista inicial de prioridades de destilação.
