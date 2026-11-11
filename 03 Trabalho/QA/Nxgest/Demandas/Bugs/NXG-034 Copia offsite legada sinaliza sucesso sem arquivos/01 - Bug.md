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

# NXG-034 — Bug Copia offsite legada sinaliza sucesso sem arquivos

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]  
> **Bug:** [[01 - Bug]]  
> **Casos de teste:** [[02 - Casos de teste]]  
> **Preparação Qase:** [[04 - Preparação Qase]]  
> **Fix DEV:** pendente de encaminhamento pela Coordenação.
> **Validação QA:** [[03 Trabalho/QA/Nxgest/Demandas/Bugs/NXG-034 Copia offsite legada sinaliza sucesso sem arquivos/03 - Validação dev|Validação QA]]

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

O guia 08-SETUP-NOVA-MAQUINA §7.1 ainda orienta pull-backup.sh e scp para arquivos antigos. Em fixture com ssh dublado bem-sucedido e scp dublado falho, o script retornou zero e imprimiu sucesso com diretório vazio. Novo formato é conjunto por diretório, conforme 09-BACKUP-ROLLBACK §5, portanto a cópia antiga não comprova off-site.

---

## Passo a passo para reproduzir

**Dado** fixtures e dublês isolados do caso pai CT-012 / C7  
**Quando** a condição descrita na evidência é aplicada  
**Então** observa-se o comportamento acima, sem recursos reais.

---

## Evidências

QA independente: `.maestro/nxgest-team/qa/NXG-MEL-0009-VALIDACAO/pull-fixture.log`. Relatório pai: `.maestro/nxgest-team/NXG-MEL-0009-PARECER-QA.md`. Referência: CT-012 / C7.

---

## Resultado esperado

Sincronizar instruções e comportamento para impedir declaração de sucesso sem conjunto válido; estabelecer ou explicitar procedimento seguro de transporte e verificação do conjunto completo, sem qualquer conexão real.

---

## Critérios de aceite

- C1. A cópia externa falha com saída não zero ou estado inequívoco de falha quando transferência falha, não encontra conjunto ou recebe conjunto incompleto/corrompido; nunca anuncia sucesso nesses casos. ^c1
- C2. O caminho positivo transporta o conjunto completo associado para destino sintético e confere identidade e integridade sem sobrescrever ou excluir cópia anterior. ^c2
- C3. A documentação de nova máquina não orienta o formato legado como se comprovasse cópia do conjunto novo; procedimento pendente é identificado claramente. ^c3
- C4. Testes bloqueiam previamente Docker/curl/ssh/scp reais e não tocam rede, segredos, máquinas ou dados reais. ^c4

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
