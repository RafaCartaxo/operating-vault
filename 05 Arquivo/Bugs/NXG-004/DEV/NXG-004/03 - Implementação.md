# 03 - Implementação (NXG-004)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Bugs/NXG-004/QA/NXG-004 CEP preenchido não permite salvar/01 - Bug|NXG-004 — bug]]  
> **Plano:** [[02 - Plano de correção]]  
> **Code review:** [[04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Bugs/NXG-004/QA/NXG-004 CEP preenchido não permite salvar/03 - Validação dev|Validação QA]]

---

## Rodada 1 — ✅ concluída

- Corrigida a regex de CEP nos schemas de criação e edição para aceitar oito dígitos numéricos.
- Mantidas a consulta do CEP, a localização aproximada e a regra de CEP opcional.

## Testes da correção

- [x] Teste unitário da causa corrigida.
- [x] Teste de formulário/UI, quando aplicável.
- [x] Teste de API/repositório, quando aplicável.
- [x] Regressão do cenário que originou o bug.
- [x] Caminhos dos testes e comando executado registrados.

### Evidência

Comando: `npx vitest run src/modules/cliente/application/use-cases/CreateCliente/CreateClienteInput.test.ts src/modules/cliente/application/use-cases/UpdateCliente/UpdateClienteInput.test.ts src/modules/cliente/application/use-cases/CreateCliente/CreateClienteUseCase.test.ts src/modules/cliente/application/use-cases/UpdateCliente/UpdateClienteUseCase.test.ts`

Resultado: **4 arquivos, 6 testes aprovados**.
