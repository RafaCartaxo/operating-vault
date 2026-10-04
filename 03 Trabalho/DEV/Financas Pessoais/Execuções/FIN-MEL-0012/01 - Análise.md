# 01 - Análise — FIN-MEL-0012

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0012 Recorrências mensais/01 - Demanda|FIN-MEL-0012 — Recorrências mensais sem duplicidade]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0012 Recorrências mensais/04 - Validação dev|Validação QA]]

---

## Veredito

Em uma frase: a melhoria é tecnicamente viável, mas C5 exige uma decisão de produto antes do plano e da implementação.

---

## O que foi confirmado

- O código possui apenas `lancamentos`, parcelas e vínculo textual `conta_ou_cartao`.
- Não existe tabela, endpoint ou modelo de fatura.
- Não existe campo que indique se uma recorrência já foi incluída em uma fatura.
- O cálculo mensal atual soma lançamentos; não há camada de reconciliação ou deduplicação por fatura.

---

## Abordagem e riscos

- Será necessária uma decisão sobre como representar “já incluído na fatura”.
- Sem essa decisão, gerar o lançamento recorrente como despesa pode duplicar o saldo; não gerar pode ocultar uma cobrança real.
- A alternativa técnica provável é persistir uma regra recorrente e ocorrências vinculadas, com estado explícito de inclusão na fatura, mas isso altera o contrato do C5.

---

## Alternativas descartadas

- Inferir a inclusão pela existência de outro lançamento no mesmo valor/data: rejeitada por risco de falso positivo.
- Tratar todo recorrente de cartão como controle-only: rejeitada porque pode omitir cobrança quando a fatura não estiver lançada.
- Duplicar diretamente em `lancamentos` sem origem/status: rejeitada porque impede idempotência e rastreabilidade.

---

## Perguntas abertas

- Como o usuário informa que a cobrança já está na fatura?
- A fatura será cadastrada nesta demanda ou o C5 deve usar um campo manual por ocorrência (`incluida_na_fatura`)?
- O saldo deve excluir somente ocorrências marcadas como incluídas ou toda recorrência vinculada a cartão?

## Decisão necessária antes do DEV

O item deve voltar para QA · Análise para fechar a regra de C5 e atualizar CT-008 antes da implementação. Não há alteração de código nesta execução.
