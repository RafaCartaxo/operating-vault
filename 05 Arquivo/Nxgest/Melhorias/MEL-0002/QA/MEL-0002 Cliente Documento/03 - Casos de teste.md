---
demanda: "[[01 - Demanda|MEL-0002 Cliente Documento]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: aprovado
pontos: 20
---
# Casos de teste — MEL-0002

> Os critérios ficam na demanda; esta nota concentra os cenários executáveis.

> [!info]- Navegação QA/DEV
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Melhorias/MEL-0002/DEV/MEL-0002/00 README|MEL-0002 — execução]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

## Matriz de cobertura dos critérios

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-005\|CT-005]], [[03 - Casos de teste#^ct-006\|CT-006]] |
| [[01 - Demanda#^c8\|C8]] | [[03 - Casos de teste#^ct-007\|CT-007]] |
| [[01 - Demanda#^c9\|C9]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c10\|C10]] | [[03 - Casos de teste#^ct-008\|CT-008]] |

## CTs executáveis

> [!example]- CT-001 Salvar cliente com CPF válido
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que um cliente com CPF válido pode ser salvo normalmente,
> com ou sem Documento.
>
> **Pré-condições:**
> - Usuário está na tela de cadastro de cliente.
> - O CPF informado é válido e ainda não está cadastrado.
>
> **Dado** um cliente com CPF válido
> **Quando** salvo o cadastro
> **Então** o cliente é salvo normalmente.
>
> **Resultado esperado:** o cliente é salvo sem erro.
>
> **Pós-condição:** o cliente permanece persistido e disponível para consulta.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]], [[01 - Demanda#^c9|C9]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** UI/API  
> **Automação:** automatizado + manual  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 Salvar cliente somente com Documento
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o cadastro pode ser salvo quando apenas o Documento é informado.
>
> **Pré-condições:**
> - Usuário está na tela de cadastro de cliente.
> - CPF está vazio e Documento está preenchido.
>
> ## Cenário
>
> **Dado** um cliente com CPF vazio e Documento preenchido
> **Quando** salvo o cadastro
> **Então** o cliente é salvo normalmente.
>
> **Resultado esperado:** o cliente é salvo usando o Documento como identificador informado.
>
> **Pós-condição:** o cliente permanece persistido e disponível para consulta.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 Salvar cliente sem CPF e sem Documento
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o cadastro continua permitido sem CPF e sem Documento.
>
> **Pré-condições:**
> - Usuário está na tela de cadastro de cliente.
> - CPF e Documento estão vazios.
>
> ## Cenário
>
> **Dado** um cliente com CPF e Documento vazios
> **Quando** salvo o cadastro
> **Então** o cliente é salvo normalmente.
>
> **Resultado esperado:** o cliente é salvo sem identificadores informados.
>
> **Pós-condição:** o cliente permanece persistido e disponível para consulta.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** automatizado + manual  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 Bloquear CPF inválido mesmo com Documento
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que informar um Documento não contorna a validação do CPF.
>
> **Pré-condições:**
> - Usuário está na tela de cadastro de cliente.
> - CPF informado é inválido e Documento está preenchido.
>
> ## Cenário
>
> **Dado** um cliente com CPF inválido e Documento preenchido
> **Quando** tento salvar
> **Então** o CPF mostra erro e o cadastro não é salvo.
>
> **Resultado esperado:** o cadastro é bloqueado pela validação do CPF.
>
> **Pós-condição:** nenhum cliente é criado ou alterado.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** negativo  
> **Camada:** UI  
> **Automação:** automatizado + manual  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 Persistir e editar Documento
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o Documento é persistido e pode ser atualizado posteriormente.
>
> **Pré-condições:**
> - Existe um cliente salvo com Documento.
> - Usuário consegue abrir a edição do cliente.
>
> ## Cenário
>
> **Dado** um cliente salvo com Documento
> **Quando** altero o Documento e salvo novamente
> **Então** o valor atualizado é retornado e aparece na edição.
>
> **Resultado esperado:** o novo Documento é persistido e exibido corretamente.
>
> **Pós-condição:** o cliente permanece salvo com o Documento atualizado.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c6|C6]], [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** persistência/edição  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-005

> [!example]- CT-006 Remover Documento
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o Documento pode ser removido sem excluir o cliente.
>
> **Pré-condições:**
> - Existe um cliente salvo com Documento preenchido.
> - Usuário está na tela de edição do cliente.
>
> ## Cenário
>
> **Dado** um cliente com Documento preenchido
> **Quando** limpo o campo e salvo
> **Então** o Documento é removido e persiste como `null`.
>
> **Resultado esperado:** o cliente é salvo sem Documento.
>
> **Pós-condição:** o cliente continua disponível sem Documento.
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** edição  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-006

> [!example]- CT-007 Rejeitar Documento acima do limite
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o limite de 20 caracteres do Documento é respeitado.
>
> **Pré-condições:**
> - Usuário está na tela de cadastro ou edição de cliente.
> - Documento contém mais de 20 caracteres.
>
> ## Cenário
>
> **Dado** um Documento com mais de 20 caracteres
> **Quando** tento salvar
> **Então** o campo mostra uma mensagem e o cadastro não é salvo.
>
> **Resultado esperado:** o valor acima do limite é rejeitado.
>
> **Pós-condição:** nenhum valor inválido é persistido.
>
> **Critérios cobertos:** [[01 - Demanda#^c8|C8]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** limite  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-007

> [!example]- CT-008 Manter compatibilidade de cliente existente
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que clientes antigos continuam funcionando sem Documento.
>
> **Pré-condições:**
> - Existe um cliente criado antes da inclusão do campo Documento.
> - Esse cliente não possui Documento.
>
> ## Cenário
>
> **Dado** um cliente existente sem Documento
> **Quando** abro e salvo sua edição sem preencher Documento
> **Então** o cliente continua funcionando normalmente.
>
> **Resultado esperado:** o cliente é carregado e salvo sem erro.
>
> **Pós-condição:** os dados existentes permanecem íntegros e o Documento continua vazio.
>
> **Critérios cobertos:** [[01 - Demanda#^c10|C10]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-008
