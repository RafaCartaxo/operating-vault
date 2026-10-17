---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: qa-first-delivery
pontos: 0
---

# Plano de teste — MEL-0004

> [!info]- Navegação QA
> **Demanda:** [[01 - Demanda]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]

## Objetivo

Confirmar que o mapa estrutural do README representa o estado real do NX Gest, mantém links válidos e não amplia o lote para código ou infraestrutura.

## Riscos e escopo

O risco principal é documentar uma estrutura futura como se já existisse. O teste compara o README com a raiz real e com o escopo aprovado no NXG-028.

## Estratégia de teste

- Auditoria documental e de links.
- Revisão do diff para confirmar escopo.
- Verificação de nomenclatura canônica.

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | regressão | manual | automatizado | [[04 - Validação dev#Resultado dos casos de teste|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | regressão | manual | manual | [[04 - Validação dev#Resultado dos casos de teste|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | funcional | manual | manual | [[04 - Validação dev#Resultado dos casos de teste|Registrar resultado]] |

## Entrada e saída

**Entrada:** README raiz e árvore real do repositório.
**Saída:** README atualizado, auditado e coerente com MEL-0004.
