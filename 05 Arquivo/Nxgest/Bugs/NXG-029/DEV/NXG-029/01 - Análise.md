# 01 - Análise (NXG-029)

> [!info]- Navegação QA/DEV
> **README DEV:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/00 README|README DEV]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/01 - Bug|Demanda QA]]  
> **Casos de teste QA:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/02 - Casos de teste|Casos de teste QA]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/03 - Validação dev|Validação QA]]  
> **Épico:** [[04 Projetos/Nxgest/Epicos/NXG-EPIC-0001 Organizacao do NX Gest/00 README|Épico]]  
> **Análise:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/01 - Análise|Análise]]  
> **Plano:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/02 - Plano de correção|Plano]]  
> **Implementação:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/03 - Implementação|Implementação]]  
> **Code review:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/04 - Code review|Code review]]  

## Veredito

Causa confirmada: o `source` do ambiente gerado tratava o valor com espaço como sintaxe shell; a correção isolada é viável.

## O que foi confirmado

O gerador escrevia `MAIL_FROM_NAME=NX Gest` e carregava o arquivo com `source`, o que podia falhar e executar conteúdo arbitrário.

## Abordagem e riscos

`scripts/staging-env.sh` gera e carrega configurações como dados via Bash; `scripts/deploy-staging.sh` chama funções versionadas. O novo valor é gerado entre aspas e o legado sem aspas com espaço é aceito. Não executar deploy nem ler envs reais. O carregador aceita apenas chaves conhecidas e rejeita chaves/escapes não suportados; a compatibilidade com configurações legadas reais não foi observada.

Alternativas consideradas: Continuar usando `source` de arquivo de configuração mantém execução arbitrária; o helper Node introduziria requisito não demonstrado no host. Foram substituídos por Bash.
