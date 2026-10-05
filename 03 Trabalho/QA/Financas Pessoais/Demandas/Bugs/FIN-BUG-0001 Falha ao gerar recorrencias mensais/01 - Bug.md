---
prioridade: alta
status: execucao
tipo: bug
etapa_atual: "DEV · Análise técnica"
modulo: "Recorrências mensais"
plano: ""
execucao: ""
ambiente: dev
origem: validação
projeto: "Financas Pessoais"
epico: ""
pai: "FIN-MEL-0012"
data_inicio: "2026-10-05"
data_fim: ""
responsavel: ""
pontos_alocados: 3
---

# FIN-BUG-0001 — Geração mensal de recorrências bloqueia a lista de lançamentos

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Demanda pai:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0012 Recorrências mensais/01 - Demanda|FIN-MEL-0012]]
> **Casos de teste:** [[02 - Casos de teste]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Fix DEV:** será criado após o gate QA deste defeito.
> **Validação QA:** [[03 - Validação dev|Validação QA]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** `Financas Pessoais`


---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> Preencha apenas `pontos_alocados` no frontmatter com a capacidade reservada para este bug.
> 
> Exemplo: se houver 50 pontos disponíveis no ciclo, use `pontos_alocados: 50`.

```dataviewjs
const projeto = String(dv.current().projeto || "").toUpperCase();
const id = (dv.current().file.path.match(new RegExp(`${projeto || "[A-Z]{2,8}"}-\\d+`)) || [""])[0];
const paginas = dv.pages().where(p => id && p.file.path.includes(id) && typeof p.pontos === "number");
const lista = paginas.sort(p => p.file.name);
const necessario = lista.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
const alocado = Number(dv.current().pontos_alocados || 0);
const diferenca = alocado - necessario;
if (lista.length > 0) {
  dv.table(["Etapa/artefato", "Pontos"], lista.map(p => [p.file.link, p.pontos]));
} else {
  dv.paragraph("Nenhum artefato com pontos registrado ainda.");
}
dv.paragraph(`**Esforço necessário:** ${necessario} · **Capacidade alocada:** ${alocado} · **${diferenca >= 0 ? "Saldo" : "Déficit"}:** ${Math.abs(diferenca)} pontos`);
```

---

## Comportamento observado

Durante a validação da `FIN-MEL-0012`, a tela de Acompanhamento não consegue carregar os lançamentos quando existe ao menos uma recorrência ativa. A API retorna `500` com `{"erro":"não foi possível gerar as recorrências do mês"}`. A causa interna reproduzida em banco temporário foi `database is locked (5) (SQLITE_BUSY)`.

---

## Passo a passo para reproduzir

**Dado** uma recorrência ativa cadastrada para o mês consultado
**E** a aplicação está disponível em ambiente `dev`
**Quando** acesso a tela de Acompanhamento ou consulto `GET /api/lancamentos?mes=2026-10`
**Então** a geração automática das ocorrências falha e a lista de lançamentos não é carregada.

---

## Evidências

- `GET /api/health` retornou `200` e `{"status":"ok"}`.
- `GET /api/recorrencias` retornou `200` e listou as recorrências cadastradas.
- `GET /api/lancamentos?mes=2026-10` retornou `500` com `não foi possível gerar as recorrências do mês`.
- Reprodução direta do `EnsureMonth` retornou `database is locked (5) (SQLITE_BUSY)`.

---

## Resultado esperado

A lista de lançamentos deve carregar normalmente e cada recorrência ativa deve gerar no máximo uma ocorrência para a competência consultada.

---

## Critérios de aceite

- C1. A consulta mensal não retorna erro quando existem recorrências ativas. ^c1
- C2. A geração mensal permanece idempotente e não duplica ocorrências. ^c2

> Critérios são definições reutilizáveis e podem ser cobertos por vários CTs. O resultado é acompanhado na validação, não marcando esta lista.

---

## Checklist de entrega ao DEV

- [x] Sintoma, ambiente e passos de reprodução estão claros.
- [x] Resultado esperado está definido.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Contexto da execução

- Ambiente: `dev` · `hml` · `prod`
- Versão/build:
