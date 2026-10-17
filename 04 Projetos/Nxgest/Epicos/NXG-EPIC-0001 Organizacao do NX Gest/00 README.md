---
id: NXG-EPIC-0001
tipo: epico
status: analise
projeto: nxgest
prioridade: alta
data_inicio: 2026-10-17
data_fim: ""
responsavel: ""
---

# NXG-EPIC-0001 — Organização do NX Gest

> [!info]- Navegação do épico
> **Projeto:** [[04 Projetos/Nxgest/README|Nxgest]]  
> **Plano de governança:** [[03 Trabalho/QA/Nxgest/Demandas/Planos/NXG-028 Governanca da reorganizacao do NX Gest|NXG-028]]  
> **Board QA:** [[01 Board/QA/BOARD QA — Nxgest|Board QA]]  
> **Board DEV:** [[01 Board/DEV/BOARD DEV — Nxgest|Board DEV]]

## Objetivo

Organizar o NX Gest segundo um padrão claro, reproduzível e fácil de clonar, preservando o funcionamento atual e separando adequadamente raiz, infraestrutura, ambientes, documentação e agentes.

## Escopo do épico

- Atualizar o mapa documental da raiz.
- Agrupar infraestrutura em `infra/` quando os caminhos e validações estiverem preparados.
- Organizar comandos e onboarding de ambientes.
- Manter `AGENTS.md` como contrato global e `.opencode/agents/` como agentes especializados.
- Consolidar o padrão de nomenclatura `nxgest`.
- Validar clone limpo, build, testes, documentação e compatibilidade de staging/produção.

## Fora de escopo

- Renomear volumes, redes, domínios ou diretórios reais da infraestrutura existente.
- Alterar segredos ou credenciais.
- Criar outro repositório oficial.
- Fazer deploy em produção sem autorização específica.

## Demandas vinculadas

| ID | Demanda | Relação | Estado |
|---|---|---|---|
| MEL-0004 | [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/MEL-0004 README e mapa da raiz/00 README|README e mapa da raiz]] | primeiro lote documental | Em análise |
| MEL-0005 | a criar após aprovação do plano | infraestrutura em `infra/` | Backlog |
| MEL-0006 | a criar após aprovação do plano | scripts e onboarding | Backlog |
| MEL-0007 | a criar após aprovação do plano | agentes especializados | Opcional |

## Dependências

- [[03 Trabalho/QA/Nxgest/Demandas/Planos/NXG-028 Governanca da reorganizacao do NX Gest|NXG-028 — Governança da reorganização do NX Gest]] define decisões e lotes.
- O trabalho não commitado do repositório deve ser preservado antes de lotes estruturais.

## Fluxo do épico

```mermaid
flowchart LR
    A[NXG-028\nGovernança] --> B[MEL-0004\nREADME]
    B --> C[MEL-0005\ninfra/]
    C --> D[MEL-0006\nOnboarding]
    D --> E[MEL-0007\nAgentes]
```

## Status consolidado

| Gate | Situação |
|---|---|
| Escopo do épico | ✅ definido |
| Plano de governança | ✅ em criação |
| MEL-0004 | 🟡 em análise QA |
| Lotes estruturais | ⏳ aguardando decisões e gate QA |
| Execução no NX Gest | ⏳ não iniciada |

## Critério de conclusão

O épico será concluído quando as demandas vinculadas tiverem critérios aprovados, implementações revisadas, CTs executados, documentação sincronizada e nenhuma pendência bloqueante, sem exigir alteração não autorizada da infraestrutura real.
