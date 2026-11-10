---
demanda: "[[01 - Bug]]"
status: planejado
pontos: 3
---
# Casos de teste — NXG-031

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Fix DEV:** [[03 Trabalho/DEV/Nxgest/Fixes/NXG-031/00 README|Fix DEV]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-031 Transicao segura do deploy e continuidade operacional/03 - Validação dev|Validação QA]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os cenários de reprodução e regressão vivem nesta nota. A validação registra resultado e evidência; não duplica os CTs.

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Bug#^c1|C1]] | [[02 - Casos de teste#^ct-b01|CT-B01]], [[02 - Casos de teste#^ct-b04|CT-B04]] |
| [[01 - Bug#^c2|C2]] | [[02 - Casos de teste#^ct-b02|CT-B02]], [[02 - Casos de teste#^ct-b03|CT-B03]] |
| [[01 - Bug#^c3|C3]] | [[02 - Casos de teste#^ct-b01|CT-B01]], [[02 - Casos de teste#^ct-b04|CT-B04]] |
| [[01 - Bug#^c4|C4]] | [[02 - Casos de teste#^ct-b02|CT-B02]], [[02 - Casos de teste#^ct-b05|CT-B05]] |
| [[01 - Bug#^c5|C5]] | [[02 - Casos de teste#^ct-b06|CT-B06]] |

> [!example]- CT-B01 · Primeira transição legado para infra
>
> ## Cenário
>
> **Descrição:** Primeira transição legado para infra.
>
> **Pré-condições:**
> Checkout isolado com layout e script antigos, alvo com infra e helper.
>
> **Dado** Checkout isolado com layout e script antigos, alvo com infra e helper.
> **Quando** o bootstrap recebe o SHA alvo
> **Então** o script alvo e seu helper executam com Compose novo e env sintético preservado
>
> **Resultado esperado:** o script alvo e seu helper executam com Compose novo e env sintético preservado.
>
> **Pós-condição:** Fixtures isolados preservados para conferência e removidos ao final; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** infra  
> **Automação:** ambos  
> **Execução:** planejado

^ct-b01



> [!example]- CT-B02 · Fetch ou SHA inválido falha antes de build
>
> ## Cenário
>
> **Descrição:** Fetch ou SHA inválido falha antes de build.
>
> **Pré-condições:**
> Repositório isolado e Docker interceptado.
>
> **Dado** Repositório isolado e Docker interceptado.
> **Quando** fetch falha ou ref é inexistente
> **Então** nenhum build/up ocorre e checkout/env permanecem íntegros
>
> **Resultado esperado:** nenhum build/up ocorre e checkout/env permanecem íntegros.
>
> **Pós-condição:** Fixtures isolados preservados para conferência e removidos ao final; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]], [[01 - Bug#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** infra  
> **Automação:** ambos  
> **Execução:** planejado

^ct-b02



> [!example]- CT-B03 · Alterações remotas são preservadas
>
> ## Cenário
>
> **Descrição:** Alterações remotas são preservadas.
>
> **Pré-condições:**
> Checkout fixture com alteração rastreada e arquivo não rastreado conflitante.
>
> **Dado** Checkout fixture com alteração rastreada e arquivo não rastreado conflitante.
> **Quando** o deploy tenta atualizar
> **Então** o fluxo recusa conflito sem descartar trabalho ou revelar valores
>
> **Resultado esperado:** o fluxo recusa conflito sem descartar trabalho ou revelar valores.
>
> **Pós-condição:** Fixtures isolados preservados para conferência e removidos ao final; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** infra  
> **Automação:** ambos  
> **Execução:** planejado

^ct-b03



> [!example]- CT-B04 · Repetição, env com espaços e uso manual
>
> ## Cenário
>
> **Descrição:** Repetição, env com espaços e uso manual.
>
> **Pré-condições:**
> Env sintético incluindo MAIL_FROM_NAME="NX Gest" e segunda execução no SHA alvo.
>
> **Dado** Env sintético incluindo MAIL_FROM_NAME="NX Gest" e segunda execução no SHA alvo.
> **Quando** a entrada manual e a automatizada são executadas
> **Então** ambas usam código alvo, preservam env e não interpretam seus valores como comandos
>
> **Resultado esperado:** ambas usam código alvo, preservam env e não interpretam seus valores como comandos.
>
> **Pós-condição:** Fixtures isolados preservados para conferência e removidos ao final; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c1|C1]], [[01 - Bug#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** infra  
> **Automação:** ambos  
> **Execução:** planejado

^ct-b04



> [!example]- CT-B05 · Gates produção, backup e compartilhamento de checkout
>
> ## Cenário
>
> **Descrição:** Gates produção, backup e compartilhamento de checkout.
>
> **Pré-condições:**
> Workflows/scripts atuais e fixtures sem Docker real.
>
> **Dado** Workflows/scripts atuais e fixtures sem Docker real.
> **Quando** são examinados/exercitados erro de staging, falta de backup e disputa de atualização aplicável
> **Então** produção permanece bloqueada nas falhas e a sequência garante SHA e caminhos corretos sem corrida no checkout
>
> **Resultado esperado:** produção permanece bloqueada nas falhas e a sequência garante SHA e caminhos corretos sem corrida no checkout.
>
> **Pós-condição:** Fixtures isolados preservados para conferência e removidos ao final; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** infra  
> **Automação:** ambos  
> **Execução:** planejado

^ct-b05



> [!example]- CT-B06 · Portabilidade de segredos e documentação de operação
>
> ## Cenário
>
> **Descrição:** Portabilidade de segredos e documentação de operação.
>
> **Pré-condições:**
> Dois homes sintéticos com arquivos e subpasta, sem credenciais reais.
>
> **Dado** Dois homes sintéticos com arquivos e subpasta, sem credenciais reais.
> **Quando** o procedimento documentado transfere os fixtures para outro usuário
> **Então** destino correto, diretórios atravessáveis e arquivos privados; dev não exige credenciais operacionais; Cloudflare tem checklist de confirmação e limites explícitos
>
> **Resultado esperado:** destino correto, diretórios atravessáveis e arquivos privados; dev não exige credenciais operacionais; Cloudflare tem checklist de confirmação e limites explícitos.
>
> **Pós-condição:** Fixtures isolados preservados para conferência e removidos ao final; infraestrutura real intacta.
>
> **Critérios cobertos:** [[01 - Bug#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** infra  
> **Automação:** ambos  
> **Execução:** planejado

^ct-b06


