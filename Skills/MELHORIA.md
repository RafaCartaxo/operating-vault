# Skill: Melhoria (NX Gest)

Ciclo da melhoria — da ideia ao card validado no board. Adaptado do `brainwork` (SKILL_MELHORIA) — sem Notion: o "cadastro" é criar o card no board; sem Qase: os CTs vivem em `03 - Casos de teste.md`.

## Onde nasce

- **Daily** → seção `## Melhorias propostas`, checkbox `MEL-NNNN · <Título>` — ou direto no board como card `MEL-NNNN` com template `Melhoria`.
- **Número**: sequencial (`MEL-0001`, `MEL-0002`...) e nunca reutilizado. O identificador é estável: não vira `NXG-NNN` ao longo do ciclo. Quando necessário, a implementação recebe um `PLAN-NNN` no repositório.

## Ciclo

1. **Registrar** a ideia (daily/board).
2. **Refinar a demanda** — preencher Problema, Objetivo, Decisões de produto, Escopo, Fora de escopo e Regras de negócio em `01 - Demanda.md`.
3. **Resolver pendências** — uma decisão que altere escopo, regra ou critério mantém a melhoria em `analise`; não criar PLAN nem iniciar implementação enquanto ela estiver aberta.
4. **Definir critérios e CTs** — cada critério de aceite deve ser coberto por pelo menos um `CT-001..` em `03 - Casos de teste.md`, dentro da pasta da demanda (formato `Skills/CASOS-DE-TESTE`). Os critérios são identificados por `C1..Cn` e IDs de bloco, sem checkbox de aprovação; quando houver vários CTs para o mesmo critério, todos precisam passar na validação.
5. **Planejar e executar** — quando a demanda estiver pronta, vincular o `PLAN-NNN` do repositório e seguir a esteira: `📥 Backlog → 🔍 Em análise → ⚙️ Em execução → 🧪 Em validação → ✅ Feito` — validação em `dev` (local) e, quando aplicável, `hml` (staging) e `prod`.
6. **Sincronizar cada transição** — ao mudar de etapa, atualizar `status` e `etapa_atual` da demanda, a coluna do Board, o `00 README.md` da demanda e a execução DEV; em validação, manter também o registro QA vinculado.
7. **✅ Feito** → move o card para `05 Arquivo/`.

## Melhoria × Bug

| Aspecto | Bug | Melhoria |
|---|---|---|
| Natureza | Comportamento errado que existe | Funciona, pode funcionar melhor |
| Pacote QA | `Templates/Bug/` | `Templates/Melhoria/` (hub — agrega regras, CTs e bugs filhos) |
| Validação | Esteira normal | Esteira normal |

## Bugs encontrados na validação da melhoria

Se um CT da melhoria reprovar em `dev` → abre **Defeito** filho (`pai: MEL-NNNN`, `Skills/BUG`).

Os pontos do defeito filho são esforço adicional e não alteram o total original da melhoria. O vínculo `pai` permite identificar a origem e apresentar separadamente o retrabalho gerado pela falha.

## Definição de pronta para planejar

Antes de criar ou vincular um `PLAN-NNN`, confirmar:

- problema e objetivo estão distintos e compreensíveis sem contexto oral;
- decisões de produto não têm pendência bloqueante;
- escopo e fora de escopo estão registrados;
- regras de negócio são verificáveis;
- critérios de aceite são objetivos e cada um aponta para CTs;
- casos feliz, de borda/validação e de erro foram avaliados.

## Identificadores e vínculos

- **Melhoria:** `MEL-NNNN`, estável do registro ao arquivo.
- **Bug/defeito:** `NXG-NNN`, inclusive quando for filho de uma melhoria (`pai: MEL-NNNN`).
- **Plano técnico:** `PLAN-NNN` no repositório; é vinculado no campo `plano`, sem substituir o ID da demanda.
- **Esforço:** `pontos` registra o esforço da passagem pela melhoria, usando a [[ESCALA-DE-ESFORCO|escala Fibonacci]]. Pode ficar vazio ao registrar a ideia, mas deve ser preenchido antes de a melhoria sair de `QA · Triagem`.
