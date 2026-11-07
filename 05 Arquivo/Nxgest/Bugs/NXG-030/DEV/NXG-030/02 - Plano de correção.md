# 02 - Plano de correção (NXG-030)

> [!info]- Navegação QA/DEV
> **README DEV:** [[05 Arquivo/Nxgest/Bugs/NXG-030/DEV/NXG-030/00 README|README DEV]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Bugs/NXG-030/QA/NXG-030 Smoke protege banco e interpreta opcoes/01 - Bug|Demanda QA]]  
> **Casos de teste QA:** [[05 Arquivo/Nxgest/Bugs/NXG-030/QA/NXG-030 Smoke protege banco e interpreta opcoes/02 - Casos de teste|Casos de teste QA]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Bugs/NXG-030/QA/NXG-030 Smoke protege banco e interpreta opcoes/03 - Validação dev|Validação QA]]  
> **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|Épico]]  
> **Análise:** [[05 Arquivo/Nxgest/Bugs/NXG-030/DEV/NXG-030/01 - Análise|Análise]]  
> **Plano:** [[05 Arquivo/Nxgest/Bugs/NXG-030/DEV/NXG-030/02 - Plano de correção|Plano]]  
> **Implementação:** [[05 Arquivo/Nxgest/Bugs/NXG-030/DEV/NXG-030/03 - Implementação|Implementação]]  
> **Code review:** [[05 Arquivo/Nxgest/Bugs/NXG-030/DEV/NXG-030/04 - Code review|Code review]]  

## Resultado esperado

Recusar alvos/opções inseguros antes de conectar ou semear e limpar apenas processos próprios em sucesso ou falha.

## Mudança planejada

- Arquivos e abordagem: `scripts/smoke.mjs`, `scripts/smoke-supervisor.mjs`, `scripts/safety-check.mjs`, gate CI e guia de testes; usar somente banco sintético exclusivo.
- Decisão: Após QA, substituir `/proc` por `ps` com início, grupo e nonce, e tratar PID desaparecido com sonda sinal 0. Manter erro de identidade sem sinalização.
- Regressões: testes controlados em `scripts/safety-check.mjs` e smoke em recursos próprios quando aplicável.

## Fora de escopo

Deploy, push, VPS, recursos e envs reais, aprovação dos CTs e fechamento do épico.

## Pronto quando

- [ ] CTs executados e decididos por QA: [[05 Arquivo/Nxgest/Bugs/NXG-030/QA/NXG-030 Smoke protege banco e interpreta opcoes/02 - Casos de teste|casos de teste]].
- [x] Regressão automatizada executada.
- [x] Gates técnicos aplicáveis executados, com limitações registradas.
- [x] Code review técnico concluído.
