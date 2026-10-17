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

Criar `.opencode/agents/product-planner.md` e `.opencode/agents/qa-reviewer.md`, com permissões escopadas confirmadas pela documentação oficial do OpenCode, sem editar `AGENTS.md` (auditoria concluiu que não há lacuna objetiva).

---

## Vínculo e sequência

1. Criar `.opencode/agents/product-planner.md`: frontmatter com `description`, `mode: subagent`, `permission` (`edit` escopado a `docs/plans/**`, `read: allow`, `bash` escopado, `webfetch`/`websearch: deny`); corpo com Contexto/Tarefas suportadas/Regras, espelhando `SKILL-003`/`SKILL-004`.
2. Criar `.opencode/agents/qa-reviewer.md`: frontmatter com `edit: deny` (flat), `read: allow`, `bash` escopado para auditorias/testes; corpo espelhando `SKILL-005`/`006`/`007`/`008`.
3. Não editar `AGENTS.md` (decisão já registrada em `01 - Análise.md`).
4. Validar: ausência de placeholders, links internos resolvendo, `git diff --check`, inspeção manual das permissões contra a sintaxe confirmada, e releitura dos CTs do pacote QA um a um contra o resultado real.

---

## Escopo aprovado

- **Pode mudar:** `.opencode/agents/product-planner.md` (novo), `.opencode/agents/qa-reviewer.md` (novo).
- **Deve permanecer intacto:** `AGENTS.md`, `.opencode/agents/{docs-sync,ops-runner}.md`, código em `src/`/`frontend/`, `infra/`, `.env*`, scripts de deploy, e os 27 arquivos modificados + 10 untracked já existentes.

---

## Decisões

- Sintaxe de permissão confirmada pelo Orquestrador com a documentação oficial do OpenCode: `edit` cobre write/edit/apply_patch; caminho escopado via objeto (`{"docs/plans/**": "allow", "*": "deny"}`); nenhuma chave `write` separada.
- `AGENTS.md` não é editado — a frase genérica já existente ("Subagentes customizados... ficam em `.opencode/agents/`") já cobre os novos agentes, sem necessidade de nomeá-los individualmente (mesmo tratamento dado a `docs-sync`/`ops-runner`).

---

## Pronto quando

- Critérios da demanda: [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/01 - Demanda#^c1|C1]] a [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/01 - Demanda#^c7|C7]].
- Os 2 arquivos de agente existem, com permissão sintaticamente correta (conforme a fonte oficial) e sem duplicar `AGENTS.md`/os 2 agentes existentes.
- `git status -sb` mostra apenas os 2 arquivos novos como alteração, sobre o baseline protegido.

### Testes desta etapa

- **Estrutural:** leitura e comparação dos 2 novos arquivos com `docs-sync.md`/`ops-runner.md`.
- **Permissão:** inspeção literal do bloco `permission` de cada agente contra a sintaxe confirmada.
- **Regressão de escopo:** `git status -sb` antes/depois; `git diff --check`.
