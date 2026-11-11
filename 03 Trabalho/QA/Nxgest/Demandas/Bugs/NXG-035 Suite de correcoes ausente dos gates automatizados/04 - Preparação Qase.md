---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: bug
projeto: nxgest
modulo: ci
qase_projeto: nxgest
qase_suite_id: ""
casos_origem: ""
validacao_origem: ""
---
# Preparação Qase — NXG-035

> **Posição no pacote:** melhoria → `05 - Preparação Qase.md`; bug → `04 - Preparação Qase.md`. O conteúdo deste modelo é o mesmo nos dois casos.

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]<br>
> **Casos de teste (bug):** [[02 - Casos de teste]]<br>
> **Validação (bug):** [[03 - Validação dev]]<br>

Esta nota transforma os CTs refinados do vault em casos da Qase. Não crie CT novo aqui: apenas traduza o caso existente para os campos da API.

## Configuração

- **Projeto Qase:** não configurado
- **Suite Qase:** não configurada
- **Origem:** nota de casos de teste do próprio card (`02` para bug, `03` para melhoria)

## Mapeamento dos campos

| Vault | Qase | Regra |
|---|---|---|
| Título do CT | `title` | manter o título humano do cenário |
| Descrição | `description` | resumir o objetivo do CT |
| Pré-condições | `preconditions` | copiar sem misturar com os passos |
| Dado/Quando/Então | `steps` | separar cada ação do resultado esperado |
| Pós-condição | `postconditions` | registrar somente o estado após o teste |
| Tipo, camada, automação | campos Qase | usar os valores normalizados abaixo |

Valores normalizados: `funcional`/`regressão`; camada `E2E`/`API`/`unit`; automação `manual`/`automatizado`/`ambos`.

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: usar o ID da demanda e o módulo (`NXG-035`, `ci`); não criar uma tag para cada CT, pois o título e o ID do caso já fazem essa identificação.


## Casos preparados

### CT-B01 — CI executa os dois testes

- **Origem:** [[02 - Casos de teste#^ct-b01|CT-B01]].
- **Pré-condições:** Workflow CI representado localmente e runner sintético que registra cada teste executado; guardas verificadas.
- **Ação:** exercitar o gate de CI em fixture.
- **Resultado:** os dois nomes distintos são efetivamente executados e reportados, sem recurso real.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / CI / ambos. Não enviado.

### CT-B02 — CD manual executa os dois testes

- **Origem:** [[02 - Casos de teste#^ct-b02|CT-B02]].
- **Pré-condições:** Caminho workflow_dispatch representado localmente; runner sintético e guardas previamente verificadas.
- **Ação:** exercitar o gate manual em fixture.
- **Resultado:** os dois testes executam e o resultado aparece no gate; não se chama deploy real.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / CI / ambos. Não enviado.

### CT-B03 — Falha de cada teste bloqueia cada gate

- **Origem:** [[02 - Casos de teste#^ct-b03|CT-B03]].
- **Pré-condições:** Os dois testes podem falhar individualmente por injeção em cópia sintética; CI e CD manual dublados.
- **Ação:** injetar cada falha em cada gate.
- **Resultado:** todos os quatro cenários retornam falha não mascarada e nenhum passo dependente de promoção executa.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / CI / ambos. Não enviado.

### CT-B04 — Dublês ausentes ou desviados

- **Origem:** [[02 - Casos de teste#^ct-b04|CT-B04]].
- **Pré-condições:** Guardas de docker, curl, ssh e scp; fixture permite trocar resolução por binário proibido ou remover uma guarda.
- **Ação:** sondar cada comando e subprocesso antes dos testes.
- **Resultado:** guarda ausente, divergente ou falha aborta antes do teste e nenhuma chamada chega ao CLI/daemon ou rede real.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / CI / ambos. Não enviado.

### CT-B05 — Runner sem pressupor ambiente pessoal

- **Origem:** [[02 - Casos de teste#^ct-b05|CT-B05]].
- **Pré-condições:** Fixture sem /home do usuário, sem bwrap ou com namespace de usuário indisponível; Node/auxiliares controlados.
- **Ação:** inicializar runner em cada variante.
- **Resultado:** runner usa requisitos explicitamente providos ou aborta com erro antes de qualquer teste; não infere ambiente GitHub real.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / CI / ambos. Não enviado.

### CT-B06 — Regressão dos gates anteriores

- **Origem:** [[02 - Casos de teste#^ct-b06|CT-B06]].
- **Pré-condições:** CI/CD dublados e testes anteriores representados por sentinelas sintéticas com possibilidade de falha.
- **Ação:** verificar descoberta e executar cada falha em fixture.
- **Resultado:** test:safety, test:deploy e test:backup continuam incluídos, falhas propagam e NO-GO operacional não é removido.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / CI / ambos. Não enviado.

### CT-B07 — Resultados e limitações explícitos

- **Origem:** [[02 - Casos de teste#^ct-b07|CT-B07]].
- **Pré-condições:** Relatório e documentação gerados somente com dados sintéticos; CI externo não foi executado.
- **Ação:** revisar evidências e logs com marcador secreto sintético.
- **Resultado:** nenhum segredo é exposto, execução isolada é identificada e compatibilidade/restore/proveniência reais não são declarados comprovados.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / CI / ambos. Não enviado.

## Checklist de envio

Envio externo fora do escopo.
