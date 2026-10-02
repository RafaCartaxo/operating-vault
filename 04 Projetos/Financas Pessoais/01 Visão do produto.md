---
projeto: financas-pessoais
tipo: visao
---

# Visão do produto

## Problema

O planejamento financeiro atual é útil, mas exige edição manual de faturas, parcelas, recorrências e saldos em vários trechos de Markdown.

## Solução

Uma aplicação local com entrada rápida de dados, cálculo automático e geração de visões mensais no vault financeiro.

## Princípios

- Registrar cada informação uma única vez.
- Usar SQLite no desenvolvimento e banco persistente com backup na produção.
- Manter o vault como camada de leitura, histórico e relatórios.
- Separar coordenação, implementação e dados financeiros.
- Começar pequeno com um fluxo completo antes de ampliar o domínio.
