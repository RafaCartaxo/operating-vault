# NX Gest — Vault de Trabalho

> Board de tarefas do projeto **NX Gest** (`RafaCartaxo/nxgest`) — inspirado no `brainwork`, focado em **organização de tasks**. O repo continua sendo a fonte de verdade de planos/BRs; este vault é a camada de trabalho.

---

## Como usar

| Área | Função |
|---|---|
| [[Dashboard.md\|Dashboard]] | ★ **Central de trabalho** — entrada rápida e visão do fluxo |
| [[01 Board/BOARD.md\|01 Board — BOARD]] | ★ **Kanban visual** — arraste cards entre as colunas |
| [[01 Board/BOARD QA.md\|BOARD QA]] | Fila operacional das etapas de QA |
| [[01 Board/BOARD DEV.md\|BOARD DEV]] | Fila operacional das etapas de DEV |
| [[01 Board/Fluxo QA DEV.excalidraw\|Fluxo QA ↔ DEV]] | Diagrama visual das dependências entre as camadas |
| [[03 Trabalho QA/00 README.md\|03 Trabalho QA]] | **Fonte dos cards** — uma nota por demanda (frontmatter + corpo) |
| [[04 Trabalho DEV/00 README.md\|04 Trabalho DEV]] | **Trabalho do DEV** — `Fixes` para bugs e `Execuções` para melhorias |
| [[00 Inbox/Inbox.md\|00 Inbox]] | Captura temporária — linhas soltas que viram card depois |
| [[02 Daily/00 README.md\|02 Daily]] | Notas diárias (espelham o `CHECKLIST.md` do repo) |
| [[05 Arquivo/00 README.md\|05 Arquivo]] | Concluídas/arquivadas |
| [[Skills/BUG.md\|Skills]] | Regras de bug (`BUG`) · melhoria (`MELHORIA`) · casos de teste (`CASOS-DE-TESTE`) · execução (`EXECUCAO`) |
| [[Agentes/PROCESSAR.md\|Agentes]] | QA (`PROCESSAR`: classifica→limpa→roteia→registra) · DEV (`FIXAR`: confirma→planeja→implementa→testa→valida→fecha) |
| [[Templates/00 README.md\|Templates]] | Modelos de card, bug, melhoria, execução, fix e daily |

## Fluxo QA → DEV

1. **QA** — relato/inbox → `PROCESSAR` classifica→limpa→roteia. Bug recebe `NXG-NNN` em `03 Trabalho QA/Demandas/Bugs/`; melhoria recebe `MEL-NNNN` em `03 Trabalho QA/Demandas/Melhorias/`. Ambos entram no board; melhoria com decisão pendente permanece em 🔍 Em análise.
2. **DEV** — `FIXAR` pega o item pronto. Bug exige causa confirmada; melhoria exige decisões, escopo, critérios, CTs e `PLAN-NNN` definidos. Cria `04 Trabalho DEV/Fixes/<ID>/` ou `04 Trabalho DEV/Execuções/<ID>/` → implementa → testa → valida → fecha, preservando o ID original.

**Regra universal de templates:** todo artefato deve ser criado copiando o template correspondente em `Templates/` e preenchendo seus placeholders. Isso vale para demandas, bugs, casos de teste, planos, validações, execuções, fixes, code reviews e Dailies. A estrutura não deve ser recriada manualmente.

## Regras

1. **Board = visão** (mexe aqui para mover status). **03 Trabalho QA = fonte** (cada card é uma nota).
2. **Novo item** nasce no `00 Inbox` → destila em `03 Trabalho QA` (usa o template) → aparece no board.
3. **Bug/melhoria/casos/execução** seguem as regras de `Skills/` (BUG · MELHORIA · CASOS-DE-TESTE · EXECUCAO) — adaptadas do `brainwork`, **sem Notion/SGV/Qase** (NXG-NNN/MEL-NNNN + PLAN-NNN + board).
4. **✅ Concluído** → move a nota para `05 Arquivo/` e remove do board.
5. **Status** no frontmatter do card: `backlog · analise · execucao · validacao · concluido` (colunas do board). Catálogo de validação do repo: ✅/🔵/⏳/🚨/❌/🐛/🔁.
6. **Ambiente**: `dev` (local) · `hml` (staging) · `prod`.
7. **Links pro repo**: sempre `docs/plans/PLAN-*.md` etc. — nunca duplicar conteúdo do repo aqui.

## Propriedades dos cards

| Propriedade | Uso | Obrigatoriedade |
|---|---|---|
| `prioridade` | ordenação da demanda | comum |
| `status` | coluna do board (`backlog`, `analise`, `execucao`, `validacao`, `concluido`) | comum |
| `tipo` | natureza do item (`bug`, `melhoria`, `plano`, `demanda`) | comum |
| `etapa_atual` | etapa detalhada com camada (`QA · ...` ou `DEV · ...`) | comum |
| `modulo` | módulo ou área afetada | comum |
| `plano` | vínculo com `PLAN-NNN` do repositório | quando houver plano |
| `execucao` | vínculo com a pasta em `04 Trabalho DEV` | quando o DEV iniciar |
| `ambiente` | ambiente observado ou validado (`dev`, `hml`, `prod`) | comum |
| `origem` | origem do item (`repo`, `observado`, conversa etc.) | comum |
| `pai` | ID da demanda pai de um defeito | somente filho |
| `data_inicio` / `data_fim` | início e fechamento do ciclo | quando aplicável |
| `responsavel` | pessoa responsável pelo item | quando atribuído |

Regra: não criar propriedades novas para anotações pontuais. Relações usam IDs (`MEL-NNNN`, `NXG-NNN`, `PLAN-NNN`); detalhes pertencem ao corpo do documento.

### Etapas permitidas

`QA · Triagem` · `QA · Análise da demanda` · `QA · Plano de teste` · `QA · Casos de teste` · `DEV · Análise técnica` · `DEV · Plano de execução` · `DEV · Implementação` · `DEV · Code review` · `QA · Validação` · `Concluído`.

## Seed (criado em 29/08/2026)

Cards em `03 Trabalho QA/` (NXG-001..027) cobrindo: bugs/dívidas funcionais · planos pendentes · backlog · prod/segurança. Origem marcada no frontmatter (`repo` = documentado no repo; `observado` = reportado na conversa).

## Vaults irmãos

- `brainwork` (`~/Documentos/Desenvolvimento/brainwork`) — QA/Sogov (trabalho). Este vault é separado por ora.
