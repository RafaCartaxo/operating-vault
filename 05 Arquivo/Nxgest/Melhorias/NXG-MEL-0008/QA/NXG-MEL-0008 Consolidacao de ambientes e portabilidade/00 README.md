---
projeto: "nxgest"
epico: "NXG-EPIC-0001"
responsavel: "NX Gest · QA e Coordenação"
id: "NXG-MEL-0008"
status: "concluido"
etapa_atual: "Concluído"
tipo: "melhoria"
data_inicio: "2026-11-07"
pontos: 1
data_fim: "2026-11-07"
execucao: "[[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/00 README]]"
---
# NXG-MEL-0008 — Consolidacao de ambientes e portabilidade


> [!info]- Navegação QA/DEV
> **Demanda:** [[01 - Demanda]]  
> **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|NXG-EPIC-0001]]
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/00 README|Execução DEV]]

## Auditoria de integridade QA

> Executar antes de mover o card para `QA_READY_FOR_DEV`:
>
> ```bash
> python3 scripts/validar_pacote_qa.py "<pasta-da-demanda>"
> ```

- **Responsável pela execução:** QA/`qa-first-delivery`
- **Data da última execução:** 2026-11-07
- **Resultado do gate:** PACOTE QA APROVADO NO GATE DE INTEGRIDADE
- **Evidência detalhada:** saída do comando no registro da execução ou na daily relacionada.

O handoff para DEV só é permitido com resultado `PACOTE QA APROVADO NO GATE DE INTEGRIDADE`.

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!info]- Cards relacionados
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/00 README|Execução DEV]]

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
> const projeto = String(dv.current().projeto || "").toLowerCase();
> const id = (dv.current().file.folder.match(/(?:[A-Z]{2,8}-)?MEL-\d+/) || [""])[0];
> const defeitos = dv.pages().where(p => projeto && p.file.path.includes(`03 Trabalho/QA/${projeto}/Demandas/Bugs`) && String(p.pai ?? "").includes(id));
> const adicional = defeitos.array().reduce((soma, pagina) => soma + (typeof pagina.pontos === "number" ? pagina.pontos : 0), 0);
> const original = dv.pages().where(p => id && p.file.path.includes(id) && typeof p.pontos === "number").array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.table(["Defeito filho", "Pontos"], defeitos.map(p => [p.file.link, p.pontos ?? 0]));
> dv.paragraph(`**${id || "NXG-MEL-0008"} — Retrabalho por defeitos filhos:** ${adicional} pontos (${defeitos.length} defeitos)`);
> ```

Pacote QA para `NXG-MEL-0008`:

```text
NXG-MEL-0008/
├── 00 README.md
├── 01 - Demanda.md
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
├── 04 - Validação dev.md
└── 05 - Preparação Qase.md
```

---

## Histórico e autorização

- 2026-11-07: usuário autorizou executar a checklist até o parecer final, com delegação e decisões técnicas. Inclui implementação, registros, validação e commits locais; sem push/deploy/encerramento do épico.
- Pacote copiado dos templates oficiais e adaptado por QA. Handoff depende de auditoria e sincronização.

## Resultado final QA

QA_APPROVED com ressalvas não bloqueantes de documentação/abrangência do teste. [[06 - Evidências QA|Resultados e limites]]. Épico encerrado em 2026-11-10 após aceite do usuário; evidências anteriores preservadas.
