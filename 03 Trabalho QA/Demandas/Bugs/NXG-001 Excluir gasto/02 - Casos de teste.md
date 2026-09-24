---
demanda: "[[01 - Bug]]"
status: planejado
pontos: ""
---
# Casos de teste — NXG-001

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> [!example]- CT-B01 Excluir gasto pela lista ^ct-b01
> **Tipo:** regressão
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado
> **Dado** um gasto existente na lista
> **Quando** confirmo a exclusão
> **Então** a API remove o gasto e ele deixa de aparecer.
> **Evidência:**

> [!example]- CT-B02 Cancelar exclusão ^ct-b02
> **Tipo:** regressão
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado
> **Dado** um gasto existente
> **Quando** cancelo a confirmação
> **Então** o gasto permanece e nenhuma exclusão é enviada.
> **Evidência:**

> [!example]- CT-B03 Tratar erro na exclusão ^ct-b03
> **Tipo:** negativo
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado
> **Dado** que a API retorna erro
> **Quando** tento excluir
> **Então** uma mensagem é exibida e o gasto permanece disponível.
> **Evidência:**
