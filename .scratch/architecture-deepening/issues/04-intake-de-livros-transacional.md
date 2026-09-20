# 04: Dar profundidade transacional ao intake de livros

**What to build:** Como responsável por um intake de livro, quero receber texto e metadados em `raw/` e um índice navegável em `library/` como uma única operação segura, para que uma falha do extrator nunca deixe o projeto em estado parcialmente materializado.

**Blocked by:** 01 — Tornar o projeto de fonte um contrato executável

**Status:** ready-for-agent

- [ ] Manter a integração com o extrator externo atrás de um adapter de processo e preservar a política de instalação explícita.
- [ ] Normalizar o resultado do extrator antes de materializar os artefatos do projeto.
- [ ] Publicar texto, metadados e índice somente depois de validar o resultado completo.
- [ ] Preservar falhas, códigos de saída, diagnóstico e ausência de arquivos esperados sem criar artefatos parciais.
- [ ] Exigir overwrite explícito e preservar os artefatos existentes quando ele não for informado.
- [ ] Cobrir sucesso, falha, metadados inválidos, saída incompleta, overwrite e links relativos do índice com testes de comportamento.
