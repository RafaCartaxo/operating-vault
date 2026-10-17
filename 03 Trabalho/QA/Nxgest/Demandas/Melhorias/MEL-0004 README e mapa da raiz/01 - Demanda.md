---
prioridade: media
status: concluido
tipo: melhoria
etapa_atual: "Concluído"
modulo: organizacao-repositorio
plano: "[[03 Trabalho/QA/Nxgest/Demandas/Planos/NXG-028 Governanca da reorganizacao do NX Gest|NXG-028]]"
execucao: "[[03 Trabalho/DEV/Nxgest/Execuções/MEL-0004 README e mapa da raiz/00 README|Execução MEL-0004]]"
ambiente: dev
origem: repo
projeto: nxgest
epico: NXG-EPIC-0001
pai: ""
data_inicio: ""
data_fim: ""
responsavel: ""
pontos_alocados: 0
---

# MEL-0004 — README e mapa da raiz do NX Gest

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Nxgest/Execuções/MEL-0004 README e mapa da raiz/00 README|Execução MEL-0004]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** `nxgest`


> [!info] Status atual
> **Resultado:** QA aprovado com ressalva documental sobre links preexistentes fora do escopo.

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

O NX Gest funciona, mas o mapa visual da raiz não representa toda a estrutura mantida pelo projeto. Isso reduz a clareza para quem clona o repositório ou consulta a documentação de entrada.

---

## Objetivo

O README raiz deve apresentar uma visão completa e coerente da estrutura oficial do repositório, incluindo `.github/` e `.opencode/`, sem sugerir movimentações que não foram aprovadas.

### Entrega desta capacidade

Atualizar exclusivamente a seção de estrutura do README raiz e suas referências diretamente afetadas. A organização física de `infra/`, ambientes, agentes e diretório local será tratada em demandas filhas próprias.

---

## Decisões de produto

- `nxgest` é o nome canônico do produto e do repositório.
- A raiz mantém arquivos exigidos por ferramentas e pontos de entrada do projeto.
- Este lote é documental e não altera código, infraestrutura ou nomes de arquivos.

---

## Escopo

- Revisar o mapa de diretórios do README raiz.
- Incluir `.github/`, `.opencode/`, `docs/`, `scripts/`, `src/` e `frontend/` quando aplicável.
- Garantir que o texto não contradiga o plano NXG-028.

---

## Fora de escopo

- Mover Dockerfile, Caddyfile ou compose files.
- Mover arquivos `.env` ou alterar carregamento de ambientes.
- Criar ou reorganizar agentes.
- Renomear a pasta local `nxgestao`.
- Alterar código ou infraestrutura do NX Gest.

---

## Critérios de aceite

- C1. O README raiz representa a estrutura real e oficial do repositório, incluindo `.github/` e `.opencode/`, sem listar diretórios inexistentes. ^c1
- C2. Todos os links e caminhos documentais afetados continuam resolvendo após a alteração. ^c2
- C3. A atualização não altera código, configuração de ambiente, Docker, agentes ou infraestrutura. ^c3
- C4. A nomenclatura nova usa `nxgest`; ocorrências de `nxgestao` permanecem apenas quando forem compatibilidade de infraestrutura ou histórico. ^c4

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- QA executado e aprovado com ressalva; lote concluído.
