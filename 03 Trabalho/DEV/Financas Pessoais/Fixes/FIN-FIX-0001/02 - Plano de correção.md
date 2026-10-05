# 02 - Plano de correção (FIN-FIX-0001)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Bugs/FIN-BUG-0001 Falha ao gerar recorrencias mensais/01 - Bug|FIN-BUG-0001]]
> **Análise:** [[01 - Análise|01 - Análise]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Casos de teste QA:** [[03 Trabalho/QA/<projeto>/Demandas/Bugs/<ID>/02 - Casos de teste|Casos de teste]]  
> **Validação QA:** [[03 Trabalho/QA/<projeto>/Demandas/Bugs/<ID>/03 - Validação dev|Validação QA]]

> Congelado na aprovação. Alteração posterior vira decisão registrada em `03 - Implementação.md`.

---

## Resultado esperado

Em uma frase: a consulta mensal volta a carregar lançamentos e gerar ocorrências sem bloquear o SQLite.

---

## Mudança planejada

- Arquivos/áreas a tocar: `backend/internal/recorrencias/repository.go` e teste do repositório.
- Abordagem mínima: materializar o resultado da consulta, fechar as linhas e só então executar as inserções idempotentes.
- Regressão a proteger: uma ocorrência por recorrência e competência, inclusive em duas consultas consecutivas.

---

## Fora de escopo

- Frontend, contrato da API, regras de data, modelo de recorrência e resumo financeiro.

---

## Pronto quando

- [ ] CTs QA executados.
- [x] Regressão automatizada criada ou atualizada quando aplicável.
- [x] Gates do repositório verdes.
- [x] Code review aprovado.
