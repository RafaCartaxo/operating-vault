---
demanda: "[[01 - Bug|NXG-005]]"
validacao: "[[03 - Validação dev]]"
status: planejado
pontos: 0
---
# Casos de teste — NXG-005

> [!info]- Navegação QA/DEV
> **Bug:** [[01 - Bug]]  
> **Validação QA:** [[03 - Validação dev]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> [!example]- CT-B01 · Remover CEP salvo na edição
>
> ## Cenário
>
> **Descrição:** confirma a remoção persistida de um CEP existente.
>
> **Pré-condições:** cliente salvo com CEP e localização aproximada derivada do CEP.
>
> **Dado** um cliente com CEP salvo  
> **Quando** removo o CEP e salvo a edição  
> **Então** o CEP e a localização aproximada derivada são removidos.
>
> **Resultado esperado:** CEP vazio na edição/API; GPS manual independente permanece.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]]
>
> **Informações:** tipo regressão · camada UI/API · automação manual · execução planejado

^ct-b01
