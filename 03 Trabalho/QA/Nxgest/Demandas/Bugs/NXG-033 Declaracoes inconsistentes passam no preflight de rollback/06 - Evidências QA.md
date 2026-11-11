---
projeto: nxgest
demanda: NXG-033
responsavel: NX Gest · QA
data: 2026-11-11
---

# Evidências QA — NXG-033

Reteste independente. Antes de cada teste, runner bwrap isolou rede e confirmou guardas Docker/curl/ssh/scp por PATH, caminhos absolutos e subprocessos. 26/26 testes selecionados individualmente passaram; logs em `.maestro/nxgest-team/qa/NXG-032-034-RETESTE/case-*.log`, `resultados.json`. Testes QA adicionais e comparação byte a byte em `independente-*.log`, `backup-bytes.log`, `backup-interrupcao.log`, `copia-bytes.log`. Nenhuma operação real ou segredo foi utilizado. A violação histórica do CLI Docker por DEV, na rodada anterior, permanece documentada no parecer pai e não é retroativamente conforme.

## CT-B01

Schema desconhecido/incompatível e ausência são recusados ou mantidos em NO-GO — case-06 e revisão preflight.

^ev-b01

## CT-B02

Schema estruturado contraditório com hash recalculado é recusado — case-06.

^ev-b02

## CT-B03

Comparação sintética detecta SHA/imagem divergentes e não libera produção — case-13; preflight real permanece NO-GO.

^ev-b03

## CT-B04

Montagem/runtime divergente e prova de configuração ausente bloqueiam; sem validação real — case-06 e revisão.

^ev-b04

## CT-B05

Health negativo/timeout e integridade não declarada falham; mesmo health positivo permanece NO-GO sem SHA efetivo/integridade verificáveis — case-07.

^ev-b05

## CT-B06

Revisão humana não substituída por fixture; guardas de subprocessos e isolamento verificados — resultados.json e runbooks.

^ev-b06

## CT-B07

Fonte real ausente leva a NO-GO, comparação sintética não é autoridade operacional — case-06 e case-13.

^ev-b07

## CT-B08

Bundle divergente é recusado por comparador sintético; retorno operacional mantém NO-GO — independente-3 e case-07.

^ev-b08


## Limites

Aprovação restrita a fixtures/dublês. Sem prova de consistência temporal, restore PostgreSQL, transporte ou procedência real. Em NXG-033 o preflight e retorno seguem NO-GO pela ausência de fonte real autenticada.

## Gate final — 2026-11-11

QA_APPROVED com ressalvas após conferência da sincronização DEV. A decisão usa os resultados anteriores: nenhum teste foi repetido nesta etapa. Os limites acima e o desvio histórico de isolamento permanecem.
