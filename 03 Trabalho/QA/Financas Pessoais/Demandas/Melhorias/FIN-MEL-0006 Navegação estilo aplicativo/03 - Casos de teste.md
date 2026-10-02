---
demanda: FIN-MEL-0006
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: 2
---

# Casos de teste — FIN-MEL-0006

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
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-006\|CT-006]] |

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

> [!example]- CT-001 · Exibir navegação inferior no mobile
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
> **Descrição:** confirma que a barra inferior aparece e permite acessar as áreas principais no mobile.
>
> **Pré-condições:**
> - Aplicação aberta em viewport mobile.
>
> **Dado** que estou no mobile  
> **Quando** visualizo a aplicação  
> **Então** vejo a barra inferior com as opções principais.
>
> **Resultado esperado:** a barra é visível, utilizável e não cobre o conteúdo.
>
> **Pós-condição:** uma área permanece selecionada.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E
> **Automação:** manual  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · Alternar entre áreas
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
> **Descrição:** confirma que cada opção exibe somente sua área correspondente.
>
> **Pré-condições:**
> - Barra inferior disponível.
>
> **Dado** que estou em Lançamentos  
> **Quando** seleciono Histórico/Acompanhamento e retorno a Lançamentos  
> **Então** somente a área selecionada é exibida.
>
> **Resultado esperado:** a alternância ocorre sem rolagem de uma página única.
>
> **Pós-condição:** a área escolhida fica ativa.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Identificar área ativa e acessibilidade
>
> **Descrição:** confirma que a opção selecionada é identificada e possui nome acessível.
>
> **Pré-condições:** aplicação aberta em mobile; leitor de tela ou inspeção de atributos disponível.
>
> **Dado** que uma área está selecionada  
> **Quando** observo a barra e navego por teclado  
> **Então** a área ativa é visualmente distinta e cada opção tem nome acessível.
>
> **Resultado esperado:** estado ativo e semântica de navegação são claros.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Informações do CT**  
> **Tipo:** acessibilidade  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Preservar os fluxos de lançamento
>
> **Descrição:** confirma que a navegação não interfere em criar, editar ou excluir lançamentos.
>
> **Pré-condições:** dados de teste disponíveis.
>
> **Dado** que alterno entre as áreas  
> **Quando** crio, edito e excluo um lançamento  
> **Então** cada operação mantém o comportamento já aprovado.
>
> **Resultado esperado:** nenhum dado é perdido e as operações continuam funcionando.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Responsividade mobile e desktop
>
> **Descrição:** confirma que a navegação se adapta aos tamanhos suportados.
>
> **Pré-condições:** viewport mobile e desktop disponíveis.
>
> **Dado** que redimensiono ou acesso a aplicação em dispositivos distintos  
> **Quando** uso a navegação e as telas  
> **Então** nenhum controle ultrapassa o container e o conteúdo permanece utilizável.
>
> **Resultado esperado:** layout legível, sem sobreposição ou rolagem horizontal indevida.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> **Informações do CT**  
> **Tipo:** responsividade  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-005

> [!example]- CT-006 · Estrutura preparada para nova área
>
> **Descrição:** confirma que a navegação usa uma estrutura extensível para futuras áreas.
>
> **Pré-condições:** implementação revisada.
>
> **Dado** que analiso a configuração/componente da navegação  
> **Quando** verifico a inclusão de uma nova opção  
> **Então** ela pode ser adicionada sem reescrever as áreas existentes.
>
> **Resultado esperado:** responsabilidades de navegação e conteúdo permanecem separadas.
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> **Informações do CT**  
> **Tipo:** arquitetura  
> **Camada:** code review  
> **Automação:** manual  
> **Execução:** planejado

^ct-006
