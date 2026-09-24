---
prioridade: media
status: concluido
tipo: melhoria
etapa_atual: "Concluído"
modulo: clientes
plano: ""
execucao: ""
ambiente: dev
origem: repo
pai: ""
data_inicio: ""
data_fim: ""
responsavel: ""
pontos_alocados: ""
---

# MEL-0003 — Expandir e recolher com chevron

> [!info]- Navegação QA/DEV
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Execução DEV:** [[05 Arquivo/Melhorias/MEL-0003/DEV/MEL-0003/00 README|Execução DEV]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`


> [!info] Status atual
> **Próximo passo:** nenhum — melhoria implementada, revisada e validada.

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> **Capacidade alocada:** preencher `pontos_alocados`.
> Exemplo: se houver 50 pontos disponíveis no ciclo, usar `pontos_alocados: 50`.
>
> ```dataviewjs
> const id = (dv.current().file.path.match(/MEL-\d+/) || [""])[0];
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

Os controles de expandir e recolher exibem o texto por extenso. Isso ocupa espaço e torna menos imediata a leitura do estado de cada seção.

---

## Objetivo

Usar um chevron para indicar visualmente se a seção está expandida ou recolhida, mantendo o comportamento atual de abrir e fechar.

### Entrega desta capacidade

Aplicar o chevron nos controles de expandir/recolher da tela de clientes, com estado visual coerente e acessível. O comportamento funcional das seções permanece inalterado.

---

## Decisões de produto

- O chevron deve apontar para a direita quando a seção estiver recolhida e para baixo quando estiver expandida.
- O controle continua clicável e deve manter nome acessível para leitores de tela.

---

## Escopo

- Substituição do texto visual do controle por um chevron.
- Estados expandido e recolhido claramente distinguíveis.

---

## Fora de escopo

- Alterações no conteúdo ou na ordem das seções.
- Mudanças no comportamento de persistência dos dados.

---

## Critérios de aceite

- C1. O controle exibe chevron à direita quando a seção está recolhida. ^c1
- C2. O controle exibe chevron para baixo quando a seção está expandida. ^c2
- C3. Clicar no controle continua expandindo e recolhendo a seção normalmente. ^c3
- C4. O controle mantém nome acessível e não perde sua função sem mouse. ^c4

---

## Checklist de entrega ao DEV

- [ ] Decisões e regras de negócio estão fechadas.
- [ ] Escopo e fora de escopo estão claros.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Nenhuma. Se houver pendência, manter `status: analise`.
