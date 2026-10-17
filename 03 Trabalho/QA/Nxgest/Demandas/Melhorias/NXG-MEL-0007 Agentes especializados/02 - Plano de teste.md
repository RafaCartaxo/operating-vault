---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: qa-first-delivery
pontos: 2
---

# Plano de teste — NXG-MEL-0007

> [!info]- Navegação QA
> **Demanda:** [[01 - Demanda]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]

## Objetivo

Confirmar que a governança de agentes do NX Gest passou a depender de uma fonte canônica neutra (`AGENTS.md` + `agents/`), com os 4 contratos (`docs-sync.md`, `ops-runner.md`, `product-planner.md`, `qa-reviewer.md`) livres de frontmatter/schema do OpenCode, e que o plano de remoção futura de `.opencode/` cobre todas as referências estruturais ativas — tudo isso nesta etapa apenas como revisão do pacote QA, sem nenhuma mudança no repositório NX Gest.

## Riscos e escopo

O risco principal é o pacote continuar amarrado à estrutura antiga (`.opencode/agents/` como fonte canônica, schema de permissão do OpenCode) ou deixar de cobrir alguma referência ativa (`README.md`, `AGENTS.md`, `SKILL-009`, `PLAN-084`, `.dockerignore`), produzindo um gate aprovado que não reflete a decisão real do Orquestrador. A validação compara cada critério da demanda com a arquitetura-alvo registrada no handoff e em `NXG-028`.

## Estratégia de teste

- **Documental/estrutural:** leitura da demanda, de `NXG-028`, do épico e do Board QA, confirmando a arquitetura-alvo (CT-001, CT-002).
- **Conteúdo dos contratos:** inspeção da definição esperada de cada contrato neutro, sem frontmatter/schema de plataforma (CT-003).
- **Inventário de referências:** busca por `.opencode/agents` no repositório e comparação com a lista registrada na demanda (CT-004).
- **Coerência documental planejada:** confirmação de que `README.md`/`AGENTS.md`/`SKILL-009`/`PLAN-084` estão listados para atualização futura, e não alterados agora (CT-005).
- **Regressão:** `git status -sb` do NX Gest para confirmar nenhuma mudança de código/infra/ambiente (CT-006).
- **Integridade do pacote:** validador oficial + checagem de links e aninhamento dos CTs (CT-007).

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | regressão | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | regressão | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | regressão | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | regressão | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-007\|CT-007]] | regressão | manual | automatizado | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |

## Entrada e saída

**Entrada:** `AGENTS.md`, `.opencode/agents/{docs-sync,ops-runner}.md` atuais, `NXG-028`, épico e Board QA (arquitetura-alvo registrada).
**Saída:** pacote QA revisado e aprovado no gate de integridade, `NXG-028`/épico/Board QA sincronizados, execução DEV anterior marcada obsoleta — nenhuma mudança no repositório NX Gest nesta etapa.
