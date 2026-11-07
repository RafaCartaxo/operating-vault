---
demanda: "[[01 - Bug]]"
status: "concluido"
pontos: 3
projeto: "nxgest"
epico: "NXG-EPIC-0001"
responsavel: "NX Gest · QA e Coordenação"
---
# Casos de teste — NXG-030

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Fix DEV:** [[05 Arquivo/Nxgest/Bugs/NXG-030/DEV/NXG-030/00 README|Execução DEV]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Bugs/NXG-030/QA/NXG-030 Smoke protege banco e interpreta opcoes/03 - Validação dev|Validação QA]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os cenários de reprodução e regressão vivem nesta nota. A validação registra resultado e evidência; não duplica os CTs.

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Bug#^c1\|C1]] | [[02 - Casos de teste#^ct-b01\|CT-B01]] |
| [[01 - Bug#^c2\|C2]] | [[02 - Casos de teste#^ct-b02\|CT-B02]] |
| [[01 - Bug#^c3\|C3]] | [[02 - Casos de teste#^ct-b03\|CT-B03]] |

> [!example]- CT-B01 · Recusa de alvo inseguro
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[03 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** O smoke recusa alvo alheio ao teste antes de conectar, encerrar sessões ou recriar banco; não usa DATABASE_URL genérica como autorização de destruição.
>
> **Pré-condições:** variáveis sintéticas representando bancos de dev, prod ou nome reservado; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** variáveis sintéticas representando bancos de dev, prod ou nome reservado  
> **Quando** invoco o smoke com esses alvos usando dublês sem acesso a banco real  
> **Então** o comando termina com erro seguro antes de qualquer ação de banco.
>
> **Resultado esperado:** o comando termina com erro seguro antes de qualquer ação de banco.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** unit  
> **Automação:** ambos  
> **Execução:** executado

^ct-b01

> [!example]- CT-B02 · Opcoes sem ambiguidade
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[03 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** --no-recreate funciona como opção isolada ou junto do subcomando; argumentos desconhecidos falham sem mutações.
>
> **Pré-condições:** um harness com conexão e processos simulados; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** um harness com conexão e processos simulados  
> **Quando** invoco as combinações válidas e inválidas de argumentos  
> **Então** a opção impede DROP/CREATE e argumentos desconhecidos não iniciam a pilha.
>
> **Resultado esperado:** a opção impede DROP/CREATE e argumentos desconhecidos não iniciam a pilha.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** unit  
> **Automação:** ambos  
> **Execução:** executado

^ct-b02

> [!example]- CT-B03 · Smoke isolado funcional
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[03 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** O fluxo padrão em banco explicitamente isolado cria schema, seed, executa o smoke e encerra processos próprios mesmo em falha.
>
> **Pré-condições:** instância PostgreSQL exclusiva da validação e portas livres; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** instância PostgreSQL exclusiva da validação e portas livres  
> **Quando** executo smoke com sucesso e simulo falhas do fluxo  
> **Então** o resultado é correto, processos próprios são encerrados e nenhum banco de desenvolvimento é alterado.
>
> **Resultado esperado:** o resultado é correto, processos próprios são encerrados e nenhum banco de desenvolvimento é alterado.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Bug#^c3|C3]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** unit  
> **Automação:** ambos  
> **Execução:** executado

^ct-b03
