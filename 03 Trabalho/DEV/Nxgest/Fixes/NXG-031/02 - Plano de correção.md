# 02 - Plano de correção (NXG-031)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-031 Transicao segura do deploy e continuidade operacional/01 - Bug|NXG-031 — Transição segura do deploy]]  
> **Análise:** [[01 - Análise|01 - Análise]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Casos de teste QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-031 Transicao segura do deploy e continuidade operacional/02 - Casos de teste|Casos de teste]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-031 Transicao segura do deploy e continuidade operacional/03 - Validação dev|Validação QA]]

> Congelado na aprovação. Alteração posterior vira decisão registrada em `03 - Implementação.md`.

---

## Resultado esperado

A primeira transição e as entradas repetida/manual usam código do SHA alvo, preservam trabalho e env e falham fechadas.

---

## Mudança planejada

Ajustar workflows, bootstrap e scripts de deploy; sincronizar onboarding, runbook e Cloudflare; executar testes com Git local sintético, Docker dublê e transporte cifrado entre homes sintéticos.

---

## Fora de escopo

Commit, push, deploy, SSH/VPS, painel Cloudflare, segredos reais, trabalho WIP e aprovação funcional QA.

---

## Pronto quando

[x] Regressões técnicas e gates aplicáveis executados.
- [x] Code review DEV com limitações.
- [ ] Seis CTs executados e decididos pelo QA independente.

---

