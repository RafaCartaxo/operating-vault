---
prioridade: media
status: "concluido"
tipo: melhoria
etapa_atual: "Concluído"
modulo: "infraestrutura"
plano: ""
execucao: "[[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/00 README]]"
ambiente: dev
origem: repo
projeto: "nxgest"
epico: "NXG-EPIC-0001"
pai: ""
data_inicio: "2026-11-07"
data_fim: "2026-11-07"
responsavel: "NX Gest · QA e Coordenação"
pontos_alocados: 20
---

# NXG-MEL-0008 — Consolidacao de ambientes e portabilidade

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/00 README|Execução DEV]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** `nxgest`.


> [!info] Status atual
> **Próximo passo:** QA validou; pacote concluído e arquivado. Épico aguarda decisão do usuário no parecer final.

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> **Capacidade alocada:** capacidade reservada no frontmatter.
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

A reorganização de infra/agentes está localmente implementada, mas há configuração duplicada, comandos obsoletos e ausência de prova integrada em checkout limpo. Há trabalho de clientes, identidade e Qase a preservar separadamente.

---

## Objetivo

Concluir a consolidação e demonstrar setup reproduzível, preservando o trabalho local e entregando parecer final sem encerrar o épico.

### Entrega desta capacidade
Pacote integrado de ambiente, documentação, preservação e validação; estimativa de coordenação registrada em pontos, sem promessa de duração.

---

## Decisões de produto

- Um .env.example canônico na raiz; desenvolvimento funcional e diferenças nos guias existentes.
- infra/ simples com seus cinco arquivos; agents/ neutro; sem refatoração do produto.
- Correções independentes NXG-029 e NXG-030 antes do teste integrado.
- Estado do épico continua execucao até decisão do usuário no parecer final.

---

## Escopo

- Consolidar modelos, scripts consumidores, README, setup e runbook.
- Corrigir referências ativas e links dos planos 088/089, preservando contexto das demandas de origem.
- Classificar e preservar todos os diffs, organizar commits locais e validar checkout limpo.
- Organizar nome local e referências de ferramentas sem perder instalação/dados.
- Sincronizar registros QA/DEV e governança com evidências.

---

## Fora de escopo

- Push, deploy, acesso ou alterações à VPS, segredos e recursos reais.
- Reescrita de histórico, descarte de trabalho e envio a Qase externo.
- Encerramento do épico antes do parecer ao usuário.
- Comando doctor é opcional e não bloqueia esta entrega.

---

## Critérios de aceite

- C1. O único modelo versionado .env.example cobre as variáveis suportadas, com defaults de desenvolvimento e obrigações de staging/prod documentadas nos guias existentes. Nenhum segredo real é versionado. ^c1
- C2. README e guia de nova máquina usam caminhos reais e instalação pelo lockfile; infra/ aparece no mapa e não há comandos ativos dependentes da antiga localização dos arquivos. ^c2
- C3. O plano de validação usa banco, portas, nomes de containers e volumes próprios, sem alterar recursos existentes. ^c3
- C4. Testes, build, check-dist e auditorias de documentação, links, UI, estilos e módulos passam; avisos históricos são classificados com encaminhamento. ^c4
- C5. Um checkout limpo de revisão identificada instala dependências, inicializa banco vazio e permite autenticação e um fluxo básico de clientes; reiniciar preserva os dados de teste. ^c5
- C6. Todo trabalho local prévio é preservado e classificado por assunto, incluindo arquivos novos; commits locais são coerentes, sem push/deploy e sem incluir segredos. ^c6
- C7. A pasta local final nxgest e as referências ativas de ferramentas ficam coerentes; caminhos históricos de infraestrutura real permanecem compatíveis. ^c7
- C8. NXG-028, épico e boards refletem a execução e suas evidências; o épico permanece em execução aguardando parecer final ao usuário. ^c8

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

Nenhuma de produto. Decisões técnicas e preservação serão registradas pelo DEV; lacunas descobertas voltam para QA sem ampliar silenciosamente o escopo.

