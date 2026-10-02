---
demanda: FIN-MEL-0002
status: planejado
responsavel: ""
pontos: 1
---

# Plano de teste — FIN-MEL-0002

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0002/00 README|Execução DEV]]

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Comprovar que o usuário consegue consultar os lançamentos de qualquer mês e entende os estados normal, vazio e erro.

---

## Riscos e escopo

- Risco de o mês enviado não seguir `AAAA-MM`.
- Risco de valores de receita entrarem indevidamente no total de despesas.
- Risco de lista vazia ser confundida com erro.
- Risco de carregamento quebrar a experiência em celular.

---

## Estratégia de teste

- **Unitário:** filtro de despesas, soma e formatação monetária.
- **API/repositório:** contrato do `GET /api/lancamentos?mes=AAAA-MM`.
- **UI/E2E:** carregamento, troca de mês, lista, vazio, erro e responsividade.
- **Regressão:** cadastro de nova despesa continua funcionando.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001|CT-001]] | Funcional | UI/API | Manual + automatizado | [[04 - Validação dev|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002|CT-002]] | Funcional | UI/unit | Manual + automatizado | [[04 - Validação dev|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003|CT-003]] | Funcional | UI/unit | Manual + automatizado | [[04 - Validação dev|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004|CT-004]] | Funcional | UI/API | Manual | [[04 - Validação dev|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005|CT-005]] | Negativo | UI/API | Manual | [[04 - Validação dev|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006|CT-006]] | Responsividade | UI | Manual | [[04 - Validação dev|Registrar resultado]] |

---

## Entrada e saída

**Entrada:** frontend integrado, backend iniciado, dados de teste em mais de um mês e contrato da API confirmado.  
**Saída:** CTs executados, cálculos conferidos, estados de UI validados e nenhum bloqueio crítico aberto.
