# 05: Tornar único o contrato do agent_creator

**What to build:** Como responsável por criar ou validar um Agent Product, quero que a especificação Markdown, a CLI e o validador aceitem o mesmo contrato de `ProductSpec`, para que a forma de entrada não produza scaffolds ou erros diferentes.

**Blocked by:** None (can start immediately)

**Status:** ready-for-agent

- [ ] Consolidar campos obrigatórios, enums, defaults e normalização em uma única fonte executável.
- [ ] Fazer a entrada Markdown, a entrada por argumentos e a validação convergirem para o mesmo contrato.
- [ ] Alinhar os valores aceitos pelo core com os valores expostos pela CLI, preservando compatibilidade dos adapters legados.
- [ ] Produzir mensagens de erro consistentes para campo ausente, placeholder editorial e valor inválido.
- [ ] Cobrir paridade entre entradas, scaffold produzido e validação final com testes de comportamento observável.
- [ ] Manter o creator sem conhecimento de domínio específico e sem promover fontes automaticamente.
