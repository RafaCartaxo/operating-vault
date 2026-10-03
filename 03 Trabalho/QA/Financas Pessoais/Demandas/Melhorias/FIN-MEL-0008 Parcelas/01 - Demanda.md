---
prioridade: media
status: analise
tipo: melhoria
etapa_atual: "QA · Plano de teste"
modulo: lancamentos
plano: "[[02 - Plano de teste]]"
execucao: ""
ambiente: dev
origem: conversa
projeto: financas-pessoais
pai: ""
data_inicio: 2026-10-02
data_fim: ""
responsavel: ""
pontos_alocados: 8
---

# FIN-MEL-0008 — Parcelas

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

O sistema já possui campos de parcela no modelo, mas o usuário ainda não consegue registrar uma compra parcelada nem consultar suas parcelas nos meses correspondentes.

---

## Objetivo

Permitir registrar um lançamento parcelado e visualizar cada parcela no mês correto, mantendo os valores e a identificação da série consistentes.

### Entrega desta capacidade

Será entregue o primeiro fluxo de parcelamento, com geração dos lançamentos da série, distribuição monetária em centavos e identificação de parcela atual/total.

---

## Decisões de produto

- O usuário informa o valor total da compra, a quantidade de parcelas e a data da primeira parcela.
- O valor total será distribuído em centavos; eventual diferença de arredondamento ficará na última parcela.
- As parcelas serão geradas mensalmente, preservando o dia quando possível e ajustando para o último dia do mês quando necessário.
- Cada parcela será um lançamento consultável no mês correspondente.

---

## Escopo

- Campos de parcelamento no formulário.
- Validação de quantidade e valor total.
- Geração e persistência da série de parcelas.
- Exibição de parcela atual/total no histórico.
- Consulta mensal das parcelas geradas.

---

## Fora de escopo

- Recorrências automáticas.
- Juros, taxas ou correção monetária.
- Faturas de cartão.
- Alteração em lote após a criação da série.
- Sincronização offline.

---

## Critérios de aceite

- C1. O formulário permite informar que o lançamento é parcelado e a quantidade de parcelas. ^c1
- C2. O sistema rejeita quantidade inválida e valores que não podem gerar parcelas. ^c2
- C3. O valor total é distribuído em centavos e a soma das parcelas corresponde ao total. ^c3
- C4. Cada parcela recebe a data mensal correta e aparece no mês correspondente. ^c4
- C5. Cada parcela identifica sua posição e o total da série. ^c5
- C6. A criação da série é atômica: falha não deixa parcelas incompletas. ^c6
- C7. Lançamentos não parcelados continuam funcionando sem alteração de comportamento. ^c7
- C8. Editar ou excluir uma parcela, mediante confirmação, altera ou remove toda a série. ^c8

---

## Checklist de entrega ao DEV

- [ ] Decisões e regras de negócio estão fechadas.
- [ ] Escopo e fora de escopo estão claros.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Edição ou exclusão iniciada em uma parcela afeta toda a série, com confirmação explícita.
- Datas em meses menores são ajustadas para o último dia do mês.
- Decisões de produto aprovadas; seguir para plano e casos de teste.
