---
demanda: ""
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — <ID>

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[04 Trabalho DEV/Execuções/<ID>/00 README|Execução DEV]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam na demanda; esta nota concentra os cenários executáveis.

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-001\|CT-001]] |

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

> [!example]- CT-001 · Título claro do cenário
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
> **Descrição:** explique em uma frase o que este caso confirma.
>
> **Pré-condições:**
> - Informe o que precisa estar preparado antes do teste.
> - Inclua usuário, dados ou estado necessário.
>
> **Dado** que ...
> **Quando** ...
> **Então** ...
>
> **Resultado esperado:** descreva o comportamento observado em linguagem direta.
>
> **Pós-condição:** registre como o sistema deve ficar depois do teste.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · Reabrir o fluxo sem perder os dados preenchidos
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
> **Descrição:** confirma que a melhoria mantém os dados ao sair e retornar ao fluxo.
>
> **Pré-condições:**
> - O fluxo foi iniciado com dados válidos.
> - A melhoria está disponível no ambiente de teste.
>
> **Dado** um registro com os dados da melhoria preenchidos  
> **Quando** avanço, volto ou reabro o fluxo  
> **Então** os dados continuam disponíveis e o comportamento permanece consistente.
>
> **Resultado esperado:** o fluxo pode ser retomado sem perda de informação.
>
> **Pós-condição:** registro permanece íntegro e pronto para conclusão.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-002
