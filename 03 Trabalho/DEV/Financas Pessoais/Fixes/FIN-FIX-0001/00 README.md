---
status: concluido
tipo: bug
etapa_atual: "Concluído"
demanda: "FIN-BUG-0001"
epico: ""
commit: ""
pontos: ""
---

# FIN-FIX-0001 — Liberar cursor antes de gerar recorrências


> [!info]- Navegação QA/DEV
> **Bug QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Bugs/FIN-BUG-0001 Falha ao gerar recorrencias mensais/01 - Bug|FIN-BUG-0001 — Geração mensal de recorrências bloqueia lançamentos]]
> **Épico:** não aplicável
> **Análise:** [[01 - Análise]]  
> **Plano de correção:** [[02 - Plano de correção]]  
> **Implementação:** [[03 - Implementação]]  
> **Code review:** [[04 - Code review]]  
> **Casos de teste QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Bugs/FIN-BUG-0001 Falha ao gerar recorrencias mensais/02 - Casos de teste|Casos de teste]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!info]- Cards relacionados
> **Bug QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Bugs/FIN-BUG-0001 Falha ao gerar recorrencias mensais/01 - Bug|FIN-BUG-0001]]
> **Casos de teste:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Bugs/FIN-BUG-0001 Falha ao gerar recorrencias mensais/02 - Casos de teste|Casos de teste]]
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Bugs/FIN-BUG-0001 Falha ao gerar recorrencias mensais/03 - Validação dev|Validação QA]]
> **Implementação:** [[03 - Implementação]]  
> **Code review:** [[04 - Code review]]

> [!tip]- Esforço
> ```dataviewjs
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + dv.current().file.folder + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.table(["Artefato DEV", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos · **Esforço total do fix DEV:** ${total} pontos`);
> ```

Índice do trabalho de desenvolvimento para a correção do bug. O fix altera somente a geração mensal das ocorrências; não altera o contrato funcional da recorrência.

---


---

## Checklist de transição DEV


- [x] Causa confirmada no código
- [x] Plano de correção aprovado
- [x] Implementação concluída
- [x] Code review aprovado
- [x] Validação QA concluída — CT-B01 e CT-B02 aprovados.
- [x] Sincronização documental verificada: frontmatter, README, board, links, evidências, histórico e pendências
