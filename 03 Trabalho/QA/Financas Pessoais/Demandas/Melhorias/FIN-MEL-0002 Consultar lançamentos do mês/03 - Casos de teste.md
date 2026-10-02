---
demanda: FIN-MEL-0002
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: 1
---

# Casos de teste — FIN-MEL-0002

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0002/00 README|Execução DEV]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam na demanda; esta nota concentra os cenários executáveis.

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-006\|CT-006]] |

---

> [!example]- CT-001 · Carregar lançamentos do mês atual
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma o carregamento inicial usando o mês atual.
>
> **Pré-condições:**
> - Backend Go iniciado.
> - Existem lançamentos no mês atual.
> - A tela de consulta mensal está disponível.
>
> **Dado** que o usuário abre a consulta mensal  
> **Quando** a tela termina de carregar  
> **Então** a aplicação chama `GET /api/lancamentos?mes=AAAA-MM` para o mês atual e exibe os registros.
>
> **Resultado esperado:** lista carregada sem erro e com o mês atual selecionado.
>
> **Pós-condição:** consulta permanece pronta para troca de mês.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · Exibir dados e valores formatados
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que cada lançamento apresenta os dados principais em formato legível.
>
> **Pré-condições:** mês com pelo menos uma despesa e uma receita.
>
> **Dado** que existem lançamentos no mês  
> **Quando** a lista é exibida  
> **Então** cada item mostra data, descrição, tipo e valor em reais.
>
> **Resultado esperado:** valores são exibidos com máscara brasileira e os tipos são visualmente distinguíveis.
>
> **Pós-condição:** os dados permanecem disponíveis para consulta.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Calcular total de despesas
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que receitas não entram no total de despesas.
>
> **Pré-condições:** mês com despesas e receitas conhecidas.
>
> **Dado** que o mês possui despesas de R$ 10,00 e R$ 20,00 e uma receita  
> **Quando** a tela calcula o resumo  
> **Então** o total de despesas exibido é R$ 30,00.
>
> **Resultado esperado:** total correto, sem somar receitas.
>
> **Pós-condição:** resumo permanece consistente com os itens exibidos.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/unit  
> **Automação:** ambos  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Trocar o mês consultado
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o seletor mensal permite escolher outro mês sem digitação manual e atualiza a lista, inclusive após salvar um lançamento com data retroativa.
>
> **Pré-condições:** existem dados diferentes em dois meses.
>
> **Dado** que o usuário está consultando um mês  
> **Quando** clica no botão do mês e seleciona outro mês no painel mensal  
> **Então** a aplicação consulta o novo `AAAA-MM` e substitui os resultados. Se o lançamento recém-salvo tiver data em outro mês, esse mês passa a ser selecionado automaticamente; o botão “Voltar para o mês atual” retorna ao período corrente.
>
> **Resultado esperado:** lista, total e mês exibido correspondem ao novo período.
>
> **Pós-condição:** a consulta fica no mês selecionado.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Exibir vazio e tratar erro
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que vazio e erro são estados distintos e compreensíveis.
>
> **Pré-condições:**
> - Testar um mês sem dados.
> - Simular uma resposta de erro da API.
>
> **Dado** que a API retorna lista vazia ou erro  
> **Quando** a consulta termina  
> **Então** a tela mostra o estado correspondente e oferece nova tentativa quando houver erro.
>
> **Resultado esperado:** usuário entende se não existem registros ou se a consulta falhou.
>
> **Pós-condição:** após falha, o usuário pode tentar novamente sem recarregar a aplicação.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** resiliência  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-005

> [!example]- CT-006 · Usar a consulta em celular e desktop
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que a lista e o seletor permanecem utilizáveis em diferentes larguras.
>
> **Pré-condições:** frontend disponível em viewport móvel e desktop.
>
> **Dado** que o usuário abre a consulta em celular ou desktop  
> **Quando** navega pela lista e troca o mês  
> **Então** nenhum conteúdo essencial fica cortado ou inacessível.
>
> **Resultado esperado:** consulta legível, navegável e sem rolagem horizontal indevida.
>
> **Pós-condição:** o fluxo permanece utilizável nos dois contextos.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** usabilidade  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-006
