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

---

## Objetivo

Comprovar que o usuário consegue registrar uma despesa válida e recebe orientação adequada nos cenários de erro, em celular e desktop.

---

## Riscos e escopo

- Risco de o formulário não ser utilizável em telas pequenas.
- Risco de divergência entre o payload do frontend e o contrato Go.
- Risco de perda dos dados preenchidos quando a API falha.

---

## Estratégia de teste

- **Unitário:** regras de validação do formulário, quando isoladas.
- **API/repositório:** contrato e persistência continuam cobertos pela suíte Go existente.
- **UI/E2E:** preenchimento, envio, mensagens e responsividade.
- **Regressão:** execução dos testes atuais do backend após a integração.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | Funcional | E2E/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Funcional | E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Negativo | E2E/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Regressão | API | Automatizado | [[04 - Validação dev\|Registrar resultado]] |

---

## Entrada e saída

**Entrada:** frontend disponível, backend iniciado, contrato da API atualizado e casos revisados.  
**Saída:** todos os CTs executados; nenhum bloqueio crítico aberto; evidências registradas na validação.
