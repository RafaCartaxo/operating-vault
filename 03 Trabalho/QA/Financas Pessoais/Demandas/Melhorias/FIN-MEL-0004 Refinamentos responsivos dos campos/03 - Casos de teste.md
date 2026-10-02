---
demanda: FIN-MEL-0004
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: 1
---

# Casos de teste — FIN-MEL-0004

> [!info]- Navegação QA
> **README:** [[00 README]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano:** [[02 - Plano de teste]]  
> **Casos:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0004/00 README|Execução DEV]]

> [!settings]- Controle dos casos de teste
> **Status:** planejado

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1|C1]] | [[03 - Casos de teste#^ct-001|CT-001]] |
| [[01 - Demanda#^c2|C2]] | [[03 - Casos de teste#^ct-002|CT-002]] |
| [[01 - Demanda#^c3|C3]] | [[03 - Casos de teste#^ct-003|CT-003]] |
| [[01 - Demanda#^c4|C4]] | [[03 - Casos de teste#^ct-004|CT-004]] |
| [[01 - Demanda#^c5|C5]] | [[03 - Casos de teste#^ct-005|CT-005]] |
| [[01 - Demanda#^c6|C6]] | [[03 - Casos de teste#^ct-006|CT-006]] |
| [[01 - Demanda#^c7|C7]] | [[03 - Casos de teste#^ct-007|CT-007]] |

> [!example]- CT-001 · Data no iPhone
>
> **Dado** que estou no formulário em iPhone Chrome  
> **Quando** visualizo o campo de data  
> **Então** ele cabe no container e abre o seletor nativo ao tocar.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> **Informações do CT:** funcional · UI/E2E · manual · planejado
>
> ^ct-001

> [!example]- CT-002 · Data no Android
>
> **Dado** que estou no formulário em Android Chrome  
> **Quando** visualizo o campo de data  
> **Então** ele cabe no container e abre o seletor nativo ao tocar.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Informações do CT:** funcional · UI/E2E · manual · planejado
>
> ^ct-002

> [!example]- CT-003 · Alinhamento do reset mensal
>
> **Dado** que estou na consulta mensal em viewport mobile  
> **Quando** visualizo o mês e o botão de reset  
> **Então** o reset fica alinhado verticalmente ao seletor.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Informações do CT:** usabilidade · UI/E2E · manual · planejado
>
> ^ct-003

> [!example]- CT-004 · Primeiro dígito monetário
>
> **Dado** que o valor está vazio  
> **Quando** digito o primeiro número  
> **Então** ele permanece no cursor esperado e a máscara não reposiciona a edição.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Informações do CT:** usabilidade · UI/unit · ambos · planejado
>
> ^ct-004

> [!example]- CT-005 · Estado inicial do valor
>
> **Dado** que o formulário é aberto  
> **Quando** visualizo o valor sem digitar  
> **Então** o campo exibe R$ 0,00 sem considerar zero como valor válido enviado.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> **Informações do CT:** funcional · UI/E2E · manual · planejado
>
> ^ct-005

> [!example]- CT-006 · Regressão desktop
>
> **Dado** que acesso a aplicação em desktop  
> **Quando** uso data, filtro e valor  
> **Então** os campos permanecem alinhados e funcionais.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> **Informações do CT:** regressão · UI/E2E · manual · planejado
>
> ^ct-006

> [!example]- CT-007 · Impedir zoom automático nos campos
>
> **Dado** que estou no iPhone Chrome  
> **Quando** toco nos campos de texto, valor ou data  
> **Então** a página não aplica zoom automático e mantém o enquadramento.
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> **Informações do CT:** usabilidade · UI/E2E · manual · planejado

^ct-007
