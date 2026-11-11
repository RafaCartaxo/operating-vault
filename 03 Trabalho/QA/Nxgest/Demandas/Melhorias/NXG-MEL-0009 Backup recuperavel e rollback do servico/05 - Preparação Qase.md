---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: melhoria
projeto: nxgest
modulo: infra
qase_projeto: nxgest
qase_suite_id: ""
casos_origem: ""
validacao_origem: ""
---
# Preparação Qase — NXG-MEL-0009

> **Posição no pacote:** melhoria → `05 - Preparação Qase.md`; bug → `04 - Preparação Qase.md`. O conteúdo deste modelo é o mesmo nos dois casos.

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Casos de teste (melhoria):** [[03 - Casos de teste]]  
> **Validação (melhoria):** [[04 - Validação dev]]  

Esta nota transforma os CTs refinados do vault em casos da Qase. Não crie CT novo aqui: apenas traduza o caso existente para os campos da API.

## Configuração

- **Projeto Qase:** não configurado; envio fora de escopo
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

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: usar o ID da demanda e o módulo (`NXG-MEL-0009`, `cliente`); não criar uma tag para cada CT, pois o título e o ID do caso já fazem essa identificação.


## Casos preparados

### CT-001 — Conjunto completo de banco e anexos

- **Origem:** [[03 - Casos de teste#^ct-001|CT-001]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Banco e anexos sintéticos associados a identificador de execução; dublês isolados.
- **Passo — ação:** o backup é solicitado.
- **Resultado esperado:** o conjunto reúne banco, anexos e metadados íntegros, sem segredo e com resultado explícito.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-002 — Nenhum anexo legítimo versus erro de acesso

- **Origem:** [[03 - Casos de teste#^ct-002|CT-002]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Uma fixture prova diretório vazio; outra simula permissão negada ou diretório inacessível.
- **Passo — ação:** cada cenário é avaliado.
- **Resultado esperado:** vazio é registrado como estado comprovado e erro recusa sucesso; nunca substitui falha por tar vazio.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-003 — Falhas em dump, cópia, arquivo de anexos e verificação

- **Origem:** [[03 - Casos de teste#^ct-003|CT-003]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Um backup íntegro anterior e dublês que falham individualmente em dump, cópia, tar e verificação.
- **Passo — ação:** cada falha é injetada.
- **Resultado esperado:** processo reporta erro sem alegar conjunto completo ou permitir promoção e o conjunto anterior permanece intacto.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-004 — Corrupção e conjuntos misturados

- **Origem:** [[03 - Casos de teste#^ct-004|CT-004]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Dump, arquivo de anexos e metadados sintéticos incluindo versões corrompidas e de execuções diferentes.
- **Passo — ação:** integridade e associação são avaliadas.
- **Resultado esperado:** corrupção, ausência ou combinação de execuções diferentes impede sucesso e restauração.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-005 — Ensaio isolado de restauração e conteúdo

- **Origem:** [[03 - Casos de teste#^ct-005|CT-005]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Fixtures exclusivas com registros identificáveis e anexos com hashes, e destino temporário comprovadamente isolado.
- **Passo — ação:** ensaio de restore sintético é executado.
- **Resultado esperado:** conteúdos e associações esperados são comparados; resultado identifica dublê e não afirma restore real PostgreSQL.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-006 — Colisão e falha parcial preservam conjunto anterior

- **Origem:** [[03 - Casos de teste#^ct-006|CT-006]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Conjunto anterior com hashes conhecidos e duas tentativas com mesmo identificador ou interrupção na escrita.
- **Passo — ação:** ocorrem colisão e interrupção em cada etapa de publicação.
- **Resultado esperado:** nenhum conjunto anterior é sobrescrito nem apagado e estado parcial não é rotulado completo.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-007 — Concorrência entre backup, deploy e rollback

- **Origem:** [[03 - Casos de teste#^ct-007|CT-007]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Dublês controlam lock e registram efeitos sem Docker ou rede.
- **Passo — ação:** operações concorrentes tentam atuar no mesmo conjunto/checkout.
- **Resultado esperado:** uma aguarda ou falha antes de conflito; falha não libera promoção e outros trabalhos permanecem intactos.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-008 — Imagem anterior ausente ou ameaçada por prune

- **Origem:** [[03 - Casos de teste#^ct-008|CT-008]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Inventário sintético com imagem anterior presente, ausente e ameaçada por limpeza.
- **Passo — ação:** precondições de promoção e rollback são avaliadas.
- **Resultado esperado:** somente imagem identificada e preservada permite prosseguir; ausência ou preservação não comprovada bloqueia operação pertinente.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-009 — Schema e mounts incompatíveis

- **Origem:** [[03 - Casos de teste#^ct-009|CT-009]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Metadados sintéticos de revisão e configurações, incluindo migração incompatível e bind mount ausente.
- **Passo — ação:** compatibilidade é avaliada.
- **Resultado esperado:** incompatibilidade ou informação ausente interrompe rollback do serviço com motivo e sem aplicar mudanças.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-010 — Escolha explícita: aplicação ou dados

- **Origem:** [[03 - Casos de teste#^ct-010|CT-010]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Procedimento documentado com dois cenários sintéticos e impacto de perda de dados identificável.
- **Passo — ação:** operador escolhe estratégia no ensaio.
- **Resultado esperado:** cada caminho exige decisão explícita e autorização operacional correspondente e nunca restaura dados automaticamente.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-011 — Health falho ou estado ambíguo

- **Origem:** [[03 - Casos de teste#^ct-011|CT-011]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Dublês retornam health negativo, timeout, dados ausentes e sucesso.
- **Passo — ação:** sequência de retorno é avaliada.
- **Resultado esperado:** falha/ambiguidade impede declarar recuperação bem-sucedida; sucesso exige integridade e health verificados.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-012 — Checklist operacional e ausência de segredos

- **Origem:** [[03 - Casos de teste#^ct-012|CT-012]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Runbook e evidências sintéticas com marcador de segredo fictício e configurações sem valores reais.
- **Passo — ação:** checklist e logs são inspecionados.
- **Resultado esperado:** todos os itens de C7 têm responsável/evidência; marcador e conteúdo de env não aparecem em logs ou artefatos.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-013 — Regressão dos gates NXG-031

- **Origem:** [[03 - Casos de teste#^ct-013|CT-013]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Suíte de transição NXG-031 e dublês de Git, Docker e serviços, sem recursos reais.
- **Passo — ação:** regressão local é executada.
- **Resultado esperado:** SHA, staging, lock, preservação de env e backup obrigatório continuam protegidos.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

### CT-014 — Restauração real permanece pendente

- **Origem:** [[03 - Casos de teste#^ct-014|CT-014]]; projeto/suite externos não configurados; não enviado.
- **Descrição/pré-condições:** Relatório exclusivamente sintético; sem Docker/PG real e sem dados reais nesta entrega.
- **Passo — ação:** parecer e checklist são preparados.
- **Resultado esperado:** resultado local não declara recuperabilidade real nem go de produção; teste real e autorização específica permanecem pendentes.
- **Pós-condição:** fixtures conferidas e removidas; recursos reais intactos.
- **Tipo/camada/automação:** regressão / infra / ambos.

## Checklist de envio

Envio externo não autorizado; apenas preparação local derivada dos CTs canônicos.
