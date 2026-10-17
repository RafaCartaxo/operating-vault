---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: 6
---

# Casos de teste — NXG-MEL-0006

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

> [!example]- CT-001 · Script npm sobe o Postgres de desenvolvimento
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
> **Descrição:** confirma que um script npm sobe o Postgres de desenvolvimento a partir de `infra/docker-compose.yml`, sem o desenvolvedor digitar o caminho.
>
> **Pré-condições:**
> - `NXG-MEL-0005` aplicado (compose já em `infra/`).
>
> **Dado** o `package.json` após o lote  
> **Quando** executo `npm run db:up` (ou o nome final do script)  
> **Então** o Postgres de desenvolvimento sobe normalmente, equivalente a `docker compose -f infra/docker-compose.yml up -d postgres`.
>
> **Resultado esperado:** banco de dev disponível sem comando manual com `-f`.
>
> **Pós-condição:** container de Postgres de dev saudável.
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

> [!example]- CT-002 · README usa o novo comando
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
> **Descrição:** confirma que a seção "Instalação Rápida" do README usa o novo comando npm, não mais `docker compose up -d postgres` direto.
>
> **Pré-condições:**
> - README atualizado pelo lote.
>
> **Dado** a seção "Instalação Rápida" do `README.md`  
> **Quando** leio o passo de subir o banco  
> **Então** o comando documentado é o script npm, não o `docker compose` direto sem `-f`.
>
> **Resultado esperado:** instrução coerente com a nova localização do compose.
>
> **Pós-condição:** README sem instrução quebrada.
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

> [!example]- CT-003 · Setup de nova máquina usa o novo comando
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
> **Descrição:** confirma que o Passo 4 de `08-SETUP-NOVA-MAQUINA.md` usa o mesmo comando novo do README.
>
> **Pré-condições:**
> - Documento atualizado pelo lote.
>
> **Dado** o Passo 4 de `docs/engineering/08-SETUP-NOVA-MAQUINA.md`  
> **Quando** leio a instrução de subir o PostgreSQL local  
> **Então** o comando é idêntico ao documentado no README.
>
> **Resultado esperado:** documentação de onboarding consistente entre os dois arquivos.
>
> **Pós-condição:** nenhuma divergência entre README e guia de setup.
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

> [!example]- CT-004 · Configuração de ambiente permanece simples
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
> **Descrição:** confirma que `cp .env.example .env` continua sendo o único passo de configuração de ambiente documentado.
>
> **Pré-condições:**
> - README e guia de setup revisados.
>
> **Dado** a documentação de configuração de ambiente após o lote  
> **Quando** comparo com a instrução anterior ao lote  
> **Então** `cp .env.example .env` permanece idêntico, sem passo adicional.
>
> **Resultado esperado:** nenhuma mudança na experiência de configuração de ambiente.
>
> **Pós-condição:** `.env.example` continua na raiz, sem alteração.
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

> [!example]- CT-005 · Clone limpo completa sem passo manual extra
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
> **Descrição:** confirma que um clone novo, seguindo o passo a passo atualizado, completa a instalação sem precisar de nenhum passo não documentado.
>
> **Pré-condições:**
> - `NXG-MEL-0005` e `NXG-MEL-0006` aplicados no ambiente de teste.
>
> **Dado** uma pasta vazia  
> **Quando** sigo o passo a passo atualizado do `08-SETUP-NOVA-MAQUINA.md` (clone, `npm install`, `cp .env.example .env`, novo comando de banco, `npm run dev`)  
> **Então** a aplicação sobe normalmente, sem passo manual além do documentado.
>
> **Resultado esperado:** clone limpo funciona de ponta a ponta.
>
> **Pós-condição:** ambiente de desenvolvimento local operacional.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** planejado

^ct-005

> [!example]- CT-006 · Staging e produção intocados
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
> **Descrição:** confirma que `scripts/deploy.sh`, `scripts/deploy-staging.sh` e `.opencode/agents/ops-runner.md` não foram alterados por este lote.
>
> **Pré-condições:**
> - Lote de onboarding aplicado no ambiente de teste.
>
> **Dado** os 3 arquivos citados após o lote  
> **Quando** comparo com o estado anterior ao lote  
> **Então** nenhum deles foi modificado (esses já foram tratados em `NXG-MEL-0005`).
>
> **Resultado esperado:** nenhuma sobreposição de escopo entre os lotes.
>
> **Pós-condição:** scripts de deploy e documentação operacional inalterados.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** automatizado  
> **Execução:** planejado

^ct-006

> [!example]- CT-007 · Repositório NX Gest intacto nesta etapa de QA
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
> **Descrição:** confirma que a criação deste pacote QA não alterou o repositório NX Gest nem expôs segredos.
>
> **Pré-condições:**
> - Nenhuma execução DEV foi aberta para este lote.
>
> **Dado** o repositório NX Gest no momento da criação deste pacote QA  
> **Quando** executo `git status -sb`  
> **Então** o estado é idêntico ao estado protegido anterior (nenhuma mudança).
>
> **Resultado esperado:** repositório intacto até a execução DEV ser autorizada.
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
