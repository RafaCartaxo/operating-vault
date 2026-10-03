---
prioridade: media
status: validacao
tipo: melhoria
etapa_atual: "QA · Validação"
modulo: lancamentos
plano: "[[02 - Plano de teste]]"
execucao: "[[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0009/00 README|Execução DEV]]"
ambiente: dev
origem: conversa
projeto: financas-pessoais
epico: "[[04 Projetos/Financas Pessoais/Epicos/FIN-EPIC-0001 Evolução lançamentos mobile/00 README|FIN-EPIC-0001 — Evolução da experiência de lançamentos mobile]]"
pai: "[[FIN-MEL-0006 Navegação estilo aplicativo/01 - Demanda|FIN-MEL-0006 — Navegação estilo aplicativo]]"
data_inicio: ""
data_fim: ""
responsavel: ""
pontos_alocados: 8
---

# FIN-MEL-0009 — Navegação do lançamento por modal

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** será criada após aprovação QA.

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** preencher `projeto` no frontmatter antes de roteiar a melhoria.


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

Após a FIN-MEL-0006, o sistema possui áreas separadas de Lançamentos e Acompanhamento. No uso mobile, abrir uma área exclusiva apenas para cadastrar uma despesa ou receita adiciona uma etapa desnecessária. O Acompanhamento deve funcionar como tela principal, enquanto o cadastro passa a ser uma ação rápida.

---

## Objetivo

Permitir que o usuário consulte o Acompanhamento como tela principal e abra o formulário de lançamento em um modal pelo botão de adicionar, sem perder as validações e fluxos já aprovados.

### Entrega desta capacidade

Será entregue a reorganização da entrada de lançamentos em modal/container, com botão de adicionar, atualização do acompanhamento após sucesso e comportamento responsivo no mobile.

---

## Decisões de produto

- A tela principal será Acompanhamento/Histórico.
- A criação será iniciada por um botão de adicionar visível e acessível.
- O formulário existente será reutilizado dentro do modal; campos, máscara, validações e parcelamento permanecem os mesmos.
- O modal só será fechado automaticamente após confirmação de sucesso.
- Lançamentos com data fora do mês filtrado serão salvos, mas não aparecerão indevidamente na lista filtrada.
- A demanda depende da navegação entregue em FIN-MEL-0006 e não substitui seus critérios aprovados; ela evolui o ponto de entrada do cadastro.

---

## Escopo

- Acompanhamento como tela inicial/principal.
- Botão de adicionar para abrir novo lançamento.
- Formulário de lançamento dentro de modal/container com rolagem quando necessário.
- Preservação dos campos, validações, máscara de valor e parcelamento existentes.
- Atualização do acompanhamento após salvamento bem-sucedido.
- Tratamento de carregamento, erro e prevenção de envio duplicado.
- Compatibilidade com mobile e desktop.

---

## Fora de escopo

- Alterações nas regras financeiras ou na API de lançamentos.
- Novos tipos de lançamento, recorrência ou sincronização offline.
- Menu lateral ou novas áreas de navegação.
- Reconstrução da edição de lançamentos; ela deve apenas continuar funcionando se já estiver disponível.

---

## Critérios de aceite

- C1. O Acompanhamento é apresentado como tela principal, sem exigir uma área exclusiva de lançamento. ^c1
- C2. O botão de adicionar é visível, acessível e não cobre filtros/cards; ao ser acionado, abre o formulário em modal/container com fechamento/cancelamento disponível. ^c2
- C3. O modal permanece utilizável no mobile, com conteúdo contido, rolagem e interação correta com teclado e data. ^c3
- C4. O formulário mantém campos, validações, máscara de valor e parcelamento já aprovados. ^c4
- C5. Um lançamento válido é salvo e o acompanhamento é atualizado sem recarregamento manual. ^c5
- C6. O filtro de mês ativo é respeitado para lançamentos com data fora do período. ^c6
- C7. Salvamento em andamento impede múltiplos envios e o modal não fecha antes da confirmação. ^c7
- C8. Erro de API ou rede exibe feedback e não indica sucesso falso; desktop permanece sem regressão. ^c8
- C9. Fechar ou cancelar o modal sem salvar não cria nem altera lançamentos. ^c9
- C10. A edição de lançamento existente continua acessível e funcional após a mudança de entrada. ^c10

---

## Checklist de entrega ao DEV

- [ ] Decisões e regras de negócio estão fechadas.
- [ ] Escopo e fora de escopo estão claros.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- No mobile, o lançamento será apresentado em bottom sheet/modal com rolagem interna.
- No desktop, o lançamento será apresentado em modal centralizado.
- No mobile, o acesso será por botão flutuante; no desktop, por ação visível no cabeçalho.
