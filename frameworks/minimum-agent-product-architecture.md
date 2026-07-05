# Minimum Agent Product Architecture

Usar quando uma base de conhecimento ou método começa a pedir forma operacional própria.

## Pergunta Central

A pergunta não é apenas:

> Isso já virou um agent product de verdade?

A pergunta completa é:

> Este conhecimento pede qual forma operacional agora: nota, method-wiki, skill, workflow, operador estruturado, sistema de domínio ou plataforma?

O objetivo é impedir dois erros simétricos:

- promover conhecimento cedo demais para agente-produto
- manter conhecimento maduro como nota solta quando ele já pede operação repetível

## Escada De Forma Operacional

### 0. Nota / Knowledge Base

Use quando:

- o conhecimento ainda é referência passiva
- não há uso recorrente claro
- não há output repetido
- não há estado vivo

Pacote mínimo:

- nota bem nomeada
- fonte rastreável
- tags ou links suficientes

Não criar agente.

### 1. Method-Wiki

Use quando:

- há método, conceito, heurística, checklist ou padrão reutilizável
- o conhecimento melhora julgamento em mais de um caso
- ainda não há sequência operacional fechada

Pacote mínimo:

- entrada em `_method-wiki/` ou camada equivalente
- links para fontes/destilações
- exemplos ou sinais de uso

Não criar skill ainda se o método não disser claramente quando e como agir.

### 2. Skill / Workflow

Use quando:

- há uma tarefa repetível
- existe gatilho claro de uso
- o agente precisa seguir passos, não apenas conhecer conceito
- a saída esperada é definida

Escolha:

- `skill`: capacidade delimitada e reutilizável em vários contextos
- `workflow`: sequência operacional de um produto/contexto específico

Pacote mínimo:

- propósito
- quando usar
- entradas
- passos
- saída esperada
- persistência, se houver
- verificação mínima

### 3. Assistente Leve

Use quando:

- há uma superfície própria de conversa/uso
- a persistência é baixa
- a saída é majoritariamente textual
- o risco operacional é pequeno

Pacote mínimo:

- `README.md`
- `AGENTS.md` ou equivalente
- fonte viva explicitada
- outputs esperados

### 4. Operador Estruturado

Use quando:

- produz artefatos recorrentes
- mexe em fontes vivas
- tem fluxo repetível
- exige verificação mínima

Pacote mínimo:

- tudo do Assistente Leve
- `DATA_CONTRACT.md`
- templates
- exemplos calibradores
- outputs canônicos
- `doctor` ou checklist de setup
- `verify` quando houver artefato validável

### 5. Sistema Operacional De Domínio

Use quando:

- há múltiplas fontes vivas
- existe risco de drift
- há estados ou ciclo de vida
- outputs intermediários alimentam fontes canônicas
- `doctor`, `verify`, `sync-check` e liveness/frescor podem ser perguntas diferentes

Pacote mínimo:

- tudo do Operador Estruturado
- estados canônicos, se houver lifecycle
- pipeline/inbox, se houver fila real
- artifact additions quando fonte consolidada for sensível
- merge/normalize/dedup quando houver regra objetiva
- `HEALTH_CHECK.md` quando o operador precisar diagnosticar saúde do sistema

### 6. Plataforma Local-First / Multi-superfície

Use somente quando:

- o produto já tem fonte canônica estável
- múltiplas superfícies precisam operar sobre a mesma fonte: CLI, scripts, dashboard, Web UI, plugins ou índices derivados
- há dor real de navegação, consulta, integração ou visualização

Pacote mínimo:

- tudo do Sistema Operacional De Domínio que ainda se aplica
- fonte canônica única declarada
- regra explícita para índices derivados e caches
- UI/dashboard/plugin escrevendo pelo contrato existente
- credenciais, toggles e integrações em camada de usuário
- fallback operacional sem superfície visual ou plugin

## Matriz De Decisão Rápida

