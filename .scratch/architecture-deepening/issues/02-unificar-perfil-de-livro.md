# 02: Unificar coleção e intake de livros no projeto de fonte

**What to build:** Como responsável por uma fonte de livro, quero usar uma única forma de projeto que preserve índice editorial, matéria-prima e biblioteca, para que a coleção de capítulos e o intake técnico não criem estruturas paralelas.

**Blocked by:** 01 — Tornar o projeto de fonte um contrato executável

**Status:** ready-for-agent

- [ ] Fazer o perfil de livro representar tanto o índice editorial inicial quanto a preparação para artefatos em `raw/` e `library/`.
- [ ] Preservar no índice a unidade por capítulo, prioridade, status editorial e destino provável.
- [ ] Permitir que a coleção comece somente com índice e evolua para intake sem migrar manualmente para outra estrutura.
- [ ] Garantir que o perfil de livro não escreva conhecimento diretamente em `method-wiki/`, `operations/` ou `agent-product/`.
- [ ] Cobrir a criação e a evolução do projeto com testes de comportamento observável.
