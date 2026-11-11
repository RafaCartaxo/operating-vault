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
# Preparação Qase — NXG-034

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

### CT-B01 — Transferência falha

- **Origem:** [[02 - Casos de teste#^ct-b01|CT-B01]].
- **Pré-condições:** SSH e SCP dublados, com SSH bem-sucedido e SCP falho, destino vazio e guardas verificadas.
- **Ação:** executar fluxo de cópia em fixture.
- **Resultado:** retorna erro e não anuncia sucesso com zero arquivos.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B02 — Nenhum conjunto disponível

- **Origem:** [[02 - Casos de teste#^ct-b02|CT-B02]].
- **Pré-condições:** Origem sintética sem conjuntos completos e dublês de transporte.
- **Ação:** solicitar cópia.
- **Resultado:** retorna falha explícita sem criar falsa evidência off-site.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B03 — Conjunto completo válido

- **Origem:** [[02 - Casos de teste#^ct-b03|CT-B03]].
- **Pré-condições:** Origem sintética com banco, anexos, metadados, manifesto e conclusão compatíveis; destino isolado.
- **Ação:** executar transporte dublado e conferir hashes.
- **Resultado:** todos os componentes e ID correspondem, sucesso só após verificação; nenhuma conexão real.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B04 — Conjunto parcial ou corrompido

- **Origem:** [[02 - Casos de teste#^ct-b04|CT-B04]].
- **Pré-condições:** Fixtures com arquivo ausente, hash divergente e ID trocado, mais cópia anterior válida.
- **Ação:** avaliar cada condição.
- **Resultado:** nenhuma é publicada como sucesso e cópia anterior permanece intacta.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B05 — Colisão ou erro de escrita

- **Origem:** [[02 - Casos de teste#^ct-b05|CT-B05]].
- **Pré-condições:** Destino sintético contém conjunto anterior e dublê falha escrita/cópia.
- **Ação:** executar cada falha.
- **Resultado:** fluxo interrompe, não sobrescreve a cópia anterior e não registra sucesso.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B06 — Documentação e isolamento

- **Origem:** [[02 - Casos de teste#^ct-b06|CT-B06]].
- **Pré-condições:** Guia 08, runbook 09 e guardas de chamadas reais previamente conferidos.
- **Ação:** revisar instruções e exercitar dublês.
- **Resultado:** instruções são coerentes com formato de conjunto ou declaram explicitamente ausência de solução; nenhum SSH/SCP/Docker real.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B07 — Espaços em caminhos e chave sintética

- **Origem:** [[02 - Casos de teste#^ct-b07|CT-B07]].
- **Pré-condições:** Diretórios e caminho de chave fictícia com espaços; SSH/SCP dublados e guardas verificadas.
- **Ação:** copiar conjunto válido por argumentos estruturados.
- **Resultado:** a fixture completa chega ao destino correto sem interpretar caminho como comando ou acionar rede real.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B08 — Interrupção, destino inacessível e origem inválida

- **Origem:** [[02 - Casos de teste#^ct-b08|CT-B08]].
- **Pré-condições:** Fixtures de interrupção, destino inacessível e ID de origem inválido com conjunto anterior preservado.
- **Ação:** exercitar cada falha com dublês.
- **Resultado:** a cópia falha fechada, não publica sucesso e mantém o anterior íntegro.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

## Checklist de envio

Qase externo fora do escopo; nenhum envio.
