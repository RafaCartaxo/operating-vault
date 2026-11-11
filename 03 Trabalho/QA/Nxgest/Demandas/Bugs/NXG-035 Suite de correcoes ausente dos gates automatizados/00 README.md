---
status: execucao
tipo: bug
etapa_atual: "DEV · Análise técnica"
projeto: nxgest
pai: NXG-MEL-0009
---

# NXG-035 — Suite de correcoes ausente dos gates automatizados


> [!info]- Navegação QA/DEV
> **Bug:** [[01 - Bug]]<br>
> **Pai:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/01 - Demanda|NXG-MEL-0009]].
> **Casos de teste:** [[02 - Casos de teste]]<br>
> **Preparação Qase:** [[04 - Preparação Qase]]<br>
> **Fix DEV:** aguardando encaminhamento pela Coordenação.
> **Validação QA:** [[03 - Validação dev|Validação QA]] — criada junto com o Bug, copiando `Templates/QA/04 - Validação dev.md` e renomeando para `03 - Validação dev.md`.

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`<br>
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!info]- Cards relacionados
> **Bug:** [[01 - Bug]]<br>
> **Casos de teste:** [[02 - Casos de teste]]<br>
> **Validação:** [[03 - Validação dev]]<br>
> **Preparação Qase:** [[04 - Preparação Qase]]<br>
> **Fix DEV:** aguardando encaminhamento pela Coordenação.

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
> dv.paragraph(`**${id || "NXG-035"} — Retrabalho por defeitos derivados:** ${adicional} pontos (${derivados.length} defeitos)`);
> ```

Pacote QA para `NXG-035`:

```text
NXG-035/
├── 00 README.md
├── 01 - Bug.md
├── 02 - Casos de teste.md
├── 03 - Validação dev.md
└── 04 - Preparação Qase.md
```

O arquivo de validação nasce junto com o Bug e é preenchido após o Fix DEV.

---


Cada CT usa um callout recolhível com identificador (`^ct-b01`). A nota de validação aponta para esse bloco na tabela; ao passar o mouse sobre o link, o Obsidian mostra a prévia do cenário completo.

## Estado

QA_READY_FOR_DEV após auditoria estrutural; sete CTs aguardando implementação e reteste. Coordenação encaminha; QA não despacha DEV.

## Gate de integridade — 2026-11-11

Cinco critérios e sete CTs planejados. [[05 - Gate de integridade QA|Evidência do gate]]. Nenhum CT foi executado; CI GitHub e isolamento do runner real não foram verificados.
