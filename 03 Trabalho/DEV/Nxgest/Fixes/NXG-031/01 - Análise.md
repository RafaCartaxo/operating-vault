# 01 - Análise (NXG-031)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-031 Transicao segura do deploy e continuidade operacional/01 - Bug|NXG-031 — Transição segura do deploy]]  
> **Plano:** [[02 - Plano de correção|02 - Plano de correção]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Casos de teste QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-031 Transicao segura do deploy e continuidade operacional/02 - Casos de teste|Casos de teste]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-031 Transicao segura do deploy e continuidade operacional/03 - Validação dev|Validação QA]]

---

## Veredito

Causa confirmada: o workflow executava o script legado carregado antes de trocar o checkout, podendo chamar o Compose da raiz removido. O CD também usava reset destrutivo no mesmo checkout. Correção implementada e exercitada somente em fixtures.

---

## O que foi confirmado

O script legado no commit de referência atualizava o Git após iniciar; o layout alvo usa infra/. Staging e produção compartilham checkout; envs reais e Cloudflare não foram consultados.

---

## Abordagem e riscos

Workflow adquire flock, faz fetch do SHA completo e lê o bootstrap do próprio alvo por git show; bootstrap recusa árvore suja, protege ignorados, posiciona SHA e chama script alvo. Staging registra sucesso por SHA; produção exige marcador correspondente e backup. Git, Bash e flock são requisitos no host. Retornos, operação real e backup instalado não foram observados; revisão e pré-publicação permanecem com QA/operação.

---

