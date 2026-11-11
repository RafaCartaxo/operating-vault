# 02 - Plano de correção (NXG-034 — Copia offsite legada sinaliza sucesso sem arquivos)

> [!info]- Navegação QA/DEV
> **Bug QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-034 Copia offsite legada sinaliza sucesso sem arquivos/01 - Bug|Bug e critérios]]  
> **Casos QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-034 Copia offsite legada sinaliza sucesso sem arquivos/02 - Casos de teste|8 CTs]]  
> **Gate QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-034 Copia offsite legada sinaliza sucesso sem arquivos/05 - Gate de integridade QA|QA_READY_FOR_DEV]]  
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]

## Resultado esperado

`scripts/pull-backup.sh` copia ID explícito em staging privado, chama `verify-backup.sh` e publica sem sobrescrita. `scripts/corrections.check.mjs` usa SSH/SCP dublados; guia 08 e runbook 09 explicitam limitações.

## Mudança planejada

Preservar delta NXG-031; implementar correção e regressão em fixtures isoladas com guardas confirmadas antes da execução.

## Fora de escopo

Docker CLI/daemon, SSH/SCP real, rede, serviços, segredos, commit, push, deploy e recursos reais.

## Pronto quando

- [x] Verificação técnica sintética e code review DEV registrados.
- [ ] CTs e aprovação funcional QA independentes.
