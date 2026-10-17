---
prioridade: media
status: execucao
tipo: melhoria
etapa_atual: "DEV · Análise técnica"
modulo: agentes
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
pontos_alocados: 10
---

# NXG-MEL-0007 — Agentes especializados

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** ainda não criada — gate QA aprovado (`QA_READY_FOR_DEV`), execução sendo aberta nesta tarefa

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** `nxgest`


> [!info] Status atual
> **Resultado:** gate de integridade QA aprovado — `QA_READY_FOR_DEV` emitido em 17/10/2026.
> **Próximo passo:** execução DEV sendo aberta nesta tarefa, com autorização explícita do Orquestrador.

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> **Capacidade alocada:** 10 pontos (~< 2h), estimado para criar 2 arquivos de agente + 1 ajuste pontual em `AGENTS.md`, sem tocar código, infraestrutura ou ambiente.
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

O NX Gest hoje tem 2 agentes especializados em `.opencode/agents/` (`docs-sync.md` — documentação, e `ops-runner.md` — operação/produção), cada um com permissões escopadas ao seu propósito. Falta um agente de **produto** (planejamento de features/planos, espelhando SKILL-003/SKILL-004) e um agente de **QA/qualidade** (revisão, espelhando SKILL-005/006/007/008) — hoje essas atividades só existem como skills de documentação (`docs/skills/`), sem um subagente dedicado com permissões próprias no runtime.

---

## Objetivo

Formalizar `.opencode/agents/product-planner.md` e `.opencode/agents/qa-reviewer.md`, cada um com permissões escopadas ao seu propósito, seguindo exatamente o mesmo padrão estrutural de `docs-sync.md`/`ops-runner.md` (frontmatter `description`/`mode`/`permission`, corpo com Contexto/Tarefas suportadas/Regras), sem duplicar o conteúdo de `AGENTS.md`.

### Entrega desta capacidade

Entrega: os 2 arquivos de agente completos + um ajuste pontual em `AGENTS.md` (seção "Agentes do projeto") caso os critérios de ausência de duplicação exijam uma referência explícita aos 2 novos nomes. Fica fora: qualquer mudança de comportamento de código, infraestrutura, scripts de deploy ou ambiente.

---

## Decisões de produto

- `product-planner`: planejamento de features e planos (`PLAN-NNN`), espelhando `SKILL-003 — Feature Planner` e `SKILL-004 — Vertical Slice Builder`. Permissão de escrita escopada a `docs/plans/**`; leitura ampla; sem acesso a `webfetch`/`websearch` (mesmo padrão dos 2 agentes existentes).
- `qa-reviewer`: revisão de qualidade e CTs, espelhando `SKILL-005 — Code Reviewer`, `SKILL-006 — Bug Investigator`, `SKILL-007 — UX Reviewer` e `SKILL-008 — Release Reviewer`. Somente leitura (sem `edit`/`write`), com `bash` liberado para auditorias e testes (`npm run docs:audit`, `audit:links`, `test`) e `ask` para o restante.
- Nenhum dos dois agentes repete o contexto geral do projeto (stack, produção, comandos) já descrito em `AGENTS.md` — cada um só documenta seu próprio escopo e remete a `AGENTS.md`/`docs/skills/` para o resto, seguindo o princípio já usado por `docs-sync.md`/`ops-runner.md`.
- `AGENTS.md` permanece o contrato global único; não recebe o detalhamento operacional dos novos agentes, só uma referência (já existe a frase "Subagentes customizados (se existirem) ficam em `.opencode/agents/`" — avaliar na execução DEV se basta ou se precisa nomear os agentes explicitamente).
- Este lote não altera código, infraestrutura, `.env` ou scripts de deploy — e não é aplicado ao repositório NX Gest nesta etapa de QA.

---

## Escopo

- Criar `.opencode/agents/product-planner.md` com frontmatter (`description`, `mode: subagent`, `permission` escopada) e corpo (Contexto, Tarefas suportadas, Regras).
- Criar `.opencode/agents/qa-reviewer.md` com a mesma estrutura, permissões read-only.
- Revisar `AGENTS.md` e atualizar a seção "Agentes do projeto" somente se necessário para evitar ambiguidade (sem duplicar regras).
- Validar que nenhum dos 2 agentes duplica conteúdo de `AGENTS.md`, `docs-sync.md` ou `ops-runner.md`.

---

## Fora de escopo

- Alterar código em `src/`/`frontend/`, infraestrutura (`infra/`), `.env` ou scripts de deploy.
- Implementar a lógica/comportamento real dos agentes além da definição declarativa (frontmatter + instruções em Markdown) — não há código executável a escrever.
- Criar execução DEV nesta tarefa — só a criação do pacote QA.
- Aplicar qualquer mudança no repositório NX Gest nesta etapa de QA.

---

## Critérios de aceite

- C1. `.opencode/agents/product-planner.md` existe, com `description`, `mode: subagent` e `permission` escopada (leitura ampla, escrita restrita a `docs/plans/**`, sem `webfetch`/`websearch`), seguindo o mesmo formato estrutural de `docs-sync.md`/`ops-runner.md`. ^c1
- C2. `.opencode/agents/qa-reviewer.md` existe, com `description`, `mode: subagent` e `permission` somente leitura (`edit: deny`, `write: deny`, `bash` liberado só para auditorias/testes). ^c2
- C3. As permissões de cada agente são coerentes com seu propósito declarado (nenhum dos dois tem permissão mais ampla do que o necessário). ^c3
- C4. Nenhum dos 2 agentes duplica o conteúdo de `AGENTS.md` (contexto do projeto, produção, comandos gerais) — cada um só documenta seu próprio escopo. ^c4
- C5. `AGENTS.md` continua coerente com os novos agentes (referência à pasta `.opencode/agents/`, sem detalhar regras internas de cada um). ^c5
- C6. Nenhuma alteração em código, `infra/`, `.env` ou scripts de deploy. ^c6
- C7. Todos os links internos do pacote QA resolvem; nenhuma mudança é aplicada ao repositório NX Gest nesta etapa de criação do pacote QA. ^c7

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
- Confirmar, na execução DEV, se `AGENTS.md` precisa mesmo de edição (C5) ou se a frase genérica já existente é suficiente.
