---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: melhoria
projeto: financas-pessoais
modulo: lancamentos
qase_projeto: ""
qase_suite_id: ""
casos_origem: "[[03 - Casos de teste]]"
validacao_origem: "[[04 - Validação dev]]"
---

# Preparação Qase — FIN-MEL-0001

> **Posição no pacote:** melhoria → `05 - Preparação Qase.md`.

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/00 README|Execução DEV]]

Esta nota transforma os CTs refinados do vault em casos da Qase. Não crie CT novo aqui: apenas traduza os casos existentes em [[03 - Casos de teste]].

## Configuração

- **Projeto Qase:** preencher.
- **Suite Qase:** preencher.
- **Origem:** [[03 - Casos de teste]].

## Mapeamento dos campos

| Vault | Qase | Regra |
|---|---|---|
| Título do CT | `title` | manter o título humano do cenário |
| Descrição | `description` | resumir o objetivo do CT |
| Pré-condições | `preconditions` | copiar sem misturar com os passos |
| Dado/Quando/Então | `steps` | separar cada ação e resultado esperado |
| Pós-condição | `postconditions` | registrar somente o estado após o teste |
| Tipo, camada, automação | campos Qase | usar os valores normalizados |

Valores normalizados: `funcional`/`regressão`; camada `E2E`/`API`/`unit`; automação `manual`/`automatizado`/`ambos`.

## Casos preparados

Os CTs candidatos são `CT-001` a `CT-007`, mantidos exclusivamente na nota [[03 - Casos de teste]].

## Checklist de envio

- [ ] Todos os CTs têm descrição, pré-condições e passos.
- [ ] Projeto e suite confirmados.
- [ ] Campos normalizados e passos separados.
- [ ] Tags limitadas ao ID da demanda e ao módulo.
- [ ] Envio realizado sem duplicação.
- [ ] IDs da Qase registrados nesta nota.
- [ ] Status alterado para `enviado`.
