---
demanda: "[[01 - Bug]]"
status: "concluido"
pontos: 3
projeto: "nxgest"
epico: "NXG-EPIC-0001"
responsavel: "NX Gest · QA e Coordenação"
---
# Casos de teste — NXG-029

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Fix DEV:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/00 README|Execução DEV]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/03 - Validação dev|Validação QA]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os cenários de reprodução e regressão vivem nesta nota. A validação registra resultado e evidência; não duplica os CTs.

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Bug#^c1\|C1]] | [[02 - Casos de teste#^ct-b01\|CT-B01]] |
| [[01 - Bug#^c2\|C2]] | [[02 - Casos de teste#^ct-b02\|CT-B02]] |

> [!example]- CT-B01 · Valores com espacos
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[03 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** A configuração recém-gerada de staging aceita MAIL_FROM_NAME com espaço sem tentar executar parte do valor como comando.
>
> **Pré-condições:** diretório temporário sem env existente e comandos externos substituídos por dublês; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** diretório temporário sem env existente e comandos externos substituídos por dublês  
> **Quando** gero e carrego a configuração com o fluxo do script  
> **Então** o carregamento conclui e MAIL_FROM_NAME mantém NX Gest.
>
> **Resultado esperado:** o carregamento conclui e MAIL_FROM_NAME mantém NX Gest.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** unit  
> **Automação:** ambos  
> **Execução:** executado

^ct-b01

> [!example]- CT-B02 · Preservacao de configuracao
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[03 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** A correção mantém geração de segredos aleatórios, permissões restritas, e-mail console e arquivo existente sem sobrescrever seus valores.
>
> **Pré-condições:** configuração sintética existente ou recém-gerada; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** configuração sintética existente ou recém-gerada  
> **Quando** executo os testes isolados de geração e reutilização  
> **Então** não há sobrescrita de segredo existente, permissão é restrita no arquivo novo e não se envia e-mail real.
>
> **Resultado esperado:** não há sobrescrita de segredo existente, permissão é restrita no arquivo novo e não se envia e-mail real.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** unit  
> **Automação:** ambos  
> **Execução:** executado

^ct-b02
