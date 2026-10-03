# 01 - Análise (FIN-MEL-0009)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0009 Navegação lançamento modal/01 - Demanda|FIN-MEL-0009 — Navegação do lançamento por modal]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0009 Navegação lançamento modal/04 - Validação dev|Validação QA]]

---

## Veredito

Melhoria viável como refatoração frontend, reutilizando o formulário e os serviços atuais, com alteração controlada do ponto de entrada e do container visual.

---

## O que foi confirmado

- A FIN-MEL-0006 já separa Lançamentos e Acompanhamento.
- O formulário atual concentra criação, validações, máscara monetária, data e parcelamento.
- O Acompanhamento já possui filtros e ações de edição/exclusão que precisam permanecer acessíveis.
- O estado atual renderiza o formulário e o Acompanhamento de forma condicional por `activeView`; a mudança deve transformar o formulário em conteúdo reutilizável dentro de um modal.

---

## Abordagem e riscos

- Não há mudança prevista no contrato da API ou banco.
- O modal deve ter estado de abertura, fechamento, submissão, sucesso e erro.
- Mobile usa bottom sheet com rolagem interna; desktop usa modal centralizado.
- O botão é flutuante no mobile e ação visível no cabeçalho no desktop.
- O foco deve retornar ao botão ao fechar, quando tecnicamente aplicável.
- Não há necessidade de alterar Go, SQLite ou os serviços HTTP.

---

## Alternativas descartadas

- Manter uma página exclusiva de lançamento: descartada por adicionar navegação desnecessária no mobile.
- Duplicar o formulário dentro do modal: descartado para evitar divergência de validações.

---

## Perguntas abertas

- Nenhuma. Se o layout aprovado mudar, registrar decisão antes da implementação.

## Arquivos previstos

- `src/App.tsx`: estado do modal, ação de adicionar, renderização do formulário e integração com os estados atuais.
- `src/styles.css`: modal/bottom sheet, backdrop, botão de adicionar e regras de viewport/safe area.
- `src/App.test.tsx` (a criar, se a infraestrutura de UI for introduzida): abertura, fechamento e submissão sem duplicidade.
