---
demanda: FIN-MEL-0004
status: planejado
responsavel: ""
pontos: 1
---

# Plano de teste — FIN-MEL-0004

> [!info]- Navegação QA
> **README:** [[00 README]]  
> **Demanda:** [[01 - Demanda]]  
> **Casos:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]

## Objetivo

Validar o comportamento dos campos responsivos em iPhone, Android e desktop.

## Estratégia

- Execução manual em dispositivo iPhone com Chrome.
- Execução manual em dispositivo Android com Chrome.
- Teste de viewport desktop.
- Teste funcional de máscara e cursor.
- Regressão do cadastro e consulta mensal.

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-006\|CT-006]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-007\|CT-007]] |

## Entrada e saída

**Entrada:** aplicação acessível pela URL local e dispositivos na mesma rede.  
**Saída:** campos utilizáveis, alinhados e sem overflow.
