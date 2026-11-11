# 01 - Análise (NXG-033 — Declaracoes inconsistentes passam no preflight de rollback)

> [!info]- Navegação QA/DEV
> **Bug QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/01 - Bug|Bug e critérios]]  
> **Casos QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/02 - Casos de teste|8 CTs]]  
> **Gate QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/05 - Gate de integridade QA|QA_READY_FOR_DEV]]  
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]

## Veredito

Causa local identificada no parecer QA.

## O que foi confirmado

`scripts/rollback-preflight.sh` detecta contradição em schema estruturado e mantém NO-GO sem origem verificável; `scripts/verify-rollback-return.sh` não declara sucesso sem comprovação de identidade e integridade. `scripts/rollback-evidence-fixture.mjs` compara SHA, imagem, schema, mounts, configuração e conjunto exclusivamente em fixture; não é fonte de confiança.

## Abordagem e riscos

Não existe fonte autenticada real; o bloqueio de promoção e retorno é deliberado e persistirá até haver prova verificável. O comparador sintético não é integrado como autoridade de produção. Análise técnica consolidada em `.maestro/nxgest-team/NXG-MEL-0009-CORRECOES-ANALISE.md`.
