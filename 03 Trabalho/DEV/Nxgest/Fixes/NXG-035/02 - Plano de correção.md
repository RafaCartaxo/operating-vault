# 02 - Plano de correção (NXG-035)

> [!info]- Navegação QA/DEV
> **Bug:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/01 - Bug|NXG-035]]<br>
> **Casos:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/02 - Casos de teste|Sete CTs]]<br>
> **Gate:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/05 - Gate de integridade QA|QA_READY_FOR_DEV]]<br>
> **Validação:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/03 - Validação dev|Validação QA]]<br>
> **Evidências:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/06 - Evidências QA|Evidências do reteste QA]]<br>
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]

## Resultado esperado

CI e CD manual executam os dois testes sintéticos e propagam falha; CD manual configura Node 20.

## Mudança planejada

Runner sem caminhos pessoais, guardas e isolamento verificados, requisitos explícitos e falha fechada. Preservar gates anteriores e no-go operacional.

## Fora de escopo

GitHub Actions real, Docker CLI/daemon, rede, recursos reais, SSH, push, commit e deploy.

## Pronto quando

QA concluiu o reteste independente com 7/7 CTs sintéticos e ressalvas; [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/06 - Evidências QA|Evidências do reteste QA]]. Compatibilidade GitHub Actions real permanece não comprovada.
