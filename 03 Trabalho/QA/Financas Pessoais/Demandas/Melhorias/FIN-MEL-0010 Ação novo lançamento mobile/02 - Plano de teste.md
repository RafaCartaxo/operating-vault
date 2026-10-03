---
demanda: FIN-MEL-0010
status: concluido
responsavel: ""
pontos: ""
---

# Plano de teste — FIN-MEL-0010

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0010/00 README|Execução DEV]]

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Validar a separação visual entre navegação mobile e ação de novo lançamento, preservando o modal existente e evitando sobreposição ou regressão desktop.

---

## Riscos e escopo

- **Escopo:** barra inferior mobile, botão de ação, abertura do modal existente, safe area e regressão desktop.
- **Riscos:** ação difícil de localizar, sobreposição com conteúdo/filtros, área de toque insuficiente e abertura quebrada do modal.

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
| [[03 - Casos de teste#^ct-001\|CT-001]] | Regressão | UI/API | Automatizado + manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Funcional | E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Integração | E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Responsividade | E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Regressão | E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |

> Exemplo: replique a linha para cada CT do pacote. O link do CT abre a prévia do cenário; o link de Validação leva à tabela onde o resultado e a evidência são registrados.

---

## Entrada e saída

**Entrada:** build com FIN-MEL-0009 disponível, viewport mobile e desktop, dados de teste.  
**Saída:** 5 CTs executados com evidências e decisão QA registrada.
