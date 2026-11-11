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

Rodada atual isolada passou; histórico de CLI Docker real anterior permanece não conforme, aguardando decisão de Coordenação/usuário.

^ev-013

## Achado adicional

NXG-035: `corrections.check.mjs`, que contém os dois testes de cópia/vínculo, não está incluído em `test:backup`, `test:deploy` ou nos workflows CI/CD. `npm test` usa o padrão Vitest instalado que seleciona `*.test`/`*.spec`, não `*.check.mjs`. Constatação estática; CI real não foi executado. Correção e reteste independentes pendentes.

Parecer pai: QA_REJECTED / no-go, 12 aprovados localmente e 2 bloqueados (CT-011 e CT-013); CTs dos filhos 032–034 passaram localmente; gates finais aguardam sincronização DEV, 035 em triagem.
