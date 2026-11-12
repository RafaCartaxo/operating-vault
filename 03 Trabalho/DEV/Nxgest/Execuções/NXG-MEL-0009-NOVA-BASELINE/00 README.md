---
status: execucao
tipo: melhoria
etapa_atual: "DEV · Implementação"
demanda: "NXG-MEL-0009"
---
# Nova baseline CT-011 — execução DEV

> [!info]- Navegação
> **Adendo QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/09 - Nova baseline QA|C1–C5 e CT-N01–N10]]<br>
> **Análise:** [[01 - Análise]] · **Plano:** [[02 - Plano de execução]] · **Implementação:** [[03 - Implementação]] · **Code review:** [[04 - Code review]]

## Status

DEV_READY_FOR_QA para revisão local: harness PostgreSQL opt-in implementado e testado exclusivamente com dublês isolados. Adaptador operacional de procedência não comprovado; CT-N04 real segue bloqueado até autorização e execução próprias. MEL-0009 segue QA_REJECTED/NO-GO.

Após QA_REJECTED, política controlada no workspace associa ID PG16 aprovado antes de criação/início; reteste DEV 17/17 sob dublês. DEV_READY_FOR_QA para reteste local, sem aprovação funcional; fonte real de build e CT-N04 permanecem bloqueados. Ver resultado consolidado `.maestro/nxgest-team/CT011-NOVA-BASELINE-DEV-RESULTADO.md`.

Após QA_REJECTED reteste 2, limpeza da fixture corrigida e sentinela/política sintéticas preservadas em snapshot isolado; DEV_READY_FOR_QA para novo reteste independente.

- Complemento N04: observador independente opcional preparado antes da limpeza; DEV_READY_FOR_QA para revisão. Execução real anterior positiva permanece com ressalva de independência e não valida alteração posterior.


## Adoção staging — continuidade DEV

Adoção staging: DEV_READY_FOR_QA integrado para revisão independente de política, cápsula, transporte, bootstrap e executor; não é aprovação operacional nem altera NO-GO de BA10. Evidência: .maestro/nxgest-team/CT011-ADOCAO-STAGING-DEV-RESULTADO.md.
