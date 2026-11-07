# 01 - Análise (NXG-030)

> [!info]- Navegação QA/DEV
> **README DEV:** [[05 Arquivo/Nxgest/Bugs/NXG-030/DEV/NXG-030/00 README|README DEV]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Bugs/NXG-030/QA/NXG-030 Smoke protege banco e interpreta opcoes/01 - Bug|Demanda QA]]  
> **Casos de teste QA:** [[05 Arquivo/Nxgest/Bugs/NXG-030/QA/NXG-030 Smoke protege banco e interpreta opcoes/02 - Casos de teste|Casos de teste QA]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Bugs/NXG-030/QA/NXG-030 Smoke protege banco e interpreta opcoes/03 - Validação dev|Validação QA]]  
> **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|Épico]]  
> **Análise:** [[05 Arquivo/Nxgest/Bugs/NXG-030/DEV/NXG-030/01 - Análise|Análise]]  
> **Plano:** [[05 Arquivo/Nxgest/Bugs/NXG-030/DEV/NXG-030/02 - Plano de correção|Plano]]  
> **Implementação:** [[05 Arquivo/Nxgest/Bugs/NXG-030/DEV/NXG-030/03 - Implementação|Implementação]]  
> **Code review:** [[05 Arquivo/Nxgest/Bugs/NXG-030/DEV/NXG-030/04 - Code review|Code review]]  

## Veredito

Causas confirmadas: o smoke aceitava `DATABASE_URL` genérica para recriação e ignorava `--no-recreate` na primeira posição.

## O que foi confirmado

O alvo só excluía `postgres`, podendo atingir outro banco; o parser examinava a opção apenas após o primeiro argumento. A identidade de processos também precisava impedir sinalização alheia.

## Abordagem e riscos

Exigir `SMOKE_DATABASE_URL` explícita, loopback, porta dedicada diferente de 5432/5433, nome de teste e URL sem parâmetros. Validar opções antes de operações; supervisor em grupo próprio identificado por `ps`, início e nonce. A proteção depende do banco dedicado informado e de portas isoladas. Identidade não verificável falha fechado; PID malformado é preservado. `ps` foi testado em Linux, não em macOS.

Alternativas consideradas: Aceitar apenas nome sugestivo ou PID numérico não identifica um alvo/processo com segurança. Não usar `DATABASE_URL` genérica como autorização.
