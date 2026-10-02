# 02 - Plano de execução — FIN-MEL-0002

> [!info]- Navegação QA/DEV
> **README:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0002 Consultar lançamentos do mês/01 - Demanda|FIN-MEL-0002 — Demanda QA]]  
> **Análise:** [[01 - Análise|01 - Análise]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]

> Congelado na aprovação — alterações posteriores devem ser registradas na implementação.

## O quê

Adicionar consulta mensal ao frontend existente, consumindo o GET já disponível e apresentando lista, total de despesas e estados de carregamento, vazio e erro.

## Sequência

- Adicionar tipo e função de listagem no service de lançamentos.
- Cobrir a chamada HTTP com testes unitários.
- Adicionar a seção de consulta mensal na tela React.
- Implementar seletor de mês, carregamento, erro, vazio e retry.
- Calcular e exibir somente o total de despesas.
- Ajustar CSS para celular e desktop.
- Rodar testes, build e smoke no navegador antes do code review.

## Pronto quando

- CT-001 a CT-006 estiverem tecnicamente cobertos.
- `npm test` e `npm run build` passarem.
- A consulta funcionar no endereço local e pelo IP da rede usando HTTP.
- O contrato do backend Go permanecer inalterado.
- A documentação de fluxos refletir o caminho `GET /api/lancamentos?mes=AAAA-MM`.

