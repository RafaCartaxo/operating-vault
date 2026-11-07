---
projeto: nxgest
epico: NXG-EPIC-0001
demanda: NXG-029
responsavel: "NX Gest · QA e Coordenação"
data: 2026-11-07
---

# Evidências QA — NXG-029

Revisão final: `c7b65c8ddd85efde4db7f075ca03d95a7c6c5c38`. Base de comparação funcional: `7099a97`; src/, frontend/, tsconfig e lockfile não mudaram até a revisão final. Logs locais saneados em `.maestro/nxgest-team/qa/`, fora do repositório; os resultados essenciais são registrados aqui para continuidade.

- Carregador Bash aceitou legado MAIL_FROM_NAME com espaço, sem Node no host e sem executar texto de shell. QA confirmou arquivo inalterado em fixture própria.
- test:safety cobre geração nova, reutilização byte a byte, chave desconhecida e valores literais; permissões e política console preservadas em ambiente sintético.

## Ambiente, limites e ressalvas

- Linux local; Node 20.20.2, npm 10.8.2, Compose 5.3.1. Checkout limpo criado pelo Maestro e removido após registrar resultados. Não é comprovação de execução física em outro PC ou em todos os sistemas operacionais.
- npm ci: 537 pacotes, exit 0. Vitest: 46 arquivos e 215 testes aprovados. Build: exit 0. check-dist: 4 assets presentes.
- test:safety: 9/9 em c7b65c8. Smoke completo: 286/286 em c0b0d3a; delta final revisado e validado pelos testes de limpeza. Smoke no-recreate em 2db5826: 286/286 e sentinela preservada.
- Documentação, links, UI, estilos, módulos, sintaxe Bash e diff --check sem erros. Compose dev/staging/prod validado com env sintético, sem executar stacks reais.
- Cinco avisos de órfãos aceitos nesta consolidação: três tarefas históricas (2026-08-07/ROTA-REGRESSAO-CT, 2026-08-13/HANDOFF, 2026-08-18/CHECKLIST-PLAN083), um plano arquivado (PLAN-005) e docs/qa/devboard/CTs.md. Responsável: QA e Coordenação; encaminhamento: indexação documental futura sem apagar histórico. Não bloqueiam build ou setup.
- Ícones NXG-006 e Qase permanecem WIP em branch local de preservação, não foram aprovados ou executados nesta entrega.
- Sem push/deploy; GitHub ainda não contém estes commits locais. Execução real em staging/prod, macOS e outro PC não foi feita.
