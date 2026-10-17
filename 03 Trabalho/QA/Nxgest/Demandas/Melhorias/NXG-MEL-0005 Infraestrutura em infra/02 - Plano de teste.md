---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: qa-first-delivery
pontos: 5
---

# Plano de teste — NXG-MEL-0005

> [!info]- Navegação QA
> **Demanda:** [[01 - Demanda]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]

## Objetivo

Confirmar que Dockerfile, Caddyfile e os 3 docker-compose foram agrupados em `infra/` com todos os pontos de referência (compose internos, scripts de deploy, documentação operacional) atualizados, sem alterar nomes reais de infraestrutura, sem mover `.env*.example` e sem tocar o repositório antes da execução DEV ser autorizada.

## Riscos e escopo

O risco principal é um caminho de referência ficar desatualizado (script de deploy ou documentação apontando para o local antigo), o que só se manifestaria no próximo deploy real — por isso a validação usa `docker compose config` e leitura direta dos scripts, não um deploy real. Risco secundário: renomear por engano um volume/rede/container real, o que exigiria migração de dado — mitigado por comparação explícita de nomes (CT-005).

## Estratégia de teste

- **Estrutural/documental:** inspeção de diretório, leitura de scripts e documentação (CT-001, CT-003, CT-004, CT-006).
- **Configuração:** `docker compose config` nos 3 arquivos movidos, sem subir containers (CT-002).
- **Regressão:** comparação de nomes reais de infraestrutura antes/depois (CT-005) e `git status` do repositório NX Gest (CT-007).

Não há camada de teste automatizado de aplicação (unitário/API/E2E) aplicável — este lote não altera código, apenas a localização e as referências de arquivos de infraestrutura.

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | regressão | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | regressão | manual | automatizado | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | regressão | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-007\|CT-007]] | regressão | manual | automatizado | [[04 - Validação dev#Resultado dos casos de teste\|Registrar resultado]] |

## Entrada e saída

**Entrada:** raiz atual do repositório NX Gest (Dockerfile, Caddyfile, 3 docker-compose), `scripts/deploy.sh`, `scripts/deploy-staging.sh`, `.opencode/agents/ops-runner.md`, `docs/engineering/06-PRODUCAO.md`.
**Saída:** os 5 arquivos de infraestrutura em `infra/`, com todas as referências atualizadas e validadas, sem alteração de comportamento real.
