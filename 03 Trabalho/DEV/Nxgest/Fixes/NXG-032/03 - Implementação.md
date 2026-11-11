# 03 - Implementação (NXG-032 — Consistencia semantica entre banco e anexos nao demonstrada)

> [!info]- Navegação QA/DEV
> **Bug QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/01 - Bug|Bug e critérios]]<br>
> **Casos QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/02 - Casos de teste|8 CTs]]<br>
> **Gate QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/05 - Gate de integridade QA|QA_READY_FOR_DEV]]<br>
> **Reteste:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/06 - Evidências QA|Evidências do reteste QA]] · [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/03 - Validação dev|Validação QA]]<br>
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]

## Rodadas

2026-11-11: `scripts/reconcile-fixture.mjs` confere referências restauradas sintéticas com arquivos, tamanho e caminhos seguros; órfãos são relatados. `scripts/backup-recovery.check.mjs` amplia os cenários de restore fictício e falha de escrita em `/dev/full`.

## Evidências

`.maestro/nxgest-team/nxg032-034/run-isolated.sh`: guardas verificadas em resolução, caminho absoluto e subprocesso antes dos testes; namespace de rede isolado e binários reais mascarados. Suíte conjunta 26/26; log `.maestro/nxgest-team/nxg032-034/testes-finais.log`. Inclui regressão NXG-031, falhas de escrita/colisão e cópia sintética. `git diff --check` passou. Nenhum CT QA é aprovado por este resultado.

## Testes da correção

- [x] Cenários sintéticos automatizados em `scripts/backup-recovery.check.mjs` e `scripts/corrections.check.mjs`.
- [x] Regressão em `scripts/deploy-transition.check.mjs`.
- [x] Reteste independente: **8/8 CTs sintéticos aprovados com ressalvas**; [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/06 - Evidências QA|Evidências do reteste QA]].
- [ ] Gate final de QA pendente.

A reconciliação é sintética, não garante consistência temporal de coleta nem restore PostgreSQL real. O desvio histórico de Docker CLI da MEL-0009 permanece registrado; reteste não o apaga. Sem commit.

## Reteste e pendências compartilhadas

QA registrou 24/24 CTs sintéticos nos três filhos; a aprovação é restrita a fixtures e dublês. [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/08 - Evidências reteste QA|Reteste do pai MEL-0009]]. MEL-0009 permanece QA_REJECTED/no-go: CT-011 e CT-013 bloqueados; [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/01 - Bug|NXG-035]] em triagem. A execução histórica do CLI Docker não se torna conforme retroativamente.
