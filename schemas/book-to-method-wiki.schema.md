# Schema Book To Method-Wiki

Contrato para uma sessão de destilação de livro que promove conhecimento para `_method-wiki`.

## Campos Da Sessão

| Campo | Obrigatório | Descrição |
|---|---|---|
| `book` | sim | Livro ou coleção de origem |
| `unit` | sim | Capítulo, seção ou apêndice |
| `target_agent` | sim | Produto/agente alvo |
| `lens` | sim | Lente de leitura do agente |
| `target_file` | sim | Arquivo alvo no `_method-wiki` |
| `gap` | sim | Lacuna real que justifica leitura |
| `expected_contribution` | sim | Tipo de contribuição esperada |
| `promotion_decision` | sim | Decisão final |
| `index_status` | sim | Status a registrar no índice |

## Valores Para `expected_contribution`

- `concept`
- `heuristic`
- `checklist`
- `pattern`
- `process`
- `warning`
- `question`
- `none`

## Valores Para `promotion_decision`

- `promote-to-existing-md`
- `promote-to-new-md`
- `promote-to-operation-candidate`
- `already-covered`
- `archive`
- `discard`
- `wait-for-pilot`
- `out-of-scope`

## Status Permitidos No Índice

- `já coberto`
- `parcialmente coberto`
- `destilar`
- `spec definida`
- `promovido`
- `aguardar piloto`
- `fora de escopo`
- `descartar por enquanto`

## Regras

- `target_file` deve existir antes da sessão, exceto quando a decisão for `promote-to-new-md`.
- `promote-to-new-md` exige justificativa de lacuna estrutural.
- `already-covered` exige apontar a cobertura existente.
- `discard` exige razão de descarte.
- `out-of-scope` exige domínio para onde o conteúdo pertence ou motivo de exclusão.
- Toda sessão deve atualizar o índice do livro.
