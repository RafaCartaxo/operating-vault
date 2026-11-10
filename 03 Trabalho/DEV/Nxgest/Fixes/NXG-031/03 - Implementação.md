# 03 - Implementação (NXG-031)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-031 Transicao segura do deploy e continuidade operacional/01 - Bug|NXG-031 — Transição segura do deploy]]  
> **Plano:** [[02 - Plano de correção|02 - Plano de correção]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-031 Transicao segura do deploy e continuidade operacional/03 - Validação dev|Validação QA]]

---

## Rodadas

### Rodada 1 — implementação e revisão técnica

Workflows de staging/prod adquirem lock e buscam SHA alvo; scripts/deploy-bootstrap.sh valida checkout e executa scripts do SHA. Staging marca sucesso por SHA; produção exige marcador e backup sem bypass. Guias separam desenvolvimento/operação, corrigem transporte e registram Cloudflare como inventário não auditado. A mudança do plano inclui marcador de staging e retirada do bypass para assegurar o gate C4; não houve deploy.

---

## Evidências

`npm run test:deploy`: 9/9, em `scripts/deploy-transition.check.mjs`, com repositórios sintéticos, script legado de referência, Docker/curl dublados, backup sintético e GPG real sobre dois homes sintéticos. Cobre transição, repetição/manual, fetch/ref, dirty/untracked/ignorado, falha staging, backup ausente/falho, lock, gates e transporte. `npm test`: 215/215; `npm run test:safety`: 9/9; build e check-dist passaram. docs:audit, audit:links, audit:ui, audit:styles, audit:modules, bash -n e sintaxe YAML passaram; audit:links reporta cinco avisos históricos. Não se executou Docker real, CI remoto, SSH ou VPS.

---

## Testes da correção

[x] `npm run test:deploy` — 9/9 testes.
- [x] `npm run test:safety` — 9/9.
- [x] `npm test` — 215/215; build e check-dist.
- [x] Auditorias, sintaxe Bash/YAML e diff check.
- [ ] Seis CTs funcionais sob responsabilidade do QA.

---

