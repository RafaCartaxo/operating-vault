---
status: execucao
tipo: melhoria
etapa_atual: "DEV · Análise técnica"
projeto: nxgest
---

# NXG-MEL-0009 — Backup recuperável e rollback do serviço


> [!info]- Navegação QA/DEV
> **Demanda:** [[01 - Demanda]]  
> **Épico:** demanda separada; épico de organização permanece concluído.
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** será criada pelo DEV após encaminhamento da Coordenação.

## Auditoria de integridade QA

> Executar antes de mover o card para `QA_READY_FOR_DEV`:
>
> ```bash
> python3 scripts/validar_pacote_qa.py "<pasta-da-demanda>"
> ```

- **Responsável pela execução:** QA/`qa-first-delivery`
- **Data da última execução:** 2026-11-10
- **Resultado do gate:** QA_REJECTED na rodada de validação funcional; integridade inicial do pacote segue aprovada
- **Evidência detalhada:** [[06 - Gate de integridade QA]].

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
> **Execução DEV:** será criada pelo DEV após encaminhamento da Coordenação.

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
> dv.paragraph(`**${id || "NXG-MEL-0009"} — Retrabalho por defeitos filhos:** ${adicional} pontos (${defeitos.length} defeitos)`);
> ```

Pacote QA para `NXG-MEL-0009`:

```text
NXG-MEL-0009/
├── 00 README.md
├── 01 - Demanda.md
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
├── 04 - Validação dev.md
└── 05 - Preparação Qase.md
```

---

## Histórico e próximo responsável

2026-11-10: pacote de QA independente criado a partir dos templates oficiais após proposta da Coordenação; integridade, rastreabilidade e sincronização conferidas; QA_READY_FOR_DEV. Não há CT executado. Próximo responsável pelo encaminhamento: Coordenação; DEV recebe somente após gate e despacho da Coordenação. Sem commit, push, deploy, SSH, segredos ou recursos reais.

## Validação independente — 2026-11-11

QA_REJECTED: 8 CTs aprovados localmente, 3 falharam e 3 bloqueados. Consultar [[04 - Validação dev]] e [[07 - Evidências QA]]. Defeitos filhos NXG-032, NXG-033 e NXG-034 aguardam Coordenação; teste real e publicação permanecem fora do escopo.

## Retrabalho preparado — 2026-11-11

NXG-032/033/034: QA_READY_FOR_DEV, 4 critérios e 8 CTs por pacote; Coordenação encaminha. O QA_REJECTED da demanda pai permanece vigente e a violação anterior de isolamento não é apagada por testes futuros.
