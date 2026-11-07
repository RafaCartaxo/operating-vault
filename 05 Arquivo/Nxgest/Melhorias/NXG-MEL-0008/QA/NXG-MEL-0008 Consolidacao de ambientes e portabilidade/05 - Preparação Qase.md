---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: ""
projeto: "nxgest"
modulo: ""
qase_projeto: ""
qase_suite_id: ""
casos_origem: ""
validacao_origem: ""
epico: "NXG-EPIC-0001"
responsavel: "NX Gest · QA e Coordenação"
---
# Preparação Qase — NXG-MEL-0008

> **Posição no pacote:** melhoria → `05 - Preparação Qase.md`; bug → `04 - Preparação Qase.md`. O conteúdo deste modelo é o mesmo nos dois casos.

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Casos de teste (melhoria):** [[03 - Casos de teste]]  
> **Validação (melhoria):** [[04 - Validação dev]]  

Esta nota transforma os CTs refinados do vault em casos da Qase. Não crie CT novo aqui: apenas traduza o caso existente para os campos da API.

## Configuração

- Projeto Qase: não configurado nesta execução; envio externo fora do escopo.
- Suite Qase: não aplicável sem envio.
- Origem: [[03 - Casos de teste]].
- Validação: [[04 - Validação dev]].

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

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: usar o ID da demanda e o módulo (`NXG-MEL-0008`, `cliente`); não criar uma tag para cada CT, pois o título e o ID do caso já fazem essa identificação.

## Casos preparados

- CT-001: Modelo unico completo; descrição, pré-condições, passos e pós-condição na origem. Qase ID: não enviado.
- CT-002: Onboarding coerente; descrição, pré-condições, passos e pós-condição na origem. Qase ID: não enviado.
- CT-003: Instancia de teste isolada; descrição, pré-condições, passos e pós-condição na origem. Qase ID: não enviado.
- CT-004: Regressao integrada; descrição, pré-condições, passos e pós-condição na origem. Qase ID: não enviado.
- CT-005: Clone funcional; descrição, pré-condições, passos e pós-condição na origem. Qase ID: não enviado.
- CT-006: Preservacao e commits; descrição, pré-condições, passos e pós-condição na origem. Qase ID: não enviado.
- CT-007: Nomenclatura e continuidade; descrição, pré-condições, passos e pós-condição na origem. Qase ID: não enviado.
- CT-008: Governanca verificavel; descrição, pré-condições, passos e pós-condição na origem. Qase ID: não enviado.

## Checklist de envio

- [ ] Todos os CTs candidatos têm descrição, pré-condições e passos.
- [ ] Projeto e suite confirmados.
- [ ] Campos normalizados e passos separados.
- [ ] Tags limitadas ao ID da demanda e ao módulo.
- [ ] Campos da API validados.
- [ ] Envio realizado sem duplicação.
- [ ] IDs da Qase registrados nesta nota.
- [ ] Status alterado para `enviado`.
