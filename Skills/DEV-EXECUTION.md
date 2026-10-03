# Skill: DEV Execution

Processo universal para executar uma demanda que já passou pelo gate QA. Esta é a versão legível por qualquer IA ou pessoa; a skill instalada no agente apenas operacionaliza estas regras.

## Pré-condição

Antes de alterar código, confirmar que existem demanda, critérios, CTs, validação QA preparada, links válidos e etapa indicando entrega ao DEV. Sem isso, devolver para QA/análise.

## Handoff entre etapas

Quando o gate QA estiver aprovado, o DEV assume automaticamente a demanda entregue. O usuário não precisa invocar outra skill manualmente. O DEV confirma o pacote, executa a sequência técnica e, após o code review, devolve o item para QA.

O handoff é determinado pelo estado e pelos artefatos, não por uma palavra-chave. O DEV nunca aprova CTs automaticamente; depois do code review, o próximo dono é QA.

## Procedimento

1. Ler demanda, plano de teste, CTs, validação, README, board e documentação técnica do repositório.
2. Copiar todos os arquivos de `Templates/Execução/` antes de adaptar a execução. Para bug, usar `Templates/Fix/`.
3. Registrar análise técnica, impacto, arquitetura, riscos, dependências e decisões.
4. Criar e congelar o plano de execução: arquivos, etapas, testes, documentação e fora de escopo.
5. Implementar apenas o escopo aprovado, respeitando os padrões do projeto.
6. Executar testes, build, lint, auditorias, smoke checks e auditoria documental quando aplicável.
7. Registrar arquivos, comandos, resultados, limitações e desvios em `03 - Implementação.md`.
8. Fazer code review cruzando card, critérios, plano, código, testes e documentação.
9. Atualizar execução, README, board DEV, status e links; entregar para QA executar os CTs.
10. Fechar somente após aprovação funcional do QA.

## Regras

- DEV decide como implementar; não altera silenciosamente o que o produto deve fazer.
- Mudança de regra, UX ou resultado esperado retorna para QA.
- Build verde não substitui a aprovação dos CTs.
- Falha de CT gera defeito ou ajuste vinculado, preservando o histórico da demanda pai.
- Toda mudança de comportamento ou responsabilidade deve atualizar o diagrama/fluxo pertinente.

## Artefatos esperados

Criar `03 Trabalho/DEV/<projeto>/Execuções/<ID>/` copiando `Templates/Execução/`:

- `00 README.md`
- `01 - Análise.md`
- `02 - Plano de execução.md`
- `03 - Implementação.md`
- `04 - Code review.md`

O DEV referencia os CTs existentes; não duplica os casos nem substitui a validação funcional do QA. O fluxo geral está em [[01 Board/Processos/Fluxo QA DEV|Fluxo QA → DEV]].
