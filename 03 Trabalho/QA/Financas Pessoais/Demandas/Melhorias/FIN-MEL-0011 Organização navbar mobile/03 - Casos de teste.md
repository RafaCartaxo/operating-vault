---
demanda: FIN-MEL-0011
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — FIN-MEL-0011

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

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

> [!example]- CT-001 · Centralizar um único destino
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
> **Descrição:** confirma a centralização do único destino da navbar.
>
> **Pré-condições:**
> - Aplicação disponível em viewport mobile com apenas Acompanhamento.
>
> **Dado** que existe apenas o destino Acompanhamento  
> **Quando** a navbar é exibida  
> **Então** o ícone fica centralizado dentro do container.
>
> **Resultado esperado:** não há alinhamento manual à esquerda ou à direita.
>
> **Pós-condição:** navbar pronta para receber novos destinos.
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

> [!example]- CT-002 · Distribuir múltiplos destinos
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
> **Descrição:** confirma distribuição uniforme entre 2 e 5 destinos.
>
> **Pré-condições:**
> - Navbar configurada com cenários de 2, 3, 4 e 5 destinos.
>
> **Dado** que existem de 2 a 5 destinos  
> **Quando** a navbar é exibida  
> **Então** os ícones são distribuídos uniformemente dentro do container.
>
> **Resultado esperado:** espaçamentos e alinhamentos permanecem equilibrados em todas as quantidades.
>
> **Pós-condição:** layout permanece pronto para alteração da quantidade de destinos.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Ajustar automaticamente ao adicionar ou remover destinos
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que a distribuição não depende de posicionamentos manuais.
>
> **Dado** que a quantidade de destinos é alterada  
> **Quando** um item é adicionado ou removido  
> **Então** o alinhamento e o espaçamento se ajustam automaticamente.
>
> **Resultado esperado:** nenhum item fica preso a uma posição específica.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Informações do CT**  
> **Tipo:** responsividade  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Usar ícone acessível no Acompanhamento
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o destino usa ícone coerente sem perder identificação acessível.
>
> **Dado** que Acompanhamento é exibido na navbar  
> **Quando** observo o item e navego por teclado ou leitor de tela  
> **Então** o texto fixo por extenso não é necessário visualmente, mas o nome acessível está disponível.
>
> **Resultado esperado:** ícone reconhecível, `aria-label`/tooltip adequado e estado ativo identificável.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Informações do CT**  
> **Tipo:** acessibilidade  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Preservar botão flutuante e desktop
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma a separação da ação de Novo lançamento e a ausência de regressão desktop.
>
> **Dado** que visualizo a interface mobile e desktop  
> **Quando** observo a navbar e o botão de Novo lançamento  
> **Então** o `+` permanece fora da navbar, à direita no mobile, e a ação do cabeçalho continua disponível no desktop.
>
> **Resultado esperado:** navegação e ação permanecem visualmente separadas.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-005
