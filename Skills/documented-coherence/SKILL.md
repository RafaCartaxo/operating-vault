---
name: documented-coherence
description: Camada transversal agnóstica de projeto para qualquer IA consultar primeiro a fonte vigente (North Star e documentação), responder em formato padrão, decidir pelos pontos principais, transformar decisões em documentação, verificar contradições e encaminhar para a skill ou agente correto. Aplicar antes de qualquer outra skill.
---

# Skill: Documented Coherence

Camada transversal, agnóstica de projeto e de agente. Vale para qualquer IA, qualquer produto e qualquer vault que adote este contrato: nenhuma resposta sai sem fonte vigente, nenhum ponto principal decide sozinho e nenhuma decisão nova morre na conversa.

## Propósito

Garantir que toda atuação seja coerente com a documentação vigente: consultar primeiro a fonte de verdade, responder em formato padronizado, decidir pelos pontos principais, transformar decisões novas em documentação, detectar contradições e encaminhar a responsabilidade para a skill ou agente correto.

## Quando aplicar

- Sempre, antes de qualquer outra skill ou ação: esta skill é a porta de entrada do raciocínio, não uma etapa opcional.
- Em chat novo, retomada de trabalho, mudança de projeto, divergência entre fontes ou pedido que afete processo, escopo ou documentação.
- Não se aplica apenas quando a tarefa é execução mecânica já contratada por um pacote aprovado (nesse caso, a skill orquestradora vigente continua responsável; esta skill só é consultada se surgir fato novo).

## Ordem de leitura (North Star primeiro)

Resolver nesta ordem, do mais estável ao mais volátil; parar no nível que responde, mas registrar qual nível decidiu:

1. **North Star** — o objetivo declarado do trabalho atual (documento de direção do projeto ou, na ausência dele, a demanda/critérios do pacote vigente). Se não existir North Star escrito, declarar explicitamente essa ausência em vez de inventá-lo.
2. **Regras do vault** — `Skills/README.md` e a regra especializada aplicável (`MELHORIA`, `BUG`, `CASOS-DE-TESTE`, `EXECUCAO`, `FIX`, `ESCALA-DE-ESFORCO`).
3. **Fluxo e mapas** — `01 Board/Processos/04 - Fluxo QA DEV.md`, `03 - Mapa geral de skills.md`, `02 - Mapa geral de processos.md`.
4. **Contexto do projeto** — `04 Projetos/<projeto>/`, boards, `Dashboard.md`, `02 Daily/`.
5. **Conversa atual** — por último: a conversa nunca prevalece sobre os níveis acima.

## Formato padrão de resposta

Toda resposta substantiva segue esta ordem:

1. **Fonte** — quais documentos decidiram (com caminho).
2. **Pontos principais** — os 2–4 fatos que sustentam a conclusão.
3. **Conclusão ou proposta** — direta, sem rodeios.
4. **Divergências** — contradições encontradas ou “nenhuma”.
5. **Próximo responsável** — skill ou agente e o handoff emitido.

Respostas mecânicas curtas (confirmações, leituras) dispensam o formato, mas devem citar a fonte quando afirmam estado.

## Regra de decisão

- Decidem os pontos principais extraídos da fonte de verdade vigente, nunca impressões da conversa, memória do agente ou maioria de menções.
- Em conflito entre níveis da ordem de leitura, vence o nível mais alto (mais estável); o conflito é registrado como divergência e, se alterar processo ou escopo, vira documentação (ver sincronização).
- Sem fonte que cubra o caso: declarar a lacuna, propor pelo nível mais próximo e marcar a proposta como provisória até documentação.

## Sincronização documental

Toda decisão nova que afete processo, escopo, critério, convenção ou responsabilidade deve sair da conversa e virar documentação no mesmo ciclo:

- Atualizar a nota vigente (regra, mapa, fluxo ou contexto de projeto) em vez de duplicar o conteúdo em outra nota.
- Registrar decisão, data e motivo de forma rastreável; não reescrever histórico.
- Se a decisão contraria regra vigente, a regra é revisada primeiro — nunca adaptada em silêncio.

## Verificação de contradições

Antes de concluir, cruzar: North Star × regras × fluxo × contexto do projeto × conversa. Marcar cada achado como:

- **Contradição** — fontes vigentes divergem; informar, não arbitrar em silêncio; escalar para decisão documentada.
- **Lacuna** — nenhuma fonte cobre o caso; propor provisoriamente e documentar.
- **Coerente** — prosseguir e citar as fontes.

## Handoff

Encaminhar a responsabilidade pelo estado e pelos eventos documentados, nunca por palavra-chave ou suposição:

- Informar a próxima skill ou agente, o artefato que a autoriza e o que se espera dela.
- Usar os eventos do fluxo (`QA_READY_FOR_DEV`, `DEV_READY_FOR_QA`, `QA_APPROVED`, `QA_REJECTED`) quando o trabalho estiver no ciclo QA/DEV; fora dele, nomear o responsável e o artefato equivalente.
- Quem recebe só assume com o artefato completo; caso contrário, devolve com o que falta.

## Protocolo obrigatório de conclusão entre agentes

Ao concluir, o agente executor deve avisar o agente orquestrador no pane definido — não apenas escrever no próprio painel. O aviso segue este formato exato:

- `STATUS` — um de `IN_PROGRESS`, `BLOCKED` ou `COMPLETED`.
- `SKILL` — a skill aplicada.
- `FONTE` — documentos que decidiram.
- `PONTOS_PRINCIPAIS` — os fatos que sustentam a conclusão.
- `DIVERGENCIAS` — contradições encontradas ou “nenhuma”.
- `ARQUIVOS` — criados e alterados.
- `VALIDACOES` — checagens executadas e resultado.
- `PENDENCIAS` — o que resta e quem resolve.
- `PROXIMO_RESPONSAVEL` — quem assume a seguir e com qual handoff.

O orquestrador deve confirmar o recebimento, verificar os artefatos listados e só então avançar para a próxima etapa. Sem confirmação, o handoff permanece pendente.

## Limites de autorização

- Esta skill não aprova funcionalmente, não publica, não faz push e não altera código: ela organiza o raciocínio e a documentação.
- Não cria North Star, não reescreve regra vigente sem revisão explícita e não expõe conteúdo sensível para justificar coerência.
- Diante de pedido que exceda esses limites, declarar o limite e encaminhar para o responsável correto (skill orquestradora, revisor humano ou gate de publicação).
