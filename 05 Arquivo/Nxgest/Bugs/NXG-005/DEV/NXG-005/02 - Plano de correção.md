# 02 - Plano de correção (NXG-005)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Nxgest/Bugs/NXG-005/QA/NXG-005 Remover CEP salvo/01 - Bug|NXG-005 — bug]]  
> **Análise:** [[01 - Análise]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Bugs/NXG-005/QA/NXG-005 Remover CEP salvo/03 - Validação dev|Validação QA]]

## Resultado esperado

Apagar um CEP salvo remove o CEP persistido e a localização aproximada derivada, sem remover GPS manual independente.

## Mudança planejada

- Normalizar o payload de edição para enviar `null` quando o usuário limpar o CEP.
- Ajustar a atualização da localização derivada do mesmo bloco.
- Cobrir criação, edição e persistência com testes.

## Fora de escopo

- Tornar CEP obrigatório.
- Alterar consulta de CEP ou navegação.

## Pronto quando

- [ ] CT-B01 aprovado.
- [ ] Testes automatizados atualizados.
- [ ] Code review aprovado.
