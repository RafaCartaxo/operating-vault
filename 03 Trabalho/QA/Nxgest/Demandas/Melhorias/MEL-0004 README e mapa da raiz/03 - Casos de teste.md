---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: 0
---

# Casos de teste — MEL-0004

> [!info]- Navegação QA
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Validação:** [[04 - Validação dev]]

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-004\|CT-004]] |

> [!example]- CT-001 · Estrutura oficial representada no README

```meta-bind-button
style: primary
label: ↩ Validação
action:
  type: open
  link: "[[04 - Validação dev#Resultado dos casos de teste]]"
```

## Cenário

**Descrição:** confirma que o README lista a estrutura real e oficial do repositório.

**Pré-condições:** README atualizado e árvore real do repositório disponível.

**Dado** o README e a listagem da raiz do repositório
**Quando** comparo os diretórios documentados com os diretórios existentes
**Então** os itens documentados existem e `.github/` e `.opencode/` estão representados.

**Resultado esperado:** a estrutura documentada corresponde ao estado real do lote.

**Pós-condição:** nenhuma alteração de código ou infraestrutura é introduzida.

**Critérios cobertos:** [[01 - Demanda#^c1|C1]]

**Informações do CT**
**Tipo:** funcional
**Camada:** manual
**Automação:** manual
**Execução:** planejado

^ct-001

> [!example]- CT-002 · Links documentais resolvem

```meta-bind-button
style: primary
label: ↩ Validação
action:
  type: open
  link: "[[04 - Validação dev#Resultado dos casos de teste]]"
```

## Cenário

**Descrição:** confirma que os links e caminhos afetados pelo README continuam válidos.

**Pré-condições:** README atualizado e auditoria documental disponível.

**Dado** o README revisado
**Quando** executo as auditorias de links e documentação previstas no repositório
**Então** não há referência quebrada causada pelo MEL-0004.

**Resultado esperado:** auditorias concluídas sem erro atribuível ao lote.

**Pós-condição:** documentação navegável.

**Critérios cobertos:** [[01 - Demanda#^c2|C2]]

**Informações do CT**
**Tipo:** regressão
**Camada:** manual
**Automação:** automatizado
**Execução:** planejado

^ct-002

> [!example]- CT-003 · Escopo documental preservado

```meta-bind-button
style: primary
label: ↩ Validação
action:
  type: open
  link: "[[04 - Validação dev#Resultado dos casos de teste]]"
```

## Cenário

**Descrição:** confirma que o lote não altera código, ambiente, Docker, agentes ou infraestrutura.

**Pré-condições:** estado Git inicial registrado.

**Dado** o diff do MEL-0004
**Quando** reviso os arquivos alterados
**Então** somente o README e registros autorizados do lote aparecem no escopo.

**Resultado esperado:** nenhuma alteração fora da documentação aprovada.

**Pós-condição:** demais áreas permanecem intactas.

**Critérios cobertos:** [[01 - Demanda#^c3|C3]]

**Informações do CT**
**Tipo:** regressão
**Camada:** manual
**Automação:** manual
**Execução:** planejado

^ct-003

> [!example]- CT-004 · Nomenclatura canônica preservada

```meta-bind-button
style: primary
label: ↩ Validação
action:
  type: open
  link: "[[04 - Validação dev#Resultado dos casos de teste]]"
```

## Cenário

**Descrição:** confirma que o texto novo usa `nxgest` e não transforma compatibilidade histórica em erro.

**Pré-condições:** README revisado e plano NXG-028 disponível.

**Dado** o conteúdo novo do README
**Quando** verifico nomes de produto, repositório e infraestrutura
**Então** referências novas usam `nxgest` e referências `nxgestao` permanecem justificadas.

**Resultado esperado:** nomenclatura coerente com o padrão oficial.

**Pós-condição:** nenhuma referência histórica é reescrita indevidamente.

**Critérios cobertos:** [[01 - Demanda#^c4|C4]]

**Informações do CT**
**Tipo:** funcional
**Camada:** manual
**Automação:** manual
**Execução:** planejado

^ct-004
