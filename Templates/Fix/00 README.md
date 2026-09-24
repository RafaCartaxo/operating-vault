---
status: execucao
tipo: bug
etapa_atual: "DEV · Análise técnica"
demanda: "<ID>"
commit: ""
pontos: ""
---

# <ID> — Fix

> [!info]- Navegação QA/DEV
> **Bug QA:** [[<CARD>|<ID> — <título>]]  
> **Análise:** [[01 - Análise]]  
> **Plano de correção:** [[02 - Plano de correção]]  
> **Implementação:** [[03 - Implementação]]  
> **Code review:** [[04 - Code review]]  
> **Casos de teste QA:** [[03 Trabalho/QA/<projeto>/Demandas/Bugs/<ID>/02 - Casos de teste|02 - Casos de teste]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!info]- Cards relacionados
> **Bug QA:** [[<CARD>|<ID> — <título>]]  
> **Casos de teste:** [[03 Trabalho/QA/<projeto>/Demandas/Bugs/<ID>/02 - Casos de teste|Casos de teste]]  
> **Validação QA:** [[03 Trabalho/QA/<projeto>/Demandas/Bugs/<ID>/03 - Validação dev|Validação QA]]  
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

Índice do trabalho de desenvolvimento para a correção do bug.

---


---

## Checklist de transição DEV


- [ ] Causa confirmada no código
- [ ] Plano de correção aprovado
- [ ] Implementação concluída
- [ ] Code review aprovado
- [ ] Validação QA concluída
