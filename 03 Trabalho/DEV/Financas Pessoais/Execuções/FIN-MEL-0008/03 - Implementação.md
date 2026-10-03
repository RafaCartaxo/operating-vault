# 03 - Implementação (<ID>)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[03 Trabalho/DEV/<projeto>/Execuções/<ID>/00 README|README da execução]]  
> **Demanda QA:** [[<DEMANDA>|<ID> — <título da demanda>]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[<VALIDACAO>|Validação QA]]

> Log datado do que foi realmente feito. O plano não é reescrito aqui; desvio vira decisão registrada.

---

## Rodadas

### Rodada 1 — ✅ concluída (2026-10-03)

- Adicionado vínculo de série no modelo e migration SQLite idempotente.
- Implementada criação transacional de parcelas com distribuição em centavos.
- Implementado ajuste de datas para o último dia do mês.
- Adicionados endpoints para criar, editar e excluir séries.
- Formulário React permite informar quantidade de parcelas e histórico exibe posição/total.
- Lançamentos simples permanecem no fluxo existente.
- Smoke API aprovado: R$ 100,00 em 3 parcelas gerou 3333, 3333 e 3334 centavos, nas datas 2026-01-31, 2026-02-28 e 2026-03-31.

---

## Evidências

- Testes, gates, links de CI, screenshots ou evidência de ambiente.

- Backend: go test ./... aprovado.
- Frontend: npm test com 20 testes e npm run build aprovados.

---

## Testes da implementação

- [ ] Unitários da regra/serviço alterado.
- [ ] Testes de formulário/UI, quando houver interação.
- [ ] Testes de API/repositório, quando houver contrato ou persistência.
- [ ] Testes de regressão relacionados à demanda.
- [ ] Registrar os caminhos dos arquivos de teste e o comando executado.

---

## Verificação

- [ ] CTs da demanda relacionados (fonte QA): [[03 Trabalho/QA/<projeto>/Demandas/<tipo>/<ID>/03 - Casos de teste|ver casos de teste]].
- [x] Gates aplicáveis do repositório verdes.
- [ ] Documentação sincronizada quando aplicável.
- [ ] Commit registrado no README.
