# Skills operacionais

Estas notas são a fonte de verdade do processo do Operating Vault. Elas são escritas em Markdown para serem lidas por pessoas e por qualquer IA, independentemente do agente ou produto utilizado.

## Skills de fluxo

- [[Skills/QA-FIRST-DELIVERY|QA First Delivery]] — transforma uma necessidade em demanda, critérios, CTs, cobertura e handoff aprovado.
- [[Skills/DEV-EXECUTION|DEV Execution]] — executa o pacote QA aprovado, registra evidências, revisa e devolve para validação.

As duas skills acima orquestram o ciclo. O mapa de roteamento para as regras especializadas está em [[01 Board/Processos/03 - Mapa geral de skills|Mapa geral de skills]].

## Skills específicas

- [[Skills/MELHORIA|Melhoria]]
- [[Skills/BUG|Bug]]
- [[Skills/FIX|Fix]]
- [[Skills/CASOS-DE-TESTE|Casos de teste]]
- [[Skills/EXECUCAO|Execução de demanda]]
- [[Skills/ESCALA-DE-ESFORCO|Escala de esforço]]

### Regra de chamada

O usuário informa o trabalho; não precisa escolher a próxima skill. `qa-first-delivery` inicia e classifica a entrada, usa `MELHORIA` ou `BUG` conforme o tipo, consulta `CASOS-DE-TESTE` e `ESCALA-DE-ESFORCO`, e emite `QA_READY_FOR_DEV`. Depois, `dev-execution` roteia para `EXECUCAO` ou `FIX`, conforme seja melhoria ou bug/defeito. O resultado retorna para `qa-first-delivery` em `DEV_READY_FOR_QA`.

## Regra de precedência

As skills deste diretório definem o processo compartilhado. A skill instalada em um agente, como a skill global do Codex, funciona como uma camada de execução que aponta para estas regras. Se houver divergência, o processo documentado no vault deve ser revisado antes de adaptar o agente.

O fluxo visual e o contrato entre as etapas estão em [[01 Board/Processos/04 - Fluxo QA DEV|Fluxo QA → DEV]].
