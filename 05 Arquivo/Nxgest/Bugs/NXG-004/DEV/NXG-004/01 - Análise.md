# 01 - Análise (NXG-004)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Nxgest/Bugs/NXG-004/QA/NXG-004 CEP preenchido não permite salvar/01 - Bug|NXG-004 — bug]]  
> **Plano:** [[02 - Plano de correção]]  
> **Implementação:** [[03 - Implementação]]  
> **Code review:** [[04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Bugs/NXG-004/QA/NXG-004 CEP preenchido não permite salvar/03 - Validação dev|Validação QA]]

---

## Veredito

O CEP válido é consultado e exibido, mas é rejeitado pelos schemas de criação/edição no momento do salvamento.

## O que foi confirmado

- A interface envia o CEP sem máscara.
- A API retorna `VALIDATION_ERROR` com `Dados inválidos.`.
- Os schemas `CreateClienteInput.ts` e `UpdateClienteInput.ts` usam `/^\\d{8}$/`, que procura a sequência literal `\\d` em vez de oito dígitos.
- A validação de CEP precisa aceitar oito dígitos numéricos nos fluxos de criação e edição.

## Abordagem e riscos

- Corrigir a expressão de validação compartilhada entre frontend e backend.
- Cobrir criação, edição e persistência sem alterar a consulta do CEP ou a localização aproximada.

## Arquivos identificados

- `src/modules/cliente/application/use-cases/CreateCliente/CreateClienteInput.ts`
- `src/modules/cliente/application/use-cases/UpdateCliente/UpdateClienteInput.ts`
