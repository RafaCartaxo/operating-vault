# 01 - Análise (NXG-005)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Bugs/NXG-005/QA/NXG-005 Remover CEP salvo/01 - Bug|NXG-005 — bug]]  
> **Plano:** [[02 - Plano de correção]]  
> **Validação QA:** [[05 Arquivo/Bugs/NXG-005/QA/NXG-005 Remover CEP salvo/03 - Validação dev|Validação QA]]

## Veredito

O formulário envia `undefined` quando o CEP é apagado; a atualização parcial interpreta `undefined` como “não alterar”, preservando o valor anterior.

## Abordagem e riscos

- Diferenciar campo omitido de campo explicitamente limpo.
- Enviar `null` para remover o CEP e a localização aproximada derivada.
- Preservar GPS manual independente e os demais dados do endereço.
