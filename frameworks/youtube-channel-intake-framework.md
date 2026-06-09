# Framework De Intake De Canais Do YouTube

Este framework transforma um canal ou playlist do YouTube em uma biblioteca local rastreável, pronta para destilação posterior.

Ele cobre a primeira refinaria:

```text
canal/playlist
-> metadados e legendas
-> biblioteca Markdown
-> índice por tema
-> candidatos de destilação
```

## Objetivo

Criar uma base local navegável antes de tentar extrair conhecimento.

O erro comum é pedir ao agente para "assistir o canal inteiro" e esperar uma síntese confiável. O caminho melhor é separar captação, indexação, destilação e promoção.

## Entradas

- URL de canal, playlist ou lista de vídeos.
- Arquivos `*.info.json` gerados pelo `yt-dlp`.
- Arquivos `*.srt` com legendas ou transcrições.
- Taxonomia inicial de categorias.
- Agente ou produto alvo.

## Saídas

- `raw/`: metadados e transcrições brutas.
- `videos/`: notas por vídeo, organizadas por categoria.
- `index.md`: catálogo geral do canal.
- `missing-videos.tsv`: itens indisponíveis ou sem metadados.
- `channel-intake.md`: decisão editorial sobre o que destilar primeiro.

## Estágios

1. **Capturar**: baixar metadados e legendas sem baixar os vídeos.
2. **Normalizar**: extrair título, canal, data, duração, URL, tags e capítulos.
3. **Classificar**: agrupar vídeos por tema usando regras explícitas.
4. **Materializar**: gerar uma nota Markdown por vídeo.
5. **Indexar**: gerar tabela por data, categoria, status e link.
6. **Priorizar**: escolher quais vídeos merecem destilação.
7. **Destilar**: transformar vídeos selecionados em conhecimento.
8. **Promover**: decidir o que vira method-wiki, skill, playbook ou descarte.

## Regra De Separação

A biblioteca do canal não é ainda conhecimento do agente.

Ela é uma camada de acesso organizada. O conhecimento começa quando uma unidade é lida com pergunta, contexto, evidência, síntese e decisão de promoção.

## Critérios Para Priorizar Vídeos

- Tema central para o agente.
- Vídeo canônico do canal.
- Alta recorrência em títulos, tags ou capítulos.
- Dor operacional explícita.
- Promessa de método, checklist, diagnóstico ou processo.
- Contradição útil com outras fontes.
- Atualidade relevante para o domínio.

## O Que Não Fazer

- Não destilar todos os vídeos na mesma profundidade.
- Não promover transcrição como conhecimento.
- Não tratar categoria automática como verdade.
- Não remover a fonte bruta depois da síntese.
- Não misturar comentários pessoais do agente com evidência do vídeo.

## Relação Com Outros Frameworks

- Use este framework antes do `distillation-framework`.
- Use o `promotion-framework` depois de cada lote de destilações.
- Use o `method-wiki-framework` apenas quando houver padrões recorrentes.
- Use `minimum-agent-product-architecture` quando o canal revelar um produto de agente próprio.
