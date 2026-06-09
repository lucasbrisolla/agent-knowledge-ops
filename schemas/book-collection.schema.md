# Schema De Coleção De Livros

Contrato para pastas `books/<tema>/` que alimentam agentes.

## Estrutura Recomendada

```text
books/
  tema-ou-livro/
    README.md
    tema-ou-livro-index.md
    raw/
    distillations/
    promotions/
```

## Arquivos Obrigatórios

| Arquivo | Função |
|---|---|
| `README.md` | Define papel editorial, fonte, estratégia, destinos e filtro de promoção |
| `<tema>-index.md` | Mapa por capítulo com status, destino provável e prioridade |

## Campos Do README

- fonte
- leitura atual
- papel da pasta
- estratégia
- fluxo editorial
- destinos possíveis
- filtro de promoção
- regra de uso do índice
- status
- observação

## Campos Do Índice

| Campo | Descrição |
|---|---|
| `Capítulo` | Número ou identificador da unidade |
| `Tema principal` | Tema provável do capítulo |
| `MD relacionado ou destino mais provável` | Onde o achado entraria no agente |
| `Status` | Estado editorial |
| `Observação` | Por que destilar, cobrir, descartar ou aguardar |

## Status Permitidos

- `já coberto`
- `parcialmente coberto`
- `spec definida`
- `destilar`
- `descartar por enquanto`

## Regras

- Todo capítulo deve ter status explícito.
- Todo capítulo `destilar` deve ter destino provável.
- Todo capítulo `já coberto` deve apontar para cobertura existente.
- Todo capítulo `descartar por enquanto` deve ter justificativa.
- O índice deve ser atualizado após cada sessão de leitura.
