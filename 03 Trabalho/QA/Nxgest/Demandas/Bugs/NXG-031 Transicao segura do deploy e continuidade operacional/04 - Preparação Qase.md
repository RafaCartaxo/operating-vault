---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: bug
projeto: nxgest
modulo: infra
qase_projeto: nxgest
qase_suite_id: ""
casos_origem: ""
validacao_origem: ""
---
# Preparação Qase — NXG-031

> **Posição no pacote:** melhoria → `05 - Preparação Qase.md`; bug → `04 - Preparação Qase.md`. O conteúdo deste modelo é o mesmo nos dois casos.

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Casos de teste (bug):** [[02 - Casos de teste]]  
> **Validação (bug):** [[03 - Validação dev]]  

Esta nota transforma os CTs refinados do vault em casos da Qase. Não crie CT novo aqui: apenas traduza o caso existente para os campos da API.

## Configuração

- **Projeto Qase:** não configurado; envio fora de escopo
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

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: usar o ID da demanda e o módulo (`NXG-031`, `infra`); não criar uma tag para cada CT, pois o título e o ID do caso já fazem essa identificação.


## Casos preparados

### CT-B01 — Primeira transição legado para infra

Origem: [[02 - Casos de teste#^ct-b01|CT-B01]]. Descrição/pré-condições/passos/pós-condições seguem exclusivamente o CT de origem. Camada infra, regressão, automação ambos. Não enviado; projeto/suite não configurados.

### CT-B02 — Fetch ou SHA inválido falha antes de build

Origem: [[02 - Casos de teste#^ct-b02|CT-B02]]. Descrição/pré-condições/passos/pós-condições seguem exclusivamente o CT de origem. Camada infra, regressão, automação ambos. Não enviado; projeto/suite não configurados.

### CT-B03 — Alterações remotas são preservadas

Origem: [[02 - Casos de teste#^ct-b03|CT-B03]]. Descrição/pré-condições/passos/pós-condições seguem exclusivamente o CT de origem. Camada infra, regressão, automação ambos. Não enviado; projeto/suite não configurados.

### CT-B04 — Repetição, env com espaços e uso manual

Origem: [[02 - Casos de teste#^ct-b04|CT-B04]]. Descrição/pré-condições/passos/pós-condições seguem exclusivamente o CT de origem. Camada infra, regressão, automação ambos. Não enviado; projeto/suite não configurados.

### CT-B05 — Gates produção, backup e compartilhamento de checkout

Origem: [[02 - Casos de teste#^ct-b05|CT-B05]]. Descrição/pré-condições/passos/pós-condições seguem exclusivamente o CT de origem. Camada infra, regressão, automação ambos. Não enviado; projeto/suite não configurados.

### CT-B06 — Portabilidade de segredos e documentação de operação

Origem: [[02 - Casos de teste#^ct-b06|CT-B06]]. Descrição/pré-condições/passos/pós-condições seguem exclusivamente o CT de origem. Camada infra, regressão, automação ambos. Não enviado; projeto/suite não configurados.

## Checklist de envio

Envio externo fora do escopo. Sem uso do script WIP Qase.
