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

Confirmar que `product-planner.md` e `qa-reviewer.md` existem com permissões escopadas corretas, não duplicam `AGENTS.md`, e que a documentação (`AGENTS.md` e links do pacote) permanece coerente — sem nenhuma mudança em código, infraestrutura ou ambiente.

## Riscos e escopo

O risco principal é um dos agentes receber permissão mais ampla do que o necessário (ex.: `qa-reviewer` com `write: allow`) ou duplicar conteúdo já coberto por `AGENTS.md`, gerando duas fontes de verdade divergentes. A validação compara cada agente novo com o padrão já estabelecido por `docs-sync.md`/`ops-runner.md`.

## Estratégia de teste

- **Documental/estrutural:** leitura dos 2 arquivos de agente e comparação com o padrão existente (CT-001, CT-002).
- **Escopo de permissão:** inspeção do frontmatter `permission` de cada agente (CT-003).
- **Ausência de duplicação:** comparação textual com `AGENTS.md` (CT-004).
- **Documentação:** leitura de `AGENTS.md` (CT-005).
- **Regressão:** `git status` do NX Gest para confirmar nenhuma mudança de código/infra/ambiente (CT-006, CT-007).

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | regressão | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | regressão | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | regressão | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-007\|CT-007]] | regressão | manual | automatizado | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |

## Entrada e saída

**Entrada:** `AGENTS.md`, `.opencode/agents/{docs-sync,ops-runner}.md` atuais (padrão de referência).
**Saída:** `.opencode/agents/{product-planner,qa-reviewer}.md` criados, `AGENTS.md` sincronizado se necessário, nenhuma mudança fora do escopo.
