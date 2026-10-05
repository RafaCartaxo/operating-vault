---
demanda: "[[01 - Bug]]"
status: planejado
pontos: ""
---
# Casos de teste — <ID>

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Fix DEV:** [[03 Trabalho/DEV/<projeto>/Fixes/<ID>/00 README|Fix DEV]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Validação QA:** [[03 Trabalho/QA/<projeto>/Demandas/Bugs/<ID>/03 - Validação dev|Validação QA]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os cenários de reprodução e regressão vivem nesta nota. A validação registra resultado e evidência; não duplica os CTs.

> [!example]- CT-B01 · Título claro do cenário
>
> ## Cenário
>
> **Descrição:** explique o comportamento incorreto que este caso reproduz ou protege contra regressão.
>
> **Pré-condições:**
> - Informe o estado necessário antes do teste.
> - Inclua usuário, dados e ambiente quando forem relevantes.
>
> **Dado** que ...
> **Quando** ...
> **Então** ...
>
> **Resultado esperado:** descreva o comportamento correto após a correção.
>
> **Pós-condição:** registre como o sistema deve ficar depois do teste.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-b01


> [!example]- CT-B02 · Editar registro sem perder os dados existentes
>
> ## Cenário
>
> **Descrição:** confirma que a correção mantém os dados já salvos ao editar o registro.
>
> **Pré-condições:**
> - Existe um registro criado com os dados necessários.
> - O usuário tem permissão para editá-lo.
>
> **Dado** um registro existente com dados preenchidos  
> **Quando** altero apenas o campo relacionado ao bug e salvo  
> **Então** a alteração é persistida sem apagar os demais dados.
>
> **Resultado esperado:** o comportamento corrigido funciona e os dados não relacionados permanecem intactos.
>
> **Pós-condição:** registro atualizado e disponível para consulta.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-b02
