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

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Bug#^c1\|C1]] | [[02 - Casos de teste#^ct-b01\|CT-B01]], [[02 - Casos de teste#^ct-b02\|CT-B02]], [[02 - Casos de teste#^ct-b03\|CT-B03]], [[02 - Casos de teste#^ct-b07\|CT-B07]], [[02 - Casos de teste#^ct-b08\|CT-B08]] |
| [[01 - Bug#^c2\|C2]] | [[02 - Casos de teste#^ct-b03\|CT-B03]], [[02 - Casos de teste#^ct-b06\|CT-B06]], [[02 - Casos de teste#^ct-b08\|CT-B08]] |
| [[01 - Bug#^c3\|C3]] | [[02 - Casos de teste#^ct-b04\|CT-B04]], [[02 - Casos de teste#^ct-b05\|CT-B05]] |
| [[01 - Bug#^c4\|C4]] | [[02 - Casos de teste#^ct-b06\|CT-B06]], [[02 - Casos de teste#^ct-b07\|CT-B07]] |

> [!example]- CT-B01 · Referência com anexo correspondente
>
> ## Cenário
>
> **Descrição:** Referência com anexo correspondente.
>
> **Pré-condições:** Banco e tar sintéticos com ID de conjunto igual e referência para arquivo existente.
>
> **Dado** Banco e tar sintéticos com ID de conjunto igual e referência para arquivo existente.
> **Quando** executar ensaio em destino exclusivo
> **Então** comparação de referências e conteúdo passa e evidencia identificador do conjunto.
>
> **Resultado esperado:** comparação de referências e conteúdo passa e evidencia identificador do conjunto.
>
> **Pós-condição:** fixtures isoladas verificadas e removidas; infraestrutura e dados reais intocados.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b01

> [!example]- CT-B02 · Referência sem anexo
>
> ## Cenário
>
> **Descrição:** Referência sem anexo.
>
> **Pré-condições:** Banco sintético referencia arquivo que não existe no tar, com hashes individuais válidos.
>
> **Dado** Banco sintético referencia arquivo que não existe no tar, com hashes individuais válidos.
> **Quando** comparar referências restauradas
> **Então** o ensaio identifica a referência ausente e recusa resultado consistente.
>
> **Resultado esperado:** o ensaio identifica a referência ausente e recusa resultado consistente.
>
> **Pós-condição:** fixtures isoladas verificadas e removidas; infraestrutura e dados reais intocados.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b02

> [!example]- CT-B03 · Nenhuma referência legítima versus erro
>
> ## Cenário
>
> **Descrição:** Nenhuma referência legítima versus erro.
>
> **Pré-condições:** Uma fixture demonstra lista de referências vazia e anexos vazios; outra simula falha de leitura.
>
> **Dado** Uma fixture demonstra lista de referências vazia e anexos vazios; outra simula falha de leitura.
> **Quando** validar ambas as condições
> **Então** zero legítimo é identificado como tal e erro não é tratado como vazio.
>
> **Resultado esperado:** zero legítimo é identificado como tal e erro não é tratado como vazio.
>
> **Pós-condição:** fixtures isoladas verificadas e removidas; infraestrutura e dados reais intocados.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c2|C2]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b03

> [!example]- CT-B04 · Falha de escrita ou cópia
>
> ## Cenário
>
> **Descrição:** Falha de escrita ou cópia.
>
> **Pré-condições:** Conjunto anterior íntegro com hashes conhecidos; escrita e cópia em dublês podem falhar individualmente.
>
> **Dado** Conjunto anterior íntegro com hashes conhecidos; escrita e cópia em dublês podem falhar individualmente.
> **Quando** injetar cada erro durante geração ou transporte sintético
> **Então** retorna falha sem promover conjunto parcial nem modificar arquivos e hashes anteriores.
>
> **Resultado esperado:** retorna falha sem promover conjunto parcial nem modificar arquivos e hashes anteriores.
>
> **Pós-condição:** fixtures isoladas verificadas e removidas; infraestrutura e dados reais intocados.
>
> **Critérios cobertos:** [[01 - Bug#^c3|C3]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b04

> [!example]- CT-B05 · Interrupção e retomada
>
> ## Cenário
>
> **Descrição:** Interrupção e retomada.
>
> **Pré-condições:** Conjunto anterior íntegro e saída parcial em fixture exclusiva.
>
> **Dado** Conjunto anterior íntegro e saída parcial em fixture exclusiva.
> **Quando** interromper antes da conclusão e repetir
> **Então** parcial não é marcado completo; anterior permanece byte a byte íntegro.
>
> **Resultado esperado:** parcial não é marcado completo; anterior permanece byte a byte íntegro.
>
> **Pós-condição:** fixtures isoladas verificadas e removidas; infraestrutura e dados reais intocados.
>
> **Critérios cobertos:** [[01 - Bug#^c3|C3]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b05

> [!example]- CT-B06 · Limites e isolamento
>
> ## Cenário
>
> **Descrição:** Limites e isolamento.
>
> **Pré-condições:** Interceptadores Docker/curl/ssh/scp e arquivos sintéticos em destino exclusivo.
>
> **Dado** Interceptadores Docker/curl/ssh/scp e arquivos sintéticos em destino exclusivo.
> **Quando** verificar guardas antes de cada comando e executar cenários
> **Então** nenhum binário ou serviço real é acionado e relatório distingue associação local de consistência temporal/restore real.
>
> **Resultado esperado:** nenhum binário ou serviço real é acionado e relatório distingue associação local de consistência temporal/restore real.
>
> **Pós-condição:** fixtures isoladas verificadas e removidas; infraestrutura e dados reais intocados.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]], [[01 - Bug#^c4|C4]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b06

> [!example]- CT-B07 · Caminhos inseguros e tamanho divergente
>
> ## Cenário
>
> **Descrição:** Caminhos inseguros e tamanho divergente.
>
> **Pré-condições:** Fixtures de referências relativas, caminho absoluto, travessia, link e tamanho divergente.
>
> **Dado** Fixtures de referências relativas, caminho absoluto, travessia, link e tamanho divergente.
> **Quando** reconciliar referências e anexos extraídos
> **Então** caminhos inseguros, links ou tamanho divergente são recusados; nenhum arquivo fora da fixture é lido.
>
> **Resultado esperado:** caminhos inseguros, links ou tamanho divergente são recusados; nenhum arquivo fora da fixture é lido.
>
> **Pós-condição:** fixtures conferidas e removidas; infraestrutura e dados reais intactos.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c4|C4]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b07

> [!example]- CT-B08 · Arquivos órfãos são relatados
>
> ## Cenário
>
> **Descrição:** Arquivos órfãos são relatados.
>
> **Pré-condições:** Fixtures com referências íntegras e arquivo não referenciado.
>
> **Dado** Fixtures com referências íntegras e arquivo não referenciado.
> **Quando** conciliar o conjunto sintético
> **Então** referências válidas são verificadas e órfãos são relatados sem presumir automaticamente que sejam perda ou rejeitar o conjunto por sua mera existência.
>
> **Resultado esperado:** referências válidas são verificadas e órfãos são relatados sem presumir automaticamente que sejam perda ou rejeitar o conjunto por sua mera existência.
>
> **Pós-condição:** fixtures conferidas e removidas; infraestrutura e dados reais intactos.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c2|C2]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b08
