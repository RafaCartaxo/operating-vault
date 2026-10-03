---
demanda: FIN-MEL-0009
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — FIN-MEL-0009

> [!info]- Navegação QA
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Validação:** [[04 - Validação dev]]

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
| [[01 - Demanda#^c8\|C8]] | [[03 - Casos de teste#^ct-008\|CT-008]] |

## Cenários

### CT-001 · Acompanhamento como tela principal
**Dado** que acesso a aplicação  
**Quando** a interface carrega  
**Então** o Acompanhamento é exibido como área principal, sem exigir uma página exclusiva de lançamento.

**Critérios cobertos:** [[01 - Demanda#^c1|C1]]

^ct-001

### CT-002 · Abrir novo lançamento em modal
**Dado** que estou no Acompanhamento  
**Quando** aciono o botão de adicionar  
**Então** o formulário de lançamento abre em modal/container sobre a tela atual.

**Critérios cobertos:** [[01 - Demanda#^c2|C2]]

^ct-002

### CT-003 · Modal utilizável no mobile
**Dado** que o modal está aberto no celular  
**Quando** interajo com campos, teclado, rolagem e data  
**Então** o conteúdo permanece dentro da viewport e utilizável.

**Critérios cobertos:** [[01 - Demanda#^c3|C3]]

^ct-003

### CT-004 · Preservar formulário e validações
**Dado** que abro um novo lançamento pelo modal  
**Quando** preencho descrição, valor, data e parcelas, quando aplicável  
**Então** campos, máscara e validações existentes continuam funcionando.

**Critérios cobertos:** [[01 - Demanda#^c4|C4]]

^ct-004

### CT-005 · Salvar e atualizar acompanhamento
**Dado** que preencho um lançamento válido  
**Quando** confirmo o salvamento  
**Então** o registro é salvo e o Acompanhamento é atualizado sem recarregamento manual.

**Critérios cobertos:** [[01 - Demanda#^c5|C5]]

^ct-005

### CT-006 · Respeitar filtro mensal
**Dado** que o Acompanhamento está filtrado para um mês  
**Quando** salvo lançamento com data de outro mês  
**Então** ele é salvo, mas não aparece indevidamente no mês filtrado.

**Critérios cobertos:** [[01 - Demanda#^c6|C6]]

^ct-006

### CT-007 · Impedir envio duplicado
**Dado** que um lançamento está sendo salvo  
**Quando** tento confirmar novamente antes da resposta  
**Então** o segundo envio é impedido e somente um lançamento é criado.

**Critérios cobertos:** [[01 - Demanda#^c7|C7]]

^ct-007

### CT-008 · Tratar erro e preservar desktop
**Dado** que a API retorna erro durante o salvamento  
**Quando** a operação termina  
**Então** há feedback de erro, o modal não indica sucesso falso e a experiência desktop permanece utilizável.

**Critérios cobertos:** [[01 - Demanda#^c8|C8]]

^ct-008
