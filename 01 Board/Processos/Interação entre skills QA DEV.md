---
tipo: processo
status: ativo
escopo: operating-vault
---

# Interação entre skills QA ↔ DEV

Esta página explica como as duas skills se comunicam e quem assume cada etapa. A versão canônica das regras está em [[Skills/QA-FIRST-DELIVERY|QA First Delivery]] e [[Skills/DEV-EXECUTION|DEV Execution]]; o diagrama abaixo é a fonte operacional da interação no vault.

## Regra principal

O usuário apresenta o trabalho. A etapa atual define a skill responsável e o próximo handoff. Não é necessário escolher manualmente a skill seguinte.

```mermaid
sequenceDiagram
    participant Pessoa as Pessoa/Produto
    participant QA as QA First Delivery
    participant OV as Operating Vault
    participant DEV as DEV Execution
    participant Repo as Repositório/App

    Pessoa->>QA: necessidade, melhoria ou bug
    QA->>OV: copia templates e cria pacote QA
    QA->>OV: QA_READY_FOR_DEV
    OV->>DEV: entrega critérios, CTs e links
    DEV->>Repo: analisa, planeja e implementa
    DEV->>OV: registra testes e code review
    DEV->>OV: DEV_READY_FOR_QA
    OV->>QA: entrega execução para validação
    QA->>Repo: executa CTs funcionais
    alt aprovado
        QA->>OV: QA_APPROVED
        OV->>OV: atualiza boards, roadmap e épico
    else reprovado
        QA->>OV: QA_REJECTED
        OV->>DEV: devolve defeito/ajuste vinculado
    end
```

## Matriz de roteamento

| Estado atual | Skill ativa | Ação | Próximo estado |
|---|---|---|---|
| nova ideia, melhoria ou bug | `qa-first-delivery` | classificar, copiar templates e preparar QA | QA · Triagem/Análise |
| pacote QA incompleto | `qa-first-delivery` | corrigir contexto, critérios, CTs ou links | QA · Análise |
| pacote QA aprovado | `qa-first-delivery` → `dev-execution` | emitir `QA_READY_FOR_DEV` | DEV · Análise |
| execução técnica | `dev-execution` | analisar, planejar, implementar e testar | DEV · Code review |
| code review aprovado | `dev-execution` → `qa-first-delivery` | emitir `DEV_READY_FOR_QA` | QA · Validação |
| CTs aprovados | `qa-first-delivery` | emitir `QA_APPROVED` e fechar | Concluído |
| CT reprovado/bloqueado | `qa-first-delivery` → `dev-execution` | emitir `QA_REJECTED` e vincular defeito | DEV · Análise |

## Invariantes

1. QA não implementa antes de `QA_READY_FOR_DEV`.
2. DEV não inicia sem critérios, CTs e gate QA.
3. DEV não aprova CT funcional.
4. QA não altera silenciosamente o resultado esperado durante a validação.
5. Cada handoff atualiza frontmatter, README, board, links e evidências.
6. O fluxo é orientado por estado e artefatos; não depende de `siga` ou outra palavra-chave.
