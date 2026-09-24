---
prioridade: alta
tipo: melhoria
modulo: cliente
plano: "PLAN-089 — docs/plans/PLAN-089-cliente-cep-localizacao-aproximada.md"
execucao: "[[05 Arquivo/Nxgest/Melhorias/MEL-0001/DEV/MEL-0001/00 README|MEL-0001 — execução]]"
ambiente: dev
origem: observado
projeto: nxgest
pai: ""
data_inicio: "2026-08-29"
data_fim: ""
responsavel: ""
pontos_alocados: ""
---
# MEL-0001 — Cliente: CEP e localização aproximada do endereço

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Informações
> - **Tipo:** Melhoria
> - **Responsável:**
> - **Plano relacionado:** a definir quando a melhoria estiver pronta para implementação

> [!info] Status atual
> O status geral e a etapa atual são controlados no [[00 README|README da MEL-0001]].  
> **Próximo passo:** executar os CTs restantes na [[04 - Validação dev|validação QA]].

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo
> Preencha apenas `pontos_alocados` no frontmatter com a capacidade reservada para esta melhoria. O esforço dos artefatos é somado automaticamente quando receber pontos.

---

## Problema / contexto

Preencher manualmente o endereço de um cliente consome tempo e, muitas vezes, o operador ainda precisa ir ao local para obter uma referência de navegação. Isso é especialmente custoso para o endereço do comércio, que é o destino prioritário das cobranças.

## Objetivo

Permitir informar o CEP nos endereços do cliente para preencher seus dados automaticamente e, quando possível, criar uma localização **aproximada** que ajude na navegação. O cadastro continua possível mesmo sem CEP, consulta externa ou localização.

## Decisões de produto

- CEP é opcional nos endereços pessoal e do comércio; não bloqueia criar, editar ou salvar o cliente.
- O endereço do comércio continua sendo o alvo prioritário de navegação; o endereço pessoal é o fallback já existente.
- Coordenadas obtidas a partir de CEP representam uma **aproximação da região**, não uma captura de GPS e não uma localização exata do imóvel.
- A interface deve identificar essa origem como “localização aproximada pelo CEP”; não pode exibir “GPS capturado”.
- A captura manual de GPS permanece disponível para obter maior precisão.
- Quando houver GPS manual, ele tem prioridade sobre a localização aproximada pelo CEP.
- Informar ou alterar o CEP não sobrescreve o GPS manual já capturado; apenas atualiza a localização aproximada derivada do CEP.
- A interface usa um indicador curto para diferenciar `GPS` de `CEP aprox.`.
- Ao tentar salvar com CEP inválido, a interface oferece `Corrigir` ou `Salvar sem CEP`; confirmar a segunda opção remove o CEP e salva o restante do cadastro.
- O endereço pessoal continua opcional e fica recolhido inicialmente em criar e editar; o endereço do comércio continua expandido.

## Escopo

- Adicionar CEP ao endereço pessoal e ao endereço do comércio.
- Ao concluir um CEP válido, consultar um serviço de CEP e preencher os dados disponíveis de logradouro, bairro, cidade e UF.
- Derivar coordenadas aproximadas para o mesmo bloco de endereço, quando o geocoding encontrar resultado.
- Persistir CEP, devolvê-lo na API e mostrá-lo novamente na edição.
- Permitir que localização aproximada válida seja usada pela navegação, respeitando a prioridade comércio → pessoal.
- Mostrar mensagem compreensível para consulta inválida, não encontrada ou indisponível.

## Fora de escopo

- Tornar CEP obrigatório ou validar que ele corresponde ao número do imóvel.
- Preencher ou alterar número e complemento automaticamente.
- Garantir localização exata de porta, rota ou imóvel.
- Alterar a prioridade de navegação comércio → pessoal.
- Criar histórico/auditoria específico de consultas de CEP.
- Remover a captura manual de GPS ou impedir preenchimento manual do endereço.

## Regras do negócio

