---
prioridade: alta
status: concluido
tipo: melhoria
etapa_atual: "Concluído"
modulo: lancamentos
plano: "[[02 - Plano de teste]]"
execucao: "[[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0003/00 README|Execução DEV]]"
ambiente: dev
origem: conversa
projeto: financas-pessoais
pai: ""
data_inicio: 2026-10-02
data_fim: ""
responsavel: ""
pontos_alocados: 8
---

# FIN-MEL-0003 — Editar e excluir lançamentos

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0003/00 README|Execução DEV]]

> [!info] Status atual
> Status: concluída; todos os CTs aprovados e execução DEV encerrada.

## Problema / contexto

O usuário já consegue cadastrar e consultar lançamentos, mas não consegue corrigir dados digitados incorretamente nem remover um registro lançado por engano.

## Objetivo

Permitir editar e excluir lançamentos diretamente na consulta mensal, com confirmação, validação e atualização segura da lista.

## Decisões de produto

- Editar reutilizará o formulário de cadastro preenchido com os dados atuais.
- Excluir exigirá confirmação explícita.
- Após editar ou excluir, lista e total serão atualizados.
- O backend continuará sendo a fonte de verdade.
- Falhas não podem apagar dados da tela sem comunicação clara.

## Escopo

- Endpoint de atualização.
- Endpoint de exclusão.
- Ações editar e excluir na lista.
- Formulário preenchido e validações reaproveitadas.
- Confirmação antes de excluir.
- Estados de salvamento, exclusão, sucesso e erro.
- Atualização da lista e total.
- Uso em celular e desktop.

## Fora de escopo

- Exclusão em massa.
- Histórico de alterações.
- Desfazer exclusão.
- Auditoria de usuários.
- Parcelas, recorrências e anexos.

## Critérios de aceite

- C1. Cada lançamento apresenta ações de editar e excluir.
^c1
- C2. Editar abre o formulário preenchido com os dados atuais.
^c2
- C3. Dados editados são validados e persistidos pela API.
^c3
- C4. Excluir exige confirmação e remove o registro correto.
^c4
- C5. Lista e totais são atualizados após editar ou excluir.
^c5
- C6. Erros preservam a tela e informam o usuário.
^c6
- C7. O fluxo funciona em celular e desktop.
^c7

## Checklist de entrega ao DEV

- [x] Problema e objetivo claros.
- [x] Escopo e fora de escopo definidos.
- [x] Critérios testáveis.
- [ ] Plano e CTs revisados e aprovados.
- [x] Pontos iniciais preenchidos.
