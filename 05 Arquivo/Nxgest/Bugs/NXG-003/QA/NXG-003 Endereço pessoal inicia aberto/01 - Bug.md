---
prioridade: media
status: concluido
tipo: bug
etapa_atual: "Concluído"
modulo: cliente
ambiente: dev
origem: "Validação MEL-0001"
projeto: nxgest
pai: MEL-0001
data_inicio: "2026-09-12"
data_fim: ""
responsavel: ""
pontos_alocados: ""
pontos: 0
---
# NXG-003 — Endereço pessoal inicia aberto

> [!info]- Navegação QA/DEV
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Demanda pai:** [[05 Arquivo/Nxgest/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/01 - Demanda|MEL-0001]]
> **Fix DEV:** [[05 Arquivo/Nxgest/Bugs/NXG-003/DEV/NXG-003/00 README|Fix NXG-003]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> Preencha `pontos_alocados` somente após a triagem e a estimativa do Fix.

---

## Comportamento observado

Durante a validação da MEL-0001, o bloco **Endereço pessoal** aparece expandido por padrão na criação e na edição do cliente.

---

## Passo a passo para reproduzir

**Dado** que estou no cadastro de um cliente novo ou na edição de um cliente existente  
**Quando** a tela é aberta  
**Então** o bloco Endereço pessoal é exibido expandido imediatamente.

---

## Resultado esperado

O bloco Endereço pessoal deve iniciar recolhido em criar e editar. Ao expandi-lo, os dados existentes devem continuar preservados. O bloco Endereço do comércio permanece expandido.

---

## Evidências

- Validação QA da MEL-0001: CT-008 reprovado.
- Evidência visual: bloco Endereço pessoal aparece expandido ao abrir o formulário.

---

## Critérios de aceite

- C1. Endereço pessoal inicia recolhido na criação. ^c1
- C2. Endereço pessoal inicia recolhido na edição, sem perder dados ao expandir. ^c2
- C3. Endereço do comércio continua expandido. ^c3

---

## Checklist de entrega ao DEV

- [x] Sintoma, ambiente e passos de reprodução estão claros.
- [x] Resultado esperado está definido.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Contexto da execução

- Ambiente: `dev`
- Versão/build: a preencher
- Demanda pai: [[05 Arquivo/Nxgest/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/04 - Validação dev|Validação MEL-0001]]
