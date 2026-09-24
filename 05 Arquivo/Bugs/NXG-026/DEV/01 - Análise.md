# 01 - Análise (NXG-026)

> Fix: [[05 Arquivo/Bugs/NXG-026/00 README|NXG-026]] · Bug: [[05 Arquivo/Bugs/NXG-026/QA/01 - Bug|NXG-026 Bug]]

### Veredito

**Os campos de CPF e telefone não recebem foco no erro porque o formulário não tem referência a eles** — sem referência, ele não consegue levar a tela até o campo. (`ref` = a referência que o React Hook Form precisa de cada input para focar.)

---

### O que está quebrado

Durante a validação foi identificado que, ao criar ou editar um cliente com **CPF inválido** ou **telefone incompleto/inválido** e clicar em **Salvar**, a tela **não sobe/foca no campo com erro**. O erro aparece embaixo do campo, mas o usuário não é levado até ele — em celular (campo fora da tela) isso trava o fluxo.

---

### Causa (confirmada 29/08 no repo)

- O `ClienteForm.tsx` pede para focar o 1º campo com erro no submit (`shouldFocusError: true`, l.113).
- **CPF** (l.365), **telefone** (l.357) e **telefoneComercio** são controlados à mão (`value={form.watch(...)}` + `onChange` com `setValue`) **sem registrar** (`{...form.register(...)}`) — logo o formulário **não tem a referência (`ref`)** deles.
- Sem `ref`, o foco automático **não encontra o campo** → nada acontece.
- Apenas `nome` (l.349) e `comercio` (l.383) são registrados (esses focam normalmente).
- A validação em si funciona (schema acusa `cpfInvalido`/`telefoneInvalido`) — o que falta é só o foco.
- O componente `Field` (`shared/components/Field/Field.tsx`) já encaminha referência (`forwardRef`) — está preparado para receber o `ref` no fix.

---

### Evidências (leitura do código)

- `frontend/src/modules/cliente/components/ClienteForm.tsx:112-113` (`useForm` com `shouldFocusError`)
- `l.365-367` (CPF controlado), `l.357` (telefone controlado), `l.349`/`l.383` (nome/comercio registrados)
- `shared/components/Field/Field.tsx:15-18` (`forwardRef` → `<input ref={ref}>`)
- Nenhum módulo do frontend usa `Controller` (o padrão daqui é espalhar `register`)

---

### Hipóteses descartadas

- Máscara quebrando validação: não — a máscara funciona; o erro é exibido corretamente, só o foco falta.
- Problema de backend: não — é foco no submit (frontend puro).

---

### Perguntas abertas

- Nenhuma (causa confirmada; pode planejar).
