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

### Rodada 2 — ✅ correção A aplicada e confirmada · 🚨 novo achado crítico na mesma revalidação

- **Correção A aplicada** (autorizada pelo Orquestrador): `name: nxgestao` adicionado ao topo dos 3 arquivos `infra/docker-compose.{yml,staging.yml,prod.yml}`.
- **Revalidação dos 3 ambientes** com `docker compose -f infra/docker-compose.{yml,staging.yml,prod.yml} config` — todos exit 0. Confirmado explicitamente: `name: nxgestao` nos 3; `build.context` resolve para a raiz real do repo nos 3; `dockerfile: infra/Dockerfile` nos 3; volumes/rede/containers idênticos aos documentados (`nxgestao_nxgestao_data`, `nxgestao_nxgestao_pgdata`, `nxgestao_nxgestao_staging_data`, `nxgestao_nxgestao_staging_pgdata`, `nxgestao_net`, `nxgest-postgres`, `nxgest-pg-dev`, `staging-app`, `staging-pg`, `nxgestao_caddy_data`, `nxgestao_caddy_config`); Caddyfile resolve para `infra/Caddyfile`. **C5 confirmado.**
- **Novo achado crítico (desvio do plano):** ao inspecionar o `stderr` da validação de `prod` para confirmar ausência de exposição de segredo, constatei que `JWT_SECRET` e `GITHUB_TOKEN` — que **existem de verdade** no `.env` real da raiz — apareceram como `"variable is not set. Defaulting to a blank string"`. Isso prova que o Compose **não está lendo o `.env` da raiz** quando o arquivo compose vive em `infra/` e é invocado sem flag adicional — o carregamento automático de `.env` segue o diretório do **arquivo compose** (`infra/`, sem `.env` lá dentro), não o `cwd` de quem invoca. Essa premissa (".env não precisa mudar de lugar porque o compose lê do cwd") estava **errada** e já tinha sido usada para justificar o critério C6 do pacote QA.
  - **Impacto se aplicado de verdade:** `JWT_SECRET`, `PG_PASSWORD`, `ADMIN_DEFAULT_PASSWORD` etc. subiriam **vazios** em produção/staging. Por regra do próprio `AGENTS.md` ("`JWT_SECRET` é obrigatório em produção — app falha ao iniciar sem ele"), a aplicação **não subiria** após um deploy real nesse estado.
  - **Correção testada (não aplicada ainda):** `docker compose --project-directory . -f infra/docker-compose.prod.yml config` — com a flag, `JWT_SECRET`/`GITHUB_TOKEN` deixam de aparecer como "not set" (confirmado só pela ausência do warning no stderr; o valor em si nunca foi impresso nem registrado, por segurança). Testado em combinação com o `name: nxgestao` já aplicado — nome do projeto e nomes de volume/rede/container continuam corretos com as duas coisas juntas.
  - **Arquivos que precisariam da flag** `--project-directory .` ao lado de cada `-f infra/docker-compose.*.yml`: `scripts/deploy.sh` (2×), `scripts/deploy-staging.sh` (1×), `.opencode/agents/ops-runner.md` (2×), `docs/engineering/06-PRODUCAO.md` (5×) — os mesmos 4 arquivos já tocados nesta rodada, nenhum arquivo novo.
- **Segurança:** os arquivos temporários gerados pela validação (`docker compose config` resolvido, que pode conter segredo em texto plano quando a flag funciona) foram apagados imediatamente após a inspeção; nenhum valor de segredo foi impresso, registrado ou enviado em nenhum momento — só a ausência/presença do aviso "not set" foi usada como evidência.
- **Decisão:** não declarar `DEV_READY_FOR_QA` com essa lacuna aberta — é uma falha funcional (app não sobe), não cosmética. `BLOQUEIO PARA O ORQUESTRADOR` enviado com a correção já testada, aguardando autorização.

### Rodada 3 — ✅ Correção B aplicada · achado adicional de interação corrigido na mesma rodada · todos os checks passaram

