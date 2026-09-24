# Skill: Correção de Bug — trabalho do DEV (NX Gest)

O workflow do **trabalho do DEV**, espelho do `Skills/BUG` (que é o trabalho do QA). O bug chega com causa provável (card em `analise`); o fix sai testado, validado e fechado.

## O ciclo

1. **Pega o card** — lê o bug (`03 Trabalho QA/Demandas/Bugs/NXG-NNN`, template `Templates/Bug/01 - Bug`): sintoma, causa provável, CTs, ambiente.
2. **Confirma a causa no código** — ler o código citado, reproduzir o comportamento. **Nada se assume**: causa não confirmada volta como pergunta, não como plano.
3. **Planeja o fix** — pasta `04 Trabalho DEV/Fixes/NXG-NNN/` (`00 README` + `01 - Análise` + `02 - Plano de correção` + `03 - Implementação` + `04 - Code review`; modelos em `Templates/Fix/`): arquivos a tocar, abordagem **mínima** herdando as convenções reais e **fora de escopo** explícito. O plano **congela na aprovação**; o `03 - Implementação` registra o que foi feito.
4. **Implementa** — só após o plano aprovado (no repo, módulo do bug).
5. **Testa** — regressão em `*.test.tsx` (o comportamento quebrado vira teste) + `npx tsc --noEmit` · `npm test` · `audit:ui/styles` · `build`.
6. **Valida** — executa os **CTs em `02 - Casos de teste.md`** (manual quando DOM/comportamento) + `docs:audit` se doc mudou + atualiza `UPDATES.md`/`STATUS.md` quando for entrega. O fix referencia os CTs e registra o resultado no arquivo de validação QA — nunca duplica cenários. **Push/deploy só após os CTs manuais locais verdes** — decisão do dono.
7. **Fecha** — card → ✅ Feito → `05 Arquivo/` + registro na daily. Commit convencional (`fix(<modulo>): <o quê> (<card>)`).
## Regras

- **Um bug = um fix.** Nunca dois bugs no mesmo commit sem vínculo explícito.
- **Sem escopo rastejante** — o que não está no card/plano do fix vira card novo (melhoria).
- **Sem mudança de regra de negócio** sem BR (se o fix exigir, vira plano próprio).
- **CTs do pacote QA são o teste de pronto** — fix sem CT executado não fecha.
- **Gates do repo** antes de commitar (tsc/test/audits); CI valida no push.
