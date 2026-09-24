# 03 - Implementação (MEL-0003)

> [!info]- Navegação QA/DEV
> **Execução:** [[05 Arquivo/Nxgest/Melhorias/MEL-0003/DEV/MEL-0003/00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/MEL-0003/QA/MEL-0003 Expandir e recolher com chevron/01 - Demanda|MEL-0003 — Expandir e recolher com chevron]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Melhorias/MEL-0003/QA/MEL-0003 Expandir e recolher com chevron/04 - Validação dev|Validação QA]]

> Log datado do que foi realmente feito. O plano não é reescrito aqui; desvio vira decisão registrada.

---

## Rodadas

### Rodada 1 — ✅

- Substituídos os textos visuais `Expandir`/`Recolher` por `ChevronRight` e `ChevronDown` nos dois controles de endereço do `ClienteForm`.
- Mantidos `aria-expanded`, nomes acessíveis, clique/teclado e estados iniciais existentes.
- Atualizado o teste do formulário para verificar os nomes acessíveis dos controles.
- Não houve desvio do plano.

Resultado: implementação concluída e pronta para code review.

---

## Evidências

- Arquivos alterados: `frontend/src/modules/cliente/components/ClienteForm.tsx` e `frontend/src/modules/cliente/components/ClienteForm.test.tsx`.

---

## Testes da implementação

- [x] Testes de formulário/UI, quando houver interação.
- [x] Testes de regressão relacionados à demanda.
- [x] Registrar os caminhos dos arquivos de teste e o comando executado: `npm test -- --run frontend/src/modules/cliente/components/ClienteForm.test.tsx`.
- [x] Testes de API/repositório não se aplicam a esta alteração visual.
- [x] Testes unitários de regra/serviço não se aplicam a esta alteração visual.

---

## Verificação

- [x] CTs da demanda relacionados (fonte QA): [[05 Arquivo/Nxgest/Melhorias/MEL-0003/QA/MEL-0003 Expandir e recolher com chevron/03 - Casos de teste|ver casos de teste]].
- [x] Gates aplicáveis do repositório verdes (`audit:ui`, `audit:styles`).
- [x] Documentação sincronizada quando aplicável (`docs:audit`).
- [ ] Commit registrado no README.