- **Correção B aplicada** (autorizada): `--project-directory .` adicionado a cada invocação `docker compose -f infra/docker-compose.*.yml` em `scripts/deploy.sh` (2×), `scripts/deploy-staging.sh` (1×, via variável `$COMPOSE`) e `.opencode/agents/ops-runner.md` (2×, dentro do `ssh ... 'cd /opt/nxgestao && ...'`). Em `docs/engineering/06-PRODUCAO.md`, usei `--project-directory .` nos 2 pontos que descrevem passos internos do `deploy.sh` e `--project-directory /opt/nxgestao` (absoluto) nos 4 pontos que são comandos avulsos sem `cd` garantido antes (tabela de logs/status + rollback Opção 2) — **total real: 6 ocorrências em 06-PRODUCAO.md, não 5 como eu havia contado antes** (correção de contagem registrada; apliquei em todas as 6, não só 5).
- **Achado adicional de interação, encontrado e corrigido nesta mesma rodada, antes de reportar:** ao revalidar com a forma final (`--project-directory .`), o `build.context: ..` passou a resolver para `/home/.../Desenvolvimento` (um nível ACIMA do repositório) em vez da raiz — porque `--project-directory` muda a base de resolução de TODOS os caminhos relativos do compose (não só do `.env`), incluindo `build.context` e o volume do Caddyfile. Mesma causa, mesmo mecanismo do achado anterior, mas afetando dois campos diferentes.
  - **Corrigido:** `build.context: ..` → `build.context: .` nos 3 compose (agora relativo a `--project-directory .` = raiz real). Volume do Caddyfile em `docker-compose.prod.yml`: `./Caddyfile` → `./infra/Caddyfile` (agora relativo à mesma base).
  - **Testado isoladamente antes de aplicar** (arquivo temporário, nunca nos arquivos reais) e depois aplicado + revalidado do zero nos 3 ambientes.
- **Revalidação final (forma exatamente igual à usada pelos scripts/documentação em produção real):**
  - `docker compose --project-directory . -f infra/docker-compose.yml config` → exit 0.
  - `docker compose --project-directory . -f infra/docker-compose.staging.yml config` → exit 0.
  - `docker compose --project-directory . -f infra/docker-compose.prod.yml config` → exit 0.
  - **Project name:** `nxgestao` nos 3.
  - **Build context:** `/home/rafacartaxo/Documentos/Desenvolvimento/nxgestao` (raiz real) nos 3; `dockerfile: infra/Dockerfile` nos 3.
  - **Volumes/rede/containers:** `nxgestao_nxgestao_data`, `nxgestao_nxgestao_pgdata` (dev e prod) · `nxgestao_nxgestao_staging_data`, `nxgestao_nxgestao_staging_pgdata` (staging) · `nxgestao_net` (staging+prod) · `nxgest-postgres`, `nxgest-pg-dev`, `staging-app`, `staging-pg` · `nxgestao_caddy_data`, `nxgestao_caddy_config` — todos idênticos ao documentado em `docs/STATUS.md`.
  - **Caddyfile:** resolve para `infra/Caddyfile`.
  - **Segredos:** `JWT_SECRET` e `GITHUB_TOKEN` (reais, definidos no `.env` da raiz) **não aparecem mais** como "not set" — confirmado SOMENTE pela ausência do aviso no stderr, nunca pelo valor. As demais variáveis (`PG_USER`, `PG_PASSWORD`, `CORS_ORIGIN`, `DOMAIN`, etc.) continuam "not set" porque o `.env` LOCAL de desenvolvimento genuinamente não as define (são variáveis de staging/produção) — isso é esperado e não é uma falha; em um `.env`/`.env.staging` real de staging/produção, essas variáveis estariam definidas.
  - Todos os arquivos temporários com config resolvida (que, com os segredos carregados corretamente, continham `JWT_SECRET`/`GITHUB_TOKEN` em texto plano) foram apagados imediatamente após cada inspeção. Nenhum valor de segredo foi impresso, registrado neste documento ou enviado em qualquer mensagem.
- **Escopo final tocado:** os mesmos 4 arquivos de referência (nenhum arquivo novo) + os 3 compose em `infra/` (já tocados no Lote 1, agora com `name:` + `context` + Caddyfile corrigidos). Os 27 arquivos modificados + 10 untracked protegidos permanecem intactos (confirmado por diff).
- **Decisão:** todos os critérios técnicos (C1–C7) estão satisfeitos. Nenhum deploy real foi executado. `NXG-MEL-0006` continua não iniciado. Pronto para code review e `DEV_READY_FOR_QA`.

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
