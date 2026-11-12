---
status: concluido
tipo: bug
etapa_atual: "Concluído"
demanda: "NXG-035"
commit: ""
---

# NXG-035 — Suíte de correções nos gates automatizados

> [!info]- Navegação QA/DEV
> **Bug:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/01 - Bug|NXG-035]]<br>
> **Casos:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/02 - Casos de teste|Sete CTs]]<br>
> **Gate:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/05 - Gate de integridade QA|QA_READY_FOR_DEV]]<br>
> **Validação:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/03 - Validação dev|Validação QA]]<br>
> **Evidências:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/06 - Evidências QA|Evidências do reteste QA]]<br>
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]

## Status

**QA_APPROVED com ressalvas:** 7/7 CTs aprovados em fixtures e dublês no reteste independente; [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/06 - Evidências QA|Evidências do reteste QA]]. GitHub Actions e a disponibilidade de bwrap/namespaces no runner hospedado não foram comprovados.

O pai MEL-0009 permanece **QA_REJECTED/NO-GO**, com CT-011 bloqueado. CT-013 foi aprovado somente para a rodada atual; a execução histórica do Docker CLI real permanece não conforme, sem validação retroativa.

## Checklist de transição DEV

- [x] Análise, plano, implementação, revisão e evidências locais registrados.
- [x] Requisitos e limitação de compatibilidade GitHub documentados.
- [x] Reteste QA aprovado com ressalvas no escopo sintético.
- [ ] Commit fora desta autorização.


## Continuidade CI — 2026-11-12

Continuidade de falha real do CI: correção local do sandbox awk em fix/nxg035-awk-sandbox, DEV_READY_FOR_QA para revisão específica. O anterior QA_APPROVED sintético não comprova esta alteração nem sucesso futuro do CI. Evidência em .maestro/nxgest-team/CT011-CI-AWK-DEV-RESULTADO.md.
