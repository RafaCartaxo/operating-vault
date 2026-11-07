---
projeto: nxgest
epico: NXG-EPIC-0001
demanda: NXG-MEL-0008
responsavel: "NX Gest · QA e Coordenação"
data: 2026-11-07
---

# Evidências QA — NXG-MEL-0008

Revisão final: `c7b65c8ddd85efde4db7f075ca03d95a7c6c5c38`. Base de comparação funcional: `7099a97`; src/, frontend/, tsconfig e lockfile não mudaram até a revisão final. Logs locais saneados em `.maestro/nxgest-team/qa/`, fora do repositório; os resultados essenciais são registrados aqui para continuidade.

- Exemplo único e configurações sintéticas dos três Compose; caminhos de build/Caddy verificados; envs reais não lidos.
- npm ci em árvore sem dependências/build/env/uploads; início pelo npm run dev; HTTPS e proxy API responderam 200.
- Container QA exclusivo em loopback:55439 com tmpfs, bancos/portas próprios; original nxgest-pg-dev:5433 preservado e saudável; recursos QA removidos.
- 46 arquivos/215 testes, build e check-dist aprovados em 7099a97; src/frontend/tsconfig/lock idênticos na revisão final. Auditorias finais com zero erros; 5 avisos classificados.
- Login 200, criação 201, leitura/listagem 200; documento e CEP mantidos após reinício do backend no checkout limpo.
- 45 rastreados + 20 novos preservados e restauração conferida; 8 arquivos de ícones/Qase iguais aos originais na branch WIP. Commits locais explícitos, sem push/deploy.
- Checkout em caminho independente validado; pasta definitiva nxgest organizada por DEV com metadados dos envs preservados. macOS e outro computador não foram executados.
- Demanda, CTs, evidências, governança e boards sincronizados; épico continua execucao aguardando decisão do usuário no parecer final.

## Ambiente, limites e ressalvas

- Linux local; Node 20.20.2, npm 10.8.2, Compose 5.3.1. Checkout limpo criado pelo Maestro e removido após registrar resultados. Não é comprovação de execução física em outro PC ou em todos os sistemas operacionais.
- npm ci: 537 pacotes, exit 0. Vitest: 46 arquivos e 215 testes aprovados. Build: exit 0. check-dist: 4 assets presentes.
- test:safety: 9/9 em c7b65c8. Smoke completo: 286/286 em c0b0d3a; delta final revisado e validado pelos testes de limpeza. Smoke no-recreate em 2db5826: 286/286 e sentinela preservada.
- Documentação, links, UI, estilos, módulos, sintaxe Bash e diff --check sem erros. Compose dev/staging/prod validado com env sintético, sem executar stacks reais.
- Cinco avisos de órfãos aceitos nesta consolidação: três tarefas históricas (2026-08-07/ROTA-REGRESSAO-CT, 2026-08-13/HANDOFF, 2026-08-18/CHECKLIST-PLAN083), um plano arquivado (PLAN-005) e docs/qa/devboard/CTs.md. Responsável: QA e Coordenação; encaminhamento: indexação documental futura sem apagar histórico. Não bloqueiam build ou setup.
- Ícones NXG-006 e Qase permanecem WIP em branch local de preservação, não foram aprovados ou executados nesta entrega.
- Sem push/deploy; GitHub ainda não contém estes commits locais. Execução real em staging/prod, macOS e outro PC não foi feita.
