---
demanda: "[[01 - Bug]]"
status: planejado
pontos: ""
---
# Casos de teste — NXG-035

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]<br>
> **Bug:** [[01 - Bug]]<br>
> **Casos de teste:** [[02 - Casos de teste]]<br>
> **Fix DEV:** aguardando encaminhamento pela Coordenação.
> **Preparação Qase:** [[04 - Preparação Qase]]<br>
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/03 - Validação dev|Validação QA]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os cenários de reprodução e regressão vivem nesta nota. A validação registra resultado e evidência; não duplica os CTs.

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Bug#^c1\|C1]] | [[02 - Casos de teste#^ct-b01\|CT-B01]], [[02 - Casos de teste#^ct-b02\|CT-B02]], [[02 - Casos de teste#^ct-b03\|CT-B03]] |
| [[01 - Bug#^c2\|C2]] | [[02 - Casos de teste#^ct-b03\|CT-B03]], [[02 - Casos de teste#^ct-b06\|CT-B06]] |
| [[01 - Bug#^c3\|C3]] | [[02 - Casos de teste#^ct-b01\|CT-B01]], [[02 - Casos de teste#^ct-b02\|CT-B02]], [[02 - Casos de teste#^ct-b03\|CT-B03]], [[02 - Casos de teste#^ct-b04\|CT-B04]], [[02 - Casos de teste#^ct-b07\|CT-B07]] |
| [[01 - Bug#^c4\|C4]] | [[02 - Casos de teste#^ct-b01\|CT-B01]], [[02 - Casos de teste#^ct-b02\|CT-B02]], [[02 - Casos de teste#^ct-b05\|CT-B05]], [[02 - Casos de teste#^ct-b07\|CT-B07]] |
| [[01 - Bug#^c5\|C5]] | [[02 - Casos de teste#^ct-b06\|CT-B06]], [[02 - Casos de teste#^ct-b07\|CT-B07]] |

> [!example]- CT-B01 · CI executa os dois testes
>
> ## Cenário
>
> **Descrição:** CI executa os dois testes.
>
> **Pré-condições:** Workflow CI representado localmente e runner sintético que registra cada teste executado; guardas verificadas.
>
> **Dado** Workflow CI representado localmente e runner sintético que registra cada teste executado; guardas verificadas.
> **Quando** exercitar o gate de CI em fixture
> **Então** os dois nomes distintos são efetivamente executados e reportados, sem recurso real.
>
> **Resultado esperado:** os dois nomes distintos são efetivamente executados e reportados, sem recurso real.
>
> **Pós-condição:** fixtures isoladas removidas; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c3|C3]], [[01 - Bug#^c4|C4]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** CI/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b01

> [!example]- CT-B02 · CD manual executa os dois testes
>
> ## Cenário
>
> **Descrição:** CD manual executa os dois testes.
>
> **Pré-condições:** Caminho workflow_dispatch representado localmente; runner sintético e guardas previamente verificadas.
>
> **Dado** Caminho workflow_dispatch representado localmente; runner sintético e guardas previamente verificadas.
> **Quando** exercitar o gate manual em fixture
> **Então** os dois testes executam e o resultado aparece no gate; não se chama deploy real.
>
> **Resultado esperado:** os dois testes executam e o resultado aparece no gate; não se chama deploy real.
>
> **Pós-condição:** fixtures isoladas removidas; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c3|C3]], [[01 - Bug#^c4|C4]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** CI/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b02

> [!example]- CT-B03 · Falha de cada teste bloqueia cada gate
>
> ## Cenário
>
> **Descrição:** Falha de cada teste bloqueia cada gate.
>
> **Pré-condições:** Os dois testes podem falhar individualmente por injeção em cópia sintética; CI e CD manual dublados.
>
> **Dado** Os dois testes podem falhar individualmente por injeção em cópia sintética; CI e CD manual dublados.
> **Quando** injetar cada falha em cada gate
> **Então** todos os quatro cenários retornam falha não mascarada e nenhum passo dependente de promoção executa.
>
> **Resultado esperado:** todos os quatro cenários retornam falha não mascarada e nenhum passo dependente de promoção executa.
>
> **Pós-condição:** fixtures isoladas removidas; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c2|C2]], [[01 - Bug#^c3|C3]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** CI/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b03

> [!example]- CT-B04 · Dublês ausentes ou desviados
>
> ## Cenário
>
> **Descrição:** Dublês ausentes ou desviados.
>
> **Pré-condições:** Guardas de docker, curl, ssh e scp; fixture permite trocar resolução por binário proibido ou remover uma guarda.
>
> **Dado** Guardas de docker, curl, ssh e scp; fixture permite trocar resolução por binário proibido ou remover uma guarda.
> **Quando** sondar cada comando e subprocesso antes dos testes
> **Então** guarda ausente, divergente ou falha aborta antes do teste e nenhuma chamada chega ao CLI/daemon ou rede real.
>
> **Resultado esperado:** guarda ausente, divergente ou falha aborta antes do teste e nenhuma chamada chega ao CLI/daemon ou rede real.
>
> **Pós-condição:** fixtures isoladas removidas; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c3|C3]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** CI/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b04

> [!example]- CT-B05 · Runner sem pressupor ambiente pessoal
>
> ## Cenário
>
> **Descrição:** Runner sem pressupor ambiente pessoal.
>
> **Pré-condições:** Fixture sem /home do usuário, sem bwrap ou com namespace de usuário indisponível; Node/auxiliares controlados.
>
> **Dado** Fixture sem /home do usuário, sem bwrap ou com namespace de usuário indisponível; Node/auxiliares controlados.
> **Quando** inicializar runner em cada variante
> **Então** runner usa requisitos explicitamente providos ou aborta com erro antes de qualquer teste; não infere ambiente GitHub real.
>
> **Resultado esperado:** runner usa requisitos explicitamente providos ou aborta com erro antes de qualquer teste; não infere ambiente GitHub real.
>
> **Pós-condição:** fixtures isoladas removidas; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c4|C4]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** CI/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b05

> [!example]- CT-B06 · Regressão dos gates anteriores
>
> ## Cenário
>
> **Descrição:** Regressão dos gates anteriores.
>
> **Pré-condições:** CI/CD dublados e testes anteriores representados por sentinelas sintéticas com possibilidade de falha.
>
> **Dado** CI/CD dublados e testes anteriores representados por sentinelas sintéticas com possibilidade de falha.
> **Quando** verificar descoberta e executar cada falha em fixture
> **Então** test:safety, test:deploy e test:backup continuam incluídos, falhas propagam e NO-GO operacional não é removido.
>
> **Resultado esperado:** test:safety, test:deploy e test:backup continuam incluídos, falhas propagam e NO-GO operacional não é removido.
>
> **Pós-condição:** fixtures isoladas removidas; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]], [[01 - Bug#^c5|C5]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** CI/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b06

> [!example]- CT-B07 · Resultados e limitações explícitos
>
> ## Cenário
>
> **Descrição:** Resultados e limitações explícitos.
>
> **Pré-condições:** Relatório e documentação gerados somente com dados sintéticos; CI externo não foi executado.
>
> **Dado** Relatório e documentação gerados somente com dados sintéticos; CI externo não foi executado.
> **Quando** revisar evidências e logs com marcador secreto sintético
> **Então** nenhum segredo é exposto, execução isolada é identificada e compatibilidade/restore/proveniência reais não são declarados comprovados.
>
> **Resultado esperado:** nenhum segredo é exposto, execução isolada é identificada e compatibilidade/restore/proveniência reais não são declarados comprovados.
>
> **Pós-condição:** fixtures isoladas removidas; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c3|C3]], [[01 - Bug#^c4|C4]], [[01 - Bug#^c5|C5]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** CI/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b07
