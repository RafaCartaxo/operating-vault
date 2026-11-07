# 02 - Plano de correção (NXG-029)

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

## Resultado esperado

Gerar e reutilizar staging com espaços sem avaliar conteúdo do arquivo como shell, inclusive o formato legado conhecido.

## Mudança planejada

- Arquivos e abordagem: `scripts/deploy-staging.sh`, `scripts/staging-env.sh`, testes e documentação; preservar arquivo existente e valores ao reutilizá-lo.
- Decisão: Após revisão QA, remover o helper Node e usar Bash e ferramentas já empregadas pelo deploy; não acessar a VPS.
- Regressões: testes controlados em `scripts/safety-check.mjs` e smoke em recursos próprios quando aplicável.

## Fora de escopo

Deploy, push, VPS, recursos e envs reais, aprovação dos CTs e fechamento do épico.

## Pronto quando

- [ ] CTs executados e decididos por QA: [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/02 - Casos de teste|casos de teste]].
- [x] Regressão automatizada executada.
- [x] Gates técnicos aplicáveis executados, com limitações registradas.
- [x] Code review técnico concluído.
