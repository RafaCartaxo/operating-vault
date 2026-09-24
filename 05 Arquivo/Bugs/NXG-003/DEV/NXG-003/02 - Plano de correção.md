# 02 - Plano de correção (NXG-003)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Bugs/NXG-003/QA/NXG-003 Endereço pessoal inicia aberto/01 - Bug|NXG-003 — bug]]  
> **Análise:** [[01 - Análise]]  
> **Implementação:** [[03 - Implementação]]  
> **Code review:** [[04 - Code review]]  
> **Casos de teste QA:** [[05 Arquivo/Bugs/NXG-003/QA/NXG-003 Endereço pessoal inicia aberto/02 - Casos de teste|Casos de teste]]

> Congelado na aprovação. Alteração posterior vira decisão registrada em `03 - Implementação.md`.

---

## Resultado esperado

Endereço pessoal inicia recolhido em criar e editar; comércio inicia expandido; expandir o pessoal preserva todos os dados.

---

## Mudança planejada

- **Arquivo principal:** `frontend/src/modules/cliente/components/ClienteForm.tsx`.
- **Abordagem mínima:** adicionar estado de expansão por bloco e componente recolhível sem alterar payload ou regras de endereço.
- **Regressão a proteger:** foco, valores preenchidos, CEP, GPS e comportamento atual do comércio.

---

## Fora de escopo

- Alterar regras de CEP, GPS, navegação ou persistência.
- Mudar a ordem ou o conteúdo dos campos.

---

## Pronto quando

- [ ] CT-B01 e CT-B02 executados.
- [ ] Regressão automatizada criada ou atualizada.
- [ ] Gates do repositório verdes.
- [ ] Code review aprovado.
