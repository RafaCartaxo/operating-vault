# Skill: Criação e Organização de Bugs (universal)

Criar, revisar e organizar bugs no padrão do vault. Adaptado do `brainwork` (SKILL_BUGS) — sem Notion/SGV: aqui o card é a fonte (`<PROJ>-NNN`), e o plano do repo é referência (`PLAN-NNN`).

## Bug × Defeito × Melhoria

Primeira pergunta antes de criar o card — muda o template e a esteira:

- **Bug** — comportamento errado observado (dev, staging ou prod). Template `Templates/Bug/`. Esteira normal.
- **Defeito** — reprovou um **CT de um card pai** (melhoria/funcionalidade) em `dev`. Abre como bug **filho** (`pai: <ID do card pai>`, por exemplo `pai: MEL-0001`), fecha sem passar por `hml`. Fronteira é **origem + ambiente**, não gravidade.
- **Melhoria** — funciona, pode funcionar melhor. Template `Templates/Melhoria/` (hub) — ver `Skills/MELHORIA`.

## Modos de entrada

- **Suspeita própria**: possível bug ainda não confirmado. Registra na daily (`❓ Suspeita de bug`). Só vira card **após confirmação**; descartada → não cria card.
- **Relato rápido**: descrição livre + contexto → direto no `Template/Bug`.
- **Contexto rico**: extrair ambiente, módulo, prioridade, passos, critérios — sem perder informação; ambíguo → perguntar, não assumir.
- **Via uso/produção**: relato de usuário → investigar o código/API real antes de fechar o card; se não reproduzir, marcar em Observações ("precisa confirmação").

## Estrutura padrão

Cada bug vive em uma pasta própria: `01 - Bug.md` (sintoma, reprodução, esperado e critérios), `02 - Casos de teste.md` (cenários de reprodução/regressão) e `03 - Validação <ambiente>.md` quando o fix for validado.

## Nome do arquivo e numeração

- Card com número: `<PROJ>-NNN Bug <Título>` (número atribuído no board — sequencial, nunca reutilizado).
- Sem número ainda: `Bug <Título>` (prefixo entra quando numerar).
- Defeito: `<PROJ>-NNN Defeito <Título>` com `pai` preenchido.

## Descarte

- Bug/suspeita **descartado** (não ocorre / não reproduz): move para `05 Arquivo/` com `status: descartado`. Não fica no board.

## Onde registrar

- Card em `03 Trabalho/QA/<projeto>/Demandas/Bugs/<ID>/` · status no board · registro na daily (🐛 Bug encontrado / 🗑️ descartado).
- Os **CTs da nota `02 - Casos de teste.md` são a fonte única de verificação**; a validação registra os resultados e evidências.
- O campo `pontos` registra o esforço da passagem pelo bug, usando a [[ESCALA-DE-ESFORCO|escala Fibonacci]]. Pode ficar vazio no registro inicial, mas deve ser preenchido antes de o bug sair de `QA · Triagem`.
