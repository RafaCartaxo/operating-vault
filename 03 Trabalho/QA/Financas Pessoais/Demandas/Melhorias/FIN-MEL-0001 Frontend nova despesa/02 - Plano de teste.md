---
demanda: FIN-MEL-0001
status: planejado
responsavel: ""
pontos: 1
---

# Plano de teste — FIN-MEL-0001

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/00 README|Execução DEV]]

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

## Objetivo

Comprovar que o usuário consegue registrar uma despesa válida e recebe orientação adequada nos cenários de erro, em celular e desktop.

## Estratégia

- **UI:** formulário, responsividade, mensagens e estados.
- **API/integração:** payload enviado e tratamento das respostas do backend.
- **Regressão:** testes atuais do backend continuam passando.

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Critérios |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001|CT-001]] | Funcional | UI/API | Manual + automatizável | C1, C3, C5 |
| [[03 - Casos de teste#^ct-002|CT-002]] | Funcional | UI | Manual | C2 |
| [[03 - Casos de teste#^ct-003|CT-003]] | Negativo | UI/API | Manual | C4 |
| [[03 - Casos de teste#^ct-004|CT-004]] | Regressão | API | Automatizado | C3, C6 |

## Entrada e saída

**Entrada:** frontend disponível, backend iniciado, contrato da API atualizado e casos revisados.  
**Saída:** todos os CTs executados; nenhum bloqueio crítico aberto; evidências registradas na validação.
