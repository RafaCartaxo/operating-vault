# 01 - Análise (NXG-003)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Bugs/NXG-003/QA/NXG-003 Endereço pessoal inicia aberto/01 - Bug|NXG-003 — bug]]  
> **Plano:** [[02 - Plano de correção]]  
> **Implementação:** [[03 - Implementação]]  
> **Code review:** [[04 - Code review]]  
> **Casos de teste QA:** [[05 Arquivo/Bugs/NXG-003/QA/NXG-003 Endereço pessoal inicia aberto/02 - Casos de teste|Casos de teste]]

---

## Veredito

O formulário renderiza os dois blocos de endereço diretamente e não possui estado de expansão; o fix mínimo é tornar cada bloco recolhível, iniciando o endereço pessoal fechado e o comércio aberto.

---

## O que foi confirmado

- `ClienteForm.tsx` renderiza os Cards de comércio e endereço pessoal sempre abertos.
- A MEL-0001 exige estado inicial diferente para cada bloco em criação e edição.
- A correção deve preservar os valores do formulário ao recolher/expandir.

---

## Abordagem e riscos

- Reutilizar o componente de seção recolhível existente, se compatível com o padrão visual.
- Controlar apenas a visibilidade; não desmontar o conteúdo de forma que perca valores ou refs do formulário.
- Criar regressão para criação e edição, preservando a captura GPS e os campos CEP/endereço.
