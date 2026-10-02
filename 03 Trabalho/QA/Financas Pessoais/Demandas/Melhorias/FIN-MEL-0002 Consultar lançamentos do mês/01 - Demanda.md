---
prioridade: alta
status: analise
tipo: melhoria
etapa_atual: "QA · Análise da demanda"
modulo: lancamentos
plano: "[[02 - Plano de teste]]"
execucao: "[[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0002/00 README|Execução DEV]]"
ambiente: dev
origem: conversa
projeto: financas-pessoais
pai: ""
data_inicio: 2026-10-02
data_fim: ""
responsavel: ""
pontos_alocados: 5
---

# FIN-MEL-0002 — Consultar lançamentos do mês

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0002/00 README|Execução DEV]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** preencher `projeto` no frontmatter antes de roteiar a melhoria.

> [!info] Status atual
> **Próximo passo:** revisar a demanda e os CTs antes de liberar para DEV.

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> **Capacidade alocada:** 5 pontos.
> Esta melhoria fecha o primeiro ciclo de uso: cadastrar e consultar lançamentos.

---

## Problema / contexto

O usuário já consegue registrar um lançamento, mas não consegue consultar dentro da aplicação o que foi salvo. O backend já possui `GET /api/lancamentos?mes=AAAA-MM`, porém o frontend ainda não apresenta essa informação.

---

## Objetivo

Permitir que o usuário consulte os lançamentos de um mês e confirme visualmente os registros persistidos.

### Entrega desta capacidade

Entregar uma visão mensal mobile-first com seletor de mês, lista de lançamentos, total de despesas e estados de carregamento, vazio e erro.

---

## Decisões de produto

- A consulta mensal será a primeira tela de acompanhamento após o cadastro.
- O frontend usará o endpoint existente, sem alterar o contrato do backend.
- O mês atual será o filtro inicial.
- O total exibido nesta melhoria será apenas o total de despesas listadas; receitas e saldo completo ficam para uma etapa posterior.

---

## Escopo

- Consumo de `GET /api/lancamentos?mes=AAAA-MM`.
- Seletor de mês.
- Lista de lançamentos com data, descrição, tipo e valor.
- Total mensal de despesas.
- Estado de carregamento.
- Estado vazio sem lançamentos.
- Estado de erro com possibilidade de tentar novamente.
- Layout responsivo para celular e desktop.

---

## Fora de escopo

- Edição e exclusão de lançamentos.
- Dashboard completo e gráficos.
- Saldo projetado.
- Parcelas e recorrências.
- Paginação.
- Alteração do backend ou do contrato da API.

---

## Critérios de aceite

- C1. Ao abrir a consulta mensal, o mês atual é selecionado e os lançamentos são carregados pela API. ^c1
- C2. Cada lançamento é exibido com data, descrição, tipo e valor formatado em reais. ^c2
- C3. O total de despesas do mês é calculado e exibido corretamente. ^c3
- C4. O usuário pode trocar o mês e a lista é atualizada com os dados correspondentes. ^c4
- C5. A tela apresenta estados claros de carregamento, lista vazia e erro de API, com opção de tentar novamente quando aplicável. ^c5
- C6. A consulta funciona em viewport móvel e desktop sem quebrar o layout. ^c6

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste serão vinculados antes da liberação.
- [x] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Nenhuma bloqueante. O total desta entrega considera somente despesas; saldo e receitas detalhados ficam fora do escopo.
