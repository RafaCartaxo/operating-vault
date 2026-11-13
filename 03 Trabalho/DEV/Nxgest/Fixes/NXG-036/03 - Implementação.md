# NXG-036 — Implementação e evidências

**DEV_READY_FOR_QA**, aguardando reteste independente; nenhum CT funcional aprovado pelo DEV. Branch `fix/nxg036-image-retention` em `bed9a8338ddf7cdfc5936153bd546e6a3d9d9dae`; branch WIP continua em `14f3e506f918f314a21919fec6f2ca0017cd6a4c`. Sem commit, push ou alteração de recursos reais.

## Fechamento do achado CT-B04

`load-verified-image.sh` valida lock, digest do tar autenticado, manifest único com tag esperada e arquivo de configuração único e regular, nome `blobs/sha256/<hash>`, bytes e plataforma. O preflight restringe o modelo ao daemon confiável Docker Engine `26.1.3|linux|amd64`, driver `overlay2` e DriverStatus estruturado sem indicação de containerd/snapshotter. A comparação de `sha256` dos bytes da configuração com o ID é suportada somente nesse domínio; não se igualam genericamente índice, manifest e config. O diagnóstico histórico `staging-bed9-runtime-diagnostic.json` observou essa igualdade no Docker 26.1.3, porém não comprova o driver atual nem esta implementação: verificar o backend real por procedimento autorizado antes de uso. Modelo, tar ou resultado desconhecido recusam antes do load. O ID efetivo é revalidado depois do load.

Sob lock e antes de qualquer load, preflight consulta listagem e, se houver pin `nxgest-retained:<sha>`, exige ID único exatamente igual ao config digest e inspeção confirmatória; tag temporária preexistente segue recusada. `deploy-bootstrap.sh` chama o preflight do SHA candidato antes de checkout/pending na adoção e antes de pending no staging; `initial-baseline.sh` antes do pending de produção. O loader reexecuta a verificação imediatamente antes do load. Pin exato pode ser reutilizado; colisão ou ambiguidade falha sem chamadas Docker mutáveis. O helper preserva/revalida pin antes de retirar somente tag própria.

Baseline revalida tar, pin, imagem e health; publica marker exclusivo e arquiva pending próprio somente após validar dispositivo/inode/owner/modo. Estados parciais preservam pendência ou evidência de conclusão e impedem reentrada indevida. O plano de reparo histórico continua em [[05 - Reparo histórico (plano)]], sem execução nem exclusão do pending real.

## Testes e limites

`bash scripts/test-corrections-isolated.sh`: **100/100**, exit 0; guardas PATH/absoluto/subprocessos Docker, curl, ssh, scp e gh, namespace sem rede e ausência do socket host confirmados antes dos testes. [[evidencia-preload-sintetico.log|Log da rodada final]]. Sentinel e política sintética preexistentes preservadas. `git diff --check` limpo; sem espaços finais nos três arquivos novos. Não se executou Docker/daemon, GH, SSH, rede, testes reais ou suíte de 215. A rodada intermediária 100/100 antecede os últimos ajustes e não é a evidência final.

Casos DEV: loader aceita pin exato e recusa divergente antes de `load/tag/rm`, tag temporária preexistente, versão/backend não suportado, arquivo de configuração duplicado/adulterado e tar divergente; dublês integrados de staging, adoção e baseline recusam colisão antes de chamadas Docker mutáveis e pending. Também foram exercitados modelo de última tag, pin, health, lock, marker, conclusão/troca do pending e falhas preexistentes dos fluxos. Os 13 CTs, inclusive plano histórico CT-B11/B12, continuam para QA independente; os dublês não demonstram daemon real, durabilidade após perda de energia nem uma operação histórica. Origem de imagem depende do verificador autenticado anterior; hash de config sozinho não é proveniência. BA10 e rollback permanecem NO-GO até gates e provas próprios.

