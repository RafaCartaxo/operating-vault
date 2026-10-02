---
projeto: financas-pessoais
tipo: decisoes
---

# Decisões do projeto

## DEC-001 — Projeto separado do NX Gest

Finanças pessoais será um produto separado. O NX Gest é empresarial/multiempresa e não deve receber esse domínio neste momento.

## DEC-002 — Backend em Go

O backend será escrito em Go por ser uma aplicação local, pequena, independente e adequada a um binário simples.

## DEC-003 — Três espaços com responsabilidades distintas

- `operating-vault`: coordena o trabalho.
- `financas-pessoais`: implementa o software.
- `financas-vault`: armazena e apresenta os dados financeiros.

## DEC-004 — Aplicação web mobile-first

O sistema será desenvolvido localmente, mas o destino é uma aplicação web responsiva, acessível por URL HTTPS no celular. O frontend deverá evoluir para PWA e o backend deverá ser preparado para implantação remota, autenticação, banco persistente e backup.
