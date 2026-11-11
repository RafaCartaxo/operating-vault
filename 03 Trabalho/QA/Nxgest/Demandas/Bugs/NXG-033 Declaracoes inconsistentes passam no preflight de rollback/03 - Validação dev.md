---
demanda: "[[01 - Bug]]"
execucao: ""
ambiente: dev
versao: "c7b65c8 + working tree reteste"
status: concluido
responsavel: "NX Gest · QA"
resultado: aprovado_com_ressalvas
# Pontos da etapa de validação; substitua pelo valor planejado para esta etapa.
pontos: 0
ct_resultados:
  ct_001: "✅ Aprovado"
  ct_002: "✅ Aprovado"
  ct_003: "✅ Aprovado"
  ct_004: "✅ Aprovado"
  ct_005: "✅ Aprovado"
  ct_006: "✅ Aprovado"
  ct_007: "✅ Aprovado"
  ct_008: "✅ Aprovado"
data_inicio: 2026-11-11
data_fim: 2026-11-11
---

# Validação — NXG-033

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Bug]]  
> **Plano de teste:** [[02 - Casos de teste]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Validação:** [[03 - Validação dev]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Execução DEV:** pendente de encaminhamento da Coordenação.

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`  
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Template canônico de validação QA para melhorias e bugs. Para Bugs, copie esta nota, renomeie para `03 - Validação dev.md` e troque os links/identificadores `CT-B01` pelos CTs `CT-BNN` do bug.

> Registro da execução dos CTs e das evidências. Os cenários permanecem em `02 - Casos de teste.md`.

> Dica: use a prévia ao passar o mouse sobre o link do CT; abra a nota somente para editar o cenário.

---

## Contexto

- Ambiente: fixtures/dublês; isolamento e interceptação a confirmar antes de executar.
- Versão: c7b65c8 + delta dos Fixes no working tree; 8 CTs aprovados no escopo sintético; sem execução operacional real.

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
| [[02 - Casos de teste#^ct-b01\|CT-B01]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_001]` | [[06 - Evidências QA#^ev-b01\|Evidência]] | Schema desconhecido/incompatível e ausência são recusados ou mantidos em NO-GO — case-06 e revisão preflight. | — | `= choice(this.ct_resultados.ct_001 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[02 - Casos de teste#^ct-b02\|CT-B02]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002]` | [[06 - Evidências QA#^ev-b02\|Evidência]] | Schema estruturado contraditório com hash recalculado é recusado — case-06. | — | `= choice(this.ct_resultados.ct_002 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[02 - Casos de teste#^ct-b03\|CT-B03]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_003]` | [[06 - Evidências QA#^ev-b03\|Evidência]] | Comparação sintética detecta SHA/imagem divergentes e não libera produção — case-13; preflight real permanece NO-GO. | — | `= choice(this.ct_resultados.ct_003 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[02 - Casos de teste#^ct-b04\|CT-B04]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_004]` | [[06 - Evidências QA#^ev-b04\|Evidência]] | Montagem/runtime divergente e prova de configuração ausente bloqueiam; sem validação real — case-06 e revisão. | — | `= choice(this.ct_resultados.ct_004 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[02 - Casos de teste#^ct-b05\|CT-B05]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_005]` | [[06 - Evidências QA#^ev-b05\|Evidência]] | Health negativo/timeout e integridade não declarada falham; mesmo health positivo permanece NO-GO sem SHA efetivo/integridade verificáveis — case-07. | — | `= choice(this.ct_resultados.ct_005 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[02 - Casos de teste#^ct-b06\|CT-B06]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_006]` | [[06 - Evidências QA#^ev-b06\|Evidência]] | Revisão humana não substituída por fixture; guardas de subprocessos e isolamento verificados — resultados.json e runbooks. | — | `= choice(this.ct_resultados.ct_006 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[02 - Casos de teste#^ct-b07\|CT-B07]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_007]` | [[06 - Evidências QA#^ev-b07\|Evidência]] | Fonte real ausente leva a NO-GO, comparação sintética não é autoridade operacional — case-06 e case-13. | — | `= choice(this.ct_resultados.ct_007 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[02 - Casos de teste#^ct-b08\|CT-B08]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_008]` | [[06 - Evidências QA#^ev-b08\|Evidência]] | Bundle divergente é recusado por comparador sintético; retorno operacional mantém NO-GO — independente-3 e case-07. | — | `= choice(this.ct_resultados.ct_008 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |

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

> A prévia do CT é exibida pelo Obsidian ao passar o mouse sobre cada link. A tabela é o registro da execução; o conteúdo do cenário permanece em `02 - Casos de teste.md`.

---

## Histórico de validação

- 2026-11-11: reteste independente, 8/8 aprovados em escopo sintético. O desvio histórico do CLI Docker permanece registrado no pai; não foi apagado por esta rodada.

Use esta seção somente quando houver reteste após correção:

- **Rodada inicial:** registre o CT reprovado e o defeito aberto.
- **Correção:** vincule o bug e o Fix DEV.
- **Reteste:** registre o resultado final e a data.

---

## Decisão

**Resultado geral:** QA_APPROVED com ressalvas: 8/8 CTs passaram em fixtures/dublês, e sincronização DEV foi conferida. Sem validação real ou go operacional; pai permanece QA_REJECTED. Ver [[06 - Evidências QA]].

---

## Checklist de encerramento QA

- [x] Todos os CTs executados ou com justificativa registrada.
- [x] Evidências e observações preenchidas quando necessário.
- [x] Bugs filhos: não aplicável; nenhum defeito filho novo neste reteste.
- [x] Resultado da rodada e gate final definidos com ressalvas.
- [x] Status da validação e da demanda atualizados.
- [x] Próximo passo: Coordenação conduzir NXG-035; pai permanece NO-GO.
- [x] Registros e board QA verificados; atualização dos registros DEV comunicada à Coordenação.

## Gate final — 2026-11-11

QA_APPROVED com ressalvas para o escopo sintético; decisão baseada no reteste independente já registrado, sem repetição. A sincronização DEV foi conferida nos cinco documentos do Fix. A Coordenação recebe o resultado para sincronizar os registros sob responsabilidade DEV.
