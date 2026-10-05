---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: bug
projeto: "Financas Pessoais"
modulo: ""
qase_projeto: ""
qase_suite_id: ""
casos_origem: "[[02 - Casos de teste]]"
validacao_origem: "[[03 - Validação dev]]"
---
# Preparação Qase — FIN-BUG-0001

> **Posição no pacote:** melhoria → `05 - Preparação Qase.md`; bug → `04 - Preparação Qase.md`. O conteúdo deste modelo é o mesmo nos dois casos.

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Casos de teste (melhoria):** [[03 - Casos de teste]]  
> **Casos de teste (bug):** [[02 - Casos de teste]]  
> **Validação (melhoria):** [[04 - Validação dev]]  
> **Validação (bug):** [[03 - Validação dev]]  
> Remova as duas linhas que não correspondem ao tipo do card.

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

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: usar `FIN-BUG-0001` e `recorrencias`; não criar uma tag para cada CT, pois o título e o ID do caso já fazem essa identificação.

## Casos preparados

> O bloco abaixo é um exemplo de preenchimento. Ao criar a nota do card, substitua-o pelos CTs reais da nota de origem. Não envie este exemplo para a Qase.

### CT-B01 — Carregar lançamentos com recorrência ativa

- **Qase ID:** não enviado
- **Descrição:** confirma que a consulta mensal carrega quando há recorrência ativa.
- **Pré-condições:** existe uma recorrência ativa e o backend está disponível.
- **Passo 1 — Ação:** acessar Acompanhamento no mês da recorrência
  **Resultado esperado:** a aplicação solicita os lançamentos do mês.
- **Passo 2 — Ação:** consultar `GET /api/lancamentos?mes=2026-10`
  **Resultado esperado:** a API retorna os lançamentos sem HTTP 500.
- **Pós-condição:** lista mensal disponível para o usuário.
- **Tipo:** regressão.
- **Camada:** API/E2E.
- **Automação:** manual.
- **Prioridade Qase:** média.
- **Severidade Qase:** normal.
- **Comportamento:** positivo.
- **Tags Qase:** `FIN-BUG-0001`, `recorrencias`

### CT-B02 — Recalcular mês sem duplicar ocorrências

- **Qase ID:** não enviado
- **Descrição:** confirma que consultar novamente a mesma competência não duplica a ocorrência.
- **Pré-condições:** existe uma recorrência ativa e uma ocorrência já processada.
- **Passo 1 — Ação:** consultar novamente `GET /api/lancamentos?mes=2026-10`
  **Resultado esperado:** a API retorna os lançamentos sem erro.
- **Passo 2 — Ação:** comparar as ocorrências da recorrência na competência
  **Resultado esperado:** existe no máximo uma ocorrência.
- **Pós-condição:** consulta repetida concluída sem duplicidade.
- **Tipo:** regressão.
- **Camada:** API/E2E.
- **Automação:** manual.
- **Prioridade Qase:** média.
- **Severidade Qase:** normal.
- **Comportamento:** positivo.
- **Tags Qase:** `FIN-BUG-0001`, `recorrencias`

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
