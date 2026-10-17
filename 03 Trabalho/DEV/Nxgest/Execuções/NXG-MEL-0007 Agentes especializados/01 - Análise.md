# 01 - Análise (NXG-MEL-0007)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/01 - Demanda|NXG-MEL-0007 — Agentes especializados]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados/04 - Validação dev|Validação QA]]

---

## Veredito

A melhoria é viável. O bloqueio de sintaxe de permissão foi resolvido pelo Orquestrador com a documentação oficial do OpenCode.

---

## Fonte oficial da sintaxe (registrado conforme solicitado)

O Orquestrador confirmou, com base na documentação oficial do OpenCode, que:
- `edit:` é a chave que cobre write/edit/apply_patch — **não existe uma chave `write` separada** a inventar. Caminho escopado via objeto: `edit: { "docs/plans/**": "allow", "*": "deny" }`.
- Para `product-planner.md`: `edit` escopado a `docs/plans/**` (allow) e negado para o resto (`*`: deny); `read: allow`; `bash` escopado conforme necessário; `webfetch`/`websearch`: deny.
- Para `qa-reviewer.md`: `edit: deny` (flat, sem escopo — nega tudo) e `read: allow`.

Isso corrige minha inferência anterior (que também cogitava uma chave `write` separada, por analogia com `bash`) — **não implementada**, pois o Orquestrador confirmou que `edit` sozinho já cobre o caso.

---

## O que foi confirmado

- **Auditoria de `AGENTS.md` concluída:** a seção "Agentes do projeto" (linha 84-86) já diz "Subagentes customizados (se existirem) ficam em `.opencode/agents/`. Cada um tem escopo e permissões próprios; todos herdam estas regras." — frase genérica que **não nomeia** `docs-sync` nem `ops-runner` (os 2 agentes já existentes), por desenho. **Não há lacuna objetiva** para descobrir `product-planner`/`qa-reviewer`: a mesma frase genérica já cobre agentes novos, exatamente como já cobre os 2 existentes. **Decisão: não editar `AGENTS.md`** (C5 satisfeito pelo texto já existente).
- `docs-sync.md` e `ops-runner.md` — os únicos 2 exemplos reais no repositório — usam **somente** `edit: deny` / `write: deny` (valor único, sem escopo de caminho). Nenhum dos dois demonstra uma permissão `write`/`edit` restrita a um glob de caminho específico.
- Busca em `.opencode/` (incluindo `node_modules` do próprio OpenCode) não encontrou documentação de schema que confirme se `write`/`edit` aceitam um mapa de glob (como `bash` aceita, ex.: `"git status *": allow`).

---

## Abordagem e riscos

- **Ponto de pausa:** a demanda QA pede explicitamente "`product-planner` somente leitura por padrão e escrita exclusiva em `docs/plans/**`" — isso exige uma sintaxe de permissão escopada por caminho que não tenho como confirmar com os exemplos disponíveis no repositório.
- Risco de **inventar uma sintaxe não suportada**: se eu escrever `write: {"docs/plans/**": allow, "*": deny}` sem confirmação, o OpenCode pode ignorar silenciosamente a estrutura (tratando como `write: ask`/`deny` por padrão, ou lançando erro de parse) — isso violaria o critério C3 (permissões corretamente escopadas) sem que o `validar_pacote_qa.py` ou qualquer auditoria textual consiga detectar, já que o script não valida semântica de permissão do OpenCode, só estrutura do pacote QA.

---

## Alternativas descartadas (por ora)

- Aplicar `write: deny` simples (igual a `qa-reviewer`) para `product-planner` também — descartado por não atender ao requisito explícito de "escrita exclusiva em `docs/plans/**`" (perderia a capacidade de escrever planos, que é o propósito central do agente).
- Aplicar `write: ask` simples (sem escopo de caminho) — mitigaria o risco de escrita indevida (qualquer escrita exigiria confirmação humana), mas não implementaria literalmente "escrita exclusiva em docs/plans/**" como pedido.

---

## Perguntas abertas

- Nenhuma. Sintaxe confirmada pelo Orquestrador com a documentação oficial do OpenCode (ver seção acima).
