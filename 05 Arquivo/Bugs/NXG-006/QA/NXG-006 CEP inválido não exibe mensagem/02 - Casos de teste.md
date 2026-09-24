---
demanda: "[[01 - Bug|NXG-006]]"
validacao: "[[03 - Validação dev]]"
status: planejado
pontos: 0
---
# Casos de teste — NXG-006

> [!info]- Navegação QA/DEV
> **Bug:** [[01 - Bug]]  
> **Validação QA:** [[03 - Validação dev]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> [!example]- CT-B01 · Informar CEP inválido
>
> ## Cenário
>
> **Descrição:** confirma que o formato inválido recebe feedback claro.
>
> **Pré-condições:** formulário de cliente aberto.
>
> **Dado** um CEP com menos de oito dígitos  
> **Quando** termino de digitar ou tento salvar  
> **Então** vejo uma mensagem informando que o CEP é inválido.
>
> **Resultado esperado:** o usuário é orientado a corrigir o CEP ou salvar sem CEP, sem bloquear os demais dados.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]]
>
> **Informações:** tipo negativo · camada UI · automação manual · execução planejado

^ct-b01
