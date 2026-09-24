---
prioridade: media
status: backlog
tipo: bug
etapa_atual: "QA · Análise da demanda"
modulo: gasto
plano: ""
execucao: ""
ambiente: dev
origem: repo
projeto: nxgest
pai: ""
data_inicio: ""
data_fim: ""
responsavel: ""
pontos_alocados: ""
---
# Excluir gasto (GastoList órfão)

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> **Artefatos QA:** [[02 - Casos de teste]] · validação será criada quando o fix for executado.

## Sintoma

Backend DELETE /api/gastos/:id funciona (smoke GST-054), mas nenhuma tela usa o GastoList com onDelete — exclusão de gasto não existe na UI.

## Onde

- frontend/src/modules/gasto/components/GastoList.tsx (órfão) · GastoPage (só criação)

## Fonte

- docs/product/06-CASOS-DE-USO.md:1066 · smoke GST-054
