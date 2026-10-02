# 01 - Análise — FIN-MEL-0001

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/01 - Demanda|FIN-MEL-0001 — Cadastro mobile de nova despesa]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/04 - Validação dev|Validação QA]]

---

## Veredito

A melhoria é viável: o frontend React + Vite + TypeScript pode consumir o contrato HTTP existente do backend Go, desde que o valor seja convertido para centavos e as regras definitivas permaneçam no backend.

---

## O que foi confirmado

- O backend expõe `POST /api/lancamentos` e aceita `tipo`, `descricao`, `valorCentavos` e `data`.
- `tipo` deve ser `receita` ou `despesa`.
- `valorCentavos` deve ser inteiro positivo; a interface deve converter o valor monetário antes do envio.
- `data` deve ser enviada no formato `AAAA-MM-DD`.
- Respostas de sucesso usam `201`; erros de validação usam `422` com o campo `erro`.
- O backend Go já possui testes automatizados e smoke test; o frontend ainda não existe.
- A demanda QA cobre responsividade, validação, integração, erro, sucesso e regressão.

---

## Abordagem e riscos

- Criar o frontend em React + TypeScript + Vite, mantendo o stack já conhecido no NX Gest.
- Centralizar chamadas HTTP em um service da API, sem espalhar `fetch` pelos componentes.
- Usar formulário mobile-first com estados explícitos de edição, envio, sucesso e erro.
- Converter o valor para centavos de forma determinística antes do POST, evitando cálculo financeiro com ponto flutuante no backend.
- Não duplicar regras financeiras no frontend; a validação definitiva continua no Go.
- Configurar a origem da API por ambiente, permitindo uso local e futura publicação por URL HTTPS.
- Risco principal: divergência entre campos exibidos e o contrato real; mitigação: teste de integração e CT-001/CT-004.

---

## Alternativas descartadas

- **Svelte:** tecnicamente viável, mas reduziria o reaproveitamento do stack React já conhecido.
- **Regras de parcelas nesta primeira tela:** estão fora do escopo da demanda e aumentariam o risco do primeiro fluxo.
- **Dashboard antes do cadastro:** não valida o fluxo principal de entrada de dados.
- **Chamadas HTTP diretamente nos componentes:** dificultariam testes e futura evolução do frontend.
- **Modal como primeira tela:** a página dedicada favorece uso por URL no celular e permite evoluir para PWA sem acoplamento inicial.

---

## Perguntas abertas

- Nenhuma. A primeira entrega será uma página dedicada de nova despesa, com integração ao contrato atual e sem parcelamento ou recorrência.
