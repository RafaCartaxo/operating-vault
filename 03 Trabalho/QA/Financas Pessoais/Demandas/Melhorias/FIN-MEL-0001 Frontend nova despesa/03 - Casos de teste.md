---
demanda: FIN-MEL-0001
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
---

# Casos de teste — FIN-MEL-0001

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/00 README|Execução DEV]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1|C1]] | [[03 - Casos de teste#^ct-001|CT-001]] |
| [[01 - Demanda#^c2|C2]] | [[03 - Casos de teste#^ct-002|CT-002]] |
| [[01 - Demanda#^c3|C3]] | [[03 - Casos de teste#^ct-001|CT-001]], [[03 - Casos de teste#^ct-004|CT-004]] |
| [[01 - Demanda#^c4|C4]] | [[03 - Casos de teste#^ct-003|CT-003]] |
| [[01 - Demanda#^c5|C5]] | [[03 - Casos de teste#^ct-001|CT-001]] |
| [[01 - Demanda#^c6|C6]] | [[03 - Casos de teste#^ct-004|CT-004]] |

## CT-001 · Registrar despesa válida

**Dado** que o usuário está na tela de nova despesa e informa dados válidos  
**Quando** envia o formulário  
**Então** o frontend chama `POST /api/lancamentos`, mostra confirmação e prepara novo lançamento.

**Camada:** UI/API · **Tipo:** funcional · **Execução:** planejado

^ct-001

## CT-002 · Bloquear dados obrigatórios inválidos

**Dado** que faltam campos obrigatórios ou o valor/data é inválido  
**Quando** o usuário tenta enviar  
**Então** o envio não ocorre e cada problema é indicado de forma compreensível.

**Camada:** UI · **Tipo:** funcional · **Execução:** planejado

^ct-002

## CT-003 · Tratar falha da API

**Dado** que a API responde com erro  
**Quando** o usuário envia um lançamento válido  
**Então** aparece uma mensagem de erro, os dados preenchidos permanecem disponíveis e o usuário pode tentar novamente.

**Camada:** UI/API · **Tipo:** negativo · **Execução:** planejado

^ct-003

## CT-004 · Preservar contrato do backend

**Dado** que os testes atuais do backend estão disponíveis  
**Quando** a suíte Go é executada  
**Então** os testes passam e o endpoint continua aceitando o payload esperado pelo frontend.

**Camada:** API · **Tipo:** regressão · **Execução:** planejado

^ct-004
