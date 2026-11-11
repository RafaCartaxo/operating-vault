# 04 - Code review (NXG-MEL-0009)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[03 Trabalho/DEV/Nxgest/Execuções/NXG-MEL-0009/00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/01 - Demanda|NXG-MEL-0009 — Backup recuperável e rollback do serviço]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Implementação:** [[03 - Implementação|03 - Implementação]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/04 - Validação dev|Validação QA]]

**Estado:** revisão técnica local concluída com ressalvas; funcionalidade aguardando QA independente.

## Checklist

- [x] Escopo, plano e contratos C1–C8 confrontados com código e evidências sintéticas.
- [x] Backup falha fechado, preserva conjunto anterior e usa o lock compartilhado; imagem anterior recebe tag e prune automático foi removido.
- [x] Decisão de aplicação/dados e evidências de schema/configuração são explícitas; nenhuma restauração é automática.
- [x] Regressão NXG-031 exercitada com limitações de dublê descritas na implementação.
- [x] Ausência de segredos testada com marcador sintético; envs e recursos reais não foram lidos.
- [ ] Compatibilidade real, restauração PostgreSQL, integridade de dados e execução operacional permanecem sem prova e fora do escopo.

## Achados

- A versão anterior aceitava falha na coleta de anexos e poderia podar a imagem anterior; o código local passou a falhar fechado e preservar tag.
- Uma tentativa anterior chamou o CLI Docker real com socket inexistente; nenhum daemon foi contatado. Fixture corrigida para referência absoluta ao dublê; detalhes em [[03 - Implementação]].
- Evidência de schema, configuração, SHA anterior e integridade de retorno é declaração do operador, não verificação independente de conteúdo. `pull-backup.sh` antigo não transporta o novo formato; fluxo externo permanece pendente de autorização.
- Dump e anexos são coletados sequencialmente; consistência de ponto no tempo depende de procedimento operacional futuro. Uso real requer Linux `/proc`, utilitários documentados e instalação autorizada do script.

## Decisão

- [x] Revisão técnica local concluída; `DEV_READY_FOR_QA` para avaliação independente.
- [ ] Aprovação funcional, execução real, commit e fechamento permanecem pendentes.

Pacote QA: [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/00 README|demanda e plano]], [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/03 - Casos de teste|14 CTs]] e [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/06 - Gate de integridade QA|gate de integridade]].
