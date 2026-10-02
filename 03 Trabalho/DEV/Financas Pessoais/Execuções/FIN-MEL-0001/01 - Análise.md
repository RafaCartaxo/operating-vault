# 01 - Análise — FIN-MEL-0001

> [!info]- Navegação
> **Execução:** [[00 README|README da execução]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]

## Veredito

A próxima entrega deve ser um frontend web responsivo, mantendo o backend Go como API e permitindo uso posterior por URL no celular.

## O que foi confirmado

- O backend possui `POST /api/lancamentos` validado por testes e smoke test.
- A API recebe valores em centavos e data no formato `AAAA-MM-DD`.
- O projeto ainda não possui frontend.
- O fluxo técnico esperado está documentado em `financas-pessoais/docs/fluxos.md`.
- A interface deve ser mobile-first e preparada para futura instalação como PWA.

## Abordagem e riscos

- Usar React + TypeScript + Vite, reaproveitando conhecimento e padrões do NX Gest.
- Criar uma camada de service para a API, sem chamadas HTTP espalhadas pelos componentes.
- Usar formulário com validação de interface e mensagens amigáveis.
- Não duplicar regras financeiras no frontend; a validação definitiva permanece no Go.
- Garantir configuração de URL da API por ambiente.

## Alternativas descartadas

- Svelte: tecnicamente viável, mas reduziria o reaproveitamento do stack já conhecido.
- Colocar regras de parcelas no frontend: geraria divergência com o backend.
- Começar pelo dashboard: não valida o fluxo principal de entrada de dados.

## Perguntas abertas

- Definir se a primeira tela será uma página dedicada ou um modal/quick action.
- Definir a estratégia visual final dos componentes, mantendo o design system documentado.
