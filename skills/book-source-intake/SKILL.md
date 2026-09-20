---
name: book-source-intake
description: Use quando um livro ou conjunto de documentos precisa entrar em um projeto de fonte como matéria-prima e biblioteca navegável, antes de destilação ou promoção.
---

# Book Source Intake

Use esta skill para executar o intake técnico de livros com o extrator do
`book-to-skill` e preservar a separação entre fonte bruta, biblioteca,
destilação e promoção.

## Quando Usar

- Há um livro, PDF, EPUB, DOCX, Markdown ou conjunto de documentos para
  alimentar um agente.
- O projeto de fonte já existe ou precisa ser criado.
- É necessário extrair texto, metadados e capítulos detectados antes da leitura
  seletiva.

## Pré-requisito

Crie um projeto de fonte para livros quando ele ainda não existir:

```bash
python3 tools/create-source-project.py caminho/do/projeto --template book
```

O extrator do `book-to-skill` deve estar disponível. Neste ambiente:

```bash
export BOOK_TO_SKILL_ROOT=/home/lucas/Downloads/book-to-skill-master
```

Também é possível passar `--extractor-root` diretamente no comando.

## Comando

```bash
python3 tools/extract-book-source.py \
  caminho/do/projeto \
  caminho/do/livro.epub
```

Ou, sem variável de ambiente:

```bash
python3 tools/extract-book-source.py \
  caminho/do/projeto \
  caminho/do/livro.pdf \
  --extractor-root /home/lucas/Downloads/book-to-skill-master \
  --mode technical
```

O modo `technical` é indicado para código, tabelas, fórmulas e diagramas. O
modo `text` é suficiente para prosa com pouca estrutura técnica e é o padrão.

## Saída

```text
projeto/
  raw/
    full_text.txt
    metadata.json
  library/
    book-index.md
```

`metadata.json` preserva as métricas e fontes do extrator, com `output_text`
apontando para o arquivo persistido em `raw/`.

## Próxima Etapa

Depois do intake:

1. Abrir `library/book-index.md`.
2. Confirmar a unidade de trabalho e o agente-alvo.
3. Aplicar `book-distillation` a um capítulo ou seção.
4. Registrar a decisão na matriz de promoção.
5. Usar `book-to-method-wiki` somente quando o destino já estiver definido.

## Guardrails

- Não criar `SKILL.md` automaticamente.
- Não promover `raw/` ou `library/` como conhecimento canônico.
- Não ler o livro inteiro sem unidade e destino editorial.
- Não sobrescrever artefatos sem `--overwrite` explícito.
- Não instalar dependências sem escolher `--install-missing ask|yes`.
- Não escrever diretamente em `method-wiki/`, `operations/` ou
  `agent-product/`.
- Não apagar `raw/`; ele mantém a rastreabilidade da fonte.
