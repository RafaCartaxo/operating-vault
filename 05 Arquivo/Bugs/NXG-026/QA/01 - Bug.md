---
prioridade: media
status: feito
modulo: cliente
plano: ""
origem: observado
ambiente: prod
pai: ""
data_inicio: 2026-08-29
data_fim: 2026-08-29
responsavel: ""
---
# CPF e telefone inválido não foca o campo ao salvar (cliente)

### Descrição

Durante validação foi identificado que, ao criar ou editar um cliente com **CPF inválido** ou **telefone incompleto/inválido** e clicar em **Salvar**, a tela **não sobe/foca no campo com erro** — o usuário não é levado ao campo incorreto para corrigir.

---

### Passo a passo para reproduzir

**Dado** a tela de criar/editar cliente (`/clientes/novo` ou `/clientes/:id/editar`)
**E** CPF inválido (ex.: `111.111.111-11`) **ou** telefone incompleto/inválido (ex.: DDD incompleto)
**E** demais campos obrigatórios válidos (para o campo ser o 1º erro)
**Quando** clico em **Salvar**
**Então** o erro aparece sob o campo, mas não há foco/scroll até ele

---

### Evidências

- (a capturar na validação: screencast/limite de scroll)

---

### Resultado Esperado

Salvar com erro rola/foca o **primeiro campo com erro** (`shouldFocusError`).

---

### Critérios de aceite

- [ ] CPF inválido → foco/scroll para o CPF (criar e editar)
- [ ] Telefone incompleto → foco/scroll para o telefone (criar e editar)
- [ ] Telefone do comércio → idem

---

### Casos de Teste Básicos

#### **CT-B01 CPF inválido foca o campo**

**Dado** cliente com CPF inválido e demais campos ok
**Quando** clico em Salvar
**Então** o campo CPF recebe foco (e a tela rola até ele)

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B02 Telefone incompleto foca o campo**

**Dado** cliente com telefone incompleto/inválido e demais campos ok
**Quando** clico em Salvar
**Então** o campo telefone recebe foco (e a tela rola até ele)

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B03 Telefone do comércio inválido foca o campo**

**Dado** cliente com telefone do comércio inválido e demais campos ok
**Quando** clico em Salvar
**Então** o campo do telefone do comércio recebe foco

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B04 Mesmo comportamento em criar e editar**

**Dado** CT-B01/B02/B03 validados na criação
**Quando** executo os mesmos passos na edição (`/clientes/:id/editar`)
**Então** o foco/scroll acontece igual

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Ambiente: `dev` (local) · `prod` (reportado em uso)
- Versão: main (28-29/08)

---

### Informações adicionais

- **Fix:** [[05 Arquivo/Bugs/NXG-026/00 README|05 Arquivo/Bugs/NXG-026]] (pasta do fix: análise, plano, review, verificação)
- **Causa provável (investigação 29/08):** `ClienteForm.tsx` usa `shouldFocusError: true` (l.113), mas **CPF** (l.365), **telefone** (l.357) e **telefoneComercio** são controlados via `watch`+`onChange` **sem `register`** — o RHF não tem `ref` deles e não consegue focar no submit inválido. Apenas `nome` (l.349) e `comercio` (l.383) são registrados. O `shouldFocusError` então só foca campos registrados.
- Demanda relacionada: —
- Observações: fix = dar `ref`/registrar os campos controlados (ou `Controller`) para o `shouldFocusError` focar.
- Histórico:
  - 2026-08-29 - 🐛 Bug confirmado (reportado: CPF; confirmado também telefone) e cadastrado
