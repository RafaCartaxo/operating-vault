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

### Rodada 1 — 🚨 bloqueada (achado crítico na validação)

- Implementado conforme o plano: `mv` dos 5 arquivos para `infra/`; `build.context: ..` + `build.dockerfile: infra/Dockerfile` nos 3 compose; `scripts/deploy.sh` (2 ocorrências), `scripts/deploy-staging.sh` (1), `.opencode/agents/ops-runner.md` (2) e `docs/engineering/06-PRODUCAO.md` (5) atualizados para `infra/docker-compose.*.yml`.
- **Desvio do plano — achado crítico:** `docker compose -f infra/docker-compose.prod.yml config` (C2) passou sintaticamente (exit 0), mas o `build.context` resolvido mostrou corretamente a raiz do repo — **porém o nome do projeto Compose, que por padrão é o basename do diretório do arquivo compose (não do `cwd` de invocação), mudou de `nxgestao` para `infra`**. Isso faz os volumes nomeados (`nxgestao_data`, `nxgestao_pgdata`) resolverem para `infra_nxgestao_data`/`infra_nxgestao_pgdata` em vez dos nomes reais documentados em produção (`nxgestao_nxgestao_data`, confirmado em `docs/STATUS.md`). **Isso violaria o critério C5** (nomes reais de infraestrutura preservados) e, se aplicado de verdade, faria o próximo `docker compose up` em produção criar volumes novos vazios, órfãos do banco real.
- **Correção testada (não aplicada ainda, aguardando autorização):** adicionar `name: nxgestao` (chave de topo, suportada pela Compose Specification) aos 3 arquivos compose. Testado com `COMPOSE_PROJECT_NAME=nxgestao docker compose -f infra/docker-compose.prod.yml config` — restaura exatamente `nxgestao_net`, `nxgestao_nxgestao_data`, `nxgestao_nxgestao_pgdata`, idêntico ao documentado em produção.
- **Decisão:** parar aqui, não prosseguir para `NXG-MEL-0006`, e reportar ao Orquestrador para autorizar a correção antes de fechar este lote — conforme a regra "pare antes do lote 6 e informe" se a validação do lote 5 falhar.

### Rodada 2 — ⏳ aguardando autorização da correção

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
