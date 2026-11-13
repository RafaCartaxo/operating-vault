---
demanda: "[[01 - Bug]]"
status: planejado
pontos: 0
---
# Casos de teste — NXG-036

> [!info]- Navegação QA/DEV
> **README:** [[00 README]] · **Bug:** [[01 - Bug]] · **Casos:** [[02 - Casos de teste]] · **Validação:** [[03 - Validação dev]] · **Qase:** [[04 - Preparação Qase]] · **Pai:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/00 README|NXG-MEL-0009]]

> Todos os cenários são planejados; resultado deve ser preenchido somente após execução independente.

> [!example]- CT-B01 · Modelo Docker último vínculo
>
> ## Cenário
>
> **Descrição:** Modelo Docker último vínculo.
>
> **Pré-condições:** Imagem sintética em uso tem somente tag temporária.
>
> **Dado/Quando/Então:** Dado o container em execução, quando o dublê remove a última tag sem force, então falha e imagem/tag permanecem.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c4|C4]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b01

> [!example]- CT-B02 · Três fluxos com pin novo
>
> ## Cenário
>
> **Descrição:** Três fluxos com pin novo.
>
> **Pré-condições:** Staging normal, adoção e baseline usam imagem autenticada e dublê stateful.
>
> **Dado/Quando/Então:** Dado pin ausente, quando cada fluxo cria e verifica pin antes de untag, então remove somente a tag temporária, conserva imagem e conclui seus próprios gates.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]] · [[01 - Bug#^c3|C3]] · [[01 - Bug#^c4|C4]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b02

> [!example]- CT-B03 · Pin existente exato
>
> ## Cenário
>
> **Descrição:** Pin existente exato.
>
> **Pré-condições:** Pin sintético já aponta ao ID autenticado.
>
> **Dado/Quando/Então:** Dado pin exato, quando o fluxo o revalida, então pode reutilizá-lo sem alterar imagem ou tag alheia e apenas remover a temporária própria.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]] · [[01 - Bug#^c2|C2]] · [[01 - Bug#^c3|C3]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b03

> [!example]- CT-B04 · Colisão de pin e origem ausente
>
> ## Cenário
>
> **Descrição:** Colisão de pin e origem ausente.
>
> **Pré-condições:** Pin divergente ou seleção/origem autenticada ausente.
>
> **Dado/Quando/Então:** Dado um desses estados, quando o fluxo inicia, então falha antes de untag e não altera recursos nem publica sucesso.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]] · [[01 - Bug#^c2|C2]] · [[01 - Bug#^c3|C3]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b04

> [!example]- CT-B05 · Tag temporária preexistente
>
> ## Cenário
>
> **Descrição:** Tag temporária preexistente.
>
> **Pré-condições:** Loader recebe tar sintético válido e tag temporária já existe, inclusive com mesmo ID.
>
> **Dado/Quando/Então:** Dado conflito, quando o loader tenta carregar, então recusa sem alterar a tag, criar pin ou iniciar serviço.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]] · [[01 - Bug#^c3|C3]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b05

> [!example]- CT-B06 · Erros e ambiguidade de pin/untag
>
> ## Cenário
>
> **Descrição:** Erros e ambiguidade de pin/untag.
>
> **Pré-condições:** Dublê injeta erro ou timeout antes/depois de tag, inspect e untag.
>
> **Dado/Quando/Então:** Dado resultado desconhecido ou falho, quando ocorre a operação, então não há sucesso nem promoção e estado parcial próprio é preservado para reparo.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]] · [[01 - Bug#^c3|C3]] · [[01 - Bug#^c6|C6]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b06

> [!example]- CT-B07 · Concorrência e identidade trocada
>
> ## Cenário
>
> **Descrição:** Concorrência e identidade trocada.
>
> **Pré-condições:** Duas operações competem pelo lock ou a referência muda entre inspeções.
>
> **Dado/Quando/Então:** Dado lock ocupado ou identidade divergente, quando se tenta prosseguir, então apenas a operação válida pode alterar referências e nenhuma publicação incorreta ocorre.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]] · [[01 - Bug#^c2|C2]] · [[01 - Bug#^c3|C3]] · [[01 - Bug#^c6|C6]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b07

> [!example]- CT-B08 · Baseline completa conclui pending
>
> ## Cenário
>
> **Descrição:** Baseline completa conclui pending.
>
> **Pré-condições:** Imagem/tar/seleção/saúde sintéticos válidos; estado inicial sem marker nem pending.
>
> **Dado/Quando/Então:** Dado fluxo inicial bem-sucedido, quando pin e marker completos são verificados, então sucesso só é emitido após conclusão ou arquivo verificável do pending próprio.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]] · [[01 - Bug#^c4|C4]] · [[01 - Bug#^c5|C5]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b08

> [!example]- CT-B09 · Falhas em marker e conclusão
>
> ## Cenário
>
> **Descrição:** Falhas em marker e conclusão.
>
> **Pré-condições:** Fixtures injetam escrita parcial, colisão, falha de arquivamento, interrupção antes/depois de marker e ausência de health.
>
> **Dado/Quando/Então:** Dado cada ponto de falha, quando acontece interrupção, então não há falso retorno zero; pending ou evidência equivalente preserva estado e repetição indevida é bloqueada.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c5|C5]] · [[01 - Bug#^c6|C6]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b09

> [!example]- CT-B10 · Reentrada com marker completo
>
> ## Cenário
>
> **Descrição:** Reentrada com marker completo.
>
> **Pré-condições:** Marker sintético completo existe com pending concluído ou presente.
>
> **Dado/Quando/Então:** Dado baseline estabelecida, quando se tenta nova primeira entrada, então a entrada é recusada antes de efeitos independentemente do pending.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c5|C5]] · [[01 - Bug#^c6|C6]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b10

> [!example]- CT-B11 · Plano de reparo do estado atual
>
> ## Cenário
>
> **Descrição:** Plano de reparo do estado atual.
>
> **Pré-condições:** Fixture espelha marker completo, pending remanescente, pin, tar e seleção; nenhuma origem real é acessada.
>
> **Dado/Quando/Então:** Dado estado compatível, quando o procedimento proposto verifica evidências sob lock, então só prepara conclusão controlada e registra prova, sem executar reparo real.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c6|C6]] · [[01 - Bug#^c7|C7]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b11

> [!example]- CT-B12 · Reparo recusa evidência inconsistente
>
> ## Cenário
>
> **Descrição:** Reparo recusa evidência inconsistente.
>
> **Pré-condições:** Fixture possui um entre SHA, tar, imagem, health, marker, pending, owner, lock ou seleção divergente/ausente.
>
> **Dado/Quando/Então:** Dado cada divergência, quando o reparo sintético é avaliado, então falha fechado e preserva evidências, recursos e legado; não remove pending nem aceita atestado autodeclarado.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]] · [[01 - Bug#^c6|C6]] · [[01 - Bug#^c7|C7]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b12

> [!example]- CT-B13 · Regressão e isolamento dos gates
>
> ## Cenário
>
> **Descrição:** Regressão e isolamento dos gates.
>
> **Pré-condições:** Runner local isolado com dublês para rede e binários externos.
>
> **Dado/Quando/Então:** Dado os gates existentes, quando executados com falha sintética e com sucesso, então propagam falhas e cobrem os três fluxos sem Docker/SSH/GH/curl reais.
>
> **Resultado esperado:** observar as condições acima e não publicar sucesso em falha.
>
> **Pós-condição:** preservar recursos sintéticos fora da operação e registrar evidências.
>
> **Critérios cobertos:** [[01 - Bug#^c3|C3]] · [[01 - Bug#^c4|C4]]
>
> **Tipo:** regressão · **Camada:** integração local · **Automação:** automatizado · **Execução:** planejado

^ct-b13

## Matriz de cobertura

| Critério | CTs |
|---|---|
| C1 | CT-B02, CT-B03, CT-B04, CT-B07, CT-B08 |
| C2 | CT-B03, CT-B04, CT-B05, CT-B06, CT-B07, CT-B12 |
| C3 | CT-B02, CT-B03, CT-B04, CT-B05, CT-B06, CT-B07, CT-B13 |
| C4 | CT-B01, CT-B02, CT-B08, CT-B13 |
| C5 | CT-B08, CT-B09, CT-B10 |
| C6 | CT-B06, CT-B07, CT-B09, CT-B10, CT-B11, CT-B12 |
| C7 | CT-B11, CT-B12 |
