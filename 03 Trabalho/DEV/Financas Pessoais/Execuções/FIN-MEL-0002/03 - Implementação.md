# 03 - Implementação — FIN-MEL-0002

> [!info]- Navegação QA/DEV
> **README:** [[00 README|README da execução]]  
> **Análise:** [[01 - Análise|01 - Análise]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0002 Consultar lançamentos do mês/04 - Validação dev|Validação QA]]

## Estado

✅ Implementação concluída — code review aprovado e liberado para QA.

## Registro técnico

- `listLancamentos(month)` foi adicionado ao service frontend.
- `App.tsx` agora consulta o mês atual, permite trocar o mês, exibe lista, total de despesas, vazio, erro e retry.
- O mês inicia no período atual e é selecionado por um botão que abre um painel mensal próprio; não existe campo digitável e o comportamento é consistente entre navegadores.
- Após salvar um lançamento retroativo, o filtro muda automaticamente para o mês da data salva e recarrega a lista.
- A máscara monetária existente foi reaproveitada para exibição dos valores.
- `docs/fluxos.md` e `docs/api.md` foram atualizados com o fluxo GET.
- Backend: sem alteração.

## Verificações

- [x] Testes automatizados: 14 testes frontend aprovados.
- [x] Build frontend aprovado.
- [x] Smoke HTTP backend/frontend aprovado em `127.0.0.1:3000` e `127.0.0.1:5173`.
- [ ] Smoke visual celular pela rede local: aguarda revisão no navegador.
