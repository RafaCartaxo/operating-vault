---
status: validacao
tipo: bug
etapa_atual: "QA · Validação"
demanda: "NXG-033"
commit: ""
---

# NXG-033 — Declaracoes inconsistentes passam no preflight de rollback

> [!info]- Navegação QA/DEV
> **Bug QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/01 - Bug|Bug e critérios]]<br>
> **Casos QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/02 - Casos de teste|8 CTs]]<br>
> **Gate QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/05 - Gate de integridade QA|QA_READY_FOR_DEV]]<br>
> **Reteste:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/06 - Evidências QA|Evidências do reteste QA]] · [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/03 - Validação dev|Validação QA]]<br>
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]


## Status

O reteste independente de QA registrou **8/8 CTs aprovados no escopo sintético, com ressalvas** para este filho; no conjunto dos três filhos são 24/24. O gate final do QA permanece pendente após esta sincronização. O pai MEL-0009 continua QA_REJECTED/no-go: CT-011 e CT-013 seguem bloqueados, e [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/01 - Bug|NXG-035]] está em triagem. [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/08 - Evidências reteste QA|Reteste do pai MEL-0009]].

## Checklist de transição DEV

- [x] Causa, plano, implementação, teste sintético e revisão registrados.
- [x] Evidências e limitações vinculadas; board DEV atualizado.
- [x] Reteste independente de QA registrado no escopo sintético, com ressalvas.
- [ ] Gate final e decisão de QA pendentes.
- [ ] Commit e fechamento, fora desta autorização.
