---
prioridade: alta
status: execucao
tipo: bug
etapa_atual: "DEV · Análise técnica"
modulo: infra
plano: ""
execucao: "[[03 Trabalho/DEV/Nxgest/Fixes/NXG-031/00 README]]"
ambiente: dev
origem: observado
projeto: nxgest
epico: ""
pai: ""
data_inicio: 2026-11-10
data_fim: ""
responsavel: QA e Coordenação
pontos_alocados: 13
---

# NXG-031 — Bug Transicao segura do deploy e continuidade operacional

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Fix DEV:** [[03 Trabalho/DEV/Nxgest/Fixes/NXG-031/00 README|Fix DEV]]  
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-031 Transicao segura do deploy e continuidade operacional/03 - Validação dev|Validação QA]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** preencher `projeto` no frontmatter antes de roteiar o bug.


---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> Preencha apenas `pontos_alocados` no frontmatter com a capacidade reservada para este bug.
> 
> Exemplo: se houver 50 pontos disponíveis no ciclo, use `pontos_alocados: 50`.

```dataviewjs
const projeto = String(dv.current().projeto || "").toUpperCase();
const id = (dv.current().file.path.match(new RegExp(`${projeto || "[A-Z]{2,8}"}-\\d+`)) || [""])[0];
const paginas = dv.pages().where(p => id && p.file.path.includes(id) && typeof p.pontos === "number");
const lista = paginas.sort(p => p.file.name);
const necessario = lista.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
const alocado = Number(dv.current().pontos_alocados || 0);
const diferenca = alocado - necessario;
if (lista.length > 0) {
  dv.table(["Etapa/artefato", "Pontos"], lista.map(p => [p.file.link, p.pontos]));
} else {
  dv.paragraph("Nenhum artefato com pontos registrado ainda.");
}
dv.paragraph(`**Esforço necessário:** ${necessario} · **Capacidade alocada:** ${alocado} · **${diferenca >= 0 ? "Saldo" : "Déficit"}:** ${Math.abs(diferenca)} pontos`);
```

---

## Comportamento observado

O CI chama o deploy-staging.sh instalado antes do fetch. O script de origin/main mantém docker-compose.staging.yml na raiz; o alvo c7b65c8 move para infra/. Reprodução com dublês falha no caminho antigo. Onboarding também contém restauração em / com home original e chmod indiscriminado.

---

## Passo a passo para reproduzir

**Dado** script legado em 9bff3f7 e alvo c7b65c8  
**E** git/docker interceptados, sem infraestrutura real  
**Quando** o trecho antigo atualiza a árvore e executa Compose  
**Então** busca docker-compose.staging.yml inexistente na raiz (exit 46 do dublê).

---

## Evidências

Relatório local: `/home/rafacartaxo/Documentos/Desenvolvimento/.maestro/nxgest-team/REVISAO-PUBLICACAO-2026-11-10.md`. Fontes: ci.yml:227, deploy-staging.sh, setup nova máquina §5.2, runbook produção.

---

## Resultado esperado

Atualização repetível e verificável sem depender de script antigo carregado, com preservação de env/trabalho local e documentação reproduzível. Fora de escopo: SSH/VPS, painel Cloudflare, segredos reais, push, deploy e commits nesta rodada. Épico anterior permanece concluído; esta é correção pré-publicação separada.

---

## Critérios de aceite

- C1. O pipeline carrega o script e os helpers do SHA alvo antes de qualquer operação de staging; a primeira transição do layout antigo para infra funciona. ^c1
- C2. Fetch/ref inválido ou trabalho remoto não preservável interrompe antes de checkout destrutivo/build, sem descartar alterações nem divulgar envs. ^c2
- C3. Env e dados existentes são preservados; valores com espaços são lidos como dados; repetição e entrada manual não executam código antigo após atualizar. ^c3
- C4. Produção mantém backup obrigatório, SHA validado, bloqueio após CI/staging falho e caminhos Compose/Caddy corretos; avaliar concorrência no checkout compartilhado. ^c4
- C5. Onboarding separa dev de operação e o transporte usa home de destino e permissões adequadas, comprovado com fixtures; inventário Cloudflare indica o que está documentado e o que requer confirmação real. ^c5

---

## Checklist de entrega ao DEV

- [x] Sintoma, ambiente e passos de reprodução estão claros.
- [x] Resultado esperado está definido.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Contexto da execução

- Ambiente: dev isolado, dublês e fixtures sintéticas.
- Base: c7b65c8; remote base de referência 9bff3f7.
- Handoff: QA_READY_FOR_DEV; implementação autorizada pelo pedido direto de correção. Sem commit/push/deploy.
- 2026-11-10: critérios e CTs preparados; DEV recebe execução, QA mantém validação independente.
