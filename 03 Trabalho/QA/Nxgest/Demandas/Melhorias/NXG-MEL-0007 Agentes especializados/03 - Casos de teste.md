---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: 6
---

# Casos de teste — NXG-MEL-0007

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** ainda não criada — aguarda gate QA

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
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-006\|CT-006]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-007\|CT-007]] |

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

> [!example]- CT-001 · product-planner.md criado no padrão correto
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
> **Descrição:** confirma que `.opencode/agents/product-planner.md` existe com `description`, `mode: subagent` e `permission` escopada, no mesmo formato estrutural dos agentes existentes.
>
> **Pré-condições:**
> - Lote de execução DEV aplicado no repositório de teste.
>
> **Dado** `.opencode/agents/product-planner.md` após o lote  
> **Quando** comparo seu frontmatter e estrutura (Contexto/Tarefas suportadas/Regras) com `docs-sync.md` e `ops-runner.md`  
> **Então** o arquivo segue o mesmo padrão, com `description`, `mode: subagent` e `permission` preenchidos.
>
> **Resultado esperado:** agente de produto formalizado e consistente com o padrão do projeto.
>
> **Pós-condição:** novo agente disponível em `.opencode/agents/`.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · qa-reviewer.md criado no padrão correto
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
> **Descrição:** confirma que `.opencode/agents/qa-reviewer.md` existe com `description`, `mode: subagent` e `permission` somente leitura.
>
> **Pré-condições:**
> - Lote de execução DEV aplicado no repositório de teste.
>
> **Dado** `.opencode/agents/qa-reviewer.md` após o lote  
> **Quando** comparo seu frontmatter e estrutura com o padrão existente  
> **Então** o arquivo segue o mesmo padrão, com `edit: deny` e `write: deny`.
>
> **Resultado esperado:** agente de QA formalizado, somente leitura.
>
> **Pós-condição:** novo agente disponível em `.opencode/agents/`.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Permissões escopadas corretamente
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
> **Descrição:** confirma que nenhum dos 2 agentes tem permissão mais ampla do que o necessário para seu propósito.
>
> **Pré-condições:**
> - Os 2 agentes já criados.
>
> **Dado** o bloco `permission` de `product-planner.md` e `qa-reviewer.md`  
> **Quando** comparo com o propósito declarado de cada um (planejamento vs. revisão)  
> **Então** `product-planner` tem escrita restrita a `docs/plans/**` e `qa-reviewer` não tem `edit`/`write` em nenhum caminho.
>
> **Resultado esperado:** permissões mínimas necessárias, sem excesso.
>
> **Pós-condição:** nenhum agente com acesso de escrita amplo ou irrestrito.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Nenhuma duplicação de AGENTS.md
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
> **Descrição:** confirma que nenhum dos 2 agentes repete o contexto geral do projeto (stack, produção, comandos) já descrito em `AGENTS.md`.
>
> **Pré-condições:**
> - Os 2 agentes já criados; `AGENTS.md` revisado.
>
> **Dado** o conteúdo de `product-planner.md` e `qa-reviewer.md`  
> **Quando** comparo com as seções de `AGENTS.md` (projeto, produção, comandos)  
> **Então** nenhum dos 2 agentes duplica esse conteúdo — cada um só documenta seu próprio escopo.
>
> **Resultado esperado:** uma única fonte de verdade por tipo de informação, como já praticado por `docs-sync.md`/`ops-runner.md`.
>
> **Pós-condição:** nenhuma divergência entre `AGENTS.md` e os novos agentes.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · AGENTS.md coerente com os novos agentes
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
> **Descrição:** confirma que `AGENTS.md` continua correto após o lote, com ou sem edição.
>
> **Pré-condições:**
> - Decisão tomada na execução DEV sobre editar ou não `AGENTS.md`.
>
> **Dado** `AGENTS.md` após o lote  
> **Quando** leio a seção "Agentes do projeto"  
> **Então** a referência a `.opencode/agents/` continua válida e não detalha regras internas dos agentes específicos.
>
> **Resultado esperado:** `AGENTS.md` permanece o contrato global único, sem redundância.
>
> **Pós-condição:** nenhuma contradição entre `AGENTS.md` e os agentes específicos.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** planejado

^ct-005

> [!example]- CT-006 · Código, infra e ambiente intocados
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
> **Descrição:** confirma que o lote não altera `src/`, `frontend/`, `infra/`, `.env` ou scripts de deploy.
>
> **Pré-condições:**
> - Estado Git inicial registrado.
>
> **Dado** o diff do NXG-MEL-0007  
> **Quando** reviso os arquivos alterados  
> **Então** somente `.opencode/agents/{product-planner,qa-reviewer}.md` e, no máximo, `AGENTS.md` aparecem no escopo.
>
> **Resultado esperado:** nenhuma alteração fora da documentação/contratos de agente aprovados.
>
> **Pós-condição:** `infra/`, código e ambiente permanecem exatamente como estavam após o `NXG-MEL-0006`.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** planejado

^ct-006

> [!example]- CT-007 · Links do pacote resolvem e repositório intacto nesta etapa de QA
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
> **Descrição:** confirma que os links internos do pacote QA resolvem e que a criação deste pacote não alterou o repositório NX Gest.
>
> **Pré-condições:**
> - Nenhuma execução DEV foi aberta para este lote.
>
> **Dado** o pacote QA `NXG-MEL-0007` e o repositório NX Gest no momento de sua criação  
> **Quando** executo `python3 scripts/validar_pacote_qa.py` e `git status -sb` no NX Gest  
> **Então** o pacote é aprovado no gate de integridade e o repositório está idêntico ao estado protegido anterior.
>
> **Resultado esperado:** pacote íntegro, repositório intacto até a execução DEV ser autorizada.
>
> **Pós-condição:** nenhuma alteração prematura no NX Gest.
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** automatizado  
> **Execução:** planejado

^ct-007
