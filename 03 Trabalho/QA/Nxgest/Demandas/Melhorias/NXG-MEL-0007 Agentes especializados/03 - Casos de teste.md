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
> **Execução DEV:** ainda não criada — aguarda novo gate QA

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

> [!example]- CT-001 · AGENTS.md permanece contrato global após a migração
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
> **Descrição:** confirma que `AGENTS.md` continua sendo o contrato global único na raiz, sem duplicar o conteúdo dos contratos de `agents/`.
>
> **Pré-condições:**
> - Lote de execução DEV aplicado no repositório de teste (futuro), com `agents/` já criado.
>
> **Dado** `AGENTS.md` após o lote  
> **Quando** comparo seu conteúdo com os 4 contratos em `agents/`  
> **Então** `AGENTS.md` permanece o contrato global único, sem repetir regras específicas de cada agente, apenas referenciando `agents/README.md`.
>
> **Resultado esperado:** uma única fonte de verdade para regras globais e outra para contratos de agente, sem sobreposição.
>
> **Pós-condição:** nenhuma duplicação entre `AGENTS.md` e `agents/`.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · agents/ canônico com README índice e os 4 contratos
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
> **Descrição:** confirma que `agents/` existe na raiz com `agents/README.md` como índice, listando `docs-sync.md`, `ops-runner.md`, `product-planner.md` e `qa-reviewer.md`.
>
> **Pré-condições:**
> - Lote de execução DEV aplicado no repositório de teste.
>
> **Dado** o diretório `agents/` após o lote  
> **Quando** leio `agents/README.md` e os 4 arquivos de contrato  
> **Então** `agents/README.md` referencia os 4 contratos e cada um existe no diretório, sem depender de `.opencode/`.
>
> **Resultado esperado:** `agents/` é a fonte canônica única de contratos de agente do NX Gest.
>
> **Pós-condição:** os 4 contratos disponíveis fora de qualquer pasta específica de plataforma.
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

> [!example]- CT-003 · Contratos neutros, sem frontmatter nem schema de plataforma
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
> **Descrição:** confirma que `docs-sync.md`, `ops-runner.md`, `product-planner.md` e `qa-reviewer.md` descrevem identidade, responsabilidade, entradas/saídas, regras, limites, protocolo e critérios de conclusão, sem frontmatter nem schema de permissão de nenhuma plataforma.
>
> **Pré-condições:**
> - Os 4 contratos já migrados/criados em `agents/`.
>
> **Dado** o conteúdo de cada um dos 4 contratos  
> **Quando** verifico a presença de frontmatter YAML ou de chaves no formato OpenCode (`mode`, `permission`, `description` estruturado)  
> **Então** nenhum dos 4 contratos usa esse formato — todos descrevem o agente em linguagem neutra, sem metadados de plataforma.
>
> **Resultado esperado:** contratos reutilizáveis por qualquer ferramenta/agente, sem acoplamento ao OpenCode, ao Claude Code ou ao Codex.
>
> **Pós-condição:** nenhum contrato depende de uma plataforma específica para ser interpretado ou aplicado.
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

> [!example]- CT-004 · Inventário de referências ativas e remoção de .opencode sem resíduo
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
> **Descrição:** confirma que o plano cobre a remoção futura de `.opencode/` e que todas as referências estruturais ativas foram inventariadas, sem incluir registros históricos de changelog.
>
> **Pré-condições:**
> - Inventário de referências registrado na demanda/`NXG-028`.
> - `.opencode/` ainda não removido (a remoção é escopo de uma etapa DEV futura).
>
> **Dado** o inventário de referências ativas (`README.md`, `AGENTS.md`, `docs/skills/SKILL-009-documentation-sync.md`, `docs/plans/PLAN-084-organizacao-repositorio.md`, `.dockerignore`)  
> **Quando** comparo com uma nova busca por `.opencode/agents` no repositório  
> **Então** todas as referências ativas constam no inventário e nenhuma delas é um registro histórico de `docs/UPDATES.md` (que permanece intocado).
>
> **Resultado esperado:** plano de remoção completo, sem referência esquecida no momento da implementação.
>
> **Pós-condição:** lista de referências pronta para a implementação DEV atualizar.
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

> [!example]- CT-005 · Documentação ativa planejada para ficar coerente com agents/
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
> **Descrição:** confirma que `README.md`, `AGENTS.md`, `SKILL-009` e `PLAN-084` estão identificados como pendência de atualização na implementação DEV, e que nenhum deles foi editado nesta revisão de QA.
>
> **Pré-condições:**
> - Inventário do CT-004 disponível.
>
> **Dado** o estado atual de `README.md`, `AGENTS.md`, `docs/skills/SKILL-009-documentation-sync.md` e `docs/plans/PLAN-084-organizacao-repositorio.md` no repositório NX Gest  
> **Quando** comparo com o que a demanda registra como pendente de atualização  
> **Então** nenhum desses arquivos foi alterado nesta revisão de QA, e todos constam como pendência explícita da implementação DEV futura.
>
> **Resultado esperado:** nenhuma mudança prematura na documentação do repositório.
>
> **Pós-condição:** documentação do repositório idêntica ao estado anterior a esta revisão.
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

> [!example]- CT-006 · Código, infra, ambiente e trabalho protegido intocados
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
> **Descrição:** confirma que esta revisão do pacote QA não altera `src/`, `frontend/`, `infra/`, `.env`, scripts de deploy nem o trabalho protegido em andamento.
>
> **Pré-condições:**
> - Estado Git inicial do NX Gest registrado antes da revisão.
>
> **Dado** o `git status -sb` do NX Gest antes e depois desta revisão de QA  
> **Quando** comparo os dois estados  
> **Então** nenhum arquivo de código, infraestrutura, ambiente, deploy ou trabalho protegido aparece como alterado.
>
> **Resultado esperado:** nenhuma alteração fora do pacote QA do vault nesta etapa.
>
> **Pós-condição:** repositório NX Gest idêntico ao estado anterior a esta revisão.
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

> [!example]- CT-007 · Pacote QA íntegro e validador oficial aprovado
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
> **Descrição:** confirma que os links internos do pacote resolvem, a estrutura segue literalmente os templates oficiais e o validador oficial aprova o pacote.
>
> **Pré-condições:**
> - Pacote QA revisado completo (`00` a `05`).
>
> **Dado** o pacote `NXG-MEL-0007` revisado  
> **Quando** executo `python3 scripts/validar_pacote_qa.py "03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados"`  
> **Então** o resultado é `PACOTE QA APROVADO NO GATE DE INTEGRIDADE`, sem placeholders e com todos os links resolvendo.
>
> **Resultado esperado:** pacote estruturalmente íntegro antes de qualquer novo `QA_READY_FOR_DEV`.
>
> **Pós-condição:** pacote pronto para uma nova decisão de gate pelo Orquestrador.
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
