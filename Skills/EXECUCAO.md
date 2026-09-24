# Skill: Execução de demanda (NX Gest)

Conduz uma melhoria MEL-NNNN do vault até entrega verificável no repositório, preservando o ID do card e a ligação entre decisão, código e validação. Bugs NXG-NNN seguem a Skills/FIX e a pasta Fixes.

## Pré-condições

- **Melhoria MEL-NNNN:** demanda pronta para planejar, sem pendência bloqueante, e PLAN-NNN vinculado no repositório.

Sem pré-condição, o item volta ou permanece em analise; não criar pasta de execução.

## Ciclo

1. Criar 04 Trabalho DEV/Execuções/<ID>/ com os modelos de Templates/Execução/.
2. Registrar 01 - Análise.md: viabilidade, impacto, riscos e decisões técnicas da melhoria.
3. Registrar 02 - Plano de execução.md e congelá-lo na aprovação. Para melhoria, apontar ao PLAN-NNN do repo, sem duplicá-lo.
4. Implementar somente o escopo aprovado e registrar fatos, desvios e evidências em 03 - Implementação.md.
5. Revisar em 04 - Code review.md: card → plano → código → CTs.
6. Executar e marcar os CTs em `03 Trabalho QA/Demandas/<tipo>/<ID>/03 - Casos de teste.md`; a execução DEV apenas referencia os CTs e registra evidências técnicas em `03 - Implementação.md`.
7. Atualizar o README, registrar commit e mover card e pasta juntos para 05 Arquivo/<ID>/.

## Regras

- ID estável: MEL-NNNN e NXG-NNN não são renomeados.
- Sem escopo rastejante: descoberta nova vira card vinculado.
- Para mudanças de código, aplicar os gates e a matriz de documentação do repositório.
- Não registrar segredo, token, conteúdo de .env ou dados sensíveis de cliente.
