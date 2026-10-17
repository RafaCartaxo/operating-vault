---
demanda: "[[01 - Demanda]]"
execucao: "[[03 Trabalho/DEV/Nxgest/Execuções/NXG-MEL-0005 Infraestrutura em infra/00 README|Execução NXG-MEL-0005]]"
ambiente: dev
versao: ""
status: concluido
responsavel: qa-first-delivery
resultado: aprovado_com_ressalvas
pontos: 5
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

# Validação — NXG-MEL-0005

> [!info]- Navegação QA
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`  
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Registro da execução dos CTs e das evidências. Os cenários permanecem em `03 - Casos de teste.md`.

---

## Contexto

- Ambiente: dev/repositório local (forma final de invocação idêntica à usada pelos scripts/documentação de staging/produção, sem deploy real)
- Versão/build: não aplicável — lote de infraestrutura, sem alteração de código de aplicação

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
| [[03 - Casos de teste#^ct-001\|CT-001]] | ✅ Aprovado | `infra/{Dockerfile,Caddyfile,docker-compose.yml,docker-compose.staging.yml,docker-compose.prod.yml}` presentes; nenhum dos 5 remanescente na raiz | — |  | 0.71 |
| [[03 - Casos de teste#^ct-002\|CT-002]] | ✅ Aprovado | `docker compose --project-directory . -f infra/docker-compose.{yml,staging.yml,prod.yml} config` — exit 0 nos 3 | — |  | 0.71 |
| [[03 - Casos de teste#^ct-003\|CT-003]] | ✅ Aprovado | `scripts/deploy.sh` e `scripts/deploy-staging.sh` apontam para `infra/docker-compose.{prod,staging}.yml` com `--project-directory .` | — |  | 0.71 |
| [[03 - Casos de teste#^ct-004\|CT-004]] | ✅ Aprovado | `.opencode/agents/ops-runner.md` e `docs/engineering/06-PRODUCAO.md` (6 ocorrências reais, corrigida a contagem de 5→6) sem caminho desatualizado | — |  | 0.71 |
| [[03 - Casos de teste#^ct-005\|CT-005]] | ✅ Aprovado | Config resolvida: `name: nxgestao`; volumes `nxgestao_nxgestao_data`/`nxgestao_nxgestao_pgdata`/`nxgestao_nxgestao_staging_data`/`nxgestao_nxgestao_staging_pgdata`; rede `nxgestao_net`; containers `nxgest-postgres`/`nxgest-pg-dev`/`staging-app`/`staging-pg` — idênticos a `docs/STATUS.md` | — |  | 0.71 |
| [[03 - Casos de teste#^ct-006\|CT-006]] | ✅ Aprovado | `.env.example`, `.env.production.example`, `.env.staging.example` continuam na raiz | — |  | 0.71 |
| [[03 - Casos de teste#^ct-007\|CT-007]] | ✅ Aprovado | `git status -sb` idêntico ao baseline protegido (27 modificados + 10 untracked intactos); nenhum valor de segredo impresso/registrado em nenhuma rodada; nenhum deploy real executado | **Ressalva fora de escopo registrada na Decisão** |  | 0.71 |

> **Regra de esforço:** aprovado e falhou = 100% da parcela; em andamento = 25%; bloqueado = 50%; aguardando e não executado = 0%.

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

## Evidências adicionais (verificação técnica, QA independente do Orquestrador)

- `git diff --check` — exit 0 (sem conflito nem espaço em branco problemático).
- Sintaxe dos scripts — `bash -n scripts/deploy.sh` e `bash -n scripts/deploy-staging.sh` — ambos OK.
- `git diff scripts/deploy-staging.sh` — confirma que o diff deste lote altera **somente** a linha `COMPOSE="-f docker-compose.staging.yml"` → `COMPOSE="--project-directory . -f infra/docker-compose.staging.yml"`; nenhuma outra linha do script foi tocada.

---

## Histórico de validação

Nenhum reteste necessário — todos os CTs aprovados na primeira execução formal (após as correções já aplicadas e documentadas em `03 - Implementação.md` da execução DEV).

---

## Decisão

**Resultado geral:** ✅ Aprovado com ressalvas.

> **Ressalva (fora de escopo, não corrigir nesta demanda):** `scripts/deploy-staging.sh` já continha, antes deste lote, a linha `MAIL_FROM_NAME=NX Gest` sem aspas dentro do heredoc que gera `.env.staging`. Confirmado por `git diff scripts/deploy-staging.sh` que o diff deste lote altera **apenas** a linha `COMPOSE=...` — esse trecho não foi introduzido nem tocado pelo `NXG-MEL-0005` e não deve ser corrigido nesta demanda (pertence a outro escopo).

## Checklist de encerramento QA

- [x] Todos os CTs executados (CT-001 a CT-007, todos aprovados).
- [x] Evidências e observações preenchidas.
- [x] Nenhum bug filho aberto (nenhum CT reprovado).
- [x] Resultado geral definido: aprovado com ressalvas.
- [x] Status da validação e da demanda atualizados.
- [x] Próximo passo registrado: lote concluído; iniciar `NXG-MEL-0006` (já autorizado, sem pausa).
- [x] Sincronização documental verificada: frontmatter, README, board, links, evidências, histórico e pendências.
