---
demanda: "[[01 - Demanda]]"
execucao: "[[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/00 README]]"
ambiente: dev
versao: "c7b65c8ddd85efde4db7f075ca03d95a7c6c5c38"
status: "concluido"
responsavel: "NX Gest · QA e Coordenação"
resultado: "aprovado_com_ressalvas"
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
data_inicio: "2026-11-07"
data_fim: "2026-11-07"
projeto: "nxgest"
epico: "NXG-EPIC-0001"
---

# Validação — NXG-MEL-0008

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/00 README|Execução DEV]]

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
| [[03 - Casos de teste#^ct-001\|CT-001]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_001]` | [[06 - Evidências QA|Evidências independentes]] | Exemplo único e configurações sintéticas dos três Compose; caminhos de build/Caddy verificados; envs reais não lidos. | — | 0 |
| [[03 - Casos de teste#^ct-002\|CT-002]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002]` | [[06 - Evidências QA|Evidências independentes]] | npm ci em árvore sem dependências/build/env/uploads; início pelo npm run dev; HTTPS e proxy API responderam 200. | — | 0 |
| [[03 - Casos de teste#^ct-003\|CT-003]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_003]` | [[06 - Evidências QA|Evidências independentes]] | Container QA exclusivo em loopback:55439 com tmpfs, bancos/portas próprios; original nxgest-pg-dev:5433 preservado e saudável; recursos QA removidos. | — | 0 |
| [[03 - Casos de teste#^ct-004\|CT-004]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_004]` | [[06 - Evidências QA|Evidências independentes]] | 46 arquivos/215 testes, build e check-dist aprovados em 7099a97; src/frontend/tsconfig/lock idênticos na revisão final. Auditorias finais com zero erros; 5 avisos classificados. | — | 0 |
| [[03 - Casos de teste#^ct-005\|CT-005]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_005]` | [[06 - Evidências QA|Evidências independentes]] | Login 200, criação 201, leitura/listagem 200; documento e CEP mantidos após reinício do backend no checkout limpo. | — | 0 |
| [[03 - Casos de teste#^ct-006\|CT-006]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_006]` | [[06 - Evidências QA|Evidências independentes]] | 45 rastreados + 20 novos preservados e restauração conferida; 8 arquivos de ícones/Qase iguais aos originais na branch WIP. Commits locais explícitos, sem push/deploy. | — | 0 |
| [[03 - Casos de teste#^ct-007\|CT-007]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_007]` | [[06 - Evidências QA|Evidências independentes]] | Checkout em caminho independente validado; pasta definitiva nxgest organizada por DEV com metadados dos envs preservados. macOS e outro computador não foram executados. | — | 0 |
| [[03 - Casos de teste#^ct-008\|CT-008]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_008]` | [[06 - Evidências QA|Evidências independentes]] | Demanda, CTs, evidências, governança e boards sincronizados; épico continua execucao aguardando decisão do usuário no parecer final. | — | 0 |

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

Use esta seção somente quando houver reteste após correção:

- **Rodada inicial:** registre o CT reprovado e o defeito aberto.
- **Correção:** vincule o bug e o Fix DEV.
- **Reteste:** registre o resultado final e a data.

---

## Decisão

**Resultado geral:** aprovado com ressalvas documentais e de abrangência de ambiente, sem bloqueio técnico local

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
