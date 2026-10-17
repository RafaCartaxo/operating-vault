---
prioridade: alta
status: analise
modulo: processo
plano: ""
execucao: ""
ambiente: dev
origem: conversa
projeto: nxgest
epico: NXG-EPIC-0001
pai: ""
data_inicio: "2026-10-17"
data_fim: ""
responsavel: ""
---

# NXG-028 — Governança da reorganização do NX Gest

> [!info] Informações
> - **Tipo:** plano de organização e governança técnica
> - **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|NXG-EPIC-0001 — Organização do NX Gest]]
> - **Responsável:** Orquestrador, com execução delegada ao Claude
> - **Plano técnico relacionado:** decisões de arquitetura e migração da estrutura do repositório

## Problema / contexto

O NX Gest funciona, mas a organização visual e conceitual de raiz, infraestrutura, ambientes, agentes e onboarding ainda pode ser melhorada. Existem arquivos legítimos na raiz, configurações de diferentes ambientes, convenções históricas de `nxgestao` e trabalho não commitado que precisam ser preservados durante a melhoria.

## Objetivo

Definir e governar uma arquitetura organizacional clara para o NX Gest, permitindo executar lotes reversíveis que mantenham o comportamento atual, reduzam ambiguidade e facilitem o clone em qualquer computador.

## Decisões de organização

- A Estratégia A — reorganização incremental no repositório atual — é a estratégia principal.
- `nxgest` é o nome canônico do produto, repositório e referências novas.
- `nxgestao` permanece apenas em compatibilidade de infraestrutura real ou histórico legítimo.
- `AGENTS.md` permanece na raiz como contrato global.
- `agents/` na raiz passa a ser a fonte canônica neutra de contratos de agente (`agents/README.md` como índice + `docs-sync.md`/`ops-runner.md`/`product-planner.md`/`qa-reviewer.md`, sem frontmatter nem schema de permissão de plataforma). `.opencode/agents/` deixa de ser a fonte canônica e será removido do repositório somente em uma etapa DEV futura, após gate QA próprio para essa remoção (ver `NXG-MEL-0007`).
- Os arquivos reais de ambiente nunca são versionados nem expostos.
- Para CTs de organização/documentação deste épico, `Camada: manual` representa a verificação humana do processo e `Automação: manual` representa sua execução; a divergência geral da taxonomia do Vault fica registrada para melhoria futura.
- A infraestrutura pode ser agrupada em `infra/` quando o lote tiver paths, scripts e validações atualizados.
- Volumes, redes, domínios e diretórios reais de staging/produção não serão renomeados automaticamente.
- Nenhum lote estrutural deve absorver silenciosamente os 26 arquivos modificados e 10 untracked existentes no repositório.
- Regra de sequência: nenhuma execução real do `NXG-MEL-0005` ocorre antes de `NXG-MEL-0006` estar criado e com gate QA aprovado — evita que o comando de onboarding (`docker compose up -d postgres`) fique quebrado entre os dois lotes.

## Arquitetura-alvo conceitual

```text
nxgest/
├── AGENTS.md
├── agents/
│   ├── README.md
│   ├── docs-sync.md
│   ├── ops-runner.md
│   ├── product-planner.md
│   └── qa-reviewer.md
├── README.md
├── package.json / package-lock.json
├── tsconfig.json / vitest.config.ts / .nvmrc
├── .github/
├── infra/
│   ├── docker/
│   ├── caddy/
│   └── env/ (somente exemplos, se aprovado)
├── src/
├── frontend/
├── docs/
└── scripts/
```

`.opencode/` sai do repositório em uma etapa DEV futura, após o gate QA de `NXG-MEL-0007` ser aprovado especificamente para essa remoção — não faz parte da arquitetura-alvo final.

Os exemplos de ambiente permanecem inicialmente na raiz para preservar o onboarding `cp .env.example .env`; sua eventual migração para `infra/env/` exige demanda própria e atualização explícita do carregamento.

