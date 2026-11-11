---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: "NX Gest · QA"
pontos: 3
---

# Plano de teste — NXG-MEL-0009

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** será criada pelo DEV após encaminhamento da Coordenação.

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Verificar C1–C8 com 14 CTs de fixtures e dublês, cobrindo falhas, regressão, documentação e evidências; não executar nenhuma operação real.

---

## Riscos e escopo

Backup parcial/enganoso; perda de anexos; conjunto incoerente; imagem anterior removida; rollback incompatível com banco/mount; concorrência, interrupção, saúde e vazamento de segredos. Limitação: dublês não provam integridade nem restauração de dados reais.

---

## Estratégia de teste

- Testes locais automatizados, sem Docker daemon, máquinas virtuais ou serviços reais: dublês com eventos e falhas injetadas; arquivos e conteúdo sintéticos. Antes de cada caso, comprovar isolamento e que os comandos Docker/rede são interceptados por dublês; se a interceptação falhar, abortar antes de qualquer ação.
- Comparação de hashes anteriores e integridade de fixtures; ensaio em destino de teste dedicado e descartável.
- Revisão de checklist/runbook e sanidade de logs com segredo fictício; regressão NXG-031.
- Restore PostgreSQL real, recursos reais e testes de produção dependem de autorização específica posterior e não são inferidos aqui.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-007\|CT-007]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-008\|CT-008]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-009\|CT-009]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-010\|CT-010]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-011\|CT-011]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-012\|CT-012]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-013\|CT-013]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-014\|CT-014]] | regressão | infra/documentação | ambos | [[04 - Validação dev\|Registrar resultado]] |

---

## Entrada e saída

**Entrada:** pacote QA aprovado, fixtures exclusivas e autorização de implementação local.  
**Saída:** DEV_READY_FOR_QA com evidência por CT; QA executa independentemente e registra resultados. Restore real e go de publicação permanecem pendentes.

## Matriz de falhas e evidências

| Falha ou condição | CTs | Parada e evidência esperada |
|---|---|---|
| Dump/cópia/tar, ausência, corrupção ou mistura | CT-002–004 | Falha fechada; hashes do conjunto anterior e logs sem segredo |
| Interrupção, colisão ou concorrência | CT-006–007 | Efeito incompleto não promovido; lock/recusa observável |
| Imagem, schema ou mounts ausentes/incompatíveis | CT-008–009 | Interromper; razão documentada; nenhuma operação real |
| Decisão de dados, health ou segredo | CT-010–012 | Decisão explícita; health negativo não aprovado; marcador não aparece |
| Regressão e limite de simulação | CT-013–014 | Gates anteriores preservados; restore real continua pendente |
