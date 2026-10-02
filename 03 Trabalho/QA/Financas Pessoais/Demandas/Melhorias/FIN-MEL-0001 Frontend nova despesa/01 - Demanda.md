---
prioridade: media
status: triagem
tipo: melhoria
etapa_atual: "QA · Análise da demanda"
modulo: lancamentos
plano: "[[02 - Plano de teste]]"
execucao: "[[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/00 README|FIN-MEL-0001 — DEV]]"
ambiente: dev
origem: conversa
projeto: financas-pessoais
data_inicio: 2026-10-02
pontos_alocados: 5
---

# FIN-MEL-0001 — Demanda

## Problema / contexto

O backend de Finanças Pessoais já expõe o cadastro de lançamentos, mas ainda não existe uma interface simples para registrar uma despesa pelo celular ou navegador.

## Objetivo

Disponibilizar a primeira tela de cadastro de despesa, com experiência mobile-first, validação clara e integração com `POST /api/lancamentos`.

## Escopo

- Frontend React + Vite + TypeScript.
- Formulário de nova despesa.
- Campos: tipo, descrição, valor, data, conta/carteira e observação quando aplicável ao contrato atual.
- Validação de campos obrigatórios e valor monetário.
- Estados de envio, sucesso e erro.
- Layout responsivo para celular e desktop.

## Fora de escopo

- Parcelamento e recorrência.
- Dashboard e relatórios.
- Autenticação.
- Publicação em produção e PWA completa.
- Exportação para o `financas-vault`.

## Critérios de aceite

- C1. O formulário abre e permanece utilizável em viewport móvel e desktop. ^c1
- C2. Campos obrigatórios e valor/data inválidos impedem o envio e exibem mensagens compreensíveis. ^c2
- C3. Um lançamento válido chama `POST /api/lancamentos` com o contrato documentado. ^c3
- C4. Erros da API são apresentados sem perder silenciosamente os dados preenchidos. ^c4
- C5. Após sucesso, o usuário recebe confirmação clara e o formulário fica pronto para um novo lançamento. ^c5
- C6. O fluxo possui testes básicos e documentação atualizada. ^c6

## Fonte

- Código: `/home/rafacartaxo/Documentos/Desenvolvimento/financas-pessoais`
- API: `/home/rafacartaxo/Documentos/Desenvolvimento/financas-pessoais/docs/api.md`
- Fluxos: `/home/rafacartaxo/Documentos/Desenvolvimento/financas-pessoais/docs/fluxos.md`

## Checklist de entrega ao DEV

- [x] Contexto e objetivo definidos.
- [x] Escopo e fora de escopo registrados.
- [x] Critérios de aceite objetivos e testáveis.
- [ ] Plano e casos de teste revisados.
- [x] Pontos alocados: 5.
