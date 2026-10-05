---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: melhoria
projeto: financas-pessoais
modulo: ""
qase_projeto: ""
qase_suite_id: ""
casos_origem: "[[03 - Casos de teste]]"
validacao_origem: "[[04 - Validação dev]]"
---
# Preparação Qase — FIN-MEL-0013

> **Posição no pacote:** melhoria → `05 - Preparação Qase.md`; bug → `04 - Preparação Qase.md`. O conteúdo deste modelo é o mesmo nos dois casos.

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]

Esta nota transforma os CTs refinados do vault em casos da Qase. Não crie CT novo aqui: apenas traduza o caso existente para os campos da API.

## Configuração

- **Projeto Qase:** a definir no envio
- **Suite Qase:** a definir no envio
- **Origem:** [[03 - Casos de teste]]

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

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: usar o ID da demanda e o módulo (`<PROJ>-MEL-NNNN`, `cliente`); não criar uma tag para cada CT, pois o título e o ID do caso já fazem essa identificação.

## Casos preparados

> O bloco abaixo é um exemplo de preenchimento. Ao criar a nota do card, substitua-o pelos CTs reais da nota de origem. Não envie este exemplo para a Qase.

### CT-001 a CT-005 — Orquestração mensal em service

- **Qase ID:** `a preencher após o envio`
- **Descrição:** importar os cinco CTs da nota de origem, preservando critérios, pré-condições, passos, resultado esperado e pós-condição.
- **Pré-condições:** usar os CTs-001 a 005 de [[03 - Casos de teste]].
- **Passos:** separar Dado/Quando/Então em passos numerados por CT.
- **Tipo:** funcional, regressão, negativo ou inspeção conforme a nota de origem.
- **Camada:** unit ou API conforme a matriz.
- **Automação:** automatizado, manual ou ambos conforme a matriz.
- **Prioridade Qase:** média.
- **Severidade Qase:** normal.
- **Comportamento:** positivo.
- **Tags Qase:** `FIN-MEL-0013`, `arquitetura/backend`

> **Regra:** critérios, evidências, esforço e resultado da execução continuam no vault ou no Test Run; não duplicar esses dados no caso da Qase.

## Checklist de envio

- [ ] Todos os CTs candidatos têm descrição, pré-condições e passos.
- [ ] Projeto e suite confirmados.
- [ ] Campos normalizados e passos separados.
- [ ] Tags limitadas ao ID da demanda e ao módulo.
- [ ] Campos da API validados.
- [ ] Envio realizado sem duplicação.
- [ ] IDs da Qase registrados nesta nota.
- [ ] Status alterado para `enviado`.
