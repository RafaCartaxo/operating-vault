---
prioridade: alta
status: backlog
tipo: bug
etapa_atual: QA · Triagem
modulo: cliente
ambiente: dev
origem: validação
pai: MEL-0001
data_inicio: 2026-09-12
data_fim: ""
responsavel: ""
pontos_alocados: ""
---
# NXG-004 — CEP preenchido não permite salvar

> [!info]- Navegação QA/DEV
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Validação QA:** [[03 - Validação dev]]  
> **Demanda pai:** [[05 Arquivo/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/01 - Demanda|MEL-0001 Cliente CEP]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> Preencha `pontos_alocados` após a triagem e a estimativa do fix.

---

## Comportamento observado

Com um CEP válido preenchido, a consulta retorna os dados do endereço e a localização aproximada é exibida como `CEP aprox.`. Ao salvar o cliente, a API retorna `VALIDATION_ERROR` com a mensagem `Dados inválidos.`.

## Passo a passo para reproduzir

**Dado** um formulário de cliente com CEP válido preenchido  
**Quando** a consulta do CEP retorna o endereço e tento salvar  
**Então** o cadastro é rejeitado com `VALIDATION_ERROR`.

## Resultado esperado

O CEP válido deve ser aceito com oito dígitos e o cliente deve ser salvo normalmente, preservando o endereço preenchido e a localização aproximada quando disponível.

## Critérios de aceite

- C1. CEP válido preenchido no endereço pessoal permite salvar o cliente normalmente. ^c1
- C2. CEP válido preenchido no endereço do comércio permite salvar o cliente normalmente. ^c2
- C3. O endereço retornado e a localização aproximada permanecem disponíveis após o salvamento. ^c3

## Evidências

- Resposta da API: `VALIDATION_ERROR` / `Dados inválidos.` após o CEP válido ser preenchido.
- Origem: [[05 Arquivo/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/04 - Validação dev|validação da MEL-0001]].

## Checklist de entrega ao DEV

- [x] Sintoma, ambiente e passos de reprodução estão claros.
- [x] Resultado esperado está definido.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.
