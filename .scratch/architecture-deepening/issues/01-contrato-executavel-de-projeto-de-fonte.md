# 01: Tornar o projeto de fonte um contrato executável

**What to build:** Como mantenedor, quero criar e validar um projeto de fonte por um contrato executável, para que estrutura, estados, manifest, promotion matrix e separação entre camadas sejam verificáveis antes de qualquer intake ou promoção.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [ ] Criar uma operação de validação que reconheça a estrutura canônica de um projeto de fonte e produza erros acionáveis para arquivos, pastas ou campos ausentes.
- [ ] Validar os estados permitidos, os tipos de fonte e as invariantes que mantêm `raw/`, `library/`, destilação, promoção, operação e produto separados.
- [ ] Fazer a criação e a validação compartilharem o mesmo contrato, sem duplicar regras em adapters de CLI.
- [ ] Cobrir o comportamento com testes de contrato em projetos temporários, incluindo projeto válido, projeto incompleto e manifest inconsistente.
- [ ] Documentar a operação como a forma canônica de verificar um projeto de fonte.
