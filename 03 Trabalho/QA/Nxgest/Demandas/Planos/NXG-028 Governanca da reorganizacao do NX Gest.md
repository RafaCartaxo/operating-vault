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
- `.opencode/agents/` permanece como espaço de agentes especializados.
- Os arquivos reais de ambiente nunca são versionados nem expostos.
- Para CTs de organização/documentação deste épico, `Camada: manual` representa a verificação humana do processo e `Automação: manual` representa sua execução; a divergência geral da taxonomia do Vault fica registrada para melhoria futura.
- A infraestrutura pode ser agrupada em `infra/` quando o lote tiver paths, scripts e validações atualizados.
- Volumes, redes, domínios e diretórios reais de staging/produção não serão renomeados automaticamente.
- Nenhum lote estrutural deve absorver silenciosamente os 26 arquivos modificados e 10 untracked existentes no repositório.

## Arquitetura-alvo conceitual

```text
nxgest/
├── AGENTS.md
├── README.md
├── package.json / package-lock.json
├── tsconfig.json / vitest.config.ts / .nvmrc
├── .github/
├── .opencode/agents/
├── infra/
│   ├── docker/
│   ├── caddy/
│   └── env/ (somente exemplos, se aprovado)
├── src/
├── frontend/
├── docs/
└── scripts/
```

Os exemplos de ambiente permanecem inicialmente na raiz para preservar o onboarding `cp .env.example .env`; sua eventual migração para `infra/env/` exige demanda própria e atualização explícita do carregamento.

## Lotes governados

1. **NXG-MEL-0004 — README e mapa da raiz:** alteração documental isolada.
2. **NXG-MEL-0005 — infraestrutura:** agrupar Dockerfile, Caddyfile e compose em `infra/` com paths validados. Pacote QA criado em 17/10, aguardando gate de integridade e autorização para execução DEV.
3. **MEL-0006 — onboarding:** encapsular comandos de ambiente e atualizar setup de clone.
4. **MEL-0007 — agentes:** formalizar agentes de produto/QA apenas se a decisão for aprovada.
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
- Decidir se agentes de produto/QA serão formalizados.

## Definição de pronto

- [ ] Arquitetura-alvo aprovada.
- [ ] Lotes e dependências registrados.
- [ ] Melhorias filhas vinculadas ao épico.
- [ ] Boards e links sincronizados.
- [ ] Nenhuma decisão bloqueante omitida.
