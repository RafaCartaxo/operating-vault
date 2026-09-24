---
demanda: "[[01 - Demanda|MEL-0002 Cliente Documento]]"
execucao: "[[05 Arquivo/Nxgest/Melhorias/MEL-0002/DEV/MEL-0002/00 README|MEL-0002 — execução]]"
ambiente: dev
versao: a preencher
status: concluido
responsavel: ""
resultado: aprovado
pontos: 10
ct_resultados:
  ct_001: ✅ Aprovado
  ct_002: ✅ Aprovado
  ct_003: ✅ Aprovado
  ct_004: ✅ Aprovado
  ct_005: ✅ Aprovado
  ct_006: ✅ Aprovado
  ct_007: ✅ Aprovado
  ct_008: ✅ Aprovado
data_inicio: 2026-09-10
data_fim: "2026-09-11"
---
# Validação — MEL-0002

> [!info]- Navegação QA
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Melhorias/MEL-0002/DEV/MEL-0002/00 README|MEL-0002 — execução]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`  
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Validação funcional dos CTs da melhoria. Preencher resultado e evidência durante a execução.

> Dica: passe o mouse sobre o link de um CT na tabela para abrir a prévia; clique apenas quando precisar editar o cenário.

---

## Contexto

- **Ambiente:** dev
- **Versão/build:** a preencher
- **Escopo da rodada:** [[03 - Casos de teste|MEL-0002 completa (CT-001 a CT-008)]]

---

## Como registrar a validação

- Em cada CT, selecione o resultado no campo interativo da tabela.
- Adicione screenshot, resposta da API ou observação reproduzível na coluna de evidência.
- Se falhar, abra um bug filho com `pai: MEL-0002`.

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

| CT                                      | Resultado | Evidência | Observação | Defeito/Bug | Pontos entregues |
| :-------------------------------------- | :-------: | --------- | ---------- | :---------: | :--------------: |
| [[03 - Casos de teste#^ct-001\|CT-001]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_001]` |           |            |             | `= choice(this.ct_resultados.ct_001 = "✅ Aprovado", round(number(this.pontos) / 8, 2), 0)` |
| [[03 - Casos de teste#^ct-002\|CT-002]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002]` |           |            |             | `= choice(this.ct_resultados.ct_002 = "✅ Aprovado", round(number(this.pontos) / 8, 2), 0)` |
| [[03 - Casos de teste#^ct-003\|CT-003]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_003]` |           |            |             | `= choice(this.ct_resultados.ct_003 = "✅ Aprovado", round(number(this.pontos) / 8, 2), 0)` |
| [[03 - Casos de teste#^ct-004\|CT-004]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_004]` |           |            |             | `= choice(this.ct_resultados["ct_004"] = "✅ Aprovado", round(this.pontos / 8, 2), 0)` |
| [[03 - Casos de teste#^ct-005\|CT-005]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_005]` |           |            |             | `= choice(this.ct_resultados.ct_005 = "✅ Aprovado", round(number(this.pontos) / 8, 2), 0)` |
| [[03 - Casos de teste#^ct-006\|CT-006]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_006]` |           |            |             | `= choice(this.ct_resultados.ct_006 = "✅ Aprovado", round(number(this.pontos) / 8, 2), 0)` |
| [[03 - Casos de teste#^ct-007\|CT-007]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_007]` |           |            |             | `= choice(this.ct_resultados.ct_007 = "✅ Aprovado", round(number(this.pontos) / 8, 2), 0)` |
| [[03 - Casos de teste#^ct-008\|CT-008]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_008]` |           |            |             | `= choice(this.ct_resultados.ct_008 = "✅ Aprovado", round(number(this.pontos) / 8, 2), 0)` |

```dataviewjs
const pagina = dv.current() ?? {};
const resultados = pagina.ct_resultados ?? {};
const pontosEtapa = Number(pagina.pontos) || 0;
const totalCTs = Object.keys(resultados).length;
const aprovados = Object.values(resultados).filter((resultado) => String(resultado).includes("Aprovado")).length;
const pesoDoStatus = (resultado) => {
  const status = String(resultado);
  if (status.includes("Aprovado") || status.includes("Falhou")) return 1;
  if (status.includes("Em andamento")) return 0.25;
  if (status.includes("Bloqueado")) return 0.5;
  return 0;
};
const executados = Object.values(resultados).filter((resultado) => pesoDoStatus(resultado) > 0).length;
const pontosPorCT = totalCTs ? pontosEtapa / totalCTs : 0;
const pontosEntregues = Math.round(Object.values(resultados).reduce((total, resultado) =>
  total + pontosPorCT * pesoDoStatus(resultado), 0) * 100) / 100;

// As consultas inline não re-renderizam de forma confiável dentro de tabelas
// quando o Meta Bind altera o frontmatter. Atualizamos somente a coluna de
// pontos da tabela, preservando os campos interativos de resultado.
const raiz = dv.container.closest(".markdown-preview-view") ?? document;
const tabela = Array.from(raiz.querySelectorAll("table")).find((item) =>
  item.innerText.includes("Pontos entregues")
);
if (tabela) {
  Array.from(tabela.querySelectorAll("tbody tr")).forEach((linha, indice) => {
    const chave = `ct_${String(indice + 1).padStart(3, "0")}`;
    const celula = linha.lastElementChild;
    if (!celula) return;
    const pontos = pontosPorCT * pesoDoStatus(resultados[chave]);
    celula.textContent = pontos ? (Math.round(pontos * 100) / 100).toString() : "0";
  });
}
```

> **Regra de esforço:** aprovado e falhou = 100% da parcela; em andamento = 25%; bloqueado = 50%; aguardando e não executado = 0%.

---

## Ocorrências e defeitos

Nenhum registrado até o momento.

---

## Decisão da validação

**Resultado:** aprovado  
**Próximo passo:** encerrar a demanda e registrar a entrega.
