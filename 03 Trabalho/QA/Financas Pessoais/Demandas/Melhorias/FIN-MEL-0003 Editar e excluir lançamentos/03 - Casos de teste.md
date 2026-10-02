---
demanda: FIN-MEL-0003
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: 1
---

# Casos de teste — FIN-MEL-0003

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0003/00 README|Execução DEV]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam na demanda; esta nota concentra os cenários executáveis.

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-003\|CT-003]], [[03 - Casos de teste#^ct-008\|CT-008]], [[03 - Casos de teste#^ct-012\|CT-012]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-006\|CT-006]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-007\|CT-007]] |

---

> [!example]- CT-001 · Exibir ações por lançamento
>
> **Descrição:** confirma que cada item apresenta editar e excluir.
>
> **Pré-condições:** mês com lançamentos persistidos.
>
> **Dado** que o usuário consulta um mês com registros  
> **Quando** a lista é exibida  
> **Então** cada item apresenta ações identificáveis e acessíveis.
>
> **Resultado esperado:** ações aparecem no item correto.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> **Informações do CT**  
> **Tipo:** funcional  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · Abrir edição preenchida
>
> **Descrição:** confirma que editar abre o formulário com os valores atuais.
>
> **Pré-condições:** existe um lançamento conhecido.
>
> **Dado** que o usuário toca em editar  
> **Quando** o formulário é aberto  
> **Então** descrição, tipo, valor e data correspondem ao lançamento selecionado.
>
> **Resultado esperado:** usuário consegue revisar os dados antes de alterar.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Informações do CT**  
> **Tipo:** funcional  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Persistir edição válida
>
> **Descrição:** confirma que uma edição válida atualiza o lançamento correto.
>
> **Pré-condições:** formulário de edição preenchido com dados válidos.
>
> **Dado** que o usuário altera um campo  
> **Quando** salva a edição  
> **Então** a API persiste a alteração e a lista apresenta os novos dados.
>
> **Resultado esperado:** somente o registro selecionado é alterado.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Informações do CT**  
> **Tipo:** funcional  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Cancelar exclusão
>
> **Descrição:** confirma que excluir exige confirmação explícita.
>
> **Pré-condições:** existe um lançamento conhecido.
>
> **Dado** que o usuário toca em excluir  
> **Quando** cancela a confirmação  
> **Então** o lançamento permanece na lista.
>
> **Resultado esperado:** cancelamento não altera dados.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Informações do CT**  
> **Tipo:** segurança funcional  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Excluir lançamento confirmado
>
> **Descrição:** confirma que o registro correto é excluído após confirmação.
>
> **Pré-condições:** existe um lançamento conhecido e identificável.
>
> **Dado** que o usuário confirma a exclusão  
> **Quando** a API conclui a operação  
> **Então** o registro desaparece e o total é atualizado.
>
> **Resultado esperado:** nenhum outro registro é removido.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]], [[01 - Demanda#^c4|C4]]
>
> **Informações do CT**  
> **Tipo:** funcional  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-005

> [!example]- CT-006 · Preservar tela quando a API falha
>
> **Descrição:** confirma que falha de edição ou exclusão não apaga dados visualmente.
>
> **Pré-condições:** simular erro da API.
>
> **Dado** que a API responde com erro  
> **Quando** a operação termina  
> **Então** a tela informa a falha e mantém os dados consistentes.
>
> **Resultado esperado:** usuário pode tentar novamente sem perder contexto.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> **Informações do CT**  
> **Tipo:** resiliência  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-006

> [!example]- CT-007 · Usar ações no celular e desktop
>
> **Descrição:** confirma que as ações permanecem acessíveis em diferentes larguras.
>
> **Pré-condições:** frontend disponível em viewport móvel e desktop.
>
> **Dado** que o usuário consulta a lista  
> **Quando** utiliza editar ou excluir  
> **Então** nenhum botão fica cortado ou inacessível.
>
> **Resultado esperado:** fluxo utilizável nos dois contextos.
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> **Informações do CT**  
> **Tipo:** usabilidade  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-007

> [!example]- CT-008 · Bloquear edição inválida
>
> **Descrição:** confirma que a edição reaproveita a validação do cadastro.
>
> **Pré-condições:** formulário de edição aberto.
>
> **Dado** que o usuário remove descrição, informa valor inválido ou data inválida  
> **Quando** tenta salvar  
> **Então** o envio é bloqueado e os erros são apresentados sem alterar o registro.
>
> **Resultado esperado:** registro original permanece intacto.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Informações do CT**  
> **Tipo:** validação  
> **Camada:** UI/E2E  
> **Automação:** ambos  
> **Execução:** planejado

^ct-008

> [!example]- CT-009 · Editar lançamento para outro mês
>
> **Descrição:** confirma que alterar a data reposiciona o registro no filtro mensal correto.
>
> **Pré-condições:** lançamento existente e dois meses consultáveis.
>
> **Dado** que o usuário altera a data para outro mês  
> **Quando** salva  
> **Então** o registro deixa de aparecer no mês antigo e aparece no novo mês.
>
> **Resultado esperado:** nenhuma duplicidade e totais consistentes nos dois meses.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]

^ct-009

> [!example]- CT-010 · Alterar tipo e total mensal
>
> **Descrição:** confirma que trocar despesa por receita recalcula o total.
>
> **Pré-condições:** mês com total de despesas conhecido.
>
> **Dado** que o usuário altera uma despesa para receita  
> **Quando** salva  
> **Então** o valor deixa de compor o total de despesas.
>
> **Resultado esperado:** lista e total refletem o novo tipo.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]

^ct-010

> [!example]- CT-011 · Tratar lançamento inexistente
>
> **Descrição:** confirma o tratamento de tentativa de editar ou excluir um ID inexistente.
>
> **Pré-condições:** simular resposta 404 ou registro removido previamente.
>
> **Dado** que a API não encontra o registro  
> **Quando** o usuário tenta editar ou excluir  
> **Então** a tela informa o erro e mantém a consulta consistente.
>
> **Resultado esperado:** nenhum outro lançamento é afetado.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]

^ct-011

> [!example]- CT-012 · Preservar contratos e regressões
>
> **Descrição:** confirma os contratos de atualização/exclusão e a permanência do cadastro e consulta mensal.
>
> **Pré-condições:** suíte backend e frontend disponível.
>
> **Dado** que os testes automatizados são executados  
> **Quando** a suíte termina  
> **Então** contratos, persistência, cadastro e consulta mensal continuam aprovados.
>
> **Resultado esperado:** nenhuma regressão nas capacidades anteriores.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]

^ct-012
