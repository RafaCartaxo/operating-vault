---
tags: [qa, qase]
tipo: referencia
status: enviado
qase_projeto: NXG
qase_suite_id: 2
demanda: "[[01 - Demanda|MEL-0003 — Expandir e recolher com chevron]]"
origem: "[[03 - Casos de teste]]"
projeto: nxgest
---
# Preparação Qase — MEL-0003

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda|MEL-0003 — Expandir e recolher com chevron]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]

Suite Qase: `Clientes > Cadastro` (`suite_id: 2`).

> **Regra de tags:** esta primeira carga preservou `CT-001` e `CT-002` para auditoria do envio inicial. Nas próximas cargas, usar somente `MEL-NNNN` e o módulo (`cliente`); o ID do CT já fica no título e no identificador do caso.

## Casos enviados

### CT-001 — Chevron indica seção recolhida e expandida

- **Qase ID:** `1`
- **Descrição:** Confirma que o chevron comunica corretamente os estados recolhido e expandido no cadastro e na edição de cliente.
- **Pré-condições:** Usuário está na tela de cadastro ou edição de cliente; existe uma seção expansível disponível.
- **Passos:** observar o controle recolhido → confirmar chevron à direita; clicar no controle → confirmar seção expandida e chevron para baixo.
- **Pós-condição:** a seção permanece expandida até novo clique.
- **Tipo:** funcional · **Camada:** E2E/UI · **Automação:** manual
- **Prioridade:** média · **Severidade:** normal · **Comportamento:** positivo
- **Tags:** `MEL-0003`, `CT-001`, `cliente`

### CT-002 — Chevron mantém acessibilidade em criar e editar

- **Qase ID:** `2`
- **Descrição:** Confirma que o controle de expandir e recolher continua acessível e funcional nos fluxos de criar e editar cliente.
- **Pré-condições:** Usuário pode acessar criar e editar cliente; melhoria disponível no ambiente de teste.
- **Passos:** acessar o controle recolhido em criar e editar → confirmar nome acessível e chevron; acionar por teclado → confirmar alternância de estado.
- **Pós-condição:** os dados do cliente permanecem íntegros.
- **Tipo:** regressão · **Camada:** E2E/UI · **Automação:** manual
- **Prioridade:** média · **Severidade:** normal · **Comportamento:** positivo
- **Tags:** `MEL-0003`, `CT-002`, `cliente`

## Estado

- [x] CT-001 enviado sem duplicação.
- [x] CT-002 enviado sem duplicação.
- [x] IDs registrados no vault.
- [x] Status: `enviado`.
