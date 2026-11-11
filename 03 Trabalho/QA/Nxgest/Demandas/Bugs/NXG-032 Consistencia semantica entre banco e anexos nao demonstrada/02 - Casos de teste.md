---
demanda: "[[01 - Bug]]"
status: planejado
pontos: ""
---
# Casos de teste — NXG-032

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Fix DEV:** pendente de encaminhamento pela Coordenação.
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/03 - Validação dev|Validação QA]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os cenários de reprodução e regressão vivem nesta nota. A validação registra resultado e evidência; não duplica os CTs.

> [!example]- CT-B01 · Reproduzir e retestar Consistencia semantica entre banco e anexos nao demonstrada
>
> ## Cenário
>
> **Descrição:** validar a correção da evidência pai CT-005 / C3.
>
> **Pré-condições:** fixtures sintéticas e dublês comprovadamente interceptados; nenhum recurso real.
>
> **Dado** o cenário descrito no bug
> **Quando** a condição é exercitada localmente
> **Então** Produzir e validar ensaio sintético que confronte referências de banco e anexos, incluindo caso divergente que bloqueie alegação de conjunto semanticamente consistente. Não extrapolar para PostgreSQL real.
>
> **Resultado esperado:** condição corrigida e preservação das garantias.
>
> **Pós-condição:** fixtures removidas sem tocar recursos reais.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c2|C2]]
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** infra/documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-b01
