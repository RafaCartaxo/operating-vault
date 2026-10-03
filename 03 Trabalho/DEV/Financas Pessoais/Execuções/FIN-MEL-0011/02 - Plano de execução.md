# 02 - Plano de execução (FIN-MEL-0011)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0011 Organização navbar mobile/01 - Demanda|FIN-MEL-0011 — Organização da navbar mobile]]  
> **Plano técnico:** não aplicável; mudança limitada ao frontend existente.  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0011 Organização navbar mobile/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Entregar uma navbar mobile extensível, centralizada e acessível, mantendo o FAB e a navegação desktop.

---

## Vínculo e sequência

- Demanda QA: [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0011 Organização navbar mobile/01 - Demanda|FIN-MEL-0011]].
- CTs: [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0011 Organização navbar mobile/03 - Casos de teste|5 CTs]].
- Etapas: adaptar modelo de dados da navbar, ajustar renderização acessível, ajustar CSS responsivo, executar gates e revisar diff.

---

## Escopo aprovado

- Alterar `src/App.tsx` e `src/styles.css`.
- Preservar `src/services`, backend, modal, formulário, FAB e regras financeiras.

---

## Decisões

- Destinos serão definidos em uma lista local e renderizados com `map`, permitindo adicionar/remover itens sem reescrever o layout.
- O texto do destino ficará oculto visualmente apenas no mobile; `aria-label` e `title` manterão a identificação acessível.

---

## Pronto quando

- Critérios C1–C5 da demanda: [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0011 Organização navbar mobile/01 - Demanda|demanda QA]].
- Os 5 CTs do pacote QA estão referenciados no code review.
- `npm test` e `npm run build` passam.

### Testes desta etapa

- **Unitários:** não aplicável; a mudança é de composição/renderização.
- **Formulário/UI:** CTs manuais do pacote QA para 1–5 destinos, acessibilidade e regressão desktop.
- **API/repositório:** não aplicável; backend não será alterado.
- **Gates:** `npm test` e `npm run build`.
