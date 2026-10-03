---
demanda: FIN-MEL-0012
status: concluido
responsavel: ""
pontos: ""
---

# Plano de teste — FIN-MEL-0012

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** ainda não criada — aguarda aprovação do pacote QA.

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Validar o cadastro, a geração mensal, o encerramento e o cálculo sem duplicidade das despesas recorrentes.
---

## Riscos e escopo

- **Escopo:** regra recorrente mensal, ocorrências, vínculo com cartão/conta e saldo mensal.
- **Riscos:** duplicação de cobrança, geração além do término, alteração retroativa indevida e ocorrência parcial após erro.
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
| [[03 - Casos de teste#^ct-001\|CT-001]] | Funcional | E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Integração | E2E/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Funcional | E2E/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Regressão | E2E/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Financeiro | Integração | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | Validação | E2E/API | Manual | [[04 - Validação dev\|Registrar resultado]] |

> Exemplo: replique a linha para cada CT do pacote. O link do CT abre a prévia do cenário; o link de Validação leva à tabela onde o resultado e a evidência são registrados.

---

## Entrada e saída

**Entrada:** aplicação disponível, regra recorrente mensal e faturas/lançamentos de teste.  
**Saída:** 6 CTs executados com evidências e decisão QA registrada.
