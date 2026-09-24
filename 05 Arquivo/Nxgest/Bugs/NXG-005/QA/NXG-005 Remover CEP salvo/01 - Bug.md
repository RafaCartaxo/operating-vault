---
prioridade: media
status: backlog
tipo: bug
etapa_atual: "QA · Triagem"
modulo: cliente
ambiente: dev
origem: "Validação MEL-0001"
projeto: nxgest
pai: MEL-0001
data_inicio: "2026-09-12"
data_fim: ""
responsavel: ""
pontos_alocados: ""
---
# NXG-005 — Remover CEP salvo não limpa o cadastro

> [!info]- Navegação QA/DEV
> **Bug:** [[00 README]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Validação QA:** [[03 - Validação dev]]  
> **Demanda pai:** [[05 Arquivo/Nxgest/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/01 - Demanda|MEL-0001 — Cliente CEP]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> Preencha `pontos_alocados` após a triagem e a estimativa do fix.

## Comportamento observado

Um cliente possui CEP salvo. Ao editar o cadastro, apagar o CEP e salvar, o CEP antigo continua no cadastro.

## Passo a passo para reproduzir

**Dado** um cliente com CEP salvo  
**Quando** apago o CEP e salvo a edição  
**Então** o CEP anterior permanece salvo.

## Resultado esperado

O CEP deve ser removido e retornar vazio na próxima edição/API. A localização aproximada derivada também deve ser removida; um GPS manual independente deve permanecer.

## Critério de aceite

- C1. Remover um CEP salvo limpa o CEP persistido e a localização aproximada derivada. ^c1

## Checklist de entrega ao DEV

- [x] Sintoma, ambiente e passos de reprodução estão claros.
- [x] Resultado esperado está definido.
- [x] Critério de aceite é objetivo e testável.
- [ ] Casos de teste executados.
- [ ] `pontos_alocados` foi preenchido.
