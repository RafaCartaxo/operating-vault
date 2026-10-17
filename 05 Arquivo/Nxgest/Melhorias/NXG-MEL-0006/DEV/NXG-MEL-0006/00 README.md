---
status: execucao
tipo: melhoria
etapa_atual: "DEV · Code review"
demanda: "[[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0006/QA/NXG-MEL-0006 Onboarding de ambientes/01 - Demanda|NXG-MEL-0006]]"
epico: NXG-EPIC-0001
plano: "[[03 Trabalho/QA/Nxgest/Demandas/Planos/NXG-028 Governanca da reorganizacao do NX Gest|NXG-028]]"
commit: ""
pontos: 10
---

# NXG-MEL-0006 — Execução (onboarding de ambientes encapsulado em scripts npm)

> [!info]- Navegação QA/DEV
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0006/QA/NXG-MEL-0006 Onboarding de ambientes/01 - Demanda|NXG-MEL-0006 — Onboarding de ambientes]]  
> **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|NXG-EPIC-0001 — Organização do NX Gest]]
> **Análise:** [[01 - Análise|01 - Análise]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Plano técnico:** não se aplica — lote de organização  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!info]- Cards relacionados
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0006/QA/NXG-MEL-0006 Onboarding de ambientes/01 - Demanda|NXG-MEL-0006]]  
> **Plano técnico:** não se aplica  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0006/QA/NXG-MEL-0006 Onboarding de ambientes/04 - Validação dev|Validação QA]]

> [!tip]- Esforço
> ```dataviewjs
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + dv.current().file.folder + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.table(["Artefato DEV", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos · **Esforço total da execução DEV:** ${total} pontos`);
> ```

> `package.json` ganhou `db:up`/`db:down`/`db:ps`; `README.md` e `08-SETUP-NOVA-MAQUINA.md` usam os novos comandos. `db:up`/`db:ps` validados de verdade contra o Postgres de dev já existente; `db:down` deliberadamente não executado para não derrubar um ambiente ativo do usuário (ver `03 - Implementação`). Pronto para QA.

---

## Status

| Etapa | Estado | Data |
|---|---|---|
| Análise | ✅ | 2026-10-17 |
| Plano de execução | ✅ | 2026-10-17 |
| Execução | ✅ | 2026-10-17 |
| Code review | ✅ | 2026-10-17 |
| Verificação (CTs) | ✅ aprovado com ressalva | 2026-10-17 |
| Fechamento | ✅ | 2026-10-17 |

---

## Histórico

- 2026-10-17 — execução criada (sem pausa, logo após conclusão do NXG-MEL-0005).
- 2026-10-17 — `package.json`/`README.md`/`08-SETUP-NOVA-MAQUINA.md` implementados; `db:up`/`db:ps` validados de verdade; `db:down` deliberadamente não executado (container de dev pré-existente do usuário). Code review aprovado. Handoff emitido: `DEV_READY_FOR_QA`.
- 2026-10-17 — QA independente do Orquestrador encontrou referência residual em `08-SETUP-NOVA-MAQUINA.md` (checklist da seção 9). Corrigida, revalidada (`rg`, `git diff --check`, `package.json`). Handoff reemitido: `DEV_READY_FOR_QA`.
- 2026-10-17 — QA aprovou com ressalva (limitação de permissão do socket Docker para reexecução independente, não um defeito). Lote concluído.

---

## Checklist de transição

- [x] Status da demanda atualizado — a sincronizar em `01 - Demanda.md` (QA) ao receber o handoff.
- [x] Card no Board — QA decide a coluna ao assumir o handoff.
- [x] Esta tabela atualizada.
- [x] Bloco "Status atual" da demanda — QA atualiza ao assumir o handoff.
- [ ] Validação vinculada/atualizada quando aplicável — reservado ao QA.
- [x] Sincronização documental verificada: frontmatter, README, board, links, evidências e histórico desta execução estão coerentes.
