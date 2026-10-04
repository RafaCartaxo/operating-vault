# 03 - Implementação — FIN-MEL-0012

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0012 Recorrências mensais/01 - Demanda|FIN-MEL-0012 — Recorrências mensais sem duplicidade]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0012 Recorrências mensais/04 - Validação dev|Validação QA]]

> Log datado do que foi realmente feito. O plano não é reescrito aqui; desvio vira decisão registrada.

---

## Rodadas

### Rodada 1 — ✅ concluída em 2026-10-04

- Backend: migration 003, entidade/repositório/rotas de recorrências e geração idempotente por competência.
- Backend: ocorrências vinculadas a `recorrencia_id`, `recorrencia_competencia` e marcador explícito `incluida_na_fatura`.
- Frontend: serviços tipados, tela de cadastro/edição/encerramento e navegação de Recorrências.
- Frontend: recorrências incluídas na fatura permanecem visíveis, mas são excluídas do resumo financeiro.
- Arquitetura: documentação de arquitetura, modelo, API e fluxos sincronizada.
- Robustez: migrations executadas instrução a instrução, permitindo reabrir bases que já tenham uma coluna aplicada.

---

## Evidências

- `npm test -- --run`: 23 testes aprovados.
- `npm run build`: TypeScript e bundle Vite aprovados.
- `GOCACHE=/tmp/financas-go-test-cache GOPATH=/tmp/financas-go-test-path go test ./...`: pacotes Go aprovados.
- Gate QA da demanda: validador de pacote QA aprovado.
- Smoke HTTP local não executado neste ambiente: o sandbox recusou abrir socket em `127.0.0.1:3300`; o servidor compilou normalmente.

---

## Testes da implementação

- [x] Unitários da regra alterada (`backend/internal/recorrencias/model_test.go`).
- [x] Testes de validação e resumo (`src/utils/validation.test.ts`, `src/utils/monthlySummary.test.ts`).
- [x] Testes de regressão frontend e backend executados.
- [x] Comandos e limitações registrados nas evidências.

---

## Verificação

- [ ] CTs funcionais da demanda: [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0012 Recorrências mensais/03 - Casos de teste|ver casos de teste]] — aguardando QA.
- [x] Gates aplicáveis do repositório verdes.
- [x] Documentação sincronizada.
- [ ] Commit registrado no README — sem commit solicitado.
