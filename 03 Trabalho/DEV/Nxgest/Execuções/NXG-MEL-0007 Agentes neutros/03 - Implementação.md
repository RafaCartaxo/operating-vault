# 03 - Implementação (NXG-MEL-0007)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/01 - Demanda|NXG-MEL-0007 — Agentes especializados]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/04 - Validação dev|Validação QA]]

> Log datado do que foi realmente feito. O plano não é reescrito aqui; desvio vira decisão registrada.

---

## Rodadas

### Rodada 1 — 2026-10-17 — ✅

- Criado `agents/` na raiz do NX Gest com `agents/README.md` (índice) e os 4 contratos neutros: `agents/docs-sync.md`, `agents/ops-runner.md`, `agents/product-planner.md`, `agents/qa-reviewer.md`. Todos em Markdown puro (Identidade/Responsabilidade/Entradas/Saídas/Limites/Regras de segurança/Protocolo de comunicação/Critérios de conclusão), sem frontmatter nem schema de permissão de plataforma.
- `docs-sync.md` e `ops-runner.md` migrados a partir do conteúdo funcional de `.opencode/agents/{docs-sync,ops-runner}.md` (Contexto/Tarefas suportadas/Regras reorganizados na estrutura neutra; `permission` traduzido em regras de texto na seção "Limites").
- `product-planner.md` e `qa-reviewer.md` escritos neutros desde o início (os antigos `.opencode/agents/{product-planner,qa-reviewer}.md`, untracked e nunca aprovados, não foram usados como base funcional — só a descrição de propósito já registrada na demanda).
- `AGENTS.md` (seção "Agentes do projeto", linha 86) atualizado para referenciar `agents/README.md`, sem duplicar o conteúdo dos contratos.
- `README.md` atualizado: árvore de "Estrutura" (linha 21) trocou `.opencode/` por `agents/`; adicionada frase apontando para `AGENTS.md` e `agents/README.md`.
- `docs/skills/SKILL-009-documentation-sync.md` atualizado (2 ocorrências): referência ao agente passou de `.opencode/agents/docs-sync.md` para `agents/docs-sync.md`; o comando `audita-docs (opencode)` foi generalizado para o script direto (`node scripts/audit-docs.mjs` / `npm run docs:audit`).
- `docs/plans/PLAN-084-organizacao-repositorio.md` atualizado: nota datada (17/10/2026) adicionada no início da seção "Classificação do repositório"; linhas de "Permanecem rastreados" e "Devem ser ignorados" que citavam `.opencode/package.json`+lock e `.opencode/agents/**` foram ajustadas para `agents/**`. Os blocos de execução 1–5 (concluídos em 20/08) não foram tocados.
- `.dockerignore` atualizado: removida a entrada `.opencode/node_modules/` (obsoleta após a remoção da pasta).
- `.opencode/` removido por completo (`rm -rf .opencode`): os 2 arquivos rastreados (`agents/docs-sync.md`, `agents/ops-runner.md`, dentro de `.opencode/`) aparecem como deletados no `git status`; os 2 untracked do escopo antigo (`product-planner.md`, `qa-reviewer.md`) e a instalação local do OpenCode (`node_modules/`, `package.json`, `package-lock.json`, `.gitignore` interno) desapareceram sem registro no git (nunca foram rastreados).
- Nenhum desvio do plano. Nenhum arquivo fora do escopo aprovado foi tocado.

---

## Evidências

- `git status -sb` (após a implementação): mostra exatamente `.dockerignore`, `AGENTS.md`, `README.md`, `docs/plans/PLAN-084-organizacao-repositorio.md`, `docs/skills/SKILL-009-documentation-sync.md` como modificados; `.opencode/agents/docs-sync.md` e `.opencode/agents/ops-runner.md` como deletados; `agents/` como novo (untracked). Todos os demais itens (arquivos protegidos de `PLAN-088`/`PLAN-089`, `infra/`, scripts, frontend) permanecem idênticos ao estado anterior a esta execução.
- `git diff --check` → saída vazia, `exit 0` (nenhum erro de espaço em branco).
- `test -d .opencode` → `removido` (diretório não existe mais).
- `ls agents/` → `README.md`, `docs-sync.md`, `ops-runner.md`, `product-planner.md`, `qa-reviewer.md` (5 arquivos).
- Busca por placeholders (`<ID>`, `TODO`, `FIXME`) em `agents/*.md` → nenhuma ocorrência.
- Busca por frontmatter YAML (`---` na primeira linha) em `agents/*.md` → nenhuma ocorrência.
- Busca por `.opencode` em todo o repositório (excluindo `node_modules`/`.git`) → só 3 ocorrências: `docs/UPDATES.md` (histórico, changelog, não editado), `docs/engineering/tasks/2026-08-10/CHECKLIST.md` (checklist datado de uma tarefa já concluída em 10/08, mesma natureza de registro histórico — não editado) e a nota nova adicionada em `docs/plans/PLAN-084-organizacao-repositorio.md` (explica a própria mudança). Nenhuma referência ativa residual.
- `python3 scripts/validar_pacote_qa.py "03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados"` (vault) → `PACOTE QA APROVADO NO GATE DE INTEGRIDADE`.

### Ambiente e smoke check

- Não aplicável — este lote não altera comportamento de código/API (não há backend/frontend a subir ou testar via smoke).

---

## Testes da implementação

- [x] Estrutural: leitura dos 4 contratos + índice — estrutura (Identidade/Responsabilidade/Entradas/Saídas/Limites/Regras de segurança/Protocolo/Conclusão) confirmada, sem frontmatter/schema de plataforma.
- [x] Documentação: busca por referências residuais a `.opencode/agents` — zero ativas (ver Evidências).
- [x] Regressão: `git status -sb` / `git diff --check` — conforme Evidências.

---

## Verificação

- [ ] CTs da demanda relacionados (fonte QA): [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/03 - Casos de teste|ver casos de teste]] — **execução dos CTs é responsabilidade do QA**, não desta implementação.
- [x] Gates aplicáveis do repositório verdes (`git diff --check` limpo; sem gates de build/teste aplicáveis a este lote documental).
- [ ] Documentação sincronizada quando aplicável — `README.md`/`AGENTS.md`/`SKILL-009`/`PLAN-084`/`.dockerignore` sincronizados; `NXG-028`, o épico e os Boards QA/DEV **não** foram sincronizados nesta rodada (fora do escopo explicitamente autorizado — ver ressalva no `DEV_READY_FOR_QA`).
- [x] Commit registrado no README — **não aplicável**: nenhum commit foi criado (nenhum comando `git add`/`commit` foi executado, conforme instrução).
