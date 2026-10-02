# 01 - Análise — FIN-MEL-0003

> [!info]- Navegação QA/DEV
> **README:** [[00 README]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0003 Editar e excluir lançamentos/01 - Demanda|FIN-MEL-0003 — Demanda QA]]  
> **Plano:** [[02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação]]  
> **Code review:** [[04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0003 Editar e excluir lançamentos/04 - Validação dev|Validação QA]]

## Veredito

A melhoria é viável. O backend Go já possui criação e consulta por ID no repositório, mas ainda não expõe atualização ou exclusão HTTP. O frontend deve reutilizar o formulário atual e atualizar a consulta mensal após cada operação.

## Abordagem

- Adicionar PUT e DELETE no mesmo recurso /api/lancamentos/{id}.
- Reutilizar a validação de domínio existente.
- Reutilizar o formulário React para cadastro e edição.
- Exigir confirmação explícita antes do DELETE.
- Reconsultar o mês após edição ou exclusão.
- Preservar a tela e comunicar erros HTTP.

## Riscos

- Alterar ou excluir ID incorreto.
- Editar para outro mês e deixar a lista antiga inconsistente.
- Alterar tipo e não recalcular o total.
- Excluir sem confirmação.
- Divergência entre payload de edição e criação.

## Perguntas abertas

Nenhuma bloqueante.

