---
prioridade: alta
status: concluido
tipo: melhoria
etapa_atual: "Concluído"
modulo: onboarding
plano: "[[03 Trabalho/QA/Nxgest/Demandas/Planos/NXG-028 Governanca da reorganizacao do NX Gest|NXG-028]]"
execucao: "[[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0006/DEV/NXG-MEL-0006/00 README|Execução NXG-MEL-0006]]"
ambiente: dev
origem: conversa
projeto: nxgest
epico: NXG-EPIC-0001
pai: ""
data_inicio: ""
data_fim: "2026-10-17"
responsavel: ""
pontos_alocados: 10
---

# NXG-MEL-0006 — Onboarding de ambientes

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0006/DEV/NXG-MEL-0006/00 README|Execução NXG-MEL-0006]] — concluída, aguardando QA

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** `nxgest`


> [!info] Status atual
> **Resultado:** QA aprovado com ressalva (17/10/2026) — CTs C1–C7 atendidos. Ressalva de limitação de ambiente (permissão do socket Docker para reexecução independente), não um defeito — ver [[04 - Validação dev]].
> **Próximo passo:** nenhum — lote concluído e arquivado.

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> **Capacidade alocada:** 10 pontos (~< 2h), estimado para 1 adição em `package.json` (scripts npm) e 2 ajustes de documentação (`README.md`, `08-SETUP-NOVA-MAQUINA.md`), sem alterar comportamento de staging/produção.
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

O lote `NXG-MEL-0005` (já com gate QA aprovado) move `docker-compose.yml` da raiz para `infra/`. Sem este lote complementar, o comando de onboarding documentado hoje (`docker compose up -d postgres`, em `README.md` e `docs/engineering/08-SETUP-NOVA-MAQUINA.md`) deixaria de funcionar assim que `NXG-MEL-0005` fosse aplicado — o desenvolvedor precisaria saber manualmente o novo caminho (`-f infra/docker-compose.yml`), quebrando a promessa de clone simples em qualquer computador.

---

## Objetivo

Encapsular os comandos Docker de desenvolvimento em scripts npm (ex.: `db:up`/`db:down`), de forma que o onboarding continue com um único comando simples, independentemente de o compose estar em `infra/` ou na raiz. Atualizar `README.md` e `docs/engineering/08-SETUP-NOVA-MAQUINA.md` para usar esse comando, preservando `cp .env.example .env` e a experiência de clone limpo.

### Entrega desta capacidade

Entrega: `package.json` com script(s) npm que sobem/derrubam o Postgres de desenvolvimento a partir de `infra/docker-compose.yml`; `README.md` e `08-SETUP-NOVA-MAQUINA.md` atualizados para usar o novo comando. Fica fora: qualquer mudança nos scripts de deploy de staging/produção (`scripts/deploy.sh`, `scripts/deploy-staging.sh`) ou em `.opencode/agents/ops-runner.md` — esses já foram tratados em `NXG-MEL-0005`.

---

## Decisões de produto

- O onboarding de desenvolvimento usa um comando npm (ex.: `npm run db:up`) como camada de abstração — o desenvolvedor não precisa saber o caminho físico do `docker-compose.yml`.
- `cp .env.example .env` continua sendo o único passo de configuração de ambiente, sem mudança de instrução.
- Nenhuma mudança em `npm install`, nas dependências do projeto ou no fluxo de build/test.
- Este lote não altera scripts de deploy, agentes ou qualquer comportamento de staging/produção.
- Este lote não é aplicado ao repositório NX Gest nesta etapa de QA — a execução DEV só começa com autorização explícita do Orquestrador, e só depois de `NXG-MEL-0006` (este lote) ter gate QA aprovado, pois `NXG-MEL-0005` depende dele (regra de sequência).

---

## Escopo

- Adicionar script(s) npm em `package.json` (ex.: `db:up`/`db:down`) apontando para `infra/docker-compose.yml`.
- Atualizar a seção "Instalação Rápida" do `README.md` para usar o novo comando no lugar de `docker compose up -d postgres`.
- Atualizar o Passo 4 de `docs/engineering/08-SETUP-NOVA-MAQUINA.md` para o mesmo comando.
- Validar que um clone novo, seguindo o passo a passo atualizado, completa a instalação sem passo manual extra.

---

## Fora de escopo

- Mover Dockerfile, Caddyfile ou docker-compose — isso é escopo de `NXG-MEL-0005`.
- Alterar `scripts/deploy.sh`, `scripts/deploy-staging.sh` ou `.opencode/agents/ops-runner.md`.
- Mover `.env`, `.env.example` ou qualquer variante de ambiente.
- Criar ou reorganizar agentes (`NXG-MEL-0007`).
- Executar deploy real em staging ou produção.
- Aplicar qualquer mudança no repositório NX Gest nesta etapa — isso só ocorre na execução DEV, após gate QA aprovado e autorização explícita.

---

## Critérios de aceite

- C1. `package.json` ganha script(s) npm (ex.: `db:up`/`db:down`) que sobem/derrubam o Postgres de desenvolvimento a partir de `infra/docker-compose.yml`, sem exigir que o desenvolvedor digite o caminho manualmente. ^c1
- C2. `README.md` (seção "Instalação Rápida") usa o novo comando npm no lugar de `docker compose up -d postgres`. ^c2
- C3. `docs/engineering/08-SETUP-NOVA-MAQUINA.md` (Passo 4) é atualizado para o mesmo comando/caminho. ^c3
- C4. `cp .env.example .env` continua sendo o único passo de configuração de ambiente documentado, sem mudança de instrução. ^c4
- C5. Um clone novo em pasta vazia, seguindo o passo a passo atualizado, completa a instalação (`npm install` + novo comando de banco) sem passo manual extra além do documentado. ^c5
- C6. Nenhuma alteração em `scripts/deploy.sh`, `scripts/deploy-staging.sh`, Docker de staging/produção ou segredo. ^c6
- C7. Nenhuma mudança é aplicada ainda no repositório NX Gest nesta etapa de criação do pacote QA — qualquer mudança real só ocorre na execução DEV, após autorização explícita. ^c7

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Nenhuma. Lote concluído com ressalva em 17/10/2026 (ver [[04 - Validação dev]]).
