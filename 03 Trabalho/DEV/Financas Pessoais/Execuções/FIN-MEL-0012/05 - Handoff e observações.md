# Handoff — FIN-MEL-0012

> Relatório de contexto para retomada por outro chat/agente. Este documento registra observações; não representa confirmação de funcionamento nem aprovação funcional.

## Contexto

A FIN-MEL-0012 implementa recorrências mensais para Finanças Pessoais.

Objetivos observados:

- cadastrar uma regra recorrente;
- gerar uma ocorrência mensal;
- evitar duplicidade por recorrência e competência;
- permitir encerramento preservando o histórico;
- marcar explicitamente recorrências já incluídas em fatura;
- manter essas ocorrências visíveis, mas fora do saldo quando aplicável.

## Implementação realizada

### Backend

- Tabela `recorrencias`.
- Campos de vínculo em `lancamentos`.
- Índice único por `recorrencia_id` e `recorrencia_competencia`.
- Geração idempotente das ocorrências.
- Endpoints:

```text
GET /api/recorrencias
POST /api/recorrencias
PUT /api/recorrencias/{id}
DELETE /api/recorrencias/{id}
```

### Frontend

- Tela de Recorrências.
- Criação, edição e encerramento.
- Validação dos campos.
- Checkbox “Já está incluída na fatura”.
- Atualização do resumo mensal.
- Navegação própria para Recorrências.

### Documentação e processo

Foram atualizados os documentos de arquitetura, modelo de dados, API, fluxos, ambiente local, execução DEV e templates de implementação.

## Validações técnicas realizadas

- 23 testes frontend aprovados.
- Build TypeScript/Vite aprovado.
- Testes Go aprovados.
- Gate documental do pacote QA aprovado.
- Testes de domínio para datas de recorrência adicionados.
- Migração e reabertura de banco analisadas.
- Proxy Vite alterado para aceitar `VITE_API_PROXY_TARGET`.
- `strictPort: true` adicionado para impedir fallback silencioso de `5173` para `5174`.
- Launcher `npm run dev:local` criado.

## Observação funcional principal

A criação de recorrência foi confirmada, mas a consulta mensal que gera automaticamente suas ocorrências falhou durante a validação funcional.

Foi observado o erro de interface:

```text
não foi possível salvar recorrência
```

Também foi observado:

```text
Port 5173 is in use, trying another one...
Local: http://localhost:5174/
Network: http://192.168.0.86:5174/
```

Após a regularização do ambiente, o erro permaneceu reproduzível diretamente na API de lançamentos.

O diagnóstico capturou `database is locked (5) (SQLITE_BUSY)` na função `EnsureMonth`: o backend mantém o cursor da consulta de recorrências aberto enquanto tenta inserir as ocorrências na mesma base SQLite.

## Estado do ambiente

Foram feitas tentativas de:

- identificar processos antigos;
- liberar as portas `3000`, `3001`, `5173` e `5174`;
- iniciar o backend em `3001`;
- iniciar o frontend em `5173`;
- testar via navegador;
- testar via celular;
- iniciar um launcher único.

O ambiente do agente não conseguiu controlar os processos iniciados em outro chat/terminal. Também houve bloqueio do sandbox para:

- abrir sockets locais;
- inspecionar processos escutando portas;
- acessar o navegador integrado;
- baixar dependências Go pela rede.

Não há confirmação de que o launcher tenha sido executado com sucesso no ambiente real do usuário.

## Launcher criado

Arquivo:

```text
financas-pessoais/scripts/dev-local.sh
```

Uso previsto:

```bash
npm run dev:local
```

Parar instâncias gerenciadas pelo launcher:

```bash
npm run dev:local -- --stop
```

Comportamento previsto:

1. encerrar instâncias previamente gerenciadas;
2. iniciar o backend em `3001`;
3. aguardar `GET /api/health`;
4. iniciar o frontend em `5173`;
5. configurar o proxy para `3001`;
6. manter logs em `/tmp/financas-pessoais-dev/`.

Esse comportamento ainda precisa ser observado em execução real.

## Observações sobre o entendimento do Vault

O Vault descreve a separação `QA → DEV → QA`, mas alguns pontos não estavam suficientemente explícitos para execução automatizada:

- build verde não equivale a aplicação funcional disponível;
- o smoke check do backend deve usar `/api/health`, não `/`;
- o endereço acessado pelo celular é o frontend, não o backend;
- a porta do backend e o destino do proxy precisam ser registrados juntos;
- uma porta alternativa escolhida pelo Vite não deve ser aceita sem atualizar o endereço usado no celular;
- processos iniciados em outro terminal/chat não são necessariamente controláveis pelo agente atual;
- documentação de ambiente não garante que o ambiente esteja ativo;
- a etapa “entregue para QA” não deve ocorrer antes de confirmar navegador, API e fluxo funcional quando o CT depende deles.

## Situação da demanda

A FIN-MEL-0012 está tecnicamente implementada, mas a validação funcional reprovou o CT-002. O defeito filho `FIN-BUG-0001` foi criado e a correção retornou ao DEV.

Não registrar como aprovada funcionalmente até confirmar:

1. backend respondendo em `/api/health`;
2. frontend em `5173`;
3. proxy encaminhando para o backend correto;
4. criação via `POST /api/recorrencias`;
5. recorrência aparecendo na tela;
6. execução dos CTs no navegador e no celular.

## Próxima observação recomendada

Executar no ambiente real:

```bash
curl -i http://localhost:3001/api/health
curl -i http://localhost:5173/
```

Depois observar no navegador a chamada:

```text
POST /api/recorrencias
```

Registrar URL efetiva, status HTTP, corpo da resposta, porta do frontend, porta do backend e se a chamada veio do Vite ou de outro processo.

A funcionalidade só deve avançar para aprovação após essas observações e os CTs correspondentes.
