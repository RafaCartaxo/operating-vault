---
prioridade: alta
status: concluido
modulo: processo
plano: ""
execucao: ""
ambiente: dev
origem: conversa
projeto: nxgest
epico: NXG-EPIC-0001
pai: ""
data_inicio: "2026-10-17"
data_fim: "2026-11-10"
responsavel: "NX Gest · QA e Coordenação"
---

# NXG-028 — Governança da reorganização do NX Gest

> [!info] Informações
> - **Tipo:** plano de organização e governança técnica
> - **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|NXG-EPIC-0001 — Organização do NX Gest]]
> - **Responsável:** NX Gest · QA e Coordenação, com execução delegada ao NX Gest · DEV
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
- `agents/` na raiz passa a ser a fonte canônica neutra de contratos de agente (`agents/README.md` como índice + `docs-sync.md`/`ops-runner.md`/`product-planner.md`/`qa-reviewer.md`, sem frontmatter nem schema de permissão de plataforma). `.opencode/agents/` deixou de ser a fonte canônica e foi removido no lote NXG-MEL-0007, após gate QA próprio; histórico preservado nos registros arquivados.
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
│   ├── Dockerfile
│   ├── Caddyfile
│   ├── docker-compose.yml
│   ├── docker-compose.staging.yml
│   └── docker-compose.prod.yml
├── src/
├── frontend/
├── docs/
└── scripts/
```

`.opencode/` já foi removido do repositório no `NXG-MEL-0007` (17/10) — `agents/` é a fonte canônica de contratos de agente, independente de plataforma.

Os exemplos de ambiente permanecem inicialmente na raiz para preservar o onboarding `cp .env.example .env`; sua eventual migração para `infra/env/` exige demanda própria e atualização explícita do carregamento.

## Lotes governados

1. **NXG-MEL-0004 — README e mapa da raiz:** alteração documental isolada.
2. **NXG-MEL-0005 — infraestrutura:** agrupar Dockerfile, Caddyfile e compose em `infra/` com paths validados. ✅ Concluído com ressalva (17/10) — infraestrutura movida localmente, nenhum deploy real ainda; arquivado em `05 Arquivo/Nxgest/Melhorias/NXG-MEL-0005/`.
3. **NXG-MEL-0006 — onboarding:** encapsular comandos docker de dev em scripts npm e atualizar README/08-SETUP-NOVA-MAQUINA.md para `infra/docker-compose.yml`. ✅ Concluído com ressalva (17/10) — arquivado em `05 Arquivo/Nxgest/Melhorias/NXG-MEL-0006/`.
4. **NXG-MEL-0007 — agentes:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0007/QA/NXG-MEL-0007 Agentes especializados/01 - Demanda|NXG-MEL-0007]] — governança de agentes independente de plataforma — fonte canônica neutra em `agents/` (`agents/README.md` + `docs-sync.md`/`ops-runner.md`/`product-planner.md`/`qa-reviewer.md`), sem frontmatter/schema do OpenCode; `.opencode/` removido do repositório. ✅ Concluído (17/10) — implementação em [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0007/DEV/NXG-MEL-0007/00 README|execução NXG-MEL-0007 Agentes neutros]], QA aprovou os 7 CTs, lote arquivado em `05 Arquivo/Nxgest/Melhorias/NXG-MEL-0007/`. A execução anterior (escopo OpenCode) permanece obsoleta em `03 Trabalho/DEV/Nxgest/Execuções/`.
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
| Inconsistência entre planos (`PLAN-084-organizacao-repositorio.md` tratava `.opencode/agents/**` como parte permanente do pacote de distribuição) | Mitigado: `PLAN-084` foi atualizado na implementação do `NXG-MEL-0007` (nota datada de 17/10 + seção "Classificação do repositório" ajustada para `agents/**`); não é mais uma ação futura |

## Critérios de aceite do plano

- C1. A estratégia incremental e os lotes estão registrados com dependências e rollback.
- C2. Cada lote que altera o repositório possui melhoria filha, critérios e CTs próprios.
- C3. O trabalho não commitado é preservado antes de qualquer lote estrutural.
- C4. A arquitetura-alvo distingue raiz, infra, docs, scripts, agentes e ambientes.
- C5. O plano não autoriza exposição de segredos nem alteração automática da infraestrutura real.
- C6. O épico e as demandas vinculadas permanecem sincronizados com os boards QA/DEV.

## Pendências de decisão

- Resolvida na consolidação: infra/ com cinco arquivos diretos; um .env.example na raiz; diferenças nos guias existentes.
- Resolvida em 2026-11-07: recuperação conferida e branch WIP para ícones/Qase; commits locais por dependências.
- ~~Validar o novo gate de integridade de `NXG-MEL-0007` e decidir se/quando autorizar sua execução DEV.~~ Resolvida: gate aprovado, execução DEV concluída, QA aprovou os 7 CTs, lote arquivado (17/10).
- ~~`PLAN-084-organizacao-repositorio.md` trata `.opencode/agents/**` como parte permanente do pacote de distribuição.~~ Resolvida: `PLAN-084` atualizado na implementação DEV do `NXG-MEL-0007` (nota datada + classificação do repositório ajustada para `agents/**`).
- Regra histórica atendida: execução NXG-MEL-0005 ocorreu após gate NXG-MEL-0006; não é autorização pendente atual.

## Definição de pronto

- [x] Arquitetura-alvo aprovada — `agents/` canônico implementado e validado (`NXG-MEL-0007`).
- [x] Lotes e dependências registrados — 1 a 5 registrados acima, com sequência e dependências explícitas.
- [x] Melhorias filhas vinculadas ao épico — `NXG-MEL-0004`, `0005`, `0006` e `0007` vinculadas e arquivadas.
- [x] Boards e links sincronizados — Boards QA/DEV e épico refletem os 4 lotes concluídos e arquivados.
- [x] Nenhuma decisão bloqueante omitida — consolidação, commits locais, validação e sincronização concluídos. Parecer final apresentado para decisão do usuário; push/deploy e encerramento do épico não executados.

## Execução complementar autorizada — 2026-11-07

O usuário autorizou avançar até o parecer final, com decisões e delegação; implementação, registros, validação e commits locais permitidos. Push, deploy e encerramento do épico permanecem fora do escopo. Responsáveis atuais: NX Gest · QA e Coordenação e NX Gest · DEV. A estrutura implementada é infra/ com cinco arquivos; exemplos serão consolidados em .env.example, com diferenças nos guias existentes, após validação. Pendências redigidas acima como futuras representam o histórico; a estratégia de commits e prova integrada serão consolidadas nesta rodada.

- [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/QA/NXG-MEL-0008 Consolidacao de ambientes e portabilidade/00 README|NXG-MEL-0008 Consolidacao de ambientes e portabilidade]]
- [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/00 README|NXG-029 Staging carrega valores com espacos]]
- [[05 Arquivo/Nxgest/Bugs/NXG-030/QA/NXG-030 Smoke protege banco e interpreta opcoes/00 README|NXG-030 Smoke protege banco e interpreta opcoes]]

### Inventário protegido e decisões de preservação

- Contagem exata no manifesto inicial: 45 caminhos rastreados + 20 novos (65 entradas). A referência histórica a 22 novos estava imprecisa.
- Recuperação local restrita em `.maestro/nxgest-team/recovery/2026-11-07/`: patch binário, arquivos novos, hashes/modos e restauração conferida; não inclui envs reais ou dados ignorados.
- Ícones NXG-006 e `scripts/qase-sync.mjs` preservados em `14f3e50` na branch local `wip/nxg-preservacao-icones-qase-20261107`. QA confirmou os oito arquivos contra a recuperação. São WIP, não entrega aprovada. Qase permanece pendente de revisão/escopo próprio e não foi executado.
- Documento/CEP e chevrons possuem registros históricos em MEL-0001/0002/0003; a organização de commits não substitui essas aprovações nem reabre os lotes.

## Resultado da consolidação — 2026-11-07

Parecer técnico favorável local, com limites registrados em [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/01 Parecer final|Parecer final]]. Repo definitivo `nxgest/`, HEAD `c7b65c8ddd85efde4db7f075ca03d95a7c6c5c38`; working tree limpo, sete commits locais além de origin/main. Pacotes NXG-MEL-0008/NXG-029/NXG-030 aprovados e arquivados; treze CTs. Rename preservou identidade do diretório e metadados do env real sem ler valores. Recursos temporários removidos; original saudável. Plano e épico concluídos após aceite do usuário em 2026-11-07.

## Aceite e encerramento — 2026-11-07

O usuário aceitou o parecer e determinou: “Finalizemos a demanda”, confirmando entendimento do plano. Encerramento da organização local autorizado em 2026-11-07, reconfirmado e formalizado nos registros em 2026-11-10. Não há impedimento técnico identificado no ambiente validado. Ressalvas documentais e de abrangência de teste permanecem registradas, com encaminhamentos próprios. A decisão não autoriza push/deploy nem encerra os trabalhos separados de ícones/Qase.

Governança concluída. Não há decisão bloqueante pendente nesta demanda. Publicação e implantação dependem de autorização separada.

## Conferência de encerramento — 2026-11-10

Aceite do usuário reconfirmado e registro concluído nesta data. HEAD permanece `c7b65c8ddd85efde4db7f075ca03d95a7c6c5c38`; árvore de código limpa e sem alteração desde a revisão validada. Não foi necessário repetir testes para esta atualização exclusivamente documental. Nenhum impedimento novo identificado; publicação segue fora do escopo.
