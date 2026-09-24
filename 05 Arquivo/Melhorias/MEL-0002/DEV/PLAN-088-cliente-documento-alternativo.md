---
tipo: plano tecnico
id: PLAN-088
status: concluido
demanda: "[[05 Arquivo/Melhorias/MEL-0002/QA/MEL-0002 Cliente Documento/01 - Demanda|MEL-0002 Cliente Documento]]"
execucao: "[[05 Arquivo/Melhorias/MEL-0002/DEV/MEL-0002/00 README|MEL-0002 — execução]]"
---
# PLAN-088 — Cliente: documento alternativo

> Hub do plano técnico relacionado à [[05 Arquivo/Melhorias/MEL-0002/QA/MEL-0002 Cliente Documento/01 - Demanda|MEL-0002 Cliente Documento]]. O detalhamento de implementação permanece em `nxgestao/docs/plans/PLAN-088-cliente-documento-alternativo.md`.

## Objetivo

Adicionar o campo opcional `documento` (RG ou outro identificador) abaixo do CPF no cadastro de clientes, preservando as regras atuais do CPF.

## Regras principais

- CPF e Documento podem ficar vazios simultaneamente.
- CPF informado continua validado e único no escopo atual.
- Documento é texto livre, sem máscara, validação de RG ou unicidade.
- Limite de 20 caracteres; espaços externos são removidos; vazio persiste como `null`.

## Escopo técnico

- Migração idempotente de `clientes.documento`.
- Propagação no domínio, schemas, casos de uso, repositório e API.
- Campo nos formulários de criação e edição.
- Traduções e testes automatizados.

## Estado

| Etapa | Estado |
|---|---|
| Planejamento | ✅ |
| Implementação | ✅ |
| Code review | ✅ |
| Validação funcional | 🔵 |

## Verificação

Os CTs da melhoria são a fonte de aceite: CT-001 a CT-008. O registro da rodada atual está em [[05 Arquivo/Melhorias/MEL-0002/QA/MEL-0002 Cliente Documento/04 - Validação dev]].

## Referência técnica

Arquivo completo no repositório: `nxgestao/docs/plans/PLAN-088-cliente-documento-alternativo.md`.
