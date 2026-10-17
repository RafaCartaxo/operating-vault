# 01 - Análise (NXG-MEL-0007)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0007/QA/NXG-MEL-0007 Agentes especializados/01 - Demanda|NXG-MEL-0007 — Agentes especializados]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0007/QA/NXG-MEL-0007 Agentes especializados/04 - Validação dev|Validação QA]]

---

## Veredito

A melhoria é viável. Diferente da tentativa anterior (escopo OpenCode, hoje obsoleta), esta abordagem não depende de nenhuma sintaxe de permissão específica de plataforma — os 4 contratos são Markdown simples (Identidade/Responsabilidade/Entradas/Saídas/Limites/Regras de segurança/Protocolo de comunicação/Critérios de conclusão), então não há bloqueio de schema a resolver.

---

## O que foi confirmado

- `.opencode/` no repositório contém: `agents/docs-sync.md` e `agents/ops-runner.md` (rastreados pelo git), `agents/product-planner.md` e `agents/qa-reviewer.md` (untracked, escritos na tentativa anterior com schema OpenCode — nunca aprovados, nunca fizeram parte de um `DEV_READY_FOR_QA`), e uma instalação local do próprio OpenCode (`node_modules/`, `package.json`, `package-lock.json`, `.gitignore`) — nenhum desses 4 últimos itens é rastreado pelo git (ignorados pelo próprio `.opencode/.gitignore`).
- Referências ativas confirmadas por busca no repositório: `README.md:21`, `AGENTS.md:86`, `docs/skills/SKILL-009-documentation-sync.md` (menção ao comando `audita-docs (opencode)` e ao agente `.opencode/agents/docs-sync.md`), `docs/plans/PLAN-084-organizacao-repositorio.md` (linhas da seção "Classificação do repositório" que tratam `.opencode/package.json`+lock e `.opencode/agents/**` como rastreados), `.dockerignore:22` (`.opencode/node_modules/`).
- `docs/UPDATES.md` tem 2 menções históricas a `.opencode/agents` (linhas ~333 e ~930) — tratadas como changelog, não editadas.
- `PLAN-084-organizacao-repositorio.md` está com `status: ✅ Concluído` — os blocos de execução (1 a 5) descrevem o que já foi feito em 20/08 e não serão reescritos; apenas a seção "Classificação do repositório" (que é inventário vivo, não um registro de execução) será atualizada, com nota datada da mudança.

---

## Abordagem e riscos

- Migrar `docs-sync.md` e `ops-runner.md` para `agents/`, preservando o conteúdo funcional (Contexto/Tarefas suportadas/Regras → reorganizado em Identidade/Responsabilidade/Entradas/Saídas/Limites/Regras de segurança/Protocolo/Conclusão), removendo o frontmatter YAML e traduzindo os antigos blocos `permission` em regras de texto equivalentes (ex.: "somente leitura" em vez de `edit: deny`).
- Criar `product-planner.md` e `qa-reviewer.md` diretamente neutros — os 2 arquivos antigos (`.opencode/agents/product-planner.md`/`qa-reviewer.md`, untracked, nunca aprovados) não são reaproveitados como base funcional; servem apenas de referência de conteúdo (tarefas suportadas) já que documentam o mesmo propósito de produto/QA.
- `.opencode/` será removido por completo (`agents/`, instalação local do OpenCode e `.gitignore` interno) — é uma remoção física de diretório, sem comando git (os 2 arquivos rastreados aparecerão como deletados no `git status`; os demais, por serem untracked/ignorados, simplesmente deixam de existir sem registro no git).
- Risco mitigado: editar `PLAN-084` (plano concluído) sem descaracterizar seu histórico — resolvido adicionando uma nota datada na seção de classificação, sem tocar nos blocos 1–5 já fechados.
- Risco observado e não resolvido nesta execução (fora do escopo autorizado): o `00 README.md` do pacote QA, `NXG-028`, o épico e os Boards QA/DEV ainda não foram atualizados para refletir este `DEV_READY_FOR_QA` — a demanda (`01 - Demanda.md`) foi atualizada por ser explicitamente parte do escopo autorizado ("atualizar a demanda QA para apontar para esta execução"), mas a sincronização dos demais artefatos de governança depende de nova autorização do Orquestrador.

---

## Alternativas descartadas

- Manter `.opencode/agents/` como "adaptador" apontando para `agents/` — descartado por instrução explícita ("não criar adaptadores OpenCode nesta demanda").
- Manter o frontmatter dos contratos migrados, apenas esvaziando o `permission` — descartado porque o objetivo é remover todo acoplamento de schema de plataforma, não só o conteúdo das permissões.
- Reaproveitar o texto dos `.opencode/agents/product-planner.md`/`qa-reviewer.md` antigos como base literal — descartado porque eles foram escritos com estrutura e linguagem OpenCode-specific (frontmatter, "mode: subagent"); os novos contratos são escritos do zero na estrutura neutra, preservando apenas o propósito/escopo documentado na demanda.

---

## Perguntas abertas

- Nenhuma. Se houver decisão que altere escopo, regra ou aceite, o card volta para análise.
