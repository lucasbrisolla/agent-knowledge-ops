# Módulo `agent-creator` Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Criar o módulo interno `agent_creator` para transformar uma especificação aprovada em uma arquitetura inicial de Agent Product, com validação de contrato e compatibilidade com a CLI existente.

**Architecture:** O pacote `agent_creator` será dono da implementação, dos templates genéricos e do schema de produto. Os scripts atuais em `tools/` permanecerão como adapters compatíveis. O `agent-knowledge-ops` continuará responsável por interpretar escopo, registrar decisão de promoção e chamar o módulo.

**Tech Stack:** Python 3, `unittest`, Markdown com frontmatter YAML, templates textuais e filesystem local.

---

### Task 1: Definir a interface estruturada com testes falhando

**Files:**
- Create: `tests/test_agent_creator.py`
- Modify: `tests/test_create_agent_product.py`

- [ ] **Step 1: Escrever o teste de criação a partir de uma especificação Markdown**

O teste deve criar um arquivo `agent-product-spec.md` temporário com frontmatter válido, chamar `create_from_spec(spec_path, target_path)` e verificar `README.md`, `domain.md`, `DATA_CONTRACT.md`, `HEALTH_CHECK.md`, `states.yml` e os diretórios mínimos.

- [ ] **Step 2: Escrever o teste de validação de enums e campos editoriais**

O teste deve provar que `recommended_form: "forma-inexistente"` e valores `[definir]` em campos obrigatórios retornam erro explícito.

- [ ] **Step 3: Escrever o teste de preservação com `force`**

O teste deve criar um `README.md` pré-existente, executar a criação com `force=True` e confirmar que o conteúdo original permanece intacto.

- [ ] **Step 4: Rodar apenas os testes novos e confirmar RED**

Run: `python3 -m unittest tests.test_agent_creator -v`

Expected: falha porque o pacote `agent_creator` e `create_from_spec` ainda não existem.

### Task 2: Extrair a implementação genérica para `agent_creator`

**Files:**
- Create: `agent_creator/__init__.py`
- Create: `agent_creator/core.py`
- Create: `agent_creator/templates/`
- Create: `agent_creator/schemas/agent-product.schema.md`
- Modify: `tools/agent_product.py`
- Modify: `tools/create-agent-product.py`
- Modify: `tools/validate-agent-product.py`

- [ ] **Step 1: Mover os templates genéricos de agente-produto para `agent_creator/templates/`**

Mover somente os arquivos `agent-product-*.md` e `agent-product-states.yml` que hoje vivem em `templates/`. Os templates de source projects, livros, evidence bundles e YouTube permanecem no `agent-knowledge-ops`.

- [ ] **Step 2: Implementar `ProductSpec` e o parser de frontmatter**

Criar uma interface sem dependências externas:

```python
def load_spec(path: Path) -> ProductSpec: ...
def create_from_spec(spec_path: Path, project: Path, force: bool = False) -> None: ...
def validate_product(project: Path) -> tuple[list[str], list[str]]: ...
```

O parser deve aceitar o frontmatter YAML simples já usado pelo schema, sem introduzir uma dependência YAML para o v1. Campos desconhecidos podem gerar aviso; campos obrigatórios ausentes e enums inválidos devem gerar erro.

- [ ] **Step 3: Fazer o core usar os templates do módulo**

`template_root()` deve apontar para `agent_creator/templates`, deixando o módulo autocontido e eliminando a dependência da pasta genérica de templates do agente de conhecimento.

- [ ] **Step 4: Implementar validação de contrato**

Validar os valores permitidos para `state_needed`, `verification_needed`, `recommended_form` e `status`, rejeitar `[definir]` nos campos mínimos e manter avisos para status diferente de `candidate`.

- [ ] **Step 5: Rodar os testes novos e confirmar GREEN**

Run: `python3 -m unittest tests.test_agent_creator -v`

Expected: todos os testes novos passam.

