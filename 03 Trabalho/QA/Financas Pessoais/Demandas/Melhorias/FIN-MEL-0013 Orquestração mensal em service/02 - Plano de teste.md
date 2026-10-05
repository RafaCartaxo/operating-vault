---
demanda: "[[01 - Demanda]]"
status: concluido
responsavel: QA/qa-first-delivery
pontos: 1
---

# Plano de teste — FIN-MEL-0013

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

Verificar que a orquestração mensal foi extraída para uma camada de aplicação sem alterar o contrato HTTP, as regras de recorrência, a idempotência ou o tratamento de falhas.
---

## Riscos e escopo

O principal risco é a refatoração chamar a listagem antes da materialização, duplicar ocorrências ou esconder uma falha como resposta vazia/sucesso. O escopo cobre backend, persistência via API e documentação arquitetural; não cobre novas regras de negócio.
---

## Estratégia de teste

- **Unitário:** fronteira e ordem da orquestração do service.
- **API/repositório:** contrato mensal, persistência e idempotência.
- **Regressão:** recorrências ativas, datas-limite, inclusão em fatura e falhas.

Defina apenas as camadas aplicáveis; não crie testes por obrigação quando não houver risco naquela camada.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | Funcional | unit | Automatizado | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Regressão | API | Automatizado + manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Regressão | API | Automatizado + manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Negativo | API | Automatizado + manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Inspeção | unit | Manual | [[04 - Validação dev\|Registrar resultado]] |

> Exemplo: replique a linha para cada CT do pacote. O link do CT abre a prévia do cenário; o link de Validação leva à tabela onde o resultado e a evidência são registrados.

---

## Entrada e saída

**Entrada:** implementação DEV da FIN-MEL-0013 no ambiente dev, com testes e documentação atualizados.
**Saída:** cinco CTs executáveis, matriz completa, evidências e decisão QA.
