# CT-011 — adendo QA para nova baseline futura

2026-11-11 · O usuário esclareceu que os dados atuais de produção podem ser descartados e priorizou o funcionamento futuro. A decisão permite preparar uma nova baseline sem exigir primeiro a origem histórica da imagem legada; **não é execução ou autorização de descarte**, tampouco prova de origem/recuperação antiga. `CT011-C-MEDICAO-RESULTADO-PRIVADO.md` relata SSH zero e sete metadados com valores restritos; QA revisou somente o registro, não a consulta. Versão/tamanhos são pontuais e o banco selecionado pelo ambiente ainda não está vinculado à aplicação. Não reproduzir nomes privados neste adendo.

## Contrato de escopo

- Histórico: E1 da imagem antiga e a recuperação legada permanecem **não comprovados**, sem aprovação retroativa. A declaração do usuário altera a prioridade de preservação dos dados atuais; não atesta a origem de artefato antigo nem autoriza exclusão, reset ou deploy.
- Alvo novo: um conjunto novo tem identidade verificável do código/artefato/imagem efetiva, compatibilidade de schema/configuração e backup consistente de PostgreSQL e anexos associados. Cópia, restauração e comparação precisam de evidência independente suficiente, com falha fechada. Nenhuma marca, serviço de assinatura ou plataforma é imposta por nome.
- Gates atuais `rollback-preflight.sh` e `verify-rollback-return.sh` permanecem NO-GO até haver substituição **condicional** efetivamente implementada, validada e aprovada: fonte/evidência desconhecida, inválida ou divergente falha; caso positivo passa somente com evidências suficientes. Não perpetuar NO-GO incondicional como solução final, nem aceitar autoafirmação como prova.
- Reutilizar scripts, dublês e CTs existentes de MEL-0009/032–035; não reabrir NXG-031 ou épico. Trabalho local preparado pode ser implementado por DEV após gate desta proposta; nenhuma operação real, Docker CLI/daemon, rede, segredo, dados reais, descarte, commit, push ou deploy está autorizada por este adendo.

## Critérios observáveis e matriz QA

| Critério | Aceite | Casos |
|---|---|---|
| C1 — conjunto e consistência | Banco e anexos sintéticos associados ao mesmo ID; ausência legítima distinta de erro; controle verificável de quiescência/snapshot ou bloqueio sem alegar consistência; não sobrescrever último conjunto íntegro. | CT-N01, N02 |
| C2 — cópia e restauração | Cópia completa íntegra e verificada; ensaio **PostgreSQL real** isolado restaura dados sintéticos e anexos do mesmo conjunto e compara conteúdo/referências, órfãos e invariantes. Dublê não é restore real. | N03, N04 |
| C3 — nova identidade/compatibilidade | Fonte de build autenticada e verificável liga commit completo e digest de artefato à imagem efetiva e baseline nova; distinguir image-config-ID de manifest digest. Schema/config/mounts e estratégia revisados para imagem e estado alvo; tags/labels e autodeclarações isoladas não bastam. | N05, N06 |
| C4 — gates e retorno | Ausência, assinatura/fonte/política inválida, divergência, evidência obsoleta ou ambígua, saúde ruim/timeout e integridade insuficiente bloqueiam; caminho positivo autorizado com evidências reais suficientes pode passar, sem NO-GO incondicional; não executa restore automaticamente. | N06, N07, N08 |
| C5 — isolamento e regressão | Execução local com fixtures/dublês e interceptação comprovada para Docker CLI/daemon, curl, SSH/SCP e subprocessos; preservar gates NXG-031 e NXG-032–035, dados e WIP. Teste real posterior somente com autorização agrupada e recursos exclusivos. | N09, N10 |

## CTs planejados — nenhum executado

