# 04 - Code review (NXG-MEL-0005)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0005/QA/NXG-MEL-0005 Infraestrutura em infra/01 - Demanda|NXG-MEL-0005 — Infraestrutura em infra/]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0005/QA/NXG-MEL-0005 Infraestrutura em infra/04 - Validação dev|Validação QA]]

**Estado:** ✅ revisado (2026-10-17)

---

## Checklist

- [x] O código respeita as convenções reais do repositório (estrutura `infra/` conforme a arquitetura-alvo do NXG-028; `docker compose --project-directory .` é um padrão suportado nativamente pela Compose Specification, não uma gambiarra).
- [x] O diff está limitado ao escopo aprovado — confirmado por `git status -sb`/diff contra o baseline: só os 5 arquivos de infraestrutura (movidos + `name`/`context`/Caddyfile corrigidos) + os 4 arquivos de referência (`scripts/deploy.sh`, `scripts/deploy-staging.sh`, `.opencode/agents/ops-runner.md`, `docs/engineering/06-PRODUCAO.md`) foram tocados.
- [x] O plano foi seguido; **2 desvios registrados em `03 - Implementação.md`** (achado crítico de nome de projeto Compose, corrigido com `name: nxgestao`; achado crítico de carregamento de `.env`, corrigido com `--project-directory .` + ajuste de `build.context`/Caddyfile) — ambos reportados ao Orquestrador como `BLOQUEIO` antes de aplicados, com correção testada isoladamente e autorização explícita recebida para cada um.
- [x] Testes de regressão e gates aplicáveis estão verdes: `docker compose config` válido (exit 0) nos 3 ambientes, na forma final exata usada pelos scripts/documentação.
- [x] Critérios de aceite do pacote QA cobertos: C1 (arquivos em `infra/`, nada na raiz) ✅; C2 (`docker compose config` válido nos 3) ✅; C3 (scripts de deploy apontam para `infra/`) ✅; C4 (`ops-runner.md`/`06-PRODUCAO.md` sem caminho desatualizado) ✅; C5 (nomes reais de volume/rede/container preservados — crítico, só confirmado após a Correção A) ✅; C6 (`.env*.example` continuam na raiz) ✅; C7 (nenhuma mudança prematura/segredo exposto) ✅.
- [x] Documentação sincronizada: `.opencode/agents/ops-runner.md` e `docs/engineering/06-PRODUCAO.md` refletem os novos caminhos (incluindo a correção de contagem: 6 ocorrências reais em `06-PRODUCAO.md`, não 5).
- [x] Não foram introduzidos segredos, dados sensíveis ou dependências desnecessárias — nenhum valor de `.env` foi impresso, registrado ou enviado em nenhum momento; arquivos temporários de config resolvida (que continham segredo em texto plano após a correção funcionar) foram apagados imediatamente após cada inspeção.

---

## Achados

- 2 achados críticos de infraestrutura encontrados e corrigidos durante a própria execução (ver `03 - Implementação.md`, Rodadas 1–3): (1) nome de projeto Compose mudando de `nxgestao` para `infra`, quebrando nomes reais de volume; (2) `.env` real não carregado sem `--project-directory .`, o que impediria o boot em produção (`JWT_SECRET` obrigatório). Ambos corrigidos, testados e revalidados antes de fechar o lote. Nenhum achado remanescente.

---

## Decisão

- [x] Aprovar
- [ ] Solicitar ajustes
