---
prioridade: media
status: backlog
tipo: bug
etapa_atual: "QA · Triagem"
modulo: ""
plano: ""
execucao: ""
ambiente: dev
origem: observado
projeto: ""
pai: ""
data_inicio: ""
data_fim: ""
responsavel: ""
pontos_alocados: ""
---

# <PROJ>-NNN — Bug <Título curto>

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Fix DEV:** [[03 Trabalho/DEV/<projeto>/Fixes/<ID>/00 README|Fix DEV]]  
> **Validação QA:** [[03 Trabalho/QA/<projeto>/Demandas/Bugs/<ID>/03 - Validação dev|Validação QA]]

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

Durante a validação foi identificado que ...

---

## Passo a passo para reproduzir

**Dado** ...  
**E** ...  
**Quando** ...  
**Então** ...

---

## Evidências

- Screenshot, log ou link reproduzível.

---

## Resultado esperado

-

---

## Critérios de aceite

- C1. O comportamento incorreto deixa de ocorrer após a correção. ^c1
- C2. O fluxo relacionado permanece íntegro após a correção. ^c2

> Critérios são definições reutilizáveis e podem ser cobertos por vários CTs. O resultado é acompanhado na validação, não marcando esta lista.

---

## Checklist de entrega ao DEV

- [ ] Sintoma, ambiente e passos de reprodução estão claros.
- [ ] Resultado esperado está definido.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Contexto da execução

- Ambiente: `dev` · `hml` · `prod`
- Versão/build:
