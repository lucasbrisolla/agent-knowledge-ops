# Especificação — Aprofundamento dos contratos da refinaria

**Status:** ready-for-agent

## Problem Statement

Como mantenedor do `agent-knowledge-ops`, quero que os fluxos de fonte e a
fábrica de Agent Products tenham contratos executáveis e coerentes, porque hoje
preciso conhecer detalhes diferentes de estrutura, caminhos, estados e campos
dependendo do adapter que estou usando.

O projeto já descreve uma refinaria com etapas claras — intake, library,
destilação, promoção, method-wiki, operações e produto — mas parte dessas
regras está espalhada entre scripts, skills, schemas e templates. O schema de
projeto de fonte define uma forma geral, enquanto coleção de livros, intake de
livros e biblioteca de YouTube materializam formas parcialmente diferentes. O
`agent_creator` já tem um seam útil em `ProductSpec`, mas campos, enums,
defaults e parsing ainda podem divergir entre o core, as CLIs e a documentação.

O resultado é perda de locality para quem mantém o código, menor leverage para
novos pipelines e testes que precisam conhecer detalhes de implementação para
verificar se um projeto foi materializado corretamente.

## Solution

Criar uma camada executável de contrato para o projeto de fonte e fazer os
fluxos de livro e YouTube usarem esse contrato. O módulo de projeto de fonte
será responsável por concentrar estrutura, invariantes, estados, perfis de
fonte, validação e separação entre matéria-prima, library, destilação e
promoção. Os scripts atuais permanecerão como adapters finos.

O fluxo de livros terá um perfil único que comporte tanto o índice editorial de
coleção quanto o intake técnico. O intake continuará preservando a extração
bruta, exigindo overwrite explícito e publicando artefatos somente depois de
uma execução bem-sucedida.

A biblioteca de YouTube será alinhada ao mesmo contrato, mantendo suas regras
de categoria, transcrição, notas e índice atrás de um módulo com mais depth.

Em paralelo, o `agent_creator` consolidará o contrato de `ProductSpec` para que
Markdown, CLI, validação e scaffold compartilhem campos, enums e defaults. O
seam existente do `agent_creator` será preservado; não haverá acoplamento entre
o creator de Agent Products e o projeto de fonte.

## User Stories

1. Como mantenedor, quero criar um projeto de fonte com uma estrutura previsível, para que qualquer pipeline consiga localizar suas camadas sem conhecimento específico do script.
2. Como mantenedor, quero validar um projeto de fonte antes de processá-lo, para que erros de estrutura sejam encontrados antes de artefatos serem gravados.
3. Como agente, quero receber mensagens de validação que expliquem a regra violada, para que consiga corrigir um projeto sem explorar a implementação.
4. Como mantenedor, quero que os estados permitidos de um projeto sejam verificáveis, para que o status editorial não vire texto arbitrário em cada fluxo.
5. Como mantenedor, quero que o contrato preserve a diferença entre `raw/`, `library/`, destilação e promoção, para que matéria-prima não seja confundida com conhecimento canônico.
6. Como responsável por uma fonte, quero escolher um perfil de livro, YouTube ou outro tipo suportado, para que a variação de unidade e cobertura fique explícita sem duplicar o projeto inteiro.
7. Como responsável por uma coleção de livros, quero manter um índice editorial por capítulo dentro do projeto de fonte, para que a seleção de leitura continue rastreável.
8. Como responsável por uma coleção de livros, quero que o índice registre status, destino provável e prioridade, para que a leitura seletiva não se transforme em releitura do livro inteiro.
9. Como responsável por um intake de livro, quero persistir texto e metadados em `raw/` e navegação em `library/`, para que a extração termine antes da destilação e da promoção.
10. Como responsável por um intake de livro, quero que uma falha do extrator não deixe artefatos parciais, para que o projeto continue confiável e recuperável.
11. Como responsável por um intake de livro, quero exigir overwrite explícito, para que uma nova extração não destrua matéria-prima ou decisões já existentes sem intenção clara.
12. Como responsável por uma biblioteca de YouTube, quero transformar metadados e legendas em notas navegáveis dentro do projeto de fonte, para que a biblioteca respeite o mesmo contrato das demais fontes.
13. Como responsável por uma biblioteca de YouTube, quero preservar arquivos brutos e indicar vídeos sem transcrição, para que a ausência de dados seja visível e não pareça cobertura completa.
14. Como responsável por uma biblioteca de YouTube, quero configurar categorias sem editar o código, para que a taxonomia possa evoluir com o domínio da fonte.
15. Como responsável por uma biblioteca de YouTube, quero que parsing de SRT, slugs e renderização fiquem escondidos atrás do módulo da biblioteca, para que callers aprendam uma interface pequena.
16. Como mantenedor, quero que o pipeline de YouTube não dependa implicitamente da pasta corrente, para que ele possa operar em qualquer projeto de fonte válido.
17. Como responsável pela criação de um Agent Product, quero que a especificação Markdown e a CLI aceitem o mesmo conjunto de campos e valores, para que a forma de entrada não altere o scaffold produzido.
18. Como responsável pela validação de um Agent Product, quero que campos obrigatórios, enums e defaults tenham uma única fonte de verdade, para que mudanças de contrato não criem divergências silenciosas.
19. Como mantenedor, quero preservar os adapters legados do `agent_creator`, para que usuários existentes possam migrar sem perder seus comandos.
20. Como mantenedor, quero testar o comportamento observável pelo seam mais alto disponível, para que os testes verifiquem contratos e não detalhes internos de parsing, templates ou filesystem.
21. Como mantenedor, quero que cada fluxo possa ser verificado isoladamente, para que uma falha em livro não esconda uma regressão em YouTube ou em Agent Products.
22. Como agente executor, quero encontrar uma spec e tickets com dependências explícitas, para que eu possa trabalhar primeiro na frontier desbloqueada sem adivinhar a ordem arquitetural.
23. Como mantenedor, quero que a documentação operacional aponte para o contrato executável, para que skills e schemas não prescrevam estruturas que os scripts não conseguem validar.
24. Como mantenedor, quero executar a suíte completa ao final da migração, para que o aprofundamento aumente locality sem quebrar os adapters existentes.

