---
status: execucao
tipo: melhoria
etapa_atual: "DEV · Análise técnica"
demanda: "<ID>"
plano: ""
commit: ""
pontos: ""
---

# <ID> — Execução (<resultado em uma frase>)

> [!info]- Navegação QA/DEV
> **Demanda QA:** [[<DEMANDA>|<ID> — <título da demanda>]]  
> **Análise:** [[04 Trabalho DEV/Execuções/<ID>/01 - Análise|01 - Análise]]  
> **Plano:** [[04 Trabalho DEV/Execuções/<ID>/02 - Plano de execução|02 - Plano de execução]]  
> **Plano técnico:** [[04 Trabalho DEV/Planos/PLAN-NNN|PLAN-NNN — <título técnico>]]  
> **Implementação:** [[04 Trabalho DEV/Execuções/<ID>/03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 Trabalho DEV/Execuções/<ID>/04 - Code review|04 - Code review]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!info]- Cards relacionados
> **Demanda QA:** [[<DEMANDA>|<ID> — <título da demanda>]]  
> **Plano técnico:** [[04 Trabalho DEV/Planos/PLAN-NNN|PLAN-NNN]]  
> **Implementação:** [[04 Trabalho DEV/Execuções/<ID>/03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 Trabalho DEV/Execuções/<ID>/04 - Code review|04 - Code review]]  
> **Validação QA:** [[<VALIDACAO>|Validação QA]]

> [!tip]- Esforço
> ```dataviewjs
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + dv.current().file.folder + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.table(["Artefato DEV", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos · **Esforço total da execução DEV:** ${total} pontos`);
> ```

> Resumo humano do comportamento entregue e do motivo.

---


---

## Status

> Ao avançar uma etapa, atualize sempre os quatro pontos relacionados: propriedade `status` da demanda, coluna no Board, esta tabela e o registro de validação quando a etapa for QA.

| Etapa | Estado | Data |
|---|---|---|
| Análise | ⏳ | |
| Plano de execução | ⏳ | |
| Execução | ⏳ | |
| Code review | ⏳ | |
| Verificação (CTs) | ⏳ | |
| Fechamento | ⏳ | |

---

## Histórico

- YYYY-MM-DD — pasta de execução criada.

---

## Checklist de transição

- [ ] Status da demanda atualizado
- [ ] Card movido para a coluna correspondente no Board
- [ ] Esta tabela atualizada
- [ ] Bloco “Status atual” da demanda atualizado
- [ ] Validação vinculada/atualizada quando aplicável
