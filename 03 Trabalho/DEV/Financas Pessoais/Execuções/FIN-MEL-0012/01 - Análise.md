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

## Arquitetura existente considerada

- O backend usa `handler.go` para HTTP, `model.go` para tipos/validação e `repository.go` para SQLite; não há camada de serviço separada.
- As migrations são embutidas por `database.go` e aplicadas na abertura do banco.
- O frontend concentra a composição de tela em `App.tsx`, mantém contratos em `src/types.ts`, chamadas HTTP em `src/services/` e validações de formulário em `src/utils/validation.ts`.
- O resumo mensal é calculado no frontend a partir do retorno de `GET /api/lancamentos?mes=AAAA-MM`.
- O fluxo existente de parcelas usa série identificável, transação no repository e endpoints próprios; recorrências devem seguir o mesmo padrão sem reutilizar semântica de parcela.

## Proposta técnica

- Criar o domínio `internal/recorrencias` com modelo, validação, handler e repository próprios.
- Persistir regras recorrentes em tabela própria, com descrição, valor em centavos, conta/cartão, início, término opcional, estado ativo e `incluida_na_fatura`.
- Adicionar vínculo e competência às ocorrências persistidas em `lancamentos`, com índice único por regra e competência para garantir idempotência.
- Gerar a ocorrência sob demanda quando o mês for consultado, dentro do backend, antes da listagem mensal.
- Copiar `incluida_na_fatura` da regra para a ocorrência; ocorrências históricas não serão reescritas quando a regra for editada.
- Expor CRUD de regras em `/api/recorrencias`; edição altera a regra e o encerramento define o término/estado sem apagar histórico.
- Adicionar a tela de Recorrências ao `App.tsx`, usando services tipados, validação compartilhada e componentes/padrões visuais já existentes.
- O resumo mensal deve excluir do saldo as ocorrências marcadas como incluídas na fatura, mas continuar exibindo-as na lista com indicação visual de controle.

## Riscos e limites

- Não será criado um módulo completo de faturas nesta melhoria; a marcação explícita é o contrato mínimo para C5.
- A mudança deve preservar lançamentos e parcelas existentes, além da idempotência em consultas repetidas.
- Migrations precisam ser compatíveis com bancos existentes e os fluxos Mermaid/documentação de API e dados devem ser atualizados junto com o código.

## Decisão necessária antes do DEV

Validar com QA a alteração observável do C5/CT-008 para explicitar a marcação `incluida_na_fatura`. Com essa decisão, o plano técnico pode ser congelado e a implementação full-stack iniciada.
