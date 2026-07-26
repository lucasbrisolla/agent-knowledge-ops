# `agent_creator`

Módulo interno para materializar uma especificação aprovada em uma arquitetura inicial de Agent Product.

## Papel

O módulo recebe uma especificação estruturada e cria uma casa operacional candidata. Ele não decide sozinho se um conhecimento merece virar agente e não inventa método de domínio.

## Interface

```text
create(specification, target)
validate(target)
```

Via CLI:

```bash
python3 tools/create-agent-product-from-spec.py \
  caminho/agent-product-spec.md \
  caminho/value-ops

python3 tools/validate-agent-product.py caminho/value-ops
```

## O Que É Gerado

- entrada (`AGENTS.md`, `CLAUDE.md` e `README.md`);
- contrato de dados;
- mapa de domínio e routing inicial;
- índice operacional;
- health check;
- estado inicial;
- esqueletos de método, workflows, skills, templates, contexto, exemplos, evals, scripts e archive.

O produto começa como `candidate`. O primeiro workflow, método de domínio e caso de avaliação devem ser preenchidos depois de existir um uso real.

## O Que Fica Fora

- conhecimento específico de domínio;
- contexto empresarial, pessoal ou de caso;
- runtime multiagente;
- dashboard, banco primário ou integrações externas;
- ativação automática do produto.

## Relação Com O `agent-knowledge-ops`

O `agent-knowledge-ops` interpreta o pedido, consulta seus frameworks, registra a decisão de promoção e chama este módulo. O `agent_creator` é a implementação da seam de materialização, não uma segunda refinaria de conhecimento.
