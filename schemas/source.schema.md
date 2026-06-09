# Source Schema

Contrato minimo para registrar uma fonte antes da destilação.

## Campos

| Campo | Obrigatorio | Descricao |
|---|---|---|
| `id` | sim | Identificador curto e estável da fonte |
| `type` | sim | `book`, `youtube`, `article`, `reddit`, `site`, `pdf`, `note` |
| `title` | sim | Título humano da fonte |
| `author_or_channel` | não | Autor, canal, usuario ou instituicao |
| `url_or_path` | sim | Link, caminho local ou referencia de arquivo |
| `date_accessed` | não | Data de acesso ou ingestao |
| `target_agent` | não | Produto/agente alvo |
| `reading_lens` | sim | Pergunta ou filtro de leitura |
| `status` | sim | Estado editorial atual |

## Estados Validos

- `new`
- `indexed`
- `distill`
- `partially-covered`
- `covered`
- `promoted`
- `discard-for-now`
- `wait-for-real-use`

## Regra

Fonte sem `reading_lens` não deve entrar em destilação profunda.
