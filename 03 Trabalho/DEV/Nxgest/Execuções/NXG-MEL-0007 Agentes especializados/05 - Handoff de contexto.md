# Handoff de contexto — NXG-MEL-0007

> Documento de recuperação para uma nova sessão do Executor. Não iniciar implementação antes de concluir a pré-condição abaixo.

## Papel

O Executor implementa e registra evidências. O Orquestrador audita, autoriza cada transição e entrega o resultado ao QA. Não presumir autorização por existir uma execução DEV aberta.

## Objetivo vigente

Tornar a governança de agentes do NX Gest independente de plataforma:

```text
AGENTS.md                 contrato global na raiz
agents/
  README.md               índice e regras de uso
  docs-sync.md            contrato neutro de documentação
  ops-runner.md           contrato neutro de operação
  product-planner.md      escrita somente em docs/plans/**
  qa-reviewer.md          somente leitura e revisão
```

Depois da migração, `.opencode/` deve sair completamente do repositório. O README deve apontar para `AGENTS.md` e `agents/README.md`, sem duplicar regras. Não criar adaptadores OpenCode agora.

## Estado obrigatório antes da implementação

O pacote QA do NXG-MEL-0007 foi criado originalmente para `.opencode/agents`, mas esse escopo foi superado. A demanda deve voltar para QA/análise e seus critérios, CTs, plano, épico e boards devem ser atualizados para a arquitetura neutra.

Não emitir `QA_READY_FOR_DEV` nesta etapa. Não criar agentes reais nem executar a implementação antes de um novo gate QA aprovado.

Antes de editar, ler o pacote completo NXG-MEL-0007, NXG-028, NXG-EPIC-0001, templates oficiais, boards Nxgest e toda documentação do repositório que referencia `.opencode/agents`.

Os CTs devem preservar literalmente o template oficial: callouts recolhíveis, todo o conteúdo aninhado com `>`, e âncora fora do callout. Criar/adaptar sempre copiando os templates antes.

Ao finalizar esta fase, executar:

```bash
python3 scripts/validar_pacote_qa.py "03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0007 Agentes especializados"
```

## Critérios do pacote revisado

- `AGENTS.md` permanece na raiz como contrato global.
- `agents/README.md` e os cinco contratos ficam no diretório neutro.
- `product-planner.md` documenta leitura padrão e escrita exclusiva em `docs/plans/**`; não inventar sintaxe de permissão sem fonte confirmada.
- Todos os agentes têm escopo claro e não duplicam o contrato global.
- `.opencode/` e referências ativas a ele são removidos/atualizados sem links quebrados.
- README, AGENTS e documentação de agentes refletem a arquitetura neutra.
- Código, infra, env, deploy e trabalho protegido permanecem intocados.

## Proibições

Não tocar em `src/`, `frontend/`, `infra/`, scripts de deploy, `.env*`, `package.json`, `package-lock.json`, produção, branches ou Git. Não resetar, limpar, stashar, commitar, fazer checkout, merge, pull ou push. Não arquivar NXG-MEL-0007. Não alterar outros projetos, especialmente Finanças Pessoais. Não usar substituição global: o vault possui `FIN-MEL-*` e outros projetos.

O repositório NX Gest tem aproximadamente 27 arquivos modificados e 10 untracked de trabalho protegido, além das mudanças autorizadas dos lotes anteriores. Preservar tudo.

## Resposta inicial exigida do Executor

Antes de qualquer alteração, responder ao Orquestrador com:

```text
STATUS: CONTEXTO_RECEBIDO
ESCOPO_ENTENDIDO: ...
PRECONDICAO: ...
ARQUIVOS_PROIBIDOS: ...
PRIMEIRO_PASSO: ...
PENDENCIAS/DUVIDAS: ...
```

Só depois de nova autorização do Orquestrador iniciar a auditoria do pacote e devolvê-lo ao QA.