## Implementation Decisions

- O principal seam será o contrato executável de projeto de fonte. Ele será o ponto mais alto comum aos fluxos de criação, validação e materialização de bibliotecas.
- O módulo de projeto de fonte terá profundidade suficiente para esconder caminhos, invariantes de estrutura, estados permitidos, perfis e regras de separação editorial.
- Os scripts de linha de comando continuarão sendo adapters. Eles traduzirão argumentos, chamarão o módulo e apresentarão erros e resultados ao usuário.
- O perfil de livro será a forma canônica para combinar índice editorial, matéria-prima e biblioteca. A coleção editorial não deverá continuar como uma segunda forma estrutural sem relação explícita com o projeto de fonte.
- O perfil de YouTube produzirá sua biblioteca dentro do contrato do projeto de fonte. A política de categorias, transcrição ausente, nomes de arquivo e índice permanecerá interna ao módulo da biblioteca.
- O intake de livros manterá a integração com o extrator externo como um adapter de processo. O diretório temporário, a validação do resultado, a proteção contra overwrite e a materialização final serão tratados como uma operação transacional.
- O `agent_creator` manterá o seam existente de `ProductSpec`, mas será a fonte executável única para campos, enums, defaults e normalização. O schema Markdown continuará documentando o contrato, sem criar uma segunda regra executável.
- A compatibilidade das CLIs legadas será preservada durante a migração. A remoção de caminhos antigos só poderá acontecer depois que todos os callers estiverem cobertos pelos testes de contrato.
- As diferenças entre perfis serão expressas como variações de política e cobertura, não como cópias independentes de todo o scaffold.
- O trabalho será implementado em expand–contract: primeiro o contrato e a validação, depois a migração dos pipelines, e por fim a contração de estruturas paralelas quando não houver mais callers.
- Nenhuma decisão de promoção será automatizada por esta mudança. O contrato organiza rastreabilidade; não transforma `raw/` ou `library/` em method-wiki, operação ou Agent Product.

## Testing Decisions

- Os testes devem observar comportamento externo: estrutura criada, arquivos produzidos, estados aceitos ou rejeitados, mensagens de erro, preservação de dados e ausência de efeitos fora do escopo.
- O seam mais alto preferido será a operação de cada pipeline sobre um projeto temporário completo. Testes internos só serão adicionados quando uma regra determinística não puder ser coberta de forma clara pelo contrato.
- O contrato de projeto de fonte terá testes para criação, validação de estrutura, manifest, promotion matrix, estados, perfis e separação entre camadas.
- O perfil de livro terá testes para índice editorial, unidade por capítulo, destinos, status e coexistência com os artefatos de intake.
- O intake de livros terá testes de sucesso, falha do extrator, ausência de artefatos esperados, overwrite e preservação contra resultados parciais, seguindo o extrator falso já usado no repositório.
- A biblioteca de YouTube terá testes para metadados válidos, legenda ausente, parsing de SRT, regras de categoria, índice, caminhos do projeto e política de sobrescrita.
- O `agent_creator` terá testes de paridade entre especificação Markdown, CLI, validação e scaffold, incluindo valores aceitos pelo core que anteriormente não eram expostos pela CLI.
- A suíte existente de criação de projeto de fonte, coleção de livros, Agent Product e intake de livros será preservada e ampliada, não substituída por testes acoplados a funções privadas.
- A verificação final incluirá a suíte completa, checagem de sintaxe dos scripts, `git diff --check` e inspeção de que nenhum fluxo escreve diretamente em destinos de promoção sem decisão editorial.

## Out of Scope

- Criar um runtime de agentes, dashboard ou banco de dados.
- Transformar o repositório em um pacote instalável ou implementar a CLI `ako` completa.
- Criar um pipeline end-to-end de destilação e promoção de livros ou vídeos.
- Promover automaticamente qualquer conteúdo para method-wiki, operations ou agent-product.
- Reescrever o extrator externo de livros ou copiar seus parsers para o repositório.
- Adicionar novos tipos de fonte além dos perfis necessários para validar o contrato.
- Escolher ou alterar o domínio de um Agent Product real.
- Remover adapters legados antes da conclusão da migração e da verificação integradora.
- Criar `CONTEXT.md` ou ADR apenas por causa desta iniciativa; esses documentos devem nascer quando uma decisão de domínio ou arquitetura exigir registro permanente.

## Further Notes

- A recomendação principal da revisão arquitetural é começar pelo contrato de projeto de fonte, porque ele oferece leverage para os fluxos de livros e YouTube e corresponde ao próximo melhor passo já registrado no backlog.
- O aprofundamento do `agent_creator` é independente e especulativo. Ele deve permanecer com prioridade menor se o contrato atual não estiver mudando com frequência.
- Não há `CONTEXT.md` nem `docs/adr/` no snapshot analisado. A linguagem desta spec segue `AGENTS.md`, `ARCHITECTURE.md`, `FRAMEWORK.md`, o schema de projeto de fonte e o backlog.
- O worktree já continha mudanças locais relacionadas ao intake de livros, specs e testes. Elas devem ser preservadas e incorporadas à validação, sem serem sobrescritas.
