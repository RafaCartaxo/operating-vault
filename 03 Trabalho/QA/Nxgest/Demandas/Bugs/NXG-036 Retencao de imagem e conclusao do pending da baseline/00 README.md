---
projeto: Nxgest
status: concluido
etapa_atual: "Concluído"
pai: NXG-MEL-0009
tipo: bug
---
# NXG-036 — Retenção de imagem e conclusão do pending da baseline

> [!info]- Navegação QA/DEV
> **README:** [[00 README]] · **Bug:** [[01 - Bug]] · **Casos:** [[02 - Casos de teste]] · **Validação:** [[03 - Validação dev]] · **Qase:** [[04 - Preparação Qase]] · **Pai:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/00 README|NXG-MEL-0009]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`


**Gate vigente:** QA_APPROVED com ressalvas para 13/13 CTs sintéticos. Fix DEV aguarda sincronização pelo responsável; nenhuma operação real foi aprovada.

- [[01 - Bug]]: fatos, critérios e limites.
- [[02 - Casos de teste]]: 13 CTs e matriz.
- [[03 - Validação dev]]: resultados reservados ao reteste.
- [[04 - Preparação Qase]]: mapeamento sem envio.
- [[05 - Gate de integridade QA]]: auditoria e handoff.

## Reteste QA — 2026-11-13

QA_REJECTED para fechamento integral por cobertura incompleta; suíte isolada 100/100 e sonda adicional 4/4. O plano histórico é documental; B11/B12 bloqueados e B06/B09/B13 parciais. Parecer: `.maestro/nxgest-team/NXG-036-PARECER-QA.md`. Nenhum pending histórico ou serviço real foi operado.

## Decisão vigente — 2026-11-13

QA_APPROVED com ressalvas para 13/13 CTs sintéticos após retrabalho; o QA_REJECTED anterior permanece histórico. Backend real deve ser confirmado antes de operação; fixture não autoriza reparo histórico. Parecer `.maestro/nxgest-team/NXG-036-PARECER-QA.md`.
