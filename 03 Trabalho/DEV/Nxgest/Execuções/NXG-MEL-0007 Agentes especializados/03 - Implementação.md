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

### Rodada 1 — ⏳

- O que foi implementado.
- Desvio do plano, se houver, e decisão correspondente.

---

## Evidências

- Testes, gates, links de CI, screenshots ou evidência de ambiente.

### Ambiente e smoke check

- **Backend:** `FINANCAS_ADDR=<host>:<porta>`
- **Proxy frontend:** `VITE_API_PROXY_TARGET=http://localhost:<porta>`
- **Frontend:** `:5173`
- **Health check:** `GET http://localhost:<porta>/api/health`
- **Resultado:** registrar resposta e qualquer limitação de ambiente.

> A raiz `/` do backend não é uma página da aplicação; `404 page not found` nela é esperado. O smoke check deve usar `/api/health` ou um endpoint do contrato da demanda.

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
- [ ] Gates aplicáveis do repositório verdes.
- [ ] Documentação sincronizada quando aplicável.
- [ ] Commit registrado no README.
