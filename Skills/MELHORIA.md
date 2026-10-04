# Skill: Melhoria (universal)

Ciclo da melhoria — da ideia ao card validado no board. Adaptado do `brainwork` (SKILL_MELHORIA). O card é criado no board; os CTs vivem em `03 - Casos de teste.md` e podem ser preparados para Qase quando o projeto usar essa integração.

## Onde nasce

- **Daily** → seção `## Melhorias propostas`, checkbox `<PROJ>-MEL-NNNN · <Título>` — ou direto no board como card `<PROJ>-MEL-NNNN` com template `Melhoria`.
- **Número**: sequencial por projeto (`<PROJ>-MEL-0001`, `<PROJ>-MEL-0002`...) e nunca reutilizado. O identificador é estável durante todo o ciclo. IDs históricos sem prefixo de projeto permanecem válidos.

## Ciclo

1. **Registrar** a ideia (daily/board).
2. **Identificar o épico, quando houver** — preencher `epico` com o link do agrupamento estratégico. O épico organiza várias demandas; não substitui `pai`, que continua representando dependência direta.
3. **Instanciar o pacote** — criar os seis arquivos copiando os templates correspondentes, preservando ordem, headings, callouts, blocos Dataview/Meta Bind, anchors e tabelas. Só depois preencher placeholders e adaptar o conteúdo da demanda.
4. **Refinar a demanda** — preencher Problema, Objetivo, Decisões de produto, Escopo, Fora de escopo e Regras de negócio em `01 - Demanda.md`.
5. **Resolver pendências** — uma decisão que altere escopo, regra ou critério mantém a melhoria em `analise`; não criar PLAN nem iniciar implementação enquanto ela estiver aberta.
6. **Definir critérios e CTs** — cada critério de aceite deve ser coberto por pelo menos um `CT-001..` em `03 - Casos de teste.md`, dentro da pasta da demanda (formato `Skills/CASOS-DE-TESTE`). Os critérios são identificados por `C1..Cn` e IDs de bloco, sem checkbox de aprovação; quando houver vários CTs para o mesmo critério, todos precisam passar na validação.
7. **Validar a instância do template** — QA/`qa-first-delivery` deve executar `python3 scripts/validar_pacote_qa.py <pasta-da-demanda>` antes de mover para DEV e registrar o resultado resumido no `00 README.md`. O comando deve confirmar os seis arquivos, headings e blocos canônicos, critérios, matriz, âncoras, links, CTs na validação e resultados no YAML; qualquer erro mantém a melhoria em QA.
8. **Planejar e executar** — quando a demanda estiver pronta, vincular o `PLAN-NNN` do repositório e seguir a esteira: `📥 Backlog → 🔍 Em análise → ⚙️ Em execução → 🧪 Em validação → ✅ Feito` — validação em `dev` (local) e, quando aplicável, `hml` (staging) e `prod`.
9. **Sincronizar cada transição** — ao mudar de etapa, atualizar `status` e `etapa_atual` da demanda, a coluna do Board, o `00 README.md` da demanda, o épico e a execução DEV; em validação, manter também o registro QA vinculado.
10. **✅ Feito** → move o card para `05 Arquivo/` e atualiza o status consolidado do épico.

## Melhoria × Bug

| Aspecto | Bug | Melhoria |
|---|---|---|
| Natureza | Comportamento errado que existe | Funciona, pode funcionar melhor |
| Pacote QA | `Templates/Bug/` | `Templates/Melhoria/` (hub — agrega regras, CTs e bugs filhos) |
| Validação | Esteira normal | Esteira normal |

## Bugs encontrados na validação da melhoria

Se um CT da melhoria reprovar em `dev` → abre **Defeito** filho (`pai: <PROJ>-MEL-NNNN`, `Skills/BUG`).

Os pontos do defeito filho são esforço adicional e não alteram o total original da melhoria. O vínculo `pai` permite identificar a origem e apresentar separadamente o retrabalho gerado pela falha.

## Definição de pronta para planejar

Antes de criar ou vincular um `PLAN-NNN`, confirmar:

- problema e objetivo estão distintos e compreensíveis sem contexto oral;
- decisões de produto não têm pendência bloqueante;
- escopo e fora de escopo estão registrados;
- regras de negócio são verificáveis;
- critérios de aceite são objetivos e cada um aponta para CTs;
- casos feliz, de borda/validação e de erro foram avaliados.

### Integridade obrigatória do template

A adaptação de uma melhoria não é uma recriação livre. O procedimento obrigatório é:

1. copiar `Templates/Melhoria/00 README.md` para `00 README.md`;
2. copiar `Templates/Melhoria/01 - Demanda.md` para `01 - Demanda.md`;
3. copiar os templates de `Templates/QA/` para os quatro artefatos restantes;
4. substituir placeholders e preencher o conteúdo específico;
5. preservar a estrutura, os blocos de automação e os campos do template;
6. revisar a matriz de cobertura e os resultados de todos os CTs antes de entregar ao DEV.

Não substituir blocos do template por uma versão resumida nem criar uma estrutura paralela “equivalente”. Se o template precisar mudar, atualizar primeiro o template e só depois instanciar o card.

## Identificadores e vínculos

- **Melhoria:** `<PROJ>-MEL-NNNN`, estável do registro ao arquivo.
- **Bug/defeito:** `<PROJ>-NNN`, inclusive quando for filho de uma melhoria (`pai: <PROJ>-MEL-NNNN`).
- **Plano técnico:** `PLAN-NNN` no repositório; é vinculado no campo `plano`, sem substituir o ID da demanda.
- **Esforço:** `pontos` registra o esforço da passagem pela melhoria, usando a [[ESCALA-DE-ESFORCO|escala Fibonacci]]. Pode ficar vazio ao registrar a ideia, mas deve ser preenchido antes de a melhoria sair de `QA · Triagem`.
