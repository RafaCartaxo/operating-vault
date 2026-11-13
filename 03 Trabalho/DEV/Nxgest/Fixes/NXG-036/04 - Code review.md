# NXG-036 — Code review DEV

**Achado anterior CT-B04 corrigido para revisão QA:** preflight da identidade e colisão ocorre antes do load nos três caminhos, antes de pending e checkout onde aplicável; pin exato é permitido, tag temporária preexistente é recusada, e os IDs são rechecados após load e antes/depois do untag. Testes dublados cobrem ausência de mutações em colisão e modelo incompatível, conteúdo duplicado/adulterado e a execução com pin exato. A cadeia de autenticação prévia permanece responsável pela origem do tar; o hash do config não a substitui.

Revisados reentrada, lock cooperativo, ausência de force/prune, marker/pending por hard link e inode e falhas que preservam estado. **Limites:** driver/back-end real não foi consultado; o modelo restrito se apoia na observação histórica em Docker 26 e deve ser verificado independentemente no alvo antes de operação. Não há prova de durabilidade após perda abrupta de energia/fsync nem de exclusão de concorrente que não respeite o lock. CT-B11/B12 são plano para reteste QA, sem operação ou aprovação do estado histórico. Nenhum CT foi aprovado pelo DEV.

## Retrabalho após parecer QA_REJECTED

Cobertura anterior insuficiente, sem defeito reproduzido por QA. Revisitados B06 (timeout e erro após efeito), B09 (interrupção e escrita parcial), B11/B12 (procedimento unicamente sintético com lock e evidências independentes simuladas) e B13 (falha intencional propagada ao exit do gate). Revisado o único ajuste operacional: chamadas do helper usam timeout, retornam erro em ambiguidades e não alegam desfazer ações no daemon. Não se realizou nem se automatizou reparo histórico.

As evidências 107/107 e 106/107 com uma falha deliberada comprovam apenas cenários com fixtures. O verificador de origem simulado não substitui autenticação da cadeia real; ausência de origem verificada, backend compatível ou qualquer evidência operacional ainda fecha o gate. Nenhuma aprovação QA foi atribuída pelo DEV.
