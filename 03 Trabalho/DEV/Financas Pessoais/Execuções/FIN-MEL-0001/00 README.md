---
status: concluido
tipo: melhoria
etapa_atual: "Concluído"
demanda: "FIN-MEL-0001"
plano: ""
commit: ""
pontos: 5
---

# FIN-MEL-0001 — Cadastro mobile de nova despesa

> [!info]- Navegação QA/DEV
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/01 - Demanda|FIN-MEL-0001 — Cadastro mobile de nova despesa]]  
> **Análise:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/01 - Análise|01 - Análise]]  
> **Plano:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/02 - Plano de execução|02 - Plano de execução]]  
> **Plano técnico:** a definir após a análise técnica  
> **Implementação:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/03 - Implementação|03 - Implementação]]  
> **Code review:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/04 - Code review|04 - Code review]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!info]- Cards relacionados
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/01 - Demanda|FIN-MEL-0001 — Demanda QA]]  
> **Plano técnico:** a definir após a análise técnica  
> **Implementação:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/03 - Implementação|03 - Implementação]]  
> **Code review:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/04 - Validação dev|Validação QA]]

> [!tip]- Esforço
> ```dataviewjs
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + dv.current().file.folder + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.table(["Artefato DEV", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos · **Esforço total da execução DEV:** ${total} pontos`);
> ```

> Resumo: primeira tela mobile-first para cadastrar uma despesa e enviá-la ao backend Go existente.

---

## Status

> Ao avançar uma etapa, atualizar `status` e `etapa_atual` da demanda, a coluna do Board, esta tabela e o registro de validação quando a etapa for QA.

| Etapa | Estado | Data |
|---|---|---|
| Análise | 🔵 | 2026-10-02 |
| Plano de execução | ⏳ | |
| Execução | ⏳ | |
| Code review | ✅ | 2026-10-02 |
| Verificação (CTs) | ✅ | 2026-10-02 |
| Fechamento | ✅ | 2026-10-02 |

---

## Histórico

- 2026-10-02 — QA concluído e execução DEV liberada.
- 2026-10-02 — análise técnica preenchida.
- 2026-10-02 — implementação concluída e code review aprovado; liberado para QA.
- 2026-10-02 — todos os CTs aprovados; melhoria concluída.

---

## Checklist de transição

- [x] Status da demanda atualizado
- [x] Card movido para a coluna correspondente no Board
- [x] Esta tabela atualizada
- [x] Bloco “Status atual” da demanda atualizado
- [x] Validação vinculada/atualizada quando aplicável
