# 03 - Implementação (MEL-0002)

> [!info]- Navegação QA/DEV
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/MEL-0002/QA/MEL-0002 Cliente Documento/01 - Demanda|Demanda]]  
> **Plano:** [[02 - Plano de execução]]  
> **Code review:** [[04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Melhorias/MEL-0002/QA/MEL-0002 Cliente Documento/04 - Validação dev|Validação]]

## Rodadas

### Rodada 1 — ✅

- Adicionado `clientes.documento` com migração idempotente.
- Propagado Documento na entidade, schemas Zod, casos de uso, repositório e contrato de API.
- Adicionado campo abaixo do CPF no formulário de criação/edição, sem máscara, com limite de 20 caracteres.
- Exibição do Documento na ficha do cliente e traduções pt-BR/en/es.
- Edição sem valor normaliza para `null`; clientes existentes continuam compatíveis.

## Evidências

- `npm test -- --run frontend/src/modules/cliente/components/ClienteForm.test.tsx` — 8 testes aprovados.
- `npm run build` — backend e frontend compilados.
- `npm run audit:ui` — aprovado.
- `npm run audit:styles` — aprovado.
- `npm run docs:audit` — nenhuma divergência.

## Verificação

- CTs do pacote QA: CT-001 até CT-008 (execução registrada na validação QA).
- [x] Gates aplicáveis do repositório verdes.
- [x] Documentação sincronizada quando aplicável.
- [ ] Commit registrado no README.
