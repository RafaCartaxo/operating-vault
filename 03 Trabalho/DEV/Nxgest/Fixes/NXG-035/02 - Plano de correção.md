# 02 - Plano de correção (NXG-035)

## Resultado esperado

CI e CD manual executam os dois testes sintéticos e propagam falha; CD manual configura Node 20.

## Mudança planejada

Runner sem caminhos pessoais, guardas e isolamento verificados, requisitos explícitos e falha fechada. Preservar gates anteriores e no-go operacional.

## Fora de escopo

GitHub Actions real, Docker CLI/daemon, rede, recursos reais, SSH, push, commit e deploy.

## Pronto quando

Testes sintéticos e revisão local evidenciados; QA valida independentemente.
