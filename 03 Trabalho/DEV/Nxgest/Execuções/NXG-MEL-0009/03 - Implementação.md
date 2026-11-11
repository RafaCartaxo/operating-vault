# 03 - Implementação (NXG-MEL-0009)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Execução:** [[03 Trabalho/DEV/Nxgest/Execuções/NXG-MEL-0009/00 README|README da execução]]  
> **Demanda QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/01 - Demanda|NXG-MEL-0009 — Backup recuperável e rollback do serviço]]  
> **Plano:** [[02 - Plano de execução|02 - Plano de execução]]  
> **Code review:** [[04 - Code review|04 - Code review]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/04 - Validação dev|Validação QA]]

> Log datado do que foi realmente feito. O plano não é reescrito aqui; desvio vira decisão registrada.

---

## Rodadas

### Rodada 1 — 2026-11-11

- `scripts/backup-nxgest.sh`: conjunto privado com dump, anexos, metadados, hashes, imagem etiquetada e marca final; lock compartilhado e falha fechada. `scripts/verify-backup.sh` verifica associação e integridade.
- `scripts/rollback-preflight.sh` confere imagem e evidências declaradas de configuração/schema e decisão de dados; `scripts/verify-rollback-return.sh` confere declaração de integridade e health. São verificações documentais e sintéticas, sem executar restore ou provar compatibilidade.
- `scripts/deploy.sh` exige backup instalado correspondente e preflight antes de promover; remove prune automático. `docs/engineering/09-BACKUP-ROLLBACK.md` descreve procedimento e checklist. CI/CD e `package.json` incluem `test:backup`.
- `scripts/backup-recovery.check.mjs` exercita fixtures isoladas; `scripts/deploy-transition.check.mjs` adapta dublês para integração com os gates, mantendo cenários NXG-031.
- Diff NXG-031 foi preservado em `.maestro/nxgest-team/nxg-mel-0009/` antes das alterações; alguns arquivos comuns receberam acréscimos MEL-0009. HEAD `c7b65c8ddd85efde4db7f075ca03d95a7c6c5c38`; branch WIP `14f3e506f918f314a21919fec6f2ca0017cd6a4c`. Sem commit.

## Evidências

- `npm run test:backup`: 10/10 testes sintéticos; cobre falhas de dump/tar/inspeção/tag/publicação, corrupção, mistura, colisão, concorrência, preflight, health e integração de deploy. Restore de banco é dublê que confere conteúdo fictício, não PostgreSQL real; anexos fictícios são extraídos em fixture isolada.
- `npm run test:deploy`: 12/12 com dublês; o preflight MEL-0009 é dublado nessa suíte e exercitado com código real na integração sintética de `test:backup`. `npm run test:safety`: 9/9. `npm test`: 215/215; `npm run build` passou; auditorias de documentação, links, UI, estilos e módulos passaram, com cinco avisos históricos de órfãos na auditoria de links.
- Comandos e saídas finais: `.maestro/nxgest-team/nxg-mel-0009/` (logs locais de testes); `bash -n` e `git diff --check` executados. CTs oficiais: [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/03 - Casos de teste|CT-001 a CT-014]]; [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/06 - Gate de integridade QA|gate QA de integridade]]. Nenhum CT foi aprovado pelo DEV.

### Desvio de isolamento

Em uma tentativa anterior do caso de herança de lock, o PATH não reteve o dublê e o executável Docker real foi invocado, em desacordo com a proibição de chamadas ao CLI real. A conexão foi direcionada exclusivamente ao socket inexistente `unix:///nxg0009-inexistente` e falhou; nenhum daemon foi contatado. Corrigiu-se a fixture para substituir referências Docker por caminho absoluto ao dublê e verificar interceptação antes dos casos; a suíte posterior passou. O ocorrido é registrado para avaliação independente, sem alegar conformidade retroativa.

### Ambiente e smoke check

Não houve smoke real nem acesso a daemon, VPS, rede externa ou dados reais. As verificações de health usam `curl` dublado. A listagem `pg_restore -l` e o ensaio de dublê não comprovam restauração real nem consistência temporal transacional entre banco e anexos.

## Testes da implementação

- [x] Casos sintéticos de backup, falha, concorrência, evidências e integração.
- [x] Regressões sintéticas NXG-031 e gates pertinentes.
- [ ] Restore PostgreSQL real e operação real: fora da autorização, pendentes de futura decisão operacional.

## Verificação

- [x] Referência aos 14 CTs e aos limites entregue ao QA.
- [x] Documentação DEV e runbook sincronizados.
- [ ] CTs funcionais e aprovação: aguardam QA independente.
- Commit não autorizado nesta rodada.
