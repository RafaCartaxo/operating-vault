---
demanda: FIN-MEL-0012
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: concluido
---

# Casos de teste — FIN-MEL-0012

## Matriz de cobertura

| Critério | CTs |
|---|---|
| C1 | CT-001 |
| C2 | CT-002 |
| C3 | CT-003 |
| C4 | CT-004 |
| C5 | CT-005 |
| C6 | CT-006 |

> [!example]- CT-001 · Cadastrar recorrência mensal
> Dado descrição, valor, cartão/conta e data inicial válidos; quando salvo; então a regra mensal fica ativa e identificável.
> **Resultado esperado:** regra criada sem duplicidade. **Critérios:** C1. **Execução:** planejado.

^ct-001

> [!example]- CT-002 · Gerar uma ocorrência por mês
> Dado uma regra ativa; quando o sistema recalcula dois meses; então gera uma ocorrência por mês sem duplicar a competência.
> **Resultado esperado:** origem e valor preservados. **Critérios:** C2. **Execução:** planejado.

^ct-002

> [!example]- CT-003 · Respeitar data final
> Dado uma regra com término; quando consulto o mês final e o seguinte; então gera no mês final e não depois.
> **Resultado esperado:** regra sem término permanece ativa. **Critérios:** C3. **Execução:** planejado.

^ct-003

> [!example]- CT-004 · Editar e encerrar sem apagar histórico
> Dado uma regra com ocorrência; quando altero ou encerro; então o histórico permanece e novas ocorrências respeitam o estado.
> **Resultado esperado:** nenhuma ocorrência anterior é apagada. **Critérios:** C4. **Execução:** planejado.

^ct-004

> [!example]- CT-005 · Não duplicar recorrente já incluído em fatura
> Dado recorrência vinculada a cartão e fatura contendo a cobrança; quando consulto o mês; então aparece para controle sem somar novamente ao saldo.
> **Resultado esperado:** fatura descontada uma única vez. **Critérios:** C5. **Execução:** planejado.

^ct-005

> [!example]- CT-006 · Rejeitar regra inválida sem ocorrência parcial
> Dado valor, data, cartão/conta ou término inválidos; quando tento salvar; então exibe erro e não cria regra nem ocorrência.
> **Resultado esperado:** nenhum dado parcial é persistido. **Critérios:** C6. **Execução:** planejado.

^ct-006
