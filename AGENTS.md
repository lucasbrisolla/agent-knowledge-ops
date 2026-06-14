# Instruções Para Agentes

Este arquivo é a fonte canônica de orientação para agentes trabalhando neste repositório.

Se outro arquivo de instrução existir, como `CLAUDE.md`, ele deve apontar para este arquivo em vez de duplicar regras.

## Missão Do Repositório

O `agent-knowledge-ops` é uma refinaria operacional de conhecimento para agentes.

Sua função é transformar fontes brutas em:

- bibliotecas rastreáveis
- destilações por unidade
- conhecimento promovido
- method-wiki
- operações reutilizáveis
- candidatos a agente-produto

## Ordem De Leitura

Antes de editar, leia nesta ordem:

1. `README.md`
2. `ARCHITECTURE.md`
3. `FRAMEWORK.md`
4. `ROADMAP.md`
5. O framework, schema, template ou skill diretamente relacionado à tarefa

## Backlog Canônico

O backlog deste repositório fica em:

- `/home/lucas/Dropbox/Obsidian Vault/Agent Products/_backlog/backlog-agent-knowledge-ops.md`

Ao priorizar trabalho, consulte esse arquivo antes de abrir novas frentes.

## Princípio Central

Fonte bruta não entra direto no agente.

O fluxo correto é:

```text
source intake
-> library
-> distillation
-> promotion decision
-> knowledge/method/operation
-> agent product, se houver maturidade
```

## Como Organizar Projetos De Fonte

Use projetos de fonte para qualquer fonte grande ou recorrente.

Estrutura padrão:

```text
project/
  README.md
  source-manifest.md
  promotion-matrix.md
  raw/
  library/
  distillations/
  promotions/
  method-wiki/
  operations/
  agent-product/
```

Comando base:

```bash
python3 tools/create-source-project.py caminho/do/projeto --template youtube
```

## Responsabilidade Das Camadas

- `raw/`: matéria-prima original ou exportada.
- `library/`: índice navegável, notas geradas e unidades discretas.
- `distillations/`: leitura refinada por unidade.
- `promotions/`: decisões editoriais e justificativas.
- `method-wiki/`: conhecimento promovido como método.
- `operations/`: skills, workflows, playbooks e templates candidatos.
- `agent-product/`: material de produto apenas quando houver maturidade.

## Guardrails

- Não promova transcrição, PDF, artigo ou post bruto como conhecimento canônico.
- Não confunda biblioteca com destilação.
- Não confunda destilação com método.
- Não crie skill sem método claro.
- Não crie agente-produto por entusiasmo inicial.
- Não apague `raw/` quando a fonte for difícil de recuperar.
- Não duplique regras entre arquivos de instrução.

## Regras De Edição

- Escreva documentação em pt-BR com acentuação correta.
- Preserve identificadores estáveis em inglês quando forem usados por scripts, schemas ou nomes de pasta.
- Prefira mudanças pequenas e composáveis.
- Atualize `README.md`, `ARCHITECTURE.md` ou `ROADMAP.md` quando criar uma peça estrutural nova.
- Coloque templates em `templates/`, contratos em `schemas/`, frameworks em `frameworks/`, skills em `skills/` e scripts em `tools/`.

## Comandos Úteis

Criar projeto de fonte:

```bash
python3 tools/create-source-project.py ../meu-projeto --template book
```

Criar coleção editorial de livro:

```bash
python3 tools/create-book-collection.py ../books/budgeting --book-title "Budgeting" --target-agent accounting-ops
```

Gerar biblioteca de YouTube a partir de `yt-dlp`:

```bash
python3 tools/build-youtube-library.py --overwrite
```

Validar sintaxe de scripts sem gerar `__pycache__`:

```bash
python3 -c "import ast, pathlib; ast.parse(pathlib.Path('tools/create-source-project.py').read_text(encoding='utf-8'))"
```

## Git

- Não faça commit ou push sem pedido explícito do usuário.
- Antes de commitar, revise `git status -sb` e `git diff --stat`.
- Não stageie arquivos fora do escopo da tarefa.
- Mensagens de commit devem ser curtas e descritivas.

## Próxima Camada No Radar

O scaffold de agente-produto é importante, mas vem depois de projetos de fonte reais gerarem:

- destilações úteis
- promotion matrix preenchida
- método promovido
- caso de uso recorrente