## Lotes governados

1. **NXG-MEL-0004 — README e mapa da raiz:** alteração documental isolada.
2. **NXG-MEL-0005 — infraestrutura:** agrupar Dockerfile, Caddyfile e compose em `infra/` com paths validados. ✅ Concluído com ressalva (17/10) — infraestrutura movida localmente, nenhum deploy real ainda.
3. **NXG-MEL-0006 — onboarding:** encapsular comandos docker de dev em scripts npm e atualizar README/08-SETUP-NOVA-MAQUINA.md para `infra/docker-compose.yml`. ✅ Concluído com ressalva (17/10) — arquivado em `05 Arquivo/Nxgest/Melhorias/NXG-MEL-0006/`.
4. **NXG-MEL-0007 — agentes:** tornar a governança de agentes independente de plataforma — fonte canônica neutra em `agents/` (`agents/README.md` + `docs-sync.md`/`ops-runner.md`/`product-planner.md`/`qa-reviewer.md`), sem frontmatter/schema do OpenCode; `.opencode/` só sai do repositório numa etapa DEV futura, com gate próprio. 🔁 Em revisão de QA (17/10) — pacote retornado para análise; o gate anterior (`QA_READY_FOR_DEV`, escopo `.opencode/agents/`) foi invalidado por esta revisão e a execução DEV aberta para esse escopo foi marcada obsoleta.
5. **Renomeação local:** `nxgestao` → `nxgest`, registrada como decisão operacional, não como alteração do repositório.

## Riscos e controles

| Risco | Controle |
|---|---|
| Perda de trabalho não commitado | preservar estado antes de lote estrutural |
| Quebra de compose/deploy | validar `docker compose config`, paths e scripts antes de staging |
| Exposição de segredo | confirmar `git ls-files` e `.gitignore`/`.dockerignore` |
| Divergência de nomenclatura | usar `nxgest` em referências novas; preservar compatibilidade justificada |
| Documentação contraditória | executar auditorias de links e documentação |
| Mistura com produção | não alterar VPS, volumes, redes ou domínios neste épico sem autorização |
| Inconsistência entre planos (`PLAN-084-organizacao-repositorio.md` trata `.opencode/agents/**` como parte permanente do pacote de distribuição) | registrar `PLAN-084` como referência ativa a atualizar na implementação DEV do `NXG-MEL-0007`; não editar o `PLAN-084` agora |

## Critérios de aceite do plano

- C1. A estratégia incremental e os lotes estão registrados com dependências e rollback.
- C2. Cada lote que altera o repositório possui melhoria filha, critérios e CTs próprios.
- C3. O trabalho não commitado é preservado antes de qualquer lote estrutural.
- C4. A arquitetura-alvo distingue raiz, infra, docs, scripts, agentes e ambientes.
- C5. O plano não autoriza exposição de segredos nem alteração automática da infraestrutura real.
- C6. O épico e as demandas vinculadas permanecem sincronizados com os boards QA/DEV.

## Pendências de decisão

- Confirmar, no lote estrutural, a forma final de `infra/docker`, `infra/caddy` e exemplos de ambiente.
- Definir quando o trabalho não commitado será preservado.
- Validar o novo gate de integridade de `NXG-MEL-0007` (arquitetura neutra de agentes) e decidir se/quando autorizar sua execução DEV.
- `PLAN-084-organizacao-repositorio.md` trata `.opencode/agents/**` como parte permanente do pacote de distribuição — será atualizado na implementação DEV do `NXG-MEL-0007`, não nesta revisão.
- Autorizar a execução DEV do `NXG-MEL-0005` somente após `NXG-MEL-0006` ter gate QA aprovado (regra de sequência).

## Definição de pronto

- [ ] Arquitetura-alvo aprovada.
- [ ] Lotes e dependências registrados.
- [ ] Melhorias filhas vinculadas ao épico.
- [ ] Boards e links sincronizados.
- [ ] Nenhuma decisão bloqueante omitida.
