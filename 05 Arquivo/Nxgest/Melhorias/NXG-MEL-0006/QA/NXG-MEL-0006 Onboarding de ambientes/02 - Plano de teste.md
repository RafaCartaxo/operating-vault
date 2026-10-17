---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: qa-first-delivery
pontos: 2
---

# Plano de teste — NXG-MEL-0006

> [!info]- Navegação QA
> **Demanda:** [[01 - Demanda]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]

## Objetivo

Confirmar que o onboarding de desenvolvimento continua simples (um comando) após o compose mover para `infra/`, que `README.md` e `08-SETUP-NOVA-MAQUINA.md` refletem o novo comando, que `cp .env.example .env` permanece inalterado, e que nada de staging/produção foi tocado.

## Riscos e escopo

O risco principal é o onboarding ficar mais complexo (exigir que o desenvolvedor conheça o caminho `infra/`) em vez de mais simples — por isso o CT-005 valida um clone limpo de ponta a ponta. Risco secundário: alterar sem querer algo de staging/produção ao mexer em `package.json` — mitigado pelo CT-006.

## Estratégia de teste

- **Documental:** leitura de `README.md` e `08-SETUP-NOVA-MAQUINA.md` (CT-002, CT-003).
- **Configuração:** inspeção de `package.json` (CT-001) e `.env.example` (CT-004).
- **Clone limpo (regressão de onboarding):** simulação de clone novo seguindo o passo a passo atualizado (CT-005).
- **Regressão:** `scripts/deploy.sh`/`deploy-staging.sh`/`ops-runner.md` inalterados (CT-006) e `git status` do NX Gest (CT-007).

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | regressão | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | regressão | manual | automatizado | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-007\|CT-007]] | regressão | manual | automatizado | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |

## Entrada e saída

**Entrada:** `package.json`, `README.md`, `docs/engineering/08-SETUP-NOVA-MAQUINA.md` atuais do NX Gest.
**Saída:** script(s) npm de banco de dev funcionando a partir de `infra/docker-compose.yml`, documentação atualizada, clone limpo validado.
