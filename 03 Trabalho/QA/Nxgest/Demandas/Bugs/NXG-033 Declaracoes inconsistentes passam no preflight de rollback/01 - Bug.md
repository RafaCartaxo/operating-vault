---
prioridade: alta
status: validacao
tipo: bug
etapa_atual: "QA · Validação"
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

# NXG-033 — Bug Declaracoes inconsistentes passam no preflight de rollback

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Fix DEV:** pendente de encaminhamento pela Coordenação.
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-033 Declaracoes inconsistentes passam no preflight de rollback/03 - Validação dev|Validação QA]]

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

Fixture com conteúdo de schema incompatível, config divergente e previous_sha arbitrário foi aceita com schema_status=compatible, hashes correspondentes e imagem dublada; exit 0. O preflight valida sintaxe/hashes e declarações humanas, não a veracidade nem vínculo SHA-imagem; a documentação reconhece revisão externa necessária.

---

## Passo a passo para reproduzir

**Dado** fixtures e dublês isolados do caso pai CT-009 / C4  
**Quando** a condição descrita na evidência é aplicada  
**Então** observa-se o comportamento acima, sem recursos reais.

---

## Evidências

QA independente: `.maestro/nxgest-team/qa/NXG-MEL-0009-VALIDACAO/preflight-declaracao-fixture.log`. Relatório pai: `.maestro/nxgest-team/NXG-MEL-0009-PARECER-QA.md`. Referência: CT-009 / C4.

---

## Resultado esperado

Definir e tornar verificável o gate de evidência externa e revisão para compatibilidade, configuração/mounts e associação SHA-imagem; condição ausente ou contraditória deve parar ou permanecer explicitamente bloqueada sem afirmar comprovação. Não presumir que uma declaração ou hash prove compatibilidade real.

---

## Critérios de aceite

- C1. A evidência de compatibilidade e configuração tem formato verificável, identifica responsável e objeto revisado; ausência, estado incompatível ou contradição explícita bloqueiam a promoção ou mantêm no-go. ^c1
- C2. O vínculo entre SHA anterior e imagem preservada é verificável por evidência sintética associada; ausente, divergente ou não verificável impede declarar o rollback pronto. ^c2
- C3. O retorno distingue health, integridade e SHA efetivamente demonstrados de declarações; dados/health inválidos ou SHA não comprovado impedem declarar sucesso. ^c3
- C4. Nenhum teste usa CLI/daemon Docker, rede, serviços, dados reais ou segredos; atestação humana e fixtures não são prova de compatibilidade real. ^c4

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

8/8 CTs passaram em escopo sintético; gate final aguarda sincronização dos Fixes DEV; [[03 - Validação dev]] e [[06 - Evidências QA]]. Não equivale a go de produção.
