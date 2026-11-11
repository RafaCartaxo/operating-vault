---
status: validacao
tipo: bug
etapa_atual: "QA · Validação"
projeto: nxgest
pai: NXG-MEL-0009
---

# NXG-033 — Declaracoes inconsistentes passam no preflight de rollback


> [!info]- Navegação QA/DEV
> **Bug:** [[01 - Bug]]  
> **Pai:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/01 - Demanda|NXG-MEL-0009]].
> **Casos de teste:** [[02 - Casos de teste]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Fix DEV:** pendente de encaminhamento pela Coordenação.
> **Validação QA:** [[03 - Validação dev|Validação QA]] — criada junto com o Bug, copiando `Templates/QA/04 - Validação dev.md` e renomeando para `03 - Validação dev.md`.

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!info]- Cards relacionados
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Validação:** [[03 - Validação dev]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Fix DEV:** pendente de encaminhamento pela Coordenação.

> [!tip]- Esforço
> ```dataviewjs
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + dv.current().file.folder + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos`);
> dv.table(["Artefato QA", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço total do pacote QA:** ${total} pontos`);
> ```

> [!warning]- Esforço adicional por defeitos derivados
> ```dataviewjs
> const projeto = String(dv.current().projeto || dv.current().file.path.match(/03 Trabalho\/QA\/([^/]+)/)?.[1] || "").toLowerCase();
> const id = (dv.current().file.folder.match(new RegExp(`${projeto.toUpperCase() || "[A-Z]{2,8}"}-\\d+`)) || [""])[0];
> const derivados = dv.pages().where(p => projeto && p.file.path.includes(`03 Trabalho/QA/${projeto}/Demandas/Bugs`) && String(p.pai ?? "").includes(id));
> const adicional = derivados.array().reduce((soma, pagina) => soma + (typeof pagina.pontos === "number" ? pagina.pontos : 0), 0);
> const original = dv.pages('"' + dv.current().file.folder + '"').where(p => typeof p.pontos === "number").array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.table(["Defeito derivado", "Pontos"], derivados.map(p => [p.file.link, p.pontos ?? 0]));
> dv.paragraph(`**${id || "NXG-033"} — Retrabalho por defeitos derivados:** ${adicional} pontos (${derivados.length} defeitos)`);
> ```

Pacote QA para `NXG-033`:

```text
NXG-033/
├── 00 README.md
├── 01 - Bug.md
├── 02 - Casos de teste.md
├── 03 - Validação dev.md
└── 04 - Preparação Qase.md
```

O arquivo de validação nasce junto com o Bug e é preenchido após o Fix DEV.

---


Cada CT usa um callout recolhível com identificador (`^ct-b01`). A nota de validação aponta para esse bloco na tabela; ao passar o mouse sobre o link, o Obsidian mostra a prévia do cenário completo.

## Encaminhamento

Achado derivado de [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/04 - Validação dev|validação QA MEL-0009]]. Gate histórico QA_READY_FOR_DEV foi seguido de reteste. Coordenação recebe resultado; sincronização dos Fixes DEV permanece pendente. Sem acesso a recursos reais.

## Gate de integridade

2026-11-11: critérios, matriz, CTs, validação e links conferidos; ver [[05 - Gate de integridade QA]]. Nenhum CT da correção foi executado.

## Reteste QA — 2026-11-11

8/8 CTs passaram em fixtures; gate QA final aguarda sincronização dos Fixes DEV; [[03 - Validação dev]] e [[06 - Evidências QA]]. Pai mantém QA_REJECTED/no-go devido a CTs bloqueados e NXG-035.
