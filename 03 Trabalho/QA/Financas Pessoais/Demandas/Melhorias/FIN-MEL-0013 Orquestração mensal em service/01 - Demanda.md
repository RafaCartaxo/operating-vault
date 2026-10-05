---
prioridade: media
status: analise
tipo: melhoria
etapa_atual: "QA · Triagem"
modulo: arquitetura/backend
plano: "[[02 - Plano de teste]]"
execucao: ""
ambiente: dev
origem: conversa
projeto: financas-pessoais
epico: ""
pai: ""
data_inicio: "2026-10-05"
data_fim: ""
responsavel: ""
pontos_alocados: 5
---

# FIN-MEL-0013 — Orquestração mensal em service de aplicação

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/<projeto>/Execuções/<ID>/00 README|Execução DEV]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** preencher `projeto` no frontmatter antes de roteiar a melhoria.


> [!info] Status atual
> **Próximo passo:** registrar a próxima ação objetiva.

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> **Capacidade alocada:** preencher `pontos_alocados`.
> Exemplo: se houver 50 pontos disponíveis no ciclo, usar `pontos_alocados: 50`.
>
> ```dataviewjs
> const id = (dv.current().file.path.match(/(?:[A-Z]{2,8}-)?MEL-\d+/) || [""])[0];
> const paginas = dv.pages().where(p => id && p.file.path.includes(id) && typeof p.pontos === "number");
> const lista = paginas.sort(p => p.file.name);
> const necessario = lista.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> const alocado = Number(dv.current().pontos_alocados || 0);
> const diferenca = alocado - necessario;
> if (lista.length > 0) {
>   dv.table(["Etapa/artefato", "Pontos"], lista.map(p => [p.file.link, p.pontos]));
> } else {
>   dv.paragraph("Nenhum artefato com pontos registrado ainda.");
> }
> dv.paragraph(`**Esforço necessário:** ${necessario} pontos · **Capacidade alocada:** ${alocado} pontos · **${diferenca >= 0 ? "Saldo" : "Déficit"}:** ${Math.abs(diferenca)} pontos`);
> ```

---

## Problema / contexto

O endpoint mensal de lançamentos precisa garantir que as recorrências do mês sejam materializadas antes de consultar os lançamentos. Hoje essa coordenação está próxima do handler HTTP e conhece diretamente responsabilidades de recorrências e listagem. Isso funciona, mas deixa a fronteira entre transporte HTTP e caso de uso pouco explícita, dificulta testes isolados e aumenta o risco de novas integrações acoplarem regras ao handler.

O domínio permanece separado: `recorrencias` guarda regras e `lancamentos` guarda ocorrências materializadas. A melhoria trata somente da orquestração entre esses domínios.

---

## Objetivo

Extrair a orquestração da consulta mensal para um service/caso de uso de aplicação, mantendo o handler responsável por HTTP e os repositórios responsáveis por persistência.

### Entrega desta capacidade

Um fluxo explícito equivalente a `handler → MonthlyEntriesService → EnsureMonth + ListByMonth`, com testes e documentação arquitetural atualizados.

---

## Decisões de produto

- `lancamentos` e `recorrencias` continuam como módulos/domínios distintos.
- A materialização mensal continua idempotente e acontece antes da listagem mensal.
- O service de aplicação coordena o caso de uso; não deve absorver regras de persistência dos repositórios.
- O contrato HTTP existente permanece estável.

---

## Escopo

- Criar uma fronteira de aplicação para consultar lançamentos do mês.
- Injetar as dependências necessárias de recorrências e lançamentos.
- Cobrir o fluxo com testes unitários e de regressão da API.
- Atualizar `docs/arquitetura.md`, `docs/fluxos.md` e os diagramas/fluxos correspondentes no vault.

---

## Fora de escopo

- Alterar tabelas, migrations ou o modelo de dados.
- Alterar o contrato de `GET /api/lancamentos?mes=AAAA-MM`.
- Criar novas frequências de recorrência, faturas, contas fixas ou autenticação.
- Refatorar todos os módulos do backend além do fluxo mensal.

---

## Critérios de aceite

- C1. A consulta mensal passa por um service/caso de uso de aplicação que coordena materialização de recorrências e listagem de lançamentos, sem essa orquestração ficar no handler HTTP. ^c1
- C2. O endpoint `GET /api/lancamentos?mes=AAAA-MM` preserva status, formato de resposta, filtros e validações atuais. ^c2
- C3. A geração mensal mantém idempotência e preserva as regras atuais de ativo, início/fim, vínculo à recorrência e inclusão em fatura. ^c3
- C4. Falhas da materialização ou da listagem continuam sendo propagadas e traduzidas de forma consistente, sem criar resposta de sucesso parcial. ^c4
- C5. A arquitetura, os fluxos e os testes documentam a separação entre handler, service de aplicação, módulos de domínio e repositórios. ^c5

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Nenhuma para iniciar o pacote QA. A escolha do nome concreto do service pertence ao DEV, desde que preserve o contrato e o fluxo documentado.
