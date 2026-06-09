# Schema De Projeto De Fonte

Contrato mínimo para projetos de fonte criados pelo `agent-knowledge-ops`.

## Estrutura

```text
project/
  README.md
  source-manifest.md
  promotion-matrix.md
  raw/
  library/
  distillations/
  promotions/
  method-wiki/
  operations/
  agent-product/
```

## Arquivos Obrigatórios

| Arquivo | Obrigatório | Função |
|---|---|---|
| `README.md` | sim | Visão humana do projeto |
| `source-manifest.md` | sim | Contrato editorial da fonte |
| `promotion-matrix.md` | sim | Decisões de promoção |

## Pastas Obrigatórias

| Pasta | Obrigatória | Pode ficar vazia? |
|---|---|---|
| `raw/` | sim | sim |
| `library/` | sim | sim |
| `distillations/` | sim | sim |
| `promotions/` | sim | sim |
| `method-wiki/` | sim | sim |
| `operations/` | sim | sim |
| `agent-product/` | sim | sim |

## Campos Do Manifest

```yaml
project:
source_type:
source_name:
source_url:
owner:
created:
status:
target_agents: []
probable_outputs: []
```

## Status Permitidos

- `novo`
- `capturando`
- `indexado`
- `destilando`
- `parcialmente-promovido`
- `promovido`
- `arquivado`

## Tipos De Fonte

- `book`
- `youtube-channel`
- `youtube-playlist`
- `reddit`
- `web-site`
- `web-articles`
- `pdf-collection`
- `earnings-calls`
- `notes`
- `mixed`

## Destinos Prováveis

- `knowledge`
- `method-wiki`
- `checklist`
- `workflow`
- `playbook`
- `skill`
- `template`
- `agent-product`
- `archive`

## Regras

- Todo item promovido precisa apontar para fonte ou destilação.
- Toda destilação precisa ter unidade identificável.
- Todo agente-produto precisa nascer depois de evidência operacional.
- O schema organiza o projeto; ele não decide relevância sozinho.
