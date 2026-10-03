---
prioridade: media
status: backlog
tipo: melhoria
etapa_atual: "QA · Triagem"
modulo: lancamentos
plano: "[[02 - Plano de teste]]"
execucao: ""
ambiente: dev
origem: observado
projeto: financas-pessoais
epico: ""
pai: ""
data_inicio: ""
data_fim: ""
responsavel: ""
pontos_alocados: 8
---

# FIN-MEL-0012 — Recorrências mensais sem duplicidade

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** ainda não criada — aguarda aprovação do pacote QA.

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** `financas-pessoais`.


> [!info] Status atual
> **Próximo passo:** registrar a próxima ação objetiva.

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> **Capacidade alocada:** preencher `pontos_alocados`.
> Exemplo: se houver 50 pontos disponíveis no ciclo, usar `pontos_alocados: 50`.
>
> ```dataviewjs
> const id = (dv.current().file.path.match(/(?:[A-Z]{2,8}-)?MEL-\d+/) || [""])[0];
> const paginas = dv.pages().where(p => id && p.file.path.includes(id) && typeof p.pontos === "number");
> const lista = paginas.sort(p => p.file.name);
> const necessario = lista.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> const alocado = Number(dv.current().pontos_alocados || 0);
> const diferenca = alocado - necessario;
> if (lista.length > 0) {
>   dv.table(["Etapa/artefato", "Pontos"], lista.map(p => [p.file.link, p.pontos]));
> } else {
>   dv.paragraph("Nenhum artefato com pontos registrado ainda.");
> }
> dv.paragraph(`**Esforço necessário:** ${necessario} pontos · **Capacidade alocada:** ${alocado} pontos · **${diferenca >= 0 ? "Saldo" : "Déficit"}:** ${Math.abs(diferenca)} pontos`);
> ```

---

## Problema / contexto

O planejamento financeiro mantém despesas recorrentes — como TotalPass, Meli+ e VPS — separadas para controle, mas informa que elas já podem estar dentro das faturas dos cartões e não devem ser descontadas novamente. A aplicação ainda não possui uma regra de recorrência que gere as ocorrências mensais sem duplicar o valor.

---

## Objetivo

Permitir cadastrar uma despesa recorrente mensal, gerar suas ocorrências no período configurado e distinguir controle de recorrência de despesa já consolidada em fatura.

### Entrega desta capacidade

Cadastro da regra recorrente, geração mensal com série identificável, término por data final e visualização mensal sem duplicidade de cobrança.

---

## Decisões de produto

- Recorrente é uma cobrança mensal fixa, não uma parcela de quantidade fechada.
- O vínculo com cartão/conta é obrigatório para identificar onde a cobrança ocorre.
- Recorrentes associados a uma fatura devem aparecer para controle, mas não ser somados novamente ao saldo como uma despesa avulsa.
- Parcelas permanecem no fluxo de FIN-MEL-0008; contas fixas permanecem como categoria própria.

---

## Escopo

- Criar uma regra mensal com descrição, valor, cartão/conta, início e término opcional.
- Gerar uma ocorrência por mês, com vínculo à regra de origem.
- Editar, encerrar e consultar ocorrências da regra.
- Preservar o cálculo mensal sem dupla contagem de recorrentes já incluídos em faturas.

---

## Fora de escopo

- Importação automática de dados bancários ou de faturas.
- Conciliação de fatura real com transações do cartão.
- Frequências diferentes de mensal.
- Parcelamento, contas fixas e recorrências de receitas.

---

## Critérios de aceite

- C1. O usuário cadastra uma despesa recorrente mensal com descrição, valor, cartão/conta, data inicial e término opcional. ^c1
- C2. O sistema gera no máximo uma ocorrência por mês para cada regra ativa, preservando a série de origem e o valor configurado. ^c2
- C3. Uma regra com data final deixa de gerar ocorrências após o mês final; uma regra sem data final permanece ativa. ^c3
- C4. O usuário consegue editar ou encerrar a regra sem perder as ocorrências já geradas. ^c4
- C5. Recorrente associado a fatura aparece para controle, mas não é somado novamente ao saldo quando a fatura já contém a cobrança. ^c5
- C6. Falhas de validação impedem a criação de regra incompleta ou com valor/data inválidos, sem criar ocorrência parcial. ^c6

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Nenhuma. Se houver pendência, manter `status: analise`.
