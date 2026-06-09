# Schema De Biblioteca De Canal Do YouTube

Contrato textual para bibliotecas geradas a partir de canais ou playlists.

## Estrutura Mínima

```text
project/
  README.md
  index.md
  missing-videos.tsv
  raw/
    *.info.json
    *.srt
  videos/
    Categoria/
      yyyy-mm-dd-videoid-slug.md
```

## Frontmatter Por Vídeo

```yaml
title: ""
youtube_id: ""
channel: ""
url: ""
published: ""
duration: ""
category: ""
status: ""
source: "youtube"
raw_metadata: ""
raw_transcript: ""
tags: []
```

## Status Permitidos

- `transcribed`
- `missing_transcript`
- `metadata_only`
- `needs_review`

## Campos Do Índice

| Campo | Descrição |
|---|---|
| `Published` | Data de publicação normalizada |
| `Category` | Categoria editorial atribuída |
| `Video` | Wikilink para a nota do vídeo |
| `Duration` | Duração em `mm:ss` ou `hh:mm:ss` |
| `Status` | Estado da transcrição |

## Regras

- Caminhos de fonte bruta devem permanecer explícitos.
- O índice pode ser regenerado automaticamente.
- Notas em `videos/` podem ser sobrescritas quando forem puramente geradas.
- Destilações humanas ou assistidas por agente devem morar fora de `videos/` ou em seção protegida.
- A taxonomia deve ser revisável sem apagar rastreabilidade.
