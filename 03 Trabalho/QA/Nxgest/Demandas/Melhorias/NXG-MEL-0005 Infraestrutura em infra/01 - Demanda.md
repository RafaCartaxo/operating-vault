---
prioridade: alta
status: analise
tipo: melhoria
etapa_atual: "QA · Casos de teste"
modulo: infraestrutura
plano: "[[03 Trabalho/QA/Nxgest/Demandas/Planos/NXG-028 Governanca da reorganizacao do NX Gest|NXG-028]]"
execucao: ""
ambiente: dev
origem: conversa
projeto: nxgest
epico: NXG-EPIC-0001
pai: ""
data_inicio: ""
data_fim: ""
responsavel: ""
pontos_alocados: 20
---

# NXG-MEL-0005 — Infraestrutura em infra/

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** ainda não criada — gate QA aprovado (`QA_READY_FOR_DEV`), aguardando NXG-MEL-0006 (regra de sequência do NXG-028)

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** `nxgest`


> [!info] Status atual
> **Resultado:** gate de integridade QA aprovado — `QA_READY_FOR_DEV` emitido em 17/10/2026.
> **Próximo passo:** aguardar `NXG-MEL-0006` ser criado e ter seu gate QA aprovado (regra de sequência do NXG-028) antes de abrir a execução DEV deste lote.

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> **Capacidade alocada:** 20 pontos (~< 4h), estimado para mover 5 arquivos de infraestrutura e atualizar 4 pontos de referência (2 scripts + 2 documentos), sem alterar comportamento.
>
> ```dataviewjs
> const id = (dv.current().file.path.match(/(?:[A-Z]{2,8}-)?MEL-\d+/) || [""])[0];
> const paginas = dv.pages().where(p => id && p.file.path.includes(id) && typeof p.pontos === "number");
> const lista = paginas.sort(p => p.file.name);
> const necessario = lista.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> const alocado = Number(dv.current().pontos_alocados || 0);
> const diferenca = alocado - necessario;
> if (lista.length > 0) {
>   dv.table(["Etapa/artefato", "Pontos"], lista.map(p => [p.file.link, p.pontos]));
> } else {
>   dv.paragraph("Nenhum artefato com pontos registrado ainda.");
> }
> dv.paragraph(`**Esforço necessário:** ${necessario} pontos · **Capacidade alocada:** ${alocado} pontos · **${diferenca >= 0 ? "Saldo" : "Déficit"}:** ${Math.abs(diferenca)} pontos`);
> ```

---

## Problema / contexto

A raiz do NX Gest mantém `Dockerfile`, `Caddyfile` e os 3 `docker-compose.{yml,staging.yml,prod.yml}` soltos, misturados com configuração de ferramenta, código e documentação. O diagnóstico e o plano de governança ([[03 Trabalho/QA/Nxgest/Demandas/Planos/NXG-028 Governanca da reorganizacao do NX Gest|NXG-028]]) já confirmaram, por leitura integral dos scripts de deploy e dos workflows de CI/CD, que mover esses 5 arquivos para `infra/` é tecnicamente seguro (nenhum workflow de CI/CD referencia path de compose diretamente) e que `docker compose` lê o `.env` do diretório de trabalho da chamada, não do diretório do arquivo — logo mover os compose não exige mover os `.env`.

---

## Objetivo

Agrupar `Dockerfile`, `Caddyfile` e os 3 `docker-compose.{yml,staging.yml,prod.yml}` em `infra/`, atualizando exatamente os pontos de referência que apontam para eles (scripts de deploy e documentação operacional), sem alterar nomes de volumes, redes, containers ou qualquer comportamento real de staging/produção.

### Entrega desta capacidade

Entrega: os 5 arquivos fisicamente em `infra/`, com `scripts/deploy.sh`, `scripts/deploy-staging.sh`, `.opencode/agents/ops-runner.md` e `docs/engineering/06-PRODUCAO.md` atualizados para o novo caminho. Fica fora desta entrega: qualquer mudança no comando de onboarding de desenvolvimento (`docker compose up -d postgres` no README/`08-SETUP-NOVA-MAQUINA.md`) — isso é escopo do próximo lote (`NXG-MEL-0006 — onboarding`, conforme NXG-028), para não acoplar as duas mudanças num único diff.

