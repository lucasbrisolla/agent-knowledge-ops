---
name: book-distillation
description: Use when turning a book or long PDF into agent knowledge through chapter indexing, selective reading, and promotion decisions.
---

# Book Distillation

Use esta skill para destilação geral de livros.

Quando o destino for um `_method-wiki` existente, prefira a skill `book-to-method-wiki`, que é mais rigorosa e reduz risco de criar resumo sem operação.

## Fluxo

1. Criar ou abrir o índice do livro.
2. Definir produto/agente alvo e lente de leitura.
3. Mapear capítulos para destinos provaveis.
4. Marcar status editorial por capítulo.
5. Escolher apenas um capítulo ou seção por sessao.
6. Destilar a unidade escolhida.
7. Decidir promoção.
8. Atualizar o índice para evitar releitura.

## Guardrails

- Não ler o livro inteiro sem unidade e destino.
- Não promover resumo de capítulo para method-wiki.
- Não criar novo MD se arquivo existente puder ser enriquecido.
- Permitir novo MD quando houver lacuna estrutural real.
- Para `_method-wiki`, definir arquivo alvo antes de ler o capítulo.

## Output

- índice atualizado
- nota de destilação
- decisão de promoção
- próximo capítulo prioritario
