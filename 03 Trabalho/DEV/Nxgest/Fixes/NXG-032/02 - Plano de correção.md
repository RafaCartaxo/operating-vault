# 02 - Plano de correção (NXG-032 — Consistencia semantica entre banco e anexos nao demonstrada)

> [!info]- Navegação QA/DEV
> **Bug QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/01 - Bug|Bug e critérios]]<br>
> **Casos QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/02 - Casos de teste|8 CTs]]<br>
> **Gate QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/05 - Gate de integridade QA|QA_READY_FOR_DEV]]<br>
> **Reteste:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/06 - Evidências QA|Evidências do reteste QA]] · [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/03 - Validação dev|Validação QA]]<br>
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]

## Resultado esperado

`scripts/reconcile-fixture.mjs` confere referências restauradas sintéticas com arquivos, tamanho e caminhos seguros; órfãos são relatados. `scripts/backup-recovery.check.mjs` amplia os cenários de restore fictício e falha de escrita em `/dev/full`.

## Mudança planejada

Preservar delta NXG-031; implementar correção e regressão em fixtures isoladas com guardas confirmadas antes da execução.

## Fora de escopo

Docker CLI/daemon, SSH/SCP real, rede, serviços, segredos, commit, push, deploy e recursos reais.

## Pronto quando

- [x] Verificação técnica sintética e code review DEV registrados.
- [x] Oito CTs retestados por QA no escopo sintético, com ressalvas.
- [ ] Gate final e decisão de QA pendentes.
