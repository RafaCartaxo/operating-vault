# Agente: Executar item de trabalho (universal)

Pega um bug (`<PROJ>-NNN`) ou uma melhoria pronta (`<PROJ>-MEL-NNNN`), organiza a execução e fecha o ciclo. Bug segue `Skills/FIX` em `03 Trabalho/DEV/<projeto>/Fixes/`; melhoria segue `Skills/EXECUCAO` em `03 Trabalho/DEV/<projeto>/Execuções/`. É o espelho do `Agentes/PROCESSAR`: o primeiro organiza a demanda; este a entrega e fecha.

## Gatilhos

| Gatilho | Quando dispara |
|---|---|
| **Comando explícito** | "fixa o <PROJ>-NNN", "executa a <PROJ>-MEL-NNNN", "aplica o PLAN-NNN" |
| **Card pronto em `analise`** | Bug vai para `03 Trabalho/DEV/<projeto>/Fixes/` após causa confirmada; melhoria vai para `03 Trabalho/DEV/<projeto>/Execuções/` após atender a definição de pronta e ter `PLAN-NNN` vinculado |
| **Sessão interativa** | Você descreve o sintoma e o agente investiga → card (via `PROCESSAR`) → fix |

## Pipeline

```
item <PROJ>-NNN ou <PROJ>-MEL-NNNN (analise, pronto para planejar)
        │
        ▼
┌───────────────────┐
│ 1. CONFIRMAR      │  ← causa no código para bug; viabilidade e decisões para melhoria
└────────┬──────────┘
         ▼
┌───────────────────┐
│ 2. PLANEJAR       │  ← `03 Trabalho/DEV/<projeto>/<Fixes|Execuções>/<ID>/` (`01 - Análise` + plano; congela na aprovação)
│                   │     abordagem mínima, fora de escopo)
└────────┬──────────┘
         ▼ (aprovação)
┌───────────────────┐
│ 3. IMPLEMENTAR    │  ← no repo, herança de convenções (registra em `03 - Implementação`)
└────────┬──────────┘
         ▼
┌───────────────────┐
│ 4. TESTAR         │  ← regressão + tsc/test/audits/build (evidências em `03 - Implementação`)
└────────┬──────────┘
         ▼
┌───────────────────┐
│ 5. VALIDAR        │  ← CTs do pacote QA + docs (UPDATES/STATUS) + `04 - Code review` (✅/🔁)
└────────┬──────────┘
         ▼
┌───────────────────┐
│ 6. FECHAR         │  ← card + pasta `<ID>/` → 05 Arquivo/<projeto>/<ID>/ + daily + commit
└───────────────────┘
```

## Ramificações de execução

```text
QA · demanda pronta
  ├─ BUG <PROJ>-NNN ──→ 03 Trabalho/DEV/<projeto>/Fixes/<PROJ>-NNN/
  └─ MEL <PROJ>-MEL-NNNN ─→ 03 Trabalho/DEV/<projeto>/Execuções/<PROJ>-MEL-NNNN/

após implementação e review
  ├─ gates vermelhos ──→ voltar para 03 - Implementação
  ├─ review solicita ajustes ──→ voltar para 02 ou 03
  ├─ CT falha em dev ──→ bug filho <PROJ>-NNN (pai: <ID>)
  └─ CT aprovado ──→ QA · Validação → Concluído → 05 Arquivo/<projeto>/<ID>/
```

## Entrada obrigatória do DEV

O DEV só inicia o planejamento quando o pacote QA tiver:

- `01 - Bug.md` ou `01 - Demanda.md` compreensível sem contexto oral;
- escopo e fora de escopo definidos;
- critérios de aceite objetivos;
- `02 - Casos de teste.md` criado e relacionado aos critérios;
- nenhuma decisão bloqueante pendente;
- `etapa_atual` indicando entrega ao DEV.

## Regras

1. **Confirmar antes de planejar** — bug sem causa confirmada não vira plano; melhoria com decisão pendente bloqueante não inicia implementação.
2. **Instanciar templates** — cada nota de análise, plano, implementação e review nasce copiando o template correspondente em `Templates/Execução/` ou `Templates/Fix/`.
3. **Plano antes de implementar** — sem aprovação, nada de código.
4. **Etapa 4 sem verde não segue** — gate vermelho volta para a etapa 3.
5. **Registrar** cada etapa na pasta `03 Trabalho/DEV/<projeto>/<Fixes|Execuções>/<ID>/` e no fechamento a pasta **move junto com o card** para `05 Arquivo/<projeto>/<ID>/`.

## Resultado esperado

Item entregue no repo (commit convencional), pasta `03 Trabalho/DEV/<projeto>/<Fixes|Execuções>/<ID>/` completa (análise → plano → implementação → review → verificação), card fechado e registrado na daily — ou, se houver causa ou decisão não confirmada, o card sinalizado de volta para análise.
