# 03 - Implementação (NXG-006)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Bugs/NXG-006/QA/NXG-006 CEP inválido não exibe mensagem/01 - Bug|NXG-006 — bug]]  
> **Plano:** [[02 - Plano de correção]]  
> **Code review:** [[04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Bugs/NXG-006/QA/NXG-006 CEP inválido não exibe mensagem/03 - Validação dev|Validação QA]]

## Rodada 1 — ✅ concluída

O campo CEP agora informa formato inválido ao perder o foco, sem interromper a digitação. O parser também reconhece `erro: true` e `erro: "true"` na resposta do ViaCEP.

## Testes

- [x] Teste de feedback para CEP inválido.
- [x] Regressão do formulário de cliente.

Comando: `npx vitest run frontend/src/modules/cliente/components/ClienteForm.test.tsx`

Validação do parser: `npx vitest run frontend/src/shared/utils/cep.test.ts` — 4 testes aprovados.
