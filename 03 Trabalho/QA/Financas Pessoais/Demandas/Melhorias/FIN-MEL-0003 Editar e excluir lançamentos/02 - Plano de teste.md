---
demanda: FIN-MEL-0003
status: planejado
responsavel: ""
pontos: 1
---

# Plano de teste — FIN-MEL-0003

> [!info]- Navegação QA
> **README:** [[00 README]]  
> **Demanda:** [[01 - Demanda]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]

## Objetivo

Validar edição e exclusão com segurança, preservando validações, persistência e consulta mensal.

## Estratégia

- Testes funcionais de edição e exclusão.
- Testes de validação do formulário reutilizado.
- Testes de integração HTTP.
- Teste de erro sem perda da tela.
- Teste responsivo.
- Regressão do cadastro e consulta mensal.

## Riscos

- Atualizar o lançamento errado.
- Excluir sem confirmação.
- Total mensal ficar desatualizado.
- Falha da API limpar dados da tela.
- Divergência entre frontend e contrato Go.

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1|C1]] | [[03 - Casos de teste#^ct-001|CT-001]] |
| [[01 - Demanda#^c2|C2]] | [[03 - Casos de teste#^ct-002|CT-002]] |
| [[01 - Demanda#^c3|C3]] | [[03 - Casos de teste#^ct-003|CT-003]] |
| [[01 - Demanda#^c4|C4]] | [[03 - Casos de teste#^ct-004|CT-004]] |
| [[01 - Demanda#^c5|C5]] | [[03 - Casos de teste#^ct-005|CT-005]] |
| [[01 - Demanda#^c6|C6]] | [[03 - Casos de teste#^ct-006|CT-006]] |
| [[01 - Demanda#^c7|C7]] | [[03 - Casos de teste#^ct-007|CT-007]] |

## Entrada e saída

**Entrada:** lançamentos persistidos e consulta mensal disponível.  
**Saída:** edição e exclusão concluídas, canceladas ou comunicadas com erro; lista e total consistentes.

