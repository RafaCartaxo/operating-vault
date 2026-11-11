# 02 - Plano de execução (NXG-MEL-0009)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[03 Trabalho/DEV/Nxgest/Execuções/NXG-MEL-0009/00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/01 - Demanda|NXG-MEL-0009 — Backup recuperável e rollback do serviço]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/04 - Validação dev|Validação QA]]

> Congelado na aprovação — alteração posterior vira decisão registrada em 03 - Implementação.md.

---

## O quê

Entregar backup associado e verificável e protocolo seguro de rollback sem operar recursos reais.

## Vínculo e sequência

1. Preservar diff e comprovar stub Docker. 2. Implementar mecanismos e documentação. 3. Testar falhas, recuperação sintética, concorrência e regressão. 4. Registrar evidências e entregar ao QA.

## Escopo aprovado

Scripts, testes e runbook necessários; preservar as alterações NXG-031 e a branch WIP. Sem commit, Docker real, VPS, serviços, imagens, dados ou segredos.

## Decisões

Falha fechada; não substituir backup anterior e não restaurar dados automaticamente. Diferenciar ensaio sintético de prova real.

## Pronto quando

Critérios C1–C8 têm evidências técnicas adequadas e limitações documentadas; execução de CTs e aprovação são exclusivas de QA.

### Testes desta etapa

- Docker e rede interceptados por dublês antes de cada caso.
- Falhas injetadas, concorrência, conteúdo sintético e regressão NXG-031.

