---
projeto: financas-pessoais
camada: QA
status: analise
tipo: melhoria
etapa_atual: "QA · Análise da demanda"
demanda: FIN-MEL-0001
execucao: FIN-MEL-0001
---

# FIN-MEL-0001 — Frontend mobile-first para nova despesa

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/00 README|Execução DEV]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

> [!tip]- Esforço
> O esforço da demanda é a soma dos pontos registrados nos artefatos do pacote. A capacidade alocada está registrada na nota de demanda.

## Fluxo desta demanda

```text
QA · Demanda → QA · Plano e CTs → DEV · Implementação → QA · Validação → Concluído
```

## Estado

A demanda está sendo estruturada em QA. O backend já existe e está validado; o objetivo deste ciclo é construir a primeira experiência de lançamento de despesa no frontend.

## Próximo passo

Fechar os critérios e casos de teste. Depois disso, a execução DEV pode avançar para o plano técnico e a implementação.
