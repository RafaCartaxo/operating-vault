---
status: execucao
tipo: melhoria
etapa_atual: "DEV · Análise técnica"
obsoleta: true
demanda: "[[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/01 - Demanda|NXG-MEL-0007]]"
epico: "[[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|NXG-EPIC-0001]]"
plano: "[[03 Trabalho/QA/Nxgest/Demandas/Planos/NXG-028 Governanca da reorganizacao do NX Gest|NXG-028]]"
commit: ""
pontos: ""
---

# NXG-MEL-0007 — Execução (OBSOLETA/SUBSTITUÍDA — escopo antigo OpenCode)

> [!danger] OBSOLETA / SUBSTITUÍDA — NÃO AUTORIZADA PARA EXECUÇÃO
> Esta execução foi aberta para o escopo antigo de `NXG-MEL-0007` (criar `.opencode/agents/product-planner.md` e `.opencode/agents/qa-reviewer.md` com frontmatter/schema de permissão do OpenCode). Esse escopo foi **superado** pela decisão do Orquestrador de tornar a governança de agentes independente de plataforma (fonte canônica neutra em `agents/`).
>
> - Esta pasta **não é** uma execução DEV válida e **não autoriza** nenhuma implementação no repositório NX Gest.
> - O conteúdo de `01 - Análise.md` e `02 - Plano de execução.md` é mantido como registro histórico da tentativa anterior — não foi reescrito, apenas sinalizado como obsoleto.
> - A execução DEV correta para `NXG-MEL-0007` (fonte neutra em `agents/`, sem frontmatter/schema de plataforma) só será criada, a partir dos templates oficiais, depois de um **novo** `QA_READY_FOR_DEV` aprovado pelo Orquestrador para o pacote QA revisado.

> [!info]- Navegação QA/DEV
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/01 - Demanda|NXG-MEL-0007 — Agentes especializados]]  
> **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|NXG-EPIC-0001 — Organização do NX Gest]]
> **Análise:** [[01 - Análise|01 - Análise]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!info]- Cards relacionados
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/01 - Demanda|NXG-MEL-0007 — Agentes especializados]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/04 - Validação dev|Validação QA]]

> [!tip]- Esforço
> ```dataviewjs
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + dv.current().file.folder + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.table(["Artefato DEV", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos · **Esforço total da execução DEV:** ${total} pontos`);
> ```

> Resumo: tentativa de execução para o escopo antigo (agentes OpenCode-specific). Interrompida antes da implementação por um bloqueio de sintaxe de permissão; depois superada pela decisão de arquitetura neutra. Nenhum arquivo foi criado no repositório NX Gest por esta execução.

---

## Status

> Ao avançar uma etapa, atualize sempre os quatro pontos relacionados: propriedade `status` da demanda, coluna no Board, esta tabela e o registro de validação quando a etapa for QA.

| Etapa | Estado | Data |
|---|---|---|
| Análise | ✅ (escopo obsoleto) | 2026-10-17 |
| Plano de execução | ✅ (escopo obsoleto, congelado) | 2026-10-17 |
| Execução | ⏳ não iniciada | |
| Code review | ⏳ não iniciada | |
| Verificação (CTs) | ⏳ não iniciada | |
| Fechamento | 🚫 obsoleta — ver execução futura após novo gate | 2026-10-17 |

---

## Histórico

- 2026-10-17 — Pasta de execução criada para o escopo antigo (`.opencode/agents/product-planner.md`/`qa-reviewer.md`, schema OpenCode).
- 2026-10-17 — Análise concluída e plano de execução congelado para esse escopo; bloqueio de sintaxe de permissão registrado e resolvido pelo Orquestrador.
- 2026-10-17 — Execução **marcada como obsoleta/substituída**: o Orquestrador decidiu tornar a governança de agentes independente de plataforma (fonte canônica neutra em `agents/`). Nenhuma implementação chegou a ser aplicada no repositório NX Gest. O pacote QA de `NXG-MEL-0007` foi revisado e retornado para `QA · Casos de teste`; uma nova execução DEV será criada a partir dos templates oficiais somente após um novo `QA_READY_FOR_DEV`.

---

## Checklist de transição

- [x] Status da demanda atualizado (revertido para `analise`/`QA · Casos de teste` no pacote QA)
- [x] Card do Board QA atualizado (nota de revisão, sem referência a esta execução como válida)
- [x] Esta tabela atualizada com o estado obsoleto
- [ ] Bloco "Status atual" da demanda — já reflete o pacote em revisão
- [x] Validação QA não iniciada para este escopo (sem CTs executados)
- [x] Sincronização documental verificada: frontmatter, README, board, links, evidências, histórico e pendências
