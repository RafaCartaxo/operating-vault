# Operating Vault

Sistema operacional pessoal multi-projeto para organizar QA, DEV, estudos e execução: entrada, boards, dailies, pacotes de trabalho, projetos, arquivo, skills, agentes, templates e validação.

> https://github.com/RafaCartaxo/operating-vault

## O que é

Infraestrutura de organização e método de trabalho, não um produto com regra de negócio. Cada produto tem seu próprio contexto e área operacional.

## Como navegar (sem Obsidian)

| Pasta | Função |
|---|---|
| `00 Inbox/` | captura temporária |
| `01 Board/` | visões por projeto |
| `02 Daily/` | notas diárias |
| `03 Trabalho/` | pacotes de demanda/execução (fonte dos cards) |
| `04 Projetos/` | contexto por produto |
| `05 Arquivo/` | concluídos/arquivados |
| `Sistema/`, `Skills/`, `Agentes/`, `Templates/`, `scripts/` | regras, modelos e validação |

> O índice interno ([`00 README.md`](00%20README.md)) usa `[[wikilinks]]` do Obsidian; fora do Obsidian, navegue pela árvore de arquivos. [`Dashboard.md`](Dashboard.md) é a central de trabalho.

## Fluxo QA → DEV (resumo)

Entrada → QA (pacote em `03 Trabalho/QA/<projeto>/`) → DEV após `QA_READY_FOR_DEV` → concluído vai para `05 Arquivo/<projeto>/`. Todo artefato nasce de um template em `Templates/`.

## Escopo e limites

- Repositório público e operacional; contextos sensíveis de `03 Trabalho/`, `04 Projetos/` e `02 Daily/` não fazem parte da apresentação.
- Este README é camada de apresentação; não altera o vault existente.

## Repositórios relacionados

- Brainwork — sistema de conhecimento e operação de QA, apresentado apenas por casos/versão sanitizada (link direto do vault bruto não incluído, por segurança).
- https://github.com/RafaCartaxo/nxgest
