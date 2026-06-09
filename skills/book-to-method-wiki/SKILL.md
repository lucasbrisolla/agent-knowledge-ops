---
name: book-to-method-wiki
description: Use quando um livro deve enriquecer um `_method-wiki` existente com baixa chance de erro, editando arquivos alvo e atualizando índice editorial.
---

# Book To Method-Wiki

Use esta skill para destilar capítulos de livros diretamente para um `_method-wiki` existente.

Ela é mais rigorosa que `book-collection-setup`: aqui o objetivo não é montar a pasta do livro, mas promover conhecimento para método operacional.

## Quando Usar

- O agente já tem `_method-wiki`.
- O livro já tem `README.md` e índice editorial.
- Existe capítulo/seção priorizado.
- O destino provável já foi definido.
- A meta é enriquecer método, não resumir livro.

## Fluxo

1. Abrir índice do livro.
2. Escolher uma unidade com status `destilar`, `parcialmente coberto` ou `aguardar piloto`.
3. Confirmar lacuna real no agente.
4. Abrir o arquivo alvo no `_method-wiki`.
5. Ler apenas a unidade necessária do livro.
6. Comparar fonte com cobertura existente.
7. Enriquecer arquivo existente sempre que possível.
8. Criar novo MD só com lacuna estrutural clara.
9. Registrar decisão de promoção.
10. Atualizar status no índice do livro.

## Ordem De Preferência

1. Marcar `já coberto` se não houver ganho.
2. Enriquecer MD existente.
3. Criar seção em MD existente.
4. Criar novo MD apenas se inevitável.
5. Criar candidato operacional apenas depois de método claro.
6. Descartar ou arquivar conteúdo sem destino.

## Guardrails

- Não ler o livro inteiro.
- Não criar resumo de capítulo como destino final.
- Não editar method-wiki sem ler o arquivo alvo.
- Não criar MD novo se arquivo existente puder ser melhorado.
- Não promover conteúdo fora da lente do agente.
- Não deixar índice desatualizado depois da sessão.

## Output Esperado

- Patch ou orientação clara para arquivo alvo.
- Decisão de promoção.
- Status atualizado no índice.
- Lista do que não foi promovido.
- Próxima unidade prioritária.
