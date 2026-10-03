# Skill: QA First Delivery

Processo universal para organizar uma ideia, melhoria ou bug antes do desenvolvimento. Esta é a versão legível por qualquer IA ou pessoa; a skill instalada no agente apenas operacionaliza estas regras.

## Objetivo

Garantir que o DEV receba um contrato funcional claro:

`demanda → critérios → casos de teste → matriz de cobertura → validação do pacote → handoff`

## Procedimento

1. Identificar o projeto, o vault, o board QA e os templates oficiais.
2. Classificar a entrada como melhoria, bug ou defeito filho.
3. Gerar ou preservar um ID estável.
4. Copiar os templates oficiais antes de adaptar qualquer conteúdo. Nunca reconstruir o pacote manualmente quando houver template.
5. Preencher contexto, objetivo, fora de escopo, riscos, dependências e critérios `C1..Cn` observáveis.
6. Criar os CTs no formato oficial, com callout, âncora única, pré-condições, Dado/Quando/Então, resultado, pós-condição, tipo, camada, automação e execução.
7. Cruzar a cobertura: todo critério deve ter CT e todo CT deve apontar para critério. Avaliar sucesso, bordas, validações, erros e regressão.
8. Preparar a nota de validação com um resultado para cada CT. Qase, quando usado, deve manter os mesmos IDs.
9. Auditar arquivos, frontmatter, headings, âncoras, links internos e placeholders.
10. Atualizar README, board, roadmap e etapa/status.

## Gate para DEV

O handoff só ocorre quando:

- o pacote oficial está completo;
- os critérios são testáveis;
- todos os critérios e CTs estão cruzados;
- links e âncoras resolvem;
- não há placeholder ou pendência bloqueante;
- a demanda está marcada como pronta para DEV.

Se a descoberta mudar o objetivo ou o comportamento esperado, ela retorna para QA como complemento ou nova demanda vinculada. Não existe escopo rasteiro silencioso.

## Artefatos esperados

Para melhoria, usar o pacote de `Templates/QA/` e `Templates/Melhoria/`, conforme a convenção do projeto:

- `00 README.md`
- `01 - Demanda.md`
- `02 - Plano de teste.md`
- `03 - Casos de teste.md`
- `04 - Validação dev.md`
- `05 - Preparação Qase.md`, quando aplicável

Detalhes do formato de CT ficam em [[Skills/CASOS-DE-TESTE|Casos de teste]] e o ciclo de melhoria em [[Skills/MELHORIA|Melhoria]].
