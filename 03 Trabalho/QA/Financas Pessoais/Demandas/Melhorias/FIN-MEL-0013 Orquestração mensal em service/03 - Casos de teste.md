---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: concluido
pontos: 2
---

# Casos de teste — FIN-MEL-0013

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/<projeto>/Execuções/<ID>/00 README|Execução DEV]]

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

> [!example]- CT-001 · Service orquestra materialização e listagem
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
> **Descrição:** confirma que o handler delega o caso de uso mensal ao service, que coordena as dependências na ordem correta.
>
> **Pré-condições:**
> - Código da FIN-MEL-0013 implementado.
> - Dependências do service substituíveis por doubles/mocks no teste unitário.
>
> **Dado** um mês válido e dependências de recorrências e lançamentos configuradas
> **Quando** o caso de uso mensal é executado
> **Então** a materialização é chamada antes da listagem e o resultado da listagem é devolvido.
>
> **Resultado esperado:** o handler não coordena diretamente os repositórios; o service coordena o fluxo sem alterar o resultado.
>
> **Pós-condição:** a ordem e as responsabilidades ficam cobertas por teste automatizado.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** unit  
> **Automação:** automatizado  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · Contrato HTTP mensal preservado
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o endpoint mensal continua respondendo com o mesmo contrato após a extração do service.
>
> **Pré-condições:** backend em dev; mês válido; lançamentos e/ou recorrências cadastrados.
>
> **Dado** uma requisição `GET /api/lancamentos?mes=AAAA-MM` válida
> **Quando** consulto o mês
> **Então** a API retorna o mesmo status de sucesso, formato de resposta, filtros e totalizadores existentes.
>
> **Resultado esperado:** nenhuma alteração incompatível é observada no contrato público.
>
> **Pós-condição:** dados persistidos permanecem íntegros.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** API  
> **Automação:** ambos  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Recorrência mensal idempotente após refatoração
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que a consulta gera a ocorrência necessária uma única vez e preserva as regras existentes.
>
> **Pré-condições:** regra recorrente ativa com mês inicial válido; banco limpo ou estado conhecido.
>
> **Dado** uma regra recorrente aplicável ao mês consultado
> **Quando** consulto o mesmo mês duas vezes
> **Então** a ocorrência é materializada na primeira consulta e não é duplicada na segunda.
>
> **Resultado esperado:** ativo/início/fim, vínculo de origem, valor e inclusão em fatura mantêm o comportamento anterior.
>
> **Pós-condição:** existe no máximo uma ocorrência por regra e competência.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** API  
> **Automação:** ambos  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Falha de dependência não vira sucesso parcial
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que uma falha na materialização ou na listagem chega ao chamador com tratamento consistente.
>
> **Pré-condições:** dependência do service configurada para retornar erro controlado.
>
> **Dado** que uma dependência do fluxo mensal falha
> **Quando** o endpoint é chamado
> **Então** a API retorna o status/mensagem de erro definidos, sem responder sucesso com dados incompletos.
>
> **Resultado esperado:** o erro é propagado e traduzido uma única vez pela camada HTTP.
>
> **Pós-condição:** não há criação parcial indevida.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Informações do CT**  
> **Tipo:** negativo  
> **Camada:** API  
> **Automação:** ambos  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Documentação e fronteiras arquiteturais sincronizadas
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> **Descrição:** confirma que o fluxo implementado e a documentação apresentam as mesmas responsabilidades.
>
> **Pré-condições:** implementação revisada; documentação do backend e do vault acessível.
>
> **Dado** o fluxo mensal implementado
> **Quando** comparo código, `docs/arquitetura.md`, `docs/fluxos.md` e os diagramas do vault
> **Então** handler, service, módulos e repositórios aparecem na mesma ordem e com responsabilidades compatíveis.
>
> **Resultado esperado:** não há chamada documentada para um componente inexistente nem responsabilidade atribuída à camada errada.
>
> **Pós-condição:** a evolução futura pode usar o fluxo documentado como contrato de colaboração.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> **Informações do CT**  
> **Tipo:** inspeção  
> **Camada:** unit  
> **Automação:** manual  
> **Execução:** planejado

^ct-005
