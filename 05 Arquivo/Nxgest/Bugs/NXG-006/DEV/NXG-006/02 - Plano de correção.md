# 02 - Plano de correção (NXG-006)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Nxgest/Bugs/NXG-006/QA/NXG-006 CEP inválido não exibe mensagem/01 - Bug|NXG-006 — bug]]  
> **Análise:** [[01 - Análise]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Bugs/NXG-006/QA/NXG-006 CEP inválido não exibe mensagem/03 - Validação dev|Validação QA]]

## Resultado esperado

CEP com formato inválido exibe feedback claro e orienta o usuário a corrigir ou salvar sem CEP.

## Mudança planejada

- Ajustar o fluxo de validação do campo CEP para comunicar formato inválido no momento apropriado.
- Cobrir o comportamento com teste de UI.

## Fora de escopo

- Alterar a consulta de CEP válido.
- Bloquear o restante do cadastro.

## Pronto quando

- [ ] CT-B01 aprovado.
- [ ] Teste de UI atualizado.
- [ ] Code review aprovado.
