# 03 - Implementação (NXG-035)

> [!info]- Navegação QA/DEV
> **Bug:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/01 - Bug|NXG-035]]<br>
> **Casos:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/02 - Casos de teste|Sete CTs]]<br>
> **Gate:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/05 - Gate de integridade QA|QA_READY_FOR_DEV]]<br>
> **Validação:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/03 - Validação dev|Validação QA]]<br>
> **Evidências:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/06 - Evidências QA|Evidências do reteste QA]]<br>
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]

## Rodadas

`scripts/test-corrections-isolated.sh` cria cópia restrita dos quatro scripts necessários e executa os dois testes sob bwrap, rede isolada e guardas para Docker, curl, ssh e scp por PATH e caminhos absolutos. Prova as guardas e subprocessos antes de executar os testes. Requer Linux, Node >=20, bwrap, namespaces e destinos para mascarar; ausência ou falha interrompe a execução. Sem caminhos pessoais ou fallback inseguro.

`package.json` expõe `test:corrections`. CI e CD manual chamam o comando; CD manual configura Node 20. `docs/qa/04-TESTES.md` declara requisitos e limites. Os 15 arquivos de Fix NXG-032/033/034 tiveram espaços finais removidos, substituindo quebras Markdown intencionais por `<br>`.

## Evidências

- `npm run test:corrections`: os dois testes executados passaram, sem saltos; `.maestro/nxgest-team/nxg035/suite.log`.
- `.maestro/nxgest-team/nxg035/verify-fixtures.py`: 26 cenários de gate dublados (CI e manual), incluindo os dois testes individualmente reprovados em cada gate, quatro guardas ausentes ou inválidas e bwrap/namespace indisponível. Todas as falhas bloquearam a sentinela de promoção; seis simulações adicionais cobriram falhas dos gates safety/deploy/backup. Log `fixture-resultados.log`. Simulação local não é execução de GitHub Actions.
- Regressão anterior sob guardas e isolamento: 26/26 e `docs:audit` sem divergências, `regressao.log`.
- `git diff --check` no produto e no escopo vault solicitado passou; checagem direta das 15 notas, incluindo conteúdo não apresentado pelo diff, encontrou zero linhas com espaços finais.

## Testes da correção

- [x] Execução dos dois casos em isolamento e falhas individuais simuladas.
- [x] Requisitos/guardas ausentes e regressão sintética dos gates anteriores.
- [x] Reteste independente QA: 7/7 CTs sintéticos aprovados com ressalvas; [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/06 - Evidências QA|Evidências do reteste QA]]. Nenhum GitHub Actions real executado.

O preflight e o retorno reais mantêm NO-GO por falta de fonte confiável; o histórico de chamada anterior ao CLI Docker em MEL-0009 permanece. Nenhum commit, push, deploy, SSH, Docker CLI/daemon ou recurso real nesta rodada.


## Continuidade CI — 2026-11-12

Alterado somente nxgest/scripts/test-corrections-isolated.sh na branch fix/nxg035-awk-sandbox, sem commit. SHA-256 359c3175a9e7631a07e4d49e3a38db5b5c16bd1f90ee6c176dead9fee17fac4b. bash -n passou; runner bwrap com guardas PATH/absolutas/subprocessos e rede isolada: 83/83; sonda link Ubuntu e awk controlado confirmada. Log .maestro/nxgest-team/CT011-CI-AWK-DEV-TEST.log SHA-256 5092e527b849079d5b6c3f8c4c0eed49f9f2fe9e248bdcf516e49603c0c833b9. npm run docs:audit passou; git diff --check limpo.
