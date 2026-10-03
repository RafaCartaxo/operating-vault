---
demanda: FIN-MEL-0008
status: planejado
responsavel: ""
pontos: ""
---

# Plano de teste — FIN-MEL-0008

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/<projeto>/Execuções/<ID>/00 README|Execução <ID>]]

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Validar a criação, distribuição, persistência e consulta mensal de séries parceladas, incluindo regressão para lançamentos simples.

---

## Riscos e escopo

- Escopo: frontend, API Go, persistência SQLite e regras de geração das parcelas.
- Riscos: arredondamento incorreto, datas inválidas, série incompleta e alteração indevida de lançamentos simples.
- O plano será congelado após as decisões de edição/exclusão da série e datas no fim do mês.

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
| [[03 - Casos de teste#^ct-001\|CT-001]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Validação | API | Automatizado + manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Cálculo | Unit/API | Automatizado | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Calendário | Unit/API | Automatizado + manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Integridade | API/DB | Automatizado | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | Regressão | UI/API | Automatizado + manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-007\|CT-007]] | Série | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |

> Exemplo: replique a linha para cada CT do pacote. O link do CT abre a prévia do cenário; o link de Validação leva à tabela onde o resultado e a evidência são registrados.

---

## Entrada e saída

**Entrada:**  
**Saída:**