## SHA-256 dos arquivos do delta

- `scripts/deploy-bootstrap.sh`: `13d87450aea62d3a8e84a5467ee0996898afb5f2362cde3138102cbbbe99eb4e`
- `scripts/deploy-staging.sh`: `9307209f6c0493b17ae2123a215630644a300a69b702b01f778a053fac56d1cf`
- `scripts/deploy-transition.check.mjs`: `a2db0f30a0324797d3b133295d436e2ceee7a440ed4e9497f9a2b7785d4a51f4`
- `scripts/initial-baseline.check.mjs`: `2b563581b46afc53a5b51018e058baccc93381c2ba0e51c8622611c59b5341d2`
- `scripts/initial-baseline.sh`: `52db35dc90ad4359c6755ec9dcef16b31a12d9ab9d3dce6446d6b681e32c24f2`
- `scripts/load-verified-image.check.mjs`: `c8a06c9bdbb150bfb17cebdaf46c1bf8e92cc55d3ca384a90703143a3faf1f48`
- `scripts/load-verified-image.sh`: `2e12eddecf9682436d123f117180bd40f507d30b3d69f0f0e32e56a465f0f38a`
- `scripts/staging-adoption-capsule.check.mjs`: `f9ff73cd10e545dcd306328e33516f6297dea8c7febc62bb5e630be4bc918f89`
- `scripts/staging-adoption-execute.sh`: `5ccae07af439aa8c2aad056e47d34c8addb250670006d0c4184490ee38d1eef5`
- `scripts/test-corrections-isolated.sh`: `117970ffc18a81d4205174455c6d2503139eb10bdfa93184c9372700b8b95e61`
- `scripts/guards/gh`: `6f47211f5ddcb1bbdd822c37d05cb766d5f9e9c1fd01fda52ac0a3eea962c295`
- `scripts/retain-verified-image.sh`: `68eb19bd763dac0817225b72899b0a26445fb3bae75eababe8db742cc49845ff`
- `scripts/retain-verified-image.check.mjs`: `4625fc5b2325d69d34cd433f9b9d29435414471cda38a5f49f0b63a4ca03ee58`

## Histórico anterior

A primeira entrega ficou parcial pois o pin era conferido após load. As rodadas anteriores e sua limitação ficam preservadas em [[evidencia-testes-sinteticos.log]]; não são a evidência da versão final.

## Retrabalho após QA_REJECTED — 2026-11-13

QA observou 100/100 e sonda 4/4 sintéticos, sem defeito reproduzido, mas rejeitou fechamento por cobertura B06/B09/B11/B12/B13. Este retrabalho não modifica o modelo de origem nem seus gates. `retain-verified-image.sh` limita cada chamada Docker a 10 segundos com `timeout`, mantendo falha fechada e o estado observável se a operação pode ter ocorrido. O teste usa prazo sintético de 0,8 segundo e injeta tanto timeout como erro após o efeito de `tag` e `rm`; pin é preservado e não há sucesso. A execução real do daemon pode continuar após timeout: resultado é ambíguo e requer reparo controlado.

Para B09, a fixture injeta erro antes e após link do marker e da conclusão, escrita parcial do marker temporário e SIGTERM após publicação do marker; verifica ausência de sucesso, retenção do pending/evidência e bloqueio de reentrada quando o marker existe. Para B11/B12, [[05 - Reparo histórico (plano)]] descreve `repair-baseline-fixture.check.mjs`: procedimento dentro do teste, apenas no namespace `/work`, com `flock` mantido durante verificação e conclusão sintética, owner/modo, identidade, pin, SHA, tar, marker, pending, seleção, dublê de origem e health. Exercita divergências e preservação, inclusive symlink e colisão. A chave fixa do dublê não autentica nenhuma origem real e o teste não implementa reparo operacional.

