# 03: Migrar a biblioteca de YouTube para o contrato de fonte

**What to build:** Como responsável por um canal ou playlist, quero gerar uma library de YouTube dentro de um projeto de fonte válido, para que metadados, legendas, notas e índice respeitem o mesmo contrato editorial das demais fontes.

**Blocked by:** 01 — Tornar o projeto de fonte um contrato executável

**Status:** ready-for-agent

- [ ] Fazer o pipeline localizar o projeto de fonte explicitamente, sem depender implicitamente da pasta corrente.
- [ ] Preservar os arquivos brutos e produzir notas e índice na camada de library definida pelo contrato.
- [ ] Manter a classificação, parsing de SRT, normalização de metadados, capítulos, tags e indicação de transcrição ausente.
- [ ] Permitir regras de categoria customizadas sem alterar a implementação do módulo.
- [ ] Manter a política de não sobrescrever notas existentes sem uma decisão explícita.
- [ ] Cobrir vídeos válidos, vídeos sem legenda, metadados incompletos, categorias customizadas e índice final com testes de contrato.
