---
prioridade: media
status: analise
tipo: melhoria
etapa_atual: "QA · Análise da demanda"
modulo: navegacao
plano: "[[02 - Plano de teste]]"
execucao: ""
ambiente: dev
origem: conversa
projeto: financas-pessoais
pai: ""
data_inicio: 2026-10-02
data_fim: ""
responsavel: ""
pontos_alocados: 5
---

# FIN-MEL-0006 — Navegação estilo aplicativo

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
> **Projeto:** `financas-pessoais`


> [!info] Status atual
> **Próximo passo:** revisar e aprovar o escopo, plano e casos de teste.

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

Lançamentos e acompanhamento/histórico ficam concentrados em uma única página contínua. No mobile, isso torna a tela extensa, dificulta encontrar cada área e limita a evolução da interface.

---

## Objetivo

Permitir que o usuário navegue entre as principais áreas do sistema como em um aplicativo mobile, com acesso direto a Lançamentos e Histórico/Acompanhamento.

### Entrega desta capacidade

Será entregue uma navegação inferior responsiva, com áreas separadas e estrutura extensível para futuras áreas.

---

## Decisões de produto

- A navegação inferior será o principal acesso entre as áreas no mobile.
- Lançamentos e Histórico/Acompanhamento serão visões distintas.
- A seleção da navegação exibirá somente a área correspondente.
- A mudança não altera regras de negócio nem persistência.

---

## Escopo

- Criar a barra de navegação inferior no mobile.
- Separar a área de cadastro de lançamentos da área de acompanhamento/histórico.
- Adaptar a interface para a nova navegação.
- Manter uma estrutura preparada para novas áreas.

---

## Fora de escopo

- Menu lateral.
- Novas funcionalidades além das áreas existentes.
- Alterações no backend, banco ou regras de negócio.

---

## Critérios de aceite

- C1. No mobile, o usuário acessa as áreas principais pela barra inferior. ^c1
- C2. A barra apresenta opções distintas para Lançamentos e Histórico/Acompanhamento. ^c2
- C3. Ao selecionar uma opção, somente a área correspondente é exibida. ^c3
- C4. A opção ativa fica visualmente identificada e é acessível por teclado/leitor de tela. ^c4
- C5. A navegação não perde dados já salvos nem altera os fluxos atuais de criação, edição e exclusão. ^c5
- C6. A interface permanece utilizável em mobile e desktop. ^c6
- C7. A estrutura permite adicionar novas áreas sem reescrever a navegação existente. ^c7

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [ ] Plano e casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Nenhuma. Se houver pendência, manter `status: analise`.
