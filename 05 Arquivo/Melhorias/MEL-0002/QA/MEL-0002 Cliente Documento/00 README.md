---
status: concluido
demanda: MEL-0002
tipo: melhoria
etapa_atual: "Concluído"
---
# MEL-0002 — QA

Índice do trabalho de qualidade da melhoria de Documento alternativo no cadastro de cliente.

> [!info]- Navegação QA/DEV
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** [[05 Arquivo/Melhorias/MEL-0002/DEV/MEL-0002/00 README|MEL-0002 — execução]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!tip]- Esforço
> ```dataviewjs
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + dv.current().file.folder + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos`);
> dv.table(["Artefato QA", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço total do pacote QA:** ${total} pontos`);
> ```

> [!warning]- Esforço adicional por defeitos filhos
> ```dataviewjs
> const id = (dv.current().file.folder.match(/MEL-\d+/) || [""])[0];
> const defeitos = dv.pages('"03 Trabalho QA/Demandas/Bugs"').where(p => String(p.pai ?? "").includes(id));
> const adicional = defeitos.array().reduce((soma, pagina) => soma + (typeof pagina.pontos === "number" ? pagina.pontos : 0), 0);
> const original = dv.pages().where(p => id && p.file.path.includes(id) && typeof p.pontos === "number").array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.table(["Defeito filho", "Pontos"], defeitos.map(p => [p.file.link, p.pontos ?? 0]));
> dv.paragraph(`**${id || "<ID>"} — Retrabalho por defeitos filhos:** ${adicional} pontos (${defeitos.length} defeitos)`);
> ```

## Status

| Etapa QA | Estado |
|---|---|
| Demanda | ✅ |
| Plano de teste | ✅ |
| Casos de teste | ✅ |
| Validação | ✅ |

## Checklist de transição QA

- [x] Demanda refinada e critérios de aceite definidos
- [x] Plano de teste revisado
- [x] Casos de teste criados
- [x] Execução DEV vinculada
- [x] CTs executados com evidências
- [x] Resultado da validação decidido

**Próximo passo:** executar CT-001 a CT-008 e registrar as evidências em [[04 - Validação dev]].
