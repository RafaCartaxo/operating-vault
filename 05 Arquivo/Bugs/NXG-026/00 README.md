---
status: feito
card: "NXG-026"
plano_repo: ""
commit: "8454392"
---
# NXG-026 — Fix (CPF e telefone recebem foco no erro)

> Quando o cliente tem CPF ou telefone inválido, salvar não leva a tela até o campo com erro. Este fix dá ao formulário a referência que falta para ele focar.

> Pasta do fix: QA (bug, casos e validação) + DEV (análise, plano, execução e review).

## Links

- Bug: [[05 Arquivo/Bugs/NXG-026/QA/01 - Bug|01 - Bug]]
- Casos de teste: [[05 Arquivo/Bugs/NXG-026/QA/02 - Casos de teste|02 - Casos de teste]]
- Validação: [[05 Arquivo/Bugs/NXG-026/QA/03 - Validação|03 - Validação]]
- Análise: [[05 Arquivo/Bugs/NXG-026/DEV/01 - Análise|01 - Análise]]
- Plano: [[05 Arquivo/Bugs/NXG-026/DEV/02 - Plano de execução|02 - Plano de execução]]
- Implementação: [[05 Arquivo/Bugs/NXG-026/DEV/03 - Implementação|03 - Implementação]]
- Review: [[05 Arquivo/Bugs/NXG-026/DEV/04 - Code review|04 - Code review]]

## Status

| Etapa | Estado | Data |
|---|---|---|
| Análise (causa) | ✅ confirmada | 29/08 |
| Plano | ✅ pronto | 29/08 |
| Execução | ✅ Rodada 1 (código + regressão + gates) | 29/08 |
| Code review | ✅ aprovado (sem achados) | 29/08 |
| Verificação (CTs) | ✅ B01..B04 (automatizado + manual do dono) | 29/08 |
| Fechamento | ✅ commit `8454392` (local, sem push) | 29/08 |

## Histórico

- 29/08 — pasta criada (reestruturação de `NXG-026 FIX…md` em pasta por card); causa confirmada no repo; plano pronto.
- 29/08 — reescrita de legibilidade (padrão do template de Bug: frase humana, separadores, glossário).
- 29/08 — **Rodada 1 executada**: fix aplicado + regressão (controle negativo ok) + gates verdes (`tsc` 0, 197 testes, audits, build).
- 29/08 — **Code review aprovado** + CTs manuais validados pelo dono.
- 29/08 — **Commit `8454392` local** (push/deploy pendentes por decisão do dono) + fechamento (card+fix → `05 Arquivo/Bugs/NXG-026/`).
