---
status: execucao
tipo: melhoria
etapa_atual: "DEV · Code review"
demanda: "[[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0005 Infraestrutura em infra/01 - Demanda|NXG-MEL-0005]]"
epico: NXG-EPIC-0001
plano: "[[03 Trabalho/QA/Nxgest/Demandas/Planos/NXG-028 Governanca da reorganizacao do NX Gest|NXG-028]]"
commit: ""
pontos: 20
---

# NXG-MEL-0005 — Execução (infraestrutura movida para infra/, nomes reais e segredos preservados)

> [!info]- Navegação QA/DEV
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0005 Infraestrutura em infra/01 - Demanda|NXG-MEL-0005 — Infraestrutura em infra/]]  
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
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0005 Infraestrutura em infra/01 - Demanda|NXG-MEL-0005]]  
> **Plano técnico:** não se aplica  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0005 Infraestrutura em infra/04 - Validação dev|Validação QA]]

> [!tip]- Esforço
> ```dataviewjs
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + dv.current().file.folder + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.table(["Artefato DEV", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos · **Esforço total da execução DEV:** ${total} pontos`);
> ```

> Infraestrutura movida para `infra/` com `name: nxgestao` + `build.context`/Caddyfile corretos + `--project-directory .` nas 4 referências de deploy/operação. `docker compose config` validado nos 3 ambientes na forma final: nomes de volume/rede/container idênticos aos de produção, segredos reais carregados corretamente, nenhum valor exposto. Pronto para QA.

---

## Status

> Ao avançar uma etapa, atualize sempre os quatro pontos relacionados: propriedade `status` da demanda, coluna no Board, esta tabela e o registro de validação quando a etapa for QA.

| Etapa | Estado | Data |
|---|---|---|
| Análise | ✅ | 2026-10-17 |
| Plano de execução | ✅ | 2026-10-17 |
| Execução | ✅ | 2026-10-17 |
| Code review | ✅ | 2026-10-17 |
| Verificação (CTs) | ⏳ aguardando QA | |
| Fechamento | ⏳ | |

---

## Histórico

- 2026-10-17 — execução criada após gate `QA_READY_FOR_DEV` (autorização acoplada com NXG-MEL-0006).
- 2026-10-17 — arquivos movidos para `infra/`, 4 referências atualizadas. Achado crítico 1: nome de projeto Compose muda para `infra`, quebrando nomes reais de volume. `BLOQUEIO` enviado.
- 2026-10-17 — Correção A (`name: nxgestao`) autorizada e aplicada. Revalidação revelou achado crítico 2: `.env` real não carregado sem `--project-directory .` (JWT_SECRET ficaria vazio). Novo `BLOQUEIO` enviado.
- 2026-10-17 — Correção B (`--project-directory .`) autorizada e aplicada nos 4 arquivos de referência. Revalidação revelou e corrigiu, na mesma rodada, uma interação adicional (`build.context`/Caddyfile precisavam de `.` em vez de `..`/`./Caddyfile`). Revalidação final: 3 ambientes com exit 0, nomes corretos, segredos carregados, nenhum valor exposto. Code review aprovado. Handoff emitido: `DEV_READY_FOR_QA`.

---

## Checklist de transição

- [x] Status da demanda atualizado — a sincronizar em `01 - Demanda.md` (QA) ao receber o handoff.
- [x] Card no Board — QA decide a coluna ao assumir o handoff.
- [x] Esta tabela atualizada.
- [x] Bloco "Status atual" da demanda — QA atualiza ao assumir o handoff.
- [ ] Validação vinculada/atualizada quando aplicável — reservado ao QA (execução dos CTs).
- [x] Sincronização documental verificada: frontmatter, README, board, links, evidências e histórico desta execução estão coerentes com o estado real (pronto para QA).
