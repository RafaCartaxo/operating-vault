---
prioridade: media
status: concluido
tipo: melhoria
etapa_atual: "Concluído"
modulo: navegacao
plano: "[[02 - Plano de teste]]"
execucao: "[[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0010/00 README|Execução DEV]]"
ambiente: dev
origem: conversa
projeto: financas-pessoais
epico: "[[04 Projetos/Financas Pessoais/Epicos/FIN-EPIC-0001 Evolução lançamentos mobile/00 README|FIN-EPIC-0001 — Evolução da experiência de lançamentos mobile]]"
pai: "[[FIN-MEL-0009 Navegação lançamento modal/01 - Demanda|FIN-MEL-0009 — Navegação do lançamento por modal]]"
data_inicio: ""
data_fim: ""
responsavel: ""
pontos_alocados: 5
---

# FIN-MEL-0010 — Ação de novo lançamento mobile

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0010/00 README|Execução DEV]]

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

Na FIN-MEL-0009, o acesso a “Novo lançamento” foi colocado na barra inferior com o mesmo peso visual do Acompanhamento. Isso mistura área de navegação com ação rápida e pode fazer o usuário entender que são duas telas equivalentes.

---

## Objetivo

Separar visualmente a navegação da ação principal no mobile, mantendo o Acompanhamento como área da barra inferior e oferecendo “Novo lançamento” por um botão de ação destacado.

### Entrega desta capacidade

O item “Novo lançamento” será removido da barra inferior mobile e substituído por um botão de ação destacado, sem alterar o modal ou o fluxo de persistência já implementados.

---

## Decisões de produto

- A barra inferior ficará reservada às áreas/telas de navegação.
- “Novo lançamento” será uma ação rápida representada por botão destacado, preferencialmente com `+`.
- O botão abrirá o modal existente da FIN-MEL-0009.
- O botão deve respeitar safe areas e não sobrepor filtros, cards ou ações importantes.
- O desktop permanece com a ação de cabeçalho já implementada.

---

## Escopo

- Ajuste da navegação mobile.
- Remoção de “Novo lançamento” como item equivalente da barra inferior.
- Criação/reposicionamento de botão de ação destacado.
- Reutilização do modal existente.
- Garantia de posicionamento em diferentes tamanhos de viewport mobile.

---

## Fora de escopo

- Alterações no formulário, modal ou regras financeiras.
- Alterações no histórico/acompanhamento além da navegação visual.
- Novas áreas de navegação.
- Mudanças na persistência ou API.

---

## Critérios de aceite

- C1. A barra inferior mobile apresenta somente áreas de navegação, sem “Novo lançamento” como item equivalente. ^c1
- C2. Existe uma ação destacada e acessível para iniciar um novo lançamento. ^c2
- C3. Acionar a ação abre o modal existente sem alterar seu comportamento. ^c3
- C4. O botão respeita safe areas, não cobre conteúdo e funciona em diferentes dimensões mobile. ^c4
- C5. A navegação e o botão de ação não causam regressão na experiência desktop. ^c5

---

## Checklist de entrega ao DEV

- [ ] Decisões e regras de negócio estão fechadas.
- [ ] Escopo e fora de escopo estão claros.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Plano e casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Nenhuma. Se houver pendência, manter `status: analise`.
