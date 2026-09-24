---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: ""
modulo: ""
qase_projeto: ""
qase_suite_id: ""
casos_origem: ""
validacao_origem: ""
---
# Preparação Qase — <ID>

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

- **Projeto Qase:** `<código>`
- **Suite Qase:** `<id>`
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

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: usar o ID da demanda e o módulo (`MEL-NNNN`, `cliente`); não criar uma tag para cada CT, pois o título e o ID do caso já fazem essa identificação.

## Casos preparados

> O bloco abaixo é um exemplo de preenchimento. Ao criar a nota do card, substitua-o pelos CTs reais da nota de origem. Não envie este exemplo para a Qase.

### CT-NNN — Salvar registro com dados válidos *(exemplo)*

- **Qase ID:** `preencher após o envio`
- **Descrição:** confirma que o registro pode ser salvo quando os dados obrigatórios são válidos.
- **Pré-condições:** usuário está na tela de cadastro; os dados obrigatórios estão preenchidos com valores válidos.
- **Passos:** separar Dado/Quando/Então em passos numerados, cada um com ação e resultado esperado.
- **Passo 1 — Ação:** informar dados válidos no formulário  
  **Resultado esperado:** os valores são aceitos sem mensagem de erro.
- **Passo 2 — Ação:** clicar em **Salvar**  
  **Resultado esperado:** o registro é salvo e fica disponível para consulta.
- **Pós-condição:** registro persistido com os dados informados.
- **Tipo:** funcional.
- **Camada:** E2E.
- **Automação:** manual.
- **Prioridade Qase:** média.
- **Severidade Qase:** normal.
- **Comportamento:** positivo.
- **Tags Qase:** `<ID da demanda>`, `<módulo>`

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
