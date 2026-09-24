# Agente: Processar material novo (universal)

Recebe um material bruto (relato na daily, texto no `00 Inbox`, observação do usuário, diff/nota) e executa o pipeline **classificar → limpar → rotear → registrar**, sem intervenção. Adaptado do `brainwork` (AGENTE_PROCESSAR_EXPORT) — sem Notion: o destino é sempre um card no board + registro na daily.

## Gatilhos

| Gatilho | Quando dispara |
|---|---|
| **Comando explícito** | "processa o material novo", "processa o relato", "processa o inbox" |
| **Arquivo novo no `00 Inbox/`** | Detecta texto recém-chegado e oferece processar |
| **Sessão interativa** | Você cola o relato no chat e pede pra processar |

## Pipeline

```
material bruto (daily / inbox / relato)
        │
        ▼
┌───────────────────┐
│ 1. CLASSIFICAR    │  ← é bug? melhoria? doc? descartável?
└───┬───────┬───────┘
    │       │       │
  bug     melhoria  doc/outro
    │       │       │
    ▼       ▼       ▼
┌────────────────────────────┐
│ 2. LIMPAR (essência)       │  ← extrair: sintoma, passos, ambiente,
│                            │    módulo, critérios — sem inferir
└────────────┬───────────────┘
             ▼
┌────────────────────────────┐
│ 3. ROTEAR                 │  ← template certo (Bug | Melhoria | —)
│    + numerar o tipo certo │  ← destino: 03 Trabalho/QA/<projeto>/ + board
└────────────┬───────────────┘
             ▼
┌────────────────────────────┐
│ 4. REGISTRAR              │  ← daily (🐛 Bug | 💭 MEL | ❓ suspeita)
└────────────────────────────┘
```

## Como iniciar

```text
BUG      relato + ambiente + reprodução → PROCESSAR → 03 Trabalho/QA/<projeto>/Demandas/Bugs/<PROJ>-NNN/
MELHORIA ideia + problema + resultado   → PROCESSAR → 03 Trabalho/QA/<projeto>/Demandas/Melhorias/<PROJ>-MEL-NNNN/
```

O relato pode ser colado no chat, registrado em `00 Inbox/` ou anotado na daily. Não é necessário conhecer o número do card.

## Ramificações de entrada

```text
relato
  ├─ comportamento errado confirmado? ── sim → BUG → <PROJ>-NNN
  ├─ melhoria/necessidade desejada? ───── sim → MELHORIA → <PROJ>-MEL-NNNN
  ├─ falha de CT de demanda pai? ───────── sim → DEFEITO → <PROJ>-NNN (pai: <ID>)
  ├─ suspeita não confirmada? ──────────── sim → daily como ❓, sem card
  └─ informação insuficiente? ──────────── sim → permanece no Inbox
```

## Regras

1. **Classificar** com `Skills/BUG` (bug×defeito×melhoria) — na dúvida entre bug e melhoria, **perguntar**, não assumir.
2. **Limpar**: extrair campos do template; **nada se infere** — ambíguo vira pergunta.
3. **Roteamento**: bug → `Templates/Bug/` + `<PROJ>-NNN`; melhoria → `Templates/Melhoria/` + `<PROJ>-MEL-NNNN`; sem informação para decidir → fica em `00 Inbox/` até destilar. O ID da demanda nunca é renomeado.
   O arquivo deve ser uma cópia do template correspondente; substituir placeholders, sem reconstruir a estrutura.
4. **Suspeita sem confirmação** → registra `❓` na daily, **não** cria card (regra do `Skills/BUG`).
5. **Prontidão de melhoria**: antes de mover para `backlog`, conferir Problema, Objetivo, Decisões, Escopo, Fora de escopo, Regras, Critérios e CTs. Decisão pendente que mude comportamento, escopo ou aceite mantém `status: analise`; registrar a pergunta em `## Pendências de decisão`.
6. **Registrar**: card no board (coluna 📥 Backlog) + entrada na daily.

## Resultado esperado

Card criado no padrão (template certo, numerado), linkado no board e registrado na daily — ou, se não der pra decidir, o material sinalizado como pendência de análise.
