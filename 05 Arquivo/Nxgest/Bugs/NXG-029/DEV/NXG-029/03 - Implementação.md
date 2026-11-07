# 03 - Implementação (NXG-029)

> [!info]- Navegação QA/DEV
> **README DEV:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/00 README|README DEV]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/01 - Bug|Demanda QA]]  
> **Casos de teste QA:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/02 - Casos de teste|Casos de teste QA]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/03 - Validação dev|Validação QA]]  
> **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|Épico]]  
> **Análise:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/01 - Análise|Análise]]  
> **Plano:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/02 - Plano de correção|Plano]]  
> **Implementação:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/03 - Implementação|Implementação]]  
> **Code review:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/04 - Code review|Code review]]  

## Rodadas

### Rodada 1 — implementação e ajustes

`a509f4b`: gerador com nome entre aspas e leitor como dados; `c0b0d3a`: implementação Bash, sem Node no host. Testes sintéticos cobrem geração, reutilização byte a byte, valor legado, conteúdo de shell literal e chave desconhecida.

Base `8454392`; o estado anterior foi preservado em `.maestro/nxgest-team/recovery/2026-11-07`: restauração comparada de 45 caminhos rastreados e SHA-256/modos dos 20 novos. Os sete arquivos de ícones e `scripts/qase-sync.mjs` estão na branch WIP `wip/nxg-preservacao-icones-qase-20261107`, commit `14f3e50`. Nenhum env real foi copiado. Push, deploy e encerramento do épico permanecem fora do escopo.

## Evidências

Node `20.20.2`, Docker Compose `5.3.1`. `npm test`: 46 arquivos e 215 testes passaram; `npm run build` e `node scripts/check-dist.mjs`: passaram; `npm run docs:audit`, `audit:ui`, `audit:styles`, `audit:modules`, `audit:links` e `git diff --check`: passaram. Links: zero erros e cinco avisos históricos classificados em `.maestro/nxgest-team/DEV-ENTREGA.md`. `docker compose config --quiet` passou nos três Compose com `.env.example` sintético e ambiente de processo vazio, sem iniciar stacks existentes. `npm run test:safety` passou 9/9 em `c7b65c8`.

Smoke DEV em PostgreSQL dedicado e uploads sintéticos: 286/286 na rodada do supervisor de `c0b0d3a`, antes das últimas guardas de URL/PID, testadas separadamente; container e grupo próprios encerrados. Antes disso, uma rodada obteve 285/286 ao usar uploads sob `.maestro`, pois o servidor bloqueou o caminho oculto; a rodada subsequente em caminho próprio não oculto passou. Não houve leitura de env real (`DOTENV_CONFIG_PATH=/dev/null`), deploy nem push.

## Testes da correção

- [x] `npm run test:safety`: 9/9, incluindo os dublês da causa e regressões de staging/smoke.
- [x] Gates técnicos comuns e limites registrados em Evidências.
- [ ] CTs funcionais de NXG-029: execução e decisão independentes do QA.
- Formulário/UI e API/repositório específicos deste fix: não aplicáveis; a suíte integrada foi executada.
