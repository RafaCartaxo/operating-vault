---
status: concluido
tipo: melhoria
etapa_atual: "Concluído"
demanda: "[[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0007/QA/NXG-MEL-0007 Agentes especializados/01 - Demanda|NXG-MEL-0007]]"
epico: "[[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|NXG-EPIC-0001]]"
plano: ""
commit: ""
pontos: 10
---

# NXG-MEL-0007 — Execução (agentes neutros: agents/ canônico, migração e remoção de .opencode/)


> [!info]- Navegação QA/DEV
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0007/QA/NXG-MEL-0007 Agentes especializados/01 - Demanda|NXG-MEL-0007 — Agentes especializados]]  
> **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|NXG-EPIC-0001 — Organização do NX Gest]]
> **Análise:** [[01 - Análise|01 - Análise]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!info]- Cards relacionados
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0007/QA/NXG-MEL-0007 Agentes especializados/01 - Demanda|NXG-MEL-0007 — Agentes especializados]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0007/QA/NXG-MEL-0007 Agentes especializados/04 - Validação dev|Validação QA]]

> [!tip]- Esforço
> ```dataviewjs
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + dv.current().file.folder + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.table(["Artefato DEV", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos · **Esforço total da execução DEV:** ${total} pontos`);
> ```

> `AGENTS.md` permanece o contrato global na raiz. `agents/` passa a ser a fonte canônica neutra de contratos de agente (`agents/README.md` + `docs-sync.md`/`ops-runner.md`/`product-planner.md`/`qa-reviewer.md`, sem frontmatter nem schema de permissão de plataforma). `.opencode/` foi removido do repositório após a migração do conteúdo útil. `README.md`, `AGENTS.md`, `docs/skills/SKILL-009-documentation-sync.md`, `docs/plans/PLAN-084-organizacao-repositorio.md` e `.dockerignore` foram atualizados para refletir a nova arquitetura. QA aprovou os 7 CTs — lote concluído.

---


---

## Status

> Ao avançar uma etapa, atualize sempre os quatro pontos relacionados: propriedade `status` da demanda, coluna no Board, esta tabela e o registro de validação quando a etapa for QA.

| Etapa | Estado | Data |
|---|---|---|
| Análise | ✅ | 2026-10-17 |
| Plano de execução | ✅ | 2026-10-17 |
| Execução | ✅ | 2026-10-17 |
| Code review | ✅ | 2026-10-17 |
| Verificação (CTs) | ✅ aprovado (7/7) | 2026-10-17 |
| Fechamento | ✅ | 2026-10-17 |

---

## Histórico

- 2026-10-17 — Pasta de execução criada a partir dos templates oficiais, após `QA_READY_FOR_DEV` do pacote QA revisado (arquitetura neutra de agentes).
- 2026-10-17 — Análise e plano de execução preenchidos e aprovados (auto-consistentes com a demanda; nenhum bloqueio de sintaxe desta vez, diferente da tentativa anterior com schema OpenCode).
- 2026-10-17 — Implementação concluída: `agents/README.md` + 4 contratos neutros criados; `AGENTS.md`, `README.md`, `docs/skills/SKILL-009-documentation-sync.md`, `docs/plans/PLAN-084-organizacao-repositorio.md` e `.dockerignore` atualizados; `.opencode/` removido por completo.
- 2026-10-17 — Code review concluído (ver `04 - Code review`); handoff `DEV_READY_FOR_QA` enviado ao Orquestrador.
- 2026-10-17 — QA executou e aprovou os 7 CTs (ver `04 - Validação dev.md` do pacote QA). Nenhum defeito encontrado. Lote concluído e arquivado.

---

## Checklist de transição

- [x] Status da demanda atualizado (`concluido` / "Concluído")
- [x] Card movido para a coluna correspondente no Board (✅ Concluído)
- [x] Esta tabela atualizada
- [x] Bloco "Status atual" da demanda atualizado
- [x] Validação vinculada/atualizada (`04 - Validação dev.md` — 7/7 CTs aprovados)
- [x] Sincronização documental verificada: frontmatter, README, board, links, evidências, histórico e pendências
