---
prioridade: media
status: analise
tipo: melhoria
etapa_atual: "QA · Análise da demanda"
modulo: lancamentos
plano: "[[02 - Plano de teste]]"
execucao: "[[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0005/00 README|Execução DEV]]"
ambiente: dev
origem: conversa
projeto: financas-pessoais
pai: ""
data_inicio: 2026-10-02
data_fim: ""
responsavel: ""
pontos_alocados: 3
---

# FIN-MEL-0005 — Resumo mensal financeiro

> [!info]- Navegação QA
> **README:** [[00 README]]  
> **Plano:** [[02 - Plano de teste]]  
> **Casos:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0005/00 README|Execução DEV]]

## Problema / contexto

A consulta mensal já lista os lançamentos e mostra o total de despesas, mas ainda não apresenta uma visão rápida do resultado financeiro do período.

## Objetivo

Exibir um resumo mensal com receitas, despesas, saldo e quantidade de lançamentos, usando os dados já consultados.

## Escopo

- Total de receitas.
- Total de despesas.
- Saldo do mês: receitas menos despesas.
- Quantidade de lançamentos.
- Estados consistentes para lista vazia, carregamento e erro.
- Layout responsivo.

## Fora de escopo

- Gráficos.
- Categorias e filtros avançados.
- Parcelas e recorrências.
- Alteração do backend.
- Metas financeiras.
- PWA.

## Critérios de aceite

- C1. O resumo exibe o total de receitas do mês. ^c1
- C2. O resumo exibe o total de despesas do mês. ^c2
- C3. O saldo é calculado como receitas menos despesas. ^c3
- C4. A quantidade de lançamentos corresponde à lista exibida. ^c4
- C5. O resumo acompanha a troca de mês e os estados da consulta. ^c5
- C6. O resumo funciona em celular e desktop. ^c6

## Checklist de entrega ao DEV

- [x] Problema e objetivo definidos.
- [x] Escopo e fora de escopo definidos.
- [x] Critérios objetivos e testáveis.
- [ ] Plano e CTs aprovados.
