---
demanda: "[[01 - Demanda|MEL-0001 Cliente CEP]]"
execucao: "[[05 Arquivo/Melhorias/MEL-0001/DEV/MEL-0001/00 README|MEL-0001 — execução]]"
ambiente: dev
versao: ""
status: concluido
responsavel: ""
resultado: aprovado
pontos: 0
ct_resultados:
  ct_001: ✅ Aprovado
  ct_002: ✅ Aprovado
  ct_003: ✅ Aprovado
  ct_004: ✅ Aprovado
  ct_005: ✅ Aprovado
  ct_006: ✅ Aprovado
  ct_007: ✅ Aprovado
  ct_008: ✅ Aprovado
  ct_009: ✅ Aprovado
  ct_010: ✅ Aprovado
data_inicio: ""
data_fim: ""
---
# Validação — MEL-0001

> [!info]- Navegação QA
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`  
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

---

## Contexto

- Ambiente: `dev`
- Versão/build:
- Escopo: [[03 - Casos de teste|CT-001 a CT-010]]

---

## Resumo da execução

```dataviewjs
const resultados = dv.current().ct_resultados ?? {};
const valores = Object.values(resultados).map(String);
const total = valores.length;
const aprovados = valores.filter((valor) => valor.includes("Aprovado")).length;
const peso = (valor) => {
  if (valor.includes("Aprovado") || valor.includes("Falhou")) return 1;
  if (valor.includes("Em andamento")) return 0.25;
  if (valor.includes("Bloqueado")) return 0.5;
  return 0;
};
const executados = valores.filter((valor) => peso(valor) > 0).length;
const pontos = Number(dv.current().pontos) || 0;
const entregues = total ? Math.round(valores.reduce((soma, valor) => soma + (pontos / total) * peso(valor), 0) * 100) / 100 : 0;
dv.list([
  `CTs aprovados: ${aprovados}/${total}`,
  `CTs executados: ${executados}/${total}`,
  `Pontos da etapa: ${pontos}`,
  `Pontos entregues: ${entregues} de ${pontos}`,
]);
```

> Os pontos são calculados na tabela conforme o status de cada CT: aprovado/falhou = 100%; em andamento = 25%; bloqueado = 50%; aguardando/não executado = 0%.

---

## Resultado dos casos de teste

| CT | Resultado | Evidência | Observação | Defeito/Bug | Pontos entregues |
|---|---|---|---|---|---:|
| [[03 - Casos de teste#^ct-001\|CT-001]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_001]` |  | Retestado após o Fix NXG-004: salvamento aprovado. | [[05 Arquivo/Bugs/NXG-004/QA/NXG-004 CEP preenchido não permite salvar/01 - Bug\|NXG-004]] | 0 |
| [[03 - Casos de teste#^ct-002\|CT-002]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002]` |  |  |  | 0 |
| [[03 - Casos de teste#^ct-003\|CT-003]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_003]` |  | Retestado após o Fix NXG-006: mensagem exibida ao salvar. | [[05 Arquivo/Bugs/NXG-006/QA/NXG-006 CEP inválido não exibe mensagem/01 - Bug\|NXG-006]] | 0 |
| [[03 - Casos de teste#^ct-004\|CT-004]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_004]` |  |  |  | 0 |
| [[03 - Casos de teste#^ct-005\|CT-005]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_005]` |  |  |  | 0 |
| [[03 - Casos de teste#^ct-006\|CT-006]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_006]` |  |  |  | 0 |
| [[03 - Casos de teste#^ct-007\|CT-007]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_007]` |  |  |  | 0 |
| [[03 - Casos de teste#^ct-008\|CT-008]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_008]` |  | Corrigido no NXG-003; endereço pessoal inicia recolhido e o comércio permanece expandido. | [[05 Arquivo/Bugs/NXG-003/QA/NXG-003 Endereço pessoal inicia aberto/01 - Bug\|NXG-003]] | 0 |
| [[03 - Casos de teste#^ct-009\|CT-009]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_009]` |  |  |  | 0 |
| [[03 - Casos de teste#^ct-010\|CT-010]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_010]` |  | Retestado após o Fix NXG-005: CEP removido e não retornou na edição. | [[05 Arquivo/Bugs/NXG-005/QA/NXG-005 Remover CEP salvo/01 - Bug\|NXG-005]] | 0 |

> Adicione CT-002 a CT-009 à tabela mantendo o mesmo padrão de resultado e vínculo.

---

## Histórico de validação

- **Rodada 1 — ❌ Reprovada:** CT-008 identificou o endereço pessoal expandido indevidamente.
- **Correção:** [[05 Arquivo/Bugs/NXG-003/QA/NXG-003 Endereço pessoal inicia aberto/01 - Bug|NXG-003]] → [[05 Arquivo/Bugs/NXG-003/DEV/NXG-003/00 README|Fix NXG-003]] → [[05 Arquivo/Bugs/NXG-003/DEV/NXG-003/04 - Code review|Code review aprovado]].
- **Reteste — ✅ Aprovado:** CT-008 foi executado novamente em criar e editar; o endereço pessoal inicia recolhido e o comércio permanece expandido.
- **Rodada — ❌ Reprovada:** CT-010 identificou que remover um CEP salvo não limpa o valor persistido; o defeito foi registrado como [[05 Arquivo/Bugs/NXG-005/QA/NXG-005 Remover CEP salvo/01 - Bug|NXG-005]].
- **Rodada — ❌ Reprovada:** CT-003 identificou que CEP inválido não exibe mensagem; o defeito foi registrado como [[05 Arquivo/Bugs/NXG-006/QA/NXG-006 CEP inválido não exibe mensagem/01 - Bug|NXG-006]].

---

## Decisão da validação

**Resultado geral:** ✅ aprovado — todos os CTs foram executados e aprovados após as correções NXG-003, NXG-004, NXG-005 e NXG-006.

---

## Checklist de encerramento QA

- [x] Todos os CTs executados ou justificados.
- [ ] Evidências registradas quando necessário.
- [x] Bug filho [[05 Arquivo/Bugs/NXG-003/QA/NXG-003 Endereço pessoal inicia aberto/01 - Bug|NXG-003]] vinculado.
- [x] Bug filho [[05 Arquivo/Bugs/NXG-004/QA/NXG-004 CEP preenchido não permite salvar/01 - Bug|NXG-004]] vinculado ao CT-001.
- [x] CT-008 reexecutado após a correção.
- [x] Resultado geral e status atualizados após concluir os demais CTs.
