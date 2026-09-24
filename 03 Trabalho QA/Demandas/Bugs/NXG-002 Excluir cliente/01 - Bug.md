---
prioridade: media
status: backlog
tipo: bug
etapa_atual: "QA · Análise da demanda"
modulo: cliente
plano: ""
execucao: ""
ambiente: dev
origem: repo
pai: ""
data_inicio: ""
data_fim: ""
responsavel: ""
pontos_alocados: ""
---
# Excluir cliente (sem UI)

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> **Artefatos QA:** [[02 - Casos de teste]] · validação será criada quando o fix for executado.

## Sintoma

Backend DELETE /api/clientes/:id funciona (smoke ok), mas o ClienteDetail não tem ação de excluir.

## Onde

- frontend/src/modules/cliente/pages/ClienteDetail.tsx · deleteCliente service (sem uso)

## Fonte

- docs/product/06-CASOS-DE-USO.md:1009
