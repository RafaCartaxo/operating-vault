---
demanda: FIN-MEL-0009
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — FIN-MEL-0009

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** será criada após aprovação QA.

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
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-007\|CT-007]] |
| [[01 - Demanda#^c8\|C8]] | [[03 - Casos de teste#^ct-008\|CT-008]] |

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

> [!example]- CT-001 · Acompanhamento como tela principal
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
> **Descrição:** confirma que o Acompanhamento é a área principal após acessar a aplicação.
>
> **Pré-condições:**
> - Aplicação disponível no ambiente de teste.
>
> **Dado** que acesso a aplicação  
> **Quando** a interface carrega  
> **Então** o Acompanhamento é exibido sem exigir uma página exclusiva de lançamento.
>
> **Resultado esperado:** o usuário inicia no Acompanhamento e localiza a ação de adicionar.
>
> **Pós-condição:** Acompanhamento permanece disponível para consulta.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · Abrir novo lançamento em modal
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
> **Descrição:** confirma a abertura do formulário de lançamento em modal/container.
>
> **Pré-condições:**
> - Usuário está no Acompanhamento.
>
> **Dado** que estou no Acompanhamento  
> **Quando** aciono o botão de adicionar  
> **Então** o formulário de lançamento abre sobre a tela atual.
>
> **Resultado esperado:** o modal é visível, possui fechamento e exibe os campos do lançamento.
>
> **Pós-condição:** modal aberto e pronto para preenchimento.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Modal utilizável no mobile
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o modal permanece utilizável em viewport mobile.
>
> **Pré-condições:**
> - Modal de lançamento aberto em celular.
>
> **Dado** que o modal está aberto  
> **Quando** interajo com campos, teclado, rolagem e data  
> **Então** o conteúdo permanece dentro da viewport e utilizável.
>
> **Resultado esperado:** nenhum campo ou botão fica inacessível ou cortado.
>
> **Pós-condição:** modal permanece consistente até ser fechado.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Informações do CT**  
> **Tipo:** funcional  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Preservar formulário e validações
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que campos, máscara de valor, validações e parcelamento continuam funcionando.
>
> **Dado** que abro um novo lançamento pelo modal  
> **Quando** preencho os campos obrigatórios e parcelas, quando aplicável  
> **Então** as regras existentes são aplicadas.
>
> **Resultado esperado:** entradas inválidas são rejeitadas e entradas válidas seguem para salvamento.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Salvar e atualizar acompanhamento
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma o salvamento e a atualização imediata da lista.
>
> **Dado** que preencho um lançamento válido  
> **Quando** confirmo o salvamento  
> **Então** o registro é salvo e o Acompanhamento é atualizado sem recarregamento manual.
>
> **Resultado esperado:** o modal encerra somente após sucesso e a lista reflete o novo registro.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> **Informações do CT**  
> **Tipo:** integração  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-005

> [!example]- CT-006 · Respeitar filtro mensal
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que datas fora do período não aparecem indevidamente.
>
> **Dado** que o Acompanhamento está filtrado para um mês  
> **Quando** salvo um lançamento com data de outro mês  
> **Então** ele é salvo, mas não aparece na listagem do mês filtrado.
>
> **Resultado esperado:** o filtro continua aplicado e o registro aparece ao consultar o mês correto.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> **Informações do CT**  
> **Tipo:** funcional  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-006

> [!example]- CT-007 · Impedir envio duplicado
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o salvamento em andamento impede múltiplos envios.
>
> **Dado** que um lançamento está sendo salvo  
> **Quando** tento confirmar novamente antes da resposta  
> **Então** o segundo envio é impedido e somente um registro é criado.
>
> **Resultado esperado:** o modal permanece em processamento até a resposta da API.
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> **Informações do CT**  
> **Tipo:** validação  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-007

> [!example]- CT-008 · Tratar erro e preservar desktop
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma feedback de erro e ausência de regressão no desktop.
>
> **Dado** que a API retorna erro durante o salvamento  
> **Quando** a operação termina  
> **Então** há feedback, o modal não indica sucesso falso e o desktop continua utilizável.
>
> **Resultado esperado:** o modal permanece aberto para correção ou nova tentativa.
>
> **Critérios cobertos:** [[01 - Demanda#^c8|C8]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-008
