# Code review — nova baseline CT-011

> [!info]- Navegação
> [[00 README|Execução]] · [[03 - Implementação|Implementação]] · [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/09 - Nova baseline QA|Adendo QA]]

## Achados

- A política assina e verifica envelopes com chaves do teste; é deliberadamente `fixtureOnly` e não possui âncora confiável de produção. Vínculo GitHub Actions → artefato → imagem executada não foi implementado/demonstrado.
- Harness PG real preparado: verificação de contexto/imagem, limites, isolamento e limpeza por identidade/label exercitados com dublês. Interrupção abrupta ou resposta ambígua pode deixar recursos; sem limpeza ampla. Não substituir CT-N04 por dublê.
- A extração de tar é limitada a fixture privada e não demonstrada como parser operacional de arquivos de produção.
- Verificação de quiescência é dublada. Preflight e retorno preservam NO-GO; caminho positivo operacional condicional não está pronto.

## Decisão

Revisão local identificou bloqueios concretos; manter implementação em andamento, sem declarar DEV_READY_FOR_QA completo ou aprovação funcional. O resultado parcial está registrado para Coordenação e QA; nenhum ensaio real foi executado.

- Guardas PATH/absoluto/subprocessos e rede isolada verificadas antes de 10/10 testes; execução real e proveniência operacional permanecem não comprovadas.

- Achado QA de magic ustar: exigidos bytes `ustar\0` e versão `00`; três negativos com checksum válido e teste positivo passaram na suíte isolada 11/11. O snapshot QA anterior requer nova revisão. Extração parcial e concorrência em ancestrais permanecem limitações; fixtures não provam origem operacional.

- Revisão do achado de ordem: nenhum create/start quando política/ID/major/fonte divergem; teste positivo usa política de fixture. Readiness PG não equivale a health da aplicação; timeout, disco/cópia, colisão e interrupção são simulações. SIGKILL, custódia real, daemon e origem seguem não comprovados.

- Política movida da dependência administrativa para diretório controlado no workspace; loader com hash/decisão separados, dono, permissões e symlinks testado em fixtures. O usuário/checkout continuam fronteira de confiança; hash não autentica origem. 17/17 sob guardas.

- Corrigida remoção recursiva da `.maestro` compartilhada. Criação exclusiva, identidade, colisão, falhas e preservação de sentinela/política foram exercitadas no snapshot sob guardas. Conferência e remoção não são atômicas contra substituição concorrente; não foi executado contra o checkout real.

- Observador é código confiável, não sandbox; timeout não cancela subprocessos nem bloqueio síncrono. Payload não inclui env/senhas, mas workdir contém env sintético. Ensaio real anterior não valida o novo hash; QA deve revisar.


## Adoção staging — continuidade DEV

Review DEV: sem Compose na troca, política/hash externos, payload privado 0600, NoCopy, retenção por ID, pending e rechecagem antes de receipt. Interrupções SIGKILL de processo foram simuladas; não prova durabilidade após queda do host. Imagem/claims e Docker API reais não foram exercitados; QA deve revisar domínio Docker, segurança, concorrência e recuperação independentemente.

## Correção de fotografia após revisão QA

Executor revalida Config+HostConfig, Mounts e Networks da cápsula e da inspeção atual diretamente contra a política, antes dos efeitos. Reprodução sintética da alteração conjunta para cada seção bloqueou sem stop; runner isolado 92/92. Evidência e hashes atuais em `.maestro/nxgest-team/CT011-ADOCAO-STAGING-DEV-RESULTADO.md`. Reteste independente QA pendente; sem aprovação operacional.
