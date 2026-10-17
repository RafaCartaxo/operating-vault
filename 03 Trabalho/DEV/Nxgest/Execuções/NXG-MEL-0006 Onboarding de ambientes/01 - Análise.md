# 01 - Análise (NXG-MEL-0006)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0006 Onboarding de ambientes/01 - Demanda|NXG-MEL-0006 — Onboarding de ambientes]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0006 Onboarding de ambientes/04 - Validação dev|Validação QA]]

---

## Veredito

A melhoria é viável: `infra/docker-compose.yml` já existe e foi validado (`NXG-MEL-0005`, concluído com ressalva) — encapsular o comando de banco em scripts npm é uma mudança de superfície (package.json + 2 documentos), sem tocar a infraestrutura novamente.

---

## O que foi confirmado

- `infra/docker-compose.yml` já valida com `docker compose --project-directory . -f infra/docker-compose.yml config` (confirmado no `NXG-MEL-0005`) — a forma de invocação a encapsular nos scripts npm é exatamente essa, já testada.
- `README.md` (seção "Instalação Rápida") e `docs/engineering/08-SETUP-NOVA-MAQUINA.md` (Passo 4) são os únicos 2 pontos que documentam o comando de subir o Postgres de dev para o usuário final.
- `package.json` não tem nenhum script `db:*` hoje — não há conflito de nome.
- `scripts/deploy.sh`, `scripts/deploy-staging.sh` e `.opencode/agents/ops-runner.md` já foram tratados no `NXG-MEL-0005` — fora do escopo deste lote.

---

## Abordagem e riscos

- Adicionar `db:up`, `db:down` e `db:ps` ao `package.json`, todos usando `docker compose --project-directory . -f infra/docker-compose.yml ...` — mesma forma já validada no lote anterior.
- Atualizar os 2 documentos para usar os novos comandos no lugar do `docker compose` direto.
- Validar de verdade subindo o Postgres de desenvolvimento local (`npm run db:up`) — ação local, reversível, sem tocar staging/produção nem dado real — e derrubando em seguida (`npm run db:down`), para não deixar efeito colateral persistente além do volume de dev vazio (comportamento normal de qualquer setup local).
- Risco principal: nome de script colidir com algo existente — descartado (confirmado que não há `db:*` hoje).
- Risco secundário: a validação real de "clone limpo" (criar uma pasta nova e clonar de verdade) está fora do alcance seguro desta tarefa (exigiria tocar fora do repositório protegido) — a validação será feita confirmando que o comando funciona a partir do estado atual do repositório, não via clone físico novo.

---

## Alternativas descartadas

- Usar um `Makefile` em vez de scripts npm — descartado por não ser o padrão already estabelecido no projeto (tudo já é `npm run ...`).

---

## Perguntas abertas

- Nenhuma. Nome final dos scripts (`db:up`/`db:down`/`db:ps`) já estava sinalizado como sugestão flexível na demanda QA; mantenho esse nome por ser o mais descritivo e já comunicado ao Orquestrador.
