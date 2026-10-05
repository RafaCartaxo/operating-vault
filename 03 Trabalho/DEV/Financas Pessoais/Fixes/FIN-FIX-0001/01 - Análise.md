# 01 - Análise (FIN-FIX-0001)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Bugs/FIN-BUG-0001 Falha ao gerar recorrencias mensais/01 - Bug|FIN-BUG-0001]]
> **Plano:** [[02 - Plano de correção|02 - Plano de correção]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Casos de teste QA:** [[03 Trabalho/QA/<projeto>/Demandas/Bugs/<ID>/02 - Casos de teste|Casos de teste]]  
> **Validação QA:** [[03 Trabalho/QA/<projeto>/Demandas/Bugs/<ID>/03 - Validação dev|Validação QA]]

---

## Veredito

Em uma frase: a causa foi confirmada e o fix mínimo é viável sem alterar o contrato funcional.

---

## O que foi confirmado

- `EnsureMonth` mantém o cursor de `SELECT` aberto enquanto executa `INSERT` em `lancamentos`.
- O SQLite retorna `database is locked (5) (SQLITE_BUSY)` quando há recorrência ativa.
- O erro bloqueia `GET /api/lancamentos?mes=AAAA-MM`, embora o cadastro e a listagem de recorrências funcionem.

---

## Abordagem e riscos

- Carregar as recorrências em memória, fechar o cursor e somente depois inserir as ocorrências.
- Adicionar teste de repositório cobrindo criação da ocorrência mensal.
- Reexecutar a consulta duas vezes para proteger a idempotência.
