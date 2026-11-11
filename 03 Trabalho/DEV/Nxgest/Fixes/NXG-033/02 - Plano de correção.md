# 02 - Plano de correção (NXG-033 — Declaracoes inconsistentes passam no preflight de rollback)

> [!info]- Navegação QA/DEV
> **Bug QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/01 - Bug|Bug e critérios]]<br>
> **Casos QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/02 - Casos de teste|8 CTs]]<br>
> **Gate QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/05 - Gate de integridade QA|QA_READY_FOR_DEV]]<br>
> **Reteste:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/06 - Evidências QA|Evidências do reteste QA]] · [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/03 - Validação dev|Validação QA]]<br>
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]

## Resultado esperado

`scripts/rollback-preflight.sh` detecta contradição em schema estruturado e mantém NO-GO sem origem verificável; `scripts/verify-rollback-return.sh` não declara sucesso sem comprovação de identidade e integridade. `scripts/rollback-evidence-fixture.mjs` compara SHA, imagem, schema, mounts, configuração e conjunto exclusivamente em fixture; não é fonte de confiança.

## Mudança planejada

Preservar delta NXG-031; implementar correção e regressão em fixtures isoladas com guardas confirmadas antes da execução.

## Fora de escopo

Docker CLI/daemon, SSH/SCP real, rede, serviços, segredos, commit, push, deploy e recursos reais.

## Pronto quando

- [x] Verificação técnica sintética e code review DEV registrados.
- [x] Oito CTs retestados por QA no escopo sintético, com ressalvas.
- [ ] Gate final e decisão de QA pendentes.
