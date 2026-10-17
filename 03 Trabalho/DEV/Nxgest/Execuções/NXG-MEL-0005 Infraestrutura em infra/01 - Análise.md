# 01 - Análise (NXG-MEL-0005)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0005 Infraestrutura em infra/01 - Demanda|NXG-MEL-0005 — Infraestrutura em infra/]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0005 Infraestrutura em infra/04 - Validação dev|Validação QA]]

---

## Veredito

A melhoria é viável: mover `Dockerfile`, `Caddyfile` e os 3 `docker-compose.{yml,staging.yml,prod.yml}` para `infra/` não exige mudança em nenhum workflow de CI/CD (nenhum referencia path de compose diretamente) nem em `.env`/`.env.*.example` (docker compose resolve `.env` pelo diretório de trabalho da chamada, não pelo diretório do arquivo compose).

---

## O que foi confirmado

- `.github/workflows/ci.yml` e `cd.yml` só fazem SSH e chamam `scripts/deploy.sh`/`deploy-staging.sh` — nenhuma referência direta a `docker-compose.*.yml`.
- `docker compose` resolve caminhos relativos de `build.context` e `volumes` (bind mounts) em relação à localização do **arquivo compose**, não ao diretório de invocação — confirmado na documentação oficial do Compose v2. Por isso `build: .` precisa virar `build: { context: .., dockerfile: infra/Dockerfile }` nos 3 compose (o Dockerfile também muda de pasta).
- O volume do Caddyfile (`./Caddyfile:/etc/caddy/Caddyfile:ro,z`, em `docker-compose.prod.yml`) **não precisa mudar**, pois o Caddyfile move junto para `infra/` — o caminho relativo `./Caddyfile` continua resolvendo corretamente a partir da nova localização do próprio compose.
- `.env`/`.env.*.example` continuam na raiz, fora do escopo deste lote — `docker compose` carrega `.env` a partir do diretório de trabalho de quem invoca o comando (confirmado: `scripts/deploy.sh`/`deploy-staging.sh` já fazem `cd "$(dirname "$0")/.."` antes de chamar `docker compose`, então o `.env` da raiz continua sendo encontrado mesmo com o compose em `infra/`).
- 4 pontos de referência precisam de atualização de path: `scripts/deploy.sh` (2 ocorrências), `scripts/deploy-staging.sh` (1 ocorrência), `.opencode/agents/ops-runner.md` (2 ocorrências), `docs/engineering/06-PRODUCAO.md` (5 ocorrências: build/up, 3× logs/ps, 1× restart no rollback).
- Nomes reais de volumes (`nxgestao_data`, `nxgestao_pgdata`, `nxgestao_staging_data`, `nxgestao_staging_pgdata`), rede (`nxgestao_net`) e containers (`nxgest-postgres`, `nxgest-pg-dev`, `staging-app`, `staging-pg`) não aparecem em nenhum caminho de arquivo — mover os arquivos de definição não exige tocar nesses nomes.

---

## Abordagem e riscos

- Mover os 5 arquivos com `mv` (preserva conteúdo, não é uma reescrita).
- Ajustar `build:` dos 3 compose para `context: ..` + `dockerfile: infra/Dockerfile`, validando com `docker compose -f infra/docker-compose*.yml config` antes de considerar o lote pronto.
- Atualizar os 4 arquivos de referência com edição cirúrgica (old_string/new_string exato), não reescrita ampla, para minimizar risco de alterar algo fora do escopo.
- Risco principal: misturar esta mudança com os 27 arquivos modificados e 10 untracked já existentes no repositório (trabalho em andamento de outra feature). Mitigação: `git status -sb` antes e depois, comparando a lista exata.
- Risco secundário: quebrar o contexto de build do Docker. Mitigação: `docker compose config` nos 3 ambientes antes de fechar o lote.

---

## Alternativas descartadas

- Manter `build: .` e mover só o Dockerfile via `dockerfile:` sem mudar `context` — descartado porque o contexto `.` relativo ao novo local do compose (`infra/`) não teria acesso a `package.json`, `src/`, `frontend/` etc. na raiz.

---

## Perguntas abertas

- Nenhuma. Este lote está limitado ao escopo já aprovado em QA (C1–C7 de `01 - Demanda.md`).
