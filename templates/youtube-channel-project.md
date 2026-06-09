# [Nome Do Canal] — Biblioteca De Transcrições

Biblioteca local de transcrições do canal ou playlist `[nome]`, gerada a partir de arquivos do `yt-dlp`.

## Objetivo Editorial

- Agente/produto alvo:
- Pergunta central:
- Tipo de conhecimento procurado:
- Destino provável:

## Estrutura

- `raw/`: arquivos brutos baixados pelo `yt-dlp`.
- `videos/`: notas Markdown por vídeo, organizadas por categoria.
- `index.md`: catálogo principal.
- `missing-videos.tsv`: vídeos faltantes ou indisponíveis.
- `distillations/`: destilações selecionadas.
- `promotions/`: decisões de promoção.

## Estado Atual

- Vídeos indexados:
- Com transcrição:
- Sem transcrição:
- Última atualização:

## Comando Base De Extração

```bash
yt-dlp "URL_DO_CANAL_OU_PLAYLIST" \
  --skip-download --ignore-errors \
  --write-info-json --write-subs --write-auto-subs \
  --sub-langs "en.*,pt.*" --convert-subs srt \
  --sleep-requests 2 --sleep-interval 5 --max-sleep-interval 15 \
  -o "raw/%(upload_date>%Y-%m-%d)s-%(id)s-%(title).120s.%(ext)s"
```

## Comando Para Gerar A Biblioteca

```bash
python3 tools/build-youtube-library.py --overwrite
```

## Taxonomia Inicial

| Categoria | Quando usar |
|---|---|
|  |  |

## Critérios De Destilação

- Destilar primeiro vídeos com método explícito.
- Destilar depois vídeos que repetem ou contradizem o padrão.
- Ignorar vídeos puramente promocionais, lives sem estrutura ou atualizações sem conteúdo reutilizável.

## Próximos Lotes

| Prioridade | Categoria | Vídeos | Motivo |
|---|---|---:|---|
| Alta |  |  |  |
