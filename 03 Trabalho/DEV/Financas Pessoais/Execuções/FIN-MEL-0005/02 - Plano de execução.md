# 02 - Plano de execução — FIN-MEL-0005

> [!info]- Navegação QA/DEV
> **README:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0005 Resumo mensal financeiro/01 - Demanda|FIN-MEL-0005 — Demanda QA]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0005 Resumo mensal financeiro/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Exibir receitas, despesas, saldo e quantidade de lançamentos do mês selecionado, mantendo os indicadores sincronizados com a lista consultada.

## Vínculo e sequência

- Fonte de comportamento: pacote QA da FIN-MEL-0005.
- Analisar os componentes atuais de acompanhamento e a função de formatação monetária.
- Criar função pura de agregação dos lançamentos.
- Criar componente visual do resumo.
- Integrar ao fluxo de carregamento, troca de mês, vazio e erro.
- Cobrir com testes unitários e de interface.
- Executar build, auditorias visuais e CTs antes do code review.

## Escopo aprovado

- Frontend: cálculo e apresentação do resumo mensal.
- Testes automatizados relacionados à agregação e renderização.
- Documentação técnica e registros de execução.
- Fora do escopo: novo endpoint, alteração de banco, categorias, parcelas, recorrências e PWA.

## Decisões

- O backend permanece intacto nesta melhoria.
- O resumo consome a mesma coleção de lançamentos exibida na tela.
- Receitas e despesas serão identificadas pelo tipo já persistido.
- O saldo será calculado como receitas menos despesas.

## Pronto quando

- Critérios da demanda [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0005 Resumo mensal financeiro/01 - Demanda#^c1|C1]] a [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0005 Resumo mensal financeiro/01 - Demanda#^c6|C6]] estiverem cobertos.
- Os 13 CTs do pacote QA estiverem executados.
- `npm test`, `npm run build`, `npm run audit:styles` e `npm run audit:ui` estiverem verdes.

### Testes desta etapa

- **Unitários:** soma de receitas, despesas, saldo, quantidade e mês vazio.
- **Formulário/UI:** troca de mês, estados de carregamento/erro e responsividade.
- **Regressão:** listagem mensal e formatação monetária já existentes.
