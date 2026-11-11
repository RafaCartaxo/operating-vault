---
demanda: "[[01 - Bug]]"
status: planejado
pontos: ""
---
# Casos de teste — NXG-033

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]
> **Bug:** [[01 - Bug]]
> **Casos de teste:** [[02 - Casos de teste]]
> **Fix DEV:** pendente de encaminhamento pela Coordenação.
> **Preparação Qase:** [[04 - Preparação Qase]]
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/03 - Validação dev|Validação QA]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os cenários de reprodução e regressão vivem nesta nota. A validação registra resultado e evidência; não duplica os CTs.

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Bug#^c1\|C1]] | [[02 - Casos de teste#^ct-b01\|CT-B01]], [[02 - Casos de teste#^ct-b02\|CT-B02]], [[02 - Casos de teste#^ct-b04\|CT-B04]], [[02 - Casos de teste#^ct-b06\|CT-B06]] |
| [[01 - Bug#^c2\|C2]] | [[02 - Casos de teste#^ct-b03\|CT-B03]], [[02 - Casos de teste#^ct-b04\|CT-B04]], [[02 - Casos de teste#^ct-b07\|CT-B07]] |
| [[01 - Bug#^c3\|C3]] | [[02 - Casos de teste#^ct-b05\|CT-B05]], [[02 - Casos de teste#^ct-b08\|CT-B08]] |
| [[01 - Bug#^c4\|C4]] | [[02 - Casos de teste#^ct-b06\|CT-B06]], [[02 - Casos de teste#^ct-b07\|CT-B07]], [[02 - Casos de teste#^ct-b08\|CT-B08]] |

> [!example]- CT-B01 · Schema incompatível ou ausente
>
> ## Cenário
>
> **Descrição:** Schema incompatível ou ausente.
>
> **Pré-condições:** Evidência sintética estruturada indica incompatível; variante omite prova ou responsável.
>
> **Dado** Evidência sintética estruturada indica incompatível; variante omite prova ou responsável.
> **Quando** validar precondições
> **Então** preflight recusa ou mantém no-go sem declarar compatibilidade comprovada.
>
> **Resultado esperado:** preflight recusa ou mantém no-go sem declarar compatibilidade comprovada.
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

> [!example]- CT-B02 · Declaração e prova contraditórias
>
> ## Cenário
>
> **Descrição:** Declaração e prova contraditórias.
>
> **Pré-condições:** Declaração compatible e evidência estruturada de schema incompatível; hashes corretos.
>
> **Dado** Declaração compatible e evidência estruturada de schema incompatível; hashes corretos.
> **Quando** verificar coerência dos campos
> **Então** contradição explícita é detectada e bloqueia liberação; não se exige interpretar texto arbitrário como prova.
>
> **Resultado esperado:** contradição explícita é detectada e bloqueia liberação; não se exige interpretar texto arbitrário como prova.
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

> [!example]- CT-B03 · SHA e imagem anterior divergentes
>
> ## Cenário
>
> **Descrição:** SHA e imagem anterior divergentes.
>
> **Pré-condições:** Evidência sintética relaciona SHA A à imagem A; inventário dublado apresenta imagem B ou SHA sem vínculo.
>
> **Dado** Evidência sintética relaciona SHA A à imagem A; inventário dublado apresenta imagem B ou SHA sem vínculo.
> **Quando** avaliar pré-condições
> **Então** divergência ou vínculo ausente impede prontidão; caminho positivo com mesmo SHA e imagem é verificável.
>
> **Resultado esperado:** divergência ou vínculo ausente impede prontidão; caminho positivo com mesmo SHA e imagem é verificável.
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

> [!example]- CT-B04 · Configuração e mounts incompletos
>
> ## Cenário
>
> **Descrição:** Configuração e mounts incompletos.
>
> **Pré-condições:** Inventário e evidência sintéticos com mount ausente, digest divergente ou configuração indisponível.
>
> **Dado** Inventário e evidência sintéticos com mount ausente, digest divergente ou configuração indisponível.
> **Quando** avaliar gate
> **Então** cada condição interrompe ou mantém no-go antes de qualquer operação de serviço.
>
> **Resultado esperado:** cada condição interrompe ou mantém no-go antes de qualquer operação de serviço.
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

> [!example]- CT-B05 · Health, integridade e SHA no retorno
>
> ## Cenário
>
> **Descrição:** Health, integridade e SHA no retorno.
>
> **Pré-condições:** Respostas dubladas healthy, timeout e negativas; evidências sintéticas com dados ausentes e SHA divergente.
>
> **Dado** Respostas dubladas healthy, timeout e negativas; evidências sintéticas com dados ausentes e SHA divergente.
> **Quando** avaliar separadamente os três componentes
> **Então** sem health positivo, integridade demonstrada e identidade de SHA comprovada, não declara recuperação bem-sucedida.
>
> **Resultado esperado:** sem health positivo, integridade demonstrada e identidade de SHA comprovada, não declara recuperação bem-sucedida.
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

> [!example]- CT-B06 · Revisão humana e isolamento
>
> ## Cenário
>
> **Descrição:** Revisão humana e isolamento.
>
> **Pré-condições:** Evidências sem segredo e guardas Docker/curl/ssh/scp previamente verificadas.
>
> **Dado** Evidências sem segredo e guardas Docker/curl/ssh/scp previamente verificadas.
> **Quando** executar cenários e revisar documentação
> **Então** reporte diferencia validação mecânica de revisão humana e não afirma compatibilidade real; CLI/daemon e serviços reais não são chamados.
>
> **Resultado esperado:** reporte diferencia validação mecânica de revisão humana e não afirma compatibilidade real; CLI/daemon e serviços reais não são chamados.
>
> **Pós-condição:** fixtures isoladas verificadas e removidas; infraestrutura e dados reais intocados.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c4|C4]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b06

> [!example]- CT-B07 · Proveniência ausente ou não verificável
>
> ## Cenário
>
> **Descrição:** Proveniência ausente ou não verificável.
>
> **Pré-condições:** Fonte de confiança dublada indisponível, revisão ausente ou evidência obsoleta.
>
> **Dado** Fonte de confiança dublada indisponível, revisão ausente ou evidência obsoleta.
> **Quando** avaliar proveniência do SHA e identidade da imagem
> **Então** o gate mantém no-go sem inventar confiança, sem alegar autenticidade ou compatibilidade real.
>
> **Resultado esperado:** o gate mantém no-go sem inventar confiança, sem alegar autenticidade ou compatibilidade real.
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

> [!example]- CT-B08 · Retorno vinculado ao conjunto correto
>
> ## Cenário
>
> **Descrição:** Retorno vinculado ao conjunto correto.
>
> **Pré-condições:** Relatório sintético de integridade associado a bundle diferente e identidade do serviço dublada divergente.
>
> **Dado** Relatório sintético de integridade associado a bundle diferente e identidade do serviço dublada divergente.
> **Quando** avaliar retorno e health positivo
> **Então** o vínculo incorreto ou identidade divergente impede sucesso apesar do health positivo.
>
> **Resultado esperado:** o vínculo incorreto ou identidade divergente impede sucesso apesar do health positivo.
>
> **Pós-condição:** fixtures conferidas e removidas; infraestrutura e dados reais intactos.
>
> **Critérios cobertos:** [[01 - Bug#^c3|C3]], [[01 - Bug#^c4|C4]]
>
> **Informações do CT**
>
> **Tipo:** regressão<br>
> **Camada:** infra/documentação<br>
> **Automação:** ambos<br>
> **Execução:** planejado

^ct-b08
