---
prioridade: alta
status: analise
tipo: bug
etapa_atual: "QA · Análise da demanda"
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

- C1. Produzir e validar ensaio sintético que confronte referências de banco e anexos, incluindo caso divergente que bloqueie alegação de conjunto semanticamente consistente. Não extrapolar para PostgreSQL real. ^c1
- C2. Não executar ou alegar teste em infraestrutura real; preservar NXG-031 e os dados de teste anteriores. ^c2

---

## Checklist de entrega ao DEV

- [ ] Sintoma, ambiente e passos de reprodução estão claros.
- [ ] Resultado esperado está definido.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Contexto da execução

- Ambiente: Linux local, fixtures e dublês exclusivamente; sem Docker daemon, SSH/VPS ou segredos.
- Versão: produto HEAD c7b65c8 + working tree MEL-0009.
- Próxima ação: Coordenação analisar e encaminhar DEV; QA não faz despacho. Não equivale a aprovação de teste de correção.
