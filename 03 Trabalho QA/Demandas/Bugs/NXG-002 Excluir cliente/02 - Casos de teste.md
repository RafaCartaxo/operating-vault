---
demanda: "[[01 - Bug]]"
status: planejado
pontos: ""
---
# Casos de teste — NXG-002

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> [!example]- CT-B01 Excluir cliente sem contratos ativos ^ct-b01
> **Tipo:** regressão
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado
> **Dado** um cliente sem contratos ativos
> **Quando** confirmo a exclusão
> **Então** a API remove o cliente e a navegação é atualizada.
> **Evidência:**

> [!example]- CT-B02 Impedir exclusão com contratos ativos ^ct-b02
> **Tipo:** negativo
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado
> **Dado** um cliente com contratos ativos
> **Quando** tento excluí-lo
> **Então** a exclusão é impedida e recebo orientação.
> **Evidência:**

> [!example]- CT-B03 Cancelar exclusão ou tratar erro ^ct-b03
> **Tipo:** negativo
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado
> **Dado** um cliente exibido na ficha
> **Quando** cancelo ou a API retorna erro
> **Então** o cliente permanece visível e uma mensagem é exibida.
> **Evidência:**
