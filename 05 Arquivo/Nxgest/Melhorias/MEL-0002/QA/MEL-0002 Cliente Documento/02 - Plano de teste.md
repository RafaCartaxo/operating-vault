---
demanda: "[[01 - Demanda|MEL-0002 Cliente Documento]]"
status: concluido
responsavel: ""
pontos: 10
---
# Plano de teste — MEL-0002

> [!info]- Navegação QA/DEV
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Melhorias/MEL-0002/DEV/MEL-0002/00 README|MEL-0002 — execução]]

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

## Objetivo

Confirmar que o Documento alternativo pode ser criado, persistido, editado e removido sem alterar as regras existentes do CPF.

## Riscos e escopo

- Regressão na validação ou deduplicação do CPF.
- Perda do valor durante criação, edição ou retorno da API.
- Clientes existentes sem Documento deixarem de abrir ou salvar.

Fora do escopo: formato de RG, máscara, unicidade, busca e filtro por Documento.

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | Regressão | UI/API | Automatizado + manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Funcional | UI/API | Automatizado + manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Negativo | UI | Automatizado + manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Persistência | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | Edição | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-007\|CT-007]] | Limite | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-008\|CT-008]] | Regressão | API/dados existentes | Manual | [[04 - Validação dev\|Registrar resultado]] |

## Entrada e saída

**Entrada:** ambiente `dev`, versão/build em execução e dados de teste descartáveis.  
**Saída:** CTs executados, evidências registradas e decisão de aprovação.
