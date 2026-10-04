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
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-004\|CT-004]], [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-006\|CT-006]], [[03 - Casos de teste#^ct-007\|CT-007]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-008\|CT-008]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-009\|CT-009]], [[03 - Casos de teste#^ct-010\|CT-010]] |

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
> **Quando** o sistema recalcula dois meses  
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

> [!example]- CT-003 · Recalcular sem duplicar a competência
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que repetir o recálculo não duplica a ocorrência mensal.
>
> **Pré-condições:** existe uma regra recorrente ativa e uma competência já calculada.
>
> **Dado** uma regra ativa já processada em uma competência  
> **Quando** repito o recálculo da mesma competência  
> **Então** a ocorrência existente é reutilizada e não há duplicidade.
>
> **Resultado esperado:** permanece no máximo uma ocorrência por regra e mês, com origem e valor preservados.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Tipo:** funcional  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado.

^ct-003

> [!example]- CT-004 · Respeitar data final
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
> **Pré-condições:** existe uma regra com término configurado.
>
> **Dado** uma regra com data final  
> **Quando** consulto o mês final e o mês seguinte  
> **Então** há ocorrência no mês final e nenhuma depois dele.
>
> **Resultado esperado:** a regra deixa de gerar ocorrências após o mês final.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Tipo:** regressão  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado.

^ct-004

> [!example]- CT-005 · Permanecer ativa sem data final
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que a ausência de data final mantém a regra ativa.
>
> **Pré-condições:** existe uma regra recorrente sem data final.
>
> **Dado** uma regra sem data final  
> **Quando** consulto competências futuras  
> **Então** a regra continua ativa e gera as ocorrências mensais correspondentes.
>
> **Resultado esperado:** a regra permanece ativa até ser encerrada.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Tipo:** financeiro  
> **Camada:** integração  
> **Automação:** manual  
> **Execução:** planejado.

^ct-005

> [!example]- CT-006 · Editar sem apagar histórico
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que a edição da regra não altera ocorrências já geradas.
>
> **Pré-condições:** regra criada com pelo menos uma ocorrência.
>
> **Dado** uma regra com ocorrência existente  
> **Quando** altero seus dados  
> **Então** a regra é atualizada sem apagar o histórico.
>
> **Resultado esperado:** ocorrências anteriores permanecem preservadas.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Tipo:** validação  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado.

^ct-006

> [!example]- CT-007 · Encerrar sem apagar histórico
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o encerramento impede novas ocorrências sem apagar o histórico.
>
> **Pré-condições:** regra criada com pelo menos uma ocorrência.
>
> **Dado** uma regra com histórico existente  
> **Quando** encerro a regra  
> **Então** o histórico permanece e novas ocorrências deixam de ser geradas.
>
> **Resultado esperado:** encerramento efetivo sem exclusão de ocorrências anteriores.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Tipo:** regressão  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado.

^ct-007

> [!example]- CT-008 · Não duplicar recorrente já incluído em fatura
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

^ct-008

> [!example]- CT-009 · Rejeitar regra inválida sem ocorrência parcial
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
> **Dado** um campo obrigatório ausente  
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

^ct-009

> [!example]- CT-010 · Rejeitar valor ou data inválidos
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma a rejeição de valores e datas fora das regras de negócio.
>
> **Pré-condições:** usuário na tela de cadastro de recorrência.
>
> **Dado** valor menor ou igual a zero, data inválida ou término anterior ao início  
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

^ct-010
