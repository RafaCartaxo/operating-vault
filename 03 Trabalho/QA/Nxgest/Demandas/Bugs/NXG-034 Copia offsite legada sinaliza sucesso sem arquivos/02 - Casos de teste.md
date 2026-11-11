---
demanda: "[[01 - Bug]]"
status: planejado
pontos: ""
---
# Casos de teste — NXG-034

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Fix DEV:** pendente de encaminhamento pela Coordenação.
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-034 Copia offsite legada sinaliza sucesso sem arquivos/03 - Validação dev|Validação QA]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os cenários de reprodução e regressão vivem nesta nota. A validação registra resultado e evidência; não duplica os CTs.

> [!example]- CT-B01 · Reproduzir e retestar Copia offsite legada sinaliza sucesso sem arquivos
>
> ## Cenário
>
> **Descrição:** validar a correção da evidência pai CT-012 / C7.
>
> **Pré-condições:** fixtures sintéticas e dublês comprovadamente interceptados; nenhum recurso real.
>
> **Dado** o cenário descrito no bug
> **Quando** a condição é exercitada localmente
> **Então** Sincronizar instruções e comportamento para impedir declaração de sucesso sem conjunto válido; estabelecer ou explicitar procedimento seguro de transporte e verificação do conjunto completo, sem qualquer conexão real.
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