| Sinal observado | Forma provável | Não fazer ainda |
|---|---|---|
| Ideia útil, sem uso recorrente | Nota / Knowledge Base | Skill |
| Método reaproveitável, sem sequência fechada | Method-Wiki | Agent product |
| Tarefa repetível com gatilho claro | Skill ou workflow | Produto completo |
| Conversa especializada, pouco estado | Assistente Leve | Pipeline pesado |
| Artefatos recorrentes e fonte viva | Operador Estruturado | Web UI |
| Estados, drift, consolidação e verificação viva | Sistema De Domínio | Plugin system genérico |
| Múltiplas superfícies sobre fonte estável | Plataforma Local-First | Banco primário paralelo |

## Perguntas De Promoção

Antes de criar agente-produto, responda:

1. Qual uso recorrente já apareceu?
2. Qual output se repete?
3. Qual fonte viva precisa sobreviver à conversa?
4. Existe estado ou lifecycle?
5. O que pode quebrar e como verificar?
6. Existe diferença entre setup, validade do output, sincronização interna e frescor externo?
7. O produto precisa de personalização viva?
8. O conhecimento já tem método suficiente ou ainda é só referência?
9. Uma skill/workflow resolveria antes de criar um produto inteiro?
10. Há alguma superfície além do Markdown que realmente reduziria carga cognitiva?

## Blocos Possíveis Por Tipo

| Bloco | Nota | Method-Wiki | Skill/Workflow | Assistente | Operador | Sistema | Plataforma |
|---|---|---|---|---|---|---|---|
| Fonte rastreável | sim | sim | sim | sim | sim | sim | sim |
| README | não | opcional | opcional | sim | sim | sim | sim |
| AGENTS/CLAUDE | não | não | opcional | sim | sim | sim | sim |
| DATA_CONTRACT | não | não | não | opcional | sim | sim | sim |
| Templates | não | opcional | sim | opcional | sim | sim | sim |
| Estados | não | não | opcional | raro | depende | comum | comum |
| Doctor | não | não | raro | opcional | sim | sim | sim |
| Verify | não | opcional | sim | opcional | sim | sim | sim |
| Sync-check | não | raro | raro | raro | depende | sim | sim |
| Additions/merge | não | não | raro | raro | depende | comum | comum |
| UI/dashboard/plugin | não | não | não | não | não | raro | sim |

## Resultado Da Avaliação

Use um destes resultados:

- `não promover`
- `manter como knowledge base`
- `promover para method-wiki`
- `criar skill`
- `criar workflow em produto existente`
- `criar assistente leve`
- `criar operador estruturado`
- `criar sistema operacional de domínio`
- `criar plataforma local-first / multi-superfície`
- `aguardar uso real`

## Regra De Corte

Criar a menor forma operacional que resolva a dor atual.

Ordem preferida:

```text
nota
-> method-wiki
-> skill/workflow
-> assistente leve
-> operador estruturado
-> sistema de domínio
-> plataforma multi-superfície
```

Subir um nível só quando o nível anterior estiver gerando fricção real.

## Anti-Overengineering

Não criar agente-produto quando:

- só existe entusiasmo com a fonte
- a saída ainda é resumo bonito
- não há uso recorrente
- o método ainda não foi usado em situação real
- não há artifact que precise sobreviver à conversa
- uma skill resolveria
- o produto exigiria mais manutenção que benefício

Não criar plataforma quando:

- não há fonte canônica estável
- UI seria a primeira fonte de verdade
- plugin/integrador resolveria uma dor pontual
- banco ou índice viraria store paralelo sem necessidade

## Próximo Passo Quando A Decisão For Positiva

- Para `method-wiki`: escrever ou atualizar a entrada existente e linkar fontes.
- Para `skill`: criar `SKILL.md` com gatilho, entradas, procedimento, saída e verificação.
- Para `workflow`: criar sequência operacional no produto de destino.
- Para `operador` ou `sistema`: criar primeiro `DATA_CONTRACT.md`, outputs canônicos e verificação mínima.
- Para `plataforma`: documentar fonte canônica, índice derivado, integração opt-in e fallback sem UI/plugin.
