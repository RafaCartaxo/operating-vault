# Evidências de reteste independente — NXG-035

2026-11-11 · HEAD c7b65c8 + alterações locais. Dois níveis bwrap isolaram rede e processo; o exterior montou guardas em PATH e /usr/bin, sem home, checkout, sockets ou rede do host. Antes de cada cenário, sondas por PATH e caminho absoluto foram executadas como subprocessos e retornaram 97 para docker, curl, ssh e scp. Testes e scripts operaram somente em cópias sintéticas. Logs e harness: `.maestro/nxgest-team/qa/NXG-035-RETESTE/runner.log`, `casos.log`, `fixture/harness.py`. Nenhuma operação real; GitHub Actions não executado.

## CT-B01

CI representado localmente: comando test:corrections presente no job test; runner executou dois testes distintos, 2 passaram e zero ignorados; dependência `needs: [test, smoke]` inspecionada. `casos.log`: CI ok; `runner.log` contém TAP.

^ev-b01

## CT-B02

CD manual representado localmente: workflow_dispatch declara Node 20 e test:corrections; runner executou ambos os testes e promoção sentinela somente após sucesso. `deploy-prod` depende de `validate`; inspeção estática, não execução GitHub Actions. `casos.log`: CD-manual ok.

^ev-b02

## CT-B03

Cada teste recebeu falha isolada em cópia para CI e CD manual (quatro variantes); saída não zero e promoção sentinela não executada. `casos.log`: falha-vinculo/falha-copia.

^ev-b03

## CT-B04

Cada guarda foi removida e alterada para retorno inválido em cada gate (16 variantes); todas interromperam antes de TAP e da promoção. Proteção exterior independente preservada durante essas variantes; sondas PATH, absoluto e subprocessos precederam cada caso. `casos.log`: ausente/invalida.

^ev-b04

## CT-B05

Runner sem caminhos pessoais inspecionado. Simulações Node 18, bwrap ausente e namespace recusado falharam antes dos testes em ambos os gates; runner positivo usou Node 20 e sandbox sem home pessoal. Requisitos Linux, Node >=20, bwrap, namespaces e destinos /usr/bin são explícitos. Disponibilidade no GitHub Actions não comprovada. `casos.log`: node18, sem-bwrap, namespace.

^ev-b05

## CT-B06

Presença de safety/deploy/backup nos dois workflows e NO-GO no preflight conferidos estaticamente; seis simulações com sentinelas de cada gate anterior propagaram falha. Nenhum workflow real executado. `casos.log`: test:safety/test:deploy/test:backup.

^ev-b06

## CT-B07

Marcador secreto sintético introduzido apenas no ambiente do harness não apareceu nas saídas capturadas dos 28 cenários; cada log indica sondas antes da execução. Documentação e parecer não alegam compatibilidade Actions, restore ou proveniência reais. O marcador não representa credencial.

^ev-b07

## Limites e decisão

QA_APPROVED com ressalvas para 7/7 CTs no escopo local sintético. A representação dos workflows e sentinelas não substitui GitHub Actions nem comprova disponibilidade de bwrap/namespaces no runner hospedado. MEL-0009 permanece QA_REJECTED/NO-GO, CT-011 bloqueado e CT-013 aprovado somente para a rodada atual; o desvio histórico Docker CLI continua não conforme sem validação retroativa.
