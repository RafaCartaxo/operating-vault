---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: bug
projeto: nxgest
modulo: infra
qase_projeto: nxgest
qase_suite_id: ""
casos_origem: ""
validacao_origem: ""
---
# Preparação Qase — NXG-032

> **Posição no pacote:** melhoria → `05 - Preparação Qase.md`; bug → `04 - Preparação Qase.md`. O conteúdo deste modelo é o mesmo nos dois casos.

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Casos de teste (bug):** [[02 - Casos de teste]]  
> **Validação (bug):** [[03 - Validação dev]]  

Esta nota transforma os CTs refinados do vault em casos da Qase. Não crie CT novo aqui: apenas traduza o caso existente para os campos da API.

## Configuração

- **Projeto Qase:** não configurado
- **Suite Qase:** não configurada
- **Origem:** nota de casos de teste do próprio card (`02` para bug, `03` para melhoria)

## Mapeamento dos campos

| Vault | Qase | Regra |
|---|---|---|
| Título do CT | `title` | manter o título humano do cenário |
| Descrição | `description` | resumir o objetivo do CT |
| Pré-condições | `preconditions` | copiar sem misturar com os passos |
| Dado/Quando/Então | `steps` | separar cada ação do resultado esperado |
| Pós-condição | `postconditions` | registrar somente o estado após o teste |
| Tipo, camada, automação | campos Qase | usar os valores normalizados abaixo |

Valores normalizados: `funcional`/`regressão`; camada `E2E`/`API`/`unit`; automação `manual`/`automatizado`/`ambos`.

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: usar o ID da demanda e o módulo (`<PROJ>-MEL-NNNN`, `cliente`); não criar uma tag para cada CT, pois o título e o ID do caso já fazem essa identificação.


## Casos preparados

### CT-B01 — Referência com anexo correspondente

- **Origem:** [[02 - Casos de teste#^ct-b01|CT-B01]].
- **Pré-condições:** Banco e tar sintéticos com ID de conjunto igual e referência para arquivo existente.
- **Ação:** executar ensaio em destino exclusivo.
- **Resultado:** comparação de referências e conteúdo passa e evidencia identificador do conjunto.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B02 — Referência sem anexo

- **Origem:** [[02 - Casos de teste#^ct-b02|CT-B02]].
- **Pré-condições:** Banco sintético referencia arquivo que não existe no tar, com hashes individuais válidos.
- **Ação:** comparar referências restauradas.
- **Resultado:** o ensaio identifica a referência ausente e recusa resultado consistente.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B03 — Nenhuma referência legítima versus erro

- **Origem:** [[02 - Casos de teste#^ct-b03|CT-B03]].
- **Pré-condições:** Uma fixture demonstra lista de referências vazia e anexos vazios; outra simula falha de leitura.
- **Ação:** validar ambas as condições.
- **Resultado:** zero legítimo é identificado como tal e erro não é tratado como vazio.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B04 — Falha de escrita ou cópia

- **Origem:** [[02 - Casos de teste#^ct-b04|CT-B04]].
- **Pré-condições:** Conjunto anterior íntegro com hashes conhecidos; escrita e cópia em dublês podem falhar individualmente.
- **Ação:** injetar cada erro durante geração ou transporte sintético.
- **Resultado:** retorna falha sem promover conjunto parcial nem modificar arquivos e hashes anteriores.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B05 — Interrupção e retomada

- **Origem:** [[02 - Casos de teste#^ct-b05|CT-B05]].
- **Pré-condições:** Conjunto anterior íntegro e saída parcial em fixture exclusiva.
- **Ação:** interromper antes da conclusão e repetir.
- **Resultado:** parcial não é marcado completo; anterior permanece byte a byte íntegro.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B06 — Limites e isolamento

- **Origem:** [[02 - Casos de teste#^ct-b06|CT-B06]].
- **Pré-condições:** Interceptadores Docker/curl/ssh/scp e arquivos sintéticos em destino exclusivo.
- **Ação:** verificar guardas antes de cada comando e executar cenários.
- **Resultado:** nenhum binário ou serviço real é acionado e relatório distingue associação local de consistência temporal/restore real.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B07 — Caminhos inseguros e tamanho divergente

- **Origem:** [[02 - Casos de teste#^ct-b07|CT-B07]].
- **Pré-condições:** Fixtures de referências relativas, caminho absoluto, travessia, link e tamanho divergente.
- **Ação:** reconciliar referências e anexos extraídos.
- **Resultado:** caminhos inseguros, links ou tamanho divergente são recusados; nenhum arquivo fora da fixture é lido.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B08 — Arquivos órfãos são relatados

- **Origem:** [[02 - Casos de teste#^ct-b08|CT-B08]].
- **Pré-condições:** Fixtures com referências íntegras e arquivo não referenciado.
- **Ação:** conciliar o conjunto sintético.
- **Resultado:** referências válidas são verificadas e órfãos são relatados sem presumir automaticamente que sejam perda ou rejeitar o conjunto por sua mera existência.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

## Checklist de envio

Qase externo fora do escopo; nenhum envio.
