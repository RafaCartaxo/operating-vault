# 02 - Plano de execução (NXG-MEL-0006)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0006 Onboarding de ambientes/01 - Demanda|NXG-MEL-0006 — Onboarding de ambientes]]  
> **Plano técnico:** não se aplica — lote de organização, sem `PLAN-NNN` próprio  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0006 Onboarding de ambientes/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Encapsular o comando de banco de desenvolvimento em scripts npm e atualizar `README.md`/`08-SETUP-NOVA-MAQUINA.md` para usá-los, sem tocar `infra/` novamente.

---

## Vínculo e sequência

1. `package.json`: adicionar `"db:up"`, `"db:down"`, `"db:ps"` usando `docker compose --project-directory . -f infra/docker-compose.yml ...`.
2. `README.md`: trocar `docker compose up -d postgres` (Instalação Rápida) por `npm run db:up`.
3. `docs/engineering/08-SETUP-NOVA-MAQUINA.md`: trocar, no Passo 4, `docker compose up -d postgres` por `npm run db:up` e `docker compose ps` por `npm run db:ps`.
4. Validar de verdade: `npm run db:up` (sobe o Postgres de dev), `npm run db:ps` (confirma saudável), `npm run db:down` (derruba, sem deixar efeito persistente).

---

## Escopo aprovado

- **Pode mudar:** `package.json` (só a seção `scripts`), `README.md` (só a seção "Instalação Rápida"), `docs/engineering/08-SETUP-NOVA-MAQUINA.md` (só o Passo 4).
- **Deve permanecer intacto:** `infra/` (não tocar novamente — já validado no `NXG-MEL-0005`), `scripts/deploy.sh`, `scripts/deploy-staging.sh`, `.opencode/agents/ops-runner.md`, `docs/engineering/06-PRODUCAO.md` (já tratados no lote anterior), `.env*`, código em `src/`/`frontend/`, e os 27 arquivos modificados + 10 untracked já existentes.

---

## Decisões

- Nomes dos scripts: `db:up`/`db:down`/`db:ps` (`ps` incluído para cobrir o 2º comando do Passo 4 do guia de setup, mantendo o par comando-documentação completo).

---

## Pronto quando

- Critérios da demanda: [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0006 Onboarding de ambientes/01 - Demanda#^c1|C1]] a [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0006 Onboarding de ambientes/01 - Demanda#^c7|C7]].
- `npm run db:up` sobe o Postgres de dev de verdade; `npm run db:ps` confirma saudável; `npm run db:down` derruba sem erro.
- `git status -sb` mostra apenas os 3 arquivos deste escopo como novas alterações, sobre o baseline já atualizado pelo `NXG-MEL-0005`.

### Testes desta etapa

- **Funcional real (não simulado):** `npm run db:up` → `npm run db:ps` → `npm run db:down`, local, reversível, sem tocar staging/produção.
- **Documental:** leitura de `README.md`/`08-SETUP-NOVA-MAQUINA.md` confirmando o novo comando.
- **Regressão de escopo:** `git status -sb` antes/depois.
