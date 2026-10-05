---
demanda: "[[01 - Bug]]"
status: concluido
pontos: 3
---
# Casos de teste — FIN-BUG-0001

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Fix DEV:** [[03 Trabalho/DEV/Financas Pessoais/Fixes/FIN-FIX-0001/00 README|FIN-FIX-0001 — correção técnica concluída; aguardando QA]]
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Validação QA:** [[03 - Validação dev|Validação QA]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os cenários de reprodução e regressão vivem nesta nota. A validação registra resultado e evidência; não duplica os CTs.

> [!example]- CT-B01 · Carregar lançamentos com recorrência ativa
>
> ## Cenário
>
> **Descrição:** reproduz o erro 500 ao consultar os lançamentos do mês com uma recorrência ativa.
>
> **Pré-condições:** existe uma recorrência ativa no mês consultado e o backend está disponível.
>
> **Dado** uma recorrência ativa para outubro de 2026
> **Quando** consulto `GET /api/lancamentos?mes=2026-10` ou abro Acompanhamento
> **Então** a lista de lançamentos é carregada sem erro 500.
>
> **Resultado esperado:** os lançamentos do mês são retornados e a ocorrência recorrente é exibida.
>
> **Pós-condição:** consulta mensal concluída sem bloqueio do banco.
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
> **Execução:** reprovado na rodada inicial.

^ct-b01


> [!example]- CT-B02 · Recalcular mês sem duplicar ocorrências
>
> ## Cenário
>
> **Descrição:** protege a geração idempotente depois que a consulta mensal voltar a funcionar.
>
> **Pré-condições:** existe uma recorrência ativa e uma ocorrência já gerada para a competência.
>
> **Dado** uma recorrência já processada no mês
> **Quando** consulto novamente o mesmo mês
> **Então** a lista carrega e não cria uma segunda ocorrência.
>
> **Resultado esperado:** permanece no máximo uma ocorrência por recorrência e competência.
>
> **Pós-condição:** consulta repetida concluída sem duplicidade.
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

^ct-b02
