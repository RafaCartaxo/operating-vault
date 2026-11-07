---
prioridade: media
status: "concluido"
tipo: bug
etapa_atual: "Concluído"
modulo: "infraestrutura"
plano: ""
execucao: "[[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/00 README]]"
ambiente: dev
origem: observado
projeto: "nxgest"
epico: "NXG-EPIC-0001"
pai: ""
data_inicio: "2026-11-07"
data_fim: "2026-11-07"
responsavel: "NX Gest · QA e Coordenação"
pontos_alocados: 8
---

# NXG-029 — Bug Staging carrega valores com espacos

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Fix DEV:** [[05 Arquivo/Nxgest/Bugs/NXG-029/DEV/NXG-029/00 README|Execução DEV]]  
> **Validação QA:** [[05 Arquivo/Nxgest/Bugs/NXG-029/QA/NXG-029 Staging carrega valores com espacos/03 - Validação dev|Validação QA]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`<br>
> **Projeto:** `nxgest`.


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

scripts/deploy-staging.sh gera MAIL_FROM_NAME=NX Gest e usa source sob set -e; o shell interpreta Gest como comando.

---

## Passo a passo para reproduzir

Revisão estática do script e reprodução somente com valores sintéticos/dublês; nunca executar contra infraestrutura real.

**Dado** o script atual
**Quando** percorro a entrada descrita no comportamento observado
**Então** identifico a falha descrita; a correção será comprovada pelos CTs vinculados.

---

## Evidências

Inspeção dos scripts em HEAD 8454392 com working tree preservado; diagnóstico de 2026-11-07. Reprodução controlada a registrar na execução DEV.

---

## Resultado esperado

- A configuração recém-gerada de staging aceita MAIL_FROM_NAME com espaço sem tentar executar parte do valor como comando.
- A correção mantém geração de segredos aleatórios, permissões restritas, e-mail console e arquivo existente sem sobrescrever seus valores.

---

## Critérios de aceite

- C1. A configuração recém-gerada de staging aceita MAIL_FROM_NAME com espaço sem tentar executar parte do valor como comando. ^c1
- C2. A correção mantém geração de segredos aleatórios, permissões restritas, e-mail console e arquivo existente sem sobrescrever seus valores. ^c2

---

## Checklist de entrega ao DEV

- [x] Sintoma, ambiente e passos de reprodução estão claros.
- [x] Resultado esperado está definido.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Casos de teste estão vinculados.
- [x] `pontos_alocados` foi preenchido.

---

## Contexto da execução

Ambiente: dev isolado. Base: 8454392 + trabalho local inventariado. Sem deploy ou acesso à VPS.

