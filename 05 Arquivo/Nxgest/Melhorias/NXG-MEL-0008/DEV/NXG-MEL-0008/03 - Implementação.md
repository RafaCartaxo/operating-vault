# 03 - Implementação (NXG-MEL-0008)

> [!info]- Navegação QA/DEV
> **README DEV:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/00 README|README DEV]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/QA/NXG-MEL-0008 Consolidacao de ambientes e portabilidade/01 - Demanda|Demanda QA]]  
> **Casos de teste QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/QA/NXG-MEL-0008 Consolidacao de ambientes e portabilidade/03 - Casos de teste|Casos de teste QA]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/QA/NXG-MEL-0008 Consolidacao de ambientes e portabilidade/04 - Validação dev|Validação QA]]  
> **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|Épico]]  
> **Análise:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/01 - Análise|Análise]]  
> **Plano:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/02 - Plano de execução|Plano]]  
> **Implementação:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/03 - Implementação|Implementação]]  
> **Code review:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/04 - Code review|Code review]]  

## Rodadas

### Rodada 1 — implementação e ajustes

`a509f4b`: infra, agentes, ambiente e correções; `7099a97`: cliente/documento/CEP e tratamento de CEP opcional; `b9d3954`, `2db5826`, `c0b0d3a` e `c7b65c8`: regressões e segurança de smoke/staging. O onboarding passou a indicar HTTPS e trata 15 minutos como meta não medida.

Base `8454392`; o estado anterior foi preservado em `.maestro/nxgest-team/recovery/2026-11-07`: restauração comparada de 45 caminhos rastreados e SHA-256/modos dos 20 novos. Os sete arquivos de ícones e `scripts/qase-sync.mjs` estão na branch WIP `wip/nxg-preservacao-icones-qase-20261107`, commit `14f3e50`. Nenhum env real foi copiado. Push, deploy e encerramento do épico permanecem fora do escopo.

## Evidências

Node `20.20.2`, Docker Compose `5.3.1`. `npm test`: 46 arquivos e 215 testes passaram; `npm run build` e `node scripts/check-dist.mjs`: passaram; `npm run docs:audit`, `audit:ui`, `audit:styles`, `audit:modules`, `audit:links` e `git diff --check`: passaram. Links: zero erros e cinco avisos históricos classificados em `.maestro/nxgest-team/DEV-ENTREGA.md`. `docker compose config --quiet` passou nos três Compose com `.env.example` sintético e ambiente de processo vazio, sem iniciar stacks existentes. `npm run test:safety` passou 9/9 em `c7b65c8`.

Smoke DEV em PostgreSQL dedicado e uploads sintéticos: 286/286 na rodada do supervisor de `c0b0d3a`, antes das últimas guardas de URL/PID, testadas separadamente; container e grupo próprios encerrados. Antes disso, uma rodada obteve 285/286 ao usar uploads sob `.maestro`, pois o servidor bloqueou o caminho oculto; a rodada subsequente em caminho próprio não oculto passou. Não houve leitura de env real (`DOTENV_CONFIG_PATH=/dev/null`), deploy nem push.

### Ambiente e smoke check

- Backend de smoke: `PORT=3002`; alvo definido por `SMOKE_DATABASE_URL` em PostgreSQL local dedicado e porta atribuída pelo Docker.
- Checkout anterior do QA: frontend Vite `https://localhost:5173`, proxy para API; QA relatou login, cliente e persistência em `7099a97`. O DEV não afirma tê-lo executado.
- Health: `GET http://127.0.0.1:3002/api/health` respondeu no smoke DEV; `DOTENV_CONFIG_PATH=/dev/null`.

## Testes da implementação

- [x] Unitários e UI: `npm test`, 215 testes.
- [x] Segurança/regressão: `scripts/safety-check.mjs`, 9/9.
- [x] Build, check-dist, Compose config e auditorias, com ressalvas descritas.
- [ ] CTs funcionais independentes da revisão final: responsabilidade QA.

## Verificação

- [x] Casos QA vinculados na navegação.
- [x] Gates técnicos executados e limites registrados.
- [x] Documentação e commits registrados.
- [ ] QA decidir aceites, governança e fechamento.
