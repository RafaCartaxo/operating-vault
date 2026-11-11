# 03 - Implementação (NXG-033 — Declaracoes inconsistentes passam no preflight de rollback)

> [!info]- Navegação QA/DEV
> **Bug QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/01 - Bug|Bug e critérios]]  
> **Casos QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/02 - Casos de teste|8 CTs]]  
> **Gate QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/05 - Gate de integridade QA|QA_READY_FOR_DEV]]  
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]

## Rodadas

2026-11-11: `scripts/rollback-preflight.sh` detecta contradição em schema estruturado e mantém NO-GO sem origem verificável; `scripts/verify-rollback-return.sh` não declara sucesso sem comprovação de identidade e integridade. `scripts/rollback-evidence-fixture.mjs` compara SHA, imagem, schema, mounts, configuração e conjunto exclusivamente em fixture; não é fonte de confiança.

## Evidências

`.maestro/nxgest-team/nxg032-034/run-isolated.sh`: guardas verificadas em resolução, caminho absoluto e subprocesso antes dos testes; namespace de rede isolado e binários reais mascarados. Suíte conjunta 26/26; log `.maestro/nxgest-team/nxg032-034/testes-finais.log`. Inclui regressão NXG-031, falhas de escrita/colisão e cópia sintética. `git diff --check` passou. Nenhum CT QA é aprovado por este resultado.

## Testes da correção

- [x] Cenários sintéticos automatizados em `scripts/backup-recovery.check.mjs` e `scripts/corrections.check.mjs`.
- [x] Regressão em `scripts/deploy-transition.check.mjs`.
- [ ] Reteste independente de QA.

Não existe fonte autenticada real; o bloqueio de promoção e retorno é deliberado e persistirá até haver prova verificável. O comparador sintético não é integrado como autoridade de produção. O desvio histórico de Docker CLI da MEL-0009 permanece registrado; reteste não o apaga. Sem commit.
