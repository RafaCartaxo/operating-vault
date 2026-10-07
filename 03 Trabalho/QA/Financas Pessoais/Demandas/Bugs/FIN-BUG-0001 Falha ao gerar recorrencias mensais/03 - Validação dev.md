---
demanda: "[[01 - Bug]]"
execucao: ""
ambiente: dev
versao: ""
status: concluido
responsavel: ""
resultado: aprovado
# Pontos da etapa de validação; substitua pelo valor planejado para esta etapa.
pontos: 0
ct_resultados:
  ct_b01: "✅ Aprovado"
  ct_b02: "✅ Aprovado"
data_inicio: "2026-10-05"
data_fim: "2026-10-05"
---

# Validação — FIN-BUG-0001

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Casos de teste:** [[02 - Casos de teste]]
> **Validação:** [[03 - Validação dev]]
> **Preparação Qase:** [[04 - Preparação Qase]]
> **Fix DEV:** [[03 Trabalho/DEV/Financas Pessoais/Fixes/FIN-FIX-0001/00 README|FIN-FIX-0001 — correção concluída e aprovada em QA]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`  
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Template canônico de validação QA adaptado para o defeito `FIN-BUG-0001`.

> Registro da execução dos CTs e das evidências. Os cenários permanecem em `03 - Casos de teste.md`.

> Dica: use a prévia ao passar o mouse sobre o link do CT; abra a nota somente para editar o cenário.

---

## Contexto

- Ambiente: dev local
- Versão/build: FIN-FIX-0001

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
| [[02 - Casos de teste#^ct-b01\|CT-B01]] | `✅ Aprovado` | consulta mensal retornou HTTP 200 após o fix | erro não reproduzido |  | `= choice(this.ct_resultados.ct_b01 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[02 - Casos de teste#^ct-b02\|CT-B02]] | `✅ Aprovado` | duas consultas consecutivas sem duplicidade | idempotência preservada |  | `= choice(this.ct_resultados.ct_b02 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |

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
    const chave = `ct_b${String(indice + 1).padStart(2, "0")}`;
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

Use esta seção somente quando houver reteste após correção:

- **Rodada inicial — 2026-10-05:** CT-B01 falhou com HTTP 500 e `SQLITE_BUSY`.
- **Correção — 2026-10-05:** [[03 Trabalho/DEV/Financas Pessoais/Fixes/FIN-FIX-0001/00 README|FIN-FIX-0001]] implementado e aprovado tecnicamente.
- **Reteste — 2026-10-05:** CT-B01 e CT-B02 aprovados após o FIN-FIX-0001.

---

## Decisão

**Resultado geral:** aprovado.

---

## Checklist de encerramento QA

- [x] Todos os CTs executados ou com justificativa registrada.
- [x] Evidências e observações preenchidas quando necessário.
- [ ] Bugs filhos vinculados na coluna **Defeito/Bug**.
- [x] Resultado geral definido.
- [x] Status da validação e da demanda atualizados.
- [x] Próximo passo registrado.
- [x] Sincronização documental verificada: frontmatter, README, board, links, evidências, histórico e pendências.
