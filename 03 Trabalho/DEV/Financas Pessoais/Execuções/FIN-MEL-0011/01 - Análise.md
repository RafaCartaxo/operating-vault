# 01 - Análise (FIN-MEL-0011)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0011 Organização navbar mobile/01 - Demanda|FIN-MEL-0011 — Organização da navbar mobile]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0011 Organização navbar mobile/04 - Validação dev|Validação QA]]

---

## Veredito

A melhoria é viável e fica limitada ao componente de navegação do frontend, sem alteração de API, persistência ou regras financeiras.

---

## O que foi confirmado

- `src/App.tsx` possui uma única ação de navegação renderizada manualmente com ícone e texto.
- `src/styles.css` já centraliza a navbar mobile, mas usa dimensões fixas e mantém texto visível.
- O botão flutuante e a ação desktop estão separados e devem permanecer intactos.

---

## Abordagem e riscos

- Transformar os destinos em uma lista renderizável, mantendo o estado `activeView` e adicionando `aria-label`/`title`.
- Usar flexbox para distribuição uniforme sem posições manuais.
- Ocultar apenas o texto visual na navbar mobile; o nome acessível permanece no botão.
- Risco principal: regressão visual desktop ou sobreposição com o FAB; será coberto pelos CTs manuais QA.

---

## Alternativas descartadas

- Posicionamento absoluto por quantidade de itens: descartado por não ser extensível.
- Alteração do backend ou da API: descartada porque está fora do escopo.

---

## Perguntas abertas

- Nenhuma. A implementação seguirá os cinco critérios e CTs do pacote QA.
