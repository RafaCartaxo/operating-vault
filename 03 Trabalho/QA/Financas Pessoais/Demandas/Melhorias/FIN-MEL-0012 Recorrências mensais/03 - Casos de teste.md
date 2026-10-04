---
demanda: FIN-MEL-0012
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: concluido
pontos: ""
---

# Casos de teste — FIN-MEL-0012

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** será criada após aprovação QA.

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam na demanda; esta nota concentra os cenários executáveis.

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-006\|CT-006]] |

> [!example]- CT-001 · Cadastrar recorrência mensal
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma o cadastro de uma regra recorrente mensal com os dados obrigatórios.
>
> **Pré-condições:** aplicação disponível e usuário na tela de recorrências.
>
> **Dado** descrição, valor, cartão/conta e data inicial válidos  
> **Quando** salvo a regra  
> **Então** a regra mensal fica ativa e identificável.
>
> **Resultado esperado:** regra criada sem duplicidade.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> **Tipo:** funcional  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado.

^ct-001

> [!example]- CT-002 · Gerar uma ocorrência por mês
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o recálculo idempotente gera uma única ocorrência por competência.
>
> **Pré-condições:** existe uma regra recorrente ativa.
>
> **Dado** uma regra ativa  
> **Quando** o sistema recalcula dois meses e repete o recálculo de um deles  
> **Então** gera uma ocorrência por mês sem duplicar a competência.
>
> **Resultado esperado:** origem e valor preservados, com no máximo uma ocorrência por mês.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Tipo:** integração  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado.

^ct-002

> [!example]- CT-003 · Respeitar data final
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma o limite de geração definido pela data final.
>
> **Pré-condições:** existem uma regra com término e uma regra sem término.
>
> **Dado** uma regra com data final  
> **Quando** consulto o mês final e o mês seguinte  
> **Então** há ocorrência no mês final e nenhuma depois dele.
>
> **Resultado esperado:** regra sem término permanece ativa e continua gerando ocorrências.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Tipo:** funcional  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado.

^ct-003

> [!example]- CT-004 · Editar e encerrar sem apagar histórico
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que a manutenção da regra não altera o histórico já gerado.
>
> **Pré-condições:** regra criada com pelo menos uma ocorrência.
>
> **Dado** uma regra com ocorrência  
> **Quando** altero seus dados ou a encerro  
> **Então** o histórico permanece e novas ocorrências respeitam o estado atualizado.
>
> **Resultado esperado:** nenhuma ocorrência anterior é apagada.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Tipo:** regressão  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado.

^ct-004

> [!example]- CT-005 · Não duplicar recorrente já incluído em fatura
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma a separação entre exibição de controle e cálculo financeiro.
>
> **Pré-condições:** recorrência vinculada a cartão e fatura contendo a mesma cobrança.
>
> **Dado** a recorrência e a fatura do mesmo mês  
> **Quando** consulto o mês  
> **Então** a recorrência aparece para controle sem ser somada novamente ao saldo.
>
> **Resultado esperado:** fatura descontada uma única vez.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> **Tipo:** financeiro  
> **Camada:** integração  
> **Automação:** manual  
> **Execução:** planejado.

^ct-005

> [!example]- CT-006 · Rejeitar regra inválida sem ocorrência parcial
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma as validações de entrada e a atomicidade do cadastro.
>
> **Pré-condições:** usuário na tela de cadastro de recorrência.
>
> **Dado** valor, data, cartão/conta ou término inválidos  
> **Quando** tento salvar  
> **Então** o sistema exibe erro e não cria regra nem ocorrência.
>
> **Resultado esperado:** nenhum dado parcial é persistido.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> **Tipo:** validação  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado.

^ct-006
