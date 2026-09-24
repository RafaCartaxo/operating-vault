# 02 - Plano (NXG-026)

> Fix: [[05 Arquivo/Nxgest/Bugs/NXG-026/00 README|NXG-026]] · Bug: [[05 Arquivo/Nxgest/Bugs/NXG-026/QA/01 - Bug|NXG-026 Bug]]

> Congelado na aprovação — só muda por decisão registrada (ver `03 - Implementação.md`).

### O quê

**Dar aos 3 campos (CPF, telefone, telefone do comércio) a referência que o formulário precisa**, para que salvar com erro leve a tela até o campo. Nada muda no que o usuário digita nem nas regras — só o foco passa a funcionar.

---

## Plano

- **Arquivos a tocar:**
  - `frontend/src/modules/cliente/components/ClienteForm.tsx` — registrar os 3 campos (`{...form.register("cpf"|"telefone"|"telefoneComercio")}`), **mantendo** o valor controlado e a máscara (`value` + `onChange` com `setValue` e `clearErrors` ficam iguais).
  - `frontend/src/modules/cliente/components/ClienteForm.test.tsx` — regressão nova.
- **Mudança mínima:** só a referência (`ref`) chega ao `<input>`; a submissão continua lendo o valor do jeito atual; o `onBlur` do registro só marca o campo como tocado. Máscaras, regras de validação, backend e config: **intactos**.
- **Fora de escopo (certo):** `foto`/GPS/coordenadas (não têm erro de validação) · backend · regras de validação · máscaras.

---

## Decisões

- **Registrar espalhando vs componente `Controller`:** escolheu-se espalhar o `register` — o repo **não usa `Controller`** em nenhum módulo, e o `Field` já encaminha referência (mesmo padrão de `nome`/`comercio`).
- **Não mudar a ordem de erros:** o foco vai para o **1º erro**; o fix só entrega a referência aos campos, sem reordenar validação.

---

## Pronto quando

- Salvar com CPF inválido foca o CPF (criar e editar).
- Salvar com telefone inválido foca o telefone (criar e editar).
- Nada mais mudou (máscara, validação, backend iguais).
