---
prioridade: media
status: analise
tipo: melhoria
etapa_atual: "QA · Casos de teste"
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
> **Execução DEV:** ainda não criada — aguarda novo gate QA. A execução anterior (escopo OpenCode) foi marcada obsoleta: [[03 Trabalho/DEV/Nxgest/Execuções/NXG-MEL-0007 Agentes especializados/00 README|ver execução obsoleta]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** `nxgest`


> [!info] Status atual
> **Resultado:** pacote QA revisado para a arquitetura neutra de agentes — aguardando nova execução do gate de integridade e aprovação do Orquestrador.
> **Próximo passo:** manter em `QA · Casos de teste` até o novo `validar_pacote_qa.py` ser executado e o pacote ser aprovado; só então considerar `QA_READY_FOR_DEV`.

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> **Capacidade alocada:** 10 pontos (~< 2h) para esta revisão do pacote QA (demanda, plano, CTs, validação, Qase) e atualização de NXG-028/épico/board. A criação real de `agents/`, a migração dos 4 contratos e a remoção de `.opencode/` são escopo de uma implementação DEV futura e serão reestimadas quando essa execução for aberta.
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

O NX Gest hoje tem 2 agentes especializados em `.opencode/agents/` (`docs-sync.md` — documentação, e `ops-runner.md` — operação/produção), cada um com o frontmatter e o schema de permissão específicos do OpenCode (`mode`, `permission`). Falta um agente de **produto** (planejamento de features/planos) e um agente de **QA/qualidade** (revisão). Além disso, amarrar toda a governança de agentes a `.opencode/agents/` torna o NX Gest dependente de uma única plataforma: os mesmos contratos não podem ser reaproveitados por outra ferramenta (Claude Code, Codex, etc.) sem reescrevê-los do zero.

---

## Objetivo

Tornar a governança de agentes do NX Gest independente de plataforma:

```text
AGENTS.md                 contrato global na raiz
agents/
  README.md               índice e regras de uso
  docs-sync.md            contrato neutro de documentação
  ops-runner.md           contrato neutro de operação
  product-planner.md      escrita somente em docs/plans/**
  qa-reviewer.md          somente leitura e revisão
```

`AGENTS.md` continua sendo o contrato global único na raiz. `agents/` passa a ser a fonte canônica neutra, com `agents/README.md` como índice e os 4 contratos descritos por identidade, responsabilidade, entradas/saídas, regras, limites, protocolo e critérios de conclusão — sem frontmatter nem schema de permissão de nenhuma plataforma. `.opencode/agents/` deixa de ser a fonte canônica; `.opencode/` só sai do repositório em uma etapa DEV futura, com um gate QA próprio aprovado especificamente para essa remoção. Adaptadores específicos de plataforma, se algum dia forem necessários, ficam fora do repositório ou em integrações separadas — nunca como fonte canônica.

### Entrega desta capacidade

Nesta etapa (revisão de QA), a entrega é **exclusivamente** o pacote QA revisado (`01` a `05` + `00 README`), mais a atualização de `NXG-028`, do épico e do Board QA, e a marcação de obsolescência da execução DEV anterior. Fica fora desta entrega — é escopo de uma implementação DEV futura, autorizada somente após um novo `QA_READY_FOR_DEV`: criar `agents/`, migrar/escrever os 4 contratos, remover `.opencode/` e atualizar `AGENTS.md`, `README.md`, `docs/skills/SKILL-009-documentation-sync.md` e `docs/plans/PLAN-084-organizacao-repositorio.md` no repositório.

---

## Decisões de produto

- `AGENTS.md` permanece o contrato global único na raiz — nenhuma mudança de papel.
- `agents/` na raiz é a fonte canônica neutra; `agents/README.md` funciona como índice, listando os 4 contratos e as regras de uso de cada um.
- `docs-sync.md` e `ops-runner.md` são migrados/reproduzidos como contratos neutros em `agents/` (mesmo propósito e escopo de hoje, sem frontmatter/`permission` do OpenCode); `product-planner.md` e `qa-reviewer.md` nascem diretamente neutros em `agents/`. Nenhum dos 4 depende de OpenCode, Claude ou Codex para ser lido ou aplicado.
- `product-planner`: planejamento de features e planos (`PLAN-NNN`); leitura ampla e escrita documentada como exclusiva de `docs/plans/**` — descrita como regra do contrato, não como schema de permissão de uma plataforma.
- `qa-reviewer`: revisão de qualidade e CTs; somente leitura e reporte, sem autoridade para aprovar o próprio CT que revisou.
- Contratos/adaptadores específicos de uma plataforma, se necessários no futuro, ficam fora do repositório ou em integrações separadas — nunca substituem a fonte canônica em `agents/`.
- `.opencode/` só sai do repositório em uma etapa DEV futura, com gate QA próprio para essa remoção; esta revisão **não** autoriza a remoção agora.
- Referências ativas a `.opencode/agents` — `README.md`, `AGENTS.md`, `docs/skills/SKILL-009-documentation-sync.md`, `docs/plans/PLAN-084-organizacao-repositorio.md`, `.dockerignore` — são atualizadas na implementação DEV, não nesta revisão. `docs/UPDATES.md` é histórico (changelog) e não é alterado.
- Este lote de revisão não altera código, infraestrutura, `.env` ou scripts de deploy, e não é aplicado ao repositório NX Gest nesta etapa de QA.

---

## Escopo

- Reescrever `01 - Demanda.md`, `02 - Plano de teste.md`, `03 - Casos de teste.md`, `04 - Validação dev.md`, `05 - Preparação Qase.md` e `00 README.md` do pacote `NXG-MEL-0007` para a arquitetura neutra de agentes.
- Atualizar `NXG-028` (lote 4, decisões de organização, arquitetura-alvo), o épico `NXG-EPIC-0001` (escopo, demandas vinculadas, status consolidado) e o Board QA (nota do card).
- Marcar a execução DEV anterior (`03 Trabalho/DEV/Nxgest/Execuções/NXG-MEL-0007 Agentes especializados/`) como obsoleta/substituída, sem apagar ou mover a pasta.
- Executar o validador oficial (`scripts/validar_pacote_qa.py`) e auditar links internos, placeholders e aninhamento dos CTs.

---

## Fora de escopo

- Criar `agents/` no repositório NX Gest.
- Remover `.opencode/` do repositório.
- Editar `AGENTS.md`, `README.md`, `docs/skills/SKILL-009-documentation-sync.md`, `docs/plans/PLAN-084-organizacao-repositorio.md`, `.dockerignore` ou qualquer arquivo de código, infraestrutura, ambiente ou deploy.
- Reescrever `docs/UPDATES.md` (registro histórico).
- Criar uma nova execução DEV ou emitir `QA_READY_FOR_DEV` nesta etapa.

---

## Critérios de aceite

- C1. `AGENTS.md` permanece o contrato global único na raiz do repositório, sem perder esse papel na nova arquitetura. ^c1
- C2. `agents/` passa a ser a fonte canônica neutra na raiz, com `agents/README.md` como índice, contendo `docs-sync.md`, `ops-runner.md`, `product-planner.md` e `qa-reviewer.md`. ^c2
- C3. Os 4 contratos descrevem identidade, responsabilidade, entradas/saídas, regras, limites, protocolo e critérios de conclusão, sem depender de frontmatter ou de qualquer schema de permissão específico do OpenCode (ou de outra plataforma). ^c3
- C4. A migração/remoção futura de `.opencode/` e a atualização de todas as referências estruturais ativas estão cobertas por um inventário explícito (`README.md`, `AGENTS.md`, `docs/skills/SKILL-009-documentation-sync.md`, `docs/plans/PLAN-084-organizacao-repositorio.md`, `.dockerignore`); changelogs históricos (`docs/UPDATES.md`) não precisam ser reescritos. ^c4
- C5. `README.md`, `AGENTS.md`, `SKILL-009` e `PLAN-084` ficam identificados como documentação ativa a tornar coerente com `agents/` — essa atualização é registrada como escopo da implementação DEV futura, não executada agora no repositório. ^c5
- C6. Nenhuma alteração em código, `frontend/`, `infra/`, `.env`, scripts de deploy ou no trabalho protegido em andamento. ^c6
- C7. Todos os links internos do pacote QA resolvem, a estrutura segue literalmente os templates oficiais, e o validador (`scripts/validar_pacote_qa.py`) aprova o pacote. ^c7

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Nenhuma pendência de decisão de produto. A liberação para `QA_READY_FOR_DEV` depende de uma nova execução de `python3 scripts/validar_pacote_qa.py "03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados"` e da aprovação formal do Orquestrador — nenhuma execução DEV está autorizada antes disso.
