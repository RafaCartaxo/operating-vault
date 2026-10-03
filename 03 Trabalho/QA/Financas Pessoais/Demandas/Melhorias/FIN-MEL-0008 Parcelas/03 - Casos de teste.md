---
demanda: FIN-MEL-0008
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — FIN-MEL-0008

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Execução DEV:** [[03 Trabalho/DEV/<projeto>/Execuções/<ID>/00 README|Execução DEV]]

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

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

> [!example]- CT-001 · Criar lançamento parcelado
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
> **Descrição:** confirma que o usuário consegue informar o total e a quantidade de parcelas.
>
> **Pré-condições:**
> - Aplicação e API disponíveis.
>
> **Dado** que informo uma despesa de R$ 1.000,00 em 10 parcelas  
> **Quando** salvo o lançamento  
> **Então** a série é criada com 10 parcelas.
>
> **Resultado esperado:** o fluxo aceita os campos e identifica a série.
>
> **Pós-condição:** registre como o sistema deve ficar depois do teste.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · Rejeitar quantidade inválida
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
> **Descrição:** confirma as validações de quantidade e valor para parcelamento.
>
> **Pré-condições:**
> - A melhoria está disponível no ambiente de teste.
>
> **Dado** que informo quantidade inválida, zero ou um valor menor que a quantidade de parcelas em centavos  
> **Quando** tento salvar  
> **Então** recebo validação e nenhuma parcela é criada.
>
> **Resultado esperado:** a entrada inválida é recusada sem persistência parcial.
>
> **Pós-condição:** nenhuma série inválida permanece persistida.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Informações do CT**  
> **Tipo:** validação  
> **Camada:** API/UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Distribuir o total em centavos
>
> **Descrição:** confirma que a soma das parcelas corresponde exatamente ao total informado.
>
> **Dado** que informo R$ 100,00 em 3 parcelas  
> **Quando** salvo  
> **Então** as parcelas somam R$ 100,00, com ajuste de centavos na última.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]

^ct-003

> [!example]- CT-004 · Gerar vencimentos mensais
>
> **Descrição:** confirma a geração mensal e o ajuste de datas no fim do mês.
>
> **Dado** que a primeira parcela vence no dia 31  
> **Quando** a série é gerada  
> **Então** meses menores usam o último dia válido do mês.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]

^ct-004

> [!example]- CT-005 · Criar série de forma atômica
>
> **Descrição:** confirma que uma falha não deixa parcelas incompletas.
>
> **Dado** que ocorre erro durante a persistência  
> **Quando** a operação termina  
> **Então** nenhuma parcela parcial fica gravada.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]

^ct-005

> [!example]- CT-006 · Exibir parcela no mês correto
>
> **Descrição:** confirma a identificação e consulta mensal de cada parcela.
>
> **Dado** que uma série foi criada  
> **Quando** consulto os meses correspondentes  
> **Então** cada parcela mostra sua posição e total.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]], [[01 - Demanda#^c5|C5]]

^ct-006

> [!example]- CT-007 · Manter lançamento simples
>
> **Descrição:** confirma que lançamentos sem parcelamento continuam iguais.
>
> **Dado** que salvo um lançamento comum  
> **Quando** consulto e edito o registro  
> **Então** o fluxo existente permanece funcionando sem parcelas.
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]

^ct-007

> [!example]- CT-008 · Editar e excluir a série inteira
>
> **Descrição:** confirma que as ações em uma parcela respeitam a regra de série.
>
> **Dado** que existe uma série com várias parcelas  
> **Quando** edito ou excluo uma parcela e confirmo a operação  
> **Então** todas as parcelas da série são atualizadas ou removidas.
>
> **Resultado esperado:** a série permanece consistente, sem parcelas órfãs.
>
> **Critérios cobertos:** [[01 - Demanda#^c8|C8]]

^ct-008
