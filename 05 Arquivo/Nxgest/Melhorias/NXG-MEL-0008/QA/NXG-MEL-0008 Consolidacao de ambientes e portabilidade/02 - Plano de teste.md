---
demanda: "[[01 - Demanda]]"
status: "concluido"
responsavel: "NX Gest · QA e Coordenação"
pontos: 2
projeto: "nxgest"
epico: "NXG-EPIC-0001"
---

# Plano de teste — NXG-MEL-0008

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/00 README|Execução DEV]]

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Comprovar os oito critérios de consolidação e portabilidade com observações independentes.

---

## Riscos e escopo

Preservar diffs e dados locais; isolar banco/portas/volumes; configurações sintéticas; os bugs NXG-029 e NXG-030 devem ser corrigidos antes da prova integrada.

---

## Estratégia de teste

- **Unitário:** regras e serviços isolados.
- **API/repositório:** contrato, validações e persistência.
- **UI/E2E:** comportamento do usuário e integração entre campos/telas.
- **Regressão:** fluxos existentes afetados pela mudança.

Defina apenas as camadas aplicáveis; não crie testes por obrigação quando não houver risco naquela camada.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | Regressão | manual | manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Regressão | manual | manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Regressão | manual | manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Regressão | manual | manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Regressão | manual | manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | Regressão | manual | manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-007\|CT-007]] | Regressão | manual | manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-008\|CT-008]] | Regressão | manual | manual | [[04 - Validação dev\|Registrar resultado]] |

---

## Entrada e saída

**Entrada:** pacote íntegro, autorização de execução e preservação definida.
**Saída:** CTs executados, evidências por critério, limites explícitos e parecer final sem encerramento do épico.

