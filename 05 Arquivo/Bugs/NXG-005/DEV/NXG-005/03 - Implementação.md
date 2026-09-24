# 03 - Implementação (NXG-005)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Bugs/NXG-005/QA/NXG-005 Remover CEP salvo/01 - Bug|NXG-005 — bug]]  
> **Plano:** [[02 - Plano de correção]]  
> **Code review:** [[04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Bugs/NXG-005/QA/NXG-005 Remover CEP salvo/03 - Validação dev|Validação QA]]

## Rodada 1 — ✅ concluída

O payload de edição agora envia `null` quando o CEP é removido, permitindo que o backend limpe o valor persistido e a localização derivada.

## Testes

- [x] Teste de remoção de CEP na edição.
- [x] Regressão dos fluxos de cliente.

Comando: `npx vitest run frontend/src/modules/cliente/components/ClienteForm.test.tsx`