- **CT-N01**: gerar banco/anexos sintéticos vinculados, incluindo ausência legítima e referência sem arquivo; associar IDs e rejeitar inconsistência.
- **CT-N02**: sem evidência de quiescência/snapshot, escrita/interrupção/corrida/colisão falham e conjunto íntegro anterior permanece byte a byte; variante com controle válido é demonstrada no escopo apropriado.
- **CT-N03**: cópia completa passa; vazia, parcial, adulterada, interrompida ou escrita/cópia em disco falha sem substituir anterior; dublês não comprovam transporte real.
- **CT-N04**: após autorização própria, restaurar PostgreSQL real e anexos sintéticos em recursos exclusivos isolados, validar conteúdo efetivo, referências, órfãos e invariantes; destino de produção deve ser recusado. Antes disso, marcar **bloqueado para prova real**, não aprovado por fixture.
- **CT-N05**: fonte confiável vincula commit, digest e identidade efetiva da baseline nova; divergência config-ID/manifest/SHA, imagem errada ou schema/config/mounts incompatíveis bloqueiam. Fonte concreta e política devem constar da proposta DEV.
- **CT-N06**: evidência ausente, vazia, inválida, adulterada, expirada, de outro bundle/ambiente ou revisor/fonte não autorizado falha fechada; declaração isolada não aprova.
- **CT-N07**: saúde negativa/ambígua, timeout, integridade não verificada, dados/anexos ausentes ou objeto divergente impedem alegação de retorno.
- **CT-N08**: com evidência sintética positiva e guardas, exercitar caminho condicional de sucesso; demonstra fluxo lógico, não produção. Após ensaio real autorizado, repetir avaliação com evidência real independente para baseline nova.
- **CT-N09**: sondar guardas PATH/absoluto/subprocessos ANTES de cada execução; ausência/desvio, namespace/rede indisponível, comando ou recurso real bloqueia antes do teste.
- **CT-N10**: regressão pertinente NXG-031 e MEL-0009/032–035 e CI/CD; falha dos gates impede promoção, não apaga violação histórica de Docker CLI nem altera arquivos WIP.

## Etapas, evidência e gate

1. QA define contrato e integridade documental; DEV entrega **proposta concreta** de fonte de confiança, reuso, mudanças mínimas, limites e ensaio; QA compara critérios e emite gate antes de código. **Estado atual: proposta DEV recebida e comparada; QA_READY_FOR_DEV para implementação local delimitada, conforme gate abaixo.**
2. Implementação local já autorizada após gate; testes só sintéticos/dublês com guardas comprovadas. Evidências por CT, logs sem segredos e `DEV_READY_FOR_QA`; QA retesta independente. Não executar Docker real por inferência.
3. Pedir autorização específica agrupada para PostgreSQL real com dados sintéticos, imagem/container/volumes/rede exclusivos, isolamento verificável de produção e internet, operadores, recursos, custo, retenção e limpeza explícita. Nenhum dado real ou credencial de produção; parar em dúvida ou colisão. QA verifica conteúdo restaurado e identidade independente.
4. Para publicação futura: evidências da nova baseline, CI real e staging mesmo SHA, recuperação e decisão de operação revisadas e autorização específica. Não presumir que aceitação de perda atual autorize descarte, alteração do host, commit, push ou deploy.

MEL-0009 permanece QA_REJECTED/NO-GO, CT-011 histórico bloqueado até decisão QA sobre resultados e escopo. O desvio histórico Docker CLI permanece não conforme sem validação retroativa. Esta preparação não reabre épico ou NXG-031 e não destrói nada.

## Gate de integridade e comparação DEV — 2026-11-11

**QA_READY_FOR_DEV — implementação local delimitada**, após comparação com `CT011-NOVA-BASELINE-PROPOSTA-DEV.md`. A proposta cobre C1–C5 e N01–N10: reuso dos scripts, conjunto/cópia/consistência, restore PostgreSQL real sintético em ensaio posterior, cadeia autenticável para nova imagem e separação entre fixtures e evidência real. O valor da medição é observação relatada, não capacidade reservada nem prova de banco da aplicação; nomes de banco/volume permanecem privados.

