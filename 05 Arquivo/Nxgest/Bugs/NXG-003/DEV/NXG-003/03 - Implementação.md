# 03 - Implementação (NXG-003)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Nxgest/Bugs/NXG-003/QA/NXG-003 Endereço pessoal inicia aberto/01 - Bug|NXG-003 — bug]]  
> **Plano:** [[02 - Plano de correção]]  
> **Code review:** [[04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Bugs/NXG-003/QA/NXG-003 Endereço pessoal inicia aberto/03 - Validação dev|Validação QA]]

> Log datado do que foi realmente feito. O plano não é reescrito aqui; desvios viram decisão registrada.

---

## Rodadas

### Rodada 1 — ✅ Concluída

- Adicionado estado de expansão independente para os blocos de endereço em `ClienteForm.tsx`.
- Endereço do comércio inicia expandido.
- Endereço pessoal inicia recolhido em criar e editar.
- O conteúdo permanece montado e os valores do formulário são preservados ao alternar.
- Nenhum desvio do plano.

---

## Evidências

- Teste de regressão: `frontend/src/modules/cliente/components/ClienteForm.test.tsx`.
- Resultado: 10 testes aprovados.
- TypeScript backend/frontend sem erros.

---

## Verificação

- [x] CTs QA relacionados criados: [[05 Arquivo/Nxgest/Bugs/NXG-003/QA/NXG-003 Endereço pessoal inicia aberto/02 - Casos de teste|CT-B01 e CT-B02]].
- [x] Regressão automatizada criada/atualizada.
- [x] Build e testes técnicos verdes.
- [x] Code review aprovado.
- [x] Validação QA concluída.
