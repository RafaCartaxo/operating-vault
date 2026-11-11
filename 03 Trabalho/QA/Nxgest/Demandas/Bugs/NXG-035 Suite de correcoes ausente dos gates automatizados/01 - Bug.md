---
prioridade: alta
status: execucao
tipo: bug
etapa_atual: "DEV · Análise técnica"
modulo: infra
plano: ""
execucao: ""
ambiente: dev
origem: observado
projeto: nxgest
epico: ""
pai: "NXG-MEL-0009"
data_inicio: 2026-11-11
data_fim: ""
responsavel: "NX Gest · QA"
pontos_alocados: 3
---

# NXG-035 — Bug Suite de correcoes ausente dos gates automatizados

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]<br>
> **Bug:** [[01 - Bug]]<br>
> **Casos de teste:** [[02 - Casos de teste]]<br>
> **Preparação Qase:** [[04 - Preparação Qase]]<br>
> **Fix DEV:** aguardando encaminhamento pela Coordenação.
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-035 Suite de correcoes ausente dos gates automatizados/03 - Validação dev|Validação QA]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`<br>
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`<br>
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** preencher `projeto` no frontmatter antes de roteiar o bug.


---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> Capacidade de planejamento alocada: 3 pontos.
>
> Estimativa de planejamento; DEV poderá detalhar o esforço.

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

`scripts/corrections.check.mjs` contém os dois testes sintéticos de cópia e vínculo. CI e CD manual chamam `npm test`, `test:deploy` e `test:backup`; estes executam Vitest, `deploy-transition.check.mjs` e `backup-recovery.check.mjs`, respectivamente. O padrão Vitest instalado é `**/*.{test,spec}.?(c|m)[jt]s?(x)`, que não inclui `corrections.check.mjs`. Não há comando que execute o arquivo nos workflows. Assim o CI pode passar sem esses dois testes. Constatação estática local; nenhum workflow remoto foi executado.

---

## Passo a passo para reproduzir

**Dado** o package.json, vitest.config.ts e workflows atuais<br>
**Quando** se rastreiam os arquivos executados pelos comandos CI/CD<br>
**Então** `scripts/corrections.check.mjs` não aparece como entrada e não corresponde ao padrão de descoberta do Vitest.

---

## Evidências

Inspeção local de `package.json:34–35`, `.github/workflows/ci.yml:45–53`, `.github/workflows/cd.yml:60–65` e `node_modules/vitest/dist/config.js:10`. QA executou as duas verificações individualmente em isolamento e guardas (logs `qa/NXG-032-034-RETESTE/case-13.log` e `case-14.log`); sucesso manual não prova execução pelo CI.

---

## Resultado esperado

Ambos os gates executam os dois testes, bloqueiam na falha e impedem acesso a recursos reais. O runner é configurável ou falha fechado ao identificar requisito indisponível. A implementação e escolha técnica pertencem ao DEV após encaminhamento da Coordenação; não se executa GitHub Actions real nesta demanda.

---

## Critérios de aceite

- C1. Os dois testes de scripts/corrections.check.mjs são selecionados e executados nos gates CI e CD manual; a evidência distingue testes executados de selecionados ou ignorados. ^c1
- C2. Uma falha injetada separadamente em cada um dos dois testes produz falha no gate correspondente em CI e CD manual, bloqueando seus passos dependentes de promoção. ^c2
- C3. Antes de cada execução são verificadas guardas efetivas para Docker CLI/daemon, curl, SSH/SCP e subprocessos; chamadas reais, rede, dados e serviços reais são bloqueados, inclusive em falha ou ausência da guarda. ^c3
- C4. O runner não pressupõe caminhos da máquina pessoal, instalação de bwrap, namespace permitido ou versão Node do host: os requisitos são explícitos e sua indisponibilidade interrompe antes dos testes com erro claro. Compatibilidade real GitHub Actions só é alegada após execução autorizada e evidenciada. ^c4
- C5. Os gates existentes de teste, segurança, backup e deploy e o NO-GO operacional continuam íntegros; testes isolados não são apresentados como prova de CI real, proveniência, restore ou publicação. ^c5

---

## Checklist de entrega ao DEV

- [x] Sintoma, resultado esperado e limites claros.
- [x] Critérios observáveis e sete CTs vinculados.
- [x] Matriz, validação e Qase local preparados.
- [x] Capacidade de planejamento preenchida.
- [x] Integridade e sincronização verificadas antes do handoff.

---

## Contexto da execução

- Ambiente: análise estática local; nenhum workflow remoto ou teste executado nesta triagem.
- QA_READY_FOR_DEV após gate; Coordenação encaminha ao DEV.
- Sem commit/push/deploy, Docker CLI/daemon, curl/SSH/SCP real, rede, dados ou recursos reais; testes futuros apenas com guardas e fixtures.
- Não reabrir NXG-031 ou épico. MEL-0009 permanece QA_REJECTED/NO-GO; desvio histórico Docker CLI não se torna conforme retroativamente.

## Compatibilidade do runner e histórico

2026-11-11: `nxg032-034/run-isolated.sh` aponta para diretório pessoal `/home/rafacartaxo/...`, guardas fora do repositório e Node no `.nvm`; requer `bwrap --unshare-user --unshare-net`. Por inspeção essas dependências não são portáveis para CI sem adaptação/configuração; disponibilidade real de paths, bwrap e namespaces no GitHub não foi verificada. CI declara setup-node 20; CD manual não declara setup-node no job validado. Confirmar requisitos antes de executar; ausência de prova não é prova de incompatibilidade real do serviço.

QA_READY_FOR_DEV — Coordenação encaminha o pacote; nenhuma correção ou teste de aceitação foi executado.