O gate autoriza o encaminhamento da implementação local já autorizada, não executa nem autoriza ensaio real. A implementação deve conter o caminho positivo condicional verificável e falha fechada com fonte ausente, sem reconhecer fixture como fonte real; escolha de mecanismo efetivamente disponível não pode ser substituída por autoatestado. Se a capacidade concreta de autenticação/ambiente não puder ser demonstrada, manter NO-GO e registrar bloqueio: a proposta GitHub é hipótese, não prova de disponibilidade ou vínculo do artefato em produção. Fixar identidade do verificador/política e testar emissor desconhecido, replay e mistura de artefatos. Se o encadeamento completo do build for dividido em fase futura, não declarar nova baseline operacional pronta até o vínculo autenticado e implantação do mesmo artefato serem efetivamente demonstrados.

CT-N04 PostgreSQL real permanece bloqueado até autorização específica agrupada e execução em isolamento; critérios sintéticos não encerram o pai nem fornecem autorização de publicação. Pacote preparado no vault como adendo do pai, com matriz e dez CTs rastreáveis; gate documental conferido em `09 - Nova baseline QA.md`. Nenhum teste, Docker CLI/daemon, SSH, rede, dado/segredo real, commit, push, deploy ou descarte ocorreu nesta revisão.

## Revisão documental da medição de preparação C

A Coordenação relata SSH zero e sete campos validados, incluindo versão de servidor 16.14 e tamanhos pontuais de banco 11.238.423 bytes, volume 4.055.040 bytes e imagem 359.796.176 bytes. QA conferiu o registro privado, não observou a execução nem repetiu consulta; nomes de banco/volume continuam somente no registro privado. Os valores não comprovam vínculo do banco selecionado à aplicação, espaço reservado, quiescência, consistência, origem ou restore; `du` e tamanho de imagem não garantem tamanho de exportação. Confiança SSH informada pelo usuário é preservada; origem independente/chave negociada não demonstradas pela equipe.

## Navegação canônica

[[01 - Demanda]] · [[03 - Casos de teste]] · [[04 - Validação dev]] · [[08 - Evidências reteste QA]]

## Reteste QA independente — 2026-11-11

**QA_REJECTED para aptidão do ensaio real.** Regressões sintéticas 4/4 e runner dublado 5/5 passaram sob guardas; achado: containers são iniciados antes da verificação de versão PostgreSQL, conforme sonda dublada. N04 real e gates operacionais permanecem bloqueados. Evidências e matriz N01–N10 em `.maestro/nxgest-team/CT011-NOVA-BASELINE-PARECER-QA.md`; não houve acesso real.

## Reteste QA política — 2026-11-11

QA_REJECTED: a política controla imagem/major antes do runner na fronteira acordada, mas `rehearsal-postgres.check.mjs` remove recursivamente `.maestro` do diretório corrente. Sonda em snapshot isolado reproduziu remoção de sentinela sintética; 4/4 e 11/11 testes passaram. Ver `.maestro/nxgest-team/CT011-NOVA-BASELINE-PARECER-QA.md`. Nenhum dado real removido; ensaio real/CT-N04 não autorizado e pai NO-GO.

## Reteste cleanup — 2026-11-11

Achado anterior resolvido no snapshot: sentinela e política sintéticas preservadas em bytes, estrutura e modos; 4/4 e 11/11 testes dublados sob guardas. Apto para Coordenação apresentar pedido único condicionado de ensaio PG sintético; autorização deve abranger explicitamente recursos Docker locais fora do workspace e cleanup próprio. CT-N04 real permanece bloqueado; origem nova e gates operacionais ainda pendentes. Detalhes: `.maestro/nxgest-team/CT011-NOVA-BASELINE-PARECER-QA.md`.
