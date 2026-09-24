---
demanda: "[[01 - Bug|NXG-003]]"
fix: "[[05 Arquivo/Bugs/NXG-003/DEV/NXG-003/00 README|Fix NXG-003]]"
ambiente: dev
versao: a preencher
status: concluido
responsavel: ""
resultado: aprovado
pontos: 0
ct_resultados:
  ct_b01: ✅ Aprovado
  ct_b02: ✅ Aprovado
data_inicio: "2026-09-12"
data_fim: "2026-09-12"
---
# Validação — NXG-003

> [!info]- Navegação QA/DEV
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Fix DEV:** [[05 Arquivo/Bugs/NXG-003/DEV/NXG-003/00 README|Fix NXG-003]]  
> **Validação:** [[03 - Validação dev]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`  
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Validação funcional do fix. Registrar o resultado de cada CT e anexar evidências somente quando necessário.

---

## Contexto

- **Ambiente:** `dev`
- **Versão/build:** a preencher
- **Escopo:** [[02 - Casos de teste|CT-B01 e CT-B02]]

---

## Resultado dos casos de teste

| CT | Resultado | Evidência | Observação | Defeito/Bug |
|---|---|---|---|---|
| [[02 - Casos de teste#^ct-b01\|CT-B01]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_b01]` |  |  |  |
| [[02 - Casos de teste#^ct-b02\|CT-B02]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_b02]` |  |  |  |

---

## Decisão da validação

**Resultado geral:** ✅ Aprovado

Os dois cenários foram executados em `dev`, na criação e na edição do cliente. O endereço pessoal inicia recolhido e o endereço do comércio permanece expandido.

---

## Checklist de encerramento QA

- [x] CT-B01 e CT-B02 executados ou justificados.
- [x] Evidências registradas quando necessário.
- [x] Bugs filhos vinculados, se houver nova falha.
- [x] Resultado geral e status atualizados.
