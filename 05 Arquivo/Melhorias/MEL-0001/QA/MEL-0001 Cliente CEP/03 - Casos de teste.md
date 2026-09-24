---
demanda: "[[01 - Demanda|MEL-0001 Cliente CEP]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: 0
---
# Casos de teste — MEL-0001

> [!info]- Navegação QA/DEV
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** a criar após o plano técnico

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam na demanda; esta nota concentra os cenários executáveis.

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]], [[03 - Casos de teste#^ct-008\|CT-008]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-001\|CT-001]], [[03 - Casos de teste#^ct-008\|CT-008]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-006\|CT-006]], [[03 - Casos de teste#^ct-007\|CT-007]] |
| [[01 - Demanda#^c8\|C8]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c9\|C9]] | [[03 - Casos de teste#^ct-008\|CT-008]] |
| [[01 - Demanda#^c10\|C10]] | [[03 - Casos de teste#^ct-009\|CT-009]] |
| [[01 - Demanda#^c11\|C11]] | [[03 - Casos de teste#^ct-010\|CT-010]] |

---

## Cenários executáveis

> [!example]- CT-001 · Preencher endereço comercial por CEP válido
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
> **Descrição:** confirma o preenchimento automático do endereço comercial.  
>
> **Pré-condições:** formulário aberto e CEP válido disponível.  
>
> **Dado** um endereço comercial com CEP válido  
> **Quando** concluo o preenchimento do CEP  
> **Então** logradouro, bairro, cidade e UF são preenchidos sem alterar número/complemento.  
>
> **Resultado esperado:** dados retornados aparecem corretamente.  
> **Pós-condição:** endereço pode ser salvo.  
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c2|C2]]  
>
> **Informações:** tipo funcional · camada UI/API · automação manual · execução planejado

^ct-001

> [!example]- CT-002 · Salvar cliente sem CEP
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
> **Descrição:** confirma que o CEP é opcional.  
>
> **Pré-condições:** cliente com endereço manual e CEP vazio.  
>
> **Dado** um cliente sem CEP  
> **Quando** salvo o cadastro  
> **Então** o cliente é salvo normalmente.  
>
> **Resultado esperado:** cadastro concluído sem bloqueio.  
> **Pós-condição:** cliente permanece consultável.  
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]  
>
> **Informações:** tipo funcional · camada UI/API · automação manual · execução planejado

^ct-002

> [!example]- CT-003 · Tratar CEP inválido ou serviço indisponível
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
> **Descrição:** confirma mensagem clara sem apagar dados manuais.  
>
> **Pré-condições:** formulário aberto com dados manuais.  
>
> **Dado** um CEP inválido, inexistente ou consulta indisponível  
> **Quando** concluo o preenchimento  
> **Então** vejo mensagem e o cadastro continua disponível.  
>
> **Resultado esperado:** mensagem oferece `Corrigir` ou `Salvar sem CEP`; ao confirmar, o CEP é removido e o restante é salvo.  
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]  
>
> **Informações:** tipo negativo · camada UI/API · automação manual · execução planejado

^ct-003

> [!example]- CT-004 · Persistir CEP nos dois endereços
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
> **Descrição:** confirma persistência na edição e API.  
>
> **Pré-condições:** cliente com CEP pessoal e comercial.  
>
> **Dado** um cliente com os dois CEPs  
> **Quando** salvo, reabro a edição e consulto a API  
> **Então** os CEPs retornam com oito dígitos e aparecem mascarados.  
>
> **Resultado esperado:** valores são preservados.  
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]  
>
> **Informações:** tipo persistência · camada UI/API · automação manual · execução planejado

^ct-004

> [!example]- CT-005 · Identificar e usar localização aproximada
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
> **Descrição:** confirma origem aproximada e prioridade comercial.  
>
> **Pré-condições:** CEP comercial com resultado de geocoding.  
>
> **Dado** um CEP comercial localizado  
> **Quando** a consulta termina e seleciono Navegar  
> **Então** a localização aparece como aproximada e é usada.  
>
> **Resultado esperado:** ao clicar em **Navegar**, o Google Maps é aberto normalmente; a interface identifica a origem como `CEP aprox.`, e não como GPS capturado.  
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]], [[01 - Demanda#^c8|C8]]  
>
> **Informações:** tipo funcional · camada UI/API · automação manual · execução planejado

^ct-005

> [!example]- CT-006 · Invalidar coordenadas ao alterar endereço
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
> **Descrição:** confirma invalidação ao alterar CEP ou texto relevante.  
>
> **Pré-condições:** endereço com localização aproximada.  
>
> **Dado** um endereço localizado  
> **Quando** altero CEP, logradouro, bairro, cidade, UF ou complemento  
> **Então** as coordenadas do bloco são invalidadas.  
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]  
>
> **Informações:** tipo regressão · camada UI/API · automação manual · execução planejado

^ct-006

> [!example]- CT-007 · Preservar coordenadas ao editar somente número
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
> **Descrição:** confirma a exceção para alteração apenas do número.  
>
> **Pré-condições:** endereço com localização aproximada.  
>
> **Dado** um endereço localizado  
> **Quando** altero somente o número  
> **Então** as coordenadas permanecem disponíveis.  
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]  
>
> **Informações:** tipo regressão · camada UI/API · automação manual · execução planejado

^ct-007

> [!example]- CT-008 · Preencher CEP no endereço pessoal recolhido
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
> **Descrição:** confirma comportamento do bloco pessoal recolhido.  
>
> **Pré-condições:** criação ou edição com dados existentes.  
>
> **Dado** o formulário de cliente  
> **Quando** expando o endereço pessoal  
> **Então** os dados são preservados e o CEP funciona como no comércio.  
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c2|C2]], [[01 - Demanda#^c9|C9]]  
>
> **Informações:** tipo funcional · camada UI · automação manual · execução planejado

^ct-008

> [!example]- CT-009 · Preservar captura manual de GPS
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
> **Descrição:** confirma que a captura manual continua disponível.  
>
> **Pré-condições:** endereço sem CEP ou sem resultado de geocoding.  
>
> **Dado** um endereço sem localização derivada  
> **Quando** uso a captura manual  
> **Então** o GPS continua disponível e identificado como manual.  
>
> **Critérios cobertos:** [[01 - Demanda#^c10|C10]]  
>
> **Informações:** tipo regressão · camada UI/API · automação manual · execução planejado

^ct-009

> [!example]- CT-010 · Remover CEP existente na edição
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
> **Descrição:** confirma que um CEP salvo pode ser removido durante a edição.
>
> **Pré-condições:** cliente existente com CEP e localização aproximada derivados do CEP.
>
> **Dado** um cliente com CEP salvo
> **Quando** removo o CEP e salvo a edição
> **Então** o CEP fica vazio e a localização aproximada derivada é removida.
>
> **Resultado esperado:** ao reabrir a edição ou consultar a API, o CEP não retorna mais; um GPS manual independente, se existir, permanece.
>
> **Critérios cobertos:** [[01 - Demanda#^c11|C11]]
>
> **Informações:** tipo regressão · camada UI/API · automação manual · execução planejado

^ct-010
