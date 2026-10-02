---
projeto: financas-pessoais
tipo: arquitetura-operacional
---

# Fluxo de trabalho do projeto

Este diagrama mostra como o projeto é coordenado, implementado e consumido. Os três espaços têm responsabilidades diferentes.

```mermaid
flowchart LR
    O[operating-vault\ncoordenação] -->|tarefa, plano e status| D[DEV Finanças Pessoais]
    D -->|implementa| R[financas-pessoais\ncódigo Go + React]
    R -->|API e exportação| V[financas-vault\ndados e relatórios]
    V -->|evidência de comportamento| D
    R -->|documentação técnica| D
```

## Fluxo de uma entrega

```mermaid
sequenceDiagram
    participant OV as Operating Vault
    participant Repo as financas-pessoais
    participant App as Aplicação
    participant FV as financas-vault

    OV->>OV: registra demanda e critérios
    OV->>Repo: direciona implementação
    Repo->>App: implementa e testa
    App->>FV: gera/atualiza dados e relatórios
    FV-->>OV: fornece contexto/evidência
    OV->>OV: atualiza status e encerra etapa
```

## Responsabilidade de cada local

| Local | Faz | Não faz |
|---|---|---|
| `operating-vault` | coordena trabalho, roadmap, status e decisões | não contém código da aplicação |
| `financas-pessoais` | contém backend, frontend, testes e documentação técnica | não é o painel financeiro diário |
| `financas-vault` | contém dados, painéis, relatórios e fluxos de uso | não coordena execução nem substitui o banco |

## Regra de partida

Toda nova etapa começa no `operating-vault`, aponta para o repositório técnico, atualiza a documentação de fluxos e só depois altera o vault financeiro quando houver saída de dados ou relatório.
