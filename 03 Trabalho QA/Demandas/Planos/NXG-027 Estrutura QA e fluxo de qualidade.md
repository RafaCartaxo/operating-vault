---
prioridade: alta
status: analise
modulo: processo
plano: ""
execucao: ""
ambiente: dev
origem: observado
pai: ""
data_inicio: "2026-09-09"
data_fim: ""
responsavel: ""
---
# NXG-027 — Estrutura QA e fluxo de qualidade do vault

> [!info] Informações
> - **Tipo:** Plano de organização/processo
> - **Responsável:**
> - **Plano técnico relacionado:** não se aplica; este plano organiza o vault e o processo de trabalho

---

## Problema / contexto

O vault já possui templates de bug, melhoria, casos de teste, fix e daily, mas ainda não separa claramente o trabalho de QA antes do desenvolvimento, o trabalho de DEV durante a implementação, os tipos de teste e seus níveis de automação, nem a diferença entre caso de teste, plano de testes e evidência de validação.

Também havia dois diretórios principais numerados como 04, criando ambiguidade entre correção de bug e implementação de melhoria.

## Objetivo

Estabelecer uma estrutura simples e rastreável para QA e DEV, aplicando Shift-left: cada demanda deve chegar ao desenvolvimento com contexto, risco, escopo, critérios de aceite e cobertura de testes suficientes para começar.

## Decisões de organização

- 03 Trabalho QA representa preparação, triagem, refinamento, planejamento e validação de qualidade.
- 04 Trabalho DEV representa implementação, dividido em Fixes (bugs) e Execuções (melhorias).
- 05 Arquivo é o destino final do card e dos registros concluídos.
- NXG-NNN identifica bugs e planos de trabalho existentes; MEL-NNNN identifica melhorias; nenhum ID é renomeado.
- O card é a fonte da intenção, regras, critérios e CTs. O repositório é a fonte do código e dos planos técnicos PLAN-NNN.
- Nenhuma camada de teste é criada apenas por existir como boa prática. Cada demanda declara as camadas aplicáveis e justifica as não aplicáveis.

## Estrutura-alvo

    00 Inbox/
    01 Board/
    02 Daily/
    03 Trabalho QA/
    ├── 00 README.md
    └── Demandas/
        ├── 00 README.md
        ├── Bugs/
        ├── Melhorias/
        └── Planos/
    04 Trabalho DEV/
    ├── 00 README.md
    ├── Fixes/
    └── Execuções/
    05 Arquivo/
    Agentes/
    Skills/
    Templates/

## Responsabilidades do QA

- Classificar o material: bug, melhoria, plano, dúvida ou descarte.
- Tornar o problema compreensível sem contexto oral.
- Definir objetivo, regras, escopo e fora de escopo.
- Identificar riscos e impacto.
- Escrever critérios de aceite verificáveis.
- Criar CTs em Dado/Quando/Então.
- Classificar cada CT por tipo, camada e automação.
- Criar plano de testes quando a entrega tiver múltiplos riscos ou camadas.
- Liberar a demanda para DEV somente quando não houver pendência bloqueante.
- Executar a validação final e registrar evidências.

## Taxonomia de testes

Cada plano ou CT deve poder declarar:

| Campo | Valores iniciais |
|---|---|
| Tipo | funcional, contrato, segurança, acessibilidade, performance, usabilidade |
| Camada | unit, component, API, integração, E2E, carga |
| Automação | Vitest, RTL, smoke-api, Playwright, k6, manual |
| Execução | automatizado, manual, planejado, não aplicável |

O estado atual documentado do repositório cobre unit, lógica compartilhada, componentes/UI e integração API. E2E real, performance/carga, acessibilidade formal, regressão visual e DAST permanecem como camadas futuras, priorizadas por risco.

## Fluxo QA → DEV

1. Capturar em 00 Inbox.
2. Classificar e rotear em 03 Trabalho QA.
3. Refinar problema, objetivo, regras, escopo e critérios.
4. Definir CTs e camadas aplicáveis.
5. Resolver decisões pendentes.
6. Liberar para DEV.
7. Criar o registro em 04 Trabalho DEV.
8. Implementar, revisar e executar gates do repositório.
9. Validar CTs no ambiente adequado.
10. Se um CT reprovar, abrir NXG-NNN filho com pai igual ao ID da demanda.
11. Fechar card e registros juntos em 05 Arquivo.

## Plano de execução

### Fase 1 — Estrutura

- [x] Atualizar README e índices para 03 Trabalho QA e 04 Trabalho DEV.
- [x] Manter Demandas/Bugs, Demandas/Melhorias e Demandas/Planos como categorias de entrada QA.
- [x] Manter Fixes e Execuções como categorias de trabalho DEV.
- [x] Garantir que não existam duas áreas principais com o mesmo número.

### Fase 2 — Templates e skills

