---
demanda: FIN-MEL-0007
status: concluido
responsavel: ""
pontos: ""
---

# Plano de teste — FIN-MEL-0007

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** implementação registrada diretamente no projeto; sem execução DEV separada.

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Validar os artefatos PWA, a instalação e o comportamento do app shell sem criar falsa disponibilidade offline para a API financeira.

---

## Riscos e escopo

- Escopo: manifest, ícones, service worker, metadados e build.
- Riscos: instalação indisponível, cache incompleto ou cache indevido de chamadas financeiras.

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
| [[03 - Casos de teste#^ct-001\|CT-001]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Offline | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Segurança de dados | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Build | UI | Automatizado | [[04 - Validação dev\|Registrar resultado]] |

> Exemplo: replique a linha para cada CT do pacote. O link do CT abre a prévia do cenário; o link de Validação leva à tabela onde o resultado e a evidência são registrados.

---

## Entrada e saída

**Entrada:**  
**Saída:**
