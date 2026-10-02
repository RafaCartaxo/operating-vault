# 01 - Análise — FIN-MEL-0004

> [!info]- Navegação QA/DEV
> **README:** [[00 README]]  
> **Demanda QA:** [[03 Trabalho/QA/Financas Pessoais/Demandas/Melhorias/FIN-MEL-0004 Refinamentos responsivos dos campos/01 - Demanda|Demanda QA]]  
> **Plano:** [[02 - Plano de execução]]

## Veredito

A correção é exclusivamente de frontend. O backend e os contratos da API permanecem inalterados.

## Abordagem

- Controlar o layout do campo de data com um acionador nativo limitado ao container.
- Garantir fonte mínima de 16px em campos mobile para evitar zoom automático no iOS.
- Alinhar o reset mensal ao seletor.
- Corrigir o cursor da primeira digitação monetária.

