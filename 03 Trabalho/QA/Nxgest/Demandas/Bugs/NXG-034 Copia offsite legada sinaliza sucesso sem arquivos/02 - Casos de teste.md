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

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Bug#^c1\|C1]] | [[02 - Casos de teste#^ct-b01\|CT-B01]], [[02 - Casos de teste#^ct-b02\|CT-B02]], [[02 - Casos de teste#^ct-b04\|CT-B04]], [[02 - Casos de teste#^ct-b05\|CT-B05]], [[02 - Casos de teste#^ct-b08\|CT-B08]] |
| [[01 - Bug#^c2\|C2]] | [[02 - Casos de teste#^ct-b03\|CT-B03]], [[02 - Casos de teste#^ct-b04\|CT-B04]], [[02 - Casos de teste#^ct-b05\|CT-B05]], [[02 - Casos de teste#^ct-b07\|CT-B07]], [[02 - Casos de teste#^ct-b08\|CT-B08]] |
| [[01 - Bug#^c3\|C3]] | [[02 - Casos de teste#^ct-b06\|CT-B06]] |
| [[01 - Bug#^c4\|C4]] | [[02 - Casos de teste#^ct-b06\|CT-B06]], [[02 - Casos de teste#^ct-b07\|CT-B07]], [[02 - Casos de teste#^ct-b08\|CT-B08]] |

> [!example]- CT-B01 · Transferência falha
>
> ## Cenário
>
> **Descrição:** Transferência falha.
>
> **Pré-condições:** SSH e SCP dublados, com SSH bem-sucedido e SCP falho, destino vazio e guardas verificadas.
>
> **Dado** SSH e SCP dublados, com SSH bem-sucedido e SCP falho, destino vazio e guardas verificadas.
> **Quando** executar fluxo de cópia em fixture
> **Então** retorna erro e não anuncia sucesso com zero arquivos.
>
> **Resultado esperado:** retorna erro e não anuncia sucesso com zero arquivos.
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

> [!example]- CT-B02 · Nenhum conjunto disponível
>
> ## Cenário
>
> **Descrição:** Nenhum conjunto disponível.
>
> **Pré-condições:** Origem sintética sem conjuntos completos e dublês de transporte.
>
> **Dado** Origem sintética sem conjuntos completos e dublês de transporte.
> **Quando** solicitar cópia
> **Então** retorna falha explícita sem criar falsa evidência off-site.
>
> **Resultado esperado:** retorna falha explícita sem criar falsa evidência off-site.
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

> [!example]- CT-B03 · Conjunto completo válido
>
> ## Cenário
>
> **Descrição:** Conjunto completo válido.
>
> **Pré-condições:** Origem sintética com banco, anexos, metadados, manifesto e conclusão compatíveis; destino isolado.
>
> **Dado** Origem sintética com banco, anexos, metadados, manifesto e conclusão compatíveis; destino isolado.
> **Quando** executar transporte dublado e conferir hashes
> **Então** todos os componentes e ID correspondem, sucesso só após verificação; nenhuma conexão real.
>
> **Resultado esperado:** todos os componentes e ID correspondem, sucesso só após verificação; nenhuma conexão real.
>
> **Pós-condição:** fixtures isoladas verificadas e removidas; infraestrutura e dados reais intocados.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b03

> [!example]- CT-B04 · Conjunto parcial ou corrompido
>
> ## Cenário
>
> **Descrição:** Conjunto parcial ou corrompido.
>
> **Pré-condições:** Fixtures com arquivo ausente, hash divergente e ID trocado, mais cópia anterior válida.
>
> **Dado** Fixtures com arquivo ausente, hash divergente e ID trocado, mais cópia anterior válida.
> **Quando** avaliar cada condição
> **Então** nenhuma é publicada como sucesso e cópia anterior permanece intacta.
>
> **Resultado esperado:** nenhuma é publicada como sucesso e cópia anterior permanece intacta.
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

^ct-b04

> [!example]- CT-B05 · Colisão ou erro de escrita
>
> ## Cenário
>
> **Descrição:** Colisão ou erro de escrita.
>
> **Pré-condições:** Destino sintético contém conjunto anterior e dublê falha escrita/cópia.
>
> **Dado** Destino sintético contém conjunto anterior e dublê falha escrita/cópia.
> **Quando** executar cada falha
> **Então** fluxo interrompe, não sobrescreve a cópia anterior e não registra sucesso.
>
> **Resultado esperado:** fluxo interrompe, não sobrescreve a cópia anterior e não registra sucesso.
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

^ct-b05

> [!example]- CT-B06 · Documentação e isolamento
>
> ## Cenário
>
> **Descrição:** Documentação e isolamento.
>
> **Pré-condições:** Guia 08, runbook 09 e guardas de chamadas reais previamente conferidos.
>
> **Dado** Guia 08, runbook 09 e guardas de chamadas reais previamente conferidos.
> **Quando** revisar instruções e exercitar dublês
> **Então** instruções são coerentes com formato de conjunto ou declaram explicitamente ausência de solução; nenhum SSH/SCP/Docker real.
>
> **Resultado esperado:** instruções são coerentes com formato de conjunto ou declaram explicitamente ausência de solução; nenhum SSH/SCP/Docker real.
>
> **Pós-condição:** fixtures isoladas verificadas e removidas; infraestrutura e dados reais intocados.
>
> **Critérios cobertos:** [[01 - Bug#^c3|C3]], [[01 - Bug#^c4|C4]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b06

> [!example]- CT-B07 · Espaços em caminhos e chave sintética
>
> ## Cenário
>
> **Descrição:** Espaços em caminhos e chave sintética.
>
> **Pré-condições:** Diretórios e caminho de chave fictícia com espaços; SSH/SCP dublados e guardas verificadas.
>
> **Dado** Diretórios e caminho de chave fictícia com espaços; SSH/SCP dublados e guardas verificadas.
> **Quando** copiar conjunto válido por argumentos estruturados
> **Então** a fixture completa chega ao destino correto sem interpretar caminho como comando ou acionar rede real.
>
> **Resultado esperado:** a fixture completa chega ao destino correto sem interpretar caminho como comando ou acionar rede real.
>
> **Pós-condição:** fixtures conferidas e removidas; infraestrutura e dados reais intactos.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]], [[01 - Bug#^c4|C4]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b07

> [!example]- CT-B08 · Interrupção, destino inacessível e origem inválida
>
> ## Cenário
>
> **Descrição:** Interrupção, destino inacessível e origem inválida.
>
> **Pré-condições:** Fixtures de interrupção, destino inacessível e ID de origem inválido com conjunto anterior preservado.
>
> **Dado** Fixtures de interrupção, destino inacessível e ID de origem inválido com conjunto anterior preservado.
> **Quando** exercitar cada falha com dublês
> **Então** a cópia falha fechada, não publica sucesso e mantém o anterior íntegro.
>
> **Resultado esperado:** a cópia falha fechada, não publica sucesso e mantém o anterior íntegro.
>
> **Pós-condição:** fixtures conferidas e removidas; infraestrutura e dados reais intactos.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c2|C2]], [[01 - Bug#^c4|C4]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b08
