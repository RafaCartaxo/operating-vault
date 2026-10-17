---
demanda: "[[01 - Demanda]]"
execucao: "[[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0006/DEV/NXG-MEL-0006/00 README|Execução NXG-MEL-0006]]"
ambiente: dev
versao: ""
status: concluido
responsavel: qa-first-delivery
resultado: aprovado_com_ressalvas
pontos: 2
ct_resultados:
  ct_001: "✅ Aprovado"
  ct_002: "✅ Aprovado"
  ct_003: "✅ Aprovado"
  ct_004: "✅ Aprovado"
  ct_005: "✅ Aprovado"
  ct_006: "✅ Aprovado"
  ct_007: "✅ Aprovado"
data_inicio: "2026-10-17"
data_fim: "2026-10-17"
---

# Validação — NXG-MEL-0006

> [!info]- Navegação QA
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`  
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Registro da execução dos CTs e das evidências, a preencher após a execução DEV ser autorizada e concluída. Os cenários permanecem em `03 - Casos de teste.md`.

---

## Contexto

- Ambiente: dev/repositório local
- Versão/build: não aplicável — lote de onboarding, sem alteração de código de aplicação

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
| [[03 - Casos de teste#^ct-001\|CT-001]] | ✅ Aprovado | `npm run db:up` executado de verdade pelo Executor — "Container nxgest-pg-dev Running" | Reexecução independente pelo Orquestrador bloqueada por permissão do socket Docker nesta sessão; evidência real do Executor aceita | | 0.29 |
| [[03 - Casos de teste#^ct-002\|CT-002]] | ✅ Aprovado | `README.md` (Instalação Rápida) usa `npm run db:up` | — | | 0.29 |
| [[03 - Casos de teste#^ct-003\|CT-003]] | ✅ Aprovado | `08-SETUP-NOVA-MAQUINA.md` Passo 4 e checklist da seção 9 (corrigido na Rodada 2) usam `npm run db:up`/`npm run db:ps` | — | | 0.29 |
| [[03 - Casos de teste#^ct-004\|CT-004]] | ✅ Aprovado | `cp .env.example .env` inalterado; nenhuma linha de configuração de ambiente tocada | — | | 0.29 |
| [[03 - Casos de teste#^ct-005\|CT-005]] | ✅ Aprovado | `rg -n "docker compose up -d postgres\|docker compose ps" README.md docs/engineering/08-SETUP-NOVA-MAQUINA.md` → zero ocorrências residuais | Mesma ressalva de permissão do socket Docker do CT-001 | | 0.29 |
| [[03 - Casos de teste#^ct-006\|CT-006]] | ✅ Aprovado | `scripts/deploy.sh`, `scripts/deploy-staging.sh`, `.opencode/agents/ops-runner.md`, `docs/engineering/06-PRODUCAO.md` e `infra/` não tocados neste lote (confirmado por diff) | — | | 0.29 |
| [[03 - Casos de teste#^ct-007\|CT-007]] | ✅ Aprovado | `git diff --check` exit 0; `package.json` válido (`JSON.parse`); `git status -sb` isolado ao escopo, 27+10 protegidos intactos | — | | 0.29 |

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

**Resultado geral:** ✅ Aprovado com ressalvas.

> **Ressalva (limitação de ambiente desta sessão, não um defeito do lote):** a evidência real de `npm run db:up`/`npm run db:ps` funcionando (container `nxgest-pg-dev` saudável) foi produzida e registrada pelo Executor na execução DEV. Uma reexecução independente desses comandos pelo Orquestrador, nesta sessão, está bloqueada por permissão do socket Docker — não reflete um problema na implementação, apenas uma restrição do ambiente de verificação. A evidência do Executor foi aceita como válida.

## Checklist de encerramento QA

- [x] Todos os CTs executados (CT-001 a CT-007, todos aprovados).
- [x] Evidências e observações preenchidas.
- [x] Nenhum bug filho aberto (nenhum CT reprovado).
- [x] Resultado geral definido: aprovado com ressalvas.
- [x] Status da validação e da demanda atualizados.
- [x] Próximo passo registrado: lote concluído; arquivar em `05 Arquivo/`.
- [x] Sincronização documental verificada: frontmatter, README, board, links, evidências, histórico e pendências.
