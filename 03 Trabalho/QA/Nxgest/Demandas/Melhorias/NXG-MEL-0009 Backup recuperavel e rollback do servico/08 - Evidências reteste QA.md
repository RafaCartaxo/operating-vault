# Evidências QA — reteste NXG-MEL-0009

2026-11-11 · HEAD c7b65c8 + delta local. Os 26 testes automatizados foram selecionados individualmente em 26 execuções bwrap separadas, cada qual com isolamento de rede e sondas de guardas por PATH, binário absoluto e subprocessos antes de iniciar. Todos passaram. Três cenários QA adicionais e duas variantes de preservação byte a byte também passaram com a mesma verificação prévia. Logs e `resultados.json` em `.maestro/nxgest-team/qa/NXG-032-034-RETESTE/`.

O desvio anterior do DEV — CLI Docker real iniciado contra socket inexistente sem daemon contatado — permanece no histórico e não é retroativamente conforme. A rodada atual não invocou CLI real. Nenhum restore PostgreSQL, transporte, proveniência, consistência temporal ou saúde operacional real foi comprovado.

## CT-003

Falha sintética de escrita em dump, anexos, metadados, manifesto e marca; comparação byte a byte do conjunto anterior. `case-12.log`, `backup-bytes.log`, `backup-interrupcao.log`.

^ev-003

## CT-005

Ensaio dublado confronta referências e anexos; referência ausente é rejeitada. `case-01.log`, `case-11.log`, `independente-2.log`.

^ev-005

## CT-009

Evidência estruturada contraditória rejeitada; comparação sintética detecta divergências; gate real segue NO-GO por falta de fonte autenticada. `case-06.log`, `case-13.log`, `independente-3.log`.

^ev-009

## CT-012

Cópia em fixtures inclui conjunto completo e falhas SCP dubladas; preservação anterior em bytes; guia corrigido. `case-14.log`, `copia-bytes.log`.

^ev-012

## CT-011

Health/declaração são tratados, porém SHA efetivo e integridade restaurada não possuem fonte real verificável; retorno permanece NO-GO. `case-07.log`.

^ev-011

## CT-013

Rodada atual isolada aprovada por QA no escopo local, conforme decisão da Coordenação; histórico de CLI Docker real anterior permanece não conforme, sem validação retroativa.

^ev-013

## Achado adicional

NXG-035: `corrections.check.mjs`, que contém os dois testes de cópia/vínculo, não está incluído em `test:backup`, `test:deploy` ou nos workflows CI/CD. `npm test` usa o padrão Vitest instalado que seleciona `*.test`/`*.spec`, não `*.check.mjs`. Constatação estática; CI real não foi executado. Correção e reteste independentes pendentes.

Parecer atual: QA_REJECTED / NO-GO; 13 CTs aprovados no escopo local e CT-011 bloqueado. CT-013 aprovado apenas para a rodada QA atual; violação histórica permanece não conforme. Filhos 032–034 QA_APPROVED com ressalvas em fixtures após sincronização DEV; NXG-035 encaminhado ao DEV e pendente de correção e reteste.

## Atualização NXG-035 — 2026-11-11

NXG-035 recebeu QA_APPROVED com ressalvas após 7/7 CTs sintéticos; [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/06 - Evidências QA|evidências]]. GitHub Actions real e disponibilidade do runner não foram comprovados. MEL-0009 mantém QA_REJECTED/NO-GO e CT-011 bloqueado; CT-013 é aprovado somente na rodada atual, sem apagar a não conformidade histórica.