B13: o mesmo gate inteiro foi executado com `NXG_GATE_NEGATIVE_PROBE=1`, que injeta exclusivamente uma falha de teste; retornou **exit 1**, 106/107 e a única falha foi `NXG036_GATE_FAILURE_INJECTED`. A execução normal retornou **exit 0, 107/107**. As duas execuções confirmaram antes dos testes guardas PATH, `/usr/bin` e subprocessos para Docker/curl/ssh/scp/gh e isolamento de rede; sentinela e política sintética preservadas. [[evidencia-retrabalho-positivo.log|Log positivo]] · [[evidencia-retrabalho-gate-negativo.log|Log com falha injetada]]. Nenhum CT foi aprovado por DEV; QA_REJECTED anterior continua como histórico até reteste independente.

**Limites:** Docker real, modelo/driver real, fsync e queda de energia não foram testados. O plano histórico não autoriza tocar pending real nem comprova sua origem ou health. BA10 não foi implementado nem misturado neste Fix.

## Hashes SHA-256 do retrabalho final

- `scripts/deploy-bootstrap.sh`: `13d87450aea62d3a8e84a5467ee0996898afb5f2362cde3138102cbbbe99eb4e`
- `scripts/deploy-staging.sh`: `9307209f6c0493b17ae2123a215630644a300a69b702b01f778a053fac56d1cf`
- `scripts/deploy-transition.check.mjs`: `a2db0f30a0324797d3b133295d436e2ceee7a440ed4e9497f9a2b7785d4a51f4`
- `scripts/initial-baseline.check.mjs`: `5950599556c5aa7614e40f6433db7abd8dde987c3a688253671678ba9261071c`
- `scripts/initial-baseline.sh`: `52db35dc90ad4359c6755ec9dcef16b31a12d9ab9d3dce6446d6b681e32c24f2`
- `scripts/load-verified-image.check.mjs`: `c8a06c9bdbb150bfb17cebdaf46c1bf8e92cc55d3ca384a90703143a3faf1f48`
- `scripts/load-verified-image.sh`: `2e12eddecf9682436d123f117180bd40f507d30b3d69f0f0e32e56a465f0f38a`
- `scripts/staging-adoption-capsule.check.mjs`: `f9ff73cd10e545dcd306328e33516f6297dea8c7febc62bb5e630be4bc918f89`
- `scripts/staging-adoption-execute.sh`: `5ccae07af439aa8c2aad056e47d34c8addb250670006d0c4184490ee38d1eef5`
- `scripts/test-corrections-isolated.sh`: `970e4cba983e5e67d5f2c1cdfb7431961346abdc5358b0648bec80197a73d4f9`
- `scripts/guards/gh`: `6f47211f5ddcb1bbdd822c37d05cb766d5f9e9c1fd01fda52ac0a3eea962c295`
- `scripts/retain-verified-image.sh`: `1843d4685c029ce25ac659c1be2ecf3ca74f98b8487e36f6cbb89838d02af165`
- `scripts/retain-verified-image.check.mjs`: `2b73229b32f2a90da534bd5cb7d7b4addcb6ad6bfadd67e4540dc5fa0f479d5b`
- `scripts/repair-baseline-fixture.check.mjs`: `05fc769191012979cd55be604250f24eb06d76ee894a4c8f5bdc3b86a17155e0`

## Sincronização do parecer final QA — 2026-11-13

A decisão vigente em `.maestro/nxgest-team/NXG-036-PARECER-QA.md` é **QA_APPROVED com ressalvas exclusivamente sintéticas**, 13/13 CTs, gate positivo 107/107 e gate negativo com única falha intencional. O QA_REJECTED anterior permanece como histórico. Backend real, pending histórico, CD e backup/rollback não foram aprovados nem operados. Snapshot QA contém instrumentação adicional somente no runner; os outros 13 arquivos coincidem byte a byte com seu manifesto, e o runner local preservado difere apenas das sondas QA adicionais documentadas no parecer.
