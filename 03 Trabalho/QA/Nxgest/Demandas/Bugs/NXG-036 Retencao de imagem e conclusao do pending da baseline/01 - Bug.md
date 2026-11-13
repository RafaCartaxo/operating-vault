---
prioridade: alta
status: analise
tipo: bug
etapa_atual: "QA · Validação"
modulo: deploy
ambiente: dev
origem: observado
projeto: Nxgest
epico: ""
pai: NXG-MEL-0009
data_inicio: 2026-11-12
data_fim: ""
responsavel: QA
pontos_alocados: "a definir"
---
# NXG-036 — Retenção de imagem e conclusão do pending

> [!info]- Navegação QA/DEV
> **README:** [[00 README]] · **Bug:** [[01 - Bug]] · **Casos:** [[02 - Casos de teste]] · **Validação:** [[03 - Validação dev]] · **Qase:** [[04 - Preparação Qase]] · **Pai:** [[03 Trabalho/QA/Nxgest/Demandas/Melhorias/NXG-MEL-0009 Backup recuperavel e rollback do servico/00 README|NXG-MEL-0009]]

## Comportamento observado

Staging real falhou no untag da única tag de imagem em uso; o dublê anterior aceitou a remoção e mascarou a diferença. A primeira baseline manual teve êxito com pin de mesma imagem, mas helper retornou zero deixando pending ativo e marker completo. Fontes: `.maestro/nxgest-team/CT011-PRIMEIRA-BASELINE-POS-PUBLICACAO-PARECER-QA.md`, `CT011-REPARO-UNTAG-PARECER-QA.md` e `ct011-publicacao-20261112/staging-bed9-failure-state.json`. O erro real foi observado em adoção; o padrão comum nos outros dois fluxos é risco de código, não alegação de falha real deles.

## Passo a passo para reproduzir

Dado dublê stateful com imagem em uso e única tag, quando os fluxos tentam untag sem referência adicional, então Docker modelado recusa; dado o helper atual, sucesso deixa pending e marker. Reprodução planejada somente em fixture, não executada nesta triagem.

## Evidências

Parecer pós-publicação e registros apontados acima; baseline manual observada, não evidência de backup restaurável ou de CD automático.

## Resultado esperado

Retenção segura e conclusão rastreável do pending com falhas fechadas, preservando estado e guardas.

## Critérios de aceite

- **C1.** Referência persistente da imagem autenticada é estabelecida e verificada antes do untag nos três fluxos; apenas pin já existente de identidade exata pode ser reutilizado. ^c1
- **C2.** Colisão divergente, ausência de origem ou erro/ambiguidade de inspeção, pin ou untag falham fechados; loader conserva rejeição de tag temporária preexistente. ^c2
- **C3.** Não usar force/prune nem apagar ou alterar imagem, volume, container, rede ou tag alheios; o lock e a revalidação protegem a concorrência prevista. ^c3
- **C4.** Dublê stateful modela última tag de imagem em uso como falha e remoção de uma de duas referências válidas sem perda da imagem; gates executam os testes relevantes. ^c4
- **C5.** Sucesso de primeira baseline só é publicado após identidade, saúde, tar/marker completos e pin verificados; pending próprio é concluído ou arquivado com evidência verificável antes de retorno zero. ^c5
- **C6.** Falha, interrupção ou publicação parcial mantém pending e evidências para reparo; marker completo impede nova primeira entrada e concorrência não produz falso sucesso. ^c6
- **C7.** Plano local de reparo do estado histórico distingue marker/pending e valida origem, identidade, saúde e custódia sob lock; prevê falha fechada sem apagar o pending real ou automatizar exclusão do legado. ^c7

## Escopo e limites

Cobrir `scripts/deploy-staging.sh`, `staging-adoption-execute.sh`, `initial-baseline.sh`, loader e gates pertinentes. Escolha de interface do pin pertence ao DEV. Apenas implementação e testes locais com fixtures e dublês sob guardas de PATH, caminhos absolutos e subprocessos, sem rede/socket e sem Docker/SSH/curl/GH reais. Não manipular pending atual, serviços, tags, segredos ou dados reais; não autorizar implicitamente reparo real. Legado retido e promoções futuras requerem procedimento próprio, sem exclusão automática. NXG-031 e épico permanecem encerrados. MEL-0009/BA10/CT-011 permanecem NO-GO nos limites anteriores.

## Checklist de entrega ao DEV

- [x] Sintoma, evidências e escopo definidos.
- [x] Critérios observáveis e CTs vinculados.
- [x] Matriz, validação reservada e integridade registradas.
- [ ] Pontos alocados: capacidade será definida pela Coordenação; não impede especificação técnica.

## Contexto da execução

Implementação local autorizada para encaminhamento pela Coordenação; nenhum teste, commit, push, deploy ou operação real nesta triagem.

## Reteste QA — 2026-11-13

QA_REJECTED para fechamento integral por cobertura incompleta; suíte isolada 100/100 e sonda adicional 4/4. O plano histórico é documental; B11/B12 bloqueados e B06/B09/B13 parciais. Parecer: `.maestro/nxgest-team/NXG-036-PARECER-QA.md`. Nenhum pending histórico ou serviço real foi operado.
