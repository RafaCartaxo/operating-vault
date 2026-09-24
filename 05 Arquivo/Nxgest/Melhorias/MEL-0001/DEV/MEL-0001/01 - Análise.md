# 01 - Análise (MEL-0001)

> [!info]- Navegação QA/DEV
> **Execução:** [[00 README|README da execução]]  
> **Demanda QA:** [[05 Arquivo/Nxgest/Melhorias/MEL-0001/QA/MEL-0001 Cliente CEP/01 - Demanda|Demanda]]  
> **Plano técnico:** `docs/plans/PLAN-089-cliente-cep-localizacao-aproximada.md`

---

## Objetivo da análise

Definir a solução técnica para consulta de CEP, preenchimento do endereço, geocoding aproximado e prioridade do GPS manual.

---

## O que existe hoje

- O contrato `Address` não possui CEP; o banco também não possui colunas `cep`/`comercio_cep`.
- `ClienteForm` tem dois blocos de endereço, mas só captura GPS e preenche texto por reverse geocode.
- `useGeolocation` chama Nominatim diretamente, com timeout de 10 s do navegador; quando o reverse geocode falha, mantém apenas as coordenadas.
- O estado atual do GPS só diferencia `vazio`, `capturada` e `invalidada`; a origem não é persistida.
- Alterações relevantes no texto invalidam coordenadas no frontend; alterar somente o número é a exceção existente.
- `resolveAlvoCliente` já aplica a prioridade comércio → endereço principal e `montarAlvo` prioriza coordenadas sobre texto.

## Decisões técnicas

1. Adicionar `cep` ao endereço pessoal e `cep` ao endereço comercial no contrato público, entidade, banco, repositório, casos de uso e formulário.
2. Encapsular a consulta de CEP em um serviço próprio, com máscara apenas na UI, normalização para oito dígitos, debounce e cancelamento/identificação de resposta obsoleta.
3. Preencher somente logradouro, bairro, cidade e UF retornados; nunca substituir número ou complemento.
4. Manter o GPS manual como origem exata e prioritária. Coordenadas obtidas pelo CEP terão origem `cep_aproximado` e não poderão ser exibidas como “GPS capturado”.
5. Como o provedor de CEP não entrega coordenada confiável por si só, o geocoding aproximado deve ser uma etapa separada, atrás de uma função/adapter substituível. Falha nessa etapa não impede salvar o endereço.
6. Persistir a origem da localização junto às coordenadas (ou derivá-la de um campo explicitamente equivalente), para que a edição reabra o indicador correto. Não misturar coordenadas aproximadas com endereço de outro bloco.
7. Manter a navegação atual: comércio primeiro, depois endereço pessoal; dentro do bloco, GPS manual > localização aproximada pelo CEP > texto.
8. CEP inválido, inexistente ou serviço indisponível não bloqueia o cadastro: a UI oferece corrigir ou salvar sem CEP, removendo apenas o CEP inválido.

## Impactos e riscos

- Será necessária migração não destrutiva e atualização da documentação de API/smoke.
- O serviço externo exige timeout, tratamento de indisponibilidade e proteção contra respostas fora de ordem; não deve apagar dados digitados manualmente.
- A política de geocoding/Nominatim deve respeitar CSP, limites do provedor e, se necessário, passar por gateway backend em vez de depender de cabeçalhos do navegador.
- A origem da localização precisa ser coberta na edição, na navegação e nos testes de regressão do `ClienteForm`.

---

## Veredito

Há base reutilizável para GPS e navegação, mas a MEL-0001 não é apenas ajuste visual: exige evolução de contrato e persistência. A implementação deve começar pelo modelo/API e pelo adapter de CEP/geocoding, depois integrar os dois blocos do formulário e atualizar a navegação/indicadores. O detalhamento executável está em `docs/plans/PLAN-089-cliente-cep-localizacao-aproximada.md`.
