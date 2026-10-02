# 01 - Análise — FIN-MEL-0005

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0005/00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0005 Resumo mensal financeiro/01 - Demanda|FIN-MEL-0005 — Demanda QA]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0005 Resumo mensal financeiro/04 - Validação dev|Validação QA]]

---

## Veredito

A melhoria é viável no frontend, calculando o resumo a partir dos lançamentos já retornados pela consulta mensal, sem alteração de banco ou endpoint.

## O que foi confirmado

- A tela já carrega os lançamentos filtrados por mês.
- O tipo do lançamento permite separar receitas e despesas.
- Os indicadores podem ser derivados da mesma lista exibida, evitando divergência entre resumo e tabela.
- A troca de mês e os estados de carregamento, vazio e erro já existem no fluxo de acompanhamento.

## Abordagem e riscos

- Implementar um componente de resumo mensal próximo da lista de lançamentos.
- Centralizar o cálculo em uma função pura para permitir teste unitário.
- Preservar a regra atual do valor monetário e a responsividade mobile.
- Não criar novo endpoint enquanto a origem dos dados continuar sendo a consulta mensal existente.

## Alternativas descartadas

- Criar endpoint específico para resumo: desnecessário para o escopo atual e aumentaria a superfície da API.
- Recalcular valores a partir do texto formatado: sujeito a erro; usar os valores numéricos normalizados.

## Perguntas abertas

- A aprovação QA dos 13 CTs deve ocorrer antes da implementação.
