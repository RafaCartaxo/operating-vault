# 01 - Análise (NXG-035)

> [!info]- Navegação QA/DEV
> **Bug:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/01 - Bug|NXG-035]]<br>
> **Casos:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/02 - Casos de teste|Sete CTs]]<br>
> **Gate:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/05 - Gate de integridade QA|QA_READY_FOR_DEV]]<br>
> **Validação:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/03 - Validação dev|Validação QA]]<br>
> **Evidências:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/06 - Evidências QA|Evidências do reteste QA]]<br>
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]

## Veredito

Os dois testes de `corrections.check.mjs` não são descobertos pelos comandos dos gates. O runner anterior depende de caminhos pessoais e não é portátil.

## O que foi confirmado

CI e CD manual chamam testes de backup e deploy, mas não a suíte de correções; o CD manual não configura explicitamente Node 20. Fonte: pacote QA e gate 05.

## Abordagem e riscos

Runner Linux isolado, requisitos detectados e falha fechada; guardas e namespaces precisam ser comprovados antes dos testes. Disponibilidade real no GitHub Actions é desconhecida.

## Reteste independente

QA registrou **7/7 CTs sintéticos aprovados com ressalvas**; [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/06 - Evidências QA|Evidências do reteste QA]]. GitHub Actions e disponibilidade de bwrap/namespaces no runner hospedado não foram comprovados.
