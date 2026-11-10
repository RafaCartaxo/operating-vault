---
projeto: nxgest
demanda: NXG-031
responsavel: QA e Coordenação
data: 2026-11-10
---

# Evidências QA — NXG-031

Validação independente sobre working tree de `nxgest/`, base `c7b65c8ddd85efde4db7f075ca03d95a7c6c5c38`. Treze arquivos da entrega identificados por SHA-256 no manifesto local `.maestro/nxgest-team/qa/NXG-031/files-final.json`; nenhum commit desta rodada. Logs e harness independente ficam na mesma pasta de equipe, fora do repo/vault. Os resultados essenciais estão preservados nesta nota.

## CT-B01 — Primeira transição

`npm run test:deploy` aprovado; cenário usa repositórios Git sintéticos, remoto local e Docker/curl dublados, executa o corpo SSH extraído dos workflows. O bootstrap vem do alvo antes do checkout; script/helper e Compose em infra são usados. Harness independente `check-bootstrap.py` também comprovou transição, SHA exato e envs byte a byte intactos. `bootstrap-independent.json`: sete verificações aprovadas.

## CT-B02 — Falhas de fetch e ref

Suíte de deploy confirmou ref inexistente e remoto indisponível, sem alteração de HEAD/env e sem chamada Docker. Ref antiga sem bootstrap é recusada sem executar script legado. Não houve fetch operacional nem atualização do servidor.

## CT-B03 — Preservação de trabalho

Suíte de deploy confirmou recusa de alteração rastreada, arquivo novo e arquivo ignorado em conflito. Conteúdo, HEAD e envs de fixtures preservados; texto privado sintético não aparece nos logs. Harness independente confirmou recusa de trabalho rastreado/novo e bloqueio concorrente.

## CT-B04 — Env, repetição e manual

Execução repetida e comando manual usam o alvo e preservam `.env` e `.env.staging` sintéticos, incluindo `MAIL_FROM_NAME="NX Gest"`. O teste de segurança do parser também passou; conteúdo é lido como dado. Nenhum env real foi lido ou modificado.

## CT-B05 — Gates, backup, concorrência e recuperação

Suíte final: falta/falha de backup interrompe antes de Docker; falta ou falha de staging impede produção; mesmo SHA é requerido; lock comum impede segundo deploy. Workflows mantêm gates test/smoke e CI→CD; YAMLs parseados e scripts aprovados em `bash -n`.

O complemento de recuperação executa o comando extraído do runbook com Git/backup sintéticos: só recupera arquivos do checkout antigo, exige backup e preserva alterações/envs/ignorados. Não opera serviços e não demonstra rollback de aplicação. A aprovação local deste CT não autoriza nem certifica publicação real.

## CT-B06 — Continuidade e transporte

Teste extrai o procedimento do guia e usa GPG real com senha sintética e homes distintos. Conferiu arquivo cifrado 600, diretório de extração privado 700, arquivos finais 600/diretórios 700, recusa de colisão e de descriptografia inválida sem instalar conteúdo no destino. O guia separa dev local de acesso operacional; runbook identifica confirmação pendente de Cloudflare e seus limites. Nenhum segredo real foi transportado.

## Regressão e verificações

- `npm test`: 46 arquivos / 215 testes aprovados; log `vitest.log`.
- `npm run test:safety`: 9/9 aprovados; log `safety.log`.
- Suíte de transição inicialmente 9/9 (`test-deploy.log`); complemento final 11/11 com o objeto histórico artificialmente indisponível (`no-history.log`). Essa execução usa wrapper Git que recusa somente o acesso ao commit antigo; todas as outras operações usam Git real em fixtures. Não equivale a CI remoto executado.
- Build e check-dist: aprovados, quatro assets presentes (`build.log`).
- Docs, links, UI, estilos, módulos, sintaxe Bash e diff: exit 0, logs `*-final.log`. Dois YAMLs carregaram sintaticamente por PyYAML.
- Links: zero erros; cinco avisos históricos de órfãos já aceitos, sem nova divergência.

## Limites e pré-publicação

Nenhum SSH, VPS, Cloudflare, Docker real, segredo, push ou deploy nesta execução. Linux local; compatibilidade real do host e execução GitHub Actions ainda não comprovadas. Antes de publicar: conferir ferramentas Git/Bash/flock, checkout limpo e ausência de deploy legado fora do lock, envs presentes/permissões sem exibir conteúdo, backup recuperável e plano de rollback de serviço, saúde/DNS/TLS e e-mail quando autorizado. Recuperar checkout não recupera automaticamente serviço ou banco.

## Parecer

Os seis cenários locais têm evidência aprovada. Ressalvas de abrangência e pré-publicação acima permanecem; não constituem autorização de deploy. A correção de transição local é revisável no working tree; o épico de organização anterior permanece concluído e separado.
