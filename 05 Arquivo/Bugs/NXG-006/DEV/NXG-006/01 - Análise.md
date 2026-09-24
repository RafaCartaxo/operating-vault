# 01 - Análise (NXG-006)

> [!info]- Navegação QA/DEV
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[05 Arquivo/Bugs/NXG-006/QA/NXG-006 CEP inválido não exibe mensagem/01 - Bug|NXG-006 — bug]]  
> **Plano:** [[02 - Plano de correção]]  
> **Validação QA:** [[05 Arquivo/Bugs/NXG-006/QA/NXG-006 CEP inválido não exibe mensagem/03 - Validação dev|Validação QA]]

## Veredito

O handler retorna imediatamente quando o CEP ainda não tem oito dígitos; por isso, não há feedback para formato inválido.

## Abordagem e riscos

- Exibir feedback claro para formato inválido sem interromper a digitação a cada caractere.
- Manter a mensagem de CEP não encontrado e indisponibilidade.
- Permitir corrigir ou salvar sem CEP conforme a regra da MEL-0001.
