# 04 - Code review (NXG-031)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Fix:** [[00 README|README do fix]]  
> **Bug QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-031 Transicao segura do deploy e continuidade operacional/01 - Bug|NXG-031 — Transição segura do deploy]]  
> **Plano:** [[02 - Plano de correção|02 - Plano de correção]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-031 Transicao segura do deploy e continuidade operacional/03 - Validação dev|Validação QA]]

**Estado:** revisão técnica DEV concluída; aguardando QA independente.

---

## Checklist

[x] Diff limitado à transição e à documentação operacional autorizadas.
- [x] Causas e regressões cobertas em fixtures e dublês.
- [x] Gates técnicos aplicáveis verdes, com cinco avisos históricos de links.
- [x] CTs QA vinculados; execução funcional independente pendente.

---

## Achados

A revisão identificou necessidade de serializar staging e produção por lock comum, impedir sobrescrita de arquivos ignorados, invalidar marcador antes de staging e bloquear produção sem backup. O host precisa de Git/Bash/flock e o backup instalado deve ser verificado em pré-publicação autorizada. SHA legado sem bootstrap é recusado e requer plano próprio de recuperação. A validade efetiva do painel Cloudflare e dos recursos do host não foi auditada; nenhum deploy real foi executado.

---


## Complemento QA — recuperação legada e GPG

`npm run test:deploy`: 11/11. A recuperação usa controlador por SHA e lock, requer backup, verifica layout e limpeza, recusa conflitos e não executa o deploy legado. Testes extraíram o comando do runbook e verificaram envs sintéticos e recusa em caso de falha. Trata-se exclusivamente de recuperação de checkout: não há prova de rollback do serviço ou operação em host real. GPG usa `pipefail`, `umask 077` e extração em diretório temporário `700`; teste com dois homes sintéticos cobre colisão e falha de descriptografia. Referência detalhada: `.maestro/nxgest-team/NXG-031-DEV-RESULTADO.md`. QA mantém os seis CTs para validação independente.

## Complemento QA — fixture sem histórico

`npm run test:deploy` passou 12/12 após substituir a leitura do commit histórico por fixture legada autocontida com sentinela. A suíte passou novamente em Git sintético sem o objeto `9bff3f7`, com ausência confirmada por `git cat-file`; os testes verificam que o script antigo não é executado na transição e recuperação, e um teste positivo confirma a sentinela em fixture com Docker dublado. Não representa execução real do GitHub Actions. Ver `.maestro/nxgest-team/NXG-031-DEV-RESULTADO.md`.
