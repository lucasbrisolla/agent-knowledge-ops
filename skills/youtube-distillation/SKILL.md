---
name: youtube-distillation
description: Use when turning a YouTube channel, playlist, or video into refined agent knowledge through video-by-video distillation.
---

# YouTube Distillation

Use esta skill para transformar canais, playlists e vídeos em conhecimento de agente.

## Fluxo

1. Confirmar se já existe uma biblioteca gerada pelo `youtube-channel-intake`.
2. Se não existir, criar índice do canal ou playlist.
3. Registrar tese do canal, recorrências e temas.
4. Destilar um vídeo por vez.
5. Separar episódio, tese, exemplos e modelos.
6. Extrair princípios, heurísticas, warnings e perguntas.
7. Marcar ideias recorrentes entre vídeos.
8. Promover apenas padrões que sobrevivem a mais de um vídeo ou resolvem lacuna real.

## Guardrails

- Não confundir carisma do apresentador com conhecimento promovível.
- Não promover anedota única como regra.
- Não transformar cada vídeo em nota permanente.
- Registrar contradições entre vídeos quando existirem.
- Não misturar a biblioteca gerada automaticamente com conhecimento já promovido.

## Output

- índice do canal ou playlist
- destilação por vídeo
- lista de padrões recorrentes
- candidatos a method-wiki ou operations
