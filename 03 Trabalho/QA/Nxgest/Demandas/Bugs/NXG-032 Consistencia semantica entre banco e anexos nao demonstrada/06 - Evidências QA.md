---
projeto: nxgest
demanda: NXG-032
responsavel: NX Gest · QA
data: 2026-11-11
---

# Evidências QA — NXG-032

Reteste independente. Antes de cada teste, runner bwrap isolou rede e confirmou guardas Docker/curl/ssh/scp por PATH, caminhos absolutos e subprocessos. 26/26 testes selecionados individualmente passaram; logs em `.maestro/nxgest-team/qa/NXG-032-034-RETESTE/case-*.log`, `resultados.json`. Testes QA adicionais e comparação byte a byte em `independente-*.log`, `backup-bytes.log`, `backup-interrupcao.log`, `copia-bytes.log`. Nenhuma operação real ou segredo foi utilizado. A violação histórica do CLI Docker por DEV, na rodada anterior, permanece documentada no parecer pai e não é retroativamente conforme.

## CT-B01

Restauração dublada concilia referência e conteúdo sintético — case-01.

^ev-b01

## CT-B02

Referência ausente é recusada com órfão presente — independente-2.

^ev-b02

## CT-B03

Diretório vazio e leitura de caminho ausente; anexos vazios e erro de acesso — independente-1, case-02.

^ev-b03

## CT-B04

Falhas de escrita no dump/tar/metadados/manifesto/marker; comparação byte a byte do conjunto anterior — backup-bytes.log.

^ev-b04

## CT-B05

Interrupção e falhas preservam todos os bytes do conjunto anterior — backup-interrupcao.log.

^ev-b05

## CT-B06

Isolamento de rede e guardas verificadas antes de cada teste; registro histórico preservado — resultados.json.

^ev-b06

## CT-B07

Caminhos absolutos, travessia, link e tamanho divergente recusados em fixture — case-11, independente-2.

^ev-b07

## CT-B08

Arquivo órfão relatado sem rejeição por mera existência — case-11, independente-2.

^ev-b08


## Limites

Aprovação restrita a fixtures/dublês. Sem prova de consistência temporal, restore PostgreSQL, transporte ou procedência real. Em NXG-033 o preflight e retorno seguem NO-GO pela ausência de fonte real autenticada.