---

## Decisões de produto

- `infra/` passa a ser o diretório oficial para definição de infraestrutura/containers (Dockerfile, Caddyfile, docker-compose).
- Nenhum nome real de volume (`nxgestao_data`, `nxgestao_pgdata`, `nxgestao_staging_data`, `nxgestao_staging_pgdata`), rede (`nxgestao_net`) ou container (`nxgest-postgres`, `nxgest-pg-dev`, `staging-app`, `staging-pg`) é alterado — são recursos Docker reais já em produção.
- Os 3 arquivos `.env*.example` continuam na raiz (não entram em `infra/env/`), preservando `cp .env.example .env` sem mudança de instrução.
- Este lote não altera código de aplicação, não faz deploy e não é aplicado ao repositório NX Gest nesta etapa de QA — a execução DEV só começa com autorização explícita do Orquestrador.

---

## Escopo

- Mover `Dockerfile`, `Caddyfile`, `docker-compose.yml`, `docker-compose.staging.yml` e `docker-compose.prod.yml` para `infra/`.
- Atualizar o volume do Caddyfile e o contexto de build do Dockerfile dentro dos 3 `docker-compose*.yml` para os novos caminhos relativos.
- Atualizar `scripts/deploy.sh` e `scripts/deploy-staging.sh` (flag `-f infra/docker-compose.*.yml`).
- Atualizar `.opencode/agents/ops-runner.md` e `docs/engineering/06-PRODUCAO.md` (comandos `docker compose -f ...` documentados).

---

## Fora de escopo

- Alterar o comando de onboarding de desenvolvimento (`README.md`/`08-SETUP-NOVA-MAQUINA.md`) — fica para `NXG-MEL-0006`.
- Mover `.env`, `.env.example` ou qualquer variante de ambiente.
- Renomear volumes, redes, containers ou qualquer recurso real de staging/produção.
- Criar ou reorganizar agentes (`NXG-MEL-0007`).
- Executar deploy real em staging ou produção.
- Aplicar qualquer mudança no repositório NX Gest nesta etapa — isso só ocorre na execução DEV, após gate QA aprovado e autorização explícita.

---

## Critérios de aceite

- C1. `Dockerfile`, `Caddyfile` e os 3 `docker-compose.{yml,staging.yml,prod.yml}` existem em `infra/` e não existem mais na raiz do repositório. ^c1
- C2. Os 3 `docker-compose*.yml` em `infra/` validam sem erro de caminho (`docker compose -f infra/docker-compose*.yml config`), com o volume do Caddyfile e o contexto de build do Dockerfile corretamente ajustados. ^c2
- C3. `scripts/deploy.sh` e `scripts/deploy-staging.sh` referenciam `infra/docker-compose.prod.yml` e `infra/docker-compose.staging.yml`, respectivamente, sem nenhum caminho antigo remanescente. ^c3
- C4. `.opencode/agents/ops-runner.md` e `docs/engineering/06-PRODUCAO.md` refletem os novos caminhos dos comandos `docker compose -f ...`, sem instrução desatualizada. ^c4
- C5. Os nomes reais de volumes, rede e containers permanecem idênticos aos atuais de staging/produção — nenhuma migração de dado é exigida. ^c5
- C6. `.env.example`, `.env.production.example` e `.env.staging.example` continuam na raiz do repositório. ^c6
- C7. Nenhum segredo é exposto e o repositório NX Gest não é alterado nesta etapa de criação do pacote QA — qualquer mudança real só ocorre na execução DEV, após autorização explícita. ^c7

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Gate QA aprovado e `QA_READY_FOR_DEV` já emitido (17/10/2026) — nenhuma pendência de validação de integridade.
- Aguardar `NXG-MEL-0006` ser criado e ter seu gate QA aprovado (regra de sequência do NXG-028) antes de abrir a execução DEV deste lote.
