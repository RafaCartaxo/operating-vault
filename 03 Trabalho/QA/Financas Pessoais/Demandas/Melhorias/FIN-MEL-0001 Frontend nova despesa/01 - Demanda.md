---
prioridade: media
status: analise
tipo: melhoria
etapa_atual: "QA · Análise da demanda"
modulo: lancamentos
plano: "[[02 - Plano de teste]]"
execucao: "[[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/00 README|FIN-MEL-0001 — DEV]]"
ambiente: dev
origem: conversa
projeto: financas-pessoais
pai: ""
data_inicio: 2026-10-02
pontos_alocados: 6
data_fim: ""
responsavel: ""
---

# FIN-MEL-0001 — Demanda

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/00 README|Execução DEV]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`  
> **Projeto:** `financas-pessoais`

> [!info] Status atual
> **Próximo passo:** revisar o pacote QA e fechar a entrega ao DEV.

---

## Capacidade e esforço

> **Capacidade alocada:** 5 pontos.
>
> O esforço planejado desta melhoria é distribuído entre QA, DEV e validação conforme as etapas forem detalhadas.

## Problema / contexto

O backend de Finanças Pessoais já expõe o cadastro de lançamentos, mas ainda não existe uma interface simples para registrar uma despesa pelo celular ou navegador.

## Objetivo

Disponibilizar a primeira tela de cadastro de despesa, com experiência mobile-first, validação clara e integração com `POST /api/lancamentos`.

### Entrega desta capacidade

Entregar uma tela funcional de nova despesa, responsiva, integrada ao endpoint existente e com estados claros de validação, erro e sucesso.

## Decisões de produto

- O primeiro fluxo prioriza o lançamento rápido de uma despesa simples.
- O backend Go existente é o contrato de integração desta entrega.
- O uso em celular é requisito desde o primeiro incremento.

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

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

## Pendências de decisão

- Confirmar durante a revisão do contrato se conta/carteira e observação fazem parte do payload inicial do endpoint.
