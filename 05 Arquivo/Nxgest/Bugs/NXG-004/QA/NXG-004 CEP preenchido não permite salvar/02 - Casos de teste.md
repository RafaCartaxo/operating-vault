---
demanda: "[[01 - Bug|NXG-004]]"
status: planejado
pontos: ""
---
# Casos de teste — NXG-004

> [!info]- Navegação QA/DEV
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Validação QA:** [[03 - Validação dev]]  
> **Demanda pai:** [[05 Arquivo/Nxgest/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/01 - Demanda|MEL-0001 — Cliente CEP]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os cenários vivem nesta nota; a validação registra apenas resultado e evidência.

> [!example]- CT-B01 · Salvar cliente com CEP pessoal válido
>
> **Descrição:** confirma que o CEP válido do endereço pessoal não impede o salvamento.
>
> **Pré-condições:** formulário de cliente aberto; CEP pessoal válido preenchido e consulta concluída.
>
> **Dado** um cliente com CEP pessoal válido e localização aproximada disponível  
> **Quando** salvo o cadastro  
> **Então** o cliente é salvo normalmente.
>
> **Resultado esperado:** o endereço e o CEP permanecem persistidos; a localização aproximada continua identificada como `CEP aprox.`.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c3|C3]]
>
> **Informações do CT**  
> **Tipo:** funcional · **Camada:** UI/API · **Automação:** manual · **Execução:** planejado

^ct-b01

> [!example]- CT-B02 · Salvar cliente com CEP do comércio válido
>
> **Descrição:** confirma que o CEP válido do endereço do comércio não impede o salvamento.
>
> **Pré-condições:** formulário de cliente aberto; CEP do comércio válido preenchido e consulta concluída.
>
> **Dado** um cliente com CEP do comércio válido  
> **Quando** salvo o cadastro  
> **Então** o cliente é salvo normalmente.
>
> **Resultado esperado:** o endereço comercial e o CEP permanecem persistidos; a localização aproximada continua disponível quando retornada.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]], [[01 - Bug#^c3|C3]]
>
> **Informações do CT**  
> **Tipo:** funcional · **Camada:** UI/API · **Automação:** manual · **Execução:** planejado

^ct-b02
