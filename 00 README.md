# Operating Vault

> Sistema operacional pessoal para organizar projetos, QA, desenvolvimento, estudos e execução. O vault é multi-projeto; cada produto tem seu próprio contexto e área operacional.

---

## Como usar

| Área | Função |
|---|---|
| [[Dashboard.md\|Dashboard]] | ★ **Central de trabalho** — entrada rápida e visão do fluxo |
| [[01 Board/00 README\|01 Board]] | ★ **Boards por projeto** — Nxgest, SOGOV e visão dinâmica |
| [[01 Board/BOARD Nxgest\|BOARD Nxgest]] | Kanban operacional do Nxgest |
| [[01 Board/BOARD QA — Nxgest\|BOARD QA Nxgest]] | Fila QA do Nxgest |
| [[01 Board/BOARD DEV — Nxgest\|BOARD DEV Nxgest]] | Fila DEV do Nxgest |
| [[01 Board/Fluxo QA DEV.excalidraw\|Fluxo QA ↔ DEV]] | Diagrama visual das dependências entre as camadas |
| [[03 Trabalho/QA/Nxgest/00 README.md\|03 Trabalho/QA/Nxgest]] | **Fonte dos cards** — uma nota por demanda (frontmatter + corpo) |
| [[03 Trabalho/DEV/Nxgest/00 README.md\|03 Trabalho/DEV/Nxgest]] | **Trabalho do DEV** — `Fixes` para bugs e `Execuções` para melhorias |
| [[03 Trabalho/README\|03 Trabalho]] | Índice global de QA e DEV por projeto |
| [[04 Projetos/00 README\|04 Projetos]] | Contexto, repositório, ambientes e decisões por produto |
| [[Sistema/Projetos\|Catálogo de projetos]] | Códigos, destinos e convenções dos projetos |
| [[00 Inbox/Inbox.md\|00 Inbox]] | Captura temporária — linhas soltas que viram card depois |
| [[02 Daily/00 README.md\|02 Daily]] | Notas diárias (espelham o `CHECKLIST.md` do repo) |
| [[05 Arquivo/00 README.md\|05 Arquivo]] | Concluídas/arquivadas |
| [[Skills/BUG.md\|Skills]] | Regras de bug (`BUG`) · melhoria (`MELHORIA`) · casos de teste (`CASOS-DE-TESTE`) · execução (`EXECUCAO`) |
| [[Agentes/PROCESSAR.md\|Agentes]] | QA (`PROCESSAR`: classifica→limpa→roteia→registra) · DEV (`FIXAR`: confirma→planeja→implementa→testa→valida→fecha) |
| [[Templates/00 README.md\|Templates]] | Modelos de card, bug, melhoria, execução, fix e daily |

## Fluxo QA → DEV

1. **QA** — relato/inbox → `PROCESSAR` classifica, limpa e roteia para `03 Trabalho/QA/<projeto>/`. O identificador e o projeto são definidos antes de criar o pacote.
2. **DEV** — `FIXAR` pega o item pronto em `03 Trabalho/DEV/<projeto>/`. Bug exige causa confirmada; melhoria exige decisões, escopo, critérios, CTs e plano técnico definidos.

**Regra universal de templates:** todo artefato deve ser criado copiando o template correspondente em `Templates/` e preenchendo seus placeholders. Isso vale para demandas, bugs, casos de teste, planos, validações, execuções, fixes, code reviews e Dailies. A estrutura não deve ser recriada manualmente.

## Regras

1. **Board = visão**; a fonte é o pacote da demanda dentro de `03 Trabalho/QA/<projeto>/`.
2. **Novo item** nasce no `00 Inbox` → recebe projeto → usa o template → entra no board do projeto ou no board global.
3. **Bug/melhoria/casos/execução** seguem as regras universais de `Skills/`; contexto específico fica em `04 Projetos/<projeto>/`.
4. **✅ Concluído** → move o pacote para `05 Arquivo/<projeto>/` e remove do board.
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
| `execucao` | vínculo com a pasta em `03 Trabalho/DEV/Nxgest` | quando o DEV iniciar |
| `ambiente` | ambiente observado ou validado (`dev`, `hml`, `prod`) | comum |
| `origem` | origem do item (`repo`, `observado`, conversa etc.) | comum |
| `pai` | ID da demanda pai de um defeito | somente filho |
| `data_inicio` / `data_fim` | início e fechamento do ciclo | quando aplicável |
| `responsavel` | pessoa responsável pelo item | quando atribuído |
| `projeto` | código do produto ou contexto (`nxgest`, `sogov` etc.) | obrigatório em novos cards |

Regra: não criar propriedades novas para anotações pontuais. Relações usam `projeto` + IDs estáveis; detalhes pertencem ao corpo do documento.

### Etapas permitidas

`QA · Triagem` · `QA · Análise da demanda` · `QA · Plano de teste` · `QA · Casos de teste` · `DEV · Análise técnica` · `DEV · Plano de execução` · `DEV · Implementação` · `DEV · Code review` · `QA · Validação` · `Concluído`.

## Conteúdo migrado

O conteúdo histórico do Nxgest foi preservado em `03 Trabalho/QA/Nxgest/`, `03 Trabalho/DEV/Nxgest/` e `05 Arquivo/Nxgest/`. SOGOV começa com estrutura vazia e recebe novos cards sem misturar IDs ou histórico.

## Vaults irmãos

- `brainwork` (`~/Documentos/Desenvolvimento/brainwork`) — conhecimento, método, análises e planejamento aprofundado.
