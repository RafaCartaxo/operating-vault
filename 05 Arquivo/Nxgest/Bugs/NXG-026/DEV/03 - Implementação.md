# 03 - Implementação (NXG-026)

> Fix: [[05 Arquivo/Nxgest/Bugs/NXG-026/00 README|NXG-026]] · Plano: [[05 Arquivo/Nxgest/Bugs/NXG-026/DEV/02 - Plano de execução|02 - Plano de execução]] · Review: [[05 Arquivo/Nxgest/Bugs/NXG-026/DEV/04 - Code review|04 - Code review]]

> Log datado do que foi **realmente feito** (o plano em `02 - Plano.md` não muda aqui; desvio vira decisão registrada).

## Rodadas

### Rodada 1 — ✅ executada (29/08)
- Aplicado o plano: `{...form.register("cpf"|"telefone"|"telefoneComercio")}` mantendo máscaras.
- Regressão nova (2 testes, `document.activeElement`).
- Controle negativo: sem o fix os 2 testes **falham**; com o fix **passam** (prova que pegam o bug).

---

## Evidências

- Regressão: `ClienteForm.test.tsx` — CPF inválido (+ obrigatórios válidos) + Salvar → `document.activeElement` = CPF, `onSubmit` **não** chamado; telefone idem. ✅ passando (controle negativo confirma que falham sem o fix).
- Gates (29/08): `tsc` ✅ 0 · `npm test` ✅ **197/197** (40 arquivos) · `audit:ui` ✅ · `audit:styles` ✅ · `build` ✅.

---

## Verificação

> Os CTs moram no card do bug (fonte única). Executar cada um e marcar o resultado **lá**.

- [[05 Arquivo/Nxgest/Bugs/NXG-026/QA/01 - Bug#CT-B01 CPF inválido foca o campo|CT-B01]] · [[05 Arquivo/Nxgest/Bugs/NXG-026/QA/01 - Bug#CT-B02 Telefone incompleto foca o campo|CT-B02]] · [[05 Arquivo/Nxgest/Bugs/NXG-026/QA/01 - Bug#CT-B03 Telefone do comércio inválido foca o campo|CT-B03]] · [[05 Arquivo/Nxgest/Bugs/NXG-026/QA/01 - Bug#CT-B04 Mesmo comportamento em criar e editar|CT-B04]]

- [ ] Manual: criar/editar com CPF e telefone inválidos → foco/scroll para o campo
- [ ] Docs: entrada no `UPDATES.md`
- [ ] Commit: `fix(cliente): registrar cpf/telefone para shouldFocusError focar (NXG-026)`
- [ ] **Push/deploy só após os CTs manuais locais verdes** — decisão do dono (nada sobe sem mandar)
