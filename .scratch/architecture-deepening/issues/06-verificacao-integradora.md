# 06: Verificar a integração dos contratos aprofundados

**What to build:** Como mantenedor, quero verificar os fluxos de fonte e de Agent Product juntos depois das migrações, para que o novo contrato aumente locality e leverage sem quebrar adapters, rastreabilidade ou guardrails editoriais.

**Blocked by:** 02 — Unificar coleção e intake de livros no projeto de fonte; 03 — Migrar a biblioteca de YouTube para o contrato de fonte; 04 — Dar profundidade transacional ao intake de livros; 05 — Tornar único o contrato do agent_creator

**Status:** ready-for-agent

- [ ] Executar a suíte completa e confirmar os cenários de criação, validação, coleção de livros, intake de livros, YouTube e Agent Product.
- [ ] Confirmar que todos os adapters legados continuam funcionando ou estão explicitamente documentados como migrados.
- [ ] Confirmar que nenhum fluxo escreve diretamente em destinos de promoção sem decisão editorial registrada.
- [ ] Confirmar que falhas deixam mensagens acionáveis e não deixam artefatos parciais ou estruturas inconsistentes.
- [ ] Atualizar skills, schemas, templates e documentação para apontarem ao contrato executável vigente.
- [ ] Executar checagens de sintaxe e higiene do worktree, incluindo `git diff --check`, sem alterar mudanças locais não relacionadas.
