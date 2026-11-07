---
status: "concluido"
tipo: bug
etapa_atual: "Concluído"
demanda: "NXG-029"
epico: "NXG-EPIC-0001"
commit: "a509f4b, c0b0d3a"
pontos: ""
data_fim: "2026-11-07"
---

# NXG-029 — Fix (Staging carrega valores com espaços)

> [!info]- Navegação QA/DEV
> **README DEV:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/00 README|README DEV]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/01 - Bug|Demanda QA]]  
> **Casos de teste QA:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/02 - Casos de teste|Casos de teste QA]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/03 - Validação dev|Validação QA]]  
> **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|Épico]]  
> **Análise:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/01 - Análise|Análise]]  
> **Plano:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/02 - Plano de correção|Plano]]  
> **Implementação:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/03 - Implementação|Implementação]]  
> **Code review:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/04 - Code review|Code review]]  

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Etapa atual:** `INPUT[inlineSelect(option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!info]- Cards relacionados
> **Demanda:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/01 - Bug|NXG-029]]  
> **Casos de teste:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/02 - Casos de teste|CTs QA]]  
> **Validação:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/03 - Validação dev|Validação QA]]

Gerar e reutilizar staging com espaços sem avaliar conteúdo do arquivo como shell, inclusive o formato legado conhecido.

> [!tip]- Esforço
> ```dataviewjs
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + dv.current().file.folder + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.table(["Artefato DEV", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos · **Esforço total do fix DEV:** ${total} pontos`);
> ```

**DEV_READY_FOR_QA** — revisão técnica entregue; CTs e decisão funcional aguardam QA independente.

## Checklist de transição DEV

- [x] Causa confirmada no código.
- [x] Plano de correção registrado.
- [x] Implementação concluída para validação.
- [x] Code review técnico concluído com limitações.
- [ ] Validação QA concluída.
- [x] Frontmatter, README, board DEV, links, evidências e pendências DEV conferidos; QA sincroniza seus registros.

## Retorno QA — 2026-11-07

QA independente aprovou o pacote; execução arquivada com sua validação. O épico permanece aberto até decisão do usuário.
