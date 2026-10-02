---
prioridade: media
status: concluido
tipo: melhoria
etapa_atual: "Concluído"
modulo: frontend
plano: "[[02 - Plano de teste]]"
execucao: "[[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0004/00 README|Execução DEV]]"
ambiente: dev
origem: observado
projeto: financas-pessoais
pai: ""
data_inicio: 2026-10-02
data_fim: ""
responsavel: ""
pontos_alocados: 3
---

# FIN-MEL-0004 — Refinamentos responsivos dos campos

> [!info]- Navegação QA/DEV
> **README:** [[00 README]]  
> **Plano:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0004/00 README|Execução DEV]]

## Problema / contexto

Foram identificados ajustes de usabilidade em telas pequenas: o campo de data pode ultrapassar o container no iPhone, o reset do filtro pode desalinhaar no mobile e a primeira digitação do valor pode reposicionar o cursor de forma confusa.

## Objetivo

Garantir que os campos de data, filtro mensal e valor sejam previsíveis e utilizáveis em iPhone e Android.

## Escopo

- Campo de data contido no container em iPhone Chrome.
- Campo de data contido no container em Android Chrome.
- Botão de reset alinhado ao seletor mensal.
- Primeiro dígito monetário permanece no cursor esperado.
- Máscara inicia visualmente em R$ 0,00.
- Regressão em desktop.

## Fora de escopo

- Alteração do contrato da API.
- Novo calendário de negócio.
- Mudança das regras de centavos.
- PWA ou instalação do aplicativo.

## Critérios de aceite

- C1. Campo de data cabe no container em iPhone mobile. ^c1
- C2. Campo de data cabe no container em Android mobile. ^c2
- C3. Reset do filtro fica alinhado ao seletor mensal. ^c3
- C4. Primeiro dígito do valor mantém o cursor correto. ^c4
- C5. Estado visual inicial do valor é R$ 0,00. ^c5
- C6. Layout permanece correto em desktop. ^c6
- C7. Tocar nos campos no iPhone não causa zoom automático da página. ^c7

## Checklist de entrega ao DEV

- [x] Problema e objetivo definidos.
- [x] Escopo e fora de escopo definidos.
- [x] Critérios testáveis.
- [ ] Plano e CTs aprovados.