- [x] Padronizar frontmatter dos templates de demanda.
- [x] Manter Bug autocontido para diagnóstico e CTs de defeito.
- [x] Manter Melhoria como hub de contexto, decisões, aceite e CTs.
- [x] Criar template de Plano de Teste para entregas com múltiplas camadas.
- [x] Criar template de Validação para evidências e resultado por ambiente.
- [ ] Atualizar a skill de CTs com tipo, camada, automação e execução.
- [x] Manter FIX restrita a bugs e EXECUCAO restrita a melhorias.

### Fase 3 — Agentes

- [x] Fazer PROCESSAR executar triagem e gate de prontidão QA.
- [x] Fazer FIXAR encaminhar bug para Fixes e melhoria para Execuções.
- [ ] Garantir que nenhuma execução seja criada antes das pré-condições.
- [ ] Registrar sempre card, plano, execução, CTs e evidências por links.

### Fase 4 — Cobertura de qualidade

- [ ] Mapear tipo, camada e automação dos CTs existentes.
- [ ] Relacionar a cobertura atual do repositório com cada camada.
- [ ] Selecionar um primeiro fluxo E2E de alto valor, preferencialmente login → cliente.
- [ ] Selecionar um endpoint crítico para teste de carga inicial quando houver necessidade.
- [ ] Adicionar verificações de acessibilidade aos fluxos de UI de maior risco.
- [ ] Registrar quando E2E, performance, segurança ou acessibilidade não se aplicarem.

### Fase 5 — Validação do processo

- [ ] Percorrer o fluxo completo com MEL-0001.
- [ ] Percorrer o fluxo de bug com o modelo do NXG-026.
- [ ] Confirmar que cada etapa aponta para a próxima sem caminho ambíguo.
- [ ] Confirmar que card, CTs, plano, execução e arquivo preservam o mesmo ID.

## Critérios de aceite

- [ ] C1. Existe uma única área numerada 03 Trabalho QA para preparação e qualidade.
- [ ] C2. Existe uma única área numerada 04 Trabalho DEV, com Fixes e Execuções separados.
- [ ] C3. Bug e melhoria percorrem fluxos distintos, mas com etapas equivalentes e rastreáveis.
- [ ] C4. Templates de demanda compartilham frontmatter e indicam vínculo de execução.
- [ ] C5. Toda demanda pronta possui critérios de aceite e CTs identificados.
- [ ] C6. Cada CT pode declarar tipo, camada, automação e estado de execução.
- [ ] C7. O processo distingue unitário, UI, API, integração, E2E, performance, segurança e acessibilidade.
- [ ] C8. Camadas ainda não automatizadas aparecem como planejadas ou não aplicáveis.
- [ ] C9. PROCESSAR não libera item com decisão bloqueante pendente.
- [ ] C10. Card, execução, evidências e arquivo preservam o mesmo ID sem duplicar o repositório.

## Casos de teste do processo

### CT-001 Criar melhoria pronta para DEV

**Dado** uma melhoria com contexto, objetivo, escopo, regras, critérios e CTs
**Quando** não há decisão bloqueante
**Então** o agente permite abrir 04 Trabalho DEV/Execuções/<ID> com PLAN vinculado

**Critérios cobertos:** C1, C3, C5, C9

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### CT-002 Impedir execução de melhoria incompleta

**Dado** uma melhoria com decisão de produto pendente
**Quando** alguém tenta liberá-la para DEV
**Então** ela permanece em análise e a pergunta fica registrada no card

**Critérios cobertos:** C9

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### CT-003 Encaminhar bug e melhoria para áreas corretas

**Dado** um bug NXG-NNN e uma melhoria MEL-NNNN prontos
**Quando** o agente inicia o trabalho DEV
**Então** o bug vai para Fixes e a melhoria vai para Execuções sem renomear os IDs

**Critérios cobertos:** C2, C3, C10

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### CT-004 Classificar cobertura de testes

**Dado** um conjunto de CTs unitários, UI, API e manuais
**Quando** reviso o plano de testes
**Então** cada CT possui tipo, camada, automação e estado, e lacunas ficam explícitas

**Critérios cobertos:** C6, C7, C8

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### CT-005 Fechar e arquivar a cadeia

**Dado** uma demanda implementada com CTs executados e review aprovado
**Quando** encerro o trabalho
**Então** card e pasta vão juntos para 05 Arquivo/<ID>, preservando os links

**Critérios cobertos:** C10

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

## Fora de escopo

- Implementar imediatamente ferramenta E2E, performance ou DAST.
- Reescrever todos os CTs existentes de uma só vez.
- Duplicar no vault planos técnicos mantidos em docs/plans.
- Criar ferramenta de gestão externa ou substituir o board.

## Definição de pronto

- [ ] Estrutura de pastas consolidada.
- [ ] Templates, skills e agentes apontam para os mesmos caminhos.
- [ ] Plano de testes e validação estão disponíveis como modelos.
- [ ] MEL-0001 e um bug percorrem o fluxo sem ambiguidade.
- [ ] CTs do processo executados e evidências registradas.
- [ ] README e documentação do vault sincronizados.
