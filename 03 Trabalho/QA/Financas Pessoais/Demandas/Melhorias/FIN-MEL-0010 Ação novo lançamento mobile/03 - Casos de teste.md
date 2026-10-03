---
demanda: FIN-MEL-0010
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: concluido
pontos: ""
---

# Casos de teste — FIN-MEL-0010

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

> [!example]- CT-001 · Separar navegação e ação
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
> **Descrição:** confirma que a barra inferior mobile não trata Novo lançamento como uma área equivalente.
>
> **Pré-condições:**
> - Aplicação disponível em viewport mobile.
>
> **Dado** que estou no Acompanhamento em um celular  
> **Quando** visualizo a barra inferior  
> **Então** ela apresenta somente áreas de navegação, sem Novo lançamento como item equivalente.
>
> **Resultado esperado:** Histórico/Acompanhamento mantém o papel de navegação e a ação de novo lançamento fica separada visualmente.
>
> **Pós-condição:** barra inferior permanece disponível para futuras áreas.
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

> [!example]- CT-002 · Exibir ação destacada de novo lançamento
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
> **Descrição:** confirma que a ação principal é localizável e acessível.
>
> **Pré-condições:**
> - Usuário está no Acompanhamento mobile.
>
> **Dado** que visualizo a tela em diferentes larguras mobile  
> **Quando** observo a interface  
> **Então** existe um botão destacado de Novo lançamento, com área de toque adequada.
>
> **Resultado esperado:** o botão é facilmente localizado e não depende da barra de navegação para ser encontrado.
>
> **Pós-condição:** ação permanece pronta para abrir o modal.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Abrir modal existente
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o botão reutiliza o modal de lançamento já existente.
>
> **Pré-condições:**
> - A ação de Novo lançamento está visível.
>
> **Dado** que aciono o botão de Novo lançamento  
> **Quando** a ação é processada  
> **Então** o modal existente é aberto com seus campos e comportamento preservados.
>
> **Resultado esperado:** o formulário abre sem navegação para uma nova página e sem duplicar componentes.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Informações do CT**  
> **Tipo:** integração  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Respeitar safe area e não sobrepor conteúdo
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma o posicionamento seguro do botão em diferentes dimensões mobile.
>
> **Pré-condições:**
> - Acompanhamento com filtros, resumo e lançamentos visíveis.
>
> **Dado** que visualizo a tela em larguras mobile e com safe area inferior  
> **Quando** rolo e interajo com filtros, cards e ações  
> **Então** o botão não cobre conteúdo nem impede as demais ações.
>
> **Resultado esperado:** botão permanece acessível, contido na viewport e separado da barra inferior.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Informações do CT**  
> **Tipo:** responsividade  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Preservar experiência desktop
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o ajuste exclusivo da navegação mobile não quebra o desktop.
>
> **Dado** que acesso a aplicação em viewport desktop  
> **Quando** visualizo o cabeçalho, a ação de novo lançamento e o Acompanhamento  
> **Então** os controles permanecem visíveis e utilizáveis.
>
> **Resultado esperado:** a ação do cabeçalho continua abrindo o mesmo modal e a navegação desktop permanece coerente.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-005
