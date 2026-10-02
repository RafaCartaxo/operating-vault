---
demanda: FIN-MEL-0005
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: concluido
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
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]], [[03 - Casos de teste#^ct-008\|CT-008]], [[03 - Casos de teste#^ct-015\|CT-015]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-002\|CT-002]], [[03 - Casos de teste#^ct-007\|CT-007]], [[03 - Casos de teste#^ct-015\|CT-015]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-003\|CT-003]], [[03 - Casos de teste#^ct-007\|CT-007]], [[03 - Casos de teste#^ct-008\|CT-008]], [[03 - Casos de teste#^ct-009\|CT-009]], [[03 - Casos de teste#^ct-015\|CT-015]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-004\|CT-004]], [[03 - Casos de teste#^ct-010\|CT-010]], [[03 - Casos de teste#^ct-011\|CT-011]], [[03 - Casos de teste#^ct-012\|CT-012]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-005\|CT-005]], [[03 - Casos de teste#^ct-010\|CT-010]], [[03 - Casos de teste#^ct-011\|CT-011]], [[03 - Casos de teste#^ct-012\|CT-012]], [[03 - Casos de teste#^ct-013\|CT-013]], [[03 - Casos de teste#^ct-014\|CT-014]], [[03 - Casos de teste#^ct-016\|CT-016]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-006\|CT-006]], [[03 - Casos de teste#^ct-014\|CT-014]], [[03 - Casos de teste#^ct-016\|CT-016]] |

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
> **Dado** que existem lançamentos em dois meses diferentes  
> **Quando** o usuário troca o mês selecionado  
> **Então** o resumo corresponde somente ao novo período.
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

> [!example]- CT-007 · Mês somente com despesas
>
> **Dado** que o mês possui despesas e nenhuma receita  
> **Quando** o resumo é exibido  
> **Então** receitas são R$ 0,00, despesas são somadas e o saldo fica negativo.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]], [[01 - Demanda#^c3|C3]]

^ct-007

> [!example]- CT-008 · Mês somente com receitas
>
> **Dado** que o mês possui receitas e nenhuma despesa  
> **Quando** o resumo é exibido  
> **Então** despesas são R$ 0,00, receitas são somadas e o saldo fica positivo.

> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c3|C3]]

^ct-008

> [!example]- CT-009 · Mês com saldo zero
>
> **Dado** que receitas e despesas possuem o mesmo total  
> **Quando** o resumo é calculado  
> **Então** o saldo exibido é R$ 0,00.

> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]

^ct-009

> [!example]- CT-010 · Trocar mês com composição diferente
>
> **Dado** que dois meses possuem quantidades e composições diferentes  
> **Quando** o usuário troca o mês  
> **Então** quantidade, receitas, despesas e saldo correspondem somente ao novo período.

> **Critérios cobertos:** [[01 - Demanda#^c4|C4]], [[01 - Demanda#^c5|C5]]

^ct-010

> [!example]- CT-011 · Atualizar resumo após editar
>
> **Dado** que existe um lançamento listado  
> **Quando** ele é editado  
> **Então** os indicadores são recalculados com o novo valor.

> **Critérios cobertos:** [[01 - Demanda#^c4|C4]], [[01 - Demanda#^c5|C5]]

^ct-011

> [!example]- CT-012 · Atualizar resumo após excluir
>
> **Dado** que existe um lançamento listado  
> **Quando** ele é excluído  
> **Então** os indicadores são recalculados sem manter o valor anterior.

> **Critérios cobertos:** [[01 - Demanda#^c4|C4]], [[01 - Demanda#^c5|C5]]

^ct-012

> [!example]- CT-013 · Mês vazio sem resumo antigo
>
> **Dado** que o mês selecionado não possui lançamentos  
> **Quando** a consulta termina  
> **Então** a lista fica vazia e nenhum indicador do mês anterior permanece visível.

> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]

^ct-013

> [!example]- CT-014 · Erro da API
>
> **Dado** que a API falha durante a consulta mensal  
> **Quando** o resumo é carregado  
> **Então** o erro é informado e o resumo não exibe dados inconsistentes.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> **Informações do CT:** negativo · UI/API · manual · planejado
>
^ct-014

> [!example]- CT-015 · Formatação monetária do resumo
>
> **Dado** que o mês possui valores inteiros, centavos e valores acima de mil reais  
> **Quando** o resumo é exibido  
> **Então** todos os indicadores monetários usam o padrão brasileiro, incluindo `R$ 0,00` e saldo negativo.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c2|C2]], [[01 - Demanda#^c3|C3]]
>
> **Informações do CT:** validação · UI/unit · manual + automatizado · planejado
>
^ct-015

> [!example]- CT-016 · Estado de carregamento
>
> **Dado** que a consulta mensal ainda está em andamento  
> **Quando** a tela aguarda a resposta da API  
> **Então** o estado de carregamento é exibido sem apresentar dados antigos como se fossem do mês atual.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]], [[01 - Demanda#^c6|C6]]
>
> **Informações do CT:** funcional · UI/E2E · manual · planejado
>
^ct-016
