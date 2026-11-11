---
prioridade: alta
status: execucao
tipo: melhoria
etapa_atual: "DEV · Análise técnica"
modulo: infra
plano: ""
execucao: ""
ambiente: dev
origem: repo
projeto: nxgest
epico: ""
pai: ""
data_inicio: 2026-11-10
data_fim: ""
responsavel: "NX Gest · QA"
pontos_alocados: 21
---

# NXG-MEL-0009 — Backup recuperável e rollback do serviço

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** será criada pelo DEV após encaminhamento da Coordenação.

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** `nxgest`.


> [!info] Status atual
> **Próximo passo:** Coordenação recebe QA_REJECTED e encaminha os defeitos filhos ao DEV.

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> **Capacidade de planejamento alocada:** 21 pontos.
> Estimativa de planejamento sujeita ao detalhamento do DEV.
>
> ```dataviewjs
> const id = (dv.current().file.path.match(/(?:[A-Z]{2,8}-)?MEL-\d+/) || [""])[0];
> const paginas = dv.pages().where(p => id && p.file.path.includes(id) && typeof p.pontos === "number");
> const lista = paginas.sort(p => p.file.name);
> const necessario = lista.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> const alocado = Number(dv.current().pontos_alocados || 0);
> const diferenca = alocado - necessario;
> if (lista.length > 0) {
>   dv.table(["Etapa/artefato", "Pontos"], lista.map(p => [p.file.link, p.pontos]));
> } else {
>   dv.paragraph("Nenhum artefato com pontos registrado ainda.");
> }
> dv.paragraph(`**Esforço necessário:** ${necessario} pontos · **Capacidade alocada:** ${alocado} pontos · **${diferenca >= 0 ? "Saldo" : "Déficit"}:** ${Math.abs(diferenca)} pontos`);
> ```

---

## Problema / contexto

A referência local `scripts/backup-nxgest.sh` admite erro na cópia de uploads e fallback para tar vazio; listagem do dump não prova restauração. `scripts/deploy.sh` executa image prune sem demonstrar imagem anterior retida. A proposta de Coordenação aponta ausência de evidência de recuperação integral. Não se afirma que o VPS esteja nessa condição.

---

## Objetivo

Preparar mecanismos e procedimento locais para backup recuperável e rollback de serviço, com comportamento seguro e evidência sintética verificável.

### Entrega desta capacidade

Critérios e 14 CTs, matriz de falhas e evidências para implementação local pelo DEV, seguida de QA independente. A arquitetura é escolha do DEV sujeita aos critérios; não exigir algoritmo específico.

---

## Decisões de produto

- Banco e anexos são requisitos conjuntos; ausência legítima de anexos precisa ser distinguida de erro.
- Imagem, configuração, schema e decisão de dados são pré-condições do rollback de serviço.
- Fixtures e dublês comprovam apenas o comportamento simulado; restore real é pendência operacional separada.
- Não reabrir NXG-031 nem NXG-EPIC-0001.

---

## Escopo

- Diagnóstico e correções necessárias em scripts/testes/runbook de backup e rollback, a definir tecnicamente pelo DEV.
- Conjunto associado e íntegro, parada diante de falhas, preservação de artefatos e imagem, concorrência e efeitos de interrupção.
- Checklist de pré-publicação, decisão sobre dados, saúde, evidências sem segredos e regressão NXG-031.

---

## Fora de escopo

- Commit, push, deploy, SSH, VPS, DNS, Cloudflare, segredos, dados, imagens, volumes, redes e serviços reais.
- Nenhuma chamada a Docker real, mesmo em recursos isolados, nem restauração real PostgreSQL nesta execução. Apenas dublês e fixtures sintéticas sob diretório de teste dedicado.
- Acionar DEV é responsabilidade da Coordenação; Qase externo fora do escopo. Sem alteração da automação de backup Git do vault.

---

## Critérios de aceite

- C1. Backup associa banco, anexos e metadados de execução e informa sucesso apenas quando todos os artefatos obrigatórios foram gerados e sua integridade verificada; ausência legítima de anexos é comprovada e distinta de erro. ^c1
- C2. Falha, corrupção, interrupção ou colisão bloqueia promoção e não sobrescreve nem descarta o último conjunto íntegro; operações concorrentes são serializadas ou recusadas antes de efeitos conflitantes. ^c2
- C3. Um ensaio isolado com dados exclusivamente sintéticos verifica conteúdo restaurado de banco e anexos e consistência do conjunto; dublês são identificados e não são apresentados como prova de restauração PostgreSQL real. ^c3
- C4. O procedimento identifica e preserva imagem anterior e configuração, volumes e bind mounts necessários; imagem, configuração ou compatibilidade de schema/migração não comprovadas bloqueiam rollback de serviço e promoção pertinente. ^c4
- C5. A decisão de reverter apenas aplicação ou restaurar dados é explícita, com pontos de parada, impacto/perda potencial, evidências e autorização operacional; nenhum restore ou comando destrutivo é disparado automaticamente. ^c5
- C6. A sequência de retorno exige verificação de saúde e integridade, registra SHA e artefatos sem segredos, e falha fechada diante de health negativo, dados ausentes ou estado ambíguo. ^c6
- C7. Checklist operacional lista host, checkout, concorrência, envs/Secrets sem valores, backup restaurável, imagem/configuração, schema, domínio/DNS/TLS/e-mail, responsável e gates CI → staging no mesmo SHA → produção, distinguindo preparações locais de verificações reais. ^c7
- C8. A solução preserva as garantias NXG-031 (SHA validado, staging, lock, envs e backup obrigatório), demonstra regressão em testes sintéticos e não modifica nem aciona recursos reais durante esta entrega. ^c8

---

## Checklist de entrega ao DEV

- [x] Contexto, decisões de produto e limites definidos.
- [x] Escopo e fora de escopo delimitados.
- [x] Critérios e matriz de testes vinculados.
- [x] Capacidade alocada como estimativa de planejamento.
- [x] Integridade e sincronização verificadas antes do handoff.

---

## Pendências de decisão

- Sem decisão bloqueante para análise e implementação local. Escolha técnica pertence ao DEV, respeitando critérios.
- Evidência de restauração real, janela, perda de dados aceitável, credenciais, acesso e autorização operacional permanecem pendentes para etapa posterior; não bloqueiam a criação do pacote local.
- Referência: `.maestro/nxgest-team/PROPOSTA-PRE-PUBLICACAO-ROLLBACK.md` e runbook `nxgest/docs/engineering/06-PRODUCAO.md`.

## Histórico e handoff

2026-11-10: QA definiu C1–C8 e CT-001–014, validou integridade e emitiu QA_READY_FOR_DEV. Coordenação encaminha ao DEV; nenhuma implementação ou teste funcional foi aprovado.

## Rodada QA — 2026-11-11

QA_REJECTED: CT-005/009/012 falharam; CT-003/011/013 bloqueados. Consultar [[04 - Validação dev]] e [[07 - Evidências QA]]. Defeitos NXG-032/033/034; Coordenação encaminha. Nenhum recurso real foi tocado nesta rodada QA; o desvio anterior do DEV permanece registrado.

## Preparação dos defeitos filhos — 2026-11-11

NXG-032, NXG-033 e NXG-034 têm gate QA_READY_FOR_DEV com quatro critérios e oito CTs planejados cada. A Coordenação fará o encaminhamento; nenhum CT de correção foi executado. O parecer da rodada pai permanece QA_REJECTED até reteste independente, incluindo CT-003/011 e decisão sobre o histórico de CT-013.
