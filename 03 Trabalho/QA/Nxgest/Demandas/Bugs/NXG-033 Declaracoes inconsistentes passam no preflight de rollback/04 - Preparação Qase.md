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
# Preparação Qase — NXG-033

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

### CT-B01 — Schema incompatível ou ausente

- **Origem:** [[02 - Casos de teste#^ct-b01|CT-B01]].
- **Pré-condições:** Evidência sintética estruturada indica incompatível; variante omite prova ou responsável.
- **Ação:** validar precondições.
- **Resultado:** preflight recusa ou mantém no-go sem declarar compatibilidade comprovada.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B02 — Declaração e prova contraditórias

- **Origem:** [[02 - Casos de teste#^ct-b02|CT-B02]].
- **Pré-condições:** Declaração compatible e evidência estruturada de schema incompatível; hashes corretos.
- **Ação:** verificar coerência dos campos.
- **Resultado:** contradição explícita é detectada e bloqueia liberação; não se exige interpretar texto arbitrário como prova.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B03 — SHA e imagem anterior divergentes

- **Origem:** [[02 - Casos de teste#^ct-b03|CT-B03]].
- **Pré-condições:** Evidência sintética relaciona SHA A à imagem A; inventário dublado apresenta imagem B ou SHA sem vínculo.
- **Ação:** avaliar pré-condições.
- **Resultado:** divergência ou vínculo ausente impede prontidão; caminho positivo com mesmo SHA e imagem é verificável.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B04 — Configuração e mounts incompletos

- **Origem:** [[02 - Casos de teste#^ct-b04|CT-B04]].
- **Pré-condições:** Inventário e evidência sintéticos com mount ausente, digest divergente ou configuração indisponível.
- **Ação:** avaliar gate.
- **Resultado:** cada condição interrompe ou mantém no-go antes de qualquer operação de serviço.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B05 — Health, integridade e SHA no retorno

- **Origem:** [[02 - Casos de teste#^ct-b05|CT-B05]].
- **Pré-condições:** Respostas dubladas healthy, timeout e negativas; evidências sintéticas com dados ausentes e SHA divergente.
- **Ação:** avaliar separadamente os três componentes.
- **Resultado:** sem health positivo, integridade demonstrada e identidade de SHA comprovada, não declara recuperação bem-sucedida.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B06 — Revisão humana e isolamento

- **Origem:** [[02 - Casos de teste#^ct-b06|CT-B06]].
- **Pré-condições:** Evidências sem segredo e guardas Docker/curl/ssh/scp previamente verificadas.
- **Ação:** executar cenários e revisar documentação.
- **Resultado:** reporte diferencia validação mecânica de revisão humana e não afirma compatibilidade real; CLI/daemon e serviços reais não são chamados.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B07 — Proveniência ausente ou não verificável

- **Origem:** [[02 - Casos de teste#^ct-b07|CT-B07]].
- **Pré-condições:** Fonte de confiança dublada indisponível, revisão ausente ou evidência obsoleta.
- **Ação:** avaliar proveniência do SHA e identidade da imagem.
- **Resultado:** o gate mantém no-go sem inventar confiança, sem alegar autenticidade ou compatibilidade real.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

### CT-B08 — Retorno vinculado ao conjunto correto

- **Origem:** [[02 - Casos de teste#^ct-b08|CT-B08]].
- **Pré-condições:** Relatório sintético de integridade associado a bundle diferente e identidade do serviço dublada divergente.
- **Ação:** avaliar retorno e health positivo.
- **Resultado:** o vínculo incorreto ou identidade divergente impede sucesso apesar do health positivo.
- **Pós-condição:** fixtures removidas; infraestrutura real intacta.
- **Tipo/camada/automação:** regressão / infra / ambos. Não enviado.

## Checklist de envio

Qase externo fora do escopo; nenhum envio.
