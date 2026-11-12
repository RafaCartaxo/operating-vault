# 04 - Code review (NXG-035)

> [!info]- Navegação QA/DEV
> **Bug:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/01 - Bug|NXG-035]]<br>
> **Casos:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/02 - Casos de teste|Sete CTs]]<br>
> **Gate:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/05 - Gate de integridade QA|QA_READY_FOR_DEV]]<br>
> **Validação:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/03 - Validação dev|Validação QA]]<br>
> **Evidências:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/06 - Evidências QA|Evidências do reteste QA]]<br>
> **Fix:** [[00 README|README]] · [[01 - Análise|Análise]] · [[02 - Plano de correção|Plano]] · [[03 - Implementação|Implementação]] · [[04 - Code review|Revisão]]

**Estado:** revisão local concluída; QA_APPROVED com ressalvas, restrito a 7/7 CTs sintéticos.

## Checklist

- [x] CI e CD manual apontam ao mesmo runner; Node 20 é declarado no manual.
- [x] Falhas individuais e ausência de cada guarda foram simuladas com saída não zero.
- [x] Isolamento é requisito verificado antes dos testes; não há fallback sem namespace.
- [x] Gates existentes e NO-GO foram preservados; evidência sintética não representa GitHub Actions real.
- [x] QA aprovou 7/7 CTs sintéticos com ressalvas; [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/06 - Evidências QA|Evidências do reteste QA]].

## Achados e limites

O runner depende explicitamente de Linux, bubblewrap, namespaces permitidos e binários em `/usr/bin` para os destinos a encobrir. Disponibilidade e suporte em GitHub Actions não foram verificados; se ausentes, o gate falha fechado antes dos testes. A simulação de workflow não executou Actions nem promoção real. O histórico de CT-013 não é retroativamente conforme.

## Decisão

QA_APPROVED com ressalvas no escopo sintético; sem autorização de publicação. MEL-0009 permanece QA_REJECTED/NO-GO, com CT-011 bloqueado. CT-013 aprovado apenas na rodada atual; desvio histórico do Docker CLI permanece não conforme.


## Continuidade CI — 2026-11-12

Revisão DEV: nenhum mount de /etc, homes ou sockets; PATH coloca guardas antes do awk, e sonda precede os testes. O executável real é limitado à allowlist e bibliotecas permanecem sob /usr/lib já montado. Layout Ubuntu reproduz link quebrado sintético, mas a suíte executou gawk local, não o mawk nem o runner Actions Ubuntu; QA e CI reais devem validar independentemente. Sem commit/push/merge ou aprovação QA.
