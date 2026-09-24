---
prioridade: baixa
status: backlog
modulo: ambiente
plano: ""
origem: observado
data_inicio: ""
data_fim: ""
responsavel: ""
---
# Dev servers locais (limpeza)

## Sintoma

Backend 3001 + Vite 5173 rodando via setsid (porta 3000 ocupada pelo Obsidian). Parar quando não precisar.

## Onde

- pkill -f 'tsx watch' ; pkill -f 'vite --host'

## Fonte

- sessão de 29/08
