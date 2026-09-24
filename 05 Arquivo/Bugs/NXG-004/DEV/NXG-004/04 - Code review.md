# 04 - Code review (NXG-004)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Bugs/NXG-004/QA/NXG-004 CEP preenchido não permite salvar/01 - Bug|NXG-004 — bug]]  
> **Plano:** [[02 - Plano de correção]]  
> **Implementação:** [[03 - Implementação]]  
> **Validação QA:** [[05 Arquivo/Bugs/NXG-004/QA/NXG-004 CEP preenchido não permite salvar/03 - Validação dev|Validação QA]]

**Estado:** ✅ aprovado

## Checklist

- [x] Diff limitado ao escopo do fix.
- [x] Causa e regressão cobertas.
- [x] Gates aplicáveis verdes.
- [x] CTs QA cobertos.

## Parecer

A correção é mínima e atende ao defeito: a regex passou a validar oito dígitos numéricos, sem alterar a consulta do CEP, a localização aproximada ou a regra de campo opcional.

**Testes:** `npm test -- --run` — 46 arquivos e 212 testes aprovados.
