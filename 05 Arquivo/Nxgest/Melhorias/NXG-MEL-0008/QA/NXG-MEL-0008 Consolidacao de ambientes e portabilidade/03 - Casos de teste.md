---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: "concluido"
pontos: 3
projeto: "nxgest"
epico: "NXG-EPIC-0001"
responsavel: "NX Gest · QA e Coordenação"
---

# Casos de teste — NXG-MEL-0008

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[05 Arquivo/Nxgest/Melhorias/NXG-MEL-0008/DEV/NXG-MEL-0008/00 README|Execução DEV]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam na demanda; esta nota concentra os cenários executáveis.

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-006\|CT-006]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-007\|CT-007]] |
| [[01 - Demanda#^c8\|C8]] | [[03 - Casos de teste#^ct-008\|CT-008]] |

> [!example]- CT-001 · Modelo unico completo
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
> **Descrição:** O único modelo versionado .env.example cobre as variáveis suportadas, com defaults de desenvolvimento e obrigações de staging/prod documentadas nos guias existentes. Nenhum segredo real é versionado.
>
> **Pré-condições:** um checkout com apenas arquivos versionados e valores sintéticos; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** um checkout com apenas arquivos versionados e valores sintéticos  
> **Quando** configuro os três cenários seguindo README, setup e runbook  
> **Então** as variáveis necessárias estão documentadas e os Compose resolvem sem depender de env real da máquina.
>
> **Resultado esperado:** as variáveis necessárias estão documentadas e os Compose resolvem sem depender de env real da máquina.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** executado

^ct-001

> [!example]- CT-002 · Onboarding coerente
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
> **Descrição:** README e guia de nova máquina usam caminhos reais e instalação pelo lockfile; infra/ aparece no mapa e não há comandos ativos dependentes da antiga localização dos arquivos.
>
> **Pré-condições:** documentação atualizada e ferramentas suportadas; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** documentação atualizada e ferramentas suportadas  
> **Quando** sigo o roteiro de instalação em checkout limpo  
> **Então** npm ci, configuração e inicialização seguem os comandos documentados sem arquivos herdados.
>
> **Resultado esperado:** npm ci, configuração e inicialização seguem os comandos documentados sem arquivos herdados.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** executado

^ct-002

> [!example]- CT-003 · Instancia de teste isolada
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
> **Descrição:** O plano de validação usa banco, portas, nomes de containers e volumes próprios, sem alterar recursos existentes.
>
> **Pré-condições:** a instalação original preservada e nomes/portas previamente inventariados; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** a instalação original preservada e nomes/portas previamente inventariados  
> **Quando** preparo e encerro a instância de validação  
> **Então** somente os recursos criados para a validação são usados e o ambiente original permanece íntegro.
>
> **Resultado esperado:** somente os recursos criados para a validação são usados e o ambiente original permanece íntegro.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** executado

^ct-003

> [!example]- CT-004 · Regressao integrada
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
> **Descrição:** Testes, build, check-dist e auditorias de documentação, links, UI, estilos e módulos passam; avisos históricos são classificados com encaminhamento.
>
> **Pré-condições:** a versão integrada candidata; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** a versão integrada candidata  
> **Quando** executo os gates definidos e reviso seus resultados  
> **Então** não há erro bloqueante e cada aviso aceito tem justificativa e responsável.
>
> **Resultado esperado:** não há erro bloqueante e cada aviso aceito tem justificativa e responsável.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** executado

^ct-004

> [!example]- CT-005 · Clone funcional
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
> **Descrição:** Um checkout limpo de revisão identificada instala dependências, inicializa banco vazio e permite autenticação e um fluxo básico de clientes; reiniciar preserva os dados de teste.
>
> **Pré-condições:** uma instância isolada nova e somente instruções versionadas; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** uma instância isolada nova e somente instruções versionadas  
> **Quando** instalo, inicio, autentico, crio e consulto um cliente e reinicio a aplicação  
> **Então** o fluxo funciona e o cliente permanece consultável após reinício.
>
> **Resultado esperado:** o fluxo funciona e o cliente permanece consultável após reinício.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** executado

^ct-005

> [!example]- CT-006 · Preservacao e commits
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
> **Descrição:** Todo trabalho local prévio é preservado e classificado por assunto, incluindo arquivos novos; commits locais são coerentes, sem push/deploy e sem incluir segredos.
>
> **Pré-condições:** inventário do estado 8454392 e cópia recuperável dos arquivos pendentes; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** inventário do estado 8454392 e cópia recuperável dos arquivos pendentes  
> **Quando** reviso os commits e comparo com o inventário  
> **Então** organização e trabalhos separados têm destino explícito e nenhuma alteração prévia foi descartada.
>
> **Resultado esperado:** organização e trabalhos separados têm destino explícito e nenhuma alteração prévia foi descartada.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** executado

^ct-006

> [!example]- CT-007 · Nomenclatura e continuidade
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
> **Descrição:** A pasta local final nxgest e as referências ativas de ferramentas ficam coerentes; caminhos históricos de infraestrutura real permanecem compatíveis.
>
> **Pré-condições:** referências e processos locais inventariados; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** referências e processos locais inventariados  
> **Quando** valido o checkout por caminho independente e organizo a instalação definitiva  
> **Então** o projeto funciona sem depender do antigo caminho local e não há mudança de VPS, volumes, redes ou domínios existentes.
>
> **Resultado esperado:** o projeto funciona sem depender do antigo caminho local e não há mudança de VPS, volumes, redes ou domínios existentes.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** executado

^ct-007

> [!example]- CT-008 · Governanca verificavel
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
> **Descrição:** NXG-028, épico e boards refletem a execução e suas evidências; o épico permanece em execução aguardando parecer final ao usuário.
>
> **Pré-condições:** resultados DEV e validação independente QA; ferramentas disponíveis e uso exclusivo de dados sintéticos.
>
> **Dado** resultados DEV e validação independente QA  
> **Quando** confiro frontmatter, links, boards, histórico e evidências  
> **Então** há uma cadeia consistente demanda-CT-resultado e o encerramento do épico não foi antecipado.
>
> **Resultado esperado:** há uma cadeia consistente demanda-CT-resultado e o encerramento do épico não foi antecipado.
>
> **Pós-condição:** trabalho original e recursos reais preservados; somente recursos próprios de teste podem ser limpos.
>
> **Critérios cobertos:** [[01 - Demanda#^c8|C8]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** manual  
> **Automação:** manual  
> **Execução:** executado

^ct-008
