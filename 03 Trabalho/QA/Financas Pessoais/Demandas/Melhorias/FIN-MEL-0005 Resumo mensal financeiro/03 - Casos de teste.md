---
demanda: FIN-MEL-0005
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: 1
---

# Casos de teste — FIN-MEL-0005

> [!info]- Navegação QA
> **README:** [[00 README]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano:** [[02 - Plano de teste]]  
> **Casos:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0005/00 README|Execução DEV]]

> [!settings]- Controle dos casos de teste
> Status: planejado

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1|C1]] | [[03 - Casos de teste#^ct-001|CT-001]] |
| [[01 - Demanda#^c2|C2]] | [[03 - Casos de teste#^ct-002|CT-002]] |
| [[01 - Demanda#^c3|C3]] | [[03 - Casos de teste#^ct-003|CT-003]] |
| [[01 - Demanda#^c4|C4]] | [[03 - Casos de teste#^ct-004|CT-004]] |
| [[01 - Demanda#^c5|C5]] | [[03 - Casos de teste#^ct-005|CT-005]] |
| [[01 - Demanda#^c6|C6]] | [[03 - Casos de teste#^ct-006|CT-006]] |

> [!example]- CT-001 · Total de receitas
>
> **Dado** que o mês possui receitas conhecidas  
> **Quando** o resumo é exibido  
> **Então** o total de receitas corresponde à soma das receitas.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> **Informações do CT:** cálculo · UI/unit · ambos · planejado
>
> ^ct-001

> [!example]- CT-002 · Total de despesas
>
> **Dado** que o mês possui despesas conhecidas  
> **Quando** o resumo é exibido  
> **Então** o total de despesas corresponde à soma das despesas.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Informações do CT:** cálculo · UI/unit · ambos · planejado
>
> ^ct-002

> [!example]- CT-003 · Saldo mensal
>
> **Dado** que o mês possui receitas e despesas  
> **Quando** o resumo é calculado  
> **Então** o saldo corresponde a receitas menos despesas.
>
> **Resultado esperado:** saldo positivo, negativo ou zero é exibido corretamente.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Informações do CT:** cálculo · UI/unit · ambos · planejado
>
> ^ct-003

> [!example]- CT-004 · Quantidade de lançamentos
>
> **Dado** que a lista possui registros  
> **Quando** o resumo é exibido  
> **Então** a quantidade corresponde exatamente aos itens listados.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Informações do CT:** funcional · UI/E2E · manual · planejado
>
> ^ct-004

> [!example]- CT-005 · Troca de mês e estados
>
> **Dado** que o usuário troca o mês ou consulta um mês vazio  
> **Quando** a API responde  
> **Então** indicadores, lista vazia, carregamento e erro permanecem coerentes.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> **Informações do CT:** funcional · E2E/API · manual · planejado
>
> ^ct-005

> [!example]- CT-006 · Responsividade do resumo
>
> **Dado** que o usuário acessa em celular ou desktop  
> **Quando** visualiza o resumo  
> **Então** os indicadores permanecem legíveis e acessíveis.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> **Informações do CT:** usabilidade · UI/E2E · manual · planejado
>
> ^ct-006

