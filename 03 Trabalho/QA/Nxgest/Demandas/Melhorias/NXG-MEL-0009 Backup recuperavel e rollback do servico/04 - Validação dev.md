---
demanda: "[[01 - Demanda]]"
execucao: ""
ambiente: dev
versao: "c7b65c8 + delta MEL-0009 em working tree"
status: concluido
responsavel: "NX Gest · QA"
resultado: reprovado
# Pontos da etapa de validação; substitua pelo valor planejado para esta etapa.
pontos: 5
ct_resultados:
  ct_001: "✅ Aprovado"
  ct_002: "✅ Aprovado"
  ct_003: "✅ Aprovado"
  ct_004: "✅ Aprovado"
  ct_005: "✅ Aprovado"
  ct_006: "✅ Aprovado"
  ct_007: "✅ Aprovado"
  ct_008: "✅ Aprovado"
  ct_009: "✅ Aprovado"
  ct_010: "✅ Aprovado"
  ct_011: "🚫 Bloqueado"
  ct_012: "✅ Aprovado"
  ct_013: "🚫 Bloqueado"
  ct_014: "✅ Aprovado"
data_inicio: 2026-11-10
data_fim: 2026-11-11
---

# Validação — NXG-MEL-0009

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** será criada pelo DEV após encaminhamento da Coordenação.

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`  
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Template canônico de validação QA para melhorias e bugs. Para Bugs, copie esta nota, renomeie para `03 - Validação dev.md` e troque os links/identificadores `CT-001` pelos CTs `CT-BNN` do bug.

> Registro da execução dos CTs e das evidências. Os cenários permanecem em `03 - Casos de teste.md`.

> Dica: use a prévia ao passar o mouse sobre o link do CT; abra a nota somente para editar o cenário.

---

## Contexto

- Ambiente: fixtures e dublês locais; sem recursos reais.
- Versão/build: HEAD c7b65c8 + delta MEL-0009 no working tree.
- Rodada QA 2026-11-11: 8 aprovados, 3 falharam e 3 bloqueados; sem teste real de restauração.

---

## Resumo da execução

```dataviewjs
const paginaResumo = dv.current() ?? {};
const resultadosResumo = paginaResumo.ct_resultados ?? {};
const pontosEtapaResumo = Number(paginaResumo.pontos) || 0;
const totalCTsResumo = Object.keys(resultadosResumo).length;
const aprovadosResumo = Object.values(resultadosResumo).filter((resultado) => String(resultado).includes("Aprovado")).length;
const pesoResumo = (resultado) => {
  const status = String(resultado);
  if (status.includes("Aprovado") || status.includes("Falhou")) return 1;
  if (status.includes("Em andamento")) return 0.25;
  if (status.includes("Bloqueado")) return 0.5;
  return 0;
};
const executadosResumo = Object.values(resultadosResumo).filter((resultado) => pesoResumo(resultado) > 0).length;
const pontosEntreguesResumo = totalCTsResumo
  ? Math.round(Object.values(resultadosResumo).reduce((total, resultado) => total + (pontosEtapaResumo / totalCTsResumo) * pesoResumo(resultado), 0) * 100) / 100
  : 0;

