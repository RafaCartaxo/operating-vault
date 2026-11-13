# NXG-036 — Implementação e evidências

**IMPLEMENTAÇÃO PARCIAL — não DEV_READY_FOR_QA.** A revisão identificou que colisão de pin é detectada somente após `docker image load`; o critério CT-B04 exige que a colisão não altere recursos. A entrada normal de staging e o bootstrap de adoção só conhecem o ID efetivo após o load; falta vincular uma verificação anterior ao load que também permita reusar pin exato sem supor equivalência index/config Docker 29/26. Não há aprovação de CT. Branch `fix/nxg036-image-retention` criada no objeto `bed9a8338ddf7cdfc5936153bd546e6a3d9d9dae`, cuja árvore rastreada coincidia com a branch anterior. WIP `14f3e506f918f314a21919fec6f2ca0017cd6a4c` preservado.

O helper `retain-verified-image.sh` usa lock 9, identifica e verifica pin `nxgest-retained:<sha>` para o ID fornecido pelo caminho autenticado, recusa colisão/inspeção inconclusiva, e remove somente a tag temporária após o pin e a origem coincidirem. Os três fluxos o invocam antes da troca de serviço; revalidam a imagem após health. O loader prova ausência da tag por listagem bem-sucedida antes do load e continua recusando preexistência. Baseline verifica tar conservado, pin e runtime/health, publica marker sem sobrescrita e arquiva pending próprio por hard link com verificação de dispositivo/inode/owner/modo; colisão e falhas não geram sucesso. Retorno posterior com marker continua bloqueado. O pin opera no domínio confiável do daemon e lock cooperativo, sem provar origem por si mesmo.

Comando: `bash scripts/test-corrections-isolated.sh`. Guardas PATH, caminhos absolutos e subprocessos para Docker/curl/ssh/scp/gh, namespace de rede e ausência do socket host confirmados antes dos testes; resultado **98/98**, exit 0. [[evidencia-testes-sinteticos.log|Log sintético]]. Rodada anterior passou 97/97; a primeira falhou 14/92 antes de adaptar fixtures. Uma rodada 96/96 teve exit 1 ao editar simultaneamente o runner e não é usada como evidência final. `git diff --check` limpo para rastreados. Não executados Docker real, GH, rede, serviço, testes reais ou suíte 215.

Cobertura DEV: modelo último vínculo e pin novo/exato/colisão/falhas no helper; loader preexistente, baseline com saúde/lock, pending arquivado, colisão e troca de inode; fluxo CI–staging–produção dublado e adoção com falhas, lock e preservação. O plano histórico é [[05 - Reparo histórico (plano)]], não um reparo executável; CT-B11/B12 e todos os demais CTs continuam aguardando avaliação do QA. Testes não comprovam o daemon, persistência em perda abrupta de energia ou operação histórica. Não se alterou nem aprovou BA10/CT-011/rollback.

## SHA-256 dos arquivos do delta

- `scripts/deploy-staging.sh`: `9307209f6c0493b17ae2123a215630644a300a69b702b01f778a053fac56d1cf`
- `scripts/deploy-transition.check.mjs`: `9eba26ca8b827941fa500331ce347145cef4c73210d99ce16f3c727dd898381b`
- `scripts/initial-baseline.check.mjs`: `914bfd8444edc8dc3ef803350d2e669c2b29713dc4fc3f3fbcb22ee42e244431`
- `scripts/initial-baseline.sh`: `877e4be2353821df8141ad1f2dd6eff91d22926094c22aea6b7c1cd220329c8b`
- `scripts/load-verified-image.check.mjs`: `cbd650d9a4de98bde36690d6eb9b527853c8bfe1a07d98126432c5db94075da5`
- `scripts/load-verified-image.sh`: `aa31c4f7cc41e32e9043425a57c0842ee8196ed7f5a298d3c11d748832b6cbdd`
- `scripts/staging-adoption-capsule.check.mjs`: `0cbf8a201ff71f6edc1b541ddb18ffc47dd6b5fea2081d51b1ba177cdebeb66d`
- `scripts/staging-adoption-execute.sh`: `5ccae07af439aa8c2aad056e47d34c8addb250670006d0c4184490ee38d1eef5`
- `scripts/test-corrections-isolated.sh`: `117970ffc18a81d4205174455c6d2503139eb10bdfa93184c9372700b8b95e61`
- `scripts/guards/gh`: `6f47211f5ddcb1bbdd822c37d05cb766d5f9e9c1fd01fda52ac0a3eea962c295`
- `scripts/retain-verified-image.sh`: `68eb19bd763dac0817225b72899b0a26445fb3bae75eababe8db742cc49845ff`
- `scripts/retain-verified-image.check.mjs`: `4625fc5b2325d69d34cd433f9b9d29435414471cda38a5f49f0b63a4ca03ee58`
