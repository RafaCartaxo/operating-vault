# 01 - Análise (NXG-032 — Consistencia semantica entre banco e anexos nao demonstrada)

> [!info]- Navegação QA/DEV
> **Bug QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/01 - Bug|Bug e critérios]]<br>
> **Casos QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/02 - Casos de teste|8 CTs]]<br>
> **Gate QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/05 - Gate de integridade QA|QA_READY_FOR_DEV]]<br>
> **Reteste:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/06 - Evidências QA|Evidências do reteste QA]] · [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/03 - Validação dev|Validação QA]]<br>
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]

## Veredito

Causa local identificada no parecer QA.

## O que foi confirmado

`scripts/reconcile-fixture.mjs` confere referências restauradas sintéticas com arquivos, tamanho e caminhos seguros; órfãos são relatados. `scripts/backup-recovery.check.mjs` amplia os cenários de restore fictício e falha de escrita em `/dev/full`.

## Abordagem e riscos

A reconciliação é sintética, não garante consistência temporal de coleta nem restore PostgreSQL real. Análise técnica consolidada em `.maestro/nxgest-team/NXG-MEL-0009-CORRECOES-ANALISE.md`.

## Situação após reteste QA

QA registrou 8/8 CTs aprovados somente no escopo sintético, com ressalvas; [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/06 - Evidências QA|Evidências do reteste QA]]. Gate final pendente. MEL-0009 continua QA_REJECTED/no-go, com CT-011 e CT-013 bloqueados e [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/01 - Bug|NXG-035]] em triagem.
