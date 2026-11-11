---
projeto: nxgest
demanda: NXG-034
responsavel: NX Gest · QA
data: 2026-11-11
---

# Evidências QA — NXG-034

Reteste independente. Antes de cada teste, runner bwrap isolou rede e confirmou guardas Docker/curl/ssh/scp por PATH, caminhos absolutos e subprocessos. 26/26 testes selecionados individualmente passaram; logs em `.maestro/nxgest-team/qa/NXG-032-034-RETESTE/case-*.log`, `resultados.json`. Testes QA adicionais e comparação byte a byte em `independente-*.log`, `backup-bytes.log`, `backup-interrupcao.log`, `copia-bytes.log`. Nenhuma operação real ou segredo foi utilizado. A violação histórica do CLI Docker por DEV, na rodada anterior, permanece documentada no parecer pai e não é retroativamente conforme.

## CT-B01

SSH/SCP dublados: erro de transferência falha sem sucesso — case-14.

^ev-b01

## CT-B02

Origem ausente falha sem publicar conjunto — case-14.

^ev-b02

## CT-B03

Conjunto completo sintético copiado e verificado, sem comprovação de transporte real — case-14.

^ev-b03

## CT-B04

Conteúdo corrompido ou faltante é recusado; conjunto anterior preservado byte a byte — case-14 e copia-bytes.log.

^ev-b04

## CT-B05

Colisão e falha de escrita recusadas; conjunto anterior preservado byte a byte — case-14 e copia-bytes.log.

^ev-b05

## CT-B06

Guias 08/09 distinguem formato atual e teste dublado; guardas verificadas — case-14 e revisão documental.

^ev-b06

## CT-B07

Destino e chave sintética com espaços completam cópia dublada — case-14.

^ev-b07

## CT-B08

Transferência parcial, destino ausente e ID inválido falham; cópia anterior intacta — case-14 e copia-bytes.log.

^ev-b08


## Limites

Aprovação restrita a fixtures/dublês. Sem prova de consistência temporal, restore PostgreSQL, transporte ou procedência real. Em NXG-033 o preflight e retorno seguem NO-GO pela ausência de fonte real autenticada.

## Gate final — 2026-11-11

QA_APPROVED com ressalvas após conferência da sincronização DEV. A decisão usa os resultados anteriores: nenhum teste foi repetido nesta etapa. Os limites acima e o desvio histórico de isolamento permanecem.
