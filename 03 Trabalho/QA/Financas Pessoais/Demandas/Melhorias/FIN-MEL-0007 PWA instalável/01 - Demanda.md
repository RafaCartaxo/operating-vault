---
prioridade: media
status: concluido
tipo: melhoria
etapa_atual: "Concluído"
modulo: pwa
plano: ""
execucao: ""
ambiente: dev
origem: conversa
projeto: financas-pessoais
pai: ""
data_inicio: 2026-10-02
data_fim: ""
responsavel: ""
pontos_alocados: 3
---

# FIN-MEL-0007 — PWA instalável

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** implementação registrada diretamente no projeto; sem execução separada.

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

O frontend funciona no navegador, mas ainda não possui manifest, ícones, service worker ou metadados para ser instalado como aplicativo no celular.

---

## Objetivo

Permitir instalar o Finanças Pessoais na tela inicial do Android e iPhone, abrindo em modo aplicativo e mantendo o app shell disponível offline.

### Entrega desta capacidade

Manifest PWA, ícones, registro de service worker, cache dos arquivos estáticos e metadados mobile.

---

## Decisões de produto

- O cache offline cobre somente o app shell e arquivos estáticos.
- Consultas e gravações financeiras continuam dependendo da API/rede.
- A instalação exige contexto seguro em produção ou localhost no desenvolvimento.

---

## Escopo

- Manifest, ícones Android/iOS, service worker e registro no frontend.
- Metadados de instalação e tema.
- Documentação do fluxo offline.

---

## Fora de escopo

- Sincronização offline de lançamentos.
- Banco local ou fila de operações.
- Push notifications.

---

## Critérios de aceite

- C1. O manifest define nome, escopo, modo standalone, tema e start_url. ^c1
- C2. Os ícones 192px, 512px e Apple Touch Icon são publicados no build. ^c2
- C3. O service worker é registrado em produção e cacheia o app shell. ^c3
- C4. As chamadas /api não são cacheadas nem simulam dados offline. ^c4
- C5. O build disponibiliza todos os artefatos PWA sem erro. ^c5

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Nenhuma. Se houver pendência, manter `status: analise`.
