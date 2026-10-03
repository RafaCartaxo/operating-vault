---
prioridade: media
status: backlog
tipo: melhoria
etapa_atual: "QA · Triagem"
modulo: navegacao
plano: "[[02 - Plano de teste]]"
execucao: ""
ambiente: dev
origem: conversa
projeto: financas-pessoais
pai: "[[FIN-MEL-0010 Ação novo lançamento mobile/01 - Demanda|FIN-MEL-0010 — Ação de novo lançamento mobile]]"
data_inicio: ""
data_fim: ""
responsavel: ""
pontos_alocados: 5
---

# FIN-MEL-0011 — Organização da navbar mobile

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

Após a remoção de Novo lançamento da navbar, resta apenas Acompanhamento. A barra ainda usa texto por extenso e precisa se comportar como uma coleção de destinos, preparada para crescer sem ajustes manuais de posicionamento.

---

## Objetivo

Entregar uma navbar mobile compacta, centrada e extensível, com destinos representados por ícones e distribuição automática de 1 a 5 itens.

### Entrega desta capacidade

Será ajustada a estrutura visual da navbar para usar uma lista de destinos, ícones acessíveis e distribuição automática conforme a quantidade de itens.

---

## Decisões de produto

- A navbar será exclusiva para destinos de navegação.
- Acompanhamento será representado por ícone coerente, com `aria-label`/tooltip acessível.
- Com 1 item, o destino ficará centralizado.
- Com 2 a 5 itens, os destinos serão distribuídos uniformemente.
- Novo lançamento continuará fora da navbar, como botão flutuante à direita.

---

## Escopo

- Alinhamento e distribuição automática dos destinos.
- Substituição do texto fixo de Acompanhamento por ícone acessível.
- Suporte visual para 1 a 5 destinos sem posicionamentos manuais.
- Preservação da ação flutuante e da navegação desktop.

---

## Fora de escopo

- Novas áreas ou funcionalidades de negócio.
- Alteração do botão flutuante de Novo lançamento.
- Alteração do modal, formulário, API ou regras financeiras.

---

## Critérios de aceite

- C1. Com um único destino, o ícone fica centralizado na navbar. ^c1
- C2. Com 2 a 5 destinos, os ícones são distribuídos uniformemente. ^c2
- C3. Adicionar ou remover destinos ajusta o layout automaticamente. ^c3
- C4. Acompanhamento é representado por ícone coerente e acessível, sem texto fixo por extenso. ^c4
- C5. Novo lançamento permanece fora da navbar, como botão flutuante à direita, sem regressão desktop. ^c5

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
