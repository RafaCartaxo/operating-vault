# 01 - Análise (FIN-MEL-0008)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0008 Parcelas/01 - Demanda|FIN-MEL-0008 — Parcelas]]
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0008 Parcelas/04 - Validação dev|Validação QA]]

---

## Veredito

A melhoria é viável aproveitando os campos de parcela existentes, adicionando vínculo de série, geração transacional e controles no frontend.

---

## O que foi confirmado

- O schema já contém parcela_atual e total_parcelas, mas não possui identificador de série nem geração múltipla.
- O backend atual cria um lançamento por requisição.
- O frontend ainda não possui campos de parcelamento.

---

## Abordagem e riscos

- Migração SQLite compatível com dados existentes.
- Transação obrigatória para criação/edição/exclusão da série.
- Arredondamento em centavos e calendário mensal.
- Regressão dos lançamentos simples.

---

## Alternativas descartadas

- Alternativa e motivo de não seguir.

---

## Perguntas abertas

- Nenhuma. Se houver decisão que altere escopo, regra ou aceite, voltar o card para análise.
