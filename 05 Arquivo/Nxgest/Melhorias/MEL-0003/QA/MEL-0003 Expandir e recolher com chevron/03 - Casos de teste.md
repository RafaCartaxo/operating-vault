---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: concluido
pontos: ""
---

# Casos de teste — MEL-0003

> [!info]- Navegação QA
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Melhorias/MEL-0003/DEV/MEL-0003/00 README|Execução DEV]]

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

> [!example]- CT-001 · Chevron indica seção recolhida e expandida
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
> **Descrição:** confirma que o chevron comunica corretamente os estados recolhido e expandido.
>
> **Pré-condições:**
> - Usuário está na tela de cadastro ou edição de cliente.
> - Existe uma seção expansível disponível.
>
> **Dado** que a seção está recolhida  
> **Quando** observo o controle e clico nele  
> **Então** vejo o chevron à direita antes do clique e para baixo depois, com a seção expandida.
>
> **Resultado esperado:** o indicador acompanha o estado da seção sem alterar o conteúdo.
>
> **Pós-condição:** a seção permanece expandida até novo clique.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c2|C2]], [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · Chevron mantém acessibilidade em criar e editar
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
> **Descrição:** confirma que o controle continua acessível e funcional nos fluxos de criar e editar cliente.
>
> **Pré-condições:**
> - Usuário pode acessar criar e editar cliente.
> - A melhoria está disponível no ambiente de teste.
>
> **Dado** que uma seção está recolhida  
> **Quando** aciono o controle por teclado em criar e editar  
> **Então** a seção alterna de estado e o nome acessível do controle permanece disponível.
>
> **Resultado esperado:** expandir e recolher funciona nos dois fluxos, sem perda de dados ou acessibilidade.
>
> **Pós-condição:** os dados do cliente permanecem íntegros.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-002