| Situação | Comportamento esperado |
|---|---|
| Formato | Interface mascara como `00000-000`; armazenamento e API usam os 8 dígitos sem formatação. |
| Consulta | Inicia somente com 8 dígitos; respostas de CEP anterior não podem sobrescrever o CEP atualmente digitado. |
| Preenchimento | Atualiza somente logradouro, bairro, cidade e UF que vierem da consulta; número e complemento nunca são alterados. |
| CEP inválido, inexistente ou serviço indisponível | Exibe mensagem de confirmação com as opções `Corrigir` ou `Salvar sem CEP`; nunca apaga textos preenchidos manualmente. |
| CEP alterado ou limpo | Invalida somente a localização aproximada derivada do CEP; o GPS manual permanece disponível. |
| Texto do endereço alterado | Mantém a regra existente: editar logradouro, bairro, cidade, UF ou complemento invalida as coordenadas; editar somente número não invalida. |
| Geocoding sem resultado | Mantém o endereço preenchido e informa que a localização aproximada não foi encontrada; GPS manual segue disponível. |
| Coordenadas derivadas | São associadas ao mesmo bloco de endereço do CEP, marcadas como aproximadas e não substituem o GPS manual. |
| Navegação | Prioriza GPS manual; sem GPS, usa a localização aproximada do comércio e depois a do endereço pessoal. |

## Critérios de aceite

- C1. Os dois blocos de endereço têm campo CEP com máscara `00000-000`. ^c1
- C2. CEP válido preenche os dados de endereço disponíveis, sem alterar número ou complemento. ^c2
- C3. CEP é opcional: cliente salva sem CEP e o preenchimento manual continua possível. ^c3
- C4. CEP inválido, inexistente ou serviço indisponível mostra confirmação para corrigir ou salvar sem CEP, sem bloquear o restante do cadastro. ^c4
- C5. CEP e endereço preenchidos manualmente persistem e voltam preenchidos na edição e na API. ^c5
- C6. Localização derivada por CEP é exibida como aproximada, nunca como GPS capturado, usando o indicador curto definido. ^c6
- C7. CEP alterado/limpo ou texto relevante do endereço editado invalida somente a localização aproximada daquele bloco; GPS manual e alteração apenas do número permanecem válidos. ^c7
- C8. A navegação prioriza GPS manual e, na ausência dele, usa a localização aproximada do comércio e depois a pessoal. ^c8
- C9. O endereço pessoal fica recolhido inicialmente em criação e edição, sem perder dados já existentes ao expandir. ^c9
- C10. O fluxo e a captura manual de GPS existentes permanecem funcionais. ^c10
- C11. Ao remover um CEP já salvo e salvar a edição, o CEP e a localização aproximada derivada são removidos. ^c11

## Pendências de decisão

- Nenhuma de produto. A escolha do provedor e da arquitetura de consulta pertence ao PLAN, desde que mantenha estas regras.

## Pacote QA

Os cenários executáveis ficam em [[03 - Casos de teste|03 - Casos de teste]]. O plano e o registro da validação são criados conforme a demanda avança.

## Notas técnicas para o PLAN

- Persistir `cep` e `comercio_cep` no banco, expondo-os como `endereco.cep` e `enderecoComercio.cep` no contrato da API.
- Propagar os campos por entity, use cases, repositório, controllers e schema/formulário do frontend; atualizar documentação e smoke de API conforme a matriz de propagação do repositório.
- A consulta externa deve ter timeout, debounce e proteção contra respostas fora de ordem; ViaCEP com fallback é uma opção, não uma regra de produto.
- Geocoding deve usar uma integração compatível com a política do provedor. Se for Nominatim, não depender de definir `User-Agent` pelo navegador; usar um gateway/backend quando necessário e respeitar o limite do serviço.
- Evoluir `GpsControl` e o estado/origem da localização para distinguir GPS capturado de coordenadas aproximadas por CEP, inclusive ao reabrir uma edição.
- Cobrir o comportamento com testes unitários/UI para máscara, consultas, invalidação e origem, além dos cenários de API.

## Bugs filhos

- [[05 Arquivo/Nxgest/Bugs/NXG-003/QA/NXG-003 Endereço pessoal inicia aberto/01 - Bug|NXG-003 — Endereço pessoal inicia aberto]] — originado pela reprovação do CT-008.
- [[05 Arquivo/Nxgest/Bugs/NXG-004/QA/NXG-004 CEP preenchido não permite salvar/01 - Bug|NXG-004 — CEP preenchido não permite salvar]] — originado pela reprovação do CT-001.
- [[05 Arquivo/Nxgest/Bugs/NXG-005/QA/NXG-005 Remover CEP salvo/01 - Bug|NXG-005 — Remover CEP salvo não limpa o cadastro]] — originado pela reprovação do CT-010.
- [[05 Arquivo/Nxgest/Bugs/NXG-006/QA/NXG-006 CEP inválido não exibe mensagem/01 - Bug|NXG-006 — CEP inválido não exibe mensagem]] — originado pela reprovação do CT-003.