### Task 3: Gerar a arquitetura inicial e manter compatibilidade

**Files:**
- Modify: `agent_creator/core.py`
- Modify: `tools/create-agent-product.py`
- Modify: `tools/validate-agent-product.py`
- Modify: `tests/test_create_agent_product.py`

- [ ] **Step 1: Gerar `domain.md` com routing inicial baseado na especificação**

O conteúdo deve usar domínio, usuário, uso recorrente e output repetido, mas manter uma seção explícita de decisões pendentes. Não criar workflows de domínio automaticamente.

- [ ] **Step 2: Gerar `DATA_CONTRACT.md` e `HEALTH_CHECK.md` específicos do produto**

Os arquivos devem carregar o nome, o domínio, a fonte-base, o tipo de estado e a necessidade de verificação da especificação, preservando a separação entre camada de sistema, contexto e ingestão.

- [ ] **Step 3: Fazer a CLI legada delegar ao core**

`tools/create-agent-product.py` deve continuar aceitando os mesmos argumentos, montar um `ProductSpec` e chamar `create_product`/`create_from_spec` no pacote novo. `tools/validate-agent-product.py` deve delegar ao validador novo.

- [ ] **Step 4: Rodar a suíte existente e confirmar compatibilidade**

Run: `python3 -m unittest discover -s tests -p 'test*.py' -v`

Expected: os testes existentes e os novos passam sem alterar o contrato observado pela CLI.

### Task 4: Documentar o módulo e integrá-lo ao fluxo do agente

**Files:**
- Create: `agent_creator/README.md`
- Create: `agent_creator/ARCHITECTURE.md`
- Create: `agent_creator/FRAMEWORK.md`
- Create: `skills/agent-product-creation/SKILL.md`
- Modify: `skills/agent-product-scaffold/SKILL.md`
- Modify: `README.md`
- Modify: `ARCHITECTURE.md`
- Modify: `FRAMEWORK.md`
- Modify: `AGENTS.md`
- Modify: `ROADMAP.md`

- [ ] **Step 1: Documentar a interface e a fronteira do `agent_creator`**

Explicar que o módulo materializa uma especificação aprovada, não decide sozinho a promoção nem inventa conhecimento de domínio.

- [ ] **Step 2: Criar a skill de orquestração `agent-product-creation`**

Definir o fluxo para pedidos como “crie o value-ops”: interpretar escopo, consultar o framework, preencher especificação, chamar o creator, revisar arquitetura inicial, validar e manter `candidate`.

- [ ] **Step 3: Reduzir `agent-product-scaffold` ao papel de adapter**

Fazer a skill existente apontar para o módulo interno e preservar sua função de compatibilidade, sem duplicar regras de criação.

- [ ] **Step 4: Atualizar a documentação do produto**

Adicionar o módulo ao mapa arquitetural e ao fluxo de saída, deixando explícito que padrões arquiteturais futuros serão promovidos pelo `agent-knowledge-ops` e consumidos pelo creator.

- [ ] **Step 5: Rodar a suíte completa e validar a árvore gerada**

Run: `python3 -m unittest discover -s tests -p 'test*.py' -v`

Expected: todos os testes passam; nenhum arquivo gerado contém `{{...}}` ou `[definir]` nos campos obrigatórios.

### Task 5: Revisar diff e preparar handoff

**Files:**
- Review: `git diff --stat`
- Review: `git diff --check`
- Review: todos os arquivos modificados no worktree

- [ ] **Step 1: Fazer revisão de escopo**

Confirmar que mudanças de source intake, destilação e schemas não relacionados ficaram fora da implementação.

- [ ] **Step 2: Executar verificação final**

Run: `python3 -m unittest discover -s tests -p 'test*.py' -v && git diff --check`

Expected: suíte verde e nenhuma falha de whitespace.

- [ ] **Step 3: Não fazer commit sem pedido explícito**

Entregar o worktree, os testes executados e a lista de arquivos alterados para revisão do usuário.
