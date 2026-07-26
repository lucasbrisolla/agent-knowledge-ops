# Framework De Criação Inicial De Agent Products

Use este módulo quando já existir uma especificação aprovada ou quando o `agent-knowledge-ops` tiver registrado uma decisão de productização.

## Perguntas Mínimas

- Qual é o papel e a fronteira do agente?
- Quem é o usuário principal?
- Qual uso recorrente justifica a casa própria?
- Qual output precisa sobreviver à conversa?
- Qual é a fonte viva?
- Há estado ou lifecycle?
- Que verificação responde à dor atual?

## Regra De Forma

O creator materializa apenas a forma escolhida. Ele não sobe automaticamente de skill para operador, sistema de domínio ou plataforma multi-superfície.

```text
nota
→ method-wiki
→ skill/workflow
→ assistente leve
→ operador estruturado
→ sistema de domínio
→ plataforma local-first
```

## Arquitetura Inicial

Para um produto candidato, a arquitetura deve começar com:

- superfície de entrada;
- fonte viva e contrato de dados;
- mapa de domínio e routing;
- estado declarado;
- health check;
- diretórios vazios com propósito explícito;
- status `candidate`.

Método, workflow, skill, template e eval entram somente quando houver caso de uso suficiente para justificar o conteúdo.

## Conhecimento Arquitetural Futuro

Frameworks, posts, grafos e outras fontes sobre arquitetura de agentes devem passar pelo `agent-knowledge-ops` para biblioteca, destilação, síntese e promoção. O resultado promovido poderá alimentar perfis e templates deste módulo depois de revisão e avaliação.
