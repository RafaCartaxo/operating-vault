# 02 - Plano de execução (NXG-MEL-0005)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0005/QA/NXG-MEL-0005 Infraestrutura em infra/01 - Demanda|NXG-MEL-0005 — Infraestrutura em infra/]]  
> **Plano técnico:** não se aplica — lote de organização, sem `PLAN-NNN` próprio no repositório  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0005/QA/NXG-MEL-0005 Infraestrutura em infra/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Agrupar `Dockerfile`, `Caddyfile` e os 3 `docker-compose.{yml,staging.yml,prod.yml}` em `infra/`, com todas as referências atualizadas, sem alterar comportamento real de nenhum ambiente.

---

## Vínculo e sequência

1. `mv Dockerfile infra/Dockerfile`
2. `mv Caddyfile infra/Caddyfile`
3. `mv docker-compose.yml infra/docker-compose.yml`
4. `mv docker-compose.staging.yml infra/docker-compose.staging.yml`
5. `mv docker-compose.prod.yml infra/docker-compose.prod.yml`
6. Em cada um dos 3 compose movidos, trocar `build: .` por `build:\n  context: ..\n  dockerfile: infra/Dockerfile` (serviço `app`/`staging-app`).
7. `scripts/deploy.sh`: trocar as 2 ocorrências de `docker-compose.prod.yml` por `infra/docker-compose.prod.yml`.
8. `scripts/deploy-staging.sh`: trocar `COMPOSE="-f docker-compose.staging.yml"` por `COMPOSE="-f infra/docker-compose.staging.yml"`.
9. `.opencode/agents/ops-runner.md`: trocar as 2 ocorrências de `docker-compose.prod.yml` por `infra/docker-compose.prod.yml`.
10. `docs/engineering/06-PRODUCAO.md`: trocar as 5 ocorrências (`build app`/`up -d`, logs app, logs caddy, ps, restart app) de `docker-compose.prod.yml` por `infra/docker-compose.prod.yml` (mantendo o prefixo `/opt/nxgestao/` onde já existir).

---

## Escopo aprovado

- **Pode mudar:** os 5 arquivos de infraestrutura (movidos, com `build:` ajustado) + `scripts/deploy.sh` + `scripts/deploy-staging.sh` + `.opencode/agents/ops-runner.md` + `docs/engineering/06-PRODUCAO.md`.
- **Deve permanecer intacto:** `.env*` (qualquer variante), código em `src/`/`frontend/`, `package.json`, agentes além de `ops-runner.md`, `README.md`/`08-SETUP-NOVA-MAQUINA.md` (escopo do `NXG-MEL-0006`), nomes de volumes/rede/containers, e os 27 arquivos modificados + 10 untracked já existentes no repositório antes deste lote.

---

## Decisões

- `build.context` dos 3 compose vira `..` (raiz do repo) e `build.dockerfile` vira `infra/Dockerfile`, em vez de mover o Dockerfile sem ajustar o contexto — único jeito de preservar `COPY package*.json ./` etc. funcionando a partir da raiz real.
- Volume do Caddyfile em `docker-compose.prod.yml` não muda (`./Caddyfile`), pois o Caddyfile acompanha o compose para `infra/`.

---

## Pronto quando

- Critérios da demanda: [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0005/QA/NXG-MEL-0005 Infraestrutura em infra/01 - Demanda#^c1|C1]] a [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0005/QA/NXG-MEL-0005 Infraestrutura em infra/01 - Demanda#^c7|C7]].
- `docker compose -f infra/docker-compose.yml config`, `-f infra/docker-compose.staging.yml config` e `-f infra/docker-compose.prod.yml config` validam sem erro.
- `git status -sb` mostra apenas os arquivos deste escopo como novas alterações, sobre o baseline protegido.

### Testes desta etapa

- **Configuração:** `docker compose ... config` nos 3 ambientes (sem subir containers).
- **Regressão de escopo:** `git status -sb` antes/depois, comparado arquivo a arquivo.
- **Grep de caminho antigo:** confirmar que nenhuma referência a `docker-compose.*.yml` sem o prefixo `infra/` sobra nos 4 arquivos de referência.
