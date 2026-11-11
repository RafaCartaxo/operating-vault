---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: 5
---

# Casos de teste — NXG-MEL-0009

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** será criada pelo DEV após encaminhamento da Coordenação.

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam na demanda; esta nota concentra os cenários executáveis.

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]], [[03 - Casos de teste#^ct-002\|CT-002]], [[03 - Casos de teste#^ct-003\|CT-003]], [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-003\|CT-003]], [[03 - Casos de teste#^ct-004\|CT-004]], [[03 - Casos de teste#^ct-006\|CT-006]], [[03 - Casos de teste#^ct-007\|CT-007]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-004\|CT-004]], [[03 - Casos de teste#^ct-005\|CT-005]], [[03 - Casos de teste#^ct-014\|CT-014]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-008\|CT-008]], [[03 - Casos de teste#^ct-009\|CT-009]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-009\|CT-009]], [[03 - Casos de teste#^ct-010\|CT-010]], [[03 - Casos de teste#^ct-014\|CT-014]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-001\|CT-001]], [[03 - Casos de teste#^ct-011\|CT-011]], [[03 - Casos de teste#^ct-012\|CT-012]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-012\|CT-012]], [[03 - Casos de teste#^ct-014\|CT-014]] |
| [[01 - Demanda#^c8\|C8]] | [[03 - Casos de teste#^ct-007\|CT-007]], [[03 - Casos de teste#^ct-013\|CT-013]] |

> [!example]- CT-001 · Conjunto completo de banco e anexos
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Conjunto completo de banco e anexos.
>
> **Pré-condições:**
> - Banco e anexos sintéticos associados a identificador de execução; dublês isolados.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Banco e anexos sintéticos associados a identificador de execução; dublês isolados.
> **Quando** o backup é solicitado
> **Então** o conjunto reúne banco, anexos e metadados íntegros, sem segredo e com resultado explícito.
>
> **Resultado esperado:** o conjunto reúne banco, anexos e metadados íntegros, sem segredo e com resultado explícito.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-001


> [!example]- CT-002 · Nenhum anexo legítimo versus erro de acesso
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Nenhum anexo legítimo versus erro de acesso.
>
> **Pré-condições:**
> - Uma fixture prova diretório vazio; outra simula permissão negada ou diretório inacessível.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Uma fixture prova diretório vazio; outra simula permissão negada ou diretório inacessível.
> **Quando** cada cenário é avaliado
> **Então** vazio é registrado como estado comprovado e erro recusa sucesso; nunca substitui falha por tar vazio.
>
> **Resultado esperado:** vazio é registrado como estado comprovado e erro recusa sucesso; nunca substitui falha por tar vazio.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-002


> [!example]- CT-003 · Falhas em dump, cópia, arquivo de anexos e verificação
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Falhas em dump, cópia, arquivo de anexos e verificação.
>
> **Pré-condições:**
> - Um backup íntegro anterior e dublês que falham individualmente em dump, cópia, tar e verificação.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Um backup íntegro anterior e dublês que falham individualmente em dump, cópia, tar e verificação.
> **Quando** cada falha é injetada
> **Então** processo reporta erro sem alegar conjunto completo ou permitir promoção e o conjunto anterior permanece intacto.
>
> **Resultado esperado:** processo reporta erro sem alegar conjunto completo ou permitir promoção e o conjunto anterior permanece intacto.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-003


> [!example]- CT-004 · Corrupção e conjuntos misturados
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Corrupção e conjuntos misturados.
>
> **Pré-condições:**
> - Dump, arquivo de anexos e metadados sintéticos incluindo versões corrompidas e de execuções diferentes.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Dump, arquivo de anexos e metadados sintéticos incluindo versões corrompidas e de execuções diferentes.
> **Quando** integridade e associação são avaliadas
> **Então** corrupção, ausência ou combinação de execuções diferentes impede sucesso e restauração.
>
> **Resultado esperado:** corrupção, ausência ou combinação de execuções diferentes impede sucesso e restauração.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c2|C2]], [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-004


> [!example]- CT-005 · Ensaio isolado de restauração e conteúdo
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Ensaio isolado de restauração e conteúdo.
>
> **Pré-condições:**
> - Fixtures exclusivas com registros identificáveis e anexos com hashes, e destino temporário comprovadamente isolado.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Fixtures exclusivas com registros identificáveis e anexos com hashes, e destino temporário comprovadamente isolado.
> **Quando** ensaio de restore sintético é executado
> **Então** conteúdos e associações esperados são comparados; resultado identifica dublê e não afirma restore real PostgreSQL.
>
> **Resultado esperado:** conteúdos e associações esperados são comparados; resultado identifica dublê e não afirma restore real PostgreSQL.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-005


> [!example]- CT-006 · Colisão e falha parcial preservam conjunto anterior
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Colisão e falha parcial preservam conjunto anterior.
>
> **Pré-condições:**
> - Conjunto anterior com hashes conhecidos e duas tentativas com mesmo identificador ou interrupção na escrita.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Conjunto anterior com hashes conhecidos e duas tentativas com mesmo identificador ou interrupção na escrita.
> **Quando** ocorrem colisão e interrupção em cada etapa de publicação
> **Então** nenhum conjunto anterior é sobrescrito nem apagado e estado parcial não é rotulado completo.
>
> **Resultado esperado:** nenhum conjunto anterior é sobrescrito nem apagado e estado parcial não é rotulado completo.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-006


> [!example]- CT-007 · Concorrência entre backup, deploy e rollback
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Concorrência entre backup, deploy e rollback.
>
> **Pré-condições:**
> - Dublês controlam lock e registram efeitos sem Docker ou rede.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Dublês controlam lock e registram efeitos sem Docker ou rede.
> **Quando** operações concorrentes tentam atuar no mesmo conjunto/checkout
> **Então** uma aguarda ou falha antes de conflito; falha não libera promoção e outros trabalhos permanecem intactos.
>
> **Resultado esperado:** uma aguarda ou falha antes de conflito; falha não libera promoção e outros trabalhos permanecem intactos.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]], [[01 - Demanda#^c8|C8]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-007


> [!example]- CT-008 · Imagem anterior ausente ou ameaçada por prune
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Imagem anterior ausente ou ameaçada por prune.
>
> **Pré-condições:**
> - Inventário sintético com imagem anterior presente, ausente e ameaçada por limpeza.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Inventário sintético com imagem anterior presente, ausente e ameaçada por limpeza.
> **Quando** precondições de promoção e rollback são avaliadas
> **Então** somente imagem identificada e preservada permite prosseguir; ausência ou preservação não comprovada bloqueia operação pertinente.
>
> **Resultado esperado:** somente imagem identificada e preservada permite prosseguir; ausência ou preservação não comprovada bloqueia operação pertinente.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-008


> [!example]- CT-009 · Schema e mounts incompatíveis
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Schema e mounts incompatíveis.
>
> **Pré-condições:**
> - Metadados sintéticos de revisão e configurações, incluindo migração incompatível e bind mount ausente.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Metadados sintéticos de revisão e configurações, incluindo migração incompatível e bind mount ausente.
> **Quando** compatibilidade é avaliada
> **Então** incompatibilidade ou informação ausente interrompe rollback do serviço com motivo e sem aplicar mudanças.
>
> **Resultado esperado:** incompatibilidade ou informação ausente interrompe rollback do serviço com motivo e sem aplicar mudanças.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]], [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-009


> [!example]- CT-010 · Escolha explícita: aplicação ou dados
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Escolha explícita: aplicação ou dados.
>
> **Pré-condições:**
> - Procedimento documentado com dois cenários sintéticos e impacto de perda de dados identificável.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Procedimento documentado com dois cenários sintéticos e impacto de perda de dados identificável.
> **Quando** operador escolhe estratégia no ensaio
> **Então** cada caminho exige decisão explícita e autorização operacional correspondente e nunca restaura dados automaticamente.
>
> **Resultado esperado:** cada caminho exige decisão explícita e autorização operacional correspondente e nunca restaura dados automaticamente.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-010


> [!example]- CT-011 · Health falho ou estado ambíguo
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Health falho ou estado ambíguo.
>
> **Pré-condições:**
> - Dublês retornam health negativo, timeout, dados ausentes e sucesso.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Dublês retornam health negativo, timeout, dados ausentes e sucesso.
> **Quando** sequência de retorno é avaliada
> **Então** falha/ambiguidade impede declarar recuperação bem-sucedida; sucesso exige integridade e health verificados.
>
> **Resultado esperado:** falha/ambiguidade impede declarar recuperação bem-sucedida; sucesso exige integridade e health verificados.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-011


> [!example]- CT-012 · Checklist operacional e ausência de segredos
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Checklist operacional e ausência de segredos.
>
> **Pré-condições:**
> - Runbook e evidências sintéticas com marcador de segredo fictício e configurações sem valores reais.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Runbook e evidências sintéticas com marcador de segredo fictício e configurações sem valores reais.
> **Quando** checklist e logs são inspecionados
> **Então** todos os itens de C7 têm responsável/evidência; marcador e conteúdo de env não aparecem em logs ou artefatos.
>
> **Resultado esperado:** todos os itens de C7 têm responsável/evidência; marcador e conteúdo de env não aparecem em logs ou artefatos.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]], [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-012


> [!example]- CT-013 · Regressão dos gates NXG-031
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Regressão dos gates NXG-031.
>
> **Pré-condições:**
> - Suíte de transição NXG-031 e dublês de Git, Docker e serviços, sem recursos reais.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Suíte de transição NXG-031 e dublês de Git, Docker e serviços, sem recursos reais.
> **Quando** regressão local é executada
> **Então** SHA, staging, lock, preservação de env e backup obrigatório continuam protegidos.
>
> **Resultado esperado:** SHA, staging, lock, preservação de env e backup obrigatório continuam protegidos.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c8|C8]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-013


> [!example]- CT-014 · Restauração real permanece pendente
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** Restauração real permanece pendente.
>
> **Pré-condições:**
> - Relatório exclusivamente sintético; sem Docker/PG real e sem dados reais nesta entrega.
> - ambiente isolado; apenas fixtures/dublês sob diretório de teste dedicado; sem Docker/volumes/redes, SSH, serviços ou dados reais.
>
> **Dado** Relatório exclusivamente sintético; sem Docker/PG real e sem dados reais nesta entrega.
> **Quando** parecer e checklist são preparados
> **Então** resultado local não declara recuperabilidade real nem go de produção; teste real e autorização específica permanecem pendentes.
>
> **Resultado esperado:** resultado local não declara recuperabilidade real nem go de produção; teste real e autorização específica permanecem pendentes.
>
> **Pós-condição:** Fixtures conferidas e removidas pelo responsável; nenhuma alteração em recursos reais.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]], [[01 - Demanda#^c5|C5]], [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** infra / documentação  
> **Automação:** ambos  
> **Execução:** planejado

^ct-014

