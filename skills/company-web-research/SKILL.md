---
name: company-web-research
description: Use quando precisar pesquisar uma empresa, joint venture, controladora ou operação na web e transformar fontes públicas em contexto verificável, separando evidência direta, contexto de grupo, fonte secundária e hipótese.
---

# Company Web Research

Use esta skill para transformar pesquisa web stateless sobre empresas em contexto rastreável para intake editorial.

Ela é especialmente útil quando a empresa ainda não tem fonte local organizada e há risco de confundir operação, controladora, subsidiária, marca ou joint venture.

## Quando Usar

- A empresa ainda não tem `raw/`, `library/` ou `distillations/` bem montados.
- O usuário quer pesquisa pública rápida, mas com evidência verificável.
- Há risco de misturar fatos da empresa local com narrativa da controladora.
- O objetivo é alimentar `source-manifest.md`, `evidence-bundle.md` ou a primeira destilação.
- Há necessidade de mapear estrutura societária, produtos, mercados, plantas, governança ou contexto competitivo antes da leitura profunda.

## Não Usar Como

- substituto de destilação por unidade
- licença para inferir economics sem prova
- pesquisa ampla demais sem empresa ou recorte claro
- etapa final de promoção para `method-wiki` ou `operations`

## Fluxo

1. Definir a entidade exata a pesquisar.
2. Separar empresa-alvo, controladora, sócio relevante e marcas relacionadas.
3. Formular as perguntas editoriais centrais.
4. Priorizar fontes primárias ou quase primárias.
5. Registrar achados com URL, autoria, data e nota metodológica.
6. Classificar cada evidência por tipo.
7. Separar fatos confirmados, conflitos, lacunas e hipóteses.
8. Encerrar com recomendação do próximo documento ou fonte a ler.

## Perguntas-Padrão

Adapte estas perguntas ao caso:

- O que a empresa diz que faz de fato?
- Quais produtos, linhas, aplicações e mercados finais aparecem explicitamente?
- Quais plantas, regiões, unidades ou operações parecem relevantes?
- Quais sinais existem sobre clientes, canais, supply chain, insumos, capacidade ou produtividade?
- Como a estrutura societária é descrita?
- O que é fato local e o que é só contexto de grupo?
- Há indícios concretos de integração com controladora, sócios ou sistemas comuns?
- Quais lacunas impedem leitura econômica mais forte?

## Prioridade De Fontes

Prefira nesta ordem:

1. site oficial da empresa-alvo
2. páginas institucionais, de produtos, segmentos, plantas ou governança
3. releases, apresentações, relatórios e documentos oficiais
4. registros públicos, documentos regulatórios ou societários
5. páginas da controladora ou de sócios que mencionem explicitamente a empresa-alvo
6. catálogos, manuais, folders ou materiais comerciais
7. imprensa especializada e relatórios setoriais como apoio secundário

Se a fonte for secundária, trate como apoio e não como base única para conclusão importante.

## Classificação De Evidência

Classifique cada achado com um destes rótulos:

- `evidência direta da empresa`
- `evidência direta da controladora sobre a empresa`
- `evidência direta de sócio relevante sobre a empresa`
- `fonte secundária`
- `hipótese editorial`

Use `não confirmado` quando a informação não puder ser sustentada com fonte suficiente.

## Saída Mínima Esperada

- tabela de fontes com autoridade, frescor e relevância
- lista de achados verificáveis
- conflitos e lacunas
- hipóteses explicitamente marcadas
- próximo teste recomendado

Quando o usuário já estiver dentro de um projeto de fonte, a pesquisa deve deixar material pronto para:

- preencher `source-manifest.md`
- abrir ou atualizar `evidence-bundle.md`
- escolher a primeira unidade de leitura em `raw/` ou `library/`

## Guardrails

- Não tratar controladora como prova sobre subsidiária ou joint venture.
- Não confundir texto institucional vago com fato econômico.
- Não assumir participação acionária, planta, mercado ou cliente sem confirmação explícita.
- Não fechar tese de margem, caixa, pricing ou capital apenas com marketing institucional.
- Não esconder conflito entre fontes; registre o conflito.
- Não alongar a busca quando a próxima melhor ação já for ler um documento primário encontrado.

## Critério De Encerramento

Pare quando houver material suficiente para uma destas ações:

- preencher o `source-manifest.md` com boa precisão
- montar um `evidence-bundle.md` inicial
- definir a primeira destilação prioritária
- explicitar que a web aberta não basta e que será preciso fonte local ou documento fechado

## Handoff

Depois da pesquisa:

1. registrar a fonte mais importante no `source-manifest.md`
2. consolidar achados e lacunas no `evidence-bundle.md`
3. escolher a próxima unidade de leitura
4. só então avançar para destilação ou promoção
