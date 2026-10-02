---
prioridade: media
status: concluido
tipo: melhoria
etapa_atual: "Concluído"
modulo: lancamentos
plano: "[[02 - Plano de teste]]"
execucao: "[[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/00 README|Execução DEV]]"
ambiente: dev
origem: conversa
projeto: financas-pessoais
pai: ""
data_inicio: 2026-10-02
data_fim: ""
responsavel: ""
pontos_alocados: 6
---

# FIN-MEL-0001 — Cadastro mobile de nova despesa

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/00 README|Execução DEV]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** preencher `projeto` no frontmatter antes de roteiar a melhoria.

> [!info] Status atual
> **Próximo passo:** nenhum. Melhoria concluída após aprovação de todos os CTs.

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> **Capacidade alocada:** 6 pontos.
> O esforço será distribuído entre o pacote QA e a execução DEV vinculada.
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

O backend de Finanças Pessoais já expõe o cadastro de lançamentos, mas ainda não existe uma interface simples para registrar uma despesa pelo celular ou navegador.

---

## Objetivo

Disponibilizar uma tela mobile-first para cadastrar uma despesa, com validação clara e integração com `POST /api/lancamentos`.

### Entrega desta capacidade

Entregar o formulário React + Vite + TypeScript, responsivo, com estados de validação, erro e sucesso, integrado ao contrato atual do backend Go.

---

## Decisões de produto

- O primeiro fluxo prioriza o lançamento rápido de uma despesa simples.
- O uso em celular é requisito desde o primeiro incremento.
- O backend Go existente é o contrato de integração desta entrega.

---

## Escopo

- Formulário de nova despesa.
- Campos compatíveis com o contrato atual da API: tipo, descrição, valor e data.
- Validação de campos obrigatórios e valor monetário.
- Estados de envio, sucesso e erro.
- Layout responsivo para celular e desktop.

---

## Fora de escopo

- Parcelamento e recorrência.
- Dashboard e relatórios.
- Autenticação.
- Publicação em produção e PWA completa.
- Exportação para o `financas-vault`.

---

## Critérios de aceite

- C1. O formulário abre e permanece utilizável em viewport móvel e desktop.
^c1
- C2. Campos obrigatórios e valor/data inválidos impedem o envio; o campo monetário aceita apenas números e separadores válidos, sempre exibe máscara em reais, e todos os erros são apresentados simultaneamente em ordem de formulário.
^c2
- C3. Um lançamento válido chama `POST /api/lancamentos` com o contrato documentado.
^c3
- C4. Erros da API são apresentados sem perder silenciosamente os dados preenchidos.
^c4
- C5. Após sucesso, o usuário recebe confirmação clara e o formulário fica pronto para um novo lançamento.
^c5
- C6. O fluxo possui testes básicos e documentação atualizada.
^c6

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Nenhuma. O contrato inicial considera tipo, descrição, valor e data; campos adicionais ficam fora desta melhoria.
