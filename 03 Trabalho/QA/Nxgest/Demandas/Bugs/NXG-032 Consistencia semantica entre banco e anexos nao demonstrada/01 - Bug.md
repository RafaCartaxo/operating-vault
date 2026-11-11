---
prioridade: alta
status: concluido
tipo: bug
etapa_atual: "Concluído"
modulo: infra
plano: ""
execucao: ""
ambiente: dev
origem: observado
projeto: nxgest
epico: ""
pai: "NXG-MEL-0009"
data_inicio: 2026-11-11
data_fim: 2026-11-11
responsavel: "NX Gest · QA"
pontos_alocados: 3
---

# NXG-032 — Bug Consistencia semantica entre banco e anexos nao demonstrada

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Fix DEV:** pendente de encaminhamento pela Coordenação.
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-032 Consistencia semantica entre banco e anexos nao demonstrada/03 - Validação dev|Validação QA]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** nxgest.


---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> Capacidade de planejamento: 3 pontos; a execução poderá estimar o esforço.
> 
> Estimativa não equivale a trabalho executado.

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

Um dump sintético com referência a arquivo ausente e tar contendo outro anexo passou na verificação de hashes e estrutura. O teste existente restaura cada fixture separadamente, sem caso negativo de relacionamento; não demonstra consistência cruzada. A ferramenta verify-backup declara integridade de hashes, não declara verificar semântica.

---

## Passo a passo para reproduzir

**Dado** fixtures e dublês isolados do caso pai CT-005 / C3  
**Quando** a condição descrita na evidência é aplicada  
**Então** observa-se o comportamento acima, sem recursos reais.

---

## Evidências

QA independente: `.maestro/nxgest-team/qa/NXG-MEL-0009-VALIDACAO/consistencia-fixture.log`. Relatório pai: `.maestro/nxgest-team/NXG-MEL-0009-PARECER-QA.md`. Referência: CT-005 / C3.

---

## Resultado esperado

Produzir e validar ensaio sintético que confronte referências de banco e anexos, incluindo caso divergente que bloqueie alegação de conjunto semanticamente consistente. Não extrapolar para PostgreSQL real.

---

## Critérios de aceite

- C1. O ensaio sintético demonstra correspondência entre referências de anexos restauradas do banco e arquivos restaurados, identificando referências ausentes e recusando declaração de consistência. ^c1
- C2. Ausência legítima de referências/anexos é distinguida de erro; a evidência identifica o conjunto e não afirma consistência temporal ou restore PostgreSQL real. ^c2
- C3. Falhas de escrita/cópia, interrupção ou destino cheio impedem sucesso e preservam o último conjunto válido. ^c3
- C4. Nenhuma execução toca dados, Docker CLI/daemon, rede ou serviços reais; NXG-031 e fixtures anteriores são preservados. ^c4

---

## Checklist de entrega ao DEV

- [x] Sintoma, ambiente, passos e resultado esperado definidos.
- [x] Critérios observáveis e casos de teste vinculados.
- [x] Cobertura, validação e evidências reservadas.
- [x] Pontos de planejamento e limites de isolamento registrados.
- [x] Gate de integridade conferido; Coordenação fará o encaminhamento.

---

## Contexto da execução

- Ambiente: Linux local, fixtures e dublês exclusivamente; sem Docker daemon, SSH/VPS ou segredos.
- Versão: produto HEAD c7b65c8 + working tree MEL-0009.
- Próxima ação: Coordenação analisar e encaminhar DEV; QA não faz despacho. Não equivale a aprovação de teste de correção.

## Histórico de preparação

2026-11-11: critérios e CTs detalhados; QA_READY_FOR_DEV após gate de integridade. Coordenação decide encaminhamento; nenhum CT de correção foi executado.

## Reteste QA — 2026-11-11

8/8 CTs passaram em escopo sintético; gate final posteriormente concluído; [[03 - Validação dev]] e [[06 - Evidências QA]]. Não equivale a go de produção.

## Gate final QA — 2026-11-11

**QA_APPROVED com ressalvas**, exclusivamente para as correções verificadas em fixtures/dublês: 8/8 CTs aprovados. Registros DEV sincronizados conferidos; ver [[03 - Validação dev]] e [[06 - Evidências QA]]. Não demonstra recuperação, proveniência ou consistência reais; MEL-0009 permanece QA_REJECTED/NO-GO, com CT-011 bloqueado e NXG-035 pendente. Sem testes adicionais nesta decisão.
