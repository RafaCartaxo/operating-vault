---
demanda: FIN-MEL-0001
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: 1
---

# Casos de teste — FIN-MEL-0001

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/Financas Pessoais/Execuções/FIN-MEL-0001/00 README|Execução DEV]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam na demanda; esta nota concentra os cenários executáveis.

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-001\|CT-001]], [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-005\|CT-005]] |

---

> [!example]- CT-001 · Salvar despesa com dados válidos
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
> **Descrição:** confirma que uma despesa válida pode ser enviada e concluída.
>
> **Pré-condições:**
> - Backend Go iniciado.
> - Usuário está na tela de nova despesa.
> - Campos tipo, descrição, valor e data estão disponíveis.
>
> **Dado** que os campos obrigatórios estão preenchidos com valores válidos  
> **Quando** o usuário envia o formulário  
> **Então** o frontend chama `POST /api/lancamentos` e mostra confirmação.
>
> **Resultado esperado:** lançamento persistido e formulário pronto para novo registro.
>
> **Pós-condição:** despesa criada no backend.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c3|C3]], [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · Impedir envio com dados inválidos
>
> **Descrição:** confirma que campos obrigatórios, valor e data inválidos bloqueiam o envio.
>
> **Pré-condições:** formulário de nova despesa aberto.
>
> **Dado** que existe campo obrigatório ausente ou inválido  
> **Quando** o usuário tenta enviar  
> **Então** o formulário não chama a API e mostra mensagens compreensíveis.
>
> **Resultado esperado:** usuário identifica e corrige os problemas antes do envio.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Informações do CT**  
> **Tipo:** funcional  
> **Camada:** E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Preservar dados quando a API falha
>
> **Descrição:** confirma o tratamento de erro sem perda dos dados preenchidos.
>
> **Pré-condições:** simular resposta de erro da API.
>
> **Dado** que os dados do formulário são válidos  
> **Quando** a API responde com erro  
> **Então** aparece uma mensagem, os dados permanecem e o usuário pode tentar novamente.
>
> **Resultado esperado:** falha comunicada sem apagar o formulário.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** E2E/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Manter contrato do backend
>
> **Descrição:** confirma que a integração preserva o contrato existente do backend Go.
>
> **Pré-condições:** dependências Go disponíveis e ambiente de testes configurado.
>
> **Dado** que a suíte automatizada do backend está disponível  
> **Quando** `go test ./...` é executado  
> **Então** os testes passam e o endpoint aceita o payload usado pelo frontend.
>
> **Resultado esperado:** nenhuma regressão no contrato ou na persistência.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]], [[01 - Demanda#^c6|C6]]
>
> **Informações do CT**  
> **Tipo:** regressão  
> **Camada:** API  
> **Automação:** automatizado  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Filtrar entrada monetária inválida
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
> **Descrição:** confirma que o campo de valor aceita somente números, separadores válidos e até duas casas decimais.
>
> **Pré-condições:** formulário de nova despesa aberto.
>
> **Dado** que o usuário digita letras, símbolos ou mais de duas casas no campo de valor  
> **Quando** o valor é editado  
> **Então** caracteres inválidos são removidos e a entrada permanece em formato monetário válido.
>
> **Resultado esperado:** o campo não aceita caracteres arbitrários e o valor convertido continua correto.
>
> **Pós-condição:** o formulário permanece pronto para envio com valor sanitizado.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/unit  
> **Automação:** ambos  
> **Execução:** aprovado

^ct-005

> [!example]- CT-006 · Exibir máscara monetária em tempo real
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
> **Descrição:** confirma que o valor é exibido sempre no formato monetário brasileiro.
>
> **Pré-condições:** formulário de nova despesa aberto.
>
> **Dado** que o usuário informa os dígitos `123456` ou cola `1.234,56`  
> **Quando** o campo é atualizado  
> **Então** a tela exibe `R$ 1.234,56` e o backend recebe `123456` centavos.
>
> **Resultado esperado:** o usuário visualiza o valor formatado durante a digitação sem alterar o valor enviado.
>
> **Pós-condição:** campo permanece pronto para envio com o valor canônico em centavos.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** usabilidade  
> **Camada:** UI/unit  
> **Automação:** ambos  
> **Execução:** planejado

^ct-006

> [!example]- CT-007 · Preservar posição do cursor ao editar
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
> **Descrição:** confirma que a máscara não reposiciona o cursor para o fim ao editar o valor.
>
> **Pré-condições:** campo de valor preenchido com um valor formatado.
>
> **Dado** que o cursor está no meio do valor  
> **Quando** o usuário apaga ou insere um dígito  
> **Então** o cursor permanece próximo à posição editada após a reformatação e nunca é deslocado para antes do prefixo `R$`.
>
> **Resultado esperado:** é possível corrigir o valor no meio da expressão sem precisar reposicionar o cursor manualmente.
>
> **Pós-condição:** valor permanece formatado e editável.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** usabilidade  
> **Camada:** UI/unit  
> **Automação:** ambos  
> **Execução:** planejado

^ct-007

> [!example]- CT-008 · Apresentar todos os erros obrigatórios de uma vez
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
> **Descrição:** confirma que o formulário informa todos os campos inválidos no mesmo envio.
>
> **Pré-condições:** formulário aberto; descrição, valor e data vazios ou inválidos.
>
> **Dado** que existem vários campos obrigatórios inválidos  
> **Quando** o usuário tenta salvar  
> **Então** todas as mensagens aparecem simultaneamente de cima para baixo, com foco no primeiro campo inválido.
>
> **Resultado esperado:** o usuário consegue corrigir todos os problemas sem submeter o formulário repetidamente.
>
> **Pós-condição:** cada mensagem desaparece quando seu respectivo campo é corrigido.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** validação  
> **Camada:** UI/unit  
> **Automação:** ambos  
> **Execução:** planejado

^ct-008
