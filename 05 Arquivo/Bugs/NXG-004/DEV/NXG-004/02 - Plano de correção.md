# 02 - Plano de correção (NXG-004)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Bugs/NXG-004/QA/NXG-004 CEP preenchido não permite salvar/01 - Bug|NXG-004 — bug]]  
> **Análise:** [[01 - Análise]]  
> **Implementação:** [[03 - Implementação]]  
> **Code review:** [[04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Bugs/NXG-004/QA/NXG-004 CEP preenchido não permite salvar/03 - Validação dev|Validação QA]]

> Congelado na aprovação. Alteração posterior vira decisão registrada em `03 - Implementação.md`.

---

## Resultado esperado

CEP válido preenchido permite salvar o cliente, mantendo endereço e localização aproximada retornados pela consulta.

## Mudança planejada

- **Arquivos/áreas:** `CreateClienteInput.ts` e `UpdateClienteInput.ts` no backend.
- **Abordagem mínima:** corrigir a regex para aceitar exatamente oito dígitos numéricos após a remoção da máscara.
- **Regressão a proteger:** consulta do CEP, criação, edição e persistência do endereço.

## Fora de escopo

- Alterar o provedor de CEP ou a lógica de localização.
- Tornar o CEP obrigatório.

## Pronto quando

- [x] CT-B01 e CT-B02 executados.
- [x] Testes automatizados da validação atualizados.
- [x] Gates do repositório verdes.
- [x] Code review aprovado.
