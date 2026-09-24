---
prioridade: media
status: backlog
# Preencher com o tipo real quando a demanda for criada (bug, melhoria ou outro).
tipo: ""
etapa_atual: "QA · Triagem"
modulo: ""
plano: ""
execucao: ""
ambiente: dev
origem: repo
projeto: ""
pai: ""
data_inicio: ""
data_fim: ""
responsavel: ""
pontos_alocados: ""
---

# <PROJ>-NNN — <título curto da demanda>

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/<projeto>/Execuções/<ID>/00 README|Execução DEV]]

> [!settings]- Controle da demanda
> **Tipo:** `INPUT[inlineSelect(option(bug),option(melhoria),option(plano_tecnico),option(demanda)):tipo]`  
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** preencher `projeto` no frontmatter antes de roteiar o card.

---

## Problema / contexto

Qual dificuldade, necessidade ou decisão originou esta demanda?

---

## Objetivo

Qual resultado observável é esperado?

---

## Capacidade do ciclo

- **Capacidade alocada neste ciclo:** preencher `pontos_alocados`.
- Exemplo: se houver 50 pontos disponíveis no ciclo, usar `pontos_alocados: 50`.

O esforço necessário será calculado pela soma dos pontos das etapas vinculadas à demanda.

---

## Escopo inicial

- O que parece fazer parte desta demanda.

---

## Pendências

- Decisões ou informações que ainda precisam ser esclarecidas.

---

## Critérios de aceite

- C1. Descreva o primeiro comportamento que precisa ser comprovado. ^c1
- C2. Descreva o segundo comportamento que precisa ser comprovado. ^c2

---

## Fonte

- Link no repo, conversa ou nota de origem: ...

---

## Critério de pronto

- [ ] Contexto, objetivo e próximo encaminhamento definidos.

---

## Checklist de entrega ao DEV

- [ ] Decisões e regras de negócio estão fechadas.
- [ ] Escopo e fora de escopo estão claros.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.
