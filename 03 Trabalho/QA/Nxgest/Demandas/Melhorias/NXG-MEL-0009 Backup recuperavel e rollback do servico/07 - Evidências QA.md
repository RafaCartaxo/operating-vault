---
projeto: nxgest
demanda: NXG-MEL-0009
responsavel: NX Gest · QA
data: 2026-11-11
---

# Evidências QA — rodada 1

Base: HEAD c7b65c8 + alterações MEL-0009 e NXG-031 no working tree. Sem commit, push, deploy, VPS, acesso a segredos, Docker daemon, redes ou serviços reais nesta rodada QA. QA confirmou previamente `command -v` e executou sondas nos dublês e guardas de Docker/curl/ssh/scp; logs em `.maestro/nxgest-team/qa/NXG-MEL-0009-VALIDACAO/`.

DEV relatou execução anterior do **CLI Docker real**, em desacordo com a proibição, direcionado a socket inexistente e sem daemon contatado. A fixture posterior foi corrigida; a conformidade desta rodada QA não apaga o desvio histórico. C8/CT-013 permanece bloqueado para a decisão de escopo e aceite do usuário/Coordenação.

- QA independente: `npm run test:backup` 10/10, `npm run test:deploy` 12/12, com guardas de fallback pré-verificadas; sem ocorrência BLOCKED nos logs. A segunda suíte usa preflight dublado; integração com preflight real sob fixture coberta pela primeira.
- Não reexecutei `npm test`, segurança ou build; o DEV relatou 215/215, 9/9 e build, respectivamente. Esses números são evidência DEV, não resultado independente desta rodada.
- Provas específicas: `consistencia-fixture.log` demonstra hash/tar válidos com referência de banco ausente; `preflight-declaracao-fixture.log` registra conteúdo sintético incompatível aceito por atestação; `pull-fixture.log` prova sucesso de copiador legado com SCP dublado falho e zero arquivos.
- O runbook 09 reconhece que hashes e coleta sequencial não provam consistência temporal; o preflight verifica hashes e atestação humana, não o conteúdo nem associação SHA-imagem. `pull-backup.sh` legado e seção 7.1 do guia 08 divergem do novo formato por diretório.

## Evidências por CT

### CT-001 — ✅ Aprovado

Conjunto sintético, hashes e tag dublada; 10/10 suíte backup.

^ev-001

### CT-002 — ✅ Aprovado

Vazio legítimo aceito; acesso recusado.

^ev-002

### CT-003 — 🚫 Bloqueado

Dump/tar e falhas cobertos; falha de escrita/cópia para disco não demonstrada especificamente.

^ev-003

### CT-004 — ✅ Aprovado

Corrupção/mistura de metadados sem ajuste dos hashes recusada; não prova consistência semântica.

^ev-004

### CT-005 — ❌ Falhou

Fixture com referência ausente e tar diferente passa verificação de hashes; teste atual compara conteúdos separadamente sem confronte cruzado. Defeito: NXG-032.

^ev-005

### CT-006 — ✅ Aprovado

Colisão/publicação/interrupção não alteram manifesto do conjunto anterior em fixture; revisão do isolamento.

^ev-006

### CT-007 — ✅ Aprovado

Lock em fixture bloqueia segunda operação; sem daemon.

^ev-007

### CT-008 — ✅ Aprovado

Dublês validam imagem, tag e ausência de prune; disponibilidade real não verificada.

^ev-008

### CT-009 — ❌ Falhou

Prova sintética de schema incompatível, com hash correto e declaração compatible, foi aceita; SHA anterior não é vinculado à imagem pelo gate. Defeito: NXG-033.

^ev-009

### CT-010 — ✅ Aprovado

Escolha application/data e autorização são declarações; nenhuma restauração automática; sem comprovar autorização real.

^ev-010

### CT-011 — 🚫 Bloqueado

Health negativo/timeout e declaração ausente testados; integridade do serviço restaurado e SHA efetivo dependem de atestação, não comprovados.

^ev-011

### CT-012 — ❌ Falhou

Guia 08 ainda orienta pull legado; scp dublado falhou, script retornou zero e sucesso com diretório vazio. Defeito: NXG-034.

^ev-012

### CT-013 — 🚫 Bloqueado

12/12 regressão com interceptação atual; DEV invocou CLI Docker real em tentativa anterior, socket inexistente sem daemon. Não há conformidade retroativa.

^ev-013

### CT-014 — ✅ Aprovado

Documentação separa dublês de restore PostgreSQL real e de go de produção.

^ev-014

## Critérios e limites

| Critério | Situação | Fundamentação |
|---|---|---|
| C1 | Pendente | CT-003: falha específica de escrita/cópia não demonstrada. |
| C2 | Pendente | CT-003; CT-006/007 cobertos sinteticamente. |
| C3 | Falhou | CT-005: relação banco/anexos não demonstrada; NXG-032. |
| C4 | Falhou | CT-009: declaração contraditória e SHA não vinculado; NXG-033. |
| C5 | Aprovado localmente | CT-010: decisão documentada, sem execução automática; não valida autorização real. |
| C6 | Pendente | CT-011 dependente de atestação; CT-012 falhou na alegação de cópia. |
| C7 | Falhou | CT-012: documentação e transporte legado; NXG-034. |
| C8 | Bloqueado | CT-013: regressão atual passou, mas desvio anterior não é retroativamente conforme. |

Resultado: **QA_REJECTED**, 8 aprovados, 3 falharam, 3 bloqueados. Nenhum go de publicação; restauração PostgreSQL real e consistência de produção não foram testadas. Coordenação encaminha correções; QA não despacha DEV.
