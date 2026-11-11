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
