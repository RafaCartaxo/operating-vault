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
# Preparação Qase — FIN-MEL-0012

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

- **Projeto Qase:** a definir no envio
- **Suite Qase:** a definir no envio
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

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: usar `FIN-MEL-0012` e `lancamentos`; não criar uma tag para cada CT.

## Casos preparados

> O bloco abaixo é um exemplo de preenchimento. Ao criar a nota do card, substitua-o pelos CTs reais da nota de origem. Não envie este exemplo para a Qase.

### CT-001 — Cadastrar recorrência mensal

- **Qase ID:** a registrar após o envio
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
- **Tags Qase:** `FIN-MEL-0012`, `lancamentos`

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
