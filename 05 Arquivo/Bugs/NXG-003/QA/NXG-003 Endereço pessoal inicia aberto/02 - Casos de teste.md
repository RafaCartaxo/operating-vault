---
demanda: "[[01 - Bug|NXG-003]]"
status: planejado
pontos: 0
---
# Casos de teste — NXG-003

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> [!info]- Navegação QA/DEV
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Demanda pai:** [[05 Arquivo/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/01 - Demanda|MEL-0001]]
> **Validação QA:** [[03 - Validação dev]]

> Os cenários vivem nesta nota; a validação registra apenas resultado e evidência.

---

> [!example]- CT-B01 · Criar cliente com endereço pessoal recolhido
>
> **Descrição:** confirma o estado inicial do endereço pessoal na criação.
>
> **Pré-condições:** formulário de novo cliente aberto.
>
> **Dado** um formulário de cliente novo  
> **Quando** a tela termina de carregar  
> **Então** o endereço pessoal inicia recolhido e o endereço do comércio permanece expandido.
>
> **Resultado esperado:** somente o bloco pessoal fica recolhido; nenhum dado é perdido.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c3|C3]]
>
> **Informações do CT**  
> **Tipo:** regressão · **Camada:** UI · **Automação:** manual · **Execução:** planejado

^ct-b01

> [!example]- CT-B02 · Editar cliente com endereço pessoal recolhido
>
> **Descrição:** confirma o estado inicial na edição e a preservação dos dados.
>
> **Pré-condições:** cliente existente com endereço pessoal preenchido.
>
> **Dado** um cliente com endereço pessoal salvo  
> **Quando** abro a edição e expando o bloco pessoal  
> **Então** os dados previamente salvos permanecem disponíveis.
>
> **Resultado esperado:** bloco inicia recolhido e os dados continuam intactos ao expandir.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]]
>
> **Informações do CT**  
> **Tipo:** regressão · **Camada:** UI · **Automação:** manual · **Execução:** planejado

^ct-b02
