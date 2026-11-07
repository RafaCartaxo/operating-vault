---
demanda: "[[01 - Bug]]"
execucao: "[[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/00 README]]"
ambiente: dev
versao: "c7b65c8ddd85efde4db7f075ca03d95a7c6c5c38"
status: "concluido"
responsavel: "NX Gest · QA e Coordenação"
resultado: "aprovado"
# Pontos da etapa de validação; substitua pelo valor planejado para esta etapa.
pontos: 5
ct_resultados:
  ct_b01: "✅ Aprovado"
  ct_b02: "✅ Aprovado"
data_inicio: "2026-11-07"
data_fim: "2026-11-07"
projeto: "nxgest"
epico: "NXG-EPIC-0001"
---

# Validação — NXG-029

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Bug]]  
> **Plano de teste:** [[02 - Casos de teste]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Validação:** [[03 - Validação dev]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/00 README|Execução DEV]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`  
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Template canônico de validação QA para melhorias e bugs. Para Bugs, copie esta nota, renomeie para `03 - Validação dev.md` e troque os links/identificadores `CT-001` pelos CTs `CT-BNN` do bug.

> Registro da execução dos CTs e das evidências. Os cenários permanecem em `03 - Casos de teste.md`.

> Dica: use a prévia ao passar o mouse sobre o link do CT; abra a nota somente para editar o cenário.

---

## Contexto

- Ambiente: dev isolado, sem acesso a infraestrutura real.
- Versão/build: revisão final a registrar após entrega DEV.
- Evidências: logs locais saneados e registros DEV vinculados.

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
| [[02 - Casos de teste#^ct-b01\|CT-B01]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_b01]` | [[06 - Evidências QA|Evidências independentes]] | Carregador Bash aceitou legado MAIL_FROM_NAME com espaço, sem Node no host e sem executar texto de shell. QA confirmou arquivo inalterado em fixture própria. | — | 0 |
| [[02 - Casos de teste#^ct-b02\|CT-B02]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_b02]` | [[06 - Evidências QA|Evidências independentes]] | test:safety cobre geração nova, reutilização byte a byte, chave desconhecida e valores literais; permissões e política console preservadas em ambiente sintético. | — | 0 |

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

- **Rodada inicial:** registre o CT reprovado e o defeito aberto.
- **Correção:** vincule o bug e o Fix DEV.
- **Reteste:** registre o resultado final e a data.

---

## Decisão

**Resultado geral:** aprovado

---

## Checklist de encerramento QA

- [x] Todos os CTs executados ou com justificativa registrada.
- [x] Evidências e observações preenchidas quando necessário.
- [x] Bugs filhos vinculados na coluna **Defeito/Bug**.
- [x] Resultado geral definido.
- [x] Status da validação e da demanda atualizados.
- [x] Próximo passo registrado.
- [x] Sincronização documental verificada: frontmatter, README, board, links, evidências, histórico e pendências.

## Execução independente — 2026-11-07

QA executou os CTs e verificou a revisão final. Resultados e limites em [[06 - Evidências QA]]. Nenhuma aprovação funcional foi emitida pelo DEV. A aprovação destes pacotes não encerra o épico nem autoriza push/deploy.
