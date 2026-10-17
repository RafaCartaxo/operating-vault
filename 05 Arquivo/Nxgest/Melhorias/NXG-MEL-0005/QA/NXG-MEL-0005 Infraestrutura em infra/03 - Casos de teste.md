---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: 10
---

# Casos de teste — NXG-MEL-0005

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

> [!example]- CT-001 · Arquivos de infraestrutura agrupados em infra/
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
> **Descrição:** confirma que Dockerfile, Caddyfile e os 3 docker-compose existem em `infra/` e não existem mais na raiz.
>
> **Pré-condições:**
> - Lote de execução DEV aplicado no repositório NX Gest (ambiente de teste).
>
> **Dado** a raiz e a pasta `infra/` do repositório após o lote  
> **Quando** listo os dois diretórios  
> **Então** os 5 arquivos (`Dockerfile`, `Caddyfile`, `docker-compose.yml`, `docker-compose.staging.yml`, `docker-compose.prod.yml`) estão em `infra/` e nenhuma cópia permanece na raiz.
>
> **Resultado esperado:** estrutura movida sem duplicação.
>
> **Pós-condição:** raiz do repositório sem os 5 arquivos de infraestrutura.
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

> [!example]- CT-002 · Docker compose válido nos novos caminhos
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
> **Descrição:** confirma que o volume do Caddyfile e o contexto de build do Dockerfile, referenciados pelos 3 docker-compose, resolvem corretamente a partir de `infra/`.
>
> **Pré-condições:**
> - Os 3 docker-compose já estão em `infra/`.
>
> **Dado** os 3 arquivos `infra/docker-compose.{yml,staging.yml,prod.yml}`  
> **Quando** executo `docker compose -f infra/docker-compose.yml config`, `-f infra/docker-compose.staging.yml config` e `-f infra/docker-compose.prod.yml config`  
> **Então** os 3 comandos validam sem erro de caminho.
>
> **Resultado esperado:** nenhum erro de caminho relativo (volume do Caddyfile, contexto de build).
>
> **Pós-condição:** configuração Docker válida nos 3 ambientes.
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

> [!example]- CT-003 · Scripts de deploy apontam para infra/
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
> **Descrição:** confirma que `scripts/deploy.sh` e `scripts/deploy-staging.sh` referenciam os docker-compose em `infra/`.
>
> **Pré-condições:**
> - Scripts atualizados pelo lote.
>
> **Dado** `scripts/deploy.sh` e `scripts/deploy-staging.sh` após o lote  
> **Quando** leio as linhas que chamam `docker compose -f`  
> **Então** ambas apontam para `infra/docker-compose.prod.yml` e `infra/docker-compose.staging.yml`, respectivamente.
>
> **Resultado esperado:** nenhum script aponta para o caminho antigo (raiz).
>
> **Pós-condição:** scripts prontos para uso real, sem deploy executado nesta validação.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Documentação operacional sem caminho desatualizado
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
> **Descrição:** confirma que `.opencode/agents/ops-runner.md` e `docs/engineering/06-PRODUCAO.md` refletem os novos caminhos dos comandos `docker compose`.
>
> **Pré-condições:**
> - Documentos atualizados pelo lote.
>
> **Dado** os 2 documentos após o lote  
> **Quando** busco por `docker-compose.prod.yml` e `docker-compose.staging.yml` sem o prefixo `infra/`  
> **Então** nenhuma ocorrência desatualizada é encontrada.
>
> **Resultado esperado:** documentação coerente com a nova estrutura.
>
> **Pós-condição:** nenhuma instrução operacional desatualizada.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** automatizado  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Nomes reais de infraestrutura preservados
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
> **Descrição:** confirma que nomes de volumes, rede e containers permanecem idênticos aos de produção/staging.
>
> **Pré-condições:**
> - Os 3 docker-compose já estão em `infra/`.
>
> **Dado** os 3 docker-compose em `infra/` após o lote  
> **Quando** comparo os nomes de volumes (`nxgestao_data`, `nxgestao_pgdata`, `nxgestao_staging_data`, `nxgestao_staging_pgdata`), rede (`nxgestao_net`) e containers (`nxgest-postgres`, `nxgest-pg-dev`, `staging-app`, `staging-pg`) com os nomes atuais em produção  
> **Então** todos os nomes são idênticos.
>
> **Resultado esperado:** nenhuma migração de volume necessária.
>
> **Pós-condição:** infraestrutura real de staging/produção intacta.
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

> [!example]- CT-006 · Exemplos de ambiente continuam na raiz
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
> **Descrição:** confirma que os 3 arquivos de exemplo de ambiente continuam na raiz do repositório, não em `infra/env/`.
>
> **Pré-condições:**
> - Lote aplicado no repositório de teste.
>
> **Dado** a raiz do repositório após o lote  
> **Quando** listo `.env.example`, `.env.production.example` e `.env.staging.example`  
> **Então** os 3 arquivos estão na raiz.
>
> **Resultado esperado:** `cp .env.example .env` continua funcionando sem mudança de instrução.
>
> **Pós-condição:** nenhum arquivo de ambiente movido.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** manual  
> **Automação:** manual  
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
