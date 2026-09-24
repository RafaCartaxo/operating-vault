---
prioridade: media
status: backlog
tipo: bug
etapa_atual: "QA · Triagem"
modulo: cliente
ambiente: dev
origem: "Validação MEL-0001"
pai: MEL-0001
data_inicio: "2026-09-12"
data_fim: ""
responsavel: ""
pontos_alocados: ""
---
# NXG-006 — CEP inválido não exibe mensagem

> [!info]- Navegação QA/DEV
> **Bug:** [[00 README]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Validação QA:** [[03 - Validação dev]]  
> **Demanda pai:** [[05 Arquivo/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/01 - Demanda|MEL-0001 — Cliente CEP]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> Preencha `pontos_alocados` após a triagem e a estimativa do fix.

## Comportamento observado

Ao digitar um CEP com formato inválido, nenhuma mensagem é apresentada no campo nem antes do salvamento.

## Passo a passo para reproduzir

**Dado** o formulário de cliente aberto  
**Quando** digito um CEP com menos de oito dígitos  
**Então** o sistema não informa que o CEP está inválido.

## Resultado esperado

O formulário deve informar claramente que o CEP está inválido e orientar a correção ou a opção de salvar sem CEP, conforme a regra da MEL-0001.

## Critério de aceite

- C1. CEP com formato inválido exibe uma mensagem clara antes ou durante a tentativa de salvar. ^c1

## Checklist de entrega ao DEV

- [x] Sintoma, ambiente e passos de reprodução estão claros.
- [x] Resultado esperado está definido.
- [x] Critério de aceite é objetivo e testável.
- [ ] Casos de teste executados.
- [ ] `pontos_alocados` foi preenchido.