dv.list([
  `CTs aprovados: ${aprovadosResumo}/${totalCTsResumo}`,
  `CTs executados: ${executadosResumo}/${totalCTsResumo}`,
  `Pontos da etapa: ${pontosEtapaResumo}`,
  `Pontos entregues: ${pontosEntreguesResumo} de ${pontosEtapaResumo}`,
]);
```

---

## Resultado dos casos de teste

| CT | Resultado | Evidência | Observação | Defeito/Bug | Pontos entregues |
|---|---|---|---|---|---:|
| [[03 - Casos de teste#^ct-001\|CT-001]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_001]` | [[07 - Evidências QA#^ev-001\|Evidência]] | Conjunto sintético, hashes e tag dublada; 10/10 suíte backup. | — | `= choice(this.ct_resultados.ct_001 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-002\|CT-002]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002]` | [[07 - Evidências QA#^ev-002\|Evidência]] | Vazio legítimo aceito; acesso recusado. | — | `= choice(this.ct_resultados.ct_002 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-003\|CT-003]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_003]` | [[08 - Evidências reteste QA#^ev-003\|Reteste]] | Retestado em fixtures; sem prova operacional real | Resolvido localmente | `= choice(this.ct_resultados.ct_003 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-004\|CT-004]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_004]` | [[07 - Evidências QA#^ev-004\|Evidência]] | Corrupção/mistura de metadados sem ajuste dos hashes recusada; não prova consistência semântica. | — | `= choice(this.ct_resultados.ct_004 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-005\|CT-005]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_005]` | [[08 - Evidências reteste QA#^ev-005\|Reteste]] | Retestado em fixtures; sem prova operacional real | Resolvido localmente | `= choice(this.ct_resultados.ct_005 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-006\|CT-006]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_006]` | [[07 - Evidências QA#^ev-006\|Evidência]] | Colisão/publicação/interrupção não alteram manifesto do conjunto anterior em fixture; revisão do isolamento. | — | `= choice(this.ct_resultados.ct_006 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-007\|CT-007]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_007]` | [[07 - Evidências QA#^ev-007\|Evidência]] | Lock em fixture bloqueia segunda operação; sem daemon. | — | `= choice(this.ct_resultados.ct_007 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-008\|CT-008]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_008]` | [[07 - Evidências QA#^ev-008\|Evidência]] | Dublês validam imagem, tag e ausência de prune; disponibilidade real não verificada. | — | `= choice(this.ct_resultados.ct_008 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-009\|CT-009]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_009]` | [[08 - Evidências reteste QA#^ev-009\|Reteste]] | Retestado em fixtures; sem prova operacional real | Resolvido localmente | `= choice(this.ct_resultados.ct_009 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-010\|CT-010]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_010]` | [[07 - Evidências QA#^ev-010\|Evidência]] | Escolha application/data e autorização são declarações; nenhuma restauração automática; sem comprovar autorização real. | — | `= choice(this.ct_resultados.ct_010 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-011\|CT-011]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_011]` | [[07 - Evidências QA#^ev-011\|Evidência]] | Health negativo/timeout e declaração ausente testados; integridade do serviço restaurado e SHA efetivo dependem de atestação, não comprovados. | — | `= choice(this.ct_resultados.ct_011 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-012\|CT-012]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_012]` | [[08 - Evidências reteste QA#^ev-012\|Reteste]] | Retestado em fixtures; sem prova operacional real | Resolvido localmente | `= choice(this.ct_resultados.ct_012 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-013\|CT-013]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_013]` | [[07 - Evidências QA#^ev-013\|Evidência]] | 12/12 regressão com interceptação atual; DEV invocou CLI Docker real em tentativa anterior, socket inexistente sem daemon. Não há conformidade retroativa. | — | `= choice(this.ct_resultados.ct_013 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-014\|CT-014]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_014]` | [[07 - Evidências QA#^ev-014\|Evidência]] | Documentação separa dublês de restore PostgreSQL real e de go de produção. | — | `= choice(this.ct_resultados.ct_014 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |

> **Regra de esforço:** aprovado e falhou = 100% da parcela; em andamento = 25%; bloqueado = 50%; aguardando e não executado = 0%.

> **Pontos entregues:** a coluna é calculada automaticamente conforme o status de cada CT.

```dataviewjs
const pagina = dv.current() ?? {};
const resultados = pagina.ct_resultados ?? {};
const pontosEtapa = Number(pagina.pontos) || 0;
const totalCTs = Object.keys(resultados).length;
const pesoDoStatus = (resultado) => {
  const status = String(resultado);
  if (status.includes("Aprovado") || status.includes("Falhou")) return 1;
  if (status.includes("Em andamento")) return 0.25;
  if (status.includes("Bloqueado")) return 0.5;
  return 0;
};
const raiz = dv.container.closest(".markdown-preview-view") ?? document;
const tabela = Array.from(raiz.querySelectorAll("table")).find((item) => item.innerText.includes("Pontos entregues"));
if (tabela) {
  const pontosPorCT = totalCTs ? pontosEtapa / totalCTs : 0;
  Array.from(tabela.querySelectorAll("tbody tr")).forEach((linha, indice) => {
    const chave = `ct_${String(indice + 1).padStart(3, "0")}`;
    const celula = linha.lastElementChild;
    if (celula) {
      const pontos = pontosPorCT * pesoDoStatus(resultados[chave]);
      celula.textContent = pontos ? (Math.round(pontos * 100) / 100).toString() : "0";
    }
  });
}
```

> A prévia do CT é exibida pelo Obsidian ao passar o mouse sobre cada link. A tabela é o registro da execução; o conteúdo do cenário permanece em `03 - Casos de teste.md`.

---

## Histórico de validação

- 2026-11-11: reteste independente, 12/14 aprovados localmente; CT-011/013 bloqueados. Novo defeito NXG-035 em triagem; QA_REJECTED/no-go mantido.

- 2026-11-11: QA_REJECTED; defeitos NXG-032, NXG-033 e NXG-034; desvio anterior de isolamento registrado separadamente.

Use esta seção somente quando houver reteste após correção:

- **Rodada inicial:** registre o CT reprovado e o defeito aberto.
- **Correção:** vincule o bug e o Fix DEV.
- **Reteste:** registre o resultado final e a data.

---

## Decisão

**Resultado geral:** QA_REJECTED. Reteste local resolveu CT-003/005/009/012; CT-011 permanece bloqueado por ausência de fonte autenticada real e CT-013 pelo desvio histórico. NXG-035 aponta suíte de correções ausente dos gates automatizados; ver [[08 - Evidências reteste QA]]. Coordenação encaminha correções; sem go de produção.

---

## Checklist de encerramento QA

- [ ] Todos os CTs executados ou com justificativa registrada.
- [ ] Evidências e observações preenchidas quando necessário.
- [ ] Bugs filhos vinculados na coluna **Defeito/Bug**.
- [ ] Resultado geral definido.
- [ ] Status da validação e da demanda atualizados.
- [ ] Próximo passo registrado.
- [ ] Sincronização documental verificada: frontmatter, README, board, links, evidências, histórico e pendências.
