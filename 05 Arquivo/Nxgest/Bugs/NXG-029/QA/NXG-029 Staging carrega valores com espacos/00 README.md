---
projeto: "nxgest"
epico: "NXG-EPIC-0001"
responsavel: "NX Gest · QA e Coordenação"
id: "NXG-029"
status: "concluido"
etapa_atual: "Concluído"
tipo: "bug"
data_inicio: "2026-11-07"
pontos: 1
data_fim: "2026-11-07"
execucao: "[[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/00 README]]"
---
# NXG-029 — Staging carrega valores com espacos


> [!info]- Navegação QA/DEV
> **Bug:** [[01 - Bug]]  
> **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|NXG-EPIC-0001]]
> **Casos de teste:** [[02 - Casos de teste]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Fix DEV:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/00 README|Execução DEV]]
> **Validação QA:** [[03 - Validação dev|Validação QA]] — criada junto com o Bug, copiando `Templates/QA/04 - Validação dev.md` e renomeando para `03 - Validação dev.md`.

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!info]- Cards relacionados
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Validação:** [[03 - Validação dev]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Fix DEV:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/00 README|Execução DEV]]

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
> dv.paragraph(`**${id || "NXG-029"} — Retrabalho por defeitos derivados:** ${adicional} pontos (${derivados.length} defeitos)`);
> ```

Pacote QA para `NXG-029`:

```text
NXG-029/
├── 00 README.md
├── 01 - Bug.md
├── 02 - Casos de teste.md
├── 03 - Validação dev.md
└── 04 - Preparação Qase.md
```

O arquivo de validação nasce junto com o Bug e é preenchido após o Fix DEV.

---


Cada CT usa um callout recolhível com identificador (`^ct-b01`). A nota de validação aponta para esse bloco na tabela; ao passar o mouse sobre o link, o Obsidian mostra a prévia do cenário completo.

## Histórico e autorização

- 2026-11-07: usuário autorizou executar a checklist até o parecer final, com delegação e decisões técnicas. Inclui implementação, registros, validação e commits locais; sem push/deploy/encerramento do épico.
- Pacote copiado dos templates oficiais e adaptado por QA. Handoff depende de auditoria e sincronização.

## Gate de integridade QA

2026-11-07: auditoria específica para template de bug aprovada: 5 notas, 2 critérios, 2 CTs, âncoras únicas, cobertura e linhas YAML/validação correspondentes. O validador padrão do vault é exclusivo de melhoria; não foi adaptado artificialmente para bugs.

## Resultado final QA

QA_APPROVED — todos os CTs aprovados. [[06 - Evidências QA|Resultados e limites]]. Épico permanece em execução aguardando parecer final ao usuário.
