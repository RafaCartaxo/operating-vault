# Implementação — nova baseline CT-011

> [!info]- Navegação
> [[00 README|Execução]] · [[01 - Análise|Análise]] · [[02 - Plano de execução|Plano]] · [[04 - Code review|Code review]] · [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/09 - Nova baseline QA|CT-N01–N10]]

## Rodadas

- `scripts/create-schema.mjs` não imprime mais DATABASE_URL.
- `scripts/baseline-evidence-fixture.mjs` fixa emissor/verificador/política de fixture e verifica assinatura Ed25519, validade e vínculo sujeito, retornando `operationalReady:false`; chave e observações são fornecidas pelo teste e não são fonte de confiança operacional.
- `scripts/synthetic-safe-extract.mjs` extrai tar/gzip restrito em diretório sintético vazio; `scripts/synthetic-rehearsal.mjs` orquestra capture/cópia/restore apenas via dublê, com quiescência sintética e identificação de conjunto.
- `scripts/rehearsal-postgres-real.mjs` recusa execução com código 78; não cria recursos. Adaptador para isolamento Docker/PG real, captura, restore real e cleanup seguro ainda não estão implementados.
- `test-corrections-isolated.sh` inclui novos testes sob as guardas existentes; `docs/engineering/09-BACKUP-ROLLBACK.md` registra limites. Gates operacionais permanecem incondicionalmente NO-GO por falta de adaptador autenticado real.

## Evidências técnicas — não constituem aprovação QA

`.maestro/nxgest-team/ct011-baseline-dev/tests-final.log`: 29/29 testes sintéticos/regressão e auditoria documental sem divergências; guardas PATH, absoluto e subprocessos confirmadas antes, rede isolada. `.maestro/nxgest-team/ct011-baseline-dev/gate.log`: `npm run test:corrections` 5/5, mesmas guardas. `git diff --check` passou; HEAD/WIP preservados.

| CT | Situação técnica local |
|---|---|
| N01 | Parcial: reconciliação/arquivo sintético; sem banco real. |
| N02 | Parcial: rejeita quiescência desconhecida no dublê; não controla escrita real. |
| N03 | Parcial: verificação anterior e associação de cópia dublada; sem transporte real. |
| N04 | **Bloqueado**: restore PostgreSQL real e harness de execução ainda não implementados/autorizados. |
| N05/N06 | Política de fixture com chaves sintéticas verifica emissor/verificador, validade, run, bundle e sujeitos; fonte e verificador GitHub reais não implementados. |
| N07/N08 | Saúde/integridade e fluxo positivo testados somente como fixture; gates reais seguem NO-GO. |
| N09/N10 | Guardas e regressão sintética 29/29; ausência de prova real GitHub/PG. |

Sem Docker CLI/daemon, rede, SSH, dados ou recursos reais; sem commit/push/deploy. Os resultados não são aceites dos CTs pelo QA.
