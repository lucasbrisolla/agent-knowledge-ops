# Roadmap

Ideias e próximos módulos para o `agent-knowledge-ops`.

## Princípio

O roadmap guarda possibilidades sem confundir o núcleo do framework.

Uma ideia só deve virar framework, skill ou ferramenta quando tiver:

- fonte recorrente
- saída clara
- valor para um agente
- contrato reaproveitável

## Módulos Em Aberto

| Módulo | Status | Ideia |
|---|---|---|
| `source-project-setup` | iniciado | Criar estrutura padrão para organizar fontes grandes |
| `youtube-channel-intake` | iniciado | Criar bibliotecas locais de canais e playlists |
| `book-distillation` | iniciado | Destilar livros por capítulo para conhecimento de agente |
| `book-collection-setup` | iniciado | Criar README editorial e índice de livros no padrão `books/` |
| `book-to-method-wiki` | iniciado | Promover capítulos de livros para `_method-wiki` com baixo risco de erro |
| `knowledge-synthesis` | iniciado | Sintetizar evidências de múltiplas fontes antes da promoção |
| `social-signal-research` | planejado | Transformar Reddit, HN, X, YouTube e comunidades em sinais |
| `web-article-intake` | planejado | Capturar sites e artigos como unidades rastreáveis |
| `earnings-call-intelligence` | ideia registrada | Analisar transcrições de resultados de companhias abertas |
| `agent-product-scaffold` | no radar | Gerar repositório padrão de um agente-produto |

## Earnings Call Intelligence

Ideia registrada para explorar depois.

Objetivo:

Transformar transcrições de resultados, conference calls, releases e apresentações de companhias abertas em inteligência operacional para agentes.

Possíveis perguntas:

- Quais tendências aparecem em várias empresas do mesmo setor?
- O que empresas líderes estão fazendo sobre margem, eficiência, IA, capex, pricing ou caixa?
- Quais riscos estão ficando recorrentes?
- Como a linguagem da gestão mudou ao longo dos trimestres?
- Quais práticas parecem estar se espalhando entre pares?
- Que sinais antecipam mudança de estratégia, ciclo ou pressão competitiva?

Possíveis saídas:

- índice por empresa, trimestre e setor
- destilação por call
- matriz de tendências
- comparação entre pares
- warnings setoriais
- método de análise de resultado
- skill de leitura de earnings call

## Projeto De Fonte

Primeiro pacote operacional para organizar fontes grandes.

```text
project/
  README.md
  source-manifest.md
  raw/
  library/
  distillations/
  promotions/
  method-wiki/
  operations/
  agent-product/
```

Status:

- framework criado
- schema criado
- templates criados
- skill criada
- ferramenta `create-source-project.py` criada

## Knowledge Synthesis

Pacote para aumentar rigor entre destilação e promoção.

Status:

- `knowledge-synthesis-framework.md` criado
- `source-priority-framework.md` criado
- `evidence-bundle.schema.md` criado
- `evidence-bundle.md` criado
- exemplo multissource criado

## Agente-Produto

Manter no radar, mas não implementar antes de validar bem o ciclo de projeto de fonte.

Critério para avançar:

- pelo menos um projeto de fonte com destilações reais
- pelo menos uma promotion matrix preenchida
- pelo menos um método promovido
- caso de uso recorrente claro
