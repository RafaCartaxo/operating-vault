# 02 - Plano de execução — FIN-MEL-0003

> [!info]- Navegação QA/DEV
> **README:** [[00 README]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0003 Editar e excluir lançamentos/01 - Demanda|FIN-MEL-0003 — Demanda QA]]  
> **Análise:** [[01 - Análise]]  
> **Implementação:** [[03 - Implementação]]  
> **Code review:** [[04 - Code review]]

## Sequência

- Implementar Update e Delete no repository.
- Adicionar rotas HTTP com validação de ID e payload.
- Criar testes unitários e de handler para os novos contratos.
- Adicionar updateLancamento e deleteLancamento no service frontend.
- Reutilizar o formulário para criar e editar.
- Adicionar ações e confirmação na lista.
- Atualizar lista e totais depois das operações.
- Executar testes, build e smoke.

## Contratos previstos

- PUT /api/lancamentos/{id}: recebe os campos do lançamento e retorna 200 com o registro atualizado.
- DELETE /api/lancamentos/{id}: remove o registro e retorna 204.
- Registro inexistente retorna 404 sem alterar outros dados.

## Pronto quando

- CT-001 a CT-012 estiverem tecnicamente cobertos.
- npm test, npm run build e go test ./... passarem.
- Edição e exclusão funcionarem em celular e desktop.
- Documentação da API e dos fluxos estiver atualizada.

