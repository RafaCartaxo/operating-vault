# 02 - Plano de execução (NXG-MEL-0007)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/01 - Demanda|NXG-MEL-0007 — Agentes especializados]]  
> **Plano técnico:** não se aplica — lote de organização, sem `PLAN-NNN` próprio  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Criar `agents/` na raiz do repositório como fonte canônica neutra de contratos de agente (`agents/README.md` + `docs-sync.md` + `ops-runner.md` + `product-planner.md` + `qa-reviewer.md`, todos sem frontmatter/schema de plataforma), atualizar `AGENTS.md`, `README.md`, `docs/skills/SKILL-009-documentation-sync.md`, `docs/plans/PLAN-084-organizacao-repositorio.md` e `.dockerignore` para refletir a nova fonte, e remover `.opencode/` do repositório por completo.

---

## Vínculo e sequência

1. Criar `agents/README.md` (índice e regras de uso dos 4 contratos).
2. Migrar `.opencode/agents/docs-sync.md` → `agents/docs-sync.md` (neutro).
3. Migrar `.opencode/agents/ops-runner.md` → `agents/ops-runner.md` (neutro).
4. Criar `agents/product-planner.md` (neutro, escrita documentada como exclusiva de `docs/plans/**`).
5. Criar `agents/qa-reviewer.md` (neutro, documentado como somente leitura).
6. Atualizar `AGENTS.md` (seção "Agentes do projeto") para referenciar `agents/README.md`, sem duplicar o conteúdo dos contratos.
7. Atualizar `README.md` (árvore de "Estrutura" + referência a `AGENTS.md`/`agents/README.md`).
8. Atualizar `docs/skills/SKILL-009-documentation-sync.md` (referências ao agente `docs-sync`).
9. Atualizar `docs/plans/PLAN-084-organizacao-repositorio.md` (seção "Classificação do repositório" — nota datada, sem reescrever os blocos 1–5 já concluídos).
10. Atualizar `.dockerignore` (remover a entrada `.opencode/node_modules/`, obsoleta após a remoção da pasta).
11. Remover `.opencode/` por completo (os 2 arquivos rastreados + os 2 untracked do escopo antigo + a instalação local do OpenCode, não rastreada).
12. Validar: `git status -sb`, `git diff --check`, busca por referências residuais a `.opencode/agents`, placeholders nos 4 contratos, links internos do pacote QA, e confirmação de que nenhum arquivo protegido foi tocado.

---

## Escopo aprovado

- **Pode mudar:** `agents/README.md` (novo), `agents/docs-sync.md` (novo), `agents/ops-runner.md` (novo), `agents/product-planner.md` (novo), `agents/qa-reviewer.md` (novo), `AGENTS.md`, `README.md`, `docs/skills/SKILL-009-documentation-sync.md`, `docs/plans/PLAN-084-organizacao-repositorio.md`, `.dockerignore`; remoção completa de `.opencode/**`.
- **Deve permanecer intacto:** `src/`, `frontend/`, `infra/`, scripts de deploy, `.env*`, `package.json`/`package-lock.json` da raiz do repositório, Docker, produção, branches, `docs/UPDATES.md` (histórico), e todo o trabalho protegido em andamento (arquivos modificados/untracked de `PLAN-088`/`PLAN-089` e demais lotes anteriores).

---

## Decisões

- Os contratos neutros descrevem permissão como regra textual na seção "Limites" (ex.: "somente leitura", "escrita exclusiva em `docs/plans/**`"), nunca como schema de permissão de uma plataforma (`mode`, `permission`, frontmatter YAML).
- `AGENTS.md` não duplica o conteúdo dos agentes — só referencia `agents/README.md` como índice.
- `README.md` aponta para `AGENTS.md` (contrato global) e `agents/README.md` (contratos específicos).
- `PLAN-084-organizacao-repositorio.md` recebe uma nota datada de atualização na seção "Classificação do repositório", sem reescrever os blocos de execução 1–5 já concluídos em 20/08.
- Nenhum adaptador específico de plataforma (OpenCode ou outra) é criado nesta demanda.
- `.opencode/` é removido por completo nesta execução, já autorizado pelo Orquestrador após a migração do conteúdo útil.

---

## Pronto quando

- Critérios da demanda: [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/01 - Demanda#^c1|C1]] a [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/01 - Demanda#^c7|C7]].
- `agents/README.md` e os 4 contratos existem, neutros, sem frontmatter/schema de plataforma.
- `AGENTS.md` e `README.md` apontam para `agents/`.
- `.opencode/` foi removido; nenhuma referência ativa residual a `.opencode/agents` permanece (exceto `docs/UPDATES.md`, histórico).
- `git status -sb` mostra apenas os arquivos do escopo aprovado como alterados; nenhum arquivo protegido tocado.

### Testes desta etapa

- **Estrutural:** leitura dos 4 contratos + `agents/README.md`, confirmando a estrutura (Identidade/Responsabilidade/Entradas/Saídas/Limites/Regras de segurança/Protocolo/Conclusão) e ausência de frontmatter/schema de plataforma.
- **Documentação:** busca por `.opencode/agents` no repositório, confirmando zero referências ativas residuais (exceto `docs/UPDATES.md`).
- **Regressão:** `git status -sb` antes/depois; `git diff --check`; confirmação de que nenhum arquivo protegido (`src/`, `frontend/`, `infra/`, `.env*`, scripts de deploy, trabalho de `PLAN-088`/`PLAN-089`) foi alterado.
