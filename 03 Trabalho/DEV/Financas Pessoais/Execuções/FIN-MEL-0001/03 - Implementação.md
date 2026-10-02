# 03 - Implementação — FIN-MEL-0001

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/01 - Demanda|FIN-MEL-0001 — Demanda QA]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/04 - Validação dev|Validação QA]]

> Log datado do que foi realmente feito. O plano não é reescrito aqui; desvio vira decisão registrada.

---

## Rodadas

### Rodada 1 — ✅

- Criado frontend React + Vite + TypeScript na raiz do projeto.
- Criada tela responsiva de nova despesa, com tipo, descrição, valor e data.
- Criada camada `src/services/lancamentos.ts` para o `POST /api/lancamentos`.
- Implementada conversão de valor monetário para centavos e tratamento de erros `422`.
- Adicionado teste automatizado do service da API.

---

## Evidências

- `npm test`: 2 testes aprovados.
- `npm run build`: concluído com sucesso.
- `GOCACHE=/tmp/financas-go-build GOPATH=/tmp/financas-go-path go test ./...`: backend aprovado.
- Smoke test manual pelo navegador: validação vazia exibiu erro; lançamento sintético de `R$ 12,34` retornou sucesso via backend Go.
- Verificação em viewport móvel de `390x844`: layout e campos acessíveis.

---

## Testes da implementação

- [x] Unitários do service em `src/services/lancamentos.test.ts`.
- [x] Testes de formulário/UI manual.
- [x] Teste de API/repositório via `POST /api/lancamentos`.
- [x] Testes de regressão relacionados à demanda.
- [x] Registrar os caminhos dos arquivos de teste e o comando executado: `npm test` e `npm run build`.

---

## Verificação

- [ ] CTs da demanda relacionados (fonte QA): [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0001 Frontend nova despesa/03 - Casos de teste|ver casos de teste]].
- [x] Gates aplicáveis do repositório verdes.
- [x] Documentação sincronizada: `docs/fluxos.md`.
- [ ] Commit registrado no README.
