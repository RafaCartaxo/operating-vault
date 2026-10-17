---
status: execucao
tipo: melhoria
etapa_atual: "DEV · Implementação"
demanda: "[[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0005 Infraestrutura em infra/01 - Demanda|NXG-MEL-0005]]"
epico: NXG-EPIC-0001
plano: "[[03 Trabalho/QA/Nxgest/Demandas/Planos/NXG-028 Governanca da reorganizacao do NX Gest|NXG-028]]"
commit: ""
pontos: 20
---

# NXG-MEL-0005 — Execução (infraestrutura movida para infra/, bloqueada por risco de nomenclatura de volume)

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

> Os 5 arquivos de infraestrutura foram movidos para `infra/` e as 4 referências foram atualizadas, mas a validação (`docker compose config`) revelou que o nome do projeto Compose muda de `nxgestao` para `infra`, quebrando os nomes reais de volume/rede de produção. Execução pausada — aguardando autorização para aplicar a correção já testada (`name: nxgestao` nos 3 compose).

---

## Status

> Ao avançar uma etapa, atualize sempre os quatro pontos relacionados: propriedade `status` da demanda, coluna no Board, esta tabela e o registro de validação quando a etapa for QA.

| Etapa | Estado | Data |
|---|---|---|
| Análise | ✅ | 2026-10-17 |
| Plano de execução | ✅ | 2026-10-17 |
| Execução | 🚨 bloqueada (achado crítico) | 2026-10-17 |
| Code review | ⏳ | |
| Verificação (CTs) | ⏳ | |
| Fechamento | ⏳ | |

---

## Histórico

- 2026-10-17 — execução criada após gate `QA_READY_FOR_DEV` (autorização acoplada com NXG-MEL-0006).
- 2026-10-17 — arquivos movidos para `infra/`, 4 referências atualizadas, `docker compose config` executado. Achado crítico: nome de projeto Compose muda de `nxgestao` para `infra`, quebrando nomes reais de volume/rede. Execução pausada; `BLOQUEIO PARA O ORQUESTRADOR` enviado.

---

## Checklist de transição

- [ ] Status da demanda atualizado — pendente até a correção ser autorizada e aplicada.
- [ ] Card movido para a coluna correspondente no Board — mantido em "Casos de teste" (gate aprovado) até a execução ser concluída.
- [x] Esta tabela atualizada.
- [ ] Bloco "Status atual" da demanda — a atualizar após a correção.
- [ ] Validação vinculada/atualizada quando aplicável — QA ainda não executa CTs (DEV não concluído).
- [x] Sincronização documental verificada: frontmatter, README, board, links, evidências e histórico desta execução estão coerentes com o estado real (bloqueado).
